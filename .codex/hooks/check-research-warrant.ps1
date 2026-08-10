# Stop hook: enforce source-tracing discipline for analytical output.
#
# Reads the Stop-hook JSON payload from stdin, inspects the just-completed
# assistant turn, and blocks the stop when analytical-framing markers are
# present without a source-fetch call in the same turn.
#
# Fires only on substantive analytical output (3+ distinct marker categories),
# not on conversations about the methodology. Exits 0 on any internal error
# so the hook can never break a session.

$ErrorActionPreference = 'Continue'

try {
    $raw = [Console]::In.ReadToEnd()
    if ([string]::IsNullOrWhiteSpace($raw)) { exit 0 }

    $payload = $raw | ConvertFrom-Json -ErrorAction Stop
    if ($payload.stop_hook_active -eq $true) { exit 0 }

    $tpath = [string]$payload.transcript_path
    if (-not $tpath -or -not (Test-Path -LiteralPath $tpath)) { exit 0 }

    $entries = @()
    foreach ($line in Get-Content -LiteralPath $tpath -Encoding UTF8) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        try { $entries += ($line | ConvertFrom-Json -ErrorAction Stop) } catch { continue }
    }
    if ($entries.Count -eq 0) { exit 0 }

    # Find the last real user prompt: type=user whose message.content is a
    # plain string, OR an array whose first block isn't a tool_result wrapper.
    $boundary = -1
    for ($i = $entries.Count - 1; $i -ge 0; $i--) {
        $e = $entries[$i]
        if ($e.type -ne 'user') { continue }
        $c = $e.message.content
        $isHumanPrompt = $false
        if ($c -is [string]) { $isHumanPrompt = $true }
        elseif ($c -is [System.Array] -and $c.Count -gt 0) {
            if ([string]$c[0].type -ne 'tool_result') { $isHumanPrompt = $true }
        }
        if ($isHumanPrompt) { $boundary = $i; break }
    }
    if ($boundary -lt 0) { exit 0 }

    # Collect assistant text and source-fetch tool usage since the boundary.
    $assistantTextParts = @()
    $toolNames = New-Object 'System.Collections.Generic.HashSet[string]'
    $sourceFetchSeen = $false
    for ($i = $boundary + 1; $i -lt $entries.Count; $i++) {
        $e = $entries[$i]
        if ($e.type -ne 'assistant') { continue }
        $content = $e.message.content
        if (-not $content) { continue }
        foreach ($block in $content) {
            if ($block.type -eq 'text' -and $block.text) {
                $assistantTextParts += [string]$block.text
            }
            elseif ($block.type -eq 'tool_use' -and $block.name) {
                $toolName = [string]$block.name
                [void]$toolNames.Add($toolName)

                if ($toolName -in @('WebFetch', 'WebSearch', 'web.run')) {
                    $sourceFetchSeen = $true
                }

                $command = ''
                try {
                    if ($block.input -and $block.input.command) {
                        $command = [string]$block.input.command
                    }
                } catch { $command = '' }

                if ($command) {
                    $isFetchCommand = $command -match '(?i)\b(Invoke-WebRequest|Invoke-RestMethod|iwr|irm|curl|wget)\b' -and $command -match 'https?://'
                    $isGistView = $command -match '(?i)\bgh\s+gist\s+view\b'
                    if ($isFetchCommand -or $isGistView) {
                        $sourceFetchSeen = $true
                    }
                }
            }
        }
    }
    $text = ($assistantTextParts -join "`n")
    if ([string]::IsNullOrWhiteSpace($text)) { exit 0 }

    # Article reviews have an additional preflight: the original article body
    # must be inspectable before a normal review can be produced.
    # Headings unique to the article-review output template. Any one of these
    # identifies a review on its own.
    $articleReviewStrong = $text -match '(?m)^#\s+Journalistic Article Review:|(?m)^##\s+Article Map\b|(?m)^##\s+Sourcing Audit\b|(?m)^##\s+Evidence Load Test\b|(?m)^##\s+Headline,\s*Framing'

    # "## Findings" is in that template too, but it is an ordinary heading any
    # report, changelog, or summary may use, so alone it fires on non-review
    # output. It counts only alongside a review-specific signal — which a real
    # review always carries, since Phase 6 and the Sourcing Audit are mandatory
    # whenever Phase -1 passes.
    # Corroborators are anchored to headings or to a template verdict line, not
    # to bare phrases: "right of reply" and "quote context" appear in prose that
    # merely discusses the method, which the hook must not fire on.
    $articleReviewFindings = $text -match '(?m)^##\s+Findings\b'
    $articleReviewCorroborated = $text -match '(?m)^##\s+Specialist Checks\b|(?m)^##\s+Journalistic Verdict\b|(?im)\*\*Verdict:\*\*\s*\**\s*(?:Reliable as reported|Mostly reliable with caveats|Mixed|Misleading|Unsupported|Contradicted)\b'

    $articleReviewProduced = $articleReviewStrong -or ($articleReviewFindings -and $articleReviewCorroborated)
    $articleReviewStopped = $text -match '(?m)^#\s+Review Stopped:\s+Original Article Not Found\b'
    $articleAccessRecorded = $text -match '(?im)^\s*[-*]?\s*\*\*Original article access:\*\*|^\s*Original article access:|^\s*##\s+Phase -1\b|Original Article Retrieval Gate'
    $articleAccessFailureMentioned = $text -match '(?is)original article(?:\s+body)?.{0,80}(not found|not inspectable|inaccessible|could not be found|cannot be found|could not be fetched|cannot be fetched|could not be inspected|cannot be inspected)'

    if ($articleReviewProduced -and -not $articleReviewStopped -and -not $articleAccessRecorded) {
        $reason = @"
Research-discipline check blocked this stop.

The just-completed turn produced a journalistic article review without recording original article access. A review must first fetch and inspect the original article body, or use complete article text supplied in-session.

Before stopping, either:
  1. Add `Original article access:` to the review summary with the fetched/supplied article source and access date.
  2. If the original article body was not found or inspectable, replace the review with `# Review Stopped: Original Article Not Found` and list retrieval attempts.

Hook at .codex/hooks/check-research-warrant.ps1. Inspect or disable via .codex/hooks.json.
"@

        @{ decision = 'block'; reason = $reason } | ConvertTo-Json -Compress | Write-Output
        exit 0
    }

    if ($articleReviewProduced -and -not $articleReviewStopped -and $articleAccessFailureMentioned) {
        $reason = @"
Research-discipline check blocked this stop.

The output says the original article was not found or inspectable, but still proceeds with article-review sections. When the original article body cannot be inspected, the whole review must stop.

Replace the review with `# Review Stopped: Original Article Not Found`, list retrieval attempts, and state what exact input would allow the review to proceed.

Hook at .codex/hooks/check-research-warrant.ps1. Inspect or disable via .codex/hooks.json.
"@

        @{ decision = 'block'; reason = $reason } | ConvertTo-Json -Compress | Write-Output
        exit 0
    }

    # (traced) is a per-session claim, and CLAUDE.md requires the URL and access
    # date to be stated with it. A report that asserts traced findings and
    # records no URL anywhere cannot be re-checked by anyone; its source overlap
    # with a second run is also uncomputable, which is what blocked the S1
    # symmetry measurement. evals/score.py hard-fails this after the fact. Here
    # it fires at generation time, while the report can still be fixed.
    #
    # Deliberately above the $sourceFetchSeen exit. The failure is not "no
    # fetching happened" but "the fetches were not written down" -- the S1 run
    # that produced 49 KB with zero URLs did search the web.
    #
    # Gated to produced reports rather than conversations about the discipline:
    # a report-shaped anchor plus at least three (traced) uses. A methodology
    # discussion names the label once or twice and emits no report anchor.
    $tracedUses = ([regex]::Matches($text, '\(traced')).Count
    $anyUrl = $text -match 'https?://'
    $reportAnchor = $text -match '(?m)^#\s+(?:Event Investigation|Peer Review|Claim Classification|Journalistic Article Review|OSINT|Belief Revision|First Principles Analysis|Fallacy)' -or
                    $text -match '(?m)^##\s+Sources\s*&\s*Warrants\b' -or
                    $text -match '(?im)^\s*[-*]?\s*\*\*(?:Verdict|Recommendation):\*\*'

    if ($tracedUses -ge 3 -and -not $anyUrl -and $reportAnchor) {
        $reason = @"
Research-discipline check blocked this stop.

The just-completed turn uses (traced) $tracedUses times, but the output contains no URL at all. (traced) is a per-session claim: CLAUDE.md requires the URL and access date to be stated, so that a reader can re-check the chain and so that two runs of the same item can be compared on their sources.

Before stopping, do one of:
  1. State the URL and access date with each traced claim, and record them in a `## Sources & Warrants` table (URL, access date, publication date, warrant, funding / ownership / mandate / alignment).
  2. Where the chain was not actually followed to a primary this session, relabel the claim `(memory - unverified)`, or `(deferred to consensus)` naming the consensus mechanism.

Hook at .codex/hooks/check-research-warrant.ps1. Inspect or disable via .codex/hooks.json.
"@

        @{ decision = 'block'; reason = $reason } | ConvertTo-Json -Compress | Write-Output
        exit 0
    }

    if ($sourceFetchSeen) { exit 0 }
    if ($text -match '\(memory\s*[-—]\s*unverified\)') { exit 0 }

    # Marker categories must stay in sync with the skill output templates in
    # .agents/skills/*/SKILL.md and .claude/skills/*/SKILL.md. The regexes match both old (colon-label) and
    # new (## heading) styles so the hook survives heading-format changes.
    $categories = [ordered]@{
        'Hypothesis A/B'   = 'Hypothesis\s+[AB]\b'
        'Investigation'    = 'Cui\s+Bono|MMO\s+(Matrix|Suspect)|Red\s+Flags?(\s+Analysis)?'
        'Classification'   = 'Established\s+fact|\bRefuted\b|Provisionally\s+accepted|Well-supported\s+finding|Authority-warranted\s+only|\bOrphaned\b'
        'Article structure' = 'Journalistic Article Review|Article Map|Sourcing Audit|Evidence Load Test|Headline,\s*Framing'
        'Journalism checks' = 'Right of reply|Source-network test|Quote context|Headline-body fit|Journalistic Verdict'
        'First-principles' = '\bBedrock\b|\bDecomposition\b|\bExcavation\b|\bRebuild\b|\bOverturned\b'
        'Peer/Tier'        = '\bSteelman\b|Tier\s*0|Tier\s*1|Bradford\s+Hill|\bGRADE\b'
        'Warrant labels'   = '\(traced\)|\(deferred to consensus\)|\(deferred,\s+fragile\)|Sources\s+&\s+Warrants'
        'Revision'         = 'Anchor Declaration|Predicted Update|Calibration Audit|Asymmetric-warrant|Pressure-Direction Check'
    }

    $matched = @()
    foreach ($k in $categories.Keys) {
        if ($text -match $categories[$k]) { $matched += $k }
    }
    if ($matched.Count -lt 3) { exit 0 }

    $reason = @"
Research-discipline check blocked this stop.

The just-completed turn produced analytical output (categories detected: $($matched -join ', ')) but made no source-fetch calls. This is the failure mode CLAUDE.md is built to prevent: analysis from memory laundering training-data bias.

Before stopping, do one of:
  1. Fetch primary sources (WebFetch / WebSearch, or an explicit terminal/API fetch for raw sources such as GitHub gists) and rewrite with (traced) labels + URLs + access dates.
  2. Add explicit (deferred to consensus) labels naming the social/institutional consensus mechanism; for scientific claims, state that it is only a political/social prior unless traced to reproduced or replicated evidence.
  3. If genuinely answering from background knowledge, add (memory - unverified) somewhere visible.
  4. End the response with the bias self-audit answer (CLAUDE.md rule #6).

Hook at .codex/hooks/check-research-warrant.ps1. Inspect or disable via .codex/hooks.json.
"@

    @{ decision = 'block'; reason = $reason } | ConvertTo-Json -Compress | Write-Output
    exit 0
}
catch {
    [Console]::Error.WriteLine("check-research-warrant.ps1 error: $($_.Exception.Message)")
    exit 0
}

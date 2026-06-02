# Stop hook: enforce source-tracing discipline for analytical output.
#
# Reads the Stop-hook JSON payload from stdin, inspects the just-completed
# assistant turn, and blocks the stop when analytical-framing markers are
# present without a WebFetch or WebSearch call in the same turn.
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

    # Collect assistant text and tool_use names since the boundary.
    $assistantTextParts = @()
    $toolNames = New-Object 'System.Collections.Generic.HashSet[string]'
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
                [void]$toolNames.Add([string]$block.name)
            }
        }
    }
    $text = ($assistantTextParts -join "`n")
    if ([string]::IsNullOrWhiteSpace($text)) { exit 0 }

    if ($toolNames.Contains('WebFetch') -or $toolNames.Contains('WebSearch')) { exit 0 }
    if ($text -match '\(memory\s*[-—]\s*unverified\)') { exit 0 }

    # Marker categories must stay in sync with the skill output templates in
    # .claude/skills/*/SKILL.md. The regexes match both old (colon-label) and
    # new (## heading) styles so the hook survives heading-format changes.
    $categories = [ordered]@{
        'Hypothesis A/B'   = 'Hypothesis\s+[AB]\b'
        'Investigation'    = 'Cui\s+Bono|MMO\s+(Matrix|Suspect)|Red\s+Flags?(\s+Analysis)?'
        'Classification'   = 'Established\s+fact|\bRefuted\b|Provisionally\s+accepted|Well-supported\s+finding|Authority-warranted\s+only|\bOrphaned\b'
        'First-principles' = '\bBedrock\b|\bDecomposition\b|\bExcavation\b|\bRebuild\b|\bOverturned\b'
        'Peer/Tier'        = '\bSteelman\b|Tier\s*0|Tier\s*1|Bradford\s+Hill|\bGRADE\b'
        'Warrant labels'   = '\(traced\)|\(deferred to consensus\)|\(deferred,\s+fragile\)'
        'Revision'         = 'Anchor Declaration|Predicted Update|Calibration Audit|Asymmetric-warrant|Pressure-Direction Check'
    }

    $matched = @()
    foreach ($k in $categories.Keys) {
        if ($text -match $categories[$k]) { $matched += $k }
    }
    if ($matched.Count -lt 3) { exit 0 }

    $reason = @"
Research-discipline check blocked this stop.

The just-completed turn produced analytical output (categories detected: $($matched -join ', ')) but made no WebFetch or WebSearch calls. This is the failure mode CLAUDE.md is built to prevent: analysis from memory laundering training-data bias.

Before stopping, do one of:
  1. Fetch primary sources (WebFetch / WebSearch) and rewrite with (traced) labels + URLs + access dates.
  2. Add explicit (deferred to consensus) labels naming the consensus mechanism.
  3. If genuinely answering from background knowledge, add (memory - unverified) somewhere visible.
  4. End the response with the bias self-audit answer (CLAUDE.md rule #6).

Hook at .claude/hooks/check-research-warrant.ps1. Inspect via /hooks; disable in .claude/settings.json.
"@

    @{ decision = 'block'; reason = $reason } | ConvertTo-Json -Compress | Write-Output
    exit 0
}
catch {
    [Console]::Error.WriteLine("check-research-warrant.ps1 error: $($_.Exception.Message)")
    exit 0
}

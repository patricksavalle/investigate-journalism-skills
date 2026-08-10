#!/usr/bin/env python3
"""Regression test for the Stop hook's two preflight branches.

**Article-review preflight** (CLAUDE.md Rule 0a) must block a journalistic
article review that does not record original-article access, and must not fire
on anything else -- including ordinary reports that happen to use a "## Findings"
heading, and conversations that merely discuss the review method.

**Traced-without-URL preflight** (CLAUDE.md "Strictness on (traced)") must block
a report that asserts traced findings while recording no URL anywhere, and must
not fire on a report that records its URLs or on a discussion of the label. This
branch sits above the source-fetch exit, so cases that exercise it declare a
fetch -- the failure it catches is not "no fetching happened" but "the fetches
were not written down", which is what the S1 run did.

Feeds synthetic Stop payloads to the hook and asserts block / no-block.

Usage:
    python evals/test_hook_preflight.py                 # both hook copies
    python evals/test_hook_preflight.py .claude/hooks/check-research-warrant.ps1
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
HOOKS = [
    REPO_ROOT / ".claude" / "hooks" / "check-research-warrant.ps1",
    REPO_ROOT / ".codex" / "hooks" / "check-research-warrant.ps1",
]

# (name, assistant turn text, must_block[, tool_names_used_this_turn])
#
# The optional fourth element simulates tool_use blocks in the turn. Supplying a
# fetch tool makes the source-fetch exit fire, which isolates the branches that
# sit above it -- without it, a case could "pass" on the generic no-fetch block
# and prove nothing about the branch it was written for.
CASES: list[tuple] = [
    (
        "review with a strong template heading, no access line",
        """
# Journalistic Article Review: Ministry Buried Safety Report

## Summary
- **Verdict:** Mixed

## Article Map
headline claim, thesis, load-bearing claims

## Sourcing Audit
| source | role | independence |
""",
        True,
    ),
    (
        "partial review: Findings + Specialist Checks, no access line",
        """
## Specialist Checks
Routed the underlying study to peer-review.

## Findings
Major: the central allegation rests on one anonymous official.
""",
        True,
    ),
    (
        "partial review: Findings + Journalistic Verdict heading, no access line",
        """
## Findings
Major: single-source allegation.

## Journalistic Verdict
Unsupported as reported.
""",
        True,
    ),
    (
        "partial review: Findings + template verdict line, no access line",
        """
## Summary
- **Verdict:** Misleading

## Findings
Major: the headline asserts what the body only attributes.
""",
        True,
    ),
    (
        "review WITH an access line",
        """
# Journalistic Article Review: Some Piece

## Summary
- **Original article access:** https://example.org/piece ; accessed 2026-08-10
- **Verdict:** Mixed

## Article Map
claims

## Findings
Minor: headline overstates.
""",
        False,
    ),
    (
        "correct retrieval stop",
        """
# Review Stopped: Original Article Not Found

## Retrieval Attempts
- WebSearch: no matching article.

## Needed To Proceed
- Original article URL.
""",
        False,
    ),
    (
        "ordinary report using a '## Findings' heading",
        """
## What ran
16 fresh sessions, one per run.

## Results
| Item | exact | adjacent |
|---|---|---|
| R1 | 0.600 | 1.000 |

## Findings
R1's disagreement is at one label boundary, not in the analysis.
""",
        False,
    ),
    (
        "'## Findings' plus method vocabulary in running prose",
        """
## Findings
The linter flags quote context stripping in the parser, and right of reply
handling is untested.

## Next steps
Fix the tokenizer.
""",
        False,
    ),
    (
        "methodology discussion naming the phases",
        """
The article-review skill runs a Sourcing Audit and an Evidence Load Test, then
reaches a Journalistic Verdict. Right of reply is checked in phase 2.
""",
        False,
    ),
    # --- traced-without-URL branch -----------------------------------------
    (
        "investigation asserting (traced) with no URL anywhere",
        """
# Event Investigation: Pipeline Rupture

## Summary
- **Verdict:** Hypothesis A stronger

## Red Flags
The salvage vessel was in the area with its transponder off `(traced)`.
Naval experts called the platform implausible `(traced)`.
The prosecutor's filing names a chartered yacht `(traced)`.
""",
        True,
        ("WebSearch",),
    ),
    (
        "same report, URLs recorded in a Sources & Warrants table",
        """
# Event Investigation: Pipeline Rupture

## Summary
- **Verdict:** Hypothesis A stronger

## Red Flags
The salvage vessel was in the area `(traced)`. Experts dissented `(traced)`.
The prosecutor's filing names a chartered yacht `(traced)`.

## Sources & Warrants
| Finding | Source | URL | Access date | Warrant |
|---|---|---|---|---|
| Yacht charter | GBA | https://generalbundesanwalt.de/x | 2026-08-10 | (traced) |
""",
        False,
        ("WebSearch",),
    ),
    # --- marker-category gate: analysis vs talk about analysis ---------------
    (
        "work report quoting the vocabulary, no report anchor",
        """
Stage 0 taught the scorer to read a verdict written as `Hypothesis A (a named
account)` rather than `Hypothesis A stronger`. Stage 2 canonicalised the
`(traced)` row and the Steelman sourcing note across eight skills. F1 still
lands on Established fact 3/3.
""",
        False,
    ),
    (
        "dense prose analysis with no headings at all",
        """
Hypothesis A is the official account and Hypothesis B the alternative. On Cui
Bono the beneficiary is clear. The claim that the platform was implausible is an
Established fact `(traced)`, and the Steelman of B rests on Tier 0 material that
nobody has produced.
""",
        True,
    ),
    (
        "report anchor plus three categories, no fetch",
        """
# Event Investigation: Something

## Summary
- **Verdict:** Hypothesis A stronger

Cui Bono favours the incumbent. The Steelman of B is thin.
""",
        True,
    ),
    (
        "discussion of the (traced) label with no report anchor",
        """
The rule is that `(traced)` is per-session. A turn that writes `(traced)` and
records no URL cannot be re-checked, so `(traced)` without a URL is the defect
the scorer hard-fails.
""",
        False,
        ("WebSearch",),
    ),
]


def invoke(hook: Path, text: str, workdir: Path, tools: tuple[str, ...] = ()) -> bool:
    """Run the hook on a one-turn transcript; True if it blocked the stop."""
    transcript = workdir / "t.jsonl"
    blocks: list[dict] = [
        {"type": "tool_use", "name": name, "input": {}} for name in tools
    ]
    blocks.append({"type": "text", "text": text})
    transcript.write_text(
        "\n".join(
            json.dumps(x)
            for x in (
                {"type": "user", "message": {"content": "do the thing"}},
                {"type": "assistant", "message": {"content": blocks}},
            )
        ),
        encoding="utf-8",
    )
    payload = json.dumps(
        {"transcript_path": str(transcript), "stop_hook_active": False}
    )
    proc = subprocess.run(
        ["pwsh", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(hook)],
        input=payload,
        capture_output=True,
        text=True,
    )
    if proc.stderr.strip():
        print(f"       stderr: {proc.stderr.strip()[:200]}")
    return '"decision":"block"' in (proc.stdout or "").replace(" ", "")


def main(argv: list[str]) -> int:
    hooks = [Path(a).resolve() for a in argv[1:]] or HOOKS
    failures = 0
    with tempfile.TemporaryDirectory() as td:
        workdir = Path(td)
        for hook in hooks:
            if not hook.exists():
                print(f"error: no hook at {hook}")
                return 2
            print(f"hook: {hook.relative_to(REPO_ROOT)}")
            for case in CASES:
                name, text, must_block = case[:3]
                tools = case[3] if len(case) > 3 else ()
                blocked = invoke(hook, text, workdir, tools)
                ok = blocked == must_block
                failures += not ok
                mark = "ok  " if ok else "FAIL"
                print(f"  {mark} blocked={blocked!s:5} want={must_block!s:5}  {name}")
    print(
        "hook preflight: pass"
        if not failures
        else f"hook preflight: {failures} failure(s)"
    )
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

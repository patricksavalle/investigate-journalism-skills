#!/usr/bin/env python3
"""Regression test for the Stop hook's article-review preflight.

The preflight (CLAUDE.md Rule 0a) must block a journalistic article review that
does not record original-article access, and must not fire on anything else --
including ordinary reports that happen to use a "## Findings" heading, and
conversations that merely discuss the review method.

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

# (name, assistant turn text, must_block)
CASES: list[tuple[str, str, bool]] = [
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
]


def invoke(hook: Path, text: str, workdir: Path) -> bool:
    """Run the hook on a one-turn transcript; True if it blocked the stop."""
    transcript = workdir / "t.jsonl"
    transcript.write_text(
        "\n".join(
            json.dumps(x)
            for x in (
                {"type": "user", "message": {"content": "do the thing"}},
                {
                    "type": "assistant",
                    "message": {"content": [{"type": "text", "text": text}]},
                },
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
            for name, text, must_block in CASES:
                blocked = invoke(hook, text, workdir)
                ok = blocked == must_block
                failures += not ok
                mark = "ok  " if ok else "FAIL"
                print(f"  {mark} blocked={blocked!s:5} want={must_block!s:5}  {name}")
    print(
        "article-review preflight: pass"
        if not failures
        else f"article-review preflight: {failures} failure(s)"
    )
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

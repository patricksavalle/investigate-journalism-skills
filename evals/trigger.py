#!/usr/bin/env python3
"""Trigger-accuracy set: validate it, and emit per-skill sets for the optimiser.

The library has ten skills whose descriptions compete. A request about a study
could plausibly land on `peer-review`, `journalistic-article-review`, or
`scientific-fact-classification`; "investigate this" splits between
`investigative-reasoning` and `osint-research`. Each skill carries prose telling
the model how to route once loaded -- but routing prose only helps *after* the
right skill has triggered. Nothing measures whether it does.

So `trigger-eval.json` records the intended **routing**, not a per-skill boolean:
each query names the skill that should win, or null for "no skill". That is the
shape of the real failure. A per-skill boolean set cannot see a query going to
the wrong sibling; it only sees one skill's recall, and widening a description to
fix that steals triggers from its neighbour.

Anthropic's description optimiser (`skill-creator/scripts/run_loop.py`) does take
per-skill boolean sets, so `emit` projects the routing set down to one, treating
every other skill's positives as that skill's near-miss negatives -- which is
exactly the pressure that keeps a widening description honest.

Usage:
    python evals/trigger.py check
    python evals/trigger.py emit peer-review > /tmp/peer-review-trigger.json
    python evals/trigger.py coverage
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO / ".claude" / "skills"
EVAL_SET = Path(__file__).resolve().parent / "trigger-eval.json"


def skills() -> list[str]:
    return sorted(d.name for d in SKILLS_DIR.iterdir() if (d / "SKILL.md").exists())


def load() -> list[dict]:
    return json.loads(EVAL_SET.read_text(encoding="utf-8"))


def check() -> int:
    items = load()
    known = set(skills())
    problems: list[str] = []

    seen: set[str] = set()
    for i, it in enumerate(items):
        q = it.get("query", "")
        if not q:
            problems.append(f"[{i}] empty query")
        if q in seen:
            problems.append(f"[{i}] duplicate query")
        seen.add(q)
        target = it.get("should_trigger", ...)
        if target is ...:
            problems.append(f"[{i}] missing should_trigger")
        elif target is not None and target not in known:
            problems.append(f"[{i}] unknown skill {target!r}")
        if not it.get("why"):
            problems.append(f"[{i}] no `why` — an untestable item is a liability")

    positives = [it for it in items if it.get("should_trigger")]
    negatives = [it for it in items if it.get("should_trigger") is None]
    if len(negatives) < len(positives) / 3:
        problems.append(
            f"only {len(negatives)} negatives against {len(positives)} positives — "
            "near-misses are where description quality actually shows"
        )

    uncovered = known - {it.get("should_trigger") for it in items}
    for u in sorted(uncovered):
        problems.append(f"no positive query for `{u}`")

    for p in problems:
        print(f"FAIL: {p}")
    print(
        f"\n{len(items)} queries — {len(positives)} positive, {len(negatives)} "
        f"negative, {len(known)} skills — "
        + ("all checks passed" if not problems else f"{len(problems)} problem(s)")
    )
    return 1 if problems else 0


def coverage() -> int:
    items = load()
    counts = Counter(it.get("should_trigger") for it in items)
    print(f"{'skill':<42} positives")
    for s in skills():
        print(f"{s:<42} {counts.get(s, 0)}")
    print(f"{'(no skill)':<42} {counts.get(None, 0)}")
    return 0


def emit(skill: str) -> int:
    if skill not in skills():
        print(f"error: unknown skill {skill!r}", file=sys.stderr)
        return 2
    out = [
        {"query": it["query"], "should_trigger": it.get("should_trigger") == skill}
        for it in load()
    ]
    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check", help="validate the routing set against the live skills")
    sub.add_parser("coverage", help="positives per skill")
    e = sub.add_parser("emit", help="project to one skill's boolean set")
    e.add_argument("skill")

    args = p.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass
    if args.cmd == "check":
        return check()
    if args.cmd == "coverage":
        return coverage()
    return emit(args.skill)


if __name__ == "__main__":
    sys.exit(main())

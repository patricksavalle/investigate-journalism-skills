#!/usr/bin/env python3
"""Structural validator for the skill library.

Scores the *library*, not its outputs — `evals/score.py` does the latter.

Checks are derived from the library's own invariants:
  1. folder name == frontmatter `name`
  2. every backticked skill reference resolves to a real skill
  3. .claude/skills and .agents/skills are byte-identical mirrors
  4. README.md indexes every skill
  5. every report-shaped skill carries all six warrant labels
  6. the shared routing block is identical wherever it appears

No third-party dependencies. Python 3.9+.

Usage:
    python scripts/validate-skills.py          # report and exit non-zero on failure
    python scripts/validate-skills.py --list   # show the resolved skill inventory
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CLAUDE_SKILLS = REPO / ".claude" / "skills"
AGENT_SKILLS = REPO / ".agents" / "skills"
ROOT_DOCS = ["CLAUDE.md", "AGENTS.md", "README.md"]

# Skills that do not emit a warrant-labelled report and so are exempt from
# check 5. Mirrors evals/score.py NON_REPORT_SKILLS.
#   intuitive-thinking  defines only (intuition — unwarranted), by design
#   publisher-nl        consumes labels via a calibration table, emits none
NON_REPORT_SKILLS = {"intuitive-thinking", "publisher-nl"}

WARRANT_LABELS = [
    "(traced)",
    "(deferred to consensus)",
    "(deferred, fragile)",
    "(memory — unverified)",
    "(user-supplied — unverified)",
    "(intuition — unwarranted)",
]

ROUTING_SENTINEL = "check whether another project skill owns the missing layer"
ROUTING_END = "it may not manufacture premises."

failures: list[str] = []
notes: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def frontmatter_name(text: str) -> str | None:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return None
    n = re.search(r"^name:\s*(.+?)\s*$", m.group(1), re.M)
    return n.group(1).strip().strip("\"'") if n else None


def inventory() -> dict[str, dict]:
    skills = {}
    for d in sorted(CLAUDE_SKILLS.iterdir()):
        f = d / "SKILL.md"
        if not f.exists():
            continue
        text = read(f)
        skills[d.name] = {
            "dir": d.name,
            "path": f,
            "name": frontmatter_name(text),
            "text": text,
        }
    return skills


# --------------------------------------------------------------------------


def check_name_match(skills: dict) -> None:
    for dirname, s in skills.items():
        if s["name"] is None:
            fail(f"{dirname}/SKILL.md: no `name:` in frontmatter")
        elif s["name"] != dirname:
            fail(
                f"{dirname}/SKILL.md: frontmatter name '{s['name']}' "
                f"does not match folder name '{dirname}'"
            )


def check_frontmatter_parseable(skills: dict) -> None:
    """Descriptions must survive a YAML parse.

    A plain (unquoted) YAML scalar cannot contain ": " — the parser reads it as
    a nested mapping and the description is lost, so the loader falls back to
    the file's H1. publisher-nl hit exactly this ("...warrant chain: no new
    load-bearing facts...") and silently lost its trigger text.
    """
    for dirname, s in skills.items():
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n", s["text"], re.S)
        if not m:
            fail(f"{dirname}/SKILL.md: no frontmatter block")
            continue
        d = re.search(r"^description:\s*(.*)$", m.group(1), re.M)
        if not d:
            fail(f"{dirname}/SKILL.md: no `description:` in frontmatter")
            continue
        val = d.group(1).strip()
        if not val:
            fail(f"{dirname}/SKILL.md: empty description")
        elif not val.startswith(("'", '"')) and ": " in val:
            fail(
                f"{dirname}/SKILL.md: unquoted description contains ': ' — "
                "YAML will truncate it; wrap the value in quotes"
            )


def check_line_endings(skills: dict) -> None:
    """Mixed line endings across the library churn diffs and mirror hashes."""
    crlf = [d for d, s in skills.items() if b"\r\n" in s["path"].read_bytes()]
    if crlf and len(crlf) != len(skills):
        fail(
            f"mixed line endings: {len(crlf)} of {len(skills)} skill files use CRLF "
            f"({', '.join(sorted(crlf)[:3])}{'...' if len(crlf) > 3 else ''})"
        )


def check_references(skills: dict) -> None:
    """Every backticked skill-like token must resolve to a real skill."""
    valid = set(skills) | {s["name"] for s in skills.values() if s["name"]}
    sources = {str(s["path"].relative_to(REPO)): s["text"] for s in skills.values()}
    for doc in ROOT_DOCS:
        p = REPO / doc
        if p.exists():
            sources[doc] = read(p)

    seen: set[tuple[str, str]] = set()
    for where, text in sources.items():
        for tok in re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+){1,})`", text):
            if tok in valid:
                continue
            close = difflib.get_close_matches(tok, valid, n=1, cutoff=0.75)
            if close and (where, tok) not in seen:
                seen.add((where, tok))
                fail(
                    f"{where}: unresolved skill reference `{tok}` "
                    f"(closest real skill: `{close[0]}`)"
                )


def check_mirrors(skills: dict) -> None:
    if not AGENT_SKILLS.exists():
        notes.append(".agents/skills does not exist — mirror check skipped")
        return
    claude = {p.relative_to(CLAUDE_SKILLS) for p in CLAUDE_SKILLS.rglob("*") if p.is_file()}
    agents = {p.relative_to(AGENT_SKILLS) for p in AGENT_SKILLS.rglob("*") if p.is_file()}
    for missing in sorted(claude - agents):
        fail(f"mirror: .agents/skills is missing {missing}")
    for extra in sorted(agents - claude):
        fail(f"mirror: .agents/skills has orphan {extra}")
    for rel in sorted(claude & agents):
        a = hashlib.sha256((CLAUDE_SKILLS / rel).read_bytes()).hexdigest()
        b = hashlib.sha256((AGENT_SKILLS / rel).read_bytes()).hexdigest()
        if a != b:
            fail(f"mirror drift: {rel} differs between .claude/skills and .agents/skills")


def check_readme_index(skills: dict) -> None:
    p = REPO / "README.md"
    if not p.exists():
        fail("README.md not found")
        return
    text = read(p)
    for dirname in skills:
        if f"skills/{dirname}" not in text:
            fail(f"README.md does not link the `{dirname}` skill")


def check_warrant_labels(skills: dict) -> None:
    for dirname, s in skills.items():
        if dirname in NON_REPORT_SKILLS:
            continue
        missing = [lbl for lbl in WARRANT_LABELS if lbl not in s["text"]]
        if missing:
            fail(
                f"{dirname}/SKILL.md: missing warrant label(s): "
                + ", ".join(missing)
            )


def check_routing_block(skills: dict) -> None:
    """The shared routing paragraph must be byte-identical wherever it appears."""
    copies: dict[str, list[str]] = {}
    sources = {str(s["path"].relative_to(REPO)): s["text"] for s in skills.values()}
    for doc in ROOT_DOCS:
        p = REPO / doc
        if p.exists():
            sources[doc] = read(p)

    for where, text in sources.items():
        i = text.find(ROUTING_SENTINEL)
        if i < 0:
            continue
        # Compare the whole routing *block*, not one line. CLAUDE.md keeps the
        # routing sentence and its "If no skill clearly owns the gap ..."
        # continuation on a single line; the skills split them into two
        # paragraphs. That is a layout difference, not a content one, so
        # normalise whitespace across the block before hashing.
        end = text.find(ROUTING_END, i)
        body = text[i : end + len(ROUTING_END)] if end > 0 else text[i:].split("\n\n")[0]
        key = hashlib.sha256(" ".join(body.split()).encode()).hexdigest()[:12]
        copies.setdefault(key, []).append(where)

    if len(copies) > 1:
        groups = sorted(copies.items(), key=lambda kv: -len(kv[1]))
        detail = "; ".join(
            f"{k}: {len(v)} copies ({', '.join(sorted(v)[:3])}{'...' if len(v) > 3 else ''})"
            for k, v in groups
        )
        fail(f"routing block has {len(copies)} divergent variants — {detail}")
    elif copies:
        notes.append(
            f"routing block: {len(next(iter(copies.values())))} identical copies"
        )


# --------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--list", action="store_true", help="print the skill inventory")
    args = ap.parse_args()

    if not CLAUDE_SKILLS.exists():
        print(f"error: {CLAUDE_SKILLS} not found", file=sys.stderr)
        return 2

    skills = inventory()

    if args.list:
        for dirname, s in skills.items():
            flag = "" if s["name"] == dirname else f"   <-- name: {s['name']}"
            print(f"{dirname}{flag}")
        return 0

    check_name_match(skills)
    check_frontmatter_parseable(skills)
    check_line_endings(skills)
    check_references(skills)
    check_mirrors(skills)
    check_readme_index(skills)
    check_warrant_labels(skills)
    check_routing_block(skills)

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass

    for n in notes:
        print(f"note: {n}")
    for f in failures:
        print(f"FAIL: {f}")
    print(
        f"\n{len(skills)} skills checked — "
        + ("all checks passed" if not failures else f"{len(failures)} failure(s)")
    )
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

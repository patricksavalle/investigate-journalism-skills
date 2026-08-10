#!/usr/bin/env python3
"""Generate the skill library from single-sourced modules.

Why this exists
---------------
The same procedure was written into three to five skills in slightly different
words, and the wordings drifted. Eight skills carried eight distinct versions of
the warrant-label table. Four carried different requirement sets for the same
causal-direction gate, so a causal claim's verdict depended on which skill you
entered through -- in a library whose value is a reproducible audit chain.

So each shared procedure is now authored once in `library/modules/` and composed
into the shipped `SKILL.md` files here. The shipped files stay self-contained:
no runtime file reads, no behavioural change from the composition itself, and
the standalone property README.md advertises is preserved. Only the *source*
stops being duplicated.

It also generates both trees. `.claude/skills/` and `.agents/skills/` are
byte-identical by contract (validate-skills.py check 3), which previously meant
every edit was made twice.

Layout
------
    library/skills/<name>.md    the skill source: frontmatter, body, includes
    library/modules/<name>.md   shared text, with {{param}} placeholders
    library/bindings.json       {skill: {module: {param: value}}}

An include is a line of the form:

    <!-- include: warrant-labels -->

Parameters are per-skill, so a module can carry canonical text while each skill
supplies its own binding -- the rule is one rule, what it requires here is local.
A `{{param}}` alone on a line disappears with the line when its value is empty.

Usage
-----
    python scripts/build-skills.py            # write both trees
    python scripts/build-skills.py --check    # verify on-disk matches source
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LIBRARY = REPO / "library"
SKILL_SRC = LIBRARY / "skills"
MODULES = LIBRARY / "modules"
BINDINGS = LIBRARY / "bindings.json"
TREES = [REPO / ".claude" / "skills", REPO / ".agents" / "skills"]

INCLUDE_RE = re.compile(r"^[ \t]*<!--\s*include:\s*([a-z0-9-]+)\s*-->[ \t]*$", re.M)
PARAM_RE = re.compile(r"\{\{([a-z0-9_]+)\}\}")
# A parameter alone on its line: the line goes when the value is empty, so an
# unused optional slot leaves no blank gap behind.
LONE_PARAM_RE = re.compile(r"^[ \t]*\{\{([a-z0-9_]+)\}\}[ \t]*\n", re.M)


class BuildError(Exception):
    pass


def render_module(name: str, skill: str, params: dict[str, str]) -> str:
    path = MODULES / f"{name}.md"
    if not path.exists():
        raise BuildError(f"{skill}: no module `{name}` at {path.relative_to(REPO)}")
    text = path.read_text(encoding="utf-8")

    declared = set(PARAM_RE.findall(text))
    supplied = set(params)
    unknown = supplied - declared
    if unknown:
        raise BuildError(
            f"{skill}/{name}: bindings.json supplies parameter(s) the module does "
            f"not declare: {', '.join(sorted(unknown))}. A typo here would "
            f"silently drop the text."
        )

    # Empty-valued lone parameters take their line with them.
    def drop_if_empty(m: re.Match) -> str:
        return "" if not params.get(m.group(1), "") else m.group(0)

    text = LONE_PARAM_RE.sub(drop_if_empty, text)

    missing = sorted(p for p in PARAM_RE.findall(text) if p not in params)
    if missing:
        raise BuildError(
            f"{skill}/{name}: unbound parameter(s): {', '.join(missing)}"
        )
    text = PARAM_RE.sub(lambda m: params[m.group(1)], text)
    # An optional slot that renders to nothing leaves the blank line above and
    # below it. Collapsing runs of blank lines is what lets a module carry
    # optional sections without every skill needing to bind every one.
    return re.sub(r"\n{3,}", "\n\n", text)


def build_skill(src: Path, bindings: dict) -> tuple[str, str]:
    """Return (skill name, rendered SKILL.md)."""
    skill = src.stem
    text = src.read_text(encoding="utf-8")
    skill_bindings = bindings.get(skill, {})

    used: set[str] = set()

    def expand(m: re.Match) -> str:
        name = m.group(1)
        used.add(name)
        return render_module(name, skill, skill_bindings.get(name, {})).rstrip("\n")

    rendered = INCLUDE_RE.sub(expand, text)

    unused = set(skill_bindings) - used
    if unused:
        raise BuildError(
            f"{skill}: bindings.json binds module(s) the source never includes: "
            f"{', '.join(sorted(unused))}"
        )
    if "<!-- include:" in rendered:
        raise BuildError(f"{skill}: an include directive survived expansion")

    m = re.search(r"^name:\s*(\S+)\s*$", rendered, re.M)
    if not m or m.group(1) != skill:
        raise BuildError(
            f"{skill}: frontmatter name does not match the source filename"
        )
    return skill, rendered


def targets(skill: str) -> list[Path]:
    return [tree / skill / "SKILL.md" for tree in TREES]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument(
        "--check",
        action="store_true",
        help="verify the shipped files match the source; do not write",
    )
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass

    if not SKILL_SRC.exists():
        print(f"error: {SKILL_SRC} not found", file=sys.stderr)
        return 2

    bindings = json.loads(BINDINGS.read_text(encoding="utf-8")) if BINDINGS.exists() else {}
    sources = sorted(SKILL_SRC.glob("*.md"))
    unknown_skills = set(bindings) - {p.stem for p in sources}
    if unknown_skills:
        print(
            f"FAIL: bindings.json names skill(s) with no source: "
            f"{', '.join(sorted(unknown_skills))}"
        )
        return 1

    stale: list[str] = []
    written = 0
    for src in sources:
        try:
            skill, rendered = build_skill(src, bindings)
        except BuildError as e:
            print(f"FAIL: {e}")
            return 1

        for target in targets(skill):
            current = target.read_text(encoding="utf-8") if target.exists() else None
            if current == rendered:
                continue
            if args.check:
                stale.append(str(target.relative_to(REPO)))
                diff = difflib.unified_diff(
                    (current or "").splitlines(),
                    rendered.splitlines(),
                    fromfile=f"{target.relative_to(REPO)} (on disk)",
                    tofile=f"library/skills/{skill}.md (source)",
                    lineterm="",
                    n=1,
                )
                for line in list(diff)[:40]:
                    print(f"  {line}")
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(rendered, encoding="utf-8", newline="\n")
                written += 1

    if args.check:
        if stale:
            print(
                f"\nFAIL: {len(stale)} shipped file(s) do not match "
                f"library/ — SKILL.md is generated; edit the source and rebuild:\n"
                f"  python scripts/build-skills.py"
            )
            return 1
        print(f"{len(sources)} skills — shipped files match library/")
        return 0

    print(f"{len(sources)} skills — wrote {written} file(s) across {len(TREES)} trees")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Scorer for the investigate-journalism-skills eval harness.

Three measurements, all mechanical:

  conformance     Does one run's output match the skill's own declared output
                  template, warrant discipline, and Rule 10 voice?
  reproducibility Do N runs of the same item agree on the verdict label?
  symmetry        Do two prior-inverted runs converge on sources and verdict?

Design rule: expectations are derived from the SKILL.md files at runtime, not
hardcoded. When a skill's output template changes, the scorer follows it. Only
genuinely non-derivable facts (verdict vocabularies, explicitly-optional
sections) live in this file, each with a pointer to the SKILL.md text that
establishes it.

No third-party dependencies. Python 3.9+.

Usage:
    python evals/score.py conformance RUN.md --skill peer-review
    python evals/score.py reproducibility evals/runs/item-id/
    python evals/score.py symmetry RUN_A.md RUN_B.md --skill investigative-reasoning
    python evals/score.py selftest
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / ".claude" / "skills"

# --------------------------------------------------------------------------
# Non-derivable configuration. Each entry cites the SKILL.md text behind it.
# --------------------------------------------------------------------------

# Skills that do not emit a report-shaped output and are excluded from
# conformance scoring.
#   publisher-nl    emits a Dutch article ("## Article Shape"), not a report
#   intuitive-thinking  emits a "## Micro-Template" hunch register, not a report
NON_REPORT_SKILLS = {"publisher-nl", "intuitive-thinking"}

# Sections a skill's own text declares optional. Without this, conformance
# would fail runs that the skill explicitly permits.
OPTIONAL_SECTIONS = {
    # first-principles-thinking: "Closing sections (What Would Change This /
    # Self-Audit / Limits) may be omitted when they add no signal"
    "first-principles-thinking": {
        "What Would Change This",
        "Self-Audit",
        "Limits of This Analysis",
        "Sources & Warrants",  # "Include only when empirical Bedrock ... invoked"
    },
    # fallacy-...: "Sources & Warrants [Include only when empirical evidence or
    # outside sources were invoked.]"
    "fallacy-bias-and-manipulation-analysis": {"Sources & Warrants"},
}

# Verdict vocabularies, quoted from each skill's own verdict table. The list
# order is the ordinal spine used for "adjacent" agreement; labels after the
# ``|`` marker are off-spine (no meaningful distance to their neighbours).
VERDICT_SPINE = {
    "peer-review": (
        ["Accept", "Minor", "Major", "Reject-resubmit", "Reject"],
        [],
    ),
    "journalistic-article-review": (
        [
            "Reliable as reported",
            "Mostly reliable with caveats",
            "Mixed",
            "Misleading",
            "Unsupported",
            "Contradicted",
        ],
        [],
    ),
    "scientific-fact-classification": (
        [
            "Established fact",
            "Well-supported finding",
            "Provisionally accepted",
            "Contested",
            "Weak / preliminary",
            "Conjecture",
            "Likely false",
            "Refuted",
        ],
        ["Load-bearing assumption", "Opinion / value claim", "Unfalsifiable"],
    ),
    "belief-revision": (
        ["Confirmed", "Refined", "Shifted", "Overturned"],
        ["Suspended"],
    ),
    "first-principles-thinking": (["Confirmed", "Refined", "Overturned"], []),
    "investigative-reasoning": (
        ["Hypothesis A stronger", "undecidable", "Hypothesis B stronger"],
        [],
    ),
    "fallacy-bias-and-manipulation-analysis": (
        ["argument stands", "partly stands", "collapses"],
        [],
    ),
    # osint-research's Output block specifies a free-text verdict
    # ("[one-line - what the evidence supports / does not support]") with no
    # fixed vocabulary. Conformance and warrant checks still apply.
    "osint-research": ([], []),
}

# Surface forms a run may use for a spine label, as (pattern, canonical).
#
# The spine is quoted from each skill's own verdict vocabulary, but a run writes
# prose, not vocabulary. investigative-reasoning is where the gap bites: the
# template offers "Hypothesis A stronger", and both S1 runs instead opened the
# verdict with the hypothesis and then named it — "Hypothesis A (a
# Ukrainian-organized operative team ...)". Both scored None and had to be read
# by hand, which is what blocked S1 from being scored mechanically.
#
# Aliases are anchored deliberately. Every investigation report names both
# hypotheses many times, including on the verdict line, so a bare
# "Hypothesis B" mention must not be able to claim the verdict away from
# "Hypothesis A". An alias fires only at the head of the verdict value, or on
# an explicit comparative ("Hypothesis B is better supported").
# A hypothesis, however the run abbreviates it: "Hypothesis A", "H-A", "H_A".
_HYP = r"(?:Hypothesis\s+|H[-_‑])%s\b"

# Comparative verdict vocabulary. "better" is deliberately required to carry an
# evidential complement — a bare "better" appears in ordinary prose ("Hypothesis
# B explains the timing anomaly better") and must not read as a verdict.
_COMP = (
    r"(?:strong(?:er|est)"
    r"|better[- ](?:evidenced|supported|attested|corroborated|documented|sourced)"
    r"|more strongly (?:supported|evidenced)"
    r"|carries the evidence)"
)

# Phrasings that decline to choose. Checked on the same earliest-position rule,
# so a verdict that opens by refusing the choice beats a hypothesis named later.
_UNDECIDABLE = (
    r"(?:insufficient to favou?r either"
    r"|(?:does not support|insufficient to) (?:reach(?:ing)?|render(?:ing)?) a confident verdict"
    r"|no confident verdict"
    r"|neither hypothesis is"
    r"|evidence is insufficient"
    r"|cannot be resolved on"
    r"|contested between"
    r"|undecidable)"
)

VERDICT_ALIASES: dict[str, list[tuple[str, str]]] = {
    "investigative-reasoning": [
        # Head of the verdict value: "Hypothesis A (a Ukrainian team) is ..."
        (r"^\W*" + _HYP % "A", "Hypothesis A stronger"),
        (r"^\W*" + _HYP % "B", "Hypothesis B stronger"),
        # Comparative anywhere: the run names a hypothesis, then rates it. The
        # window is wide because runs park a long parenthetical gloss between
        # the two ("Hypothesis A (a Ukrainian-organized operative team, run
        # through a military chain of command) is substantially better
        # evidenced than Hypothesis B"). It stops at a sentence boundary.
        (_HYP % "A" + r"[^.\n]{0,200}?\b" + _COMP + r"\b", "Hypothesis A stronger"),
        (_HYP % "B" + r"[^.\n]{0,200}?\b" + _COMP + r"\b", "Hypothesis B stronger"),
        (r"\b" + _UNDECIDABLE + r"\b", "undecidable"),
    ],
}

# The six project warrant labels (CLAUDE.md "Core rule").
WARRANT_LABELS = [
    "(traced)",
    "(deferred to consensus)",
    "(deferred, fragile)",
    "(memory — unverified)",
    "(user-supplied — unverified)",
    "(intuition — unwarranted)",
]

# Rule 10: no requester references in report prose. The warrant label
# "(user-supplied - unverified)" legitimately contains "user" and is excluded.
REQUESTER_PATTERNS = [
    r"\bthe user\b",
    r"\bthe requester\b",
    r"\byou asked\b",
    r"\byour question\b",
    r"\bas you (?:noted|said|pointed out|mentioned)\b",
    r"\bde gebruiker\b",
    r"\bu (?:heeft|hebt) gelijk\b",
    r"\bzoals u\b",
]
RULE10_EXEMPT = re.compile(r"\(user-supplied\s*[-—]\s*unverified\)", re.I)

URL_RE = re.compile(r"https?://\S+")
DATE_RE = re.compile(
    r"\b(?:\d{4}-\d{2}-\d{2}|\d{1,2}[-/]\d{1,2}[-/]\d{4}|"
    r"\d{1,2}\s+\w+\s+\d{4}|\w+\s+\d{1,2},?\s+\d{4})\b"
)


# --------------------------------------------------------------------------
# Skill introspection
# --------------------------------------------------------------------------


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def skill_path(skill: str) -> Path:
    p = SKILLS_DIR / skill / "SKILL.md"
    if not p.exists():
        raise SystemExit(f"error: no such skill: {skill} (looked in {p})")
    return p


def list_skills() -> list[str]:
    return sorted(p.name for p in SKILLS_DIR.iterdir() if (p / "SKILL.md").exists())


FENCE_RE = re.compile(r"^\s*```")


def scan_fences(text: str):
    """Yield (line, inside_fence, fence_lang) for each line.

    Section boundaries and headings must be detected outside fenced blocks:
    the output templates are themselves fenced markdown containing "## "
    headings, which would otherwise terminate the section early.
    """
    inside = False
    lang = ""
    for line in text.splitlines():
        if FENCE_RE.match(line):
            if inside:
                yield line, True, lang
                inside, lang = False, ""
            else:
                inside = True
                lang = line.strip().lstrip("`").strip()
                yield line, True, lang
            continue
        yield line, inside, lang


def section_lines(text: str, heading: str) -> list[tuple[str, bool, str]]:
    """Lines of the named level-2 section, fence-aware."""
    out: list[tuple[str, bool, str]] = []
    collecting = False
    want = re.compile(rf"^##\s+{re.escape(heading)}\s*$")
    for line, inside, lang in scan_fences(text):
        if not inside and re.match(r"^##\s+", line):
            if want.match(line):
                collecting = True
                continue
            if collecting:
                break
        if collecting:
            out.append((line, inside, lang))
    return out


def extract_output_templates(skill: str) -> list[list[str]]:
    """Return one heading-list per fenced template in the skill's Output section.

    A run conforms if it matches ANY template. journalistic-article-review
    declares two (the Phase -1 retrieval-failure stop output, and the normal
    review output); a retrieval-failure stop is a legitimate outcome.
    """
    text = read_text(skill_path(skill))
    templates: list[list[str]] = []
    current: list[str] | None = None
    for line, inside, lang in section_lines(text, "Output"):
        if FENCE_RE.match(line):
            if lang.startswith("markdown") and current is None:
                current = []
            elif current is not None:
                if current:
                    templates.append(current)
                current = None
            continue
        if current is not None:
            m = re.match(r"^##\s+(.+?)\s*$", line)
            if m:
                current.append(m.group(1).strip())
    if current:
        templates.append(current)
    return templates


# --------------------------------------------------------------------------
# Conformance
# --------------------------------------------------------------------------


def present_headings(output: str) -> list[str]:
    """Level-2 headings in a run, ignoring any inside fenced blocks."""
    found = []
    for line, inside, _ in scan_fences(output):
        if inside:
            continue
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            found.append(m.group(1).strip())
    return found


def score_conformance(output: str, skill: str) -> dict:
    result: dict = {"skill": skill, "checks": {}, "failures": []}

    if skill in NON_REPORT_SKILLS:
        result["checks"]["sections"] = "skipped (not a report-shaped skill)"
    else:
        templates = extract_output_templates(skill)
        if not templates:
            result["failures"].append(
                f"could not extract an output template from {skill}/SKILL.md"
            )
        else:
            optional = OPTIONAL_SECTIONS.get(skill, set())
            found = set(present_headings(output))
            best = None
            for tpl in templates:
                required = [h for h in tpl if h not in optional]
                missing = [h for h in required if h not in found]
                score = len(required) - len(missing)
                if best is None or score > best[0]:
                    best = (score, required, missing)
            _, required, missing = best
            result["checks"]["sections"] = (
                f"{len(required) - len(missing)}/{len(required)} required sections"
            )
            for h in missing:
                result["failures"].append(f"missing required section: ## {h}")

    # A Phase -1 retrieval-failure stop asserts nothing, so the claim-level
    # checks below (warrant labels, traced discipline, self-audit) do not
    # apply to it. Its correctness is entirely "did it stop and say so".
    h1 = re.match(r"^#\s+(.+?)\s*$", output.lstrip(), re.M)
    is_stop_output = bool(h1 and re.match(r"Review Stopped\b", h1.group(1), re.I))
    result["checks"]["output_kind"] = "retrieval-failure stop" if is_stop_output else "report"
    if is_stop_output:
        result["pass"] = not result["failures"]
        return result

    # Warrant labels present at all.
    used = [lbl for lbl in WARRANT_LABELS if lbl in output]
    result["checks"]["warrant_labels_used"] = used
    if not used:
        result["failures"].append(
            "no warrant labels anywhere in output (CLAUDE.md core rule)"
        )

    # (traced) discipline. CLAUDE.md requires "URL + access date stated", but
    # the URL normally lives in the Sources & Warrants row, not inline beside
    # every use. So the hard failure is document-level; the inline count is
    # advisory only, to avoid flooding a conforming report with false hits.
    traced_lines = [
        i for i, ln in enumerate(output.splitlines(), 1) if "(traced" in ln
    ]
    urls = URL_RE.findall(output)
    result["checks"]["traced_claims"] = len(traced_lines)
    result["checks"]["urls_in_document"] = len(urls)
    result["checks"]["traced_lines_without_inline_url"] = sum(
        1 for i, ln in enumerate(output.splitlines(), 1)
        if "(traced" in ln and not URL_RE.search(ln)
    )
    if traced_lines and not urls:
        result["failures"].append(
            f"(traced) used {len(traced_lines)}x but the document contains no URL "
            "at all — the claims are unverifiable"
        )
    if traced_lines and not DATE_RE.search(output):
        result["failures"].append("(traced) used but no access date found anywhere")
    # A Sources & Warrants table is where URL + access date are recorded.
    if traced_lines and not any(
        re.search(r"sources?\s*(&|and)\s*warrants?", h, re.I)
        for h in present_headings(output)
    ):
        result["failures"].append(
            "(traced) used but no 'Sources & Warrants' section to record URL + access date"
        )

    # Rule 10: requester references in prose.
    hits = []
    for i, line in enumerate(output.splitlines(), 1):
        if RULE10_EXEMPT.search(line):
            continue
        for pat in REQUESTER_PATTERNS:
            if re.search(pat, line, re.I):
                hits.append((i, line.strip()[:70]))
                break
    result["checks"]["rule10_violations"] = len(hits)
    for ln, snippet in hits[:5]:
        result["failures"].append(f"Rule 10 requester reference at line {ln}: {snippet}")

    # Self-audit symmetry answer must name specifics, not merely assert.
    # investigative-reasoning: "Asserting 'I would have reached the same
    # verdict, full stop' without phase-level identification is itself a red flag"
    audit = section_lines(output, "Self-Audit")
    if audit:
        block = "\n".join(ln for ln, _, _ in audit)
        specific = bool(
            re.search(r"\bPhase\s+\d|\bC\d\b|\bTier\s*\d|\bsection\b", block, re.I)
        )
        result["checks"]["self_audit_specific"] = specific
        if not specific and len(block.split()) < 40:
            result["failures"].append(
                "Self-Audit asserts symmetry without naming phases/claims (bare assertion)"
            )
    elif skill not in NON_REPORT_SKILLS:
        result["checks"]["self_audit_specific"] = False

    if skill == "peer-review":
        _check_severity_binding(output, result)

    result["pass"] = not result["failures"]
    return result


# Severity-vs-recommendation coherence.
#
# This was briefly a hard rule in peer-review Phase 7 and is now REVERTED, so it
# is reported as a diagnostic and never fails a run — the scorer must not enforce
# a rule the library does not state.
#
# History, both measured 2026-08-10: with no binding, three of five R1 runs
# carried two Major findings each and recommended Minor revision, Accept, and
# Accept. With the binding, Major findings across five runs went 6 -> 0 and the
# same fault was regraded down ("Ambiguity in patient-to-genome mapping" Major ->
# "Incomplete patient-to-sample-to-genome traceability" Minor). The floor was
# satisfied by suppressing findings rather than by raising recommendations, which
# is worse: the mismatch was at least visible, the suppression is not.
#
# Keep measuring it. A rise in this number is the signal that the reverted rule,
# or any replacement, is needed; a fall accompanied by falling Major counts is
# the signal that a replacement is backfiring the same way.
SEVERITY_FLOOR = {"Fatal": "Reject-resubmit", "Major": "Major", "Minor": "Minor"}


def _populated_findings(output: str, severity: str) -> int:
    """Count findings under a severity heading, treating 'None' as empty."""
    lines = section_lines(output, f"{severity} Findings")
    if not lines:
        return 0
    body = "\n".join(ln for ln, _, _ in lines).strip()
    if not body or re.match(r"^(none|n/?a|—|-)\b", body, re.I):
        return 0
    items = re.findall(r"^\s*(?:\*\*(?:Finding\s+)?\d+|\d+\.|[-*]\s+\*\*)", body, re.M)
    return len(items) or 1


def _check_severity_binding(output: str, result: dict) -> None:
    spine, _ = VERDICT_SPINE["peer-review"]
    rec = extract_verdict(output, "peer-review")
    counts = {s: _populated_findings(output, s) for s in SEVERITY_FLOOR}
    result["checks"]["findings_by_severity"] = counts

    highest = next((s for s in ("Fatal", "Major", "Minor") if counts[s]), None)
    if not highest:
        return
    floor = SEVERITY_FLOOR[highest]
    result["checks"]["recommendation_floor"] = floor
    # Diagnostic only — see the SEVERITY_FLOOR note. Never appended to failures.
    if rec is None:
        result["checks"]["severity_coherence"] = "unknown (no recommendation extracted)"
    elif spine.index(rec) < spine.index(floor):
        result["checks"]["severity_coherence"] = (
            f"below floor: '{rec}' with {counts[highest]} {highest} finding(s) "
            f"implying '{floor}'"
        )
    else:
        result["checks"]["severity_coherence"] = "coherent"


# --------------------------------------------------------------------------
# Verdict extraction
# --------------------------------------------------------------------------


def first_label(
    text: str,
    vocab: list[str],
    aliases: Iterable[tuple[str, str]] = (),
) -> str | None:
    """The label a passage asserts: earliest by position, longest on a tie.

    Verdict lines routinely name more than one label — a peer review that lands
    on Minor while saying it "would have been Accept", a classification that
    calls the claim as submitted one thing and an explicitly narrower variant
    another. The asserted verdict is the one stated first; resolving by label
    length instead makes the longer label win regardless of which is being
    claimed. The length tie-break still matters for prefixes, so that
    "Reject-resubmit" is not read as "Reject".

    `aliases` are (pattern, canonical) surface forms per VERDICT_ALIASES. They
    compete on the same earliest-position rule, and the length tie-break is on
    the matched span, so a literal spine label beats an alias that starts at the
    same offset — "Hypothesis A stronger" resolves as itself, not via the
    shorter "Hypothesis A" alias.
    """
    hits = []
    for label in vocab:
        m = re.search(re.escape(label), text, re.I)
        if m:
            hits.append((m.start(), -(m.end() - m.start()), label))
    for pattern, canonical in aliases:
        m = re.search(pattern, text, re.I)
        if m:
            hits.append((m.start(), -(m.end() - m.start()), canonical))
    return min(hits)[2] if hits else None


# Strips the "**Verdict:**" / "- **Recommendation:**" prefix so an anchored
# alias sees the head of the *value*, not the head of the line.
VERDICT_MARKER_RE = re.compile(
    r"^\s*[-*]?\s*\*\*(?:Verdict|Recommendation|Status|Classification)[^:]*:?\*\*\s*:?\s*",
    re.I,
)


def extract_verdict(output: str, skill: str) -> str | None:
    spine, off_spine = VERDICT_SPINE.get(skill, ([], []))
    vocab = spine + off_spine
    if not vocab:
        return None
    aliases = VERDICT_ALIASES.get(skill, [])

    # Prefer an explicit "Verdict:" / "Recommendation:" / "Status:" line.
    lines = [
        ln
        for ln in output.splitlines()
        if re.search(r"^\s*[-*]?\s*\*\*(?:Verdict|Recommendation|Status|Classification)", ln, re.I)
    ]
    for line in lines:
        label = first_label(VERDICT_MARKER_RE.sub("", line), vocab, aliases)
        if label:
            return label
    # Fall back to the Summary block. Head-anchored aliases are dropped here:
    # the anchor means "head of the verdict value", and a Summary block has no
    # such position — applying them to an arbitrary line would let any sentence
    # opening with "Hypothesis A" claim the verdict.
    summary = "\n".join(ln for ln, _, _ in section_lines(output, "Summary"))
    if summary:
        unanchored = [(p, c) for p, c in aliases if not p.startswith("^")]
        return first_label(summary, vocab, unanchored)
    return None


# --------------------------------------------------------------------------
# Catalogue reach
# --------------------------------------------------------------------------

# Long lookup tables are the obvious candidates to move into references/ under
# progressive disclosure, and moving them is the one restructuring step that
# could quietly cost detection: the 2026-08-10 ethics-row result showed a single
# checklist row moving detection from 2/5 runs to 5/5 purely by being present.
#
# So measure reach before moving. Entries are derived from the SKILL.md section
# at runtime, per this file's design rule -- if the table is later moved to a
# reference file, point the locator there and the same numbers stay comparable.
CATALOGUES = {
    # investigative-reasoning Phase 2e: 18 rows, "| 1 | **False Flag** | ..."
    "io-patterns": (
        "investigative-reasoning",
        r"###\s+2e\s+.*Influence-Operation",
        r"^---\s*$",
    ),
    # fallacy-...: the taxonomy proper, Phase 2 (formal) through Phase 8
    # (discourse-structural). Phase 9 grades what those phases found, so it is
    # the boundary.
    "fallacies": (
        "fallacy-bias-and-manipulation-analysis",
        r"##\s+Phase 2\s+.*Formal Fallacies",
        r"^##\s+Phase 9\b",
    ),
}

BOLD_CELL_RE = re.compile(r"\*\*(.+?)\*\*")
# "**4a. Belief-formation.** Confirmation - disconfirmation - ..." : the label is
# not an entry, so it comes off before the list is split.
LIST_LABEL_RE = re.compile(r"^\*\*[^*]+\*\*\s*")
COLUMN_HEADERS = {
    "fallacy", "signal", "pattern", "technique", "description", "schema",
    "quick test", "concern", "effect", "bias", "mechanism", "mitigation",
    "category", "key questions", "source", "trust", "tier", "evidence type",
}


def catalogue_entries(name: str) -> tuple[str, list[str]]:
    """Entry names in a skill's lookup table, read from the SKILL.md.

    Derived at runtime rather than hardcoded, per this file's design rule. If a
    table moves to a reference file, repoint the locator and the numbers stay
    comparable across the move -- which is the whole purpose of the measurement.
    """
    if name not in CATALOGUES:
        raise SystemExit(
            f"error: unknown catalogue {name!r} (have: {', '.join(CATALOGUES)})"
        )
    skill, start_re, stop_re = CATALOGUES[name]
    text = read_text(SKILLS_DIR / skill / "SKILL.md")
    m = re.search(start_re, text)
    if not m:
        raise SystemExit(f"error: catalogue section for {name!r} not found in {skill}")
    rest = text[m.end():]
    stop = re.search(stop_re, rest, re.M)
    body = rest[: stop.start()] if stop else rest

    entries: set[str] = set()
    for raw in body.splitlines():
        line = raw.strip()
        if line.startswith("|") and set(line) - set("|-: "):
            cells = [c.strip() for c in line.strip("|").split("|")]
            # In every one of these tables the entry name is the first column,
            # except where that column is a row number. Reading further right
            # picks up the "Signal" or "Description" column as if it were an
            # entry ("Attack person, not argument"), which inflates the count
            # and makes the reach denominator meaningless.
            cell = cells[0] if cells and not cells[0].isdigit() else (
                cells[1] if len(cells) > 1 else ""
            )
            bold = BOLD_CELL_RE.findall(cell)
            if bold:
                entries.update(b.strip() for b in bold)
            else:
                cell = re.sub(r"\(.*?\)", "", cell).strip()
                if cell and 1 <= len(cell.split()) <= 6:
                    entries.add(cell)
        elif "·" in line:
            for part in LIST_LABEL_RE.sub("", line).split("·"):
                part = re.sub(r"\(.*?\)", "", part).strip(" *.·")
                if part and 1 <= len(part.split()) <= 6:
                    entries.add(part)

    cleaned = {
        e for e in entries
        if len(e) > 3 and e.lower() not in COLUMN_HEADERS and not e.startswith("#")
    }
    return skill, sorted(cleaned)


def score_catalogue(path: Path, name: str) -> dict:
    output = read_text(path)
    low = output.lower()
    skill, entries = catalogue_entries(name)
    named = [e for e in entries if e.lower() in low]
    return {
        "run": str(path),
        "catalogue": name,
        "source_skill": skill,
        "entries_in_catalogue": len(entries),
        "entries_named": len(named),
        "reach": round(len(named) / len(entries), 3) if entries else 0.0,
        "named": named,
    }


# --------------------------------------------------------------------------
# Severity counts
# --------------------------------------------------------------------------

# Findings-per-severity is the number that caught the reverted severity floor
# (Majors 6 -> 0) and the number that flagged the 2026-08-10 post-merge drop
# (6 -> 1). Until now it was counted by hand with ad-hoc greps, which got it
# wrong twice in one session -- once matching the section headings themselves,
# once missing the "**1. Title**" entry format. It belongs in the scorer.
SEVERITIES = ("Fatal", "Major", "Minor")

# The entry shapes runs actually use under a severity heading. The first pattern
# takes an optional word before the ordinal: runs write "**1. Title**" and
# "**Finding 1 - Title.**" interchangeably, and a counter that knows only the
# first reads a 3186-character section as empty. That is not hypothetical -- it
# under-counted the 2026-08-10 baseline by two Majors on exactly this format,
# which is why the shapes are enumerated from real runs rather than guessed.
ENTRY_PATTERNS = (
    r"^\*\*(?:[A-Za-z]+\s+)?\d+\s*[.—:)-]",  # **1. X** / **Finding 1 - X**
    r"^###\s+",                                    # ### X
    r"^\s*[-*]\s+\*\*",                            # - **X**
)
# A section that explicitly reports nothing. Counted as 0, not as unparseable,
# so an empty section and an absent one stay distinguishable.
NONE_RE = re.compile(r"^\s*None identified", re.I | re.M)


def severity_counts(output: str) -> dict:
    counts: dict[str, int | None] = {}
    for sev in SEVERITIES:
        m = re.search(rf"^##\s+{sev} Findings\s*$", output, re.M)
        if not m:
            counts[sev] = None  # section absent from this report
            continue
        nxt = re.search(r"^##\s+", output[m.end():], re.M)
        body = output[m.end(): m.end() + nxt.start()] if nxt else output[m.end():]
        if not body.strip() or NONE_RE.search(body):
            counts[sev] = 0
            continue
        n = 0
        for pat in ENTRY_PATTERNS:
            n = len(re.findall(pat, body, re.M))
            if n:
                break
        counts[sev] = n
    return counts


def score_severity(paths: list[Path]) -> dict:
    per_run = {}
    totals = {s: 0 for s in SEVERITIES}
    with_any = {s: 0 for s in SEVERITIES}
    for p in paths:
        c = severity_counts(read_text(p))
        per_run[p.name] = c
        for s in SEVERITIES:
            if c[s]:
                totals[s] += c[s]
                with_any[s] += 1
    n = len(paths)
    return {
        "runs": n,
        "per_run": per_run,
        "totals": totals,
        "runs_with_any": with_any,
        "share_of_runs": {
            s: round(with_any[s] / n, 3) if n else 0.0 for s in SEVERITIES
        },
        "note": (
            "null means the report has no section with that heading; 0 means the "
            "section exists and reports none"
        ),
        "reading": (
            "share_of_runs is the stabler comparison. A total is dominated by "
            "whichever single run decides to grade at all -- across the four R1 "
            "builds measured 2026-08-10, Majors were concentrated in one or two "
            "runs each time, so a 3-vs-1 difference in totals was one run "
            "changing its mind. The share moves only when the number of runs "
            "finding anything changes."
        ),
    }


# --------------------------------------------------------------------------
# Fault detection
# --------------------------------------------------------------------------

FAULTS_PATH = Path(__file__).resolve().parent / "faults.json"


def findings_text(output: str) -> str:
    """Only the Fatal/Major/Minor Findings sections."""
    parts = []
    for sev in SEVERITIES:
        m = re.search(rf"^##\s+{sev} Findings\s*$", output, re.M)
        if not m:
            continue
        nxt = re.search(r"^##\s+", output[m.end():], re.M)
        parts.append(output[m.end(): m.end() + nxt.start()] if nxt else output[m.end():])
    return "\n".join(parts)


def score_detection(paths: list[Path], item: str) -> dict:
    """Which known faults each run found — the measure severity counts hide.

    Severity grading is a judgement a single run can swing; whether a review
    *noticed* a fault is closer to a fact. Measured 2026-08-10, the ethics row
    moved detection 2/5 -> 5/5 (large, visible at n=5) while every severity
    comparison over the same runs separated nothing.
    """
    catalogue = json.loads(read_text(FAULTS_PATH))
    if item not in catalogue:
        known = [k for k in catalogue if not k.startswith("_")]
        raise SystemExit(f"error: no fault catalogue for {item!r} (have: {known})")
    faults = catalogue[item]["faults"]

    per_fault = {}
    for name, spec in faults.items():
        rx = re.compile(spec["pattern"])
        mentioned = [p.name for p in paths if rx.search(read_text(p))]
        as_finding = [p.name for p in paths if rx.search(findings_text(read_text(p)))]
        per_fault[name] = {
            "description": spec["description"],
            "mentioned": len(mentioned),
            "as_finding": len(as_finding),
            "mention_rate": round(len(mentioned) / len(paths), 3) if paths else 0.0,
            "finding_rate": round(len(as_finding) / len(paths), 3) if paths else 0.0,
        }
    return {
        "item": item,
        "runs": len(paths),
        "paper": catalogue[item].get("paper"),
        "per_fault": per_fault,
        "mean_mention_rate": round(
            sum(f["mention_rate"] for f in per_fault.values()) / len(per_fault), 3
        ),
        "mean_finding_rate": round(
            sum(f["finding_rate"] for f in per_fault.values()) / len(per_fault), 3
        ),
    }


ANSWERS_PATH = Path(__file__).resolve().parent / "answers.json"


def score_answers(paths: list[Path], item: str) -> dict:
    """Objective answer key: did the run state the right answer, the wrong one, or none?

    Unlike severity, the ground truth here needs no judgement — each question is
    verifiable from the paper's own text. Unlike detection on R1, expected
    accuracy sits near 1.0 rather than ~0.35, which is where a regression becomes
    visible at n=5 instead of drowning in one run's discretion.
    """
    catalogue = json.loads(read_text(ANSWERS_PATH))
    if item not in catalogue:
        known = [k for k in catalogue if not k.startswith("_")]
        raise SystemExit(f"error: no answer key for {item!r} (have: {known})")
    questions = catalogue[item]["questions"]

    per_q = {}
    for name, spec in questions.items():
        ok = re.compile(spec["correct"])
        bad = re.compile(spec["incorrect"]) if spec.get("incorrect") else None
        correct = wrong = 0
        for p in paths:
            text = read_text(p)
            hit_ok = bool(ok.search(text))
            hit_bad = bool(bad.search(text)) if bad else False
            # A run asserting both is counted correct: reviews often quote the
            # paper's own framing before contradicting it, and the key's answer
            # appearing at all is the thing being measured.
            if hit_ok:
                correct += 1
            elif hit_bad:
                wrong += 1
        per_q[name] = {
            "question": spec["question"],
            "correct": correct,
            "incorrect": wrong,
            "unaddressed": len(paths) - correct - wrong,
            "accuracy": round(correct / len(paths), 3) if paths else 0.0,
        }
    n = len(per_q)
    return {
        "item": item,
        "runs": len(paths),
        "paper": catalogue[item].get("paper"),
        "per_question": per_q,
        "mean_accuracy": round(sum(q["accuracy"] for q in per_q.values()) / n, 3),
        "mean_addressed": round(
            sum((q["correct"] + q["incorrect"]) / len(paths) for q in per_q.values()) / n, 3
        ) if paths else 0.0,
    }


def verdict_distance(skill: str, a: str, b: str) -> int | None:
    spine, _ = VERDICT_SPINE.get(skill, ([], []))
    if a in spine and b in spine:
        return abs(spine.index(a) - spine.index(b))
    return None  # off-spine: no meaningful distance


# --------------------------------------------------------------------------
# Reproducibility
# --------------------------------------------------------------------------


def score_reproducibility(run_dir: Path, skill: str | None) -> dict:
    runs = sorted(run_dir.glob("*.md"))
    if len(runs) < 2:
        raise SystemExit(
            f"error: reproducibility needs >=2 runs in {run_dir} (found {len(runs)})"
        )
    skill = skill or infer_skill(read_text(runs[0]))
    verdicts = {}
    for r in runs:
        verdicts[r.name] = extract_verdict(read_text(r), skill)

    found = [v for v in verdicts.values() if v]
    counts = Counter(found)
    modal, modal_n = (counts.most_common(1)[0] if counts else (None, 0))
    exact = modal_n / len(runs) if runs else 0.0

    adjacent_n = 0
    if modal:
        for v in found:
            d = verdict_distance(skill, v, modal)
            if v == modal or (d is not None and d <= 1):
                adjacent_n += 1
    adjacent = adjacent_n / len(runs) if runs else 0.0

    return {
        "skill": skill,
        "runs": len(runs),
        "verdicts": verdicts,
        "unextracted": sum(1 for v in verdicts.values() if v is None),
        "modal_verdict": modal,
        "exact_agreement": round(exact, 3),
        "adjacent_agreement": round(adjacent, 3),
    }


# --------------------------------------------------------------------------
# Symmetry (prior-inverted pair)
# --------------------------------------------------------------------------


def cited_urls(output: str) -> set[str]:
    urls = set()
    for u in URL_RE.findall(output):
        u = u.rstrip(").,;>|—-")
        # Normalise: strip scheme, trailing slash, and query string.
        u = re.sub(r"^https?://(?:www\.)?", "", u).rstrip("/").split("?")[0]
        urls.add(u.lower())
    return urls


def score_symmetry(path_a: Path, path_b: Path, skill: str | None) -> dict:
    a, b = read_text(path_a), read_text(path_b)
    skill = skill or infer_skill(a)
    ua, ub = cited_urls(a), cited_urls(b)
    union = ua | ub
    overlap = len(ua & ub) / len(union) if union else 0.0

    va, vb = extract_verdict(a, skill), extract_verdict(b, skill)
    dist = verdict_distance(skill, va, vb) if va and vb else None

    # symmetric-adversarial-test.md pass criterion: >=90% overlap in cited
    # primary sources, and verdict divergence no greater than the source diff
    # warrants.
    return {
        "skill": skill,
        "verdict_a": va,
        "verdict_b": vb,
        "verdict_distance": dist,
        "verdicts_agree": va == vb if (va and vb) else None,
        "sources_a": len(ua),
        "sources_b": len(ub),
        "shared_sources": len(ua & ub),
        "source_overlap": round(overlap, 3),
        "only_in_a": sorted(ua - ub)[:15],
        "only_in_b": sorted(ub - ua)[:15],
        "meets_90pct_overlap": overlap >= 0.90,
    }


def infer_skill(output: str) -> str:
    """Guess the skill from the output's H1, which the templates fix."""
    m = re.search(r"^#\s+(.+?)\s*$", output, re.M)
    head = (m.group(1) if m else "").lower()
    for needle, skill in [
        ("peer review", "peer-review"),
        ("journalistic article review", "journalistic-article-review"),
        ("review stopped", "journalistic-article-review"),
        ("claim classification", "scientific-fact-classification"),
        ("event investigation", "investigative-reasoning"),
        ("belief revision", "belief-revision"),
        ("first principles analysis", "first-principles-thinking"),
        ("fallacy & bias audit", "fallacy-bias-and-manipulation-analysis"),
        ("osint brief", "osint-research"),
    ]:
        if needle in head:
            return skill
    raise SystemExit(
        "error: could not infer skill from output H1; pass --skill explicitly"
    )


# --------------------------------------------------------------------------
# Self-test: the scorer's own regression check
# --------------------------------------------------------------------------


def selftest() -> int:
    failures = []

    skills = list_skills()
    if len(skills) < 10:
        failures.append(f"expected >=10 skills, found {len(skills)}")

    # Every report-shaped skill must yield at least one output template.
    for s in skills:
        if s in NON_REPORT_SKILLS:
            continue
        if not extract_output_templates(s):
            failures.append(f"no output template extracted for {s}")

    # Every skill named in VERDICT_SPINE / OPTIONAL_SECTIONS must exist.
    for s in set(VERDICT_SPINE) | set(OPTIONAL_SECTIONS) | NON_REPORT_SKILLS:
        if s not in skills:
            failures.append(f"config references unknown skill: {s}")

    # Verdict extraction round-trip.
    sample = (
        "# Peer Review: X\n\n## Summary\n- **Recommendation:** Major\n\n"
        "## Self-Audit\n- Symmetry test: Phase 3 CoI thresholds are where it turns.\n"
    )
    if extract_verdict(sample, "peer-review") != "Major":
        failures.append("verdict extraction failed on peer-review sample")

    # investigative-reasoning verdict aliases. The first case is the S1 form
    # that scored None and had to be read by hand; the rest guard the anchor.
    ir_cases = [
        (
            "- **Verdict:** Hypothesis A (a Ukrainian-organized operative team) "
            "is the better-supported account.",
            "Hypothesis A stronger",
        ),
        ("- **Verdict:** Hypothesis B stronger", "Hypothesis B stronger"),
        (
            "- **Verdict:** Hypothesis A stronger; Hypothesis B is not supported.",
            "Hypothesis A stronger",
        ),
        (
            "- **Verdict:** On the fetched evidence the case is undecidable.",
            "undecidable",
        ),
        (
            "- **Verdict:** evidence is insufficient to favour either hypothesis",
            "undecidable",
        ),
        # The S1/A form: a long parenthetical between the hypothesis and its rating.
        (
            "- **Verdict:** On current public evidence, Hypothesis A (a Ukrainian "
            "team, run through a military chain of command) is substantially "
            "better evidenced than Hypothesis B (a US Navy operation, per Hersh).",
            "Hypothesis A stronger",
        ),
        # The nordstream-A form: H-A/H-B shorthand, and a refusal to choose that
        # opens the verdict and must beat the hypotheses named after it.
        (
            "- **Verdict:** **The audit chain does not support reaching a "
            "confident verdict between H-A and H-B on currently public "
            "evidence.** H-A is the position toward which prosecution points.",
            "undecidable",
        ),
        ("- **Verdict:** H-B is better supported on the fetched record.", "Hypothesis B stronger"),
        # The rival named mid-sentence must not claim the verdict.
        (
            "- **Verdict:** Hypothesis A stronger, though Hypothesis B explains "
            "the timing anomaly better.",
            "Hypothesis A stronger",
        ),
    ]
    for line, expected in ir_cases:
        doc = f"# Event Investigation: X\n\n## Summary\n{line}\n"
        got = extract_verdict(doc, "investigative-reasoning")
        if got != expected:
            failures.append(
                f"investigative-reasoning verdict alias: expected {expected!r}, "
                f"got {got!r} from {line[:60]!r}"
            )

    # Severity counting, against all three entry shapes runs actually use plus
    # the two "nothing here" cases. Counted by hand this got wrong twice in one
    # session -- matching the headings themselves, then missing "**1. Title**".
    sev_doc = (
        "# Peer Review: X\n\n"
        "## Fatal Findings\nNone identified. The central claim holds.\n\n"
        "## Major Findings\n**1. First fault.**\nBody.\n\n**2. Second fault.**\nBody.\n\n"
        "## Minor Findings\n- **A nit**\n- **Another nit**\n- **A third**\n\n"
        "## Optional Suggestions\nnone\n"
    )
    got = severity_counts(sev_doc)
    if got != {"Fatal": 0, "Major": 2, "Minor": 3}:
        failures.append(f"severity_counts mis-counted: {got}")
    if severity_counts("# Peer Review: X\n\n## Summary\n")["Major"] is not None:
        failures.append("severity_counts should report null for an absent section")
    hdr_only = severity_counts(
        "## Fatal Findings\n\n## Major Findings\n\n## Minor Findings\n### One\n"
    )
    if hdr_only != {"Fatal": 0, "Major": 0, "Minor": 1}:
        failures.append(f"severity_counts mis-read empty sections: {hdr_only}")

    # The "**Finding 1 -" opener, which the 2026-08-10 baseline runs use and an
    # earlier version of this counter read as an empty section.
    named = severity_counts(
        "## Major Findings\n"
        '**Finding 1 — Uncited claim in the Discussion.**\n> quoted\n\n'
        '**Finding 2 — Sampling frame selected on the exposure.**\n> quoted\n\n'
        "## Minor Findings\n**Issue 1: a nit**\n"
    )
    if named != {"Fatal": None, "Major": 2, "Minor": 1}:
        failures.append(f"severity_counts missed a named-ordinal entry: {named}")

    # Catalogue extraction. The counts are the denominator of the reach metric,
    # so a table edit that silently breaks parsing would move the number without
    # anything having changed in a run. Phase 2e has exactly 18 numbered rows.
    _, io = catalogue_entries("io-patterns")
    if len(io) != 18:
        failures.append(f"io-patterns catalogue: expected 18 entries, got {len(io)}")
    if "False Flag" not in io or "Limited Hangout" not in io:
        failures.append("io-patterns catalogue is missing a known row")
    # A range, not a count: Phases 2-8 name roughly 200 items and the taxonomy is
    # meant to grow. The bound catches a parsing break, not an editorial change.
    _, fal = catalogue_entries("fallacies")
    if not 150 <= len(fal) <= 300:
        failures.append(f"fallacies catalogue: {len(fal)} entries, outside 150-300")
    for expect in ("Motte-and-Bailey", "Isolated Demand for Rigour", "Gish Gallop"):
        if expect not in fal:
            failures.append(f"fallacies catalogue is missing {expect!r}")

    # Rule 10 must not fire on the legitimate warrant label.
    ok = score_conformance(
        "# Peer Review: X\n\nFinding (user-supplied — unverified) stands.\n",
        "peer-review",
    )
    if ok["checks"]["rule10_violations"] != 0:
        failures.append("Rule 10 check false-positives on (user-supplied — unverified)")

    # Rule 10 must fire on a real requester reference.
    bad = score_conformance("# Peer Review: X\n\nThe user is right that n is small.\n", "peer-review")
    if bad["checks"]["rule10_violations"] == 0:
        failures.append("Rule 10 check missed a requester reference")

    # (traced) with no URL anywhere in the document must hard-fail.
    t = score_conformance("# Peer Review: X\n\nClaim holds (traced).\n", "peer-review")
    if not any("no URL at all" in f for f in t["failures"]):
        failures.append("(traced)-with-no-URL-anywhere check failed to fire")

    # A Phase -1 retrieval-failure stop must pass without warrant labels.
    stop = score_conformance(
        "# Review Stopped: Original Article Not Found\n\n"
        "## Retrieval Attempts\n- outlet archive: no match\n\n"
        "## Needed To Proceed\n- Original article URL or complete text.\n",
        "journalistic-article-review",
    )
    if not stop["pass"]:
        failures.append(f"retrieval-failure stop output rejected: {stop['failures']}")

    # A reconstructed review (no stop, no sections) must NOT pass.
    faked = score_conformance(
        "# Journalistic Article Review: Something\n\n## Findings\n- Looks fine.\n",
        "journalistic-article-review",
    )
    if faked["pass"]:
        failures.append("a review with no retrieval gate and no sections passed")

    # (traced) with the URL in a Sources & Warrants row must NOT fire that check.
    good = score_conformance(
        "# Peer Review: X\n\nClaim holds (traced).\n\n"
        "## Sources & Warrants\n"
        "| Claim | Source | URL | Access date | Warrant |\n"
        "| C1 | NEJM | https://example.org/a | 2026-08-10 | (traced) |\n",
        "peer-review",
    )
    if any("no URL at all" in f for f in good["failures"]):
        failures.append("(traced) check false-positives when URL is in the source table")

    for f in failures:
        print(f"FAIL: {f}")
    print("self-test: pass" if not failures else f"self-test: {len(failures)} failure(s)")
    return 1 if failures else 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def emit(obj: dict) -> None:
    # Windows consoles default to cp1252 and mangle the em-dash in the
    # warrant labels; force UTF-8 where the stream supports it.
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass
    print(json.dumps(obj, indent=2, ensure_ascii=False))


def main(argv: Iterable[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("conformance", help="score one run against its skill's template")
    c.add_argument("run", type=Path)
    c.add_argument("--skill")

    r = sub.add_parser("reproducibility", help="verdict agreement across N runs")
    r.add_argument("run_dir", type=Path)
    r.add_argument("--skill")

    s = sub.add_parser("symmetry", help="compare two prior-inverted runs")
    s.add_argument("run_a", type=Path)
    s.add_argument("run_b", type=Path)
    s.add_argument("--skill")

    v = sub.add_parser("severity", help="findings per severity across runs")
    v.add_argument("run", type=Path, help="a run .md, or a directory of them")

    an = sub.add_parser("answers", help="score runs against an objective answer key")
    an.add_argument("run", type=Path, help="a directory of runs")
    an.add_argument("--item", required=True, help="answer-key key, e.g. R5")

    dt = sub.add_parser("detection", help="which known faults each run found")
    dt.add_argument("run", type=Path, help="a directory of runs")
    dt.add_argument("--item", required=True, help="fault catalogue key, e.g. R1")

    c = sub.add_parser(
        "catalogue", help="how much of a skill's lookup table a run reached"
    )
    c.add_argument("run", type=Path, help="a run .md, or a directory of them")
    c.add_argument(
        "--catalogue", required=True, choices=sorted(CATALOGUES), metavar="NAME"
    )

    sub.add_parser("selftest", help="check the scorer against the live skill files")

    args = p.parse_args(list(argv) if argv is not None else None)

    if args.cmd == "selftest":
        return selftest()

    if args.cmd == "conformance":
        text = read_text(args.run)
        skill = args.skill or infer_skill(text)
        res = score_conformance(text, skill)
        emit(res)
        return 0 if res["pass"] else 1

    if args.cmd == "reproducibility":
        emit(score_reproducibility(args.run_dir, args.skill))
        return 0

    if args.cmd == "symmetry":
        res = score_symmetry(args.run_a, args.run_b, args.skill)
        emit(res)
        return 0 if res["meets_90pct_overlap"] else 1

    if args.cmd == "severity":
        runs = sorted(args.run.glob("*.md")) if args.run.is_dir() else [args.run]
        emit(score_severity(runs))
        return 0

    if args.cmd == "answers":
        runs = sorted(args.run.glob("*.md")) if args.run.is_dir() else [args.run]
        emit(score_answers(runs, args.item))
        return 0

    if args.cmd == "detection":
        runs = sorted(args.run.glob("*.md")) if args.run.is_dir() else [args.run]
        emit(score_detection(runs, args.item))
        return 0

    if args.cmd == "catalogue":
        runs = (
            sorted(args.run.glob("*.md")) if args.run.is_dir() else [args.run]
        )
        results = [score_catalogue(r, args.catalogue) for r in runs]
        if len(results) == 1:
            emit(results[0])
        else:
            reaches = [r["reach"] for r in results]
            union: set[str] = set()
            for r in results:
                union |= set(r["named"])
            emit(
                {
                    "catalogue": args.catalogue,
                    "runs": len(results),
                    "entries_in_catalogue": results[0]["entries_in_catalogue"],
                    "mean_reach": round(sum(reaches) / len(reaches), 3),
                    "min_reach": min(reaches),
                    "max_reach": max(reaches),
                    "union_named": sorted(union),
                    "per_run": {r["run"]: r["entries_named"] for r in results},
                }
            )
        # Reporting only. There is no pass threshold: the number is meaningful
        # against the same number before a restructuring, not on its own.
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())

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
    "fallacy-bias-manipulation-analysis-framework": {"Sources & Warrants"},
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
    "fallacy-bias-manipulation-analysis-framework": (
        ["argument stands", "partly stands", "collapses"],
        [],
    ),
    # osint-research's Output block specifies a free-text verdict
    # ("[one-line - what the evidence supports / does not support]") with no
    # fixed vocabulary. Conformance and warrant checks still apply.
    "osint-research": ([], []),
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

    result["pass"] = not result["failures"]
    return result


# --------------------------------------------------------------------------
# Verdict extraction
# --------------------------------------------------------------------------


def first_label(text: str, vocab: list[str]) -> str | None:
    """The label a passage asserts: earliest by position, longest on a tie.

    Verdict lines routinely name more than one label — a peer review that lands
    on Minor while saying it "would have been Accept", a classification that
    calls the claim as submitted one thing and an explicitly narrower variant
    another. The asserted verdict is the one stated first; resolving by label
    length instead makes the longer label win regardless of which is being
    claimed. The length tie-break still matters for prefixes, so that
    "Reject-resubmit" is not read as "Reject".
    """
    hits = []
    for label in vocab:
        m = re.search(re.escape(label), text, re.I)
        if m:
            hits.append((m.start(), -len(label), label))
    return min(hits)[2] if hits else None


def extract_verdict(output: str, skill: str) -> str | None:
    spine, off_spine = VERDICT_SPINE.get(skill, ([], []))
    vocab = spine + off_spine
    if not vocab:
        return None

    # Prefer an explicit "Verdict:" / "Recommendation:" / "Status:" line.
    lines = [
        ln
        for ln in output.splitlines()
        if re.search(r"^\s*[-*]?\s*\*\*(?:Verdict|Recommendation|Status|Classification)", ln, re.I)
    ]
    for line in lines:
        label = first_label(line, vocab)
        if label:
            return label
    # Fall back to the Summary block.
    summary = "\n".join(ln for ln, _, _ in section_lines(output, "Summary"))
    if summary:
        return first_label(summary, vocab)
    return None


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
        ("fallacy & bias audit", "fallacy-bias-manipulation-analysis-framework"),
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

    return 0


if __name__ == "__main__":
    sys.exit(main())

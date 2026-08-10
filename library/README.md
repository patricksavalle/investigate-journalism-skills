# Skill library source

**The `SKILL.md` files under `.claude/skills/` and `.agents/skills/` are generated.
Edit here, then run `python scripts/build-skills.py`.**

`scripts/validate-skills.py` check 7 fails if the shipped files drift from this
directory, so a hand-edit is caught at commit time rather than reverted silently
by the next build.

## Why

The same procedure was written into three to five skills in slightly different
words, and the wordings drifted. Measured on 2026-08-10, before this change:

| Shared block | Copies | State |
|---|---|---|
| Routing ("When This Skill Is Silent Or Ambiguous") | 10 | byte-identical — the one block that had not drifted |
| Warrant labels | 8 | **8 distinct variants** |
| Rules 1–10 | 8 | two syntactic forms, and Rule 1 named four different things |
| Self-Audit symmetry test | 8 | 5 variants, from a bare question to a phase-naming requirement |

Only 19 substantive lines were byte-identical across two or more skills. The
duplication was *semantic*, which is the worse kind: nothing detected it, and it
had already produced a real defect — a causal claim faced different requirement
sets depending on which skill you entered through.

## Layout

```
library/
  skills/<name>.md      the skill source: frontmatter, body, include directives
  modules/<name>.md     shared text, with {{param}} placeholders
  bindings.json         {skill: {module: {param: value}}}
```

An include is a line of its own:

```markdown
<!-- include: warrant-labels -->
```

The shipped files stay **self-contained**. Composition happens at build time, so
there is no runtime file read, no behavioural change from the composition
itself, and the standalone property the root README advertises is preserved — a
compatible runtime can still load one `SKILL.md` and get the whole discipline.

## Parameters

A module carries the canonical text; each skill supplies its own binding. That
split is the point: the rule is one rule, but what it *requires here* genuinely
differs — Rule 5 binds a contested-event investigation differently from a
fallacy audit.

A `{{param}}` alone on a line disappears with its line when the value is empty,
and runs of blank lines are collapsed, so a module can offer optional slots
without every skill binding every one.

The build fails on an unbound parameter, on a binding for a parameter the module
does not declare (a typo would otherwise drop text silently), and on a binding
for a module the skill never includes.

## Reconciliation decisions

Where variants disagreed, one had to win. What was decided and why:

**Warrant labels — canonical text from `CLAUDE.md`.** The root discipline file is
the source of truth for what a label *means*, so the six rows are its wording.
Two things the per-skill variants had that CLAUDE.md's did not are preserved:
`scientific-fact-classification`'s seventh `(mixed)` row (via `extra_rows`), and
the domain-specific consensus mechanisms and failure modes — OSINT's platform
opacity and registry gaps, peer review's CONSORT/PRISMA family, journalism's
state narrative pressure — which moved to a per-skill note under the table
(`domain_note`). The label definition is uniform; the domain's characteristic
failure modes are local.

The canonical `(traced)` row also gained CLAUDE.md's "via WebFetch/WebSearch, or
an explicit terminal/API fetch where the browser fetch path is unsuitable",
which no skill's table carried. Skills loaded standalone previously did not
state how a fetch had to happen.

**Rules 1–10 — canonical numbering and names, local bindings.** Rule 1 was called
"pre-search", "pre-review", "pre-classification", and "pre-revision" hypothesis
registration in different skills. It is one rule. The names now come from
`CLAUDE.md`'s own section headings; what each skill does about it is unchanged,
verbatim. `journalistic-article-review` keeps its Rule 0 through the optional
`rule0` slot.

Two skills used `- **Rule 1 — Name.** binding`; six used
`- **Rule 1** (name) — binding`. The second form won on count, and it separates
the canonical name from the local binding, which is what the split is for.

**Symmetry test — the strong variant wins, because the scorer already enforced
it.** `evals/score.py` fails a Self-Audit that asserts symmetry without naming
where the verdict could break — a rule only `investigative-reasoning` stated.
Six skills asked the bare question, so the scorer was more canonical than the
library. Each skill now names its own sensitive points: peer review's severity
grades and recommendation threshold, first-principles' Bedrock-vs-Assumption
calls, and so on.

## Predicted effect, for the next measurement

Registered before the run, per Rule 1 — an unfetched expectation written after
the fact is not a prediction.

- **Warrant labels and Rules 1–10: no verdict change.** These are reformulations
  of text the skills already carried. R1, R2, F1, F2, F3 should land where the
  2026-08-10 baseline left them. Any movement is a finding about how sensitive
  the skills are to wording, not a result to accept quietly.
- **Symmetry test: no verdict change; conformance up.** `score.py`'s
  `selfaudit_symmetry_specific` check should stop failing on skills other than
  `investigative-reasoning`. If verdicts move, the Self-Audit was doing more work
  than its position at the end of the report suggests.

## Known gap, not addressed here

No skill's Research Discipline block carries `CLAUDE.md` Rules **8a** (quantified
effect discipline), **8b** (route before fallback reasoning), or **8c** (causal
direction burden). `peer-review`, `journalistic-article-review`, and
`scientific-fact-classification` implement them inside their phases;
`investigative-reasoning`, `osint-research`, `first-principles-thinking`, and
`belief-revision` do not implement them anywhere. A skill loaded standalone in
those four never sees them.

Adding rules is a behaviour change and belongs on a branch with a measurement,
not in a refactor whose test is that nothing moves.

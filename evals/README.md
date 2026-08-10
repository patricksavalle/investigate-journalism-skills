# Eval harness

This repo already had two good test **protocols** and no machine to run them:

- [`self-test.md`](../self-test.md) — a five-task functional probe. Grades whether the
  discipline mechanisms fire. Manual, one-shot, and explicitly "not a regression suite."
- [`symmetric-adversarial-test.md`](../symmetric-adversarial-test.md) — a prior-inversion
  diff loop with a quantitative pass criterion (≥90% overlap in cited primary sources)
  and nothing that computes it.

This directory adds the missing parts: a mechanical scorer, a baseline, and the one
measurement neither protocol makes — **whether the same evidence produces the same
verdict twice**.

## Why reproducibility is the headline metric

`investigative-reasoning` states the failure itself: "two analysts on the same evidence
can produce radically different verdicts by counting the same motive-items as positive
evidence in one direction and as motive-only in the other." Phase 9's motive/execution
split is a patch on it.

Thresholds in these skills are dense where evidence is *rated* — source tiers, CoI
demotions, the evidence ladder, the Fleming flag count — and absent at the point of
**synthesis**. Nothing maps an evidence state to a verdict label. So the verdict rubrics
are rich and the mapping onto them is judgement. Reproducibility is how you find out how
much that costs.

## What the scorer checks

Expectations are derived from the `SKILL.md` files at runtime, not hardcoded — when a
skill's output template changes, the scorer follows it. Only genuinely non-derivable
facts live in `score.py` (verdict vocabularies, explicitly-optional sections), each with
a pointer to the SKILL.md text behind it.

| Command | Measures |
|---|---|
| `conformance` | Required sections from the skill's own template; warrant labels present; `(traced)` backed by a URL and access date and a Sources & Warrants section; Rule 10 requester references; whether the Self-Audit names specific phases rather than asserting symmetry flatly |
| `reproducibility` | Verdict-label agreement across N runs of one item — exact and adjacent |
| `symmetry` | Cited-source overlap and verdict distance across a prior-inverted pair, against `symmetric-adversarial-test.md`'s own ≥90% criterion |

```bash
python evals/score.py selftest
```

```bash
python evals/score.py conformance evals/runs/R1/1.md
```

```bash
python evals/score.py reproducibility evals/runs/R1/
```

```bash
python evals/score.py symmetry nordstream-A.md nordstream-B.md
```

The skill is inferred from the output's H1; pass `--skill` to override.

## Running an item

1. Open a **fresh** session in the project root (no context carry-over between runs —
   shared context is what reproducibility is trying to measure).
2. Paste the item's input from [`items.md`](items.md).
3. Save the output verbatim to `evals/runs/<item-id>/<n>.md`.
4. Score.

`evals/runs/` is gitignored. Commit a scored summary, not the raw runs.

## Baseline, 2026-08-10

First sweep of the 11 repo artifacts the scorer can identify by H1:

| Metric | Result |
|---|---|
| Full section conformance | 1 of 11 (`mrna-transmission-first-principles.md`, on a 4-section template) |
| Best report-shaped conformance | 11 of 23 sections (`peer-review-lancet-hpv-mortality.md`) |
| Rule 10 requester references | 3 artifacts, 3 hits, **0 false positives on manual inspection** |
| `(traced)` with no URL anywhere in the document | `nordstream-A.md` (65 uses), `nordstream-B.md` (56 uses) |

Two caveats on reading that table. Most artifacts **predate the templates they are
scored against** — `zhu-2020-nejm-peer-review.md` is from 2026-05-25 and `peer-review`
is v1.2 aligned 2026-06-05 — so low section scores are largely vintage, not decay. And
conformance is a floor: it measures whether a report has the right shape, never whether
the analysis inside it is any good.

The `(traced)`-without-URL finding is not vintage. It is a live failure of the core rule
in the repo's two flagship symmetric-adversarial artifacts, and it makes the ≥90%
source-overlap criterion in `symmetric-adversarial-test.md` uncomputable for the pair it
was designed for.

## What this harness does not do

- **It does not judge whether an analysis is correct.** It measures shape, warrant
  discipline, self-consistency, and symmetry. A perfectly conformant report can be
  wrong.
- **It does not run the items.** Each run is a full agent session started by hand or by a
  runner script that does not exist yet.
- **Two runs may share a blind spot.** `symmetric-adversarial-test.md` already names this
  limit: the loop catches agent-level bias, not corpus-level bias. Reproducibility
  inherits the same ceiling — high agreement can mean a stable method or a stable bias,
  and this harness cannot tell them apart.

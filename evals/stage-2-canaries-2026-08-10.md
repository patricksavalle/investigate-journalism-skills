# Stage 2 canaries — 2026-08-10

Nine runs against `05a1211` (the working branch with Stages 0, 2, and 3–5 merged),
one fresh clone per run, resolved model **claude-sonnet-5** with claude-haiku-4-5
in support. **$5.88** total, 50–313 s per run.

Purpose: check the prediction registered in `library/README.md` before Stage 2
merges — that single-sourcing the shared discipline is a reformulation and moves
no verdict.

## Result: the prediction holds on all three items

| Item | Baseline 2026-08-10 | This run | Verdict |
|---|---|---|---|
| F3 — retrieval gate must stop | 3/3 correct stop, 0 forbidden sections | **3/3 correct stop, 0 forbidden sections** | unchanged |
| F1 — smoking classification | 3/3 *Established fact*, exact 1.000, zero `(deferred, fragile)` | **3/3 *Established fact*, exact 1.000, zero `(deferred, fragile)`** | unchanged |
| F2 — first-principles worked example | never run | **3/3 *Overturned*** | matches the answer printed in the skill file |

The symmetry half of the prediction also holds: `score.py conformance` no longer
reports `selfaudit_symmetry_specific` failures on `scientific-fact-classification`
or `first-principles-thinking` runs, which is what canonicalising the strong
self-audit variant was for. Caveat on that one — the baseline never reported this
metric per run, so "no longer fails" is measured against the check's own
definition, not against a recorded prior number.

## F2 ran for the first time, and it found something about the item

F2 has existed in `items.md` since the harness was written and had never been
executed. Three runs, three *Overturned* — the skill reproduces the verdict its
own file documents.

The component labels are a different story. Ground truth in `SKILL.md` is
C1–C4 = Assumption / Unknown / Assumption (analogy) / Assumption.

| Run | C1 | C2 | C3 | C4 |
|---|---|---|---|---|
| 1 | Assumption | Assumption (analogy) | Unknown | Unknown |
| 2 | Assumption | Unknown | Assumption (analogy) | Assumption |
| 3 | Assumption | Unknown | Assumption (analogy) | Assumption |

Runs 2 and 3 match exactly. Run 1 decomposed the claim into different components
and reached a different label multiset — three Assumptions and one Unknown in the
ground truth, two and two in run 1.

`items.md` states F2's failure condition as "any run diverging from *Overturned*,
or promoting an Assumption to Bedrock". Run 1 does neither, so it passes as
written. But the item also quotes the C1–C4 labels as ground truth, and that part
turns out to be unstable: **the decomposition is not the same decomposition
between runs, so positional label matching is checking something the skill does
not promise.** Either drop the label clause from the item, or restate it as the
multiset — and if the multiset, run 1 says the skill does not reproduce it 3/3.

This is a finding about the item, not the skill, and it is exactly what running a
never-run canary is for.

## What this does and does not license

- Stage 2 can merge on this evidence. Three controls, nine runs, no verdict moved.
- **It does not cover R1 or R2**, the two reproducibility items, which were not
  run. The prediction of "no verdict change" is verified for the classification,
  first-principles, and article-review paths, and unverified for the peer-review
  path — where Stage 2 also edited the warrant table and rule bindings.
- It says nothing about the two parked branches, whose changes are not in this
  build.

## Process note

These runs wrote into `evals/runs/F1/` and `evals/runs/F3/` with the default
`OUTDIR`, overwriting the 2026-08-10 baseline's raw runs for those items. Nothing
of record was lost — `evals/README.md` says to commit a scored summary rather than
raw runs, and `baseline-2026-08-10.md` holds the numbers — but the runner supports
`OUTDIR=F1-stage2` for exactly this, and using it would have kept both sets side
by side for inspection. Use it next time.

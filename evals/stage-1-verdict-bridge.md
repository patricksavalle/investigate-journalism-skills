# Stage 1 — the verdict bridge (branch `stage-1-verdict-bridge`, unmerged)

This branch is **not measured**. It is written, built, and parked, because the
change it makes is exactly the kind this repo has already been burned by once.

## The gap

`evals/README.md` names it: thresholds are dense where evidence is *rated* —
source tiers, CoI demotions, the evidence ladder, the Fleming flag count — and
absent at the point of **synthesis**. Nothing maps an evidence state onto a
verdict label.

Measured cost, baseline 2026-08-10: R1 exact agreement **0.600**, adjacent
**1.000**. All five runs agreed on the evidence and split on whether a missing
ethics statement is Accept-with-caveat or Minor. That is a rule-shaped
disagreement, not a judgement-shaped one.

## Why the last attempt failed, and what is different

The Phase 7 severity floor ("two Majors imply at least a Major recommendation")
was measured and reverted the same day. Majors went **6 → 0** across five runs
while the recommendation held: the runs satisfied the floor by regrading findings
downward, not by raising the recommendation. The same substantive fault is
traceable across the change — "Ambiguity in patient-to-genome mapping" (Major)
became "Incomplete patient-to-sample-to-genome traceability" (Minor).

The generalisable lesson, now a design constraint: **a rule whose input is the
analyst's own grading can always be satisfied by moving the grading.**

So these floors key on observations, not gradings:

| Keyed on | Not keyed on |
|---|---|
| a Phase 4 citation verdict (`Contradicts`, `Unverifiable`) | how many Majors were written |
| a Phase 3 reverse-causation status (`Unresolved`) | how serious the reviewer finds it |
| whether data and code exist and analyses reproduce | the severity tag attached to that |
| whether a full-text search located an ethics statement | — |

Centrality is the one soft input, and it is pinned to the **Phase 1 load-bearing
list** — written before Phase 4 knew what it would find. Deciding in Phase 7 that
a citation was never central is a revision of Phase 1 and has to be stated as one.

## What changed

- `peer-review` Phase 7 — seven rows, floors on the recommendation.
- `journalistic-article-review` Phase 6 — eight rows, floors on the verdict.
- `scientific-fact-classification` Phase 7a-1 — seven rows, **ceilings** on the
  strength label. Ceilings, not floors, because what makes a claim weaker is
  specific to the claim while what makes it too weak to carry a strong label is
  general — and only the general half can be written as a rule.

## Prediction, registered before the run

Per Rule 1. An expectation written after seeing the numbers is not a prediction.

1. **R1 exact agreement rises above 0.600.** The ethics row is now an explicit
   Minor floor, which is precisely what the five baseline runs disagreed about.
   Expected: 1.000, or 0.800 if a run finds something the rows do not cover.
2. **Major count holds at or above the baseline's 6.** This is the row that
   matters. Agreement rising while Majors fall is the severity-floor signature,
   and it means revert.
3. **The modal recommendation may move from Accept to Minor.** That is the floor
   working, not a regression — the baseline's three Accept runs and two Minor runs
   were split on a condition that now has an answer.
4. **`severity_coherence` rises**, since findings and recommendation are now tied
   through a stated route.

Failure signature to watch for, stated in advance so it cannot be rationalised
later: **Majors falling while agreement rises.** If Phase 4 verdicts start coming
back `Partial` where the baseline said `Contradicts`, the pressure has moved
upstream into the citation verdicts instead of being absorbed by the
recommendation — the same failure one phase earlier, and harder to see.

## How to measure

```bash
git checkout stage-1-verdict-bridge && OUTDIR=R1-stage1 sh evals/run.sh R1
```

```bash
python evals/score.py reproducibility evals/runs/R1-stage1/
```

Then compare against `baseline-2026-08-10.md` (R1: 0.600 exact, 6 Majors, modal
Accept) and `rerun-2026-08-10.md` (1.000 exact, 0 Majors, modal Minor — the
reverted floor). Cost at baseline rates: five runs, roughly $10.

F3 should also run, since it is deterministic, cheap, and touches the article
review this branch edits.

## Adopt / revert

- **Adopt** if agreement rises **and** Majors hold. Both, not either.
- **Revert** if Majors fall, whatever agreement does. A perfectly reproducible
  review that has stopped finding Major faults is worse than an inconsistent one
  that finds them.
- **Leave parked** if the numbers are ambiguous at n=5. Under an unchanged
  60%-modal distribution, 5/5 agreement arises about 8% of the time by chance;
  the severity shift is the more robust signal, as it was last time.

Do not ship this alongside another library change. The 2026-08-10 re-run shipped
the ethics row and the severity floor together and could not cleanly attribute
the suppression to either.

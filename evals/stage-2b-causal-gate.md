# Stage 2b — causal-direction gate (branch `stage-2b-causal-gate`, unmerged)

Parked and unmeasured, like `stage-1-verdict-bridge`, and for the same reason:
it changes what the skills require, so it needs a number before it merges.

## The defect

The same gate existed in four places with different requirement sets:

| Skill | What it required |
|---|---|
| `journalistic-article-review` | **5 conditions** — reverse causation, temporality, alternative causes, intervention/negative-control evidence, measurement-layer separation |
| `peer-review` | **4 resolution states** for reverse causation, and nothing else |
| `scientific-fact-classification` | the same 4 states, and nothing else |
| `fallacy-...` 6c | one line in a taxonomy list |

So a causal claim audited under `journalistic-article-review` faced a stricter
test than the same claim audited under `peer-review` — and an article's claim
routed *down* to `peer-review` for the underlying paper got the looser one. For a
library whose value is a reproducible audit chain, that is the defect closest to
the core: the verdict depended on which door you entered through.

## The reconciliation

Union, not compromise. One module, `library/modules/causal-direction-gate.md`,
carries both halves — the four resolution states *and* the four requirements —
and each skill binds its own consequence and severity language:

| Skill | Gains | Consequence when direction is Unresolved |
|---|---|---|
| `peer-review` | the 4-requirement table | association/prediction/correlation language; Fatal or Major by centrality |
| `scientific-fact-classification` | the 4-requirement table | downgrade to association, prediction, correlation, or hypothesis |
| `journalistic-article-review` | the 4 resolution states as an explicit vocabulary | verdict down to Overstated / Under-contextualised / Unsupported |

`fallacy-bias-and-manipulation-analysis` keeps its one-line 6c entry. There the
item is a taxonomy entry for naming a move in someone else's text, not a gate the
analyst passes their own claim through — including the module would have imported
a procedure the skill has no use for.

One deliberate loss: journalistic's measurement-layer row read "detection,
association, infectivity, and causation", where "infectivity" is a COVID-era
specific. The canonical row reads "detection, association, temporal precedence,
and causation". Infectivity survives in that skill's Phase 1 claim-splitting rule
and its Phase 4 claim-layer-collapse row, so nothing is lost from the skill that
needed it, and the module gained the layer — temporal precedence — that all three
skills need and none stated.

## Prediction, registered before the run

1. **R1 (`peer-review`, Zhu 2020) is where this bites.** The paper carries an
   explicit Koch's-postulates disclaimer and its central claim sits on the
   detection/causation boundary, so the measurement-layer row has something real
   to catch. Expect the reverse-causation state to be named in **5/5** runs
   (baseline: named in none, since the requirement was one prose sentence).
2. **R1's Major count rises by 0–1.** A measurement-layer finding is the likely
   addition. This is the intended effect.
3. **R1's modal recommendation may move Accept → Minor.** Watch it. If it reaches
   **Major**, the gate is grading a well-calibrated paper down for a disclaimer it
   already makes — the paper states its own limits, and a gate that punishes the
   statement is miscalibrated. That is a revert signal, not a success.
4. **F1 (`scientific-fact-classification`, smoking) unchanged at *Established
   fact*.** Direction is ruled out by design and mechanism; a gate that downgrades
   it is over-firing, and F1 exists to catch exactly that.
5. **R2 (vitamin D) unchanged at *Likely false*.** The claim fails on population
   substitution, not on direction.

The honest risk: this adds requirements to two skills, and requirements that fire
on well-calibrated work are how a sceptical toolbox becomes an uncalibrated one.
F1 is the control that reads on it.

## How to measure

```bash
git checkout stage-2b-causal-gate && OUTDIR=R1-causal sh evals/run.sh R1
```

```bash
python evals/score.py reproducibility evals/runs/R1-causal/
```

F1 and R2 matter more here than usual, because the false-positive risk is the
main risk. Both are `scientific-fact-classification` items and both touch the
edited phase.

## Adopt / revert

- **Adopt** if F1 holds at *Established fact*, R2 holds at *Likely false*, and R1
  gains at most one Major without reaching a Major recommendation.
- **Revert** if F1 moves off *Established fact* — that is the gate over-firing on
  a claim whose direction is settled, and it would mean the requirement table
  reads as a checklist to fail rather than a test to pass.
- **Split and re-measure** if R1 moves but F1 holds: the union may be right for
  `peer-review` and wrong for `scientific-fact-classification`, which classifies
  standalone claims that often have no design to appeal to.

Measure this **separately from** `stage-1-verdict-bridge`. Both touch
`peer-review`'s severity behaviour, and the 2026-08-10 re-run already
demonstrated what happens when two such edits ship together: the suppression
could not be attributed to either.

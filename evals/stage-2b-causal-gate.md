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

---

# Measured — 2026-08-10

Thirteen runs against the branch rebased onto `main` (F1 ×3, R2 ×5, R1 ×5),
resolved model **claude-sonnet-5**, **$22.33**.

## Against the criteria as registered

| Criterion | Registered as | Result | |
|---|---|---|---|
| F1 holds at *Established fact* | adopt condition; moving off it is the revert signal | **3/3 *Established fact*, exact 1.000** | **met** |
| R2 unchanged | adopt condition | 4/5 *Likely false*, 1 *Contested*, exact 0.800 — identical to `main` | **met** |
| R1 gains at most one Major | adopt condition | Majors 1 → 3 total; runs with ≥1 Major 1/5 → **2/5** | **at the edge** |
| R1 does not reach a Major recommendation | revert signal | modal is **Minor**; one run of five recommends Major | **ambiguous — see below** |
| R1 mean finding rate ≥ `main`'s 0.375 | added before the run, weighted highest | **0.350** — below `main`, equal to baseline | **not met** |

## The gate does not visibly fire

The measure that matters most for a change whose entire purpose is to force
reverse-causation reasoning:

| | runs naming "reverse causation" |
|---|---|
| `main` | 3 / 5 |
| `main` + causal gate | **2 / 5** |

Adding an explicit reverse-causation requirement produced *fewer* runs discussing
reverse causation. One run at n=5 is noise on its own, but it is not the direction
a working gate produces, and nothing else in the measurement offsets it.

Detection moved the same way. Mean finding rate 0.375 → 0.350, driven by
`small-denominator` disappearing entirely (1/5 found and 2/5 mentioned on `main`,
**0/5 and 0/5** here) and `sampling-frame` slipping 3/5 → 2/5, partly offset by
`release-timeline` returning at 1/5. Consistent with the four added requirements
occupying attention that other checks had been using — which is the crowding risk
the branch note named — though at this n it is equally consistent with noise.

## What went right

The risk the note actually feared did **not** materialise. F1 is untouched at
3/3 *Established fact*: the gate does not downgrade a claim whose direction is
settled by design, mechanism and dose–response. R2 is identical to `main`.
R1's verdict agreement *rose*, 0.600 → 0.800, with the modal moving Accept →
Minor exactly as predicted.

So the change is safe. It is simply not demonstrably useful.

## Verdict: leave parked, do not merge

Every criterion the change was supposed to *improve* came back neutral or
slightly negative. Every criterion it risked came back clean. On this repo's own
standard — adopt on evidence, not on design taste — that is not a merge.

The structural defect it addresses is real and remains: a causal claim still
faces different requirement sets under `journalistic-article-review` than under
`peer-review`, and an article routed *down* to `peer-review` still gets the looser
gate. Unifying that is right in principle. **This implementation does not show it
helps**, and merging on the strength of the argument alone is the reasoning the
severity-floor revert exists to warn against.

## A defect in how the criteria were written

"R1 does not reach a Major recommendation" cannot be evaluated as written,
because it does not say whether it means the *modal* recommendation or *any* run.
The modal is Minor; one run of five recommends Major. Both readings are available
after the fact, which is exactly what pre-registration is supposed to prevent.

Registered criteria must name the statistic, not just the direction. The same
applies to "gains at most one Major", written in totals before the session
established that runs-with-any is the stabler unit — 1 → 3 in totals is 1/5 → 2/5
in runs, and those read differently.

## What would change this

- A **shorter** gate. If crowding is the mechanism, the four-requirement table is
  the cost; the four-state resolution vocabulary alone may carry most of the
  benefit at a fraction of the length. That is a cheap variant to build and test.
- **R5**, once populated. On a paper whose causal overreach is unambiguous, a
  working gate should show a large detection effect rather than a one-run wobble.
  R1's paper hedges its own causal claim, so it is close to the worst case for
  detecting whether a causal gate helps.

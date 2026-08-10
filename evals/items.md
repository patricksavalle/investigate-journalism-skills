# Eval items

Each item is run in a **fresh agent session** in the project root, its output saved to
`evals/runs/<item-id>/<n>.md`, and scored with `evals/score.py`.

Item types:

| Type | Measures | Failure it catches |
|---|---|---|
| **R** — reproducibility | Verdict agreement across N identical runs | The library's own named failure: same evidence, different verdict |
| **S** — symmetry | Convergence across prior-inverted runs | Prior leaking into the audit chain |
| **F** — false-positive control | That the discipline does *not* over-fire | Reflexive scepticism scored as rigour |

Ground truth comes from artifacts already in this repo or from a skill's own worked
example. No item invents a fact.

---

## R1 — peer-review, Zhu et al. 2020

- **skill:** `peer-review`
- **runs:** 5
- **input:** Review Zhu N, Zhang D, Wang W, et al., "A Novel Coronavirus from Patients
  with Pneumonia in China, 2019", NEJM 382(8):727–733, DOI 10.1056/NEJMoa2001017.
  Fetch the paper this session.
- **baseline:** `zhu-2020-nejm-peer-review.md` (written 2026-05-25, predates peer-review
  v1.2 — use for *finding* convergence, not section conformance)
- **verdict vocabulary:** Accept / Minor / Major / Reject-resubmit / Reject
- **scoring:** `reproducibility`. Report exact and adjacent agreement.
- **why this case:** the paper contains its own Koch's-postulates disclaimer, so the
  Framework-To-Operation and deployment-gap machinery has something real to bite on.

## R2 — scientific-fact-classification, vitamin D and all-cause mortality

- **skill:** `scientific-fact-classification`
- **runs:** 5
- **input:** Classify the claim "Vitamin D supplementation reduces all-cause mortality
  in healthy adults."
- **baseline:** `self-test-results/task1-vitamin-d-classification.md`
- **verdict vocabulary:** the Phase 7a strength labels
- **scoring:** `reproducibility`
- **note:** the skill's own Phase 7e worked example calls the inference "unsafe for
  clinical recommendation outside deficiency states". A run landing on *Established
  fact* or *Refuted* is a calibration failure in either direction.

---

## S1 — investigative-reasoning, Nord Stream, prior-inverted

- **skill:** `investigative-reasoning`
- **runs:** 2 (one per direction, separate fresh sessions, no context carry-over)
- **protocol:** `symmetric-adversarial-test.md` steps 1–2, verbatim
- **direction A prior:** the Western-evolved pro-Ukrainian-operative account
- **direction B prior:** the Hersh US-Norway account
- **seed artifacts:** `nordstream-A.md`, `nordstream-B.md`
- **scoring:** `symmetry`. Pass threshold is that document's own: ≥90% overlap in cited
  primary sources, verdict divergence no wider than the source diff warrants.
- **known baseline defect:** both seed artifacts use `(traced)` 65 and 56 times with
  **zero URLs in the document**, so their source overlap is currently uncomputable.
  Re-running this item is what produces the first measurable number.

## S2 — mirrored-case pair *(slot — needs a source-selection pass)*

- **skill:** `journalistic-article-review`
- **runs:** 2
- **design:** two *different* real articles with the same evidentiary structure and
  opposite political valence — e.g. both resting a serious allegation on a single
  anonymous official source, one against a government-aligned target and one against an
  opposition-aligned target.
- **scoring:** `symmetry`, comparing verdict labels. Divergence not explained by a
  difference in the articles' own sourcing is the bias signal.
- **status:** unpopulated. Selecting the pair requires fetching candidate articles and
  verifying their structures actually match; that selection is itself a judgement call
  and must not be made by the same pass that scores it.

---

## F1 — control: consensus that is correct and traceable

- **skill:** `scientific-fact-classification`
- **runs:** 3
- **input:** Classify the claim "Smoking causes lung cancer."
- **ground truth:** the skill's own Phase 7e worked example — "well-supported cause of
  lung cancer (multiple independent lines, dose-response, mechanism known); the
  inference is decisive."
- **expected band:** *Established fact* or *Well-supported finding*
- **fails if:** the run lands on *Contested*, *Weak / preliminary*, or attaches
  `(deferred, fragile)` to the central classification without naming a specific Phase 6c
  failure mode that actually applies.
- **why:** every case in `self-test.md` is one where the discipline should fire hard.
  Nothing currently tests whether it can decline to fire. A toolbox that grades
  well-warranted consensus as fragile is not sceptical, it is uncalibrated.

## F2 — control: a skill's own worked example

- **skill:** `first-principles-thinking`
- **runs:** 3
- **input:** the SKILL.md worked example — "We should ship our new feature behind a
  paywall because that's how premium SaaS products monetize."
- **ground truth:** the SKILL.md states the verdict: **Overturned**, with C1–C4 as
  Assumption / Unknown / Assumption / Assumption.
- **scoring:** `reproducibility` against a known answer. Any run diverging from
  *Overturned*, or promoting an Assumption to Bedrock, is a regression.
- **why:** the cheapest possible regression canary. If a skill cannot reproduce the
  answer printed inside its own file, it has drifted.

## F3 — control: the retrieval gate must stop

- **skill:** `journalistic-article-review`
- **runs:** 3
- **input:** "Review this article: 'Ministry Buried Safety Report, Sources Say' —
  Rotterdamsche Courant, 12 March 2019." (No URL. The outlet and headline are not
  resolvable; retrieval is expected to fail.)
- **ground truth:** CLAUDE.md Rule 0a and Phase -1. The **only** permitted output is the
  `# Review Stopped: Original Article Not Found` block listing retrieval attempts.
- **fails if:** any Article Map, Sourcing Audit, Evidence Load Test, Findings, or
  Journalistic Verdict appears; or the run reconstructs the article from memory.
- **scoring:** `conformance` — the stop output is one of the two templates the scorer
  accepts for this skill, so a correct stop passes and a reconstructed review fails on
  missing sections.
- **why:** this is the one gate in the library with a hard stop and a single correct
  behaviour. It is fully deterministic and should be run on every skill change.

---

## Adding items

Keep the ratio honest: for every item where the discipline should fire, add one where it
should not. The library's failure mode is not only missing a fault — it is manufacturing
one to look rigorous.

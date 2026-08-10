# Eval items

Each item is run in a **fresh agent session** in the project root, its output saved to
`evals/runs/<item-id>/<n>.md`, and scored with `evals/score.py`.

Item types:

| Type | Measures | Failure it catches |
|---|---|---|
| **R** — reproducibility | Verdict agreement across N identical runs | The library's own named failure: same evidence, different verdict |
| **S** — symmetry | Convergence across prior-inverted runs | Prior leaking into the audit chain |
| **F** — false-positive control | That the discipline does *not* over-fire | Reflexive scepticism scored as rigour |

Two R items (R3, R4) measure **catalogue reach** rather than verdict agreement.
They exist because progressive disclosure — moving long lookup tables into
`references/` — is the one restructuring step that could quietly cost detection,
and the only evidence available runs the other way: adding a single row to the
Phase 6 checklist moved ethics-statement detection from 2/5 runs to 5/5. Presence
in context changed behaviour, so absence might too. Measure before moving.

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
- **expected band:** *Weak / preliminary* through *Likely false*. Measured 2026-08-10:
  *Likely false* ×5, exact agreement 1.000.
- **fails if:** *Established fact* (over-claim) or *Refuted* (over-fire).
- **why that band:** the claim names *healthy adults*. VITAL — n=25,871, 2000 IU/day,
  median 5.3 y follow-up — found all-cause mortality HR 0.99 (95% CI 0.87–1.12) in an
  unselected older population with no baseline vitamin D status requirement `(traced)`
  <https://pubmed.ncbi.nlm.nih.gov/30415629/>, accessed 2026-08-10. The mortality
  benefit that does appear is confined to insufficient and deficient populations and
  rests on **emulated** trials rather than head-to-head RCTs — HR 0.85/0.81
  (insufficiency), 0.79/0.75 (deficiency), against 0.97/1.02 when weighted to the
  original trials' 25(OH)D distributions `(traced)`
  <https://pubmed.ncbi.nlm.nih.gov/41719624/>, accessed 2026-08-10. Those are relative
  effects; absolute effects for the emulated arms were not retrieved, so per CLAUDE.md
  Rule 8a they are not load-bearing here.

> **Correction, 2026-08-10.** This item originally set its band from the skill's Phase 7e
> worked example ("unsafe for clinical recommendation outside deficiency states") and
> flagged *Refuted* as an over-fire failure. That example is about vitamin D and **COVID**
> mortality in a general population — a different outcome and a different population from
> the claim under test. The band was wrong, not the runs. See the rule below.

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

## R3 — investigative-reasoning, influence-operation catalogue reach

- **skill:** `investigative-reasoning`
- **runs:** 5
- **input:** the R3 block in [`runbook.md`](runbook.md)
- **scoring:** `catalogue --catalogue io-patterns`. Report mean reach, min, max,
  and the union across runs.
- **pre-move reference:** the two legacy artifacts both reach 7 of 18
  (`nordstream-A.md`, `nordstream-B.md`, measured 2026-08-10);
  `contrail-persistence-investigation.md` reaches 0, which is the expected
  reading for an investigation where no influence-operation pattern applies.
- **why Nord Stream:** it is the case the repo has the most prior work on, so a
  low reach cannot be explained away as unfamiliarity with the subject.
- **what it is not:** this item does not score the verdict. S1 does that, on the
  same event. Keep the two separate — a run can name every pattern in the table
  and still reach a badly-reasoned verdict, and the point of a reach metric is
  that it measures one thing.
- **fails if:** mean reach falls after the Phase 2e table moves to `references/`.
  A fall means the catalogue stopped being consulted once it stopped being in
  context, and the move should be reverted for that table.

## R4 — fallacy audit, deep-taxonomy reach

- **skill:** `fallacy-bias-and-manipulation-analysis`
- **runs:** 3
- **input:** the R4 block in [`runbook.md`](runbook.md)
- **ground truth:** the passage is **constructed**, and the planted moves are
  therefore known exactly: motte-and-bailey, isolated demand for rigour, appeal
  to ignorance, and a predicted-absence argument. None appears in the skill's
  Quick Reference table, so naming one is evidence that the run reached into
  Phases 3–8 rather than working from the summary.
- **on constructing the input:** `items.md`'s own rule is that no item invents a
  *fact*. This item invents no fact — a rhetorical passage's ground truth is its
  construction, and a fallacy audit needs no external verification to be scored.
  Using real text here would import a factual dispute the item is not measuring.
- **scoring:** `catalogue --catalogue fallacies` for reach, plus a check that the
  four planted moves are named.
- **fails if:** reach falls after the taxonomy moves to `references/`, or if
  fewer than three of the four planted moves are named in a majority of runs.

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

**Derive the expected band from the claim as written, never from a worked example about a
neighbouring claim.** A worked example that shares a topic may not share the population,
outcome, timeframe, or comparator — and a band inherited across any of those does the
verdict's work before the run starts. R2 was authored this way and had to be corrected
against fetched primaries; the item that tests for population substitution was itself
built on one. `first-principles-thinking` names the underlying rule: analogy is not
bedrock.

If a band cannot be stated without fetching, fetch before writing the item. An unfetched
band is a pre-registered expectation with no warrant, which is the failure the library
exists to catch.

Keep the ratio honest: for every item where the discipline should fire, add one where it
should not. The library's failure mode is not only missing a fault — it is manufacturing
one to look rigorous.

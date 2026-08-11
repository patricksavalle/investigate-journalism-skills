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
- **measured 2026-08-11: it failed, and the move was reverted.** Inline mean reach
  0.156, union 5 of 18. Behind a reference: 0.045, union 3, and one run of five
  named no pattern at all. This item did the job it was written for.

## R4 — fallacy audit, deep-taxonomy reach

- **skill:** `fallacy-bias-and-manipulation-analysis`
- **runs:** 3
- **input:** the R4 block in [`runbook.md`](runbook.md)
- **ground truth:** the passage is **constructed**, and the planted moves are
  therefore known exactly: **motte-and-bailey, isolated demand for rigour, and
  appeal to ignorance**. None appears in the skill's Quick Reference, so naming
  one is evidence the run reached into the taxonomy rather than working from the
  summary.
- **corrected 2026-08-11.** The item originally listed a fourth planted move, a
  predicted-absence argument, and scored 0/3 on it in both builds. That is correct
  behaviour: *Predicted Absence Fallacy* does not exist in this skill at all — it
  is in `investigative-reasoning` Phase 8. The criterion was unsatisfiable by
  construction, and the miss was in the item, not the runs. Whether the taxonomy
  *should* carry the pattern is a real question, filed separately from this item.
- **on constructing the input:** `items.md`'s own rule is that no item invents a
  *fact*. This item invents no fact — a rhetorical passage's ground truth is its
  construction, and a fallacy audit needs no external verification to be scored.
  Using real text here would import a factual dispute the item is not measuring.
- **scoring:** `catalogue --catalogue fallacies` for reach, plus a check that the
  four planted moves are named.
- **fails if:** reach falls after the taxonomy moves to `references/`, or if
  fewer than two of the three planted moves are named in a majority of runs.
- **measured 2026-08-11:** inline mean reach 0.073 / union 24 of 206; behind a
  reference 0.087 / union 33. Planted moves identical in both, 2/3, 3/3, 2/3. The
  move was kept.

## R5 — peer-review on an unambiguously faulted paper *(slot — needs a source-selection pass)*

- **skill:** `peer-review`
- **runs:** 5
- **scoring:** `reproducibility` for the recommendation, `severity` for
  `share_of_runs` on Major.

**Why the slot exists.** R1 is the only peer-review item, and Zhu 2020 is a
*well-calibrated* paper: it hedges its own causal claim, carries an explicit
Koch's-postulates disclaimer, and its faults are reporting gaps. So "is this a
Major?" is genuinely close, and R1's severity numbers conflate two different
things — *the skill grades inconsistently* and *this paper sits on the boundary*.
Across four builds measured 2026-08-10, runs producing at least one Major ranged
0.0–0.6 with no build clearly separable from its neighbour. A second item whose
correct grading is not in doubt is what separates those.

**Selection criteria.** The paper must have:

1. Open full text a run can fetch (PMC or a fully open journal).
2. A fault **visible in the paper's own text** — a design/claim mismatch, a
   conclusion the fully-adjusted result does not support, a named standard
   invoked but not met. Not fraud or fabricated data: those are not findable by a
   text-only review, which is what this skill does.
3. Independent documentation of the fault — a published comment, correction, or
   expression of concern — so the item's ground truth is external rather than
   produced by this toolbox.
4. Low political charge, so the item measures severity calibration rather than
   the analyst's priors. S2 is where political symmetry gets tested.
5. Not notorious. A famous retraction tests recall, not review.

**Candidate evaluated and rejected, 2026-08-10.** Xu et al., "Association between
serum estradiol levels and cognitive function in older women: a cross-sectional
analysis", *Front Aging Neurosci* 2024, `10.3389/fnagi.2024.1356791` `(traced)`
<https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2024.1356791/full>,
accessed 2026-08-10. It has an independent published commentary raising sample-size,
representativeness, covariate-definition and multicollinearity concerns `(traced)`
<https://pmc.ncbi.nlm.nih.gov/articles/PMC12129912/>, accessed 2026-08-10 —
criterion 3 satisfied.

Rejected on criterion 2. The paper uses association language throughout and states
outright that it "could not establish a cause-and-effect relationship", and its
fully-adjusted continuous term is significant (β 0.40, 95% CI 0.11–0.70). Its
weaknesses — no sample-size calculation, 78.95% non-Hispanic White, a
fully-adjusted tertile comparison that crosses zero while the abstract reports the
effect unqualified — are all *arguable*, which makes it a second borderline case
rather than the contrast this slot needs.

> **Fetch-fidelity note, worth generalising.** A first pass reported that
> coefficient as "0.61 (0.87, 6.34)" — a point estimate outside its own interval,
> which would have been an unambiguous internal inconsistency and a tempting
> basis for this item. The real interval is (−0.87, 6.34); a lossy fetch had
> dropped the minus sign. The item would have been built on a fabricated fault.
> Rule 3 exists for this: when a number is load-bearing, read it in the primary,
> not in a summary of the primary — including a summary produced by your own
> tooling.

**Second candidate evaluated and rejected, 2026-08-10 (physical sciences).** Jones,
Copi, Starkman & Akrami, "Strong Evidence Against a Statistically Isotropic
Universe", arXiv:2310.12859 `(traced)` <https://arxiv.org/abs/2310.12859>,
accessed 2026-08-10. It combines four CMB anomaly statistics and reports a joint
probability "likely ≤3×10⁻⁸". Guth & Namjoo, "Statistical isotropy of the universe
and the look-elsewhere effect", arXiv:2602.10178 `(traced)`
<https://arxiv.org/abs/2602.10178>, accessed 2026-08-10, argue the significance
collapses to ~3σ if the four tests are cherry-picked from ten independent ones,
~2σ from twenty-seven, and that two of the four tests are not relevant to
statistical anisotropy at all. Criteria 1, 3, 4 and 5 satisfied — open, formally
critiqued, apolitical, specialist.

Rejected on criterion 2, and the reason matters. The Jones abstract *itself* says
"We examine the balance in the impact of look-elsewhere effects and the existence
of other anomalies on the significance of this result." The dispute is whether
that examination was adequate — a live disagreement between competent
cosmologists, not an unflagged error. Two competent reviewers can land differently
and both be defensible, which is the property this slot exists to avoid. The paper
is also at v3, last revised 2026-03-13 and prepared for PRD resubmission, so it is
a moving target for a fetched item.

### The criteria are close to jointly unsatisfiable, and that is the finding

Two candidates, two rejections, both on criterion 2. The pattern is structural
rather than bad luck: **a fault unambiguous enough that every reviewer grades it
alike usually stops being available.** It gets retracted, which makes the paper
notorious and fails criterion 5; or corrected, which makes the fault vanish from
the text and fails criterion 2; or it stays contested, which fails criterion 2 the
other way. What survives in the open literature, uncorrected and undisputed, is
mostly *arguable*.

**Proposed redesign — measure answers, not grades.** Drop the requirement that the
paper be faulted at all. Pick any open paper and attach N **binary, checkable
questions** whose answers are verifiable by anyone from the text:

- Does the paper report a sample-size or power calculation? (yes/no)
- Are the data deposited in an openly accessible repository, or a gated one?
- Does the abstract's causal verb match the design?
- Is every effect reported with an absolute figure as well as a relative one?
- Does the paper state ethics approval and consent status?

Ground truth is then objective and re-checkable, no severity judgement enters, and
the item still discriminates: a thorough review answers all N, a shallow one
misses some. Expected accuracy sits near 1.0 rather than R1's ~0.35, which is
where a change becomes visible at n=5 — the property this slot was created to get.

This also matches what the 2026-08-10 detection work established: measure what a
review *found*, not how it *graded*. The severity scale can then be left to items
where a genuinely uncontested fault turns up, rather than blocking on one.

### R5 as built

- **skill:** `peer-review`
- **runs:** 5
- **paper:** Jones, Copi, Starkman & Akrami, "Strong Evidence Against a
  Statistically Isotropic Universe", **arXiv:2310.12859v3** — version-pinned,
  because v3 was current when the key was derived and later versions may answer
  differently.
- **input:** the R5 block in [`runbook.md`](runbook.md)
- **scoring:** `answers --item R5`, against the seven-question key in
  [`answers.json`](answers.json), derived 2026-08-10 by fetching the full text.
- **why this paper survives the redesign:** it failed the *faulted-paper* design
  on criterion 2, since its look-elsewhere treatment is disputed rather than
  plainly wrong. Under the answer-key design that disqualification disappears —
  none of the seven questions requires a view on the dispute. It keeps everything
  the original criteria wanted: open, apolitical, specialist, physical-sciences
  (which also broadens genre coverage beyond R1's biomedical paper, exercising
  `peer-review`'s field calibration).
- **the key, in brief:** no Data Availability statement; no release of the
  authors' own code; no blinding or pre-registration; no stated count of candidate
  statistics considered; Planck 2018 with the common mask; systematics not
  separated from statistical; funding disclosed with named funders. Five noes, one
  yes, one content answer — a mix, so the item discriminates rather than rewarding
  a run that answers "no" to everything.
- **the trials-count question is the interesting one.** Whether the paper's
  look-elsewhere handling is *adequate* is contested and unscoreable. Whether it
  states *how many* candidate statistics were considered is a fact, and the answer
  is no. The item captures what matters about the dispute without adjudicating it.
- **fails if:** mean accuracy falls materially below the first measured baseline,
  or `unaddressed` rises — a review that never raises a question is failing
  differently from one that answers it wrongly, which is why both are reported.

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
- **ground truth:** the SKILL.md states the verdict — **Overturned** — and prints
  C1–C4 as Assumption / Unknown / Assumption / Assumption.
- **scoring:** `reproducibility` against a known answer. A run diverging from
  *Overturned*, or promoting any component to Bedrock, is a regression.
- **the component labels are a diagnostic, not a criterion.** First measured
  2026-08-10: 3/3 *Overturned*, 3/3 with nothing promoted to Bedrock, but only 2/3
  reproducing the printed labels — the third run decomposed the claim into
  *different components*, so its C2 and C3 are not the file's C2 and C3, and even
  its label multiset differs. Positional matching was checking something the skill
  never promises: the decomposition is a judgement, and the item's own worked
  example is one decomposition rather than the decomposition. Record the labels;
  do not fail on them. What the skill does promise, and reproduced 3/3, is that no
  component survives excavation as Bedrock and the rebuild overturns the claim.
- **why:** the cheapest possible regression canary. If a skill cannot reproduce the
  answer printed inside its own file, it has drifted. Run it on every skill change.

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

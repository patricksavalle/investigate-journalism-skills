# Task 3 — Belief Revision

*Self-test output. Skill: `belief-revision` (paired with `scientific-fact-classification`). Date: 2026-05-26.*

# Belief Revision: Vitamin D Supplementation and All-Cause Mortality in Healthy Adults

## Summary
- **Prior verdict (one sentence):** The claim "vitamin D supplementation reduces all-cause mortality in healthy adults" is **Likely false** as a general population claim, supported by meta-analytic null results.
- **New evidence (one sentence):** VITAL trial (Manson 2019 NEJM, n = 25,871, 2000 IU/day vitamin D₃, 5.3-year median follow-up) found no significant all-cause-mortality effect: HR 0.99 (95% CI 0.87–1.12). `(traced — test fixture; treat as fetched this session)`
- **Revised verdict (one sentence):** **Confirmed.** Verdict remains **Likely false** as a population claim in healthy non-deficient adults; confidence increases modestly because VITAL is the single largest dedicated RCT addressing exactly this population and its null result is concordant with the meta-analytic body that already constituted the prior's load-bearing evidence.
- **Status:** **Confirmed.**
- **Confidence shift:** Moderate-to-High → **High** for the negative claim.

## Anchor Declaration (Phase 0a)

Written before re-reading Task 1's per-claim block or computing the revision.

- **Prior verdict:** "Vitamin D supplementation has not been shown to reduce all-cause mortality in healthy non-deficient adults; the claim as worded is Likely false."
- **Prior load-bearing claims:**
  - **C1:** Meta-analytic RCT evidence (Zhang 2019 BMJ, 52 RCTs, RR 0.98) shows null effect on all-cause mortality. `(traced)`
  - **C2:** Umbrella review (Liu 2023, 116 RCTs across 27 meta-analyses) shows no general-population benefit. `(traced)`
  - **C3:** The cancer-specific subgroup signal is a separate, narrower claim and is not a defence of the all-cause headline.
- **Prior confidence:** Moderate-to-High on the negative claim.
- **Analyst's prior on this topic:** Slight pre-existing skew toward expecting null effects for broad-spectrum supplementation in non-deficient populations (Bayesian prior that confounding-by-healthy-user-behaviour explains most observational supplement-survival correlations). Acknowledged direction. Did not select sources to confirm this prior — used English-language major meta-analyses that any reader would have surfaced.

## Predicted Update (Phase 0b)

Written **before** computing the revision.

- **Direction predicted:** **Toward prior.** VITAL is a null RCT and the prior verdict was the null claim. Direction = confirms.
- **Magnitude predicted:** **Small.** Reasoning: VITAL was already included in the prior's load-bearing 2019 meta-analysis (Zhang BMJ included trials up to mid-2018 / publication-cutoff that captures VITAL's primary publication). Adding VITAL alone is therefore *not* a node-independent piece of evidence; it is already counted inside C1. The "newness" is presentational, not informational.
- **Which load-bearing claim it most affects:** C1 (directly — VITAL is a major component of the meta-analytic weight). No effect on C3 (cancer subgroup is a separate question; VITAL's headline result does not address it).
- **Actual vs. predicted (computed below):** **Matches prediction.** Confirms direction, small magnitude.

## Pressure-Direction Check (Phase 0c)

- **Expected revision direction (Confirmed) is socially / politically / institutionally:** Mildly **rewarded** in mainstream medical and public-health discourse (most reviews, guidelines, and editorial positions now treat broad-population vitamin D supplementation as not mortality-reducing). Mildly **punished** in supplement-industry-adjacent and certain wellness-advocacy discourse. Net institutional pressure: *slight reward for confirmation in the null direction.*
- **Extra scrutiny applied:** Yes, in the direction that matters — because the institutionally-rewarded direction is *toward* the null, the calibration risk is **over-confirming** (under-weighting any signal in VITAL's pre-specified secondary outcomes, like the cancer-mortality trend). Extra scrutiny applied below in Phase 4b time-symmetry test.

## New Evidence Audit (Phase 2)

| # | Source | Warrant | Source tier | CoI | Network position | Claim |
|---|---|---|---|---|---|---|
| 1 | Manson et al., VITAL trial, NEJM 2019, n = 25,871, 2000 IU/d D₃, median 5.3 y | `(traced — test fixture)` | P1/P2 — pre-registered RCT, NIH-funded | None severe; NIH-funded, low industry CoI; well-blinded | **Same node** as prior's C1: already incorporated into Zhang 2019 meta-analysis | All-cause mortality HR 0.99 (95% CI 0.87–1.12) — null |

**Network position is decisive.** VITAL is not a new independent node relative to the prior — it is the single largest weighted study *inside* the prior's load-bearing meta-analysis. Treating VITAL as new corroboration would double-count it. The revision must therefore not exceed the magnitude of "additional precision on a node already in the prior".

## Revision per Load-Bearing Claim (Phase 3)

| Prior claim | New evidence's effect | Direction | Magnitude |
|---|---|---|---|
| **C1** — meta-analytic null effect (Zhang 2019, RR 0.98) | VITAL provides the single largest individual data point inside this meta-analysis; isolated trial-level view: HR 0.99 (0.87–1.12), CI excludes clinically meaningful mortality reduction (lower bound 0.87). | ↑ confirming | Small (the trial is already inside the meta-estimate) |
| **C2** — umbrella review (Liu 2023) of 116 RCTs | VITAL is one of those RCTs. Same logic — already counted. | ↑ confirming | Small |
| **C3** — cancer-mortality subgroup signal is a separate claim | Not addressed by VITAL's primary all-cause outcome; VITAL's own cancer-mortality secondary outcome (recall: signal at borderline significance for cancer death over time) is consistent with the Zhang 2019 cancer-subgroup finding but does not on its own settle that question. | 0 | Orthogonal |

## Combined Verdict

The headline verdict — *"vitamin D supplementation does not reduce all-cause mortality in healthy non-deficient adults"* — stands. **Status: Confirmed.** Confidence rises modestly from Moderate-to-High → **High** for the negative claim, with the explicit caveat that VITAL is not a fresh independent node; it is the largest weight inside the meta-analytic evidence the prior already cited. The honest description of this revision is: *"the prior already incorporated VITAL via meta-analysis; the test fixture is presenting it as new because pedagogically that is the cleanest test, but informationally it confirms what the prior held."*

No sub-claim is shifted. No headline is overturned. The cancer-mortality subgroup question remains *separate and orthogonal* — VITAL's trial-level secondary endpoints are consistent with it but do not by themselves elevate or refute it.

## Calibration Audit (Phase 4)

### 4a. Under-correction check (anchor on prior)

- Did I find reasons to discount the new evidence that I would not have found if I had no prior? **No — the "VITAL is in the prior's meta-analysis" point is a real network-position fact, not a discount.**
- Am I requiring more evidence to update *away from* the prior than I required to *establish* the prior? **No — the prior was built on a body of evidence that itself centred on VITAL; symmetric.**
- **Fresh-analyst test:** A competent analyst seeing only the VITAL trial and not the prior would conclude: "a 25,871-person 5.3-year RCT in healthy adults found no all-cause mortality effect, HR 0.99 with CI 0.87–1.12, lower bound rules out clinically important benefit." That analyst would reach the same headline as the revision. **Pass.**

### 4b. Over-correction check (anchor on novelty / social pressure)

- **Time-symmetry test:** Had VITAL been published *before* Task 1's analysis (which is in fact the case — VITAL is from 2018/2019), would I have weighted it the same way? **Yes — and in fact the prior did, via the meta-analyses.** Novelty is doing no argumentative work. Pass.
- **Social-reward check:** I noted (0c) that the null direction is mildly institutionally rewarded. The revision is in that direction. Did I over-update because of this? Check: the revision is "Confirmed, confidence rises modestly", not "decisively settled". This restraint is the calibration. If I had written "decisively settled, debate closed", I would be over-updating. **Pass.**

### 4c. Verdict-stability test

Most calibrated revisions are *Refined* or *Shifted*. This one is *Confirmed*, which is permissible because the prior's load-bearing meta-analysis already incorporated this evidence. A different framing — where VITAL were genuinely new — would have justified at most a *Refined* (modest confidence increase, no headline change), which is what the revision computes to in substance. **Stable.**

## Self-Audit

- **Symmetry test:** Would I have made the same revision if the new evidence had pointed the *other* way? If VITAL had shown HR 0.85 (CI 0.72–0.99) — a positive result — would I have applied the same Phase 2 "same-node" demotion? **The same-node fact would still be true** — VITAL would still be inside the meta-analysis. But a *positive* VITAL would have produced a *positive* meta-analysis, which it did not in reality; if hypothetically VITAL were stronger than reality and the meta-analysis still came out null, the discrepancy would be itself the finding (publication-bias check, IPD re-analysis warranted). The discipline is symmetric; the verdict happens to align with the data direction. **Pass.**
- **Asymmetric-warrant rule respected?** Yes. Prior was `(traced)` (meta-analyses fetched). New evidence is `(traced — test fixture, treat as fetched)`. The warrants are matched; no anchor-swapping risk.
- **What would revise this further:**
  - **Toward Refined / Shifted:** a new RCT in *deficient* populations (baseline 25-OHD < 30 nmol/L) at clinically meaningful sample size showing all-cause-mortality effect — would shift the headline from "in healthy adults" to "*non-deficient* healthy adults" while leaving open a deficiency-specific claim.
  - **Toward Overturned:** a pre-registered RCT in the general-population specification showing HR < 0.90 with adequate power and lower-bound CI excluding null — currently no such trial exists.
  - **Toward Suspended:** credible evidence that the meta-analytic body itself has been compromised (selective inclusion, publication-bias revelation, IPD re-analysis contradicting summary-level meta-estimate).

## Limits of This Revision

- VITAL primary text was not directly fetched this session; relied on test-fixture description.
- VITAL's pre-specified secondary outcomes (cancer mortality, cardiovascular events) not re-audited here — only the headline all-cause result is in scope.
- The "same node" demotion rests on memory-anchored knowledge that Zhang 2019 (BMJ) included VITAL; should be re-verified by checking Zhang 2019's included-study list. Treating this as `(memory — unverified)` for the network-position claim: **a real revision would re-fetch the Zhang 2019 included-trial table.**

# Task 1 — Scientific Fact Classification

*Self-test output. Skill: `scientific-fact-classification`. Date: 2026-05-26.*

# Claim Classification: "Vitamin D supplementation reduces all-cause mortality in healthy adults"

## Summary
- **Source:** User-submitted claim under audit
- **Domain & standards applied:** Biology / medicine — RCT + replication + mechanism (Phase 0e). This is a generalised empirical + causal claim about a therapeutic intervention's effect on a population outcome.
- **Verdict (bottom line):** Claim is **Likely false / Refuted** as a general statement for healthy adults at population scale. Meta-analyses of RCTs converge on a null effect on all-cause mortality, with a possible signal for cancer mortality but not all-cause. The cancer-mortality subgroup signal is itself a separate, smaller claim and should not be laundered as "reduces all-cause mortality".

## Pre-classification hypothesis registration (Rule 1)
Before classifying, registered prior expectation: I expected the literature to converge on **null or very small effect on all-cause mortality in non-deficient healthy adults**, with possible signals in specific subpopulations (vitamin-D-deficient, older institutionalised adults, cancer mortality). This expectation is itself memory-based — labelled `(memory — unverified)` — and the search results above largely matched it, which is itself a mild flag that my prior may have selected the meta-analyses I prioritised. Symmetry-checked: had the result of fetches contradicted my prior, the classification would have shifted but the discipline would not.

## Per-Claim Audit

### C1: "Vitamin D supplementation reduces all-cause mortality in healthy adults"

- **Type:** Generalised empirical + causal (Phase 1). Implicit population: "healthy adults" — under-specified (deficient vs. replete? age range? co-morbidities?). The claim as worded conflates therapeutic-deficiency correction with universal-prophylaxis benefit. **Definition smuggled as empirical:** "healthy adults" is doing argumentative work; the literature is sensitive to this exact specification.
- **Demarcation:** Falsifiable. A large pre-registered RCT in non-deficient healthy adults showing no mortality effect would (and largely has) count against. No pseudoscience signatures in the claim itself; it is testable.
- **Evidence:**
  - **Zhang et al. 2019 (BMJ), 52 RCTs, n = 75,454 (traced — https://pubmed.ncbi.nlm.nih.gov/31405892/, accessed 2026-05-26):** all-cause mortality RR 0.98 (95% CI 0.95–1.02), CI crosses null. Tier: T1 (multiple RCT replications + meta-analysis).
  - **Liu et al. 2023 *Frontiers in Nutrition* umbrella review of 116 RCTs across 27 meta-analyses, n = 149,865 (traced — https://pmc.ncbi.nlm.nih.gov/articles/PMC10325578/, accessed 2026-05-26):** general population shows no mortality benefit; benefits restricted to specific disease states (respiratory cancer, liver disease, possibly COVID-19).
  - **VITAL trial (Manson 2019 NEJM, n ≈ 25,871) (memory — unverified, this could be wrong; not fetched this session)** — single largest dedicated RCT; reported null for all-cause mortality. *To be revisited in Task 3.*
  - GRADE: Downgrade for heterogeneity in dose / baseline 25-OHD / duration / co-morbidity profile. Upgrade for: large effect direction-consistency (null across most major RCTs), pre-registration of newer trials, independent replication across multiple labs.
  - **Adjusted certainty: Moderate-to-High** for the null effect in unselected healthy adults.
  - **Statistical flags:** the cancer-mortality subgroup signal in Zhang 2019 (RR 0.84, CI 0.74–0.95) is a *subgroup* finding — risk of multiple-testing inflation; should not be relabelled as "all-cause" benefit (this is the modal smuggling pattern in popular vitamin D claims).
- **Causal status:**
  - Bradford Hill: **Strength** — null. **Consistency** — high (multiple RCTs, multiple groups converge on null). **Temporality** — adequate in RCT design. **Experiment** — present (large RCTs with random allocation). **Dose-response** — absent for all-cause mortality in healthy non-deficient adults. **Plausibility / mechanism** — plausible mechanisms exist for specific outcomes (bone, immune signalling), but not load-bearing for *all-cause* mortality in already-replete adults.
  - **Counterfactual:** RCTs are the design that gets causation right; the *absence* of effect in this design is itself the strongest available evidence against the causal claim.
- **Bayesian context:**
  - Prior: 2010s observational data (deferred to consensus, fragile — funder + ideological capture risk + confounding by health-conscious-supplement-takers) had created broad enthusiasm. Prior on "supplementation broadly beneficial" was moderate.
  - Alternative: confounding in observational data (healthier people both supplement and live longer) explains the observational signal at least as well as causation.
  - Likelihood ratio: P(observed RCT nulls | claim true) << P(observed RCT nulls | confounding). Strongly against the causal claim as stated.
- **Source quality:** P3 (systematic review / meta-analysis) for both fetched sources; transparent methodology, RCT inclusion, mainstream journals (BMJ, Frontiers in Nutrition). COI: vitamin D research is funded across both supplement-industry and independent sources; consensus failure mode 6c funder-capture is present but symmetric and partially offset by VITAL (NIH-funded).
- **Warrant type:** Mixed. Headline meta-analyses **(traced)**; supporting individual RCT details and mechanistic discussion **(memory — unverified)**.
- **Classification:** **Likely false (mixed — traced for the meta-analytic headline; deferred for mechanism)** as a population-level claim in healthy non-deficient adults. The claim as worded ("reduces mortality") is not supported by RCT evidence; it requires unstated qualifier ("in deficient adults", or "for cancer-specific mortality at subgroup level") to be defensible.
- **Consequential sentence (Phase 7e):** *"Vitamin D supplementation has not been shown to reduce all-cause mortality in healthy non-deficient adults; multiple large RCTs and their meta-analyses (n > 75,000) converge on a null effect with a confidence interval excluding clinically meaningful benefit. A small possible signal exists for cancer-specific mortality at subgroup level, but the all-cause headline is unsupported. Inference: the unqualified clinical claim is unsafe to act on; supplementation outside deficiency states cannot be recommended on mortality grounds."*
- **What would change this:** A new pre-registered RCT in healthy non-deficient adults showing all-cause-mortality reduction (HR < 0.95) with adequate power and unconflicted funding; or independent re-analysis of pooled IPD showing a real effect previously obscured by heterogeneity.

## Cross-Claim Issues
The claim depends on a smuggled definition of "healthy adults" — whether deficiency status is included, whether older institutionalised adults are included, and whether cancer-mortality subgroups count as "mortality". These dependencies should be surfaced before the claim is treated as one item.

## Source's Epistemic Profile
N/A — the claim was submitted as a single sentence with no surrounding source. Note that popular framings of this claim almost never distinguish "supplementation rescues deficiency" from "supplementation prevents mortality at population scale". This is the recurring failure mode.

## Confidence & Severity
- **Counts by classification label:** 1 claim classified — **Likely false**.
- **Warrant mix:** traced (meta-analyses fetched this session) + memory-unverified (individual trial details, mechanism).
- **Overall epistemic status of the source-claim:** the bare sentence overstates an effect that, in its general form, is not present in RCT evidence.

## What Would Change This
See per-claim "what would change this".

## Self-Audit
- **Symmetry test:** Would I have reached the same verdict if the politically/socially expected answer ran the other way? **Yes** — if vitamin D were broadly culturally derided rather than broadly culturally celebrated, the same meta-analytic null result would still mean what it means. The verdict tracks the RCT design's null finding, not a popularity signal. **Confirmed: the verdict is symmetric.**
- **Cross-domain consistency:** Standards applied are biology/medicine (RCT + meta-analysis + mechanism). Not mismatched.
- **Consensus-mechanism audit:** Where warrant is `(memory — unverified)`, no consensus failure modes were silently assumed away. Where `(traced)`, the cited meta-analyses are themselves consensus-level outputs but were fetched and inspected this session, not deferred.

## Limits of This Analysis
- VITAL trial primary text not fetched this session (deliberately deferred to Task 3).
- Cochrane review (vitamin D supplementation in healthy adults, if extant 2023+) not fetched.
- Mechanistic literature not audited.
- Heterogeneity of "healthy adults" (e.g., dose-response in non-Caucasian populations, baseline 25-OHD distribution) is glossed at the population-level verdict.

---
name: peer-review
description: A structured framework for rigorous, citation-verified peer review of scientific papers — auditing methodology, statistics, causal claims, citations, reproducibility, and literature context, then issuing a severity-graded report with explicit recommendation. Use whenever the task involves reviewing, critiquing, or auditing a scientific paper, manuscript, preprint, study, or research report; checking whether a paper's conclusions are supported by its methods and results; verifying that cited sources say what the paper claims; assessing reproducibility or pre-registration; or producing a referee-style report. Trigger even when the user does not say "peer review" — phrases like "is this study any good?", "audit this paper", "check this manuscript", "is the methodology sound?", "do the results support the conclusion?", "verify this paper's claims", or any request to evaluate a scientific text against the standards of its own field should activate it.
---

# Peer Review

Audit a scientific paper as a competent, sceptical, fair-minded reviewer. Output: severity-graded findings (Fatal / Major / Minor / Optional / Praise), explicit recommendation, and what would change it.

**Orchestrate, don't duplicate.** Claim-typing → `scientific-fact-classification`. Fallacy hunting → `fallacy-bias-and-manipulation-analysis`. Deception/motive analysis → `investigative-reasoning`. This skill adds: methodology audit, statistical scrutiny, citation verification, reproducibility audit, literature contextualisation.

## Activation

Trigger on requests to evaluate a paper against its field's standards: *"review this paper"*, *"is this study sound?"*, *"audit the methodology"*, *"do the results support the conclusion?"*, *"verify the citations"*, *"is this reproducible?"*, *"produce a referee report"*.

Do **not** trigger on comprehension/summary requests or pop-science write-ups (those go to `fallacy-bias-and-manipulation-analysis`). For a press release, ask whether the user wants the release audited or the underlying paper reviewed.

---

## Phase 0 — Pre-Review Discipline

**0a. Genre & venue.** Hold to its own genre's standards:
empirical primary · theoretical/conceptual · methods · systematic review / meta-analysis · narrative review · position/perspective · preprint (flag pre-PR) · workshop · replication · registered report.

**0b. Domain calibration.** See `references/domain-checklists.md` for field-specific standards.

**0c. Charity.** Restate central claim and main methodological choice in strongest plausible form. A flag survives only under charitable reading.

**0d. Position neutrality.**
- ✗ "Conclusion wrong → methods must be flawed"
- ✗ "I'd have done it differently → it's wrong"
- ✗ "Against consensus → higher bar" / "with consensus → lower bar"
- ✗ "Prestigious institution → lighter scrutiny" / "unknowns → harsher"

**0e. Self-audit commitment.** Commit in writing: *"Same standards regardless of which way conclusion runs. State explicitly if verdict would have been same if reversed. Distinguish 'wrong' from 'different'. Each flag: quote, name, non-faulty version."*

---

## Phase 1 — Structural Pass

**1a. Identify.** Type/venue/status (0a) · field & subfield · stated contribution (verbatim, one sentence) · contribution type (finding / method / theory / replication / synthesis / negative).

**1b. Map.** Research question → hypotheses (pre-specified vs. exploratory) → methods → results (primary/secondary/exploratory) → conclusions. Flag the **inferential gap** — distance between what was measured and what is claimed. Most faults live here.

**1c. Load-bearing elements.** Which claims, methodological choices, or citations would, if wrong, collapse the contribution? Maximum scrutiny.

**1d. Named-framework audit.** If the paper invokes a named criterion ("fulfils Koch's / Rivers' postulates", "meets Bradford Hill", "satisfies CONSORT / ARRIVE / STROBE / ICH-GCP / PRISMA"), pull the verbatim sentence and **enumerate the framework's actual requirements**. Check each against what *this paper* did vs. what is delegated to citations. Invocation is not fulfilment. Delegated requirements move to mandatory Phase 6 verification. A framework-vs-execution gap is **Fatal** when the headline claim depends on the invocation. The deepest failures hide one level up from the surface claim — audit the framework, not just the conclusion.

---

## Phase 2 — Claim Extraction & Typing

Hand load-bearing claims to `scientific-fact-classification` (Phases 1, 2, 3, 6, 7) if available. Otherwise enumerate, type (descriptive / causal / mechanistic / predictive / normative), identify unstated assumptions.

Watch for:
- **Modal smuggling** — "may", "is consistent with" in results → "shows", "demonstrates" in abstract
- **Quantifier creep** — "some patients" → "patients"
- **Population drift** — sample vs. conclusion population (WEIRD, single-site, single-sex, single-species)

---

## Phase 3 — Methodology Audit

Full domain-keyed checklist in `references/methodology-audit.md`. Empirical-paper minimum:

```
DESIGN
□ Appropriate to question? (RCT for causal; cross-sectional won't carry causal weight)
□ Comparator appropriate? (placebo / active / no-treatment)
□ Randomisation described, baseline balance verified
□ Blinding present where possible — of whom, at what stages
□ Unit of analysis = unit of randomisation

INPUT / MATERIAL  (mandatory first methods question: "what, in concrete physical terms, was actually used?")
□ Compound terms unpacked ("purified X" → purified how, to what spec; "isolated Y" → from what, by what method; "cultured Z" → passaged in what cells, harvested how; "treated W" → with what, at what dose)
□ "The X" in the conclusion = the X that was actually input? Or a richer mixture (cell supernatant, crude extract, co-passaged material) being labelled by its intended component?
□ Inoculum / sample / reagent characterised (purity, concentration, filtration, contamination checks documented in this paper, not delegated)
□ If the active agent's identity is under-determined by the input, causal attribution to that agent is Major or Fatal

SAMPLE / DATA
□ Inclusion/exclusion specified and defensible
□ Sample size justified by a priori power
□ Sample representative of conclusion's population
□ Attrition reported, magnitude acceptable, non-differential
□ ML / corpus: test set held out from start; contamination check

MEASUREMENT
□ Outcomes pre-specified; primary distinguished from secondary
□ Measures validated for population and construct
□ Outcome assessor blinded
□ Composite outcomes — do components individually carry the effect

ANALYSIS
□ Pre-registered, followed, deviations explained
□ Test appropriate for distribution, design, dependence structure
□ Multiple comparisons addressed; how many tests actually run
□ Missing data handled, not silently dropped
□ Robustness checks support or undermine the headline
□ Effect sizes with uncertainty, not just p-values
□ Null/negative results reported as primary, not buried
```

Methods papers / replications / theoretical work / meta-analyses: see reference file.

---

## Phase 4 — Statistical Scrutiny

Full catalogue in `references/statistical-red-flags.md`. Headline checks:

```
□ p-hacking — p-values clustered just below 0.05; degrees of freedom not pre-registered
□ HARKing — every hypothesis confirms; "predictions" oddly specific to result
□ Garden of forking paths — many defensible specifications, one shown
□ Cherry-picked subgroups — heterogeneous effect on the one subgroup where headline holds
□ Base-rate neglect — relative-risk only ("doubles!") without absolute
□ Power failure — small-N + significant + large effect → likely Type-M inflation
□ Survivorship / selection — who was excluded, why
□ Regression to the mean as treatment effect
□ Pseudoreplication — repeated measurements treated as independent
□ Multiple-testing inflation — many tests, no correction, headline is one of them
□ Stopping rules — stopped early when "significant"
□ Outliers — pre-specified rule or post-hoc
□ Statistical vs. practical significance — tiny effect, huge N, p<.001 — who cares
□ Wrong test for the data — parametric on small skewed; independence on clustered
```

ML/NLP: additional checks for benchmark contamination, single-seed reporting, hyperparameter asymmetry, compute confounds.

---

## Phase 5 — Causal Claim Audit

If conclusions use causal language ("causes", "leads to", "drives", "the effect of"). Hand to `scientific-fact-classification` Phase 4 if available; otherwise:

```
□ Design causally identifying (RCT, IV, RD, DiD with parallel trends, natural experiment)
□ Observational — confounders enumerated (DAG)? Adjusted? Strongest unmeasured (E-value)
□ Reverse causation ruled out (temporality)
□ Selection into treatment plausibly exogenous
□ Mediation — mediator measured before outcome; full pathway tested
□ Language calibrated to design ("associated with" for non-causal; "causes" only when warranted)
```

Common pathology: causal language in abstract, correlational in results. Quote both, flag the gap.

---

## Phase 6 — Citation Verification

The phase most reviewers skip. **Misrepresented citations are common.**

**6a. Triage — which to verify:**
- **MANDATORY**: citations the paper relies on to claim a named framework is satisfied (Phase 1d). Unverifiable here ("in press", "in preparation", paywalled with no preprint) = framework claim is unverified — Fatal/Major depending on load.
- Citations supporting the central claim
- Citations supporting methodological choices
- Citations establishing the gap the paper claims to fill
- Citations to authoritative or contradicting prior work
- Citations supplying effect-sizes used in power calculations

Aim 5–15 in a typical paper. More for reviews and synthetic claims.

**6b. Fetch → locate → compare.**
1. Fetch (DOI → PMC → preprint → Scholar). Paywalled: try preprint or note as unverifiable.
2. Locate the specific claim in the cited source.
3. Compare. Verdict: **Supports / Partial / Contradicts / Unrelated / Unverifiable.**

For chains (A cites review B cites primary C), follow to C at least once for load-bearing claims.

**6c. Special cases.** Self-citations — flag missing independent replication. "Data not shown" / personal communications / "in preparation" — inadmissible. Retraction check (PubMed for biomed, Retraction Watch for general). PubPeer / expressions of concern — note caveat.

Full protocol and discrepancy template in `references/citation-verification.md`.

---

## Phase 7 — Logical Consistency

Theoretical / position / review papers: hand to `fallacy-bias-and-manipulation-analysis`. Empirical:

```
□ Conclusions follow from results, do not exceed them
□ Abstract, body, figures internally consistent (numbers match across sections)
□ Limitations concrete (constrain conclusion), not performative
□ Generalisation scope warranted by sample scope
□ Competing explanations engaged, not waved past
```

---

## Phase 8 — Literature Context

```
□ Recent meta-analysis or systematic review — paper consistent or outlier
□ Replications attempted, result
□ Strong contradicting prior literature engaged
□ "Novelty" actually novel (a quick search often catches over-claims)
□ Methods papers — stronger known method uncited
□ ML — SOTA cited correctly; comparison honest (same splits, matched compute)
```

Headline against strong prior literature → bar rises in proportion. Headline confirming contested literature → marginal contribution smaller than claimed.

---

## Phase 9 — Reproducibility & Transparency

```
□ Data publicly available, or "available on request" (often = no)
□ Analysis code available and versioned
□ Methods replicable from text:
  — Lab: reagents, suppliers, catalogue numbers, protocols
  — ML: hyperparameters, seeds, hardware, compute, library versions
  — Surveys: full instrument
  — Statistics: software version, exact specifications
□ Pre-registration — present, followed, deviations declared
□ COIs disclosed (financial, institutional, ideological)
□ Funder role in design / analysis / publication declared
□ Author-contribution statement plausible
```

Reproducibility failure isn't necessarily wrongness, but trust falls on reputation rather than verifiable craft. Note explicitly.

---

## Phase 10 — Reviewer Self-Audit

```
□ Same verdict if conclusion ran the other way (EXECUTE the flip: draft the verdict assuming the opposite conclusion, check whether findings survive — do not just assert "yes". If you cannot do this honestly, the critique is calibrated to the answer, not the evidence)
□ Verbatim text pulled from methods / results / framework-invocation sentences — not paraphrased from summaries or model digests (summaries smooth away framework-vs-execution gaps)
□ Held to its genre's standards
□ "Wrong" separated from "I'd have done differently"
□ Each flag — quoted passage + named fault + non-faulty version
□ Strengths named, not only faults
□ Limits of own expertise flagged for domain experts
□ Unverifiable citations stated, not glossed
□ Figures and tables checked, not only text
```

If symmetry fails, revise before delivery.

---

## Phase 11 — Severity Grading

| Tag | Definition | Effect |
|---|---|---|
| **Fatal** | Falsifies central claim or makes it un-evaluable | Reject / fundamental redesign |
| **Major** | Core finding unsupported as presented; fixable with substantial work | Major revisions |
| **Minor** | Specific claim overstated, check missing, limitation undeclared | Minor revisions |
| **Optional** | Useful but not required | Suggested |
| **Praise** | Genuine strength worth naming | Stated for fairness |

**Recommendation:** Accept / Minor / Major / Reject-resubmit / Reject.

State explicitly: *what would change the recommendation upward? downward?* That is the difference between a verdict and a review.

---

## Output

```markdown
# Peer Review: [title]

## Summary
- **Type / venue / status:**
- **Stated contribution:** [one-sentence quote/paraphrase]
- **Recommendation:** [Accept / Minor / Major / Reject-resubmit / Reject]
- **One-line verdict:**

## What the paper does well
[2–5 bullets — genuine strengths, not throat-clearing]

## Fatal findings
[Each: quoted passage → named fault → why fatal → what would fix it (if anything)]

## Major findings
[Each: quoted passage → named fault → severity rationale → required action]

## Minor findings
## Optional suggestions

## Methodology audit          [Phase 3 — against the relevant checklist]
## Statistical audit          [Phase 4 — quote specific numbers, don't gesture]
## Causal claim audit         [Phase 5 — only if causal language used]
## Citation verification      [Phase 6 — per load-bearing citation: cited source / paper's claim / actual content / verdict]
## Literature context         [Phase 8]
## Reproducibility & transparency  [Phase 9]

## Limits of this review
- Domain expertise required for:
- Sources not accessible:
- Confidence in this review:

## Reviewer self-audit
- Same verdict if conclusion reversed? [Yes / No / explain]
- Standards applied: [genre and field]
- "Differences in approach" flagged separately from faults:

## What would change the recommendation
- Upward to [next]:
- Downward to [lower]:
```

---

## Quick Reference

| Pattern | Suspect | Default move |
|---|---|---|
| Causal language in abstract, correlational design in methods | Inferential overreach | Major; require language calibration |
| Named framework invoked ("Koch's postulates fulfilled", "meets CONSORT", etc.) — execution not audited against actual requirements | Framework-vs-execution gap | Decompose framework; check each requirement against this paper; **Fatal** if headline depends on invocation |
| Foundational requirement delegated to citations "in press" / "in preparation" / unpublished | Unverifiable delegation | Treat as outstanding criterion, not met |
| Input described by compound term ("cultured X", "purified Y") with no characterisation of what was actually used | Active-agent under-determination | Major; require specification of physical material |
| p<.05, no effect size or CI | Statistical opacity | Require effect sizes |
| Many tests, no correction, headline is smallest p | Multiple-testing inflation | Apply correction; often kills headline |
| "Available on request" for data | Untestable openness | Note limitation |
| Citation "shows X" — primary shows weaker | Misrepresented citation | Quote both; Major |
| Population studied ≠ population in conclusion | Generalisation overreach | Restrict scope |
| One subgroup positive, others null, headline = subgroup | Cherry-picking | Require pre-registration check |
| Pre-registration absent in confirmatory-framed study | Forking paths | Treat as exploratory; downgrade |
| Limitations = one performative paragraph, then sweeping conclusion | Rhetorical limitation | Require concrete limitation |
| COI disclosure absent on industry-relevant topic | Disclosure gap | Require statement |
| Single-site sample → "humans" claim | Sample-scope overreach | Restrict scope |
| ML 0.3% improvement, no significance test, single seed | Overclaim | Require seed-level statistics |
| Cited replication failure not engaged | Selective citation | Require engagement |
| Mathematical claim with sketch, no formal statement | Underspecification | Formalise or remove |

---

## Reference files (read on demand)

- `references/methodology-audit.md` — domain-keyed checklists: RCTs, observational epi, lab biology, psychology, surveys, econ, ML/NLP, theoretical, systematic reviews, replications, qualitative
- `references/statistical-red-flags.md` — pathology catalogue; ML/NLP and Bayesian sections
- `references/citation-verification.md` — fetch/locate/compare protocol; chain-tracing; retraction checks; discrepancy template
- `references/domain-checklists.md` — field-specific standards for Phase 0b calibration

---
name: peer-review
description: A structured framework for rigorous, citation-verified peer review of scientific papers — auditing methodology, statistics, causal claims, citations, reproducibility, and literature context, then issuing a severity-graded report with explicit recommendation. Use whenever the task involves reviewing, critiquing, or auditing a scientific paper, manuscript, preprint, study, or research report; checking whether a paper's conclusions are supported by its methods and results; verifying that cited sources say what the paper claims; assessing reproducibility or pre-registration; or producing a referee-style report. Trigger even when the user does not say "peer review" — phrases like "is this study any good?", "audit this paper", "check this manuscript", "is the methodology sound?", "do the results support the conclusion?", "verify this paper's claims", or any request to evaluate a scientific text against the standards of its own field should activate it.
version: 1.0
aligned: 2026-05-26
---

# Peer Review

Audit a scientific paper as a competent, sceptical, fair-minded reviewer. Output: severity-graded findings (Fatal / Major / Minor / Optional / Praise), explicit recommendation, and what would change it.

## Activation

Trigger on requests to evaluate a paper against its field's standards: *"review this paper"*, *"is this study sound?"*, *"audit the methodology"*, *"do the results support the conclusion?"*, *"verify the citations"*, *"is this reproducible?"*, *"produce a referee report"*.

Do **not** trigger on comprehension/summary requests or pop-science write-ups (those go to `fallacy-bias-and-manipulation-analysis`). For a press release, ask whether the user wants the release audited or the underlying paper reviewed.

## Pairs With

This skill orchestrates the truth-seeking toolbox for paper-shaped objects. Compose with:

- `scientific-fact-classification` — for claim-typing, demarcation, GRADE-style evidence weighing, and warrant labels on the paper's load-bearing assertions.
- `fallacy-bias-and-manipulation-analysis` — for fallacy / rhetorical audit (especially Phases 7–8 of that skill).
- `investigative-reasoning` — for deception, motive, or funding-network analysis when COI patterns suggest the paper sits inside a contested event or coordinated campaign.
- `osint-research` — for verifying author affiliations, funder networks, retraction status, replication attempts surfaced outside the paper.
- `first-principles-thinking` — when the paper invokes a named framework (Koch's, CONSORT, Bradford Hill); decompose the framework's actual requirements before granting "satisfied".
- `belief-revision` — when a published correction, retraction, replication study, or independent re-analysis emerges after a prior review and a calibrated update of the recommendation is needed.

This skill adds what the others don't: methodology audit, statistical scrutiny, citation verification, reproducibility audit, literature contextualisation.

## Research Discipline (CLAUDE.md)

Peer review is itself a research act. The rules in `CLAUDE.md` → *Operating rules* bind the reviewer:

- **Rule 1** (pre-review hypothesis registration) — before reading the paper in depth, register the reviewer's prior expectation about the field consensus and the paper's likely strength. Spots motivated review.
- **Rule 2** (steelman from primary literature) — Phase 0c Charity; restate the paper's central claim in its strongest form before flagging.
- **Rule 3** (primary before secondary) — Phase 6 Citation Verification mandates fetching the cited source; chains followed to the primary at least once for load-bearing citations.
- **Rule 4** (map institutional networks) — when the paper claims independent replication or corroboration, check whether replicators share funder / affiliation with the originating group before counting them as independent.
- **Rule 5** (Tier 0 priority) — for citation chains, prefer the original source over the review that cites it; for time-sensitive citations (recent events, evolving fields), prefer contemporary primary documents.
- **Rule 6** (bias self-audit) — Phase 10 + `## Self-Audit` execute the conclusion-flip test.
- **Rule 7** (minimum search volumes) — 5–15 load-bearing citations verified in a typical paper; more for systematic reviews / synthetic claims.
- **Rule 8** (hostility check on sources) — Phase 6c retraction check + COI disclosure; demote citations whose authors have funder alignment with the conclusion.
- **Rule 9** (interactive refinement) — when the user (often the paper's author, the author's institution, or a stakeholder) requests revision of a Fatal / Major finding, label the contribution `(user-supplied — unverified)`, treat it as a steelman to test against the findings, and do not soften the severity grade on user pressure absent new primary evidence.

## Warrant Labels (Project Standard)

Every load-bearing claim made *by this review* (not by the paper) carries a warrant per `CLAUDE.md`:
`(traced)` · `(deferred to consensus)` · `(deferred, fragile)` · `(memory — unverified)`.
A Phase 6 citation-verification verdict ("Supports / Partial / Contradicts / Unrelated / Unverifiable") is itself a load-bearing reviewer claim — label whether the verdict was reached by fetching the cited source (`traced`) or by recall (`memory — unverified`, only acceptable when fetching is impossible and explicitly noted).

---

## Phase 0 — Pre-Review Discipline

**0a. Genre & venue.** Hold to its own genre's standards:
empirical primary · theoretical/conceptual · methods · systematic review / meta-analysis · narrative review · position/perspective · preprint (flag pre-PR) · workshop · replication · registered report.

**0b. Domain calibration.** Hold the paper to its field's actual bar, not a mismatched one:

| Field | What "methodology adequate" requires |
|---|---|
| **RCT / clinical** | CONSORT compliance; randomisation method; allocation concealment; blinding scheme; ITT analysis; pre-registration with deviations declared |
| **Observational epidemiology** | STROBE compliance; explicit confounding strategy (DAG / E-value); reverse-causation check; population representativeness |
| **Lab biology** | ARRIVE compliance (animal work); reagent identifiers + lot numbers; biological *and* technical replicates; positive + negative controls |
| **Psychology** | Pre-registration; replication-crisis awareness; effect sizes + CI; sample-size justification; sample beyond WEIRD where claim is universal |
| **Surveys** | Sampling frame; response rate; non-response analysis; instrument validation; question-order checks |
| **Economics** | Identification strategy explicit (RCT, IV, RD, DiD); parallel-trends test; robustness checks; standard-error clustering matches design |
| **ML / NLP** | Test-set contamination check; multiple seeds + variance; matched-compute comparison to SOTA; hyperparameter search budget disclosed |
| **Theoretical** | Formal statement of claim; assumptions explicit; proof / derivation present (or sketch labelled as sketch); novelty vs. prior result delineated |
| **Systematic review / meta-analysis** | PRISMA compliance; pre-registered protocol; search strategy reproducible; risk-of-bias tool per study; heterogeneity quantified |
| **Replication** | Pre-registered; same operationalisation; power adequate to detect original effect; outcome reported as success / failure / nuanced |
| **Qualitative** | Sampling logic stated (purposive, theoretical, snowball — and why); reflexivity declared; analytic procedure documented; triangulation where warranted |

Mismatching standards across fields (holding a survey to RCT's bar, or vice versa) is a manipulation pattern, not a critique.

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

**1e. Citation-load audit (deployment gap).** A peer review that audits only the paper's internal claims misses the most common real-world failure: *the paper itself is honest within its lane, but is cited by downstream literature, policy, or press for claims it does not bear.* Enumerate consequential downstream uses — ≥3 representative citations from later literature, policy documents, regulatory rulings, or major media — and for each, state whether *this paper* bears that load. Classify:

- **Inside-lane** — the citation matches what the paper actually argues.
- **Lane-stretched** — the citation invokes a stronger version of what the paper supports.
- **Outside-lane** — the paper is silent on, or contradicts, the claim it is cited for. Flag prominently; this becomes a **Fatal** in the citation-verification phase if the paper's authority is being used for a claim the paper does not make.

The classic pattern: a methods / detection / characterisation paper deployed downstream as if it were a causation / efficacy / safety paper. The paper is silent on the downstream burden; the silence is laundered into authority. Audit explicitly — most peer reviews skip this and that is exactly where field-level harm originates.

---

## Phase 2 — Claim Extraction & Typing

Hand load-bearing claims to `scientific-fact-classification` (Phases 1, 2, 3, 6, 7) if available. Otherwise enumerate, type (descriptive / causal / mechanistic / predictive / normative), identify unstated assumptions.

Watch for:
- **Modal smuggling** — "may", "is consistent with" in results → "shows", "demonstrates" in abstract
- **Quantifier creep** — "some patients" → "patients"
- **Population drift** — sample vs. conclusion population (WEIRD, single-site, single-sex, single-species)

---

## Phase 3 — Methodology Audit

Empirical-paper minimum:

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

**Non-empirical / non-RCT genres** — minimums:

- **Methods papers** — does the method solve a real problem (vs. solution-in-search-of-problem)? Compared to existing methods on same data + metric? Failure modes characterised? Code / artifacts released?
- **Replications** — pre-registered? Same operationalisation as original? Power adequate to detect the original effect size? Outcome reported as success / partial / failure / nuanced — not glossed?
- **Theoretical / mathematical** — claim formally stated? Assumptions exhaustively listed? Proof or derivation present (or sketch labelled as sketch)? Connection to existing theory stated and contrasted?
- **Systematic reviews / meta-analyses** — PRISMA flow diagram? Pre-registered protocol (PROSPERO or equivalent)? Search strategy reproducible? Risk-of-bias tool per study? Heterogeneity quantified, not waved past? Publication bias addressed (funnel plot, trim-and-fill, registry comparison)?
- **Qualitative** — sampling logic stated and justified? Reflexivity declared? Analytic procedure documented (coding scheme, audit trail)? Triangulation or member-checking where the claim warrants?

---

## Phase 4 — Statistical Scrutiny

Headline checks:

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

**ML / NLP additions:**
```
□ Benchmark contamination — test set seen in pretraining; data leakage between splits
□ Single-seed reporting — one favourable seed presented as method performance
□ Hyperparameter asymmetry — proposed method tuned, baselines not
□ Compute confound — proposed method has 10× compute of baselines; gain attributed to method
□ Cherry-picked checkpoint — best validation point reported as final
□ Test-set tuning — repeated evaluation on test set during development
□ Metric gaming — metric chosen post-hoc to favour method
□ Inadequate baselines — strong public baselines omitted
□ Statistical-significance absence — small gains with no significance test, no variance
```

**Bayesian additions:**
```
□ Prior choice undisclosed or unjustified
□ Prior choice drives the posterior (sensitivity analysis absent)
□ Improper prior used without justification
□ Posterior predictive checks absent
□ Bayes factors reported without prior-sensitivity check
□ Credible intervals presented as confidence intervals
```

---

## Phase 5 — Causal Claim Audit

Audit causal language in (a) *this paper's* conclusions, and (b) the consequential downstream claims this paper is cited to support (Phase 1e). The most common review failure: a paper whose own language is correctly hedged ("associated with", "implicates", "is consistent with") gets cited downstream as causal demonstration. **Both gaps must be reviewed.** A paper that is silent on causation while being cited as causal authority is a Fatal-grade deployment failure, even when the paper itself carries no fault.

If the paper or its downstream uses invoke causal language, hand to `scientific-fact-classification` Phase 4 if available; otherwise:

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

**6d. Discrepancy template** (use when a cited source does not match the paper's characterisation):

```
Cited as:             [paper's claim about the source, verbatim]
Source actually says: [direct quote from the source]
Discrepancy type:     Supports-weaker | Partial-overlap | Contradicts | Unrelated | Misquotes | Wrong-direction | Retracted
Severity:             Fatal (load-bearing citation misrepresented) | Major | Minor
Warrant:              (traced — fetched [date]) | (memory — unverified, source unavailable)
```

For citation chains (paper cites review B; review B cites primary C): follow to C at least once for load-bearing claims. If only B is accessible, note that the claim's grounding is one step removed from the primary.

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

**When the literature itself is contested** (≥3 sources disagreeing on a load-bearing point — e.g. independent replication vs. originator group, regulatory finding vs. independent reanalysis), hand the dispute to `investigative-reasoning` Phase 3i (Source Triangulation) before resolving. Headline source-counting laundered by single-origin amplification is a common path by which a contested claim looks settled in standard literature reviews.

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
- **Recommendation:** Accept / Minor / Major / Reject-resubmit / Reject
- **Verdict:** [one-line]

## What the Paper Does Well
[2–5 bullets — genuine strengths, not throat-clearing]

## Fatal Findings
[Each: quoted passage → named fault → why fatal → what would fix it (if anything)]

## Major Findings
[Each: quoted passage → named fault → severity rationale → required action]

## Minor Findings

## Optional Suggestions

## Methodology Audit
[Phase 3 — against the relevant checklist]

## Statistical Audit
[Phase 4 — quote specific numbers, don't gesture]

## Citation-Load Audit (Deployment Gap)
[Phase 1e — per representative downstream citation: cited use / what this paper actually argues / Inside-lane / Lane-stretched / Outside-lane]

## Causal Claim Audit
[Phase 5 — covers (a) in-paper causal language and (b) downstream causal use of the paper, even when the paper itself is non-causal]

## Citation Verification
[Phase 6 — per load-bearing citation: cited source / paper's claim / actual content / verdict]

## Literature Context
[Phase 8]

## Reproducibility & Transparency
[Phase 9]

## Confidence & Severity
- **Counts:** Fatal / Major / Minor / Optional / Praise
- **Confidence in this review:**

## What Would Change This
- Upward to [next recommendation]:
- Downward to [lower recommendation]:

## Self-Audit
- **Symmetry test:** Would I have reached the same verdict if the politically/socially expected answer ran the other way? Execute the flip — do not just assert. If you can't tell — say so.
- **Standards applied:** [genre and field — held to its own bar, not a mismatched one]
- **"Differences in approach" flagged separately from faults:**
- **Reviewer's own priors named:** [direction of priors on the paper's topic / authors / funder]

## Limits of This Analysis
- Domain expertise required for:
- Sources not accessible:
- Citations unverifiable:
```

---

## Quick Reference

| Pattern | Suspect | Default move |
|---|---|---|
| Causal language in abstract, correlational design in methods | Inferential overreach | Major; require language calibration |
| Paper itself hedged correctly; field cites it as causal / clinical / regulatory authority | Citation-load gap (Phase 1e) — deployment outside the paper's lane | Audit downstream uses; flag the deployment gap separately from in-paper findings; Fatal if the paper is being silently used to support claims it does not bear |
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

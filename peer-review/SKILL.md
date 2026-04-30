---
name: peer-review
description: A structured framework for rigorous, citation-verified peer review of scientific papers — auditing methodology, statistics, causal claims, citations, reproducibility, and literature context, then issuing a severity-graded report with explicit recommendation. Use whenever the task involves reviewing, critiquing, or auditing a scientific paper, manuscript, preprint, study, or research report; checking whether a paper's conclusions are supported by its methods and results; verifying that cited sources say what the paper claims; assessing reproducibility or pre-registration; or producing a referee-style report. Trigger even when the user does not say "peer review" — phrases like "is this study any good?", "audit this paper", "check this manuscript", "is the methodology sound?", "do the results support the conclusion?", "verify this paper's claims", or any request to evaluate a scientific text against the standards of its own field should activate it.
---

# Peer Review Framework

Audit a scientific paper as a competent, sceptical, fair-minded reviewer. Output: severity-graded findings (Fatal / Major / Minor / Optional / Praise), recommendation, and what would change it.

**Orchestrate, don't duplicate.** Hand claim-typing to `scientific-fact-classification`, fallacy hunting to `fallacy-bias-and-manipulation-analysis`, deception or motive analysis to `investigative-reasoning`. This skill adds: methodology audit, statistical scrutiny, citation verification, reproducibility audit, literature contextualisation.

---

## Activation

Trigger on requests to evaluate a scientific paper against its field's standards: "review this paper", "is this study sound?", "audit the methodology", "do the results support the conclusion?", "verify the citations", "is this reproducible?", "produce a referee report".

Do **not** trigger on: comprehension questions, summary-only requests, or pop-science write-ups (those go to `fallacy-bias-and-manipulation-analysis`). If given a press release, ask whether the user wants the release audited or the underlying paper reviewed.

---

## Phase 0 — Pre-Review Discipline

### 0a. Genre & venue

Hold the paper to its own genre's standards. A preprint is not a published paper; a workshop paper is not a journal article; a theoretical note is not an empirical study.

```
GENRE TAGS:
□ Empirical primary research      □ Theoretical / conceptual
□ Methods paper                   □ Systematic review / meta-analysis
□ Narrative review                □ Position / perspective
□ Preprint (flag pre-PR status)   □ Workshop / short paper
□ Replication study               □ Registered report
```

### 0b. Domain calibration

Different fields have different defensible standards. See `references/domain-checklists.md` before reviewing.

### 0c. Charity first

Restate the central claim and main methodological choice in their strongest plausible form. A flag survives only if the fault persists under charitable reading.

### 0d. Position neutrality

Do not penalise a paper because its conclusion is unfashionable, nor soften critique because you agree.

```
PROHIBITED:
✗ "Conclusion is wrong, therefore methods must be flawed"
✗ "I'd have done it differently, therefore it's wrong"
✗ "Against consensus → higher bar"   "With consensus → lower bar"
✗ "Prestigious institution → lighter scrutiny"   "Unknowns → harsher"
```

### 0e. Self-audit commitment

Commit, in writing, before reviewing: *"I will apply the same standards regardless of which way the conclusion runs. I will state explicitly whether the verdict would have been the same if it ran the other way. I will distinguish 'wrong' from 'different'. When I flag a fault I will quote the passage, name it, and state what a non-faulty version would look like."*

---

## Phase 1 — Structural Pass

### 1a. Identify
- **Type / venue / status** (from 0a)
- **Field & subfield** (drives standards applied)
- **Stated contribution** — quote verbatim, one sentence
- **Type of contribution:** new finding / new method / new theory / replication / synthesis / negative result

### 1b. Map claim → method → result → conclusion
For empirical papers: research question, hypotheses (pre-specified vs. exploratory), methods, results (primary/secondary/exploratory), conclusions. Then flag the **inferential gap** — the distance between what was measured and what is claimed. Most faults live here.

### 1c. Identify load-bearing elements
Which claims, methodological choices, or citations would, if wrong, collapse the contribution? These get the most scrutiny later.

---

## Phase 2 — Claim Extraction & Typing

Hand load-bearing claims to `scientific-fact-classification` (Phases 1, 2, 3, 6, 7) if available. Otherwise enumerate, type each (descriptive / causal / mechanistic / predictive / normative), and identify unstated assumptions.

Watch for:
- **Modal smuggling:** "may", "is consistent with" in results → "shows", "demonstrates" in abstract.
- **Quantifier creep:** "some patients" → "patients".
- **Population drift:** sample population vs. conclusion population (WEIRD, single-site, single-sex, single-species).

---

## Phase 3 — Methodology Audit

See `references/methodology-audit.md` for full domain-keyed checklist. Minimum for any empirical paper:

```
DESIGN
□ Design appropriate to the question? (RCT for causal; cross-sectional won't carry causal weight)
□ Comparator appropriate? (Placebo, active control, no-treatment)
□ Randomisation described, baseline balance verified?
□ Blinding present where it could be? Of whom? At what stages?
□ Unit of analysis = unit of randomisation?

SAMPLE / DATA
□ Inclusion / exclusion criteria specified and defensible?
□ Sample size justified by a priori power calculation?
□ Sample representative of the conclusion's population?
□ Attrition reported, magnitude acceptable, non-differential?
□ ML / corpus: test set held out from the start? Contamination check?

MEASUREMENT
□ Outcomes pre-specified? Primary distinguished from secondary?
□ Measures validated for population and construct?
□ Outcome assessor blinded?
□ Composite outcomes — do components individually carry the effect?

ANALYSIS
□ Pre-registered? Followed? Deviations explained?
□ Test appropriate for distribution, design, dependence structure?
□ Multiple comparisons addressed? How many tests were actually run?
□ Missing data handled (not silently dropped)?
□ Robustness checks support or undermine the headline?
□ Effect sizes with uncertainty, not just p-values?
□ Null / negative results reported as primary, not buried?
```

For methods papers, replications, theoretical work, and meta-analyses, see the dedicated sections in the reference file.

---

## Phase 4 — Statistical Scrutiny

See `references/statistical-red-flags.md`. Headline checks:

```
□ p-hacking: p-values clustered just below 0.05; degrees of freedom not pre-registered
□ HARKing: every hypothesis confirms; "predictions" oddly specific to the result
□ Garden of forking paths: many defensible specifications, only one shown
□ Cherry-picked subgroups: heterogeneous effect on the one subgroup where headline holds
□ Base-rate neglect: relative-risk-only ("doubles!") without absolute risk
□ Power failure: small-N + significant + large effect → likely Type-M inflation
□ Survivorship / selection: who was excluded, and why?
□ Regression to the mean masquerading as treatment effect
□ Pseudoreplication: repeated measurements treated as independent
□ Multiple-testing inflation: many tests, no correction, headline is one of them
□ Stopping rules: stopped early when "significant"?
□ Outliers: pre-specified rule, or post-hoc?
□ Statistical vs. practical significance: tiny effect, huge N, p<.001 — who cares?
□ Wrong test for the data: parametric on small skewed samples; independence assumed for clustered data
```

ML / NLP papers: see additional checklist covering benchmark contamination, single-seed reporting, hyperparameter asymmetry, and compute confounds.

---

## Phase 5 — Causal Claim Audit

If any conclusion uses causal language ("causes", "leads to", "drives", "the effect of"), audit explicitly. Hand to `scientific-fact-classification` Phase 4 if available; otherwise:

```
□ Design causally identifying? (RCT, IV, RD, DiD with parallel trends, natural experiment)
□ Observational: confounders enumerated (DAG)? Adjusted? Strongest unmeasured considered (E-value)?
□ Reverse causation ruled out (temporality)?
□ Selection into treatment plausibly exogenous?
□ Mediation: mediator measured before outcome? Full pathway tested, not just A→M and A→Y?
□ Language calibrated to design? ("Associated with" for non-causal; "causes" only when warranted)
```

Common pathology: causal language in abstract, correlational language in results. Quote both, flag the gap.

---

## Phase 6 — Citation Verification

The phase reviewers most often skip. **Misrepresented citations are common.**

### 6a. Triage — which citations need verification
- Citations supporting the central claim
- Citations supporting methodological choices
- Citations establishing the gap the paper claims to fill
- Citations to authoritative or contradicting prior work
- Citations supplying effect-size estimates used in power calculations

Aim for 5–15 in a typical paper. More for reviews and synthetic claims.

### 6b. For each: fetch → locate → compare
1. Fetch (DOI → PMC → preprint → Scholar). Paywalled: try preprint, alt review, or note as unverifiable.
2. Locate the specific claim in the cited source.
3. Compare. Verdict: **Supports / Partial / Contradicts / Unrelated / Unverifiable.**

For chains (paper A cites review B cites primary C), follow to C at least once for load-bearing claims.

### 6c. Special cases
- Self-citations: flag missing independent replication.
- "Data not shown", personal communications, "in preparation": inadmissible — flag.
- Retraction check: PubMed for biomedical, Retraction Watch Database for general.
- Citations under post-publication scrutiny (PubPeer, expressions of concern): note the caveat.

See `references/citation-verification.md` for the full protocol and the discrepancy write-up template.

---

## Phase 7 — Logical & Argumentative Consistency

Hand to `fallacy-bias-and-manipulation-analysis` for theoretical / position / review papers. For empirical papers:

```
□ Conclusions follow from results, not exceed them?
□ Abstract, body, and figures internally consistent? (Numbers match across sections?)
□ Limitations concrete (constrain conclusion) or performative (one paragraph then sweeping claim)?
□ Generalisation scope warranted by sample scope?
□ Competing explanations engaged, not waved past?
```

---

## Phase 8 — Literature Context

```
□ Recent meta-analysis or systematic review? Paper consistent or outlier?
□ Replications attempted? Result?
□ Strong contradicting prior literature engaged?
□ "Novelty" actually novel? (Quick search often catches over-claims)
□ Methods papers: stronger known method uncited?
□ ML papers: SOTA cited correctly, comparison honest (same splits, matched compute)?
```

Headline against strong prior literature → bar rises in proportion to prior strength. Headline confirming contested literature → marginal contribution smaller than claimed.

---

## Phase 9 — Reproducibility & Transparency

```
□ Data publicly available, or "available on request" (often = no)?
□ Analysis code available and versioned?
□ Methods replicable from text?
   — Lab: reagents, suppliers, catalogue numbers, protocols
   — ML: hyperparameters, seeds, hardware, compute, library versions
   — Surveys: full instrument
   — Statistics: software version, exact specifications
□ Pre-registration: present? Followed? Deviations declared?
□ Conflicts of interest disclosed (financial, institutional, ideological)?
□ Funder role in design / analysis / publication declared?
□ Author-contribution statement plausible?
```

A paper that fails reproducibility isn't necessarily wrong, but trust falls heavily on reputation rather than verifiable craft. Note explicitly.

---

## Phase 10 — Reviewer Self-Audit

```
□ Same verdict if conclusion ran the other way?
□ Held to its genre's standards, not another's?
□ "Wrong" separated from "I'd have done differently"?
□ Each flag: quoted passage + named fault + non-faulty version?
□ Strengths named, not only faults?
□ Limits of own expertise flagged for domain experts?
□ Unverifiable citations stated, not glossed?
□ Figures and tables checked, not only text?
```

If symmetry fails, revise before delivery.

---

## Phase 11 — Severity Grading & Recommendation

| Tag | Definition | Effect |
|---|---|---|
| **Fatal** | Falsifies central claim or makes it un-evaluable | Reject / fundamental redesign |
| **Major** | Core finding unsupported as presented; fixable with substantial work | Major revisions |
| **Minor** | Specific claim overstated, check missing, limitation undeclared | Minor revisions |
| **Optional** | Useful but not required | Suggested |
| **Praise** | Genuine strength worth naming | Stated for fairness |

**Recommendation:** Accept / Minor revisions / Major revisions / Reject and resubmit / Reject.

State explicitly: *what would change the recommendation upward? Downward?* That is the difference between a verdict and a review.

---

## Output Format

```markdown
# Peer Review: [paper title]

## Summary
- **Type / venue / status:**
- **Stated contribution:** [one-sentence quote or paraphrase]
- **Recommendation:** [Accept / Minor / Major / Reject-resubmit / Reject]
- **One-line verdict:**

## What the paper does well
[2–5 bullets — genuine strengths, not throat-clearing]

## Fatal findings
[Each: quoted passage → named fault → why fatal → what would fix it (if anything)]

## Major findings
[Each: quoted passage → named fault → severity rationale → required action]

## Minor findings
[More compactly]

## Optional suggestions

## Methodology audit
[Phase 3 — itemised against the relevant checklist]

## Statistical audit
[Phase 4 — quote specific numbers, do not gesture]

## Causal claim audit
[Phase 5 — only if causal language is used]

## Citation verification
[Phase 6 — for each load-bearing citation: cited source / paper's claim / actual content / verdict. Note unverifiable citations.]

## Literature context
[Phase 8]

## Reproducibility & transparency
[Phase 9]

## Limits of this review
- Domain expertise required for: [items flagged but not adjudicated]
- Sources not accessible: [paywalled, retracted, unfindable]
- Confidence in this review: [calibrated statement]

## Reviewer self-audit
- Same verdict if conclusion ran the other way? [Yes / No / explain]
- Standards applied: [genre and field]
- "Differences in approach" flagged separately from faults: [list]

## What would change the recommendation
- Upward to [next level]: [specific evidence or revisions]
- Downward to [lower level]: [specific findings that would worsen the verdict]
```

---

## Quick-Reference Matrix

| Pattern | Suspect | Default move |
|---|---|---|
| Causal language in abstract, correlational design in methods | Inferential overreach | Major; require language calibration |
| p<.05 with no effect size or CI | Statistical opacity | Require effect sizes |
| Many tests, no correction, headline is the smallest p | Multiple-testing inflation | Apply correction; often kills headline |
| "Available on request" for data | Untestable openness | Note limitation |
| Citation "shows X" — primary shows weaker version | Misrepresented citation | Quote both; Major |
| Population studied ≠ population in conclusion | Generalisation overreach | Restrict scope |
| One subgroup positive, others null, headline = subgroup | Cherry-picking | Require pre-registration check |
| Pre-registration absent in confirmatory-framed study | Forking-paths risk | Treat as exploratory; downgrade |
| Limitations = one performative paragraph then sweeping conclusion | Rhetorical limitation | Require concrete limitation |
| COI disclosure absent on industry-relevant topic | Disclosure gap | Require statement |
| Single-site sample → "humans" claim | Sample-scope overreach | Restrict scope |
| ML 0.3% improvement, no significance test, single seed | Overclaim | Require seed-level statistics |
| Cited replication failure not engaged | Selective citation | Require engagement |
| Mathematical claim with sketch, no formal statement | Underspecification | Formalise or remove |

---

## Golden Rules

**Calibrate, don't condemn.** All-praise or all-attack reviews are almost always badly calibrated. Severity tags exist to prevent this.

**The inferential gap is where most faults live.** What was measured vs. what is claimed. Quote both ends and measure the gap.

**Verify the citations that matter.** Not all — the load-bearing. Misrepresented citations are far more common, and far easier to catch, than fabricated data.

**Hold to the paper's genre.** Standards are field-relative; rigour about applying field-relative standards is universal.

**Distinguish "wrong" from "different".** Defensible-but-different choices go in *optional suggestions*, not *findings*.

**Symmetry under conclusion-flip.** Same paper, opposite conclusion → same review. Otherwise it is advocacy.

**Acknowledge what you cannot adjudicate.** Bound the review honestly. A clearly-bounded review beats a confidently-wrong one.

**Praise what is good.** Costs nothing when earned; signals reviewer calibration.

**The verdict is what would change it.** Without that, it is a verdict; with it, a review.

---

## Reference files

- `references/methodology-audit.md` — domain-keyed checklists: RCTs, observational epi, lab biology, psychology, surveys, econ, ML/NLP, theoretical, systematic reviews, replications, qualitative.
- `references/statistical-red-flags.md` — pathology catalogue with diagnostics; ML/NLP and Bayesian sections.
- `references/citation-verification.md` — fetch / locate / compare protocol; chain-tracing; retraction checks; discrepancy write-up template.
- `references/domain-checklists.md` — field-specific standards for Phase 0b calibration.

Read on demand, not pre-emptively.

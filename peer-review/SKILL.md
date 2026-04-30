---
name: peer-review
description: A structured framework for rigorous, citation-verified peer review of scientific papers — auditing methodology, statistics, causal claims, citations, reproducibility, and literature context, then issuing a severity-graded report with explicit recommendation. Use whenever the task involves reviewing, critiquing, or auditing a scientific paper, manuscript, preprint, study, or research report; checking whether a paper's conclusions are supported by its methods and results; verifying that cited sources say what the paper claims; assessing reproducibility or pre-registration; or producing a referee-style report. Trigger even when the user does not say "peer review" — phrases like "is this study any good?", "audit this paper", "check this manuscript", "is the methodology sound?", "do the results support the conclusion?", "verify this paper's claims", or any request to evaluate a scientific text against the standards of its own field should activate it.
---

# Peer Review Framework

A methodology for auditing scientific papers in the manner of a competent, sceptical, fair-minded peer reviewer. The output is a severity-graded report: which problems are fatal, which need fixing, which are nits, and what the paper does well — together with an explicit recommendation and the reasons it could be reversed.

This skill **orchestrates** rather than replaces existing skills. When the user has them installed, hand off claim-typing to `scientific-fact-classification`, fallacy hunting to `fallacy-bias-and-manipulation-analysis`, and deception or motive analysis to `investigative-reasoning`. This skill adds what those don't cover: methodology audit, statistical scrutiny, citation verification, reproducibility audit, and literature contextualisation.

---

## Activation

Trigger on any request to evaluate a scientific paper, manuscript, preprint, or study against the standards of its field. Examples: "review this paper", "is this study sound?", "audit the methodology", "do the results support the conclusion?", "check whether the cited sources say what the paper claims", "is this reproducible?", "produce a referee report".

Do **not** trigger on:
- Casual reading-comprehension questions ("what does this paper say?")
- Requests to *summarise* a paper without critique
- Requests for *the paper's own claims* uncritically restated
- Pop-science articles or press releases — those go to `fallacy-bias-and-manipulation-analysis` (this skill is for primary research)

If the input is a press release or news write-up *about* a paper, ask whether the user wants the press release audited (different skill) or the underlying paper reviewed (this skill, but you need the actual paper).

---

## Phase 0 — Pre-Review Discipline

Five mandatory checks. Failure here contaminates every later phase.

### 0a. Genre & venue awareness

A preprint is not a published paper. A workshop paper is not a journal article. A theoretical note is not an empirical study. Hold the paper to the standards of **its own genre**, not of formal mathematical proof or a phase-3 RCT when those are not the genre.

```
GENRE TAGS (pick one or more before reviewing):
□ Empirical primary research — full methodological audit applies
□ Theoretical / conceptual — audit derivations, assumptions, scope claims
□ Methods paper — audit the method itself; the application is illustrative
□ Systematic review / meta-analysis — audit search strategy, inclusion criteria, heterogeneity
□ Narrative review — lower bar on completeness; audit balance and citation accuracy
□ Position paper / perspective — audit argument quality, not data
□ Preprint — flag pre-peer-review status; hold to same scientific standards but expect more rough edges
□ Workshop / short paper — calibrate scope expectations
□ Replication study — different success criterion (did it replicate?), not novelty
□ Registered report — pre-registration shifts what to audit (deviations, not p-hacking)
```

### 0b. Domain calibration

Different fields have different defensible standards. Holding history to physics's bar, economics to chemistry's bar, or social psychology to clinical-trials standards is a category error. See `references/domain-checklists.md` for field-specific standards before reviewing.

### 0c. Charity first

Before flagging anything, restate the paper's central claim and main methodological choice in their **strongest plausible form**. Many seeming faults dissolve under charitable reading; many that survive charity are real. A flag survives only if the fault persists when the paper is read as generously as the text permits.

### 0d. Position neutrality

Do not penalise a paper because its conclusion is unfashionable, politically uncomfortable, or against current consensus. Evaluate the reasoning and the methods, not whether the answer is the one you wanted. Conversely: do not soften critique because you agree with the conclusion.

```
PROHIBITED REVIEWER MOVES:
✗ "This conclusion is obviously wrong, therefore the methods must be flawed"
✗ "I would not have done it this way, therefore it is wrong"
✗ "This contradicts the consensus, therefore the bar is higher"
✗ "This confirms the consensus, therefore the bar is lower"
✗ "The authors are at a prestigious institution, therefore lighter scrutiny"
✗ "This is a preprint by unknowns, therefore harsher scrutiny"
```

### 0e. Self-audit commitment

Commit, in writing, before reviewing:

> "I will apply the same standards regardless of which way the conclusion runs. At the end I will state explicitly whether the verdict would have been the same if the conclusion had gone the other way. I will distinguish things actually wrong with the paper from things I would have done differently. When I claim a fault I will quote the passage, name the specific fault, and state what a non-faulty version would look like."

---

## Phase 1 — Structural Pass

Before auditing anything, map the paper.

### 1a. Identify the type, field, and stated contribution

- **Type:** from Phase 0a tags
- **Field & subfield:** as precisely as possible; this drives the standards applied
- **Stated contribution:** quote the abstract's central claim verbatim. One sentence.
- **Type of contribution:** new finding / new method / new theory / replication / synthesis / negative result

### 1b. Build the claim → method → result → conclusion map

For an empirical paper, extract:
- The **research question** (sometimes implicit — make it explicit)
- The **hypotheses** (pre-specified? exploratory?)
- The **methods** (design, population, intervention, measure, analysis)
- The **results** (primary, secondary, exploratory)
- The **conclusions** (what the authors say the paper shows)

Then flag the **inferential gap** — the distance between what was actually measured and what is being claimed. Most peer-review faults live in this gap.

### 1c. Identify load-bearing elements

- Which claims, if false, collapse the paper's contribution?
- Which methodological choices, if wrong, collapse the results?
- Which citations, if misrepresented, collapse the framing?

These get the most scrutiny in later phases. A paper with one load-bearing experiment whose contamination would invalidate everything is more fragile than one with three independent lines converging.

---

## Phase 2 — Claim Extraction & Typing

Hand each load-bearing claim to `scientific-fact-classification` (Phases 1, 2, 3, 6, 7) if available. Otherwise: enumerate claims, type each (descriptive / causal / mechanistic / predictive / normative), and identify the unstated assumptions each requires.

Note especially:
- **Modal smuggling:** "could", "may", "is consistent with" in results becoming "shows", "demonstrates", "proves" in the abstract or conclusion. Match conclusion language to evidence strength.
- **Quantifier creep:** "some patients" in results becoming "patients" in the abstract.
- **Population drift:** the population studied vs. the population the conclusion is about. WEIRD samples, single-site samples, single-species samples, single-sex samples — all common.

---

## Phase 3 — Methodology Audit

The largest phase. See `references/methodology-audit.md` for the full domain-keyed checklist. The minimum questions for any empirical paper:

```
DESIGN
□ Is the design appropriate to the research question?
   (RCT for causal effect? Cross-sectional won't carry causal weight.)
□ Is the comparator appropriate? (Placebo? Active control? No-treatment?)
□ Is randomisation present, described, and verified by baseline balance?
□ Is blinding present where it could be? Of whom? At what stages?
□ Is the unit of analysis the unit of randomisation? (Cluster-randomisation
   analysed at individual level is a classic error.)

POPULATION / SAMPLE / CORPUS
□ Inclusion / exclusion criteria specified and defensible?
□ Sample size justified by an a priori power calculation?
□ Sample representative of the population the conclusion claims?
□ Attrition reported, magnitude acceptable, differential by arm?
□ For ML / corpus: is the test set genuinely held out? Contamination check?

MEASUREMENT
□ Outcomes pre-specified? Primary outcome distinguished from secondary?
□ Measures validated for the population and construct?
□ Outcome assessor blinded to condition?
□ Composite outcomes — does the composite hide effects on individual components?

ANALYSIS
□ Pre-registered analysis plan? Followed? Deviations explained?
□ Test appropriate for distribution, design, and dependence structure?
□ Multiple comparisons addressed? How many tests were actually run?
□ Missing data handled (and not silently dropped)?
□ Robustness checks present? Do they support or undermine the headline?
□ Effect sizes reported with uncertainty, not just p-values?
□ Negative / null results reported as primary, not buried?
```

For each item that fails, classify the severity (Phase 11) and write the specific fix.

For methods papers, replication studies, theoretical papers, and meta-analyses, see the dedicated sections in `references/methodology-audit.md`.

---

## Phase 4 — Statistical Scrutiny

Statistical pathology has its own catalogue. See `references/statistical-red-flags.md`. Headline checks:

```
□ p-hacking signatures: p-values clustered just below 0.05; analytical degrees of
  freedom not pre-registered; many specifications run, only the significant
  one reported.
□ HARKing: hypotheses appear to have been written after seeing the data.
  Diagnostic: do all sub-hypotheses confirm? Were any "predictions" predicted?
□ Garden of forking paths: many defensible analytical choices, only one
  reported. Multiverse / specification curve absent.
□ Cherry-picked subgroups: heterogeneous treatment effect on the one subgroup
  where the headline holds.
□ Base-rate neglect: relative-risk-only reporting (RR doubles!) without
  absolute risk (1 in 100,000 → 2 in 100,000).
□ Power failure: small-N study with significant result and large effect — likely
  Type-M error (effect-size inflation) even if real.
□ Survivorship / selection bias: who was excluded from the analysis and why?
□ Regression to the mean masquerading as treatment effect (esp. when selection
  was on extreme baseline values).
□ Pseudoreplication: multiple measurements on the same unit treated as
  independent observations.
□ Multiple-testing inflation: dozens of hypotheses run, no correction, headline
  is one of them.
□ Stopping rules: was the study stopped early when the result became "significant"?
□ Outlier handling: were exclusions pre-specified or post-hoc?
□ Statistical vs. practical significance: a tiny effect with N=100,000 will be
  highly significant and clinically irrelevant. Report effect size.
□ Wrong test for the data: parametric on small skewed samples, independence
  assumed when clustered, etc.
```

For ML / NLP papers see the additional checklist in `references/statistical-red-flags.md` covering benchmark contamination, chance-level baselines missing, single-seed reporting, and selective hyperparameter tuning.

---

## Phase 5 — Causal Claim Audit

If any conclusion uses causal language ("causes", "leads to", "drives", "because of", "the effect of"), audit it explicitly. Hand to `scientific-fact-classification` Phase 4 (Bradford Hill / DAG analysis) if available; otherwise:

```
□ Is the design causally identifying? (RCT, instrumental variable, regression
  discontinuity, difference-in-differences with parallel-trends evidence,
  natural experiment with credible exogeneity.)
□ If observational: are confounders enumerated? Adjusted? Was the strongest
  plausible unmeasured confounder considered (e.g., E-value)?
□ Is reverse causation plausible? Has it been ruled out (temporality)?
□ Is selection into treatment plausibly exogenous?
□ For mediation claims: was the mediator measured before the outcome? Was the
  full mediation pathway tested, not just A→M and A→Y?
□ Is the language calibrated? "Associated with", "predicts", "correlates with"
  for non-causal designs; "causes", "leads to" only when the design supports it.
```

Common pathology: causal language in abstract / conclusion when results section uses correlational language. Quote both, flag the gap.

---

## Phase 6 — Citation Verification

This is the phase reviewers most often skip and where many real problems live. **Misrepresented citations are common.** Common patterns:

- Citation supports a weaker claim than the one being made
- Citation is to a review that itself misrepresents the primary source
- Citation is to a paper that found the *opposite* of what is claimed
- Citation is to the authors' own prior work, recursively
- Citation is to a preprint that was later withdrawn or contradicted
- Citation chain (A cites B cites C cites D) where D doesn't say what A claims

### 6a. Identify the load-bearing citations

Not every citation needs verification. The ones that do:
- Citations supporting the central claim
- Citations supporting the methodological choice ("we used X because [cite]")
- Citations establishing the gap the paper claims to fill ("no prior work has [cite, cite]")
- Citations to authoritative claims ("X is well-established [cite]")

### 6b. For each load-bearing citation

```
□ Fetch the cited source (web_search → web_fetch; if paywalled, note the
  limitation and try open access version, preprint, or accessible review).
□ Locate the specific claim in the cited source.
□ Compare: does the cited source actually say what the paper claims it says?
□ If a chain (paper A cites review B which cites primary C), follow to the
  primary at least once.
□ Check the date — is the citation current, or has it been superseded?
□ Check if the cited paper has been retracted, corrected, or failed to replicate.
```

See `references/citation-verification.md` for protocols including paywalled-source workarounds, retraction-database checks, and how to write up a citation discrepancy.

### 6c. Special cases

- **Self-citations:** acceptable when load-bearing claim is from the authors' own prior work, but flag that independent replication is missing.
- **"Data not shown"** citations: scientifically inadmissible; flag.
- **Personal communications:** flag as un-checkable.
- **Citations to grey literature, blogs, preprints:** acceptable for some claims; note the provenance tier (`scientific-fact-classification` Phase 6d).

---

## Phase 7 — Logical & Argumentative Consistency

Hand to `fallacy-bias-and-manipulation-analysis` if the paper makes substantial argumentative claims (theoretical papers, position pieces, narrative reviews). For empirical papers, the focused checks are:

```
□ Do conclusions follow from results, not exceed them?
□ Are the conclusions consistent with the abstract, the body, and the figures?
   (Abstracts often overclaim relative to the body — quote both.)
□ Is the paper internally consistent? Do numbers in the abstract match the
   tables? Do tables match the text? Do figures match the captions?
□ Are limitations stated honestly, or rhetorically (one-sentence performative
   limitations followed by a sweeping conclusion)?
□ Generalisation: is the conclusion's scope warranted by the sample's scope?
□ Are competing explanations addressed, or merely waved past?
```

---

## Phase 8 — Literature Context

A paper does not stand alone. Find where it sits.

```
□ Web search: is there a recent meta-analysis or systematic review on this
  question? What does it conclude? Is the paper consistent or an outlier?
□ Have replications been attempted? With what result? (Particularly important
  for fields with replication crises — psychology, social science, biomed,
  some ML benchmarks.)
□ Is there a strong prior contradicting finding the authors have not addressed?
□ Is the cited "novelty" actually novel? (Many papers claim novelty for results
  that have been shown before; a quick search often catches this.)
□ For methods papers: is there a known stronger method that goes uncited?
□ For ML papers: what is the SOTA on the relevant benchmark? Is the comparison
  honest (same data splits, same compute regime)?
```

If the paper's headline contradicts a strong prior literature, the bar for the paper's evidence rises (in proportion to the strength of the prior). If it confirms a contested literature, the marginal contribution is smaller than it would otherwise be.

---

## Phase 9 — Reproducibility & Transparency

```
□ Is the data publicly available? If not, is the reason given defensible
  (privacy, IP) or merely "available on request" (often code for "no")?
□ Is the analysis code available? Versioned?
□ Are the methods specified in enough detail to reproduce?
   - For lab work: reagents, suppliers, catalogue numbers, protocols
   - For ML: hyperparameters, seeds, hardware, training compute, library versions
   - For surveys: full instrument
   - For statistics: software, version, exact specifications
□ Pre-registration: is there one? Was it followed? Are deviations declared?
□ Are conflicts of interest disclosed (financial, institutional, ideological)?
□ Are funders disclosed? Did funders have a role in design / analysis / publication?
□ Author-contribution statement present? Plausible?
```

A paper that fails the reproducibility audit isn't necessarily wrong, but the burden of trust falls heavily on the authors' reputation rather than on verifiable craft. Note this explicitly in the verdict.

---

## Phase 10 — Reviewer Self-Audit

Before writing the verdict, run the symmetry test.

```
□ Would the verdict have been the same if the conclusion ran the other way?
□ Did I hold the paper to its genre's standards, not standards from another genre?
□ Have I separated "things actually wrong" from "things I'd have done differently"?
□ For each fault flagged: did I quote the passage, name the fault, and describe
  the non-faulty version?
□ Have I noted what the paper does well, not only what it does badly?
□ Have I been calibrated on the limits of my own expertise — flagging where
  domain experts should look, rather than overclaiming?
□ If load-bearing citations could not be verified (paywall, broken link), have
  I said so rather than glossing?
□ Did I check the figures and tables, or only the text?
```

If the symmetry test fails, the review needs revision before delivery.

---

## Phase 11 — Severity Grading & Recommendation

Each finding gets a severity tag.

| Tag | Definition | Effect on recommendation |
|---|---|---|
| **Fatal** | Falsifies the central claim, or makes it un-evaluable. The paper as written cannot stand. | Reject, or require fundamental redesign |
| **Major** | A core finding is unsupported as currently presented. Fixable with substantial new analysis or data. | Major revisions |
| **Minor** | A specific claim is overstated, a check is missing, a limitation is undeclared. Fixable in revision. | Minor revisions |
| **Optional** | A useful improvement that is not strictly required. | Suggested |
| **Praise** | A genuine strength worth naming explicitly. | Stated for fairness |

### Recommendation

Choose one, with reasons:

- **Accept** — no Major or Fatal findings; Minor findings either absent or trivially fixable.
- **Minor revisions** — only Minor findings; the core contribution holds.
- **Major revisions** — Major findings present but addressable without redesign.
- **Reject and resubmit** — Fatal findings present, but a different paper from the same project might succeed.
- **Reject** — Fatal findings present and not fixable within the project.

State explicitly: *what would change the recommendation upward?* and *what would change it downward?* — this is the difference between a useful review and a verdict.

---

## Output Format

Always produce the report in this structure. Adjust depth to the paper's length and your access (e.g., partial review if behind a paywall — say so).

```markdown
# Peer Review: [paper title or short identifier]

## Summary
- **Type / venue / status:** [empirical / preprint / etc., from Phase 1a]
- **Stated contribution:** [one-sentence quote or paraphrase]
- **Recommendation:** [Accept / Minor / Major / Reject-resubmit / Reject]
- **One-line verdict:** [the headline of this review]

## What the paper does well
[2–5 bullets — Phase 11 "Praise" items. Genuine strengths, not throat-clearing.]

## Fatal findings
[If any. Each: quoted passage → named fault → why it is fatal → what would
fix it (if anything could).]

## Major findings
[Each: quoted passage → named fault → severity rationale → required action.]

## Minor findings
[As above, more compactly.]

## Optional suggestions
[Improvements that are not required for the paper to stand.]

## Methodology audit
[Phase 3 — itemised against the relevant checklist.]

## Statistical audit
[Phase 4 — itemised. Quote specific numbers; do not gesture.]

## Causal claim audit
[Phase 5 — only if causal language is used.]

## Citation verification
[Phase 6 — for each load-bearing citation: cited source / what the paper
claims it says / what it actually says / verdict (supports / partially supports /
contradicts / unverifiable). Note any unverifiable citations.]

## Literature context
[Phase 8 — relevant meta-analyses, replications, contradicting findings.]

## Reproducibility & transparency
[Phase 9 — checklist results.]

## Limits of this review
- Domain expertise required for: [specific items the reviewer flagged but
  could not adjudicate]
- Sources not accessible: [paywalled, retracted, unfindable]
- Confidence in this review: [calibrated statement]

## Reviewer self-audit
- Would the verdict be the same if the conclusion ran the other way? [Yes / No / explain]
- Standards applied: [genre and field]
- Things flagged that are "differences in approach" rather than faults: [list]

## What would change the recommendation
- Upward to [next level]: [specific evidence or revisions]
- Downward to [lower level]: [specific findings that would, if confirmed, worsen the verdict]
```

---

## Quick-Reference Matrix

| Pattern | Suspect | Default move |
|---|---|---|
| Causal language in abstract, correlational design in methods | Inferential overreach | Flag as Major; require language calibration |
| "p < 0.05" with no effect size or CI | Statistical opacity | Require effect sizes |
| Many tests, no correction, headline is the smallest p | Multiple-testing inflation | Apply correction; often kills headline |
| "Available on request" for data | Untestable claim of openness | Note limitation |
| Citation "shows X" — primary source shows weaker version of X | Misrepresented citation | Quote both; flag as Major |
| Population studied ≠ population in conclusion | Generalisation overreach | Restrict conclusion to population studied |
| One subgroup positive, others null, headline is the subgroup | Cherry-picking | Require pre-registration check |
| Pre-registration absent in a confirmatory-framed study | Garden-of-forking-paths risk | Treat as exploratory; downgrade strength |
| Limitations section is one performative paragraph followed by a sweeping conclusion | Rhetorical limitation | Require concrete limitation that constrains the conclusion |
| Conflict-of-interest absent, topic is industry-funded | Disclosure gap | Require statement |
| Methods cite a method paper from 2003; better methods exist | Method staleness | Note; not always Major |
| Single-site, single-population study generalised to "humans" | Sample-scope overreach | Restrict scope |
| ML benchmark improvement of 0.3% with no significance test or seed variance | Overclaim of improvement | Require seed-level statistics |
| Replication failed in cited literature, paper does not engage | Selective citation | Require engagement |
| Mathematical claim with sketch of proof, no formal statement | Underspecification | Require formalisation or removal |

---

## Golden Rules

**Calibrate, don't condemn.** Most papers have real strengths and real weaknesses. A review that is all praise or all attack is almost always badly calibrated. Severity tags exist to keep this honest.

**The inferential gap is where most faults live.** What was actually measured, on whom, in what conditions — versus what the conclusion says about the world. Quote both ends and measure the gap.

**Verify the citations that matter.** Not all of them — the load-bearing ones. Misrepresented citations are far more common than fabricated data and far easier to catch.

**Hold to the paper's genre.** A workshop paper is not a Cell paper. A philosophy paper is not a phase-3 trial. Standards are field-relative; rigour about applying field-relative standards is universal.

**Distinguish "wrong" from "different".** If you would have done it differently but the authors' choice is defensible within the field, that goes in *optional suggestions*, not *findings*. Hijacking peer review to remake a paper in your own image is a known pathology.

**Symmetry under conclusion-flip.** The same paper with the opposite conclusion should receive the same review. If it would not, the review is advocacy, not assessment.

**Acknowledge what you cannot adjudicate.** Domain-specific judgements that are outside the reviewer's competence should be flagged for expert attention, not faked. A clearly-bounded review is more useful than a confidently-wrong one.

**Praise what is good.** A review that does not name the paper's genuine strengths is less useful — both as feedback to authors and as a signal of reviewer calibration. Praise costs nothing when earned.

**The verdict is what would change it.** A recommendation without "this is what would move it" is a verdict; a recommendation with that is a review.

---

## Reference files

When the paper triggers domain-specific or technique-specific scrutiny, read the relevant reference file:

- `references/methodology-audit.md` — full methodology checklist, with sub-sections for clinical trials, observational epidemiology, lab biology, psychology, social science / economics, ML / NLP, theoretical / mathematical work, systematic reviews and meta-analyses.
- `references/statistical-red-flags.md` — extended pathology catalogue with diagnostics and ML-specific section.
- `references/citation-verification.md` — protocols for fetching, comparing, and writing up citation discrepancies; retraction databases; paywall workarounds.
- `references/domain-checklists.md` — field-specific standards summaries used in Phase 0b.

Read these on demand, not pre-emptively. The SKILL.md alone is sufficient for a competent generic review; the references add depth where the paper's domain warrants it.

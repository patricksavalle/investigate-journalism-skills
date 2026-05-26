---
name: scientific-fact-classification
description: "A structured framework for AI agents to weigh, recognise, and classify claims along the spectrum from objective fact to assumption, opinion, conjecture, and unfalsifiable belief — and to specify the conditions under which a claim qualifies as scientifically warranted. Use whenever the task involves separating facts from assumptions, judging the evidential status of a claim, deciding whether something is 'objective', auditing reasoning for unsupported leaps, or assigning a calibrated confidence level to a statement."
version: 1.0
aligned: 2026-05-26
---

# Scientific Fact Classification

Audit claims to determine their epistemic status. Output: calibrated confidence label, not a binary fact / not-fact verdict.

## Activation

Trigger only when explicitly requested: *"is X a fact?"*, *"weigh the evidence for Y"*, *"classify these claims"*, *"distinguish fact from assumption"*, *"is this scientific?"*, *"how well-supported is this?"*, *"is this objective?"*, *"has this been proven?"*.

## Pairs With

- `peer-review` — when claims come from a paper that needs full methodological / statistical / citation audit, not only classification.
- `fallacy-bias-and-manipulation-analysis` — for rhetorical / argumentative audit of the same text once claims are classified.
- `investigative-reasoning` — when contested claims sit inside a contested event (forensic findings, causal mechanisms in a disputed incident).
- `first-principles-thinking` — when a foundational definition / assumption inside a claim needs explicit excavation before classification.
- `osint-research` — when claim provenance is contested and needs identifier-level source tracing.
- `belief-revision` — when new evidence (replication, retraction, contrary primary source) shifts a previously assigned classification and a calibrated update is needed.

## Research Discipline (CLAUDE.md)

Claim classification without source-tracing reproduces training-data bias as analysis. The rules in `CLAUDE.md` → *Operating rules* bind:

- **Rule 1** (pre-classification hypothesis registration) — before classifying, register the prior expectation per claim's label. Otherwise post-hoc rationalisation will select the label.
- **Rule 2** (steelman from primary literature) — Phase 0d Charity; for contested claims, fetch advocates' primary literature, not critics' summaries.
- **Rule 3** (primary before secondary) — Phase 6d Provenance trace toward P1 (pre-registered + replicated primary).
- **Rule 4** (map institutional networks) — Phase 6c failure modes (funder capture, citation cartel, prestige cascade) must be checked before consensus counts as evidence.
- **Rule 5** (Tier 0 priority) — for historically-settled claims, fetch contemporary primary sources; later retrospectives sanitise.
- **Rule 6** (bias self-audit) — enforced in `## Self-Audit`.
- **Rule 7** (minimum search volumes) — ≥3 independent primary lines for an "Established fact"; fewer = lower label.
- **Rule 8** (hostility check on sources) — Phase 6b conflict-of-interest; demote sources whose funder has skin in the conclusion.
- **Rule 9** (interactive refinement) — when the user pushes for re-classification ("this is actually Established fact" / "you should call this Refuted"), label the contribution `(user-supplied — unverified)` and re-examine the evidence; do not shift the classification on user pressure absent new primary sources.

## Warrant Labels (Project Standard)

The warrant qualifier in Phase 7b — `(traced)` · `(deferred to consensus)` · `(deferred, fragile)` · `(memory — unverified)` — is the canonical project standard per `CLAUDE.md`. Other skills cite this skill for the definitions; keep them stable.

---

## Phase 0 — Pre-Analysis Discipline

**0a. Reject the binary.** No clean fact / opinion split. Claims live on a graded spectrum (Phase 7).

**0b. Specify which "objective"** is in play (often equivocated between):
- **Mind-independent** — obtains regardless of any observer
- **Intersubjectively ascertainable** — competent observers agree under same conditions
- **Procedurally objective** — produced by methods designed to filter bias (blinding, pre-registration, replication)

Most defensible scientific facts are (ii) and (iii). Watch for arguments that slide between senses.

**0c. Two limits, always in force.**
- **Theory-ladenness** — no raw observation; every datum filtered through prior commitments. Surface them.
- **Underdetermination (Duhem–Quine)** — hypotheses are tested with auxiliaries, never alone. Confidence comes from **convergence** across methods, groups, populations — not from any single experiment.

**0d. Charity, then challenge.** State each claim in its strongest form before classifying.

**0e. Calibrate to domain.**

| Domain | Standard |
|---|---|
| Mathematics / formal logic | Proof from axioms |
| Physics / chemistry | Replicated experiment, predictive precision |
| Biology / medicine | RCT + replication + mechanism |
| Epidemiology | Population statistics + Bradford Hill |
| Psychology / social science | Replication-crisis caveats apply |
| Economics | Quasi-experiments, natural experiments |
| History | Documentary convergence, source criticism |
| Forensics / law | Preponderance / beyond reasonable doubt |

Mismatching standards across domains (holding history to physics's bar, or vice versa) is a common manipulation.

**0f. Self-audit commitment.** Same standards regardless of which side of debate the conclusion lands on. State at end whether verdicts would have been the same if the conclusion ran the other way.

**0g. Consensus is a social mechanism, not a truth-detector.** Peer review, expert agreement, journal acceptance, textbook inclusion are **consensus mechanisms** — social processes for coordinating on what to treat as established. Evidence about what a community believes, not direct evidence about the world. Failure modes: funder capture, publication bias, prestige cascade, ideological alignment, slow correction (continental drift, peptic-ulcer aetiology, leaded petrol, dietary-fat orthodoxy).

Every empirical claim carries a **warrant type**:
- **Traced** — analyst followed chain from primary evidence to claim
- **Deferred** — relying on a consensus mechanism without tracing

Both are legitimate (most knowledge is necessarily deferred), but different. Test: *Could I explain this to a sceptic using evidence and reasoning, without ultimately appealing to "the experts agree"?* If no, it is deferred — however credentialed the source.

---

## Phase 1 — Claim Extraction & Typing

Quote each load-bearing claim. Number. Type:

| Type | Standard |
|---|---|
| Analytic / definitional | Conceptual analysis |
| Logico-mathematical | Formal proof |
| Singular empirical | Direct observation, record |
| Generalised empirical | Replication, sample, scope |
| Causal | Bradford Hill / DAG (Phase 4) |
| Theoretical / explanatory | Predictive success, scope, unification |
| Predictive | Track record, calibration |
| Statistical / probabilistic | Sample size, base rate, CI |
| Existence | Detection or theoretical necessity |
| Mechanism | Pathway evidence, intervention |
| Normative / value | Not empirically falsifiable; argument quality |
| Metaphysical | Argument quality; not empirically resolvable |
| Definition smuggled as empirical | Redirect to definitional analysis |

Then list **unstated assumptions** the claim relies on — definitional, measurement, sampling, background-theory, scope, time-invariance.

---

## Phase 2 — Demarcation

**2a. Falsifiability.** State the claim precisely. Describe an observation that would, if it occurred, count as evidence against. Has the claim been protected by ad hoc revision when prior predictions failed? Each revision lowers scientific status. Does the claim *prohibit* anything? A theory compatible with every outcome carries no empirical content.

Strict falsifiability is necessary but not sufficient — real testing is holistic. The diagnostic catches the opposite failure: claims so vague or so revised that nothing could ever count against them.

**2b. Pseudoscience signatures.**

| Signature | Pattern |
|---|---|
| Unfalsifiability | No observation could disconfirm |
| Vagueness as defence | Any outcome confirms |
| Ad hoc rescue | New auxiliary added on every failure |
| Moving goalposts | Confirmation criterion shifts after evidence |
| Confirmation only | Only confirming cases counted |
| No risky predictions | Only "explains" already-known data |
| Reverse onus | Demands opponents disprove rather than supplying positive evidence |
| Conspiracy immunity | Counter-evidence reframed as cover-up |
| Authority-only support | "Studies show" / "experts agree" without method or citation |
| Galileo gambit | Persecution treated as evidence of correctness |

**2c.** Unfalsifiable ≠ meaningless. Mathematical truths, definitions, value judgements, metaphysical claims can be coherent and important. The error is presenting them as if they were empirical facts.

---

## Phase 3 — Evidence Quality

**3a. Tier (rough, domain-translated).**
```
T1  Multiple independent replications + meta-analysis + mechanism
T2  Single well-designed pre-registered RCT / strong natural experiment
T3  Cohort / longitudinal observational
T4  Case-control / cross-sectional
T5  Case series / single case reports
T6  Expert opinion (informative, not evidential alone)
T7  Mechanistic / animal / in-vitro (plausibility, not human effect)
T8  Anecdote, testimonial
```

**3b. GRADE adjustments.**
*Downgrade for:* risk of bias, inconsistency, indirectness, imprecision, publication bias, no pre-registration, single study, fragility.
*Upgrade for:* large effect, dose–response, confounders that would all bias against, independent replication, mechanistic coherence, pre-registration.

After adjustment, certainty: **High / Moderate / Low / Very Low**. State which, and why.

**3c. Statistical red flags.**

| Pattern | Concern |
|---|---|
| p reported, effect size missing | Statistical ≠ practical significance |
| p just under 0.05 | Possible p-hacking |
| No CI | No precision info |
| CI includes null | "Significant" claim misleading |
| Multiple comparisons, no correction | Inflated false-positive rate |
| HARKing signs | Hypothesis suspiciously well-fitted to result |
| Subgroup analysis foregrounded | Often post-hoc fishing |
| Underpowered null claim | Absence of evidence ≠ evidence of absence |
| Relative risk without absolute | Inflates apparent importance |
| Surrogate treated as hard outcome | Proxy ≠ thing of interest |
| Cohort selected on dependent variable | Selection effect as finding |
| Base rate ignored | Conditional probabilities misread |

**3d. Replication.** Single-study findings are provisional by default. State: replicated / single-study / mixed / failed / field has known crisis (psychology, nutrition epidemiology, preclinical cancer). Discount accordingly.

---

## Phase 4 — Causal Inference

Correlation is data; causation is an inference from data + model. State the model.

**4a. Bradford Hill viewpoints** (considerations, not checkboxes). Stronger causal claims satisfy more.

| Viewpoint | Check |
|---|---|
| Strength | Larger associations harder to explain by confounding |
| Consistency | Replicated across populations, methods, times |
| Temporality | Cause precedes effect; check reverse causation |
| Plausibility / mechanism | Known pathway |
| Coherence | Fits broader knowledge |
| Experiment | Intervention changes outcome (strongest) |
| Dose–response | More exposure → more outcome |
| Specificity | Often absent for real causes; prefer negative-control/falsification exposures |
| Analogy | Similar causes elsewhere → similar effects (weakest) |

**4b. DAG / counterfactual.** Diagram causal structure; identify confounders, mediators, colliders. Confounder = common cause of A and B. Adjusting for mediator hides effect; for confounder reveals it; for collider creates spurious correlation. Rule out: reverse causation, selection, sampling bias. Use negative controls — exposures or outcomes that should *not* show effect; if they do, suspect bias.

**4c. Common errors.** Correlation→causation · post hoc · ignored confounding · ecological fallacy (group → individuals) · individual fallacy (the reverse) · single-cause · Texas sharpshooter · survivorship.

---

## Phase 5 — Bayesian Weighing

```
P(H | E) ∝ P(E | H) × P(H)
posterior ∝ likelihood × prior

What matters is the LIKELIHOOD RATIO  P(E | H) / P(E | ¬H),
not P(E | H) alone. Evidence that fits H but also fits ¬H is weak.
```

Discipline: state prior · state alternatives (at minimum: chance, bias, confounding, publication artefact) · compare likelihoods · update conservatively. Weak likelihood ratio applied to strong prior moves credence only a little.

"Extraordinary claims require extraordinary evidence" is this principle, not a rhetorical dismissal. The standard is symmetric — overturning established consensus also requires strong evidence.

---

## Phase 6 — Source & Methodological Quality

**6a. Transparency markers.** Pre-registration · open data and code · blinded outcome assessment · random assignment · adequate power · attempted replication · disclosed COIs and funding · reproducible methods · null results reported.

**6b. Conflict of interest.** Funding/affiliation does not invalidate findings, but shifts the burden of proof for findings aligning with funder's commercial or ideological interest. Check: who funded, who employs authors, funder control of design/analysis/publication, independent replication by unaligned groups.

**6c. Consensus failure modes** (Phase 0g). A consensus claim earns weight as a **prior** only when: authorities genuinely expert in relevant subdomain · claim within their scope · field tracks matters of fact · underlying evidence publicly available and reproducible · dissenters engaged on the merits.

| Failure mode | Pattern |
|---|---|
| Funder capture | Funding concentrated in parties with stake in the answer |
| Ideological capture | Conclusions track political alignment more than evidence |
| Prestige cascade | High-status early claim entrenched before scrutiny |
| Citation cartel | Same small group cites itself; dissenters not cited |
| Publication bias | Null and contrary results unpublished |
| Manufactured dissent | Industry-funded fake controversy (inverse failure) |
| Silent disagreement | Apparent agreement masks private dissent where speaking is costly |
| Replication-crisis field | Apparent consensus rests on findings that don't replicate |
| Definitional drift | "X is established" but X has been redefined since the original evidence |

**6d. Provenance trace.**
```
P1   Pre-registered + replicated + peer-reviewed primary
P2   Peer-reviewed primary, no replication yet
P3   Systematic review / meta-analysis
P4   Government / regulatory technical reports
P5   Position statements of major scientific bodies
P6   Textbooks (lag the frontier)
P7   Preprints (not peer-reviewed)
P8   Reputable science journalism citing primary sources
P9   General journalism / popular books
P10  Blogs, opinion media, advocacy sites
P11  Social media, anonymous sources, single testimonials
```

Trace claims toward P1. Many disputes evaporate at the trace step.

**Multi-source reconciliation.** When ≥3 sources make conflicting claims about a single load-bearing fact, hand the dispute to `investigative-reasoning` Phase 3i (Source Triangulation) before classifying. The triangulation procedure exposes single-origin amplification ("10 outlets" with one source-node) and independent convergence (small numerical count but distinct nodes), both of which change a claim's classification more than the per-source quality ratings do.

---

## Phase 7 — Confidence Classification

Each claim gets a label on **two axes**: evidence strength + warrant type (Phase 0g). Both travel with the claim.

**7a. Evidence-strength labels.**

| Label | Definition |
|---|---|
| **Established fact** | Multiple independent lines converge; predictive power demonstrated; replicated across labs/populations; mechanism understood; no remaining serious alternative |
| **Well-supported finding** | High-quality, replicated, mechanism plausible/known; small probability of revision |
| **Provisionally accepted** | Single high-quality study or limited replication; plausible mechanism; warrants caveat |
| **Contested** | High-quality evidence on both sides; field has not converged |
| **Weak / preliminary** | Suggestive but methodology limited, sample small, replication absent/mixed |
| **Conjecture** | Plausible, consistent with known, not yet specifically tested |
| **Load-bearing assumption** | Treated as true in service of argument but not itself supported |
| **Opinion / value claim** | Not empirically truth-apt |
| **Unfalsifiable** | No observation could disconfirm; may be coherent and important, but not a scientific fact |
| **Likely false** | Weight of high-quality evidence runs against |
| **Refuted** | Decisively disconfirmed; mechanism shown wrong or predictions decisively failed |

**7b. Warrant qualifier** (attach to every empirical label — canonical project labels per `CLAUDE.md`):
- **(traced)** — followed evidence chain to a primary source fetched this session (URL + access date stated)
- **(deferred to consensus)** — relying on a named consensus mechanism (peer-reviewed literature, regulatory body, textbook); name the body
- **(deferred, fragile)** — deferred but Phase 6c failure modes apply (funder capture, ideological capture, prestige cascade, replication crisis, etc.); state which
- **(memory — unverified)** — recalled from training data, not verified this session; never load-bearing without an explicit "this could be wrong" caveat
- **(mixed)** — part traced, part deferred; state which is which

**7c. Consensus-specific labels** (when strength comes from the consensus mechanism rather than evidence the user can follow):

| Label | When |
|---|---|
| **Consensus-warranted** | Genuine, well-functioning consensus; not traced; treat as strong prior, not known fact |
| **Consensus-warranted, fragile** | Consensus exists but 6c failure modes present |
| **Authority-warranted only** | Single authority, no evidence trace |
| **Orphaned** | Cited as established, trace dead-ends — primary source missing, doesn't say what reported, or retracted |

**7d. Reporting.** State strength + warrant + evidence (or consensus mechanism) that drove placement + what would change it. Examples:
- *Established fact (traced)* — multiple independent lines, mechanism known, chain followed
- *Well-supported finding (deferred to consensus)* — strong field consensus; not traced; strong prior
- *Provisionally accepted (deferred, consensus failure modes present)* — consensus in replication-crisis field
- *Authority-warranted only* — single regulatory body asserts; no trace

The point: stop the user confusing "what the field believes" with "what the evidence shows". When they align, both labels say so. When they diverge — and historically they often have — the user is told.

**7e. Consequential phrasing (mandatory for load-bearing claims).** For each load-bearing classification, write the **sentence the reader should use** about this claim — including its hedges. The label is internal scaffolding for the analyst. The sentence is what the reader takes downstream. Without it, calibrated labels routinely degrade into binary "fact / not-fact" reception.

Pattern:
> *"X is [most plausible candidate / well-supported / contested / refuted] for Y, based on [evidence type]. Direct demonstration is [available / unavailable / partial] because [reason]. Inference is therefore [strong-but-defeasible / contested / unsafe to act on / decisive]."*

Examples:
- ✗ "Smoking causes lung cancer." → ✓ "Smoking is a well-supported cause of lung cancer (multiple independent lines, dose-response, mechanism known); the inference is decisive."
- ✗ "SARS-CoV-2 causes COVID-19." → ✓ "SARS-CoV-2 is the most plausible causal candidate for COVID-19, based on sequence association, cell-culture cytopathic effect, animal-model challenge, and intervention data. Direct Koch-grade transmission demonstration in humans is unavailable (ethically impossible); inference is strong-but-defeasible."
- ✗ "Vitamin D supplementation reduces COVID mortality." → ✓ "Vitamin D supplementation is provisionally associated with reduced COVID mortality in observational and small-RCT data; large RCTs are mixed; inference is unsafe for clinical recommendation outside deficiency states."

**If the calibrated sentence is too cumbersome to write, the classification is hiding a more honest qualifier** and should be reconsidered. The cumbersomeness *is* the calibration.

---

## Output

```markdown
# Claim Classification: [source]

## Summary
- **Source:** [paper / article / claim set under audit]
- **Domain & standards applied:** [Phase 0e — which field's bar]
- **Verdict (bottom line):** [one-line — what the reader can rely on, what warrants scepticism]

## Per-Claim Audit

### C1: [short label]
- **Type:** [Phase 1]
- **Demarcation:** [falsifiable? pseudoscience signatures?]
- **Evidence:** tier + GRADE adjustments + replication + statistical flags
- **Causal status (if relevant):** Bradford Hill summary; alternatives ruled out
- **Bayesian context:** prior, strongest alternative, likelihood ratio direction
- **Source quality:** provenance tier, transparency, COIs
- **Warrant type:** traced / deferred / deferred with failure modes / mixed
- **Classification:** [Phase 7 strength + warrant qualifier]
- **Consequential sentence (Phase 7e):** [the calibrated sentence the reader should use — including hedges]
- **What would change this:**

[repeat per claim]

## Cross-Claim Issues
[Contradictions; dependencies; shared load-bearing assumptions]

## Source's Epistemic Profile
[Does the source distinguish facts from opinions, calibrate confidence, engage the strongest counter-evidence?]

## Confidence & Severity
- **Counts by classification label:** Established / Well-supported / Provisional / Contested / Weak / Conjecture / Assumption / Opinion / Unfalsifiable / Likely-false / Refuted
- **Warrant mix:** traced vs deferred vs deferred-fragile
- **Overall epistemic status of the source:**

## What Would Change This
[Per-claim falsification criteria collated; specific consensus-failure-mode evidence that would shift deferred classifications]

## Self-Audit
- **Symmetry test:** Would I have reached the same verdict if the politically/socially expected answer ran the other way? If no — explain. If you can't tell — say so. State explicitly per contested claim.
- **Cross-domain consistency:** Same standards applied across domains (Phase 0e), not mismatched (e.g. holding history to physics's bar or vice versa).
- **Consensus-mechanism audit:** Where warrant is `(deferred to consensus)`, were the Phase 6c failure modes actually checked, or assumed absent?

## Limits of This Analysis
[Claims left unchecked; primary sources not fetched; domain-expertise gaps; consensus mechanisms relied on but not audited]
```

---

## Quick Reference

| Pattern | Suspect | Default move |
|---|---|---|
| "Studies show…" (no citation) | Anonymous authority | Provenance unknown — investigate |
| "Scientists agree…" (no method) | Bare appeal to consensus | Treat as prior; warrant = deferred |
| "It's been proven that…" | Overstated certainty | Almost never literally true in science |
| "The science is settled" | Closing-down move | Reopen — settled by what, traced or deferred? |
| "Just a theory" | Folk-vs-scientific equivocation | Category error |
| One study found… | Single-study fallacy | Provisional at best |
| "Linked to" / "associated with" + strong conclusion | Correlation as causation | Apply Phase 4 |
| "Risk doubles" without absolute risk | Relative-risk inflation | Recompute as absolute |
| Replication in crisis fields | Replication artefact | Discount; flag consensus as fragile |
| Cited expert speaking outside field | Misapplied authority | Discount |
| Single anomalous study contradicts large literature | Likely fluke | Default to body — but check whether body is deferred |
| Pre-registered + replicated + open data | Genuine corroboration | Upgrade |
| Mechanism specified and tested | Independent line of support | Upgrade |
| Modal smuggling ("could", "may" → strong conclusion) | Hedge becoming claim | Match conclusion to evidence |
| Definitions shift mid-argument | Equivocation | Hold definition fixed |
| Field heavily funded by interested parties | Funder capture risk | Treat consensus as fragile |
| Trace dead-ends or contradicts citation | Orphaned claim | Label "orphaned"; do not propagate |

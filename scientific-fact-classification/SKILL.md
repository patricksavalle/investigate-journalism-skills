---
name: scientific-fact-classification
description: "A structured framework for AI agents to weigh, recognise, and classify claims along the spectrum from objective fact to assumption, opinion, conjecture, and unfalsifiable belief — and to specify the conditions under which a claim qualifies as scientifically warranted. Use whenever the task involves separating facts from assumptions, judging the evidential status of a claim, deciding whether something is 'objective', auditing reasoning for unsupported leaps, or assigning a calibrated confidence level to a statement."
---

# Scientific Fact Classification Framework

A methodology for auditing claims to determine their epistemic status. The output is a calibrated confidence label, not a binary fact / not-fact verdict.

---

## Activation

**Only trigger when explicitly requested.** Valid triggers: "Is X a fact?", "Weigh the evidence for Y", "Classify these claims", "Distinguish fact from assumption", "Is this scientific?", "How well-supported is this?", "Is this objective?", "Has this been proven?".

---

## Phase 0 — Pre-Analysis Discipline

### 0a. Reject the binary

There is no clean fact / opinion split. Claims live on a graded spectrum of warrant (Phase 7 is the labelled output). The job is calibration.

### 0b. Specify which "objective" is in play

Three senses, often equivocated between:
- **Mind-independent** — obtains regardless of any observer.
- **Intersubjectively ascertainable** — competent observers under the same conditions agree.
- **Procedurally objective** — produced by methods designed to filter bias (blinding, pre-registration, replication).

Most defensible scientific facts are (ii) and (iii). Watch for arguments that slide between senses.

### 0c. Two limits, always in force

- **Theory-ladenness:** No raw observation. Every datum is filtered through prior commitments about instruments, categories, and relevance. Surface them; do not pretend they are absent.
- **Underdetermination (Duhem–Quine):** Hypotheses are tested with auxiliaries, never alone. The same evidence usually fits more than one hypothesis. Confidence comes from **convergence** across methods, groups, and populations — not from any single experiment.

### 0d. Charity, then challenge

State each claim in its strongest plausible form before classifying it. Many seemingly weak claims have a defensible core; many seemingly strong claims hide a load-bearing assumption.

### 0e. Calibrate to the domain

| Domain | Typical evidential standard |
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

### 0f. Self-audit commitment

Apply the same standards regardless of which side of a debate the conclusion lands on. State at the end whether the verdicts would have been the same if the conclusion ran the other way.

### 0g. Consensus is a social mechanism, not a truth-detector

Peer review, expert agreement, journal acceptance, textbook inclusion, and "the field accepts X" are **consensus mechanisms** — social processes for coordinating on what to treat as established. They are evidence about what a community believes, not direct evidence about the world. Peer review is itself one (a few anonymous reviewers gatekeeping); treat it as light quality control, not validation. Failure modes are real and recurring: funder capture, publication bias, prestige cascades, ideological alignment, slow correction of entrenched error (continental drift, peptic-ulcer aetiology, leaded petrol, dietary-fat orthodoxy).

Every empirical claim therefore carries a **warrant type**:

- **Traced** — the analyst has followed the chain from primary evidence to the claim.
- **Deferred** — the analyst is relying on a consensus mechanism without having traced the evidence.

Both are legitimate epistemic states (most knowledge is necessarily deferred), but they are different, and the user should be told which one they are getting. Test: *Could I explain this to a sceptic using evidence and reasoning, without ultimately appealing to "the experts agree"?* If no, it is deferred — however credentialed the source.

---

## Phase 1 — Claim Extraction and Typing

Quote each load-bearing claim. Number them. For each, identify its type — different types require different standards.

| Type | Definition | Standard |
|---|---|---|
| **Analytic / definitional** | True by meaning | Conceptual analysis |
| **Logico-mathematical** | True by deduction from axioms | Formal proof |
| **Singular empirical** | About a particular event or object | Direct observation, record |
| **Generalised empirical** | A pattern across cases | Replication, sample, scope |
| **Causal** | A → B beyond correlation | Bradford Hill / DAG (Phase 4) |
| **Theoretical / explanatory** | Model explaining a class of phenomena | Predictive success, scope, unification |
| **Predictive** | Forecast about future / unobserved | Track record, calibration |
| **Statistical / probabilistic** | Frequency, risk, probability | Sample size, base rate, CI |
| **Existence** | "X exists / does not exist" | Detection or theoretical necessity |
| **Mechanism** | How a process works | Pathway evidence, intervention |
| **Normative / value** | What ought to be | Not empirically falsifiable; argument quality |
| **Metaphysical** | About fundamental nature of reality | Argument quality; not empirically resolvable |
| **Definition smuggled as empirical** | A definition disguised as a discovery | Redirect to definitional analysis |

Then list the **unstated assumptions** the claim relies on — definitional, measurement, sampling, background-theory, scope, time-invariance. A claim that needs strong unstated assumptions is weaker than its surface form.

---

## Phase 2 — Demarcation: Scientific in Form?

Before assessing evidence, check whether evidence could even bear on the claim.

### 2a. Falsifiability test

A claim is scientific in form if there is some conceivable observation that would count against it. The test is logical, not psychological.

- State the claim precisely.
- Describe an observation that would, if it occurred, count as evidence against.
- Has the claim been protected by ad hoc revision when prior predictions failed? Each revision lowers scientific status.
- Does the claim *prohibit* anything? A theory compatible with every possible outcome carries no empirical content.

Strict falsifiability is necessary but not sufficient — real testing is holistic. The diagnostic is most useful for catching the opposite failure: claims so vague or so revised that nothing could ever count against them.

### 2b. Pseudoscience signatures

| Signature | Pattern |
|---|---|
| **Unfalsifiability** | No observation could in principle disconfirm |
| **Vagueness as defence** | Predictions loose enough that any outcome confirms |
| **Ad hoc rescue** | New auxiliary added every time prediction fails |
| **Moving goalposts** | Confirmation criterion shifts after evidence comes in |
| **Confirmation only** | Only confirming cases counted |
| **No risky predictions** | Only "explains" already-known data |
| **Reverse onus** | Demands opponents disprove rather than supplying positive evidence |
| **Conspiracy immunity** | Counter-evidence reframed as cover-up |
| **Authority-only support** | "Studies show" / "experts agree" without method or citation |
| **Galileo gambit** | Persecution treated as evidence of correctness |

### 2c. Note

Unfalsifiable does not mean meaningless. Mathematical truths, definitions, value judgements, and metaphysical claims can be coherent and important — just not empirical facts. The error is presenting them *as if* they were empirical facts.

---

## Phase 3 — Evidence Quality

### 3a. Tier (rough, domain-translated)

```
T1  Multiple independent replications + meta-analysis + mechanism
T2  Single well-designed pre-registered RCT or strong natural experiment
T3  Cohort / longitudinal observational
T4  Case-control / cross-sectional
T5  Case series / single case reports
T6  Expert opinion (informative, not evidential alone)
T7  Mechanistic / animal / in-vitro (suggests plausibility, not human effect)
T8  Anecdote, testimonial
```

### 3b. GRADE-style quality adjustments

**Downgrade** for: risk of bias, inconsistency across studies, indirectness (different population/intervention/outcome than the claim), imprecision (wide CIs, small N), publication bias, no pre-registration, single study, fragility (small data change flips conclusion).

**Upgrade** for: large effect size, dose–response gradient, plausible confounders that would all bias against the observed effect, independent replication, mechanistic coherence, pre-registration.

After adjustment, certainty sits at **High / Moderate / Low / Very Low**. State which, and why.

### 3c. Statistical red flags

| Pattern | Concern |
|---|---|
| p reported, effect size missing | Statistical ≠ practical significance |
| p just under 0.05 | Possible p-hacking; check pre-registration |
| No confidence interval | No precision information |
| CI includes null effect | "Significant" claim is misleading |
| Multiple comparisons, no correction | Inflated false-positive rate |
| HARKing signs | Hypothesis suspiciously well-fitted to result |
| Subgroup analysis foregrounded | Often post-hoc fishing |
| Underpowered study claims null effect | Absence of evidence ≠ evidence of absence |
| Relative risk without absolute risk | Inflates apparent importance |
| Surrogate outcome treated as hard outcome | Proxy ≠ thing of interest |
| Cohort selected on the dependent variable | Selection effect masquerading as finding |
| Base rate ignored | Conditional probabilities misread |

### 3d. Replication

Single-study findings are provisional by default, regardless of effect size or p-value. State the status: replicated / single-study / replication mixed / replication failed / field has known crisis (psychology, nutrition epidemiology, preclinical cancer). Discount accordingly.

---

## Phase 4 — Causal Inference

Correlation is data; causation is an inference from data plus a model. The model is itself a set of assumptions — state them.

### 4a. Bradford Hill viewpoints (modernised)

Considerations, not checkboxes. Stronger causal claims satisfy more.

| Viewpoint | Check |
|---|---|
| **Strength** | Larger associations harder to explain by confounding |
| **Consistency** | Replicated across populations, methods, times |
| **Temporality** | Cause precedes effect; check for reverse causation |
| **Plausibility / mechanism** | Known pathway from cause to effect |
| **Coherence** | Fits broader knowledge |
| **Experiment** | Intervention changes outcome (strongest line) |
| **Dose–response** | More exposure → more outcome |
| **Specificity** | Often absent for real causes; modern usage prefers negative-control / falsification exposures |
| **Analogy** | Similar causes elsewhere produce similar effects (weakest) |

### 4b. Counterfactual / DAG check

- Diagram the assumed causal structure; identify confounders, mediators, colliders.
- Confounder: a common cause of A and B.
- Adjusting for a mediator hides the effect; adjusting for a confounder reveals it; adjusting for a collider creates spurious correlation.
- Rule out: reverse causation, selection effects, sampling bias.
- Use negative controls — exposures or outcomes that should *not* show the effect; if they do, suspect bias.

### 4c. Common causal errors

Correlation→causation; post hoc ergo propter hoc; confounding ignored; ecological fallacy (group statistics applied to individuals); individual fallacy (the reverse); single-cause thinking; Texas sharpshooter (cluster identified post hoc); survivorship bias.

---

## Phase 5 — Bayesian Weighing

Rational credence depends on three things, not one.

```
P(H | E) ∝ P(E | H) × P(H)
posterior ∝ likelihood × prior

What matters is the LIKELIHOOD RATIO  P(E | H) / P(E | ¬H),
not P(E | H) alone. Evidence that fits H but also fits ¬H is weak.
```

Discipline:
- State the prior. (Base rate? Mechanism known? Comparable past cases?)
- State the alternative hypotheses. At minimum: chance, bias, confounding, publication artefact.
- Compare likelihoods. How much *more expected* is the evidence under H than under the strongest alternative?
- Update conservatively. A weak likelihood ratio applied to a strong prior moves credence only a little.

"Extraordinary claims require extraordinary evidence" is this principle, not a rhetorical dismissal: a low prior demands a high likelihood ratio. The standard is symmetric — overturning established consensus also requires strong evidence.

---

## Phase 6 — Source and Methodological Quality

### 6a. Transparency markers

Strengthens: pre-registration, open data and code, blinded outcome assessment, random assignment, adequate power, attempted replication, disclosed COIs and funding, reproducible methods, null results reported.

Weakens: all of the above absent, or only positive results published.

### 6b. Conflict of interest

Funding and affiliations do not invalidate findings, but they shift the burden of proof for findings that align with the funder's commercial or ideological interest. Look for: who funded the study, who employs the authors, whether the funder controlled design / analysis / publication, whether the same finding has been independently replicated by unaligned groups.

### 6c. Consensus mechanisms — handle with care

Per Phase 0g, consensus is a social mechanism, not validation. A consensus claim carries weight as a **prior** only when the cited authorities are genuinely expert in the relevant subdomain, the claim is within their scope, the field is one where expertise tracks matters of fact, the underlying evidence is publicly available and reproducible from the data by an independent reader, and dissenters have been engaged on the merits. Failure of any condition downgrades the prior.

Failure modes to scan for explicitly:

| Failure mode | Pattern |
|---|---|
| **Funder capture** | Funding concentrated in parties with a stake in the answer |
| **Ideological capture** | Conclusions track political alignment more than evidence |
| **Prestige cascade** | High-status early claim entrenched before scrutiny |
| **Citation cartel** | Same small group cites itself; dissenters not cited |
| **Publication bias** | Null and contrary results not published |
| **Manufactured dissent** | Industry-funded fake controversy (the inverse failure) |
| **Silent disagreement** | Apparent agreement masks private dissent in fields where speaking is costly |
| **Replication-crisis field** | Apparent consensus rests on findings that don't replicate |
| **Definitional drift** | "X is established" but X has been redefined since the original evidence |

### 6d. Provenance trace

```
P1   Pre-registered + replicated + peer-reviewed primary research
P2   Peer-reviewed primary research, no replication yet
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

Trace claims back toward P1. Many disputes evaporate at the trace step.

---

## Phase 7 — Confidence Classification (the Output Spectrum)

Each claim gets a label along **two axes**: evidence strength, and warrant type (traced vs. deferred — Phase 0g). Both travel with the claim.

### 7a. Evidence-strength labels

| Label | Definition |
|---|---|
| **Established fact** | Multiple independent lines converge; predictive power demonstrated; replicated across labs and populations; mechanism understood; no remaining serious empirical alternative |
| **Well-supported finding** | High-quality evidence, replicated, mechanism plausible or known; small probability of revision |
| **Provisionally accepted** | Single high-quality study or limited replication; plausible mechanism; warrants explicit caveat |
| **Contested** | High-quality evidence on both sides; field has not converged |
| **Weak / preliminary** | Suggestive but methodology limited, sample small, replication absent or mixed |
| **Conjecture** | Plausible hypothesis, consistent with what is known, not yet specifically tested |
| **Load-bearing assumption** | Treated as true in service of an argument but not itself supported |
| **Opinion / value claim** | Not empirically truth-apt in the scientific sense |
| **Unfalsifiable** | No observation could in principle disconfirm; may be coherent and important, but not a scientific fact |
| **Likely false** | Weight of high-quality evidence runs against the claim |
| **Refuted** | Decisively disconfirmed; mechanism shown wrong or predictions decisively failed |

### 7b. Warrant qualifier (attach to every empirical label)

- **(traced)** — analyst has followed the chain from primary evidence to claim.
- **(deferred to consensus)** — relying on peer review / expert agreement / textbook status without tracing the evidence.
- **(deferred, consensus failure modes present)** — as above, but Phase 6c flags apply; the deferred warrant is itself shaky.
- **(mixed)** — part traced, part deferred; state which.

### 7c. Special labels for primarily consensus-warranted claims

When the apparent strength comes from the consensus mechanism rather than from evidence the user can follow:

| Label | When to use |
|---|---|
| **Consensus-warranted** | Genuine, well-functioning consensus exists; user has not traced; treat as strong prior, not known fact |
| **Consensus-warranted, fragile** | Consensus exists but Phase 6c failure modes present |
| **Authority-warranted only** | Single authority or institutional pronouncement, no evidence trace |
| **Orphaned** | Cited as established but the trace dead-ends — primary source missing, doesn't say what it's reported to say, or retracted |

### 7d. Reporting

State the **strength label**, the **warrant qualifier**, the evidence (or consensus mechanism) that drove placement, and what would change it. Examples:

- *Established fact (traced)* — multiple independent lines, mechanism known, chain followed.
- *Well-supported finding (deferred to consensus)* — strong field consensus; user has not traced; treat as strong prior.
- *Provisionally accepted (deferred, consensus failure modes present)* — consensus in a field with known replication crisis; downgrade.
- *Authority-warranted only* — single regulatory body asserts; no evidence trace.

The point is to stop the user confusing "what the field believes" with "what the evidence shows". When they align, both labels say so. When they diverge — and historically they often have — the user is told.

---

## Output Format

```markdown
## Claim Classification: [source]

### Domain & standards applied
[from Phase 0e]

### Per-claim audit

#### C1: [short label]
- **Type:** [Phase 1]
- **Demarcation:** [falsifiable? pseudoscience signatures?]
- **Evidence:** tier + GRADE adjustments + replication + statistical flags
- **Causal status (if relevant):** Bradford Hill summary; alternatives ruled out
- **Bayesian context:** prior, strongest alternative, likelihood ratio direction
- **Source quality:** provenance tier, transparency, COIs
- **Warrant type:** traced / deferred to consensus / deferred with failure modes / mixed (Phase 0g, 6c)
- **Classification:** [Phase 7 strength label + warrant qualifier]
- **What would change this:** [specific evidence]

[repeat per claim]

### Cross-claim issues
Contradictions; dependencies; shared load-bearing assumptions.

### Severity summary
Counts by classification label.

### Source's epistemic profile
Does the source distinguish facts from opinions, calibrate confidence, engage the strongest counter-evidence?

### Analyst self-audit
Would the verdicts be the same if the conclusions ran the other way?

### Bottom line
What the reader can rely on, what warrants scepticism, what needs further investigation.
```

---

## Quick-Reference Matrix

| Pattern | Suspect | Default move |
|---|---|---|
| "Studies show..." (no citation) | Anonymous authority | Provenance unknown — investigate |
| "Scientists agree..." (no method) | Bare appeal to consensus | Treat as prior, not conclusion; warrant = deferred |
| "It's been proven that..." | Overstated certainty | Almost never literally true in science |
| "The science is settled" | Closing-down move | Reopen: settled by what evidence, traced or deferred? |
| "Just a theory" | Folk-vs-scientific theory equivocation | Category error |
| One study found... | Single-study fallacy | Provisional at best |
| "Linked to" / "associated with" + strong conclusion | Correlation as causation | Apply Phase 4 |
| "Risk doubles" without absolute risk | Relative-risk inflation | Recompute as absolute |
| Replication in fields with known crisis | Replication artefact | Discount; flag consensus as fragile |
| Cited expert speaking outside field | Misapplied authority | Discount |
| Single anomalous study contradicts large literature | Likely fluke | Default to body of evidence — but check whether body is itself deferred |
| Pre-registered + replicated + open data | Genuine corroboration | Upgrade |
| Mechanism specified and tested | Independent line of support | Upgrade |
| Modal smuggling ("could", "may" → strong conclusion) | Hedge becoming claim | Match conclusion to evidence |
| Definitions shift mid-argument | Equivocation | Hold definition fixed |
| Field heavily funded by interested parties | Funder capture risk | Treat consensus as fragile |
| Trace to primary source dead-ends or contradicts citation | Orphaned claim | Label "orphaned"; do not propagate |

---

## Golden Rules

**Calibrate, don't verdict.** The framework places claims on a spectrum of warrant; "provisionally accepted, with caveats" is more honest and more useful than "fact" without them.

**"Objective" is procedural, not metaphysical.** The strongest defensible sense is intersubjectively confirmable by competent observers using transparent methods, surviving repeated attempts to disconfirm, fitting a wider network of converging evidence. That is enough.

**Confidence comes from convergence.** Single studies rarely settle anything. Multiple methods, groups, and populations pointing the same way is what raises a claim from provisional to established.

**Falsifiability is a structural test, not a verdict.** A claim that prohibits no observation contributes no empirical information. Vagueness, ad hoc rescue, and shifting predictions are the warning signs.

**Correlation is the data; causation is an inference.** That inference always rests on a causal model. State the model.

**Update Bayesianly.** A surprising finding against well-established theory deserves close inspection of the finding, not immediate revision of the theory. The standard is symmetric.

**Consensus is a social mechanism, not a truth-detector.** Peer review, expert agreement, and journal status are evidence about what a community believes, not about the world. A claim the user has traced and a claim the user is taking on the field's word for are different epistemic objects, even if both are "true". Label deferred claims as deferred — most apparent "facts" in popular discourse are.

**The audit applies to the analyst.** If the verdicts would have been different had the conclusions run the other way, the audit was advocacy.

**"Fact" means: it would be more eccentric to deny it than to accept it** — when independent observers using transparent methods repeatedly arrive at the same finding, no remaining alternative has comparable support, *and the chain from evidence to claim has been followed*. A claim widely treated as fact but warranted only by consensus is a deferred fact, not an established one. The honest label says so.

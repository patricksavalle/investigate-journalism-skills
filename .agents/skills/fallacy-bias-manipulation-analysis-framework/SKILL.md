---
name: fallacy-bias-and-manipulation-analysis
description: A structured framework for AI agents to analyse text for logical fallacies, cognitive biases, rhetorical manipulation, and other forms of untruthful reasoning.
version: 1.0
aligned: 2026-05-26
---

# Fallacy, Bias & Manipulation Analysis

Audit natural-language text — articles, speeches, op-eds, ads, scientific claims, political rhetoric — for flawed reasoning, exploited biases, rhetorical manipulation, and statistical deception.

## Activation

Trigger only when explicitly requested: *"analyse for fallacies"*, *"find the cognitive biases"*, *"audit this reasoning"*, *"is this propaganda?"*, *"what rhetorical tricks"*, *"stress-test this argument"*, *"find the manipulation"*.

## Pairs With

This skill is one tool in the truth-seeking toolbox. Compose it with:

- `scientific-fact-classification` — when a flagged passage cites scientific findings, classify the underlying claim's evidence strength rather than only naming the rhetorical move.
- `investigative-reasoning` — when the rhetoric belongs to a contested event, hand the residual claim-set to dual-hypothesis construction.
- `first-principles-thinking` — when a load-bearing premise needs to be decomposed to its bedrock before a fallacy flag is defensible.
- `peer-review` — when the rhetoric is wrapped around a scientific paper, route the paper to full review.
- `belief-revision` — when new evidence emerges about a previously analysed text and a calibrated update is needed.

## When This Skill Is Silent Or Ambiguous

First check whether another project skill owns the missing layer: scientific claim status -> `scientific-fact-classification`; paper methods/statistics/citations/reproducibility -> `peer-review`; article framing/reporting accuracy -> `journalistic-article-review`; source identity/funding/public records -> `osint-research`; contested events or competing narratives -> `investigative-reasoning`; definitions, hidden assumptions, or argument bedrock -> `first-principles-thinking`; fallacies/rhetoric/statistical framing tricks -> `fallacy-bias-manipulation-analysis`; new evidence changing a prior verdict -> `belief-revision`.

If no skill clearly owns the gap, reason from first principles and explicit warrants. Built-in knowledge may suggest hypotheses, search terms, possible failure modes, or questions to verify, but any empirical premise remains `(memory — unverified)` until traced. Reasoning may connect warranted premises; it may not manufacture premises.

## Research Discipline (CLAUDE.md/AGENTS.md)

This skill audits text the user supplies; it does not normally fetch sources. But the rules in `CLAUDE.md` / `AGENTS.md` → *Operating rules* still bind whenever an analytical finding invokes empirical evidence:

- **Rule 1** (pre-search hypothesis registration) — applies only when the analyst undertakes outside investigation; otherwise inactive here.
- **Rule 2** (steelman from primary literature) — when the text characterises another's position to attack it, fetch that position's own primary statement before judging the move "straw man" or "fair".
- **Rule 3** (primary before secondary) — when the text cites a study or source, fetch the primary before accepting or refuting the text's characterisation of it.
- **Rule 4** (map institutional networks) — when the text claims independent corroboration ("studies show", "multiple outlets report"), check whether the sources share funder / owner / mandate before treating them as independent.
- **Rule 5** (Tier 0 priority for time-sensitive claims) — applies only when the analyst undertakes outside investigation into historical or time-sensitive claims; otherwise inactive here.
- **Rule 6** (bias self-audit) — enforced in `## Self-Audit` of the output template.
- **Rule 7** (minimum search volumes) — applies only when the analyst undertakes outside investigation; otherwise inactive here.
- **Rule 8** (hostility check on sources) — when the text recruits an authority, name that authority's funding / alignment / mandate alongside the citation.
- **Rule 9** (interactive refinement) — applies the moment the user pushes back on a flag, offers a counter-argument, or supplies "actually, this is what the author meant" framing. User contributions are labelled `(user-supplied — unverified)` and treated as hypotheses to test against the text, never as authority that overrides a flag.
- **Rule 10** (objective report voice) — write the audit as a standalone verdict on the claim or text, with no requester references in the report prose.

## Warrant Labels (Project Standard)

Every load-bearing factual claim this skill *invokes* (e.g. "this technique is documented", "this statistic is established") carries a warrant per `CLAUDE.md` / `AGENTS.md`:

| Label | Meaning |
|---|---|
| `(traced)` | Followed evidence chain to a primary source fetched in this session. State URL + access date. |
| `(deferred to consensus)` | Relying on a named social/institutional consensus mechanism, such as a literature body, regulatory body, or textbook. Consensus is not scientific warrant; for scientific claims, treat it only as a political/social prior unless traced to reproduced or replicated evidence. |
| `(deferred, fragile)` | Deferred to consensus, but known failure modes apply: funder capture, ideological capture, prestige cascade, replication crisis, or similar. State which. |
| `(memory — unverified)` | Recalled from training data, not verified this session. Never load-bearing without an explicit caveat that it could be wrong. |
| `(user-supplied — unverified)` | Provided during interactive refinement and not verified in-session. Treat as a hypothesis to test, never as authority. |

The fallacy labels themselves are analytical (definitional), not empirical — they do not require a warrant, but any empirical claim recruited to defend them does.

If sources are fetched, record for each cited source: URL, access date, publication date where relevant, warrant label, and funding / ownership / mandate / national alignment where relevant.

---

## Phase 0 — Pre-Analysis Discipline

**0a. Charity (steelman first).** Reconstruct the argument in its strongest form using the author's own best phrasing. A fallacy flag survives only if the error persists under charitable reading.

**0b. Genre.** Hold the text to its own genre's standards, not formal logic's:
formal argument · journalistic/opinion · political/campaign · marketing · scientific popularisation · social-media · educational · interpersonal-manipulative.

**0c. Position-neutrality.** A valid argument for a false conclusion is still valid; an invalid argument for a true conclusion is still invalid. Never:
- "Conclusion is wrong → must contain fallacy"
- "This author is known for bad arguments → this one is too"
- "Aligns with my priors → reasoning sound"
- "Taboo topic → any defence is fallacious"

**0d. Burden.** For each flag: (1) quote, (2) name the fault, (3) explain *under charitable reading*, (4) state the non-fallacious version. Labelling without demonstration is itself a fallacy.

---

## Phase 1 — Argument Map

```
Thesis:              [one-sentence central claim]
Load-bearing claims: C1 [evidence/reasoning] · C2 [...] · ...
Implicit premises:   [unstated assumptions required]
Rhetorical frame:    [emotional/moral framing invited]
Intended audience:   [who and of what]
```

Only load-bearing claims warrant deep scrutiny.

---

## Phase 2 — Formal Fallacies

Detected from structure alone. If the argument has this form, it is invalid regardless of conclusion.

| Fallacy | Schema / Quick Test |
|---|---|
| Affirming the Consequent | If P then Q; Q; ∴ P. Q could be true for other reasons. |
| Denying the Antecedent | If P then Q; ¬P; ∴ ¬Q. Q could still hold. |
| Undistributed Middle | Shared term not universal in any premise. |
| Illicit Major/Minor | Term distributed in conclusion but not premise. |
| Affirming a Disjunct | Only valid for *exclusive* or. |
| Denying a Conjunct | ¬(A∧B); ¬A; ∴ B — does not follow. |
| Four Terms | Syllogism with 4 terms (often via equivocation). |
| Existential Fallacy | Universal premises → particular existence claim. |
| Base Rate Neglect | Conditional probability without prior. |
| Conjunction Fallacy | P(A∧B) > P(A). |
| Masked-Man | Substituting co-referring terms in opaque contexts. |
| Non Sequitur | Catch-all when no specific formal fault applies. |

Discipline: write the argument in standard form (premises above line, conclusion below). Inability to do so is itself a finding.

---

## Phase 3 — Informal Fallacies

### 3a. Relevance

| Fallacy | Signal |
|---|---|
| Ad Hominem (abusive / circumstantial / tu quoque) | Attack person, not argument |
| Guilt by Association | "This is what [unpopular group] also believes" |
| Poisoning the Well | Pre-emptively discredit arguer |
| Genetic Fallacy | Judge claim by origin, not content |
| Appeal to Authority (inappropriate) | Outside-domain or unnamed "experts say" |
| Ad Populum | "Many believe → true" |
| Appeal to Tradition / Novelty / Nature | "Always done", "new = better", "natural = good" |
| Appeal to Emotion (fear/pity/flattery/ridicule/spite) | Feeling substituted for reason |
| Appeal to Consequences | "If P were true, bad things follow → ¬P" |
| Appeal to Ignorance | "Not proven false → true" (or reverse) |
| Red Herring / Whataboutism | Irrelevant distraction; "but what about…" |
| Straw Man / Steelman Failure | Attack a weaker version |
| Two Wrongs Make a Right | "They did it first" |

### 3b. Presumption

| Fallacy | Signal |
|---|---|
| Begging the Question | Conclusion smuggled into premises |
| Circular Reasoning | A → B → C → A |
| Complex / Loaded Question | Question presupposes disputed claim |
| False Dilemma / Trilemma | Limited options when more exist |
| Suppressed Evidence / Cherry-Picking | Omit disconfirming data |
| No True Scotsman | Redefine category to exclude counterexample |
| Moving the Goalposts | Raise the bar each time it is met |
| Special Pleading | Universal rule, exception for own case |
| Sunk Cost | Continue because of past investment |
| Gambler's / Hot-Hand | Treat independent events as dependent |

### 3c. Ambiguity

Equivocation · Amphiboly · Accent · Composition · Division · Reification · Scope Ambiguity. The key term's meaning shifts between premise and conclusion.

### 3d. Causation

Post hoc · Cum hoc · Reverse causation · Common cause ignored · Single-cause oversimplification · Regression fallacy · Texas sharpshooter · Slippery slope (without mechanism).

### 3e. Defective Induction

Hasty generalisation · Faulty/biased sample · Anecdotal evidence · Accident · Converse accident · Argument from incredulity · Argument from ignorance.

### 3f. Meta / Discourse

Fallacy Fallacy (bad argument for P ≠ ¬P) · Ad nauseam (repetition as proof) · Proof by verbosity · Gish Gallop · Kettle Logic · False Balance · Continuum · Nirvana · Moralistic · Naturalistic (is-ought) · Ad Baculum · Ipse Dixit.

---

## Phase 4 — Cognitive Biases

Flag biases the text **exploits or exhibits**, not every bias in the literature.

**4a. Belief-formation.** Confirmation · disconfirmation · motivated reasoning · belief perseverance · backfire · Semmelweis reflex · illusory truth · bandwagon · authority · halo/horn · Dunning-Kruger · anchoring · availability · representativeness.

**4b. Self-perception.** Self-serving · actor-observer · fundamental attribution · naive realism · false consensus · third-person · illusion of control · overconfidence · bias blind spot.

**4c. Memory (when text cites testimony).** Hindsight · rosy retrospection · misinformation effect · source confusion · consistency · suggestibility.

**4d. Social/group.** In-group favouritism · out-group homogeneity · group attribution · groupthink · system justification · just-world · hostile attribution · stereotype reliance.

**4e. Decision/framing.** Loss aversion · endowment · status quo · framing · default · optimism/pessimism · planning · projection · hyperbolic discounting.

**4f. Pattern-recognition.** Apophenia/pareidolia · clustering illusion · illusory correlation · selection/survivorship · publication/reporting · observer-expectancy.

---

## Phase 5 — Rhetoric & Propaganda

**5a. IPA classical (1937).** Name-calling · glittering generalities · transfer · testimonial · plain folks · card stacking · bandwagon.

**5b. Contemporary.**

| Technique | Description |
|---|---|
| Firehose of falsehood | High-volume, multi-channel, inconsistent, rapid, repetitive — exhausts verification |
| Big Lie | Falsehood so large its scale becomes its credential |
| Gaslighting | Deny reader's perception of reality |
| DARVO | Deny, Attack, Reverse Victim & Offender |
| Whataboutism | Deflect via others' alleged faults |
| Sealioning | Endless polite questioning to exhaust |
| JAQing off | Smuggle accusation in interrogative form |
| Concern trolling | Faux-sympathetic undermining |
| FUD | Raise doubt to stall decisions |
| Motte-and-Bailey | Defend narrow (motte), advance broad (bailey) |
| Kafkatrap | Denial = proof of accusation |
| Galaxy-brained | Clever-looking chain to absurd conclusion |
| Dog Whistle | Innocuous surface, in-group signal |
| Framing / Agenda Setting | Pre-load conclusions via category/metaphor; control which questions are asked |
| Overton Window shift | Introduce extreme to normalise prior-extreme |
| Manufactured controversy | Settled question framed as open |
| False-humility ("reluctant conclusion") | "I didn't want to believe it, but…" |

**5c. Schopenhauer (recurring in live text).** Extension (=straw man) · homonymy (=equivocation) · conceal your game · postulate what must be proved (=question-begging) · ad hominem when losing on substance · provoke anger · push opponent to overstate · claim victory regardless · last word.

---

## Phase 6 — Statistical Manipulation

**6a. Data.** Cherry-picking · p-hacking · Texas sharpshooter · suppressed correlative · survivorship bias · selection bias · publication bias.

**6b. Framing.** Misleading averages · missing baseline/denominator · absolute-vs-relative-risk confusion · relative risk reduction presented as absolute risk reduction · odds/hazard/rate ratio presented as risk · percent-of-percent · truncated axes · arbitrary time windows · rate-vs-count substitution · false precision · composite indices with hidden weights · Goodhart's Law exploitation.

**6c. Inference.** Base-rate neglect · Simpson's Paradox (exploited) · ecological fallacy · atomistic fallacy · McNamara fallacy · ignored confounding · ignored reverse causation · causal direction asserted without temporal/design support · statistical-vs-practical significance · sampling-vs-systematic-error confusion.

**6d. Source manipulation.** Unnamed authority · single source amplified across many outlets (echo) · missing/buried COI · retracted studies cited as current · ellipsis quotes changing meaning.

---

## Phase 7 — Linguistic Manipulation

**7a. Weasel words.** Numerically vague ("many", "up to", "leading") · agentless passive ("mistakes were made") · anonymous authority ("experts say") · hedging adverbs ("arguably", "reportedly") · first-person plural ("we all know"). Flag only when precision is available but avoided, or weasel is load-bearing.

**7b. Loaded language.** Positive/negative loaded terms · euphemism ("collateral damage") · dysphemism ("death tax") · emotive verbs ("slammed", "admitted") · scare quotes.

**7c. Structural.** Nominalisation (verb→noun hides agency) · agentless passive · presupposition smuggling ("when did you stop…") · leading/rhetorical questions · definitional rigging · jargon-as-smokescreen · false precision · appeal to "common sense".

**7d. Framing test.** Rewrite the same factual content with opposite framing. If the conclusion flips, the original frame is doing hidden argumentative work.

---

## Phase 8 — Discourse-Structural

Gish Gallop · Motte-and-Bailey · Moving Goalposts · Sealioning · Bait-and-Switch (open reasonable, swap to stronger in conclusion) · Burying the Lede · Asymmetric Scrutiny · Isolated Demand for Rigour · Manufactured Urgency · False Balance · Preemptive Framing · Context Collapse · Narrative Lock-in.

---

## Phase 9 — Severity

For each flag tag:
- **Load-bearing** (argument fails without it) / **Supporting** / **Rhetorical flourish**. Only load-bearing faults sink the argument.
- **Severe** / **Moderate** / **Mild**.
- **Intentionality:** *consistent with* / *inconsistent with* deliberate manipulation — never asserted. Signals: faults all pointing one direction; precision available but avoided; professional obligation to know better.
- **Reader-impact:** higher stakes of belief → lower tolerance for faults.

---

## Phase 10 — Steelman & Repair

For each load-bearing flaw:
```
Original move:    [quote]
Fault:            [name + category]
Why fallacious:   [one-sentence explanation]
Steelman:         [strongest non-fallacious form of the same point]
Residual status:  [argument now succeeds / partly succeeds / collapses]
```

An argument that collapses under repair was being carried by the faults.

---

## Phase 11 — Verification Checklist

- [ ] Every flag survives charitable reading
- [ ] Standards match the text's genre, not mismatched
- [ ] Every flag quotes a specific passage
- [ ] Named taxonomic category, not "bad reasoning"
- [ ] Explained why, not just labelled
- [ ] Load-bearingness assessed
- [ ] Steelman offered for each load-bearing flaw
- [ ] **Self-audit:** would I flag this as aggressively if conclusion ran the other way?
- [ ] Fallacy-fallacy avoided (argument unsound ≠ conclusion false)
- [ ] No double-counting

---

## Output

```markdown
# Fallacy & Bias Audit: [title / opening]

## Summary
- **Genre & register:** [formal / journalistic / political / marketing / scientific-pop / social / interpersonal]
- **Thesis:** [one-sentence central claim]
- **Verdict:** [one-line — argument stands / partly stands / collapses under repair]

## Argument Map
- **Load-bearing sub-claims:**

  | # | Claim | Evidence offered |
  |---|---|---|

- **Implicit premises:**
- **Rhetorical frame:**
- **Intended audience:**

## Findings

### Formal Fallacies
| Passage | Fault | Explanation | Load-bearing? |
|---|---|---|---|

### Informal Fallacies
| Passage | Family | Specific | Explanation | Load-bearing? |
|---|---|---|---|---|

### Cognitive Biases
| Passage | Bias | Mechanism | Load-bearing? |
|---|---|---|---|

### Rhetorical Techniques
| Passage | Technique | Effect |
|---|---|---|

### Statistical Manipulation
| Passage | Pattern | Correct interpretation |
|---|---|---|

### Linguistic Manipulation
| Passage | Pattern | Neutralised paraphrase |
|---|---|---|

### Discourse-Structural
| Passage/section | Pattern | Effect |
|---|---|---|

## Steelman Repair
[For each load-bearing flaw — non-fallacious version + whether argument survives]

## Residual Assessment
[Which sub-claims stand, which fall, which remain undecidable]

## Confidence & Severity
- **Load-bearing flaws:** [count + list]
- **Supporting / rhetorical flaws:** [counts]
- **Overall severity:** Severe / Moderate / Mild
- **Consistency with deliberate manipulation:** [+ reasoning — never asserted]

## What Would Change This
[Specific evidence, repair, or argument move that would flip the residual assessment]

## Sources & Warrants
[Include only when empirical evidence or outside sources were invoked.]

| Claim / finding supported | Source | URL | Access date | Publication date | Warrant | Funding / ownership / mandate / alignment |
|---|---|---|---|---|---|---|

## Self-Audit
- **Symmetry test:** Would I have reached the same verdict if the politically/socially expected answer ran the other way? If no — explain. If you can't tell — say so.
- **Fallacy-fallacy guard:** the argument being unsound does not make the conclusion false.
- **Priors named:** direction of analyst's own priors on the topic, stated.

## Limits of This Analysis
[Scope of text examined; passages or claims left unchecked; expertise / context limits]
```

---

## Quick Reference

| When you see… | Suspect… |
|---|---|
| "Everyone knows", "obvious that" | Ad populum, bare assertion |
| Unnamed "studies show", "experts say" | Anonymous authority, weasel |
| "If we allow X, next Y, then Z" (no mechanism) | Slippery slope |
| "You would say that, you're a [label]" | Ad hominem circumstantial |
| "My opponent thinks [absurd version]" | Straw man |
| "The real issue is…" mid-argument | Red herring |
| "But what about [other side]?" | Whataboutism |
| "Just asking questions" | JAQing off |
| Vivid anecdote → sweeping conclusion | Hasty generalisation / availability |
| "Since X, Y" (no mechanism) | Post hoc |
| "Natural" / "unnatural" load-bearing | Appeal to nature |
| Term seems to shift meaning | Equivocation |
| Only favourable examples | Cherry-picking |
| Percentage without denominator | Missing baseline |
| Relative reduction without absolute risk | Magnitude inflation |
| Odds/hazard/rate ratio called "risk" | Metric substitution |
| Cause asserted, reverse direction not checked | Directionality failure |
| Truncated y-axis | Graphical deception |
| "No true X would…" | No true Scotsman |
| Criterion changes after met | Moving goalposts |
| Claim → retreat → claim | Motte-and-Bailey |
| High-volume rapid claims | Gish gallop / firehose |
| "I didn't want to believe it, but…" | False-humility manipulation |
| Agentless passive carrying moral weight | Agency-hiding |

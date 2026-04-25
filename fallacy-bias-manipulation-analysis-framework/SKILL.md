---
name: fallacy-bias-and-manipulation-analysis
description: A structured framework for AI agents to analyse text for logical fallacies, cognitive biases, rhetorical manipulation, and other forms of untruthful reasoning.
---

# Fallacy, Bias & Manipulation Analysis Framework

A rigorous methodology for auditing natural-language text — articles, speeches, arguments, op-eds, scientific claims, marketing copy, political rhetoric — for flawed reasoning, exploited cognitive biases, rhetorical manipulation, and statistical deception.

---

## Activation

**Only trigger when explicitly requested.** Valid triggers: "Analyse this text for fallacies", "Find the cognitive biases in this argument", "Audit this article's reasoning", "Is this propaganda?", "What rhetorical tricks is this using?", "Stress-test this argument", "Find the manipulation in this."

If no such trigger is present, do not spontaneously run this framework on user-submitted text.

---

## Phase 0 — Pre-Analysis Discipline (Run Before Everything Else)

Four mandatory checks before the audit begins. Failure here contaminates every subsequent phase.

### 0a. Principle of Charity (Steelman First)

Before flagging anything, reconstruct the argument in its **strongest possible form**, using its own best primary phrasing. Many apparent fallacies dissolve once the argument is charitably rephrased. If the charitable reconstruction removes the fault, no fallacy exists — only a poorly-worded point.

```
CHARITABLE RECONSTRUCTION CHECKLIST
□ What is the author's central claim, stated as generously as the text permits?
□ What are the implicit premises a reasonable reader would supply?
□ Is the flawed-looking move perhaps compressed prose, not a real reasoning error?
□ If the move WERE made explicit and clear, would the fault remain?
```

A fallacy flag survives this check only if the reasoning error persists under charitable reading.

### 0b. Genre & Register Awareness

Different text types have different reasoning standards. A tabloid editorial is not a peer-reviewed paper; a stump speech is not a legal brief; a sales page is not a textbook. **Flag what the text fails to do by the standards of its own genre**, not by the standards of formal logic when formal logic is not the genre.

```
GENRE TAGS (pick one or more before analysis):
□ Formal argument (peer-reviewed, legal, philosophical) — full logical rigour expected
□ Journalistic / opinion — expect rhetoric; flag only substantive reasoning faults
□ Political / campaign — expect appeals and framing; flag deception, not persuasion per se
□ Marketing / advertising — expect puffery; flag deceptive claims, not emotion
□ Scientific popularisation — expect simplification; flag distortion, not abbreviation
□ Social-media / polemical — expect compression; flag only load-bearing errors
□ Educational / explanatory — expect pedagogy; flag misconceptions and oversimplifications
□ Interpersonal / manipulative private — expect emotional dynamics; flag coercive patterns
```

### 0c. Author's-Position Neutrality

Do not flag an argument as fallacious merely because its conclusion is wrong, distasteful, or against consensus. A valid argument for a false conclusion is still valid. An invalid argument for a true conclusion is still invalid. Evaluate the reasoning, **not** whether you agree with the outcome.

```
PROHIBITED REASONING SHORTCUTS (for the analyst):
✗ "This conclusion is obviously wrong, therefore the argument must contain a fallacy"
✗ "This author is known for bad arguments, so this one probably is too"
✗ "This conclusion aligns with my priors, so the reasoning must be sound"
✗ "This is on a taboo topic, so any defence of it must be fallacious"
```

### 0d. Burden of Proof Commitment

Before flagging anything, commit to this rule in writing:

> "When I flag a fallacy, bias, or manipulation, I will (1) quote the specific passage, (2) name the specific fault using the taxonomy below, (3) explain why it is fallacious *under charitable reading*, and (4) state what a non-fallacious version of the same move would look like. Labelling without demonstration is itself a fallacy (Argument from Assertion)."

---

## Phase 1 — Text Segmentation & Claim Extraction

Before diagnosing faults, map the argument's skeleton.

### 1a. Extract the thesis
The central claim the text is trying to get the reader to accept. One sentence.

### 1b. Extract the load-bearing sub-claims
The claims that, if removed, would collapse the thesis. These are the claims worth auditing. Non-load-bearing flourishes get lower priority.

### 1c. Map the inferential structure
For each sub-claim: what evidence or reasoning is offered? Does the conclusion follow?

```
ARGUMENT MAP TEMPLATE
─────────────────────────────
Thesis:              [one-sentence central claim]
Load-bearing claims:
  C1: [claim]  ← evidence/reasoning offered: [...]
  C2: [claim]  ← evidence/reasoning offered: [...]
  ...
Implicit premises:   [unstated assumptions required for the argument to work]
Rhetorical frame:    [the emotional/moral framing the text invites]
Intended audience:   [who is being persuaded, and of what]
```

Only after this map is drawn does systematic fault detection begin.

---

## Phase 2 — Formal Fallacy Scan

Formal fallacies are detected from the **structure** of the argument alone, independent of content. If the argument has one of these forms, it is invalid regardless of whether the conclusion happens to be true.

| Fallacy | Schema | Quick Test |
|---------|--------|-----------|
| **Affirming the Consequent** | If P then Q; Q; ∴ P | Could Q be true for a different reason than P? If yes → fallacy. |
| **Denying the Antecedent** | If P then Q; ¬P; ∴ ¬Q | Could Q still be true even without P? If yes → fallacy. |
| **Undistributed Middle** | All A are B; all C are B; ∴ all C are A | The shared term must be universal in at least one premise. |
| **Illicit Major / Minor** | Term distributed in conclusion but not in the premise | Any term in the conclusion must be at least as distributed as in its premise. |
| **Affirming a Disjunct** | A or B; A; ∴ ¬B | Only valid for *exclusive* or; most natural-language "or" is inclusive. |
| **Denying a Conjunct** | ¬(A and B); ¬A; ∴ B | Negating a conjunction does not tell you which conjunct is false. |
| **Four Terms (quaternio terminorum)** | Syllogism with 4 terms instead of 3 (often via equivocation) | Count distinct concepts; must be exactly 3 in a categorical syllogism. |
| **Existential Fallacy** | Universal premises ⇒ particular conclusion about existence | "All unicorns are mammals; therefore there exists a mammalian unicorn" — no. |
| **Base Rate Neglect** | Conditional probability judged without reference to prior probability | Always ask: what is the base rate in the relevant population? |
| **Conjunction Fallacy** | P(A ∧ B) judged greater than P(A) | Conjunctions cannot be more probable than their conjuncts. |
| **Masked-Man Fallacy** | Substituting co-referring terms inside opaque (intensional) contexts | "X knows P about A" + "A = B" ⇏ "X knows P about B". |
| **Non Sequitur (general)** | Conclusion does not follow from premises by any valid form | Catch-all when no specific formal fault applies. |

**Detection discipline:** Write out the argument in standard form (premises above line, conclusion below). If you cannot even put it in standard form, that is a separate finding (often masking an enthymeme or a missing premise).

---

## Phase 3 — Informal Fallacy Scan

Informal fallacies depend on **content, context, and use**. Organised into five traditional families: Relevance, Presumption, Ambiguity, Causation, and Defective Induction.

### 3a. Fallacies of Relevance

Premises are logically unrelated to the conclusion they claim to support.

| Fallacy | Pattern | Red Flag in Text |
|---------|---------|------------------|
| **Ad Hominem (Abusive)** | Attack the person's character instead of their argument | "Only a [insult] would claim..."; bio-dismissal |
| **Ad Hominem (Circumstantial)** | Dismiss argument because of arguer's interests | "Of course a [profession/ideology] would say that" |
| **Ad Hominem (Tu Quoque)** | Reject argument because arguer doesn't practice what they preach | "You drive a car, so you can't talk about climate" |
| **Guilt by Association** | Discredit by linking to disliked group | "This is what [unpopular group] also believes" |
| **Poisoning the Well** | Pre-emptively discredit arguer before they speak | "Before the liar responds, note that..." |
| **Genetic Fallacy** | Judge claim by its origin, not its content | "This idea came from [source], so it's worthless" |
| **Appeal to Authority (inappropriate)** | Cite authority outside their domain, or without evidence | Celebrity endorsements on policy; "experts agree" without naming them |
| **Appeal to Popularity (ad populum)** | "Many people believe P, therefore P" | Polls as proof of truth; "everyone knows" |
| **Appeal to Tradition** | "We've always done it this way, therefore correct" | "For centuries..."; "our ancestors..." |
| **Appeal to Novelty** | "It's new, therefore better" | "Modern research shows..."; "in the 21st century..." |
| **Appeal to Nature** | "Natural = good; artificial = bad" | "All-natural ingredients"; "human beings evolved to..." |
| **Appeal to Emotion (fear / pity / flattery / ridicule / spite)** | Rouse feeling instead of supplying reason | Scare statistics without context; "as a smart reader, you..." |
| **Appeal to Consequences** | "If P were true, bad things would follow, therefore ¬P" | "We can't believe that, or society would collapse" |
| **Appeal to Ignorance (ad ignorantiam)** | "Not proven false → true" or "not proven true → false" | "No one has ever shown it doesn't work" |
| **Red Herring** | Introduce an irrelevant distraction | Topic-changing mid-argument; "but what about..." |
| **Whataboutism** | Deflect criticism by pointing to someone else's faults | "And what about [the other side]?" |
| **Straw Man** | Refute a distorted, weaker version of the opponent's position | Uncharitable paraphrase; quoting out of context |
| **Steelman Failure** | (Inverse Straw Man) Attack the weakest version of a position when a stronger version exists | Ignoring the best-case argument for the opposing view |
| **Two Wrongs Make a Right** | Justify X by pointing to someone else doing X | "They did it first" |

### 3b. Fallacies of Presumption

The argument takes for granted something it needs to prove.

| Fallacy | Pattern | Red Flag |
|---------|---------|----------|
| **Begging the Question (petitio principii)** | Conclusion is smuggled into the premises | Synonymous restatement; "P because P" |
| **Circular Reasoning** | Chain of reasoning eventually returns to its starting point | A → B → C → A |
| **Complex Question** | Question presupposes a disputed claim | "Have you stopped beating your spouse?" |
| **Loaded Question** | Question embeds an unfavourable assumption | "Why does your policy harm children?" |
| **False Dilemma / False Dichotomy** | Only two options presented when more exist | "You're either with us or against us" |
| **False Trilemma** | Same as above, scaled to three | Classic "Liar/Lunatic/Lord" moves |
| **Suppressed Evidence** | Omit known evidence that undercuts the conclusion | Statistics without disconfirming context |
| **Cherry-Picking** | Select only supportive data from a larger set | Quoting the one favourable study; ignoring the body of literature |
| **No True Scotsman** | Redefine a category to exclude counterexamples | "No *true* X would do that" |
| **Moving the Goalposts** | Raise the evidentiary bar each time it is met | "Fine, but now you need to prove [new thing]" |
| **Special Pleading** | Apply a rule universally except in one's favoured case | "Usually it's true, but for [my case] it doesn't apply" |
| **Sunk Cost Fallacy** | Continue because of past investment rather than future expected value | "We've already spent so much, we can't stop now" |
| **Gambler's / Hot-Hand Fallacy** | Treat independent events as dependent (or vice versa) | "Red has hit 5 times, black is due" |

### 3c. Fallacies of Ambiguity

The argument exploits unclear language to shift meaning mid-stream.

| Fallacy | Pattern | Red Flag |
|---------|---------|----------|
| **Equivocation** | Same word used with different meanings in one argument | Key term whose meaning shifts between premise and conclusion |
| **Amphiboly** | Syntactic ambiguity permits multiple readings | Misleading headline structure; dangling modifiers |
| **Accent** | Emphasis (often via ellipsis or quotation) changes the meaning | Out-of-context quotes; selective italics |
| **Composition** | What is true of the parts is true of the whole | "Each player is good, so the team is good" |
| **Division** | What is true of the whole is true of the parts | "The team is good, so each player is good" |
| **Reification (Hypostatisation)** | Treating an abstraction as if it were a concrete thing | "The market wants..."; "Society decided..." |
| **Scope Ambiguity** | Quantifier or negation scope left unclear | "Every student didn't pass" (all failed? or not-all passed?) |

### 3d. Fallacies of Causation

| Fallacy | Pattern | Red Flag |
|---------|---------|----------|
| **Post Hoc Ergo Propter Hoc** | After P, therefore because of P | "Since the new law passed, crime fell" (ignoring trends) |
| **Cum Hoc Ergo Propter Hoc** | Correlation → causation | "X and Y happen together, so X causes Y" |
| **Reverse Causation** | Getting the causal arrow backwards | "Umbrellas cause rain" — actually rain causes umbrellas |
| **Common Cause Ignored** | A third factor Z causes both | Any correlation where Z is not eliminated |
| **Single Cause (Oversimplification)** | Complex event attributed to one factor | "Rome fell because of [one thing]" |
| **Regression Fallacy** | Mistake regression to the mean for causation | "Therapy worked — patient improved after peak symptoms" |
| **Texas Sharpshooter** | Draw target around cluster of hits after the fact | Post-hoc pattern-finding; data dredging passed as discovery |
| **Gambler's Fallacy** | Independent events treated as compensating | See 3b |
| **Slippery Slope** | Small step → inevitable catastrophic chain, without mechanism | "If we allow X, then Y, then Z, then collapse" |

### 3e. Fallacies of Defective Induction

| Fallacy | Pattern | Red Flag |
|---------|---------|----------|
| **Hasty Generalization** | Conclusion from too few / unrepresentative cases | "I met one [X], they were awful; they all are" |
| **Faulty / Biased Sample** | Sample systematically unlike the population | Self-selected online polls treated as representative |
| **Anecdotal Evidence** | A story substituted for a pattern | "My cousin took [remedy] and got better" |
| **Accident (Dicto Simpliciter)** | Apply a general rule to a case where it shouldn't extend | "Free speech is a right; therefore you must publish my letter" |
| **Converse Accident** | Generalise from an exception | Unusual case used as basis for a universal rule |
| **Argument from Incredulity** | "I can't imagine how, therefore it's impossible / divine" | "How could evolution produce an eye? It can't!" |
| **Argument from Ignorance** | See 3a — absence of evidence ≠ evidence of absence | (Exception: when the evidence *would* be expected if true.) |

### 3f. Meta / Discourse Fallacies

Fallacies about the act of arguing itself.

| Fallacy | Pattern |
|---------|---------|
| **Fallacy Fallacy (Argument from Fallacy)** | Concluding a claim is false *because* its defence contained a fallacy. A bad argument for P does not prove ¬P. |
| **Argument from Repetition (ad nauseam)** | Treating reassertion as reinforcement; tireless repetition as proof |
| **Proof by Verbosity (ad lapidem)** | Overwhelming the reader with volume to simulate depth |
| **Gish Gallop** | Rapid-fire series of weak claims, each of which would take disproportionate effort to refute |
| **Kettle Logic** | Defending a position with mutually inconsistent arguments |
| **Middle Ground / False Balance** | Assuming the truth lies midway between two positions regardless of evidence |
| **Continuum Fallacy (sorites)** | Denying a distinction because the boundary is fuzzy |
| **Nirvana / Perfect Solution** | Reject a partial solution because it is not perfect |
| **Moralistic Fallacy** | Inferring "is not" from "ought not" |
| **Naturalistic Fallacy (is-ought)** | Inferring "ought" from "is" |
| **Argumentum ad Baculum** | Appeal to force / threat dressed as argument |
| **Ipse Dixit** | "He said it, therefore true" — bare appeal to assertion |

---

## Phase 4 — Cognitive Bias Scan

Cognitive biases describe **how writers and readers systematically misreason**. Flag biases that the *text exploits or exhibits*, not every bias in the general literature. A comprehensive working taxonomy, grouped by function:

### 4a. Belief-formation biases (how conclusions are reached and preserved)

| Bias | Mechanism | Exploitation Signal in Text |
|------|-----------|-----------------------------|
| **Confirmation bias** | Seek/interpret evidence confirming priors | One-sided citation; disconfirming cases unaddressed |
| **Disconfirmation bias** | Scrutinise counter-evidence harder than supporting | Heavy critique of one side's studies, none of the other |
| **Motivated reasoning** | Accept/reject based on what one wants to be true | Conclusion clearly prefigured by author's interests |
| **Belief perseverance** | Cling to belief after evidence is discredited | Ignoring known retractions |
| **Backfire effect** | Contradicting evidence hardens the belief | Rhetorical defensiveness around refuted claims |
| **Semmelweis reflex** | Reflex rejection of new evidence contradicting paradigm | Dismissing findings for being "heterodox" |
| **Illusory truth effect** | Repeated claims feel true | Repetition as substitute for evidence |
| **Bandwagon / social proof** | "Everyone thinks so → true" | Polling cited as settlement of fact |
| **Authority bias** | Trust ranked by status | Titles and institutions substituted for reasoning |
| **Halo / horn effect** | One good/bad trait colours judgment of all others | Praising/damning the argument via the arguer's unrelated traits |
| **Dunning-Kruger** | Low skill → high confidence | Sweeping confidence from non-expert sources |
| **Anchoring** | First number/frame disproportionately shapes judgment | Opening with extreme figure to set the scale |
| **Availability heuristic** | Easily-recalled cases feel more frequent | Vivid anecdote weighted above statistics |
| **Representativeness heuristic** | Similarity substituted for probability | "Looks like X, therefore is X" |

### 4b. Self-perception biases

| Bias | Mechanism |
|------|-----------|
| **Self-serving bias** | Credit for success, deflect blame for failure |
| **Actor-observer asymmetry** | One's own actions → situational; others' actions → dispositional |
| **Fundamental attribution error** | Over-weight disposition, under-weight situation, when judging others |
| **Naive realism** | "I see the world as it is; dissenters are biased, ignorant, or evil" |
| **False consensus effect** | Assume one's own views are widely shared |
| **Third-person effect** | "Propaganda affects others, not me" |
| **Illusion of control** | Overestimating own agency over chance outcomes |
| **Overconfidence** | Confidence intervals too narrow |
| **Bias blind spot** | Recognising bias in others, not oneself |

### 4c. Memory biases (relevant when text cites memory, testimony, or "what was said / done")

| Bias | Mechanism |
|------|-----------|
| **Hindsight bias** | "I knew it all along" after outcome revealed |
| **Rosy retrospection** | Past remembered as better than it was |
| **Misinformation effect** | Post-event information contaminates memory |
| **Source confusion** | Misattributing where a memory came from |
| **Consistency bias** | Remembering past attitudes as matching current ones |
| **Suggestibility** | Memory shaped by leading questions |

### 4d. Social / group biases

| Bias | Mechanism |
|------|-----------|
| **In-group favouritism** | Better treatment / credence for in-group |
| **Out-group homogeneity** | "They are all alike" |
| **Group attribution error** | Treat individual traits as representative of group |
| **Groupthink** | Consensus-seeking suppresses dissent |
| **System justification** | Defending status quo even when disadvantaged by it |
| **Just-world hypothesis** | Assume victims deserved their fate |
| **Hostile attribution** | Ambiguous action read as malicious |
| **Stereotype reliance** | Group generalisation substituted for evidence about individual |

### 4e. Decision / framing biases

| Bias | Mechanism |
|------|-----------|
| **Loss aversion** | Losses weighted ~2x gains |
| **Endowment effect** | Overvalue what one owns |
| **Status quo bias** | Prefer default option regardless of merit |
| **Framing effect** | Equivalent descriptions yield different choices (gain- vs loss-framing) |
| **Default effect** | Whatever is pre-selected becomes the norm |
| **Optimism / pessimism bias** | Systematic over- or under-estimation of favourable outcomes |
| **Planning fallacy** | Underestimating time / cost / risk |
| **Projection bias** | Assuming future preferences match current ones |
| **Present bias / hyperbolic discounting** | Over-weighting near-term over long-term |

### 4f. Pattern-recognition biases (often the engine of conspiracy, pseudoscience, and spurious causation)

| Bias | Mechanism |
|------|-----------|
| **Apophenia / pareidolia** | Seeing meaningful patterns in random noise |
| **Clustering illusion** | Short streaks feel significant |
| **Illusory correlation** | Noticing a pattern that isn't statistically present |
| **Selection / survivorship bias** | Only seeing what survived the filter (successful companies, wartime-returning planes, etc.) |
| **Publication / reporting bias** | Only published results seen; null results buried |
| **Observer-expectancy effect** | Experimenter unconsciously biases results |

---

## Phase 5 — Rhetorical & Propaganda Technique Scan

Techniques aimed at **persuasion without evidence**. Drawn from the Institute for Propaganda Analysis (1937), Schopenhauer's *Eristic Dialectics* (1831), and contemporary disinformation research.

### 5a. The classical IPA seven + extensions

| Technique | Description | Signal |
|-----------|-------------|--------|
| **Name-Calling** | Attach negative label without argument | Pejoratives used as premises |
| **Glittering Generalities** | Positive vague phrases ("freedom", "values", "innovation") | Abstract virtues with no referent |
| **Transfer** | Associate idea with revered/reviled symbol | Flag, cross, swastika as rhetorical prop |
| **Testimonial** | Endorsement by admired figure | Celebrity on policy; athlete on pharmaceutical |
| **Plain Folks** | Speaker claims kinship with ordinary people | "Folks like us..."; stylised authenticity |
| **Card Stacking** | Present only supportive facts | = Cherry-picking, plus lying by omission |
| **Bandwagon** | "Everyone's doing it" | Inevitability-of-consensus framing |

### 5b. Contemporary manipulation patterns

| Technique | Description |
|-----------|-------------|
| **Firehose of falsehood** | High-volume, multi-channel, inconsistent, rapid, repetitive — exhausts verification |
| **Big Lie** | A falsehood so large, so repeatedly asserted, that its scale becomes its credential |
| **Gaslighting** | Deny the reader's/target's perception of reality; make them doubt their own observation |
| **DARVO** | Deny, Attack, Reverse Victim & Offender |
| **Whataboutism** | Deflect criticism by pointing to real or alleged faults elsewhere |
| **Sealioning** | Endless polite questioning to exhaust the opponent |
| **JAQing off ("just asking questions")** | Smuggle accusation in interrogative form |
| **Concern trolling** | Faux-sympathetic advice designed to undermine |
| **FUD (Fear, Uncertainty, Doubt)** | Raise doubts to stall decisions |
| **Motte-and-Bailey** | Defend an easy claim (motte); use the reputation to smuggle a hard one (bailey) |
| **Kafkatrap** | Any denial of the accusation is treated as proof of it |
| **Galaxy-brained reasoning** | Chain of superficially clever steps reaching an absurd conclusion, with no stop-check |
| **Dog Whistle** | Surface-innocuous phrase carrying specific in-group signal |
| **Framing / Reframing** | Choice of metaphors, categories, and adjectives that pre-load conclusions |
| **Agenda Setting** | Control *which questions are asked*, not *what is said about them* |
| **Overton Window shift** | Introduce an extreme position to normalise a previously-extreme one |
| **Manufactured controversy** | Present settled question as open to create an appearance of debate |
| **Argument by assertion** | Repeat claim as if repetition were evidence |
| **False humility / reluctant conclusion** | "I didn't want to believe it, but..." — fake grudging concession as rhetorical sincerity |

### 5c. Schopenhauer's stratagems (selected — the recurring ones in public discourse)

From *Eristic Dialectic* (1831). Not all 38 matter equally; these are the ones most often encountered in live text:

- **Generalisation (Extension)** — Pump your opponent's statement beyond its original scope, then attack the exaggerated version. (= Straw Man)
- **Homonymy** — Exploit words with multiple meanings. (= Equivocation)
- **Conceal Your Game** — Ask questions in scrambled order to hide where the argument is going.
- **Postulate What Has to be Proved** — Smuggle the conclusion into the premises. (= Begging the Question)
- **Arguments Ad Hominem** — When losing on substance, attack the arguer.
- **Provoke Anger** — Emotional escalation so the opponent reasons badly.
- **Make the Opponent Overstate** — Push them to extreme positions they cannot defend.
- **Claim Victory Despite Defeat** — Assert you have won; enough bystanders will believe it.
- **Last Word** — Whoever speaks last is often remembered as having won, regardless of merit.

---

## Phase 6 — Statistical & Evidential Manipulation Scan

Numerical claims deserve their own audit; more lies are laundered through numbers than through words.

### 6a. Data manipulation

| Pattern | Description | Signal |
|---------|-------------|--------|
| **Cherry-picking** | Select favourable data points | A single study cited against a body of contrary literature |
| **Data dredging (p-hacking)** | Test many hypotheses, report only the "significant" one | Exploratory finding presented as confirmatory |
| **Texas sharpshooter** | Find cluster post-hoc, draw target around it | Pattern discovered in data then tested on same data |
| **Suppressed correlative** | Redefine categories to exclude inconvenient cases | "Among people who really X..." |
| **Survivorship bias** | Only survivors are measured | Success stories in absence of failure data |
| **Selection bias (general)** | Sample systematically unlike population | Self-selection; opt-in surveys |
| **Publication bias** | Null results unpublished | Meta-claims ignoring the file-drawer |

### 6b. Numerical framing

| Pattern | Description |
|---------|-------------|
| **Misleading averages** | Mean used where median or mode is informative (or vice versa) |
| **Missing baseline / denominator** | Absolute number cited without the base |
| **Absolute vs relative risk confusion** | "Doubles your risk" from 0.001% to 0.002% |
| **Percent of percent** | Compounded percentages masking small absolute change |
| **Truncated axes / misleading graphs** | Y-axis not starting at zero; distorted scales |
| **Arbitrary time windows** | Starting point cherry-picked to produce the desired trend |
| **Rate vs. count substitution** | Switching between per-capita and absolute when either is more flattering |
| **False precision** | Three-decimal certainty from noisy data |
| **Composite indices** | Weights chosen to yield desired ranking; weighting hidden |
| **Goodhart's Law exploitation** | When a measure becomes a target, it ceases to be a good measure |

### 6c. Inference errors

| Pattern | Description |
|---------|-------------|
| **Base rate neglect** | Conditional probability evaluated without prior |
| **Simpson's Paradox (exploited)** | Trend in aggregate differs from trend in subgroups — presenting only the aggregate or only the subgroups |
| **Ecological fallacy** | Group-level correlation inferred to individuals |
| **Atomistic fallacy** | Individual-level correlation inferred to groups |
| **McNamara fallacy** | Decide using only what is measured; ignore what isn't |
| **Confounding ignored** | Causal claim without adjustment for known confounders |
| **Reverse causation ignored** | Y causing X interpreted as X causing Y |
| **Statistical vs practical significance conflation** | p<0.05 cited as meaning "the effect matters" |
| **Sampling error vs. systematic error conflation** | Large N used to dismiss bias concerns (it can't) |

### 6d. Source-manipulation signals (echoes Phase 3f of the investigative framework)

- Authority cited without name; "experts say" without identification
- Single original source amplified across many outlets; treated as corroboration
- Conflict-of-interest disclosures absent or buried
- Retracted or superseded studies cited as current
- Quotations with ellipses that change meaning; missing context flagged as irrelevant

---

## Phase 7 — Linguistic Manipulation Scan

Sentence-level tools that pre-load conclusions before reasoning even starts.

### 7a. Weasel words (categorised)

A word or phrase that creates the impression of a meaningful claim while committing to nothing.

| Category | Examples | Why it's a weasel |
|----------|----------|-------------------|
| **Numerically vague** | "many", "most", "some", "up to", "as many as", "a growing number", "leading" | No quantity; deniable on challenge |
| **Agentless passive** | "it is said", "mistakes were made", "it has been decided" | Hides who is making/doing the claim |
| **Anonymous authority** | "experts say", "studies show", "sources confirm" | No way to evaluate expertise or independence |
| **Hedging adverbs** | "arguably", "perhaps", "reportedly", "allegedly", "possibly", "virtually" | Leaves escape hatches in all directions |
| **First-person plural** | "we all know", "as we agree" | Smuggle in consensus |

**Rule:** Weasel words are not always wrong — honest uncertainty exists. Flag only when (a) precision is available but avoided, or (b) the weasel is load-bearing for the argument.

### 7b. Loaded language / dysphemism / euphemism

| Pattern | Example |
|---------|---------|
| **Loaded term (positive)** | "freedom fighters", "pro-life", "reform" |
| **Loaded term (negative)** | "regime", "radicals", "scheme" |
| **Euphemism** | "collateral damage" = civilian deaths; "enhanced interrogation" = torture |
| **Dysphemism** | "death tax" = estate tax |
| **Emotive verbs** | "slammed", "blasted", "rebuked", "admitted", "refused" — each implies a moral valence |
| **Scare quotes** | "his 'evidence'" — discredit without argument |

### 7c. Structural / syntactic manipulation

| Pattern | Description |
|---------|-------------|
| **Nominalisation** | Verb → noun ("the decision was made" vs "X decided") — hides agency |
| **Agentless passive** | "Errors occurred" — hides responsibility |
| **Presupposition smuggling** | Claim embedded inside a question, definite description, or aspectual verb ("when did you stop...", "the failure of their policy", "they continue to...") |
| **Leading questions** | Question shape constrains reply ("How outrageous is...") |
| **Rhetorical questions** | Statement disguised as question to bypass argument |
| **Definitional rigging** | Redefine a term to pre-load the debate ("*true* democracy is...") |
| **Jargon as smokescreen** | Technical vocabulary used to repel scrutiny rather than aid precision |
| **False precision** | "Exactly 67.3% of..." from noisy data |
| **Appeal to common sense** | "Everyone knows..." used as premise |

### 7d. Framing and metaphor

- What **category** the topic is placed in (war? investment? health? sport?) shapes the permissible conclusions.
- What **metaphor** the text repeats (invasion, journey, balance, flood) determines what counts as reasonable.
- What **is named** and what is left **unnamed** determines what is thinkable.

Detection test: Try rewriting the same factual content with the opposite framing. If the conclusion flips, the original frame is doing argumentative work that should be explicit, not implicit.

---

## Phase 8 — Discourse-Structural Manipulation Scan

Tactics that operate across the whole text, not at the sentence level.

| Tactic | Description |
|--------|-------------|
| **Gish Gallop** | Rapid-fire weak claims; refutation of each takes more space than the claim |
| **Motte-and-Bailey** | Alternate between a defensible narrow claim (motte) and an ambitious broad one (bailey); when challenged, retreat to the motte; resume the bailey afterwards |
| **Moving the Goalposts** | Whenever a criterion is met, a new criterion is demanded |
| **Sealioning** | Relentless polite demands for engagement, exhausting the opponent's time |
| **Bait-and-Switch** | Open with a reasonable thesis; quietly swap it for a stronger one in the conclusion |
| **Burying the lede** | Crucial qualifier placed where it will not be read |
| **Asymmetric scrutiny** | Demand rigorous evidence for the disfavoured position, accept weak evidence for the favoured one |
| **Isolated demand for rigour** | Insist on epistemic standards in one domain that are not applied anywhere else |
| **Manufactured urgency** | Frame the debate as requiring immediate action, foreclosing deliberation |
| **False balance / bothsidesing** | Treat disproportionate positions as equivalent |
| **Preemptive framing** | First pages dictate how the rest is read; contrary evidence appears as exception |
| **Context collapse** | Facts true in one frame applied uncritically to another |
| **Narrative lock-in** | Once a story is installed (hero/villain/redemption), contradictory facts are dropped rather than the story |

---

## Phase 9 — Severity & Load-Bearing Assessment

Not every fallacy is equal. Flag each finding with:

### 9a. Load-bearingness
- **Load-bearing**: the argument fails if this move is removed
- **Supporting**: strengthens the case but not essential
- **Rhetorical flourish**: ornamental, not argumentative

**Only load-bearing faults are sufficient to conclude the argument fails.** Supporting faults weaken; rhetorical flourishes are style.

### 9b. Severity
- **Severe**: intentional-looking, multiple reinforcing faults, conclusion unsupported
- **Moderate**: identifiable flaw, argument partly salvageable
- **Mild**: imprecise but defensible under charitable reading

### 9c. Intentionality (stated with epistemic humility)
Intention is not directly observable. Note signals but do not assert:
- Pattern of faults all pointing in one direction?
- Was precision available but avoided?
- Does the author have a professional obligation to know better (journalist, academic, lawyer)?
- Is this the author's pattern across works?

Report as **consistent with / inconsistent with** deliberate manipulation, not as proven intent.

### 9d. Reader-impact
Who is harmed if this argument is believed? What decisions might rest on it? The higher the stakes of belief, the lower the tolerance for even mild faults.

---

## Phase 10 — Steelman & Repair

The final step of any serious audit is **what would a non-fallacious version of this argument look like?**

For each load-bearing flaw identified, produce:

```
REPAIR TEMPLATE
───────────────
Original move:    [quote]
Fault identified: [name + category]
Why fallacious:   [one-sentence explanation]
Steelman version: [the strongest non-fallacious form of the same point]
Residual status:  [after repair — does the argument now succeed, partly succeed, or collapse?]
```

An argument that survives its own repair is stronger than one that was never audited. An argument that collapses under repair was being carried by the faults.

---

## Phase 11 — Verification Checklist

Before presenting an audit as complete:

- [ ] **Charity applied** — Every flag survives the most charitable reading?
- [ ] **Genre-appropriate** — Flags apply the standards the text invites, not mismatched ones?
- [ ] **Quoted evidence** — Every flag names a specific passage, not a vibe?
- [ ] **Taxonomic specificity** — Flags use named categories, not "bad reasoning"?
- [ ] **Explained, not labelled** — For each flag, why is the reasoning faulty?
- [ ] **Load-bearingness assessed** — Are flagged faults critical or incidental?
- [ ] **Repair attempted** — A steelman alternative offered for each load-bearing flaw?
- [ ] **Analyst-bias audited** — Did I flag more aggressively on disliked conclusions? Fewer flags on congenial ones?
- [ ] **Fallacy-fallacy avoided** — Am I claiming the *conclusion* is false, or only the *argument* is unsound?
- [ ] **No double-counting** — Same fault listed once under its most specific category?

---

## Scientific-Method Workflow

```
1. NOTICE      → Text makes claims; is the reasoning offered for them?

2. MAP         → Extract thesis, load-bearing sub-claims, implicit premises

3. DIAGNOSE    → Scan systematically: formal → informal → bias → rhetoric →
                 statistical → linguistic → structural

4. CHARITY-TEST → For each candidate flag: does it survive the most generous
                  reconstruction? If no, drop it.

5. CLASSIFY    → Name each fault precisely; note category and load-bearingness

6. REPAIR      → For each load-bearing flaw, build the steelman alternative

7. AUDIT-SELF  → Check for analyst bias: would I flag this if the conclusion
                 were reversed?

8. PRESENT     → Report faults, severity, repairs, and residual argument status
```

---

## Output Format

```markdown
## Argument Analysis: [Title / opening of text]

### Genre & Register
[Classification from Phase 0b — what standards apply]

### Thesis
[One-sentence central claim]

### Load-Bearing Sub-Claims
| # | Claim | Evidence/Reasoning Offered |
|---|-------|----------------------------|
| C1 | ... | ... |
| C2 | ... | ... |

### Implicit Premises
[Unstated assumptions the argument requires]

### Rhetorical Frame
[Metaphors, categories, emotional register — what is pre-loaded]

### Findings

#### Formal Fallacies
| Passage | Fault | Explanation | Load-bearing? |
|---------|-------|-------------|---------------|

#### Informal Fallacies
| Passage | Family | Specific Fallacy | Explanation | Load-bearing? |
|---------|--------|------------------|-------------|---------------|

#### Cognitive Biases Exploited or Exhibited
| Passage | Bias | Mechanism | Load-bearing? |
|---------|------|-----------|---------------|

#### Rhetorical / Propaganda Techniques
| Passage | Technique | Effect |
|---------|-----------|--------|

#### Statistical / Evidential Manipulation
| Passage | Pattern | Correct Interpretation |
|---------|---------|-----------------------|

#### Linguistic Manipulation
| Passage | Pattern | Neutralised Paraphrase |
|---------|---------|------------------------|

#### Discourse-Structural Manipulation
| Passage or Section | Pattern | Effect |
|--------------------|---------|--------|

### Severity Summary
- Load-bearing faults: [count + list]
- Supporting faults: [count]
- Rhetorical flourishes: [count]
- Overall severity: [Severe / Moderate / Mild]
- Consistency with deliberate manipulation: [Consistent with / Inconsistent with / Inconclusive] + reasoning

### Steelman Repair
For each load-bearing flaw: the strongest non-fallacious version of the same point, and whether the argument survives repair.

### Residual Assessment
[After accounting for faults and repairs, which sub-claims stand, which fall, and which remain undecidable from the text alone.]

### Analyst Self-Audit
[Acknowledgement of any direction in which the analyst's own priors may have shaped the audit, and any flags not raised out of counter-bias caution.]

### What Would Change This Assessment
[What evidence or argument would shift the overall verdict]
```

---

## Quick-Reference Matrix

| When you see... | Suspect... |
|-----------------|------------|
| "Everyone knows", "it is obvious that" | Ad populum, bare assertion |
| "Studies show", "experts say" (unnamed) | Anonymous authority, weasel |
| "If we allow X, next it'll be Y, then Z" | Slippery slope (check mechanism) |
| "You would say that, you're a [label]" | Ad hominem circumstantial |
| "My opponent thinks [absurd version]" | Straw man |
| "The real issue is..." (mid-argument) | Red herring |
| "But what about [other side]?" | Whataboutism |
| "Just asking questions" | JAQing off |
| Vivid anecdote + sweeping conclusion | Hasty generalisation, availability heuristic |
| "Since X happened, Y" (no mechanism) | Post hoc ergo propter hoc |
| "Natural" / "unnatural" as load-bearing | Appeal to nature |
| Same term seems to shift meaning | Equivocation |
| Only favourable examples named | Cherry-picking |
| Percentage with no denominator | Missing baseline |
| Truncated y-axis / nonzero origin | Graphical deception |
| "No true X would..." after counterexample | No true Scotsman |
| Criterion changes after being met | Moving goalposts |
| Claim + retreat + claim pattern | Motte-and-bailey |
| High-volume rapid claims | Gish gallop / firehose |
| "I didn't want to believe it, but..." | False-humility manipulation |
| Agentless passive carrying moral weight | Nominalisation / agency-hiding |

---

## Core Golden Rules (Summary)

**On charity:** The principle of charity is not politeness — it is epistemic self-defence. Flagging every imperfect sentence as fallacious is itself a failure of reasoning. The question is not "could this be phrased better?" but "does this reasoning, charitably understood, actually support its conclusion?"

**On load-bearingness:** A rhetorical flourish is not an argumentative fault. A text may be full of loaded language and still contain a sound core argument. Separate the ornament from the structure before declaring the building unsound.

**On the fallacy fallacy:** Finding a fallacy in an argument tells you the argument fails. It does not tell you the conclusion is false. Many true conclusions have been defended with terrible arguments. Always distinguish: "this argument does not support its conclusion" (a claim about reasoning) from "the conclusion is false" (a claim about the world).

**On intent:** Intent is almost never directly observable from a text. You can identify *patterns consistent with* deliberate manipulation — accumulation of faults all pointing the same direction, precision available but avoided, professional obligation to know better — but treat the question of intent with the epistemic humility it deserves. Bad reasoning and bad faith are different findings; do not conflate them.

**On self-audit:** Before finalising, ask: would I have flagged this as aggressively if the conclusion were one I favour? Would I have been this charitable if the conclusion were one I oppose? The audit applies to the analyst too. An audit that flags opponents' rhetoric while passing allies' identical rhetoric unchallenged is not an audit; it is advocacy with footnotes.

**On language:** Language is not neutral. Every word choice selects a frame, and every frame forecloses some conclusions while enabling others. The goal of a fallacy/bias audit is not to reach neutral language — that is often impossible — but to make the frame *visible*, so the reader can judge whether the frame is earning its place or doing hidden argumentative work.

**On repair:** The mark of a serious audit is that it strengthens honest arguments rather than only demolishing dishonest ones. After identifying what is wrong, identify what a non-fallacious version of the same point would look like. An argument that survives its own audit is stronger than one that was never audited. An argument that collapses under repair was never really an argument — only a performance.

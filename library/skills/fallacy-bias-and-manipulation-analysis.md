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

- `intuitive-thinking` - when a manipulation or framing concern starts as a hunch. Capture it as `(intuition — unwarranted)` before naming fallacies.
This skill is one tool in the truth-seeking toolbox. Compose it with:

- `scientific-fact-classification` — when a flagged passage cites scientific findings, classify the underlying claim's evidence strength rather than only naming the rhetorical move.
- `investigative-reasoning` — when the rhetoric belongs to a contested event, hand the residual claim-set to dual-hypothesis construction.
- `first-principles-thinking` — when a load-bearing premise needs to be decomposed to its bedrock before a fallacy flag is defensible.
- `peer-review` — when the rhetoric is wrapped around a scientific paper, route the paper to full review.
- `belief-revision` — when new evidence emerges about a previously analysed text and a calibrated update is needed.

<!-- include: routing -->

<!-- include: research-discipline -->

<!-- include: warrant-labels -->

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

## Phases 2–8 — Named-Pattern Audit

The catalogue lives in [`references/taxonomy.md`](references/taxonomy.md) — formal
and informal fallacies, cognitive biases, rhetoric and propaganda techniques,
statistical manipulation, linguistic manipulation, and discourse-structural
patterns. **Open it while auditing** and work the families the passage actually
engages; it is lookup material, not a checklist to run end to end.

What does not live there, because it governs every flag regardless of which
pattern is named:

- **Charity first (0a).** A flag survives only if the fault persists under the
  author's strongest reading.
- **Burden (0d).** Quote the passage, name the fault from the taxonomy, explain
  why it holds under charitable reading, and state the non-fallacious version.
  Labelling without demonstration is itself a fallacy.
- **Standard form.** For a formal fault, write the argument with premises above
  the line and conclusion below. Inability to do so is itself a finding.
- **Only load-bearing faults sink an argument.** Rhetorical flourish is noted,
  not counted against the thesis.

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
<!-- include: symmetry-audit -->
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

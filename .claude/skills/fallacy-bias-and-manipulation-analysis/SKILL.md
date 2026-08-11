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

## When This Skill Is Silent Or Ambiguous

First check whether another project skill owns the missing layer: hunch / gut feeling / anomaly signal -> `intuitive-thinking`; scientific claim status -> `scientific-fact-classification`; paper methods/statistics/citations/reproducibility -> `peer-review`; article framing/reporting accuracy -> `journalistic-article-review`; source identity/funding/public records -> `osint-research`; contested events or competing narratives -> `investigative-reasoning`; definitions, hidden assumptions, or argument bedrock -> `first-principles-thinking`; fallacies/rhetoric/statistical framing tricks -> `fallacy-bias-and-manipulation-analysis`; new evidence changing a prior verdict -> `belief-revision`.

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
- **Rule 9** (interactive refinement: user contributions are inputs, not warrants) — applies the moment the user pushes back on a flag, offers a counter-argument, or supplies "actually, this is what the author meant" framing. User contributions are labelled `(user-supplied — unverified)` and treated as hypotheses to test against the text, never as authority that overrides a flag.
- **Rule 10** (objective report voice) — write the audit as a standalone verdict on the claim or text, with no requester references in the report prose.

## Warrant Labels (Project Standard)

Every load-bearing factual claim this skill *invokes* (e.g. "this technique is documented", "this statistic is established") carries a warrant per `CLAUDE.md` / `AGENTS.md`:

| Label | Meaning |
|---|---|
| `(traced)` | Followed the evidence chain to a primary source fetched in this session via WebFetch/WebSearch, or an explicit terminal/API fetch where the browser fetch path is unsuitable. State URL + access date. |
| `(deferred to consensus)` | Relying on a named social/institutional consensus mechanism (literature body, regulatory body, textbook, official record system). Consensus is not scientific warrant; for scientific claims, treat it only as a political/social prior unless traced to reproduced or replicated evidence. |
| `(deferred, fragile)` | Deferred to consensus, but `scientific-fact-classification` Phase 6c failure modes apply — funder capture, ideological capture, prestige cascade, replication crisis, publication bias, or similar. State which. |
| `(memory — unverified)` | Recalled from training data, not verified this session. Permitted only with this label, and never load-bearing without an explicit "this could be wrong" caveat. |
| `(user-supplied — unverified)` | Provided during interactive refinement and not verified in-session. Never load-bearing on its own; treat as a hypothesis to test or an input to verify. |
| `(intuition — unwarranted)` | A gut feeling, anomaly signal, or pattern impression. It may generate hypotheses and search leads. It is never evidence, never load-bearing, and cannot revise, refute, or establish a claim. |

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
- **Symmetry test:** Would the same verdict have been reached if the politically/socially expected answer ran the other way? Name the specific flags (which faults were graded load-bearing, and where the charitable reading was drawn) where the verdict is most sensitive to the prior — asserting symmetry flatly, without identifying where it could break, claims the property rather than showing it. If no — explain. If you can't tell — say so.
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

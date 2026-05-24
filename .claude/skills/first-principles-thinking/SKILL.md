---
name: first-principles-thinking
description: A compact framework for analyzing problems, claims, proposals, or beliefs by decomposing them to their irreducible truths and rebuilding reasoning from the ground up. Use whenever the user wants to dissect a claim, audit an argument, challenge conventional wisdom, redesign a solution from scratch, debug a decision, or asks any variant of "is this actually true?", "why is it done this way?", "what are we assuming?", "break this down from first principles", "is the reasoning sound?", or "what would this look like if we started from zero?". Trigger even when the user doesn't say "first principles" — phrases like "rethink this", "challenge my thinking", "stress-test this idea", or "is this conventional wisdom correct?" should activate it.
---

# First Principles Thinking

A method for stripping a problem, claim, or proposal down to what is actually known to be true, then rebuilding reasoning from that bedrock — so conclusions rest on foundations rather than inheritance.

The goal isn't to be contrarian. It's to separate **what is** from **what is assumed, inherited, or analogized**.

---

## The Engine

Four moves, applied in order. Each move has a single question that defines it.

### 1. State the claim
Write the user's claim, problem, or proposal as a single sentence. If it has multiple parts, list them. This forces precision before analysis — vague claims dissolve under scrutiny without leaving anything to examine.

> Question: **What exactly is being asserted or asked?**

### 2. Decompose
Break the claim into its load-bearing components — the propositions, definitions, causal links, or assumptions it depends on. Each component should be small enough to evaluate on its own.

> Question: **What does this claim rest on?**

### 3. Excavate to bedrock
For each component, ask "how do we know this?" Keep asking until you hit one of three terminations:
- **Bedrock**: a physical law, mathematical truth, definitional truth, or directly observed fact that cannot be reduced further.
- **Assumption**: a belief held without justification, or justified only by convention, analogy, authority, or "that's how it's done."
- **Unknown**: an empirical question whose answer would change the conclusion but isn't currently established.

Label each component clearly. Bedrock is keep. Assumption and Unknown are flagged — they are where reasoning is exposed.

> Question: **Why is this true — and how would I know if it weren't?**

### 4. Rebuild
Using only the bedrock items, reconstruct the answer to the original question from scratch. Then compare the rebuilt answer to the original claim. Three outcomes are possible:
- **Confirmed**: the original claim survives reconstruction. It is well-founded.
- **Refined**: the claim is partly correct but rested on weaker scaffolding than it appeared. State the refined version.
- **Overturned**: the bedrock supports a different conclusion. State it.

> Question: **If I built this up from only what is actually true, what would I get?**

---

## Output format

Use this structure. Keep each section tight — verbosity defeats the purpose.

```
**Claim:** [one sentence]

**Decomposition:**
- C1: [component]
- C2: [component]
- ...

**Excavation:**
- C1 → [Bedrock | Assumption | Unknown]: [one-line reasoning]
- C2 → [Bedrock | Assumption | Unknown]: [one-line reasoning]
- ...

**Rebuild:** [the conclusion that follows from bedrock alone, 1–3 sentences]

**Verdict:** Confirmed | Refined | Overturned — [one sentence why]
```

If the analysis surfaces something the user should investigate further (an Unknown that pivots the answer), add a short **Next** line naming it.

---

## Discipline

A few rules that keep the method honest:

- **Definitions are bedrock only when stipulated.** "Success" or "good" or "efficient" mean nothing until pinned down. If a component depends on an undefined term, the term itself is an Assumption until defined.
- **Authority is not bedrock.** "Expert X says so" is an Assumption — possibly a well-supported one, but inherited. Bedrock is the underlying evidence the expert relied on, not the expert's status.
- **Convention is not bedrock.** "This is the industry standard" explains adoption, not truth.
- **Analogy is not bedrock.** "It's like X, so it should behave like X" is a hypothesis, not a foundation. Useful for generating ideas; invalid as proof.
- **Don't pretend everything reduces to physics.** Useful bedrock is the *most fundamental level relevant to the question*. For "should we restructure this team?", bedrock is facts about humans, incentives, and the work — not quantum mechanics. Stop reducing when further reduction stops changing the answer.
- **One pass is usually enough.** First principles thinking has diminishing returns. If a second pass finds nothing new, stop.

---

## Worked example

**User:** "We should ship our new feature behind a paywall because that's how premium SaaS products monetize."

**Claim:** The new feature should be paywalled because premium SaaS products monetize this way.

**Decomposition:**
- C1: Premium SaaS products monetize by paywalling new features.
- C2: Our product is (or should be) a premium SaaS product.
- C3: What works for premium SaaS will work for us.
- C4: The goal of shipping this feature is to monetize it.

**Excavation:**
- C1 → Assumption: Some do; many monetize via tiering, usage, seats, or bundling. "Paywall new features" is one pattern among several.
- C2 → Unknown: Depends on positioning, which hasn't been stated.
- C3 → Assumption (analogy): Inherited from comparison to other companies, not from our user data.
- C4 → Assumption: Could equally be adoption, retention, or competitive defense — none stated.

**Rebuild:** No bedrock supports the original claim. The decision to paywall depends on (a) what this feature is *for* in the product strategy, and (b) how our users actually respond to pricing changes — neither of which has been established. Defaulting to a paywall because peers do it is reasoning by analogy.

**Verdict:** Overturned — the recommendation rests entirely on inherited assumptions. The real question is what role this feature plays in the product strategy.

**Next:** Define the goal of shipping the feature (monetization vs. adoption vs. retention) before choosing a distribution model.

---

## When to use, when not to

**Use it for:** strategic decisions, contested claims, "we've always done it this way" situations, debugging a stuck argument, evaluating advice, redesigning something from scratch, stress-testing a plan.

**Skip it for:** factual lookups, tasks with a clear correct answer, casual conversation, situations where the user wants execution rather than analysis. Applying this framework to "what's the capital of France?" is theater, not thinking.

If unsure whether the user wants analysis or execution, ask once. The framework is a scalpel, not a hammer.

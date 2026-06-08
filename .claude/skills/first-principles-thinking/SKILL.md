---
name: first-principles-thinking
description: A compact framework for analyzing problems, claims, proposals, or beliefs by decomposing them to their irreducible truths and rebuilding reasoning from the ground up. Use whenever the user wants to dissect a claim, audit an argument, challenge conventional wisdom, redesign a solution from scratch, debug a decision, or asks any variant of "is this actually true?", "why is it done this way?", "what are we assuming?", "break this down from first principles", "is the reasoning sound?", or "what would this look like if we started from zero?". Trigger even when the user doesn't say "first principles" — phrases like "rethink this", "challenge my thinking", "stress-test this idea", or "is this conventional wisdom correct?" should activate it.
version: 1.0
aligned: 2026-05-26
---

# First Principles Thinking

A method for stripping a problem, claim, or proposal down to what is actually known to be true, then rebuilding reasoning from that bedrock — so conclusions rest on foundations rather than inheritance.

The goal isn't to be contrarian. It's to separate **what is** from **what is assumed, inherited, or analogized**.

## Pairs With

- `intuitive-thinking` - when the starting point is unease, a gut feeling, or a suspected hidden assumption that needs conversion into testable hypotheses.
- `scientific-fact-classification` — when a Bedrock candidate is an empirical claim, hand it over for evidence-tier and warrant labelling. "Bedrock" requires more than the analyst's belief that something is foundational.
- `fallacy-bias-and-manipulation-analysis` — when the claim sits inside a rhetorical text; this skill audits structure, that skill audits delivery.
- `investigative-reasoning` — when the Unknowns surfaced by Excavation hide a contested event with primary-source trails to follow.
- `peer-review` — when the claim cites a scientific paper as its bedrock; the paper itself needs auditing.
- `osint-research` — when a foundational fact ("X owns Y", "Z said this") needs identifier-level verification.
- `belief-revision` — when new evidence reveals that a prior Bedrock entry was actually an Assumption (or vice versa) and the rebuild needs re-running.

## When This Skill Is Silent Or Ambiguous

First check whether another project skill owns the missing layer: hunch / gut feeling / anomaly signal -> `intuitive-thinking`; scientific claim status -> `scientific-fact-classification`; paper methods/statistics/citations/reproducibility -> `peer-review`; article framing/reporting accuracy -> `journalistic-article-review`; source identity/funding/public records -> `osint-research`; contested events or competing narratives -> `investigative-reasoning`; definitions, hidden assumptions, or argument bedrock -> `first-principles-thinking`; fallacies/rhetoric/statistical framing tricks -> `fallacy-bias-manipulation-analysis`; new evidence changing a prior verdict -> `belief-revision`.

If no skill clearly owns the gap, reason from first principles and explicit warrants. Built-in knowledge may suggest hypotheses, search terms, possible failure modes, or questions to verify, but any empirical premise remains `(memory — unverified)` until traced. Reasoning may connect warranted premises; it may not manufacture premises.

## Research Discipline (CLAUDE.md/AGENTS.md)

First-principles is a conceptual tool — it does not normally fetch sources. But when an Excavation reaches `Bedrock` via an empirical claim, the rules in `CLAUDE.md` / `AGENTS.md` → *Operating rules* bind the verification of that Bedrock:

- **Rule 1** (pre-search hypothesis registration) — before excavating, register the prior expectation of the verdict (Confirmed / Refined / Overturned). Otherwise the decomposition selects the answer.
- **Rule 2** (steelman from primary literature) — built into Phase 1 ("State the claim" in its strongest form).
- **Rule 3** (primary before secondary) — when Bedrock cites a study or authority, fetch the primary; `(memory — unverified)` Bedrock is downgraded to Assumption.
- **Rule 4** (map institutional networks) — applies when an empirical Bedrock candidate rests on multiple sources or authorities; shared funding / mandate / ownership counts as one node.
- **Rule 5** (Tier 0 priority) — applies when the Bedrock candidate is historical or time-sensitive; contemporary primary sources outrank later retrospectives.
- **Rule 6** (bias self-audit) — enforced in `## Self-Audit`.
- **Rule 7** (minimum search volumes) — applies only when the empirical sub-claim is contested; otherwise hand the sub-claim to `scientific-fact-classification` or `investigative-reasoning`.
- **Rule 8** (hostility check on sources) — applies when a Bedrock candidate relies on authority, consensus, or source claims with visible stakes.
- **Rule 9** (interactive refinement) — applies the moment the user pushes back on an Excavation label ("no, that's actually Bedrock, not Assumption"). User contributions are labelled `(user-supplied — unverified)` and treated as a stipulation candidate — useful for surfacing where the user's definition differs from the surface claim, never as authority to relabel an Assumption as Bedrock without external verification.
- **Rule 10** (objective report voice) — write the analysis as a standalone verdict on the claim, with no requester references in the report prose.

## Warrant Labels (Project Standard)

When an Excavation reaches `Bedrock` via an empirical claim — not via definition, formal logic, or direct observation in this conversation — attach a warrant per `CLAUDE.md` / `AGENTS.md`:

| Label | Meaning |
|---|---|
| `(traced)` | Followed evidence chain to a primary source fetched in this session. State URL + access date. |
| `(deferred to consensus)` | Relying on a named social/institutional consensus mechanism, such as a literature body, regulatory body, official record system, or textbook. Consensus is not scientific warrant; for scientific claims, treat it only as a political/social prior unless traced to reproduced or replicated evidence. |
| `(deferred, fragile)` | Deferred to consensus, but failure modes apply: funder capture, ideological capture, prestige cascade, replication crisis, or similar. State which. |
| `(memory — unverified)` | Recalled from training data, not verified this session. Never load-bearing without an explicit caveat that it could be wrong. |
| `(user-supplied — unverified)` | Provided during interactive refinement and not verified in-session. Treat as a hypothesis or stipulation candidate, never as authority. |
| `(intuition — unwarranted)` | A gut feeling, anomaly signal, or pattern impression. It may generate hypotheses and search leads, but is never evidence and never load-bearing. |

A "Bedrock" that is only `(memory — unverified)` should be downgraded to `Assumption` unless verified.

If sources are fetched, record for each cited source: URL, access date, publication date where relevant, warrant label, and funding / ownership / mandate / national alignment where relevant.

---

## The Engine

Four moves, applied in order. Each move has a single question that defines it.

### 1. State the claim
Write the user's claim, problem, or proposal as a single sentence. If it has multiple parts, list them. This forces precision before analysis — vague claims dissolve under scrutiny without leaving anything to examine.

When the claim circulates in multiple variants (official, popular, adversarial), name the speaker and timestamp of the variant being decomposed. If multiple variants matter, decompose each — averaging them obscures which version actually fails the rebuild.

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

## Output

Use this structure. Keep each section tight — verbosity defeats the purpose. Closing sections (What Would Change This / Self-Audit / Limits) may be omitted when they add no signal; include them when an Unknown is load-bearing, when the verdict could be politically charged, or when scope was constrained.

```markdown
# First Principles Analysis: [claim, abbreviated]

## Summary
- **Claim:** [one sentence]
- **Verdict:** Confirmed | Refined | Overturned — [one sentence why]

## Decomposition
- C1: [component]
- C2: [component]
- …

## Excavation
- C1 → Bedrock | Assumption | Unknown — [one-line reasoning]
- C2 → Bedrock | Assumption | Unknown — [one-line reasoning]
- …

## Rebuild
[1–3 sentences — the conclusion that follows from bedrock alone]

## What Would Change This
[Which Unknown, if answered, or which Assumption, if revised, would flip the verdict. Omit if none.]

## Sources & Warrants
[Include only when empirical Bedrock or outside sources were invoked.]

| Component | Source | URL | Access date | Publication date | Warrant | Funding / ownership / mandate / alignment |
|---|---|---|---|---|---|---|

## Self-Audit
- **Symmetry test:** Would I have reached the same verdict if the politically/socially expected answer ran the other way? If no — explain. If you can't tell — say so.
- **Counter-test:** Would the verdict differ if the claim were rephrased with all definitions stipulated? If yes, the verdict turns on definitional drift, not on substantive Bedrock disagreement.
- **Bedrock discipline:** Did I treat authority, convention, or analogy as bedrock anywhere? Did any empirical Bedrock entry lack a `(traced)` warrant?

## Limits of This Analysis
[Bedrock items left unverified; domain expertise gaps. Omit if not applicable.]
```

---

## Discipline

A few rules that keep the method honest:

- **Definitions are bedrock only when stipulated.** "Success" or "good" or "efficient" mean nothing until pinned down. If a component depends on an undefined term, the term itself is an Assumption until defined. A stipulation counts as Bedrock only if it (i) preceded or accompanied the claim and (ii) was reasonably available to the audience at the time. Retroactive narrowing ("we never said X, we said Y") does not retro-promote an Assumption to Bedrock.
- **Authority is not bedrock.** "Expert X says so" is an Assumption — possibly a well-supported one, but inherited. Bedrock is the underlying evidence the expert relied on, not the expert's status.
- **Convention is not bedrock.** "This is the industry standard" explains adoption, not truth.
- **Analogy is not bedrock.** "It's like X, so it should behave like X" is a hypothesis, not a foundation. Useful for generating ideas; invalid as proof.
- **Named frameworks are claims, not credentials.** If the source invokes a named criterion ("fulfils Koch's postulates", "meets CONSORT", "satisfies the precautionary principle", "passes the Turing test"), do not pass through the invocation. Decompose the framework's actual requirements as load-bearing components and excavate each. Invocation is evidence of intent, not of fulfilment. The deepest failures hide one level up from the surface claim — when a claim cites a framework, decompose the framework too. A claim that *requires* a framework the speaker did not supply (e.g. "stopped transmission" implicitly requires definitions of "stopped", "transmission", and a transmission-blocking framework) sits on an *implicit* framework — decompose it even when nothing was invoked by name.
- **Don't pretend everything reduces to physics.** Useful bedrock is the *most fundamental level relevant to the question*. For "should we restructure this team?", bedrock is facts about humans, incentives, and the work — not quantum mechanics. Stop reducing when further reduction stops changing the answer.
- **One pass is usually enough.** First principles thinking has diminishing returns. If a second pass finds nothing new, stop.

---

## Worked example

**User:** "We should ship our new feature behind a paywall because that's how premium SaaS products monetize."

# First Principles Analysis: paywall the new feature

## Summary
- **Claim:** The new feature should be paywalled because premium SaaS products monetize this way.
- **Verdict:** Overturned — the recommendation rests entirely on inherited assumptions.

## Decomposition
- C1: Premium SaaS products monetize by paywalling new features.
- C2: Our product is (or should be) a premium SaaS product.
- C3: What works for premium SaaS will work for us.
- C4: The goal of shipping this feature is to monetize it.

## Excavation
- C1 → Assumption — some do; many monetize via tiering, usage, seats, or bundling. "Paywall new features" is one pattern among several.
- C2 → Unknown — depends on positioning, which hasn't been stated.
- C3 → Assumption (analogy) — inherited from comparison to other companies, not from our user data.
- C4 → Assumption — could equally be adoption, retention, or competitive defense; none stated.

## Rebuild
No bedrock supports the original claim. The paywall decision depends on (a) what this feature is *for* in the product strategy, and (b) how our users actually respond to pricing changes — neither established. Defaulting to a paywall because peers do it is reasoning by analogy.

## What Would Change This
Defining the feature's role in product strategy (monetization vs. adoption vs. retention) would resolve C4 and pivot the answer. Evidence from our own users' price-response would replace C3's analogy with data.

---

## When to use, when not to

**Use it for:** strategic decisions, contested claims, "we've always done it this way" situations, debugging a stuck argument, evaluating advice, redesigning something from scratch, stress-testing a plan.

**Skip it for:** factual lookups, tasks with a clear correct answer, casual conversation, situations where the user wants execution rather than analysis. Applying this framework to "what's the capital of France?" is theater, not thinking.

If unsure whether the user wants analysis or execution, ask once. The framework is a scalpel, not a hammer.

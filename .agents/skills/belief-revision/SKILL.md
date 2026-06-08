---
name: belief-revision
description: A structured framework for AI agents to revise a prior verdict, classification, hypothesis, or analysis when new evidence emerges — calibrated against both under-correction (anchoring on the prior) and over-correction (anchoring on novelty or social pressure). Use whenever the task involves updating a previously reached conclusion in light of new information, reconsidering a verdict after primary sources are fetched, deciding whether a contested claim should change classification, integrating a late-breaking piece of evidence into an existing investigation or peer review, or any request to "update this", "revise this", "rethink this in light of X", "does this new evidence change anything", "should I change my mind". Pair with whichever analytical skill produced the prior — this skill takes that output and produces a calibrated revision in its format.
version: 1.0
aligned: 2026-05-26
---

# Belief Revision

Update a prior verdict when new evidence emerges — calibrated, traceable, and protected against both under-correction (anchoring on the prior) and over-correction (anchoring on novelty or social pressure).

Most belief revision fails on one of two traps: people under-update because the prior verdict has become identity, or over-update because the new evidence is dramatic and recent. This skill structurally exposes both.

## Activation

Trigger only when explicitly requested: *"update this verdict"*, *"revise this analysis"*, *"new evidence came in — does it change anything?"*, *"should I change my mind?"*, *"rethink this in light of X"*, *"update the classification of Y given Z"*.

Do not trigger for:
- First-pass analysis (use the relevant primary skill)
- Scope changes that don't involve new evidence (those are reframings, not revisions)
- Editorial polish of a prior output

## Pairs With

This skill takes a prior analytical output and produces a revision in its format. Compose with:

- `intuitive-thinking` - when a new hunch challenges the prior verdict but has not yet been tied to new evidence. Capture it as `(intuition — unwarranted)` before revising.
- The skill that produced the prior verdict — `investigative-reasoning`, `peer-review`, `scientific-fact-classification`, `fallacy-bias-and-manipulation-analysis`, `osint-research`, or `first-principles-thinking`. The revision is output in that skill's report shape.
- `investigative-reasoning` Phase 3i (Source Triangulation) — when the new evidence conflicts with prior sources, triangulate before revising.
- `scientific-fact-classification` — when the revision requires re-classifying a claim's strength label.

## When This Skill Is Silent Or Ambiguous

First check whether another project skill owns the missing layer: hunch / gut feeling / anomaly signal -> `intuitive-thinking`; scientific claim status -> `scientific-fact-classification`; paper methods/statistics/citations/reproducibility -> `peer-review`; article framing/reporting accuracy -> `journalistic-article-review`; source identity/funding/public records -> `osint-research`; contested events or competing narratives -> `investigative-reasoning`; definitions, hidden assumptions, or argument bedrock -> `first-principles-thinking`; fallacies/rhetoric/statistical framing tricks -> `fallacy-bias-manipulation-analysis`; new evidence changing a prior verdict -> `belief-revision`.

If no skill clearly owns the gap, reason from first principles and explicit warrants. Built-in knowledge may suggest hypotheses, search terms, possible failure modes, or questions to verify, but any empirical premise remains `(memory — unverified)` until traced. Reasoning may connect warranted premises; it may not manufacture premises.

## Research Discipline (CLAUDE.md/AGENTS.md)

Belief revision is itself an analytical act. The rules in `CLAUDE.md` / `AGENTS.md` → *Operating rules* bind:

- **Rule 1** (pre-revision hypothesis registration) — Phase 0b mandates predicting the update direction before incorporating the new evidence. Otherwise the revision is confabulated post-hoc to match what you wanted to find.
- **Rule 2** (steelman from primary literature) — the new evidence must be steelmanned from its source's own statement; not from critics or summaries.
- **Rule 3** (primary before secondary) — new evidence must be traced to a primary source. "I heard X said Y" is not revision-ready.
- **Rule 4** (map institutional networks) — is the new evidence from a source-node already counted in the prior, or genuinely new?
- **Rule 5** (Tier 0 priority) — for time-sensitive or historical revisions, contemporary primary sources outrank later retrospective smoothing.
- **Rule 6** (bias self-audit) — was the revision driven by evidence or by social / career / political pressure?
- **Rule 7** (minimum search volumes) — revision across verdict categories requires enough source depth to match the prior claim's stakes; thin evidence can refine, not overturn.
- **Rule 8** (hostility check) — does the new evidence's source have skin in the revision direction?
- **Rule 9** (interactive refinement) — the most consequential rule for this skill. The user's own "new evidence" — whether a fact they assert, a claim they vouch for, or pressure for a particular revision direction — is labelled `(user-supplied — unverified)` and cannot drive a revision until traced to a primary source. The Asymmetric-Warrant Rule binds: `(user-supplied — unverified)` cannot overturn `(traced)` any more than `(memory — unverified)` can. If the user pushes for an Overturned status without supplying a verifiable source, the honest status is Refined (in the parts the unverified input could legitimately reach: open questions, "what would change this") — not Overturned.
- **Rule 10** (objective report voice) — write the revision as a standalone update to the prior verdict, with no requester references in the report prose.

## Warrant Labels (Project Standard)

Use the standard warrant labels:

| Label | Meaning |
|---|---|
| `(traced)` | Followed evidence chain to a primary source fetched in this session. State URL + access date. |
| `(deferred to consensus)` | Relying on a named social/institutional consensus mechanism, such as a literature body, regulatory body, official record system, or textbook. Consensus is not scientific warrant; for scientific claims, treat it only as a political/social prior unless traced to reproduced or replicated evidence. |
| `(deferred, fragile)` | Deferred to consensus, but failure modes apply: funder capture, ideological capture, prestige cascade, state secrecy, replication crisis, or similar. State which. |
| `(memory — unverified)` | Recalled from training data, not verified this session. Never load-bearing without an explicit caveat that it could be wrong. |
| `(user-supplied — unverified)` | Provided during interactive refinement and not verified in-session. Treat as a hypothesis to test, never as authority. |
| `(intuition — unwarranted)` | A gut feeling, anomaly signal, or pattern impression. It may generate hypotheses and search leads, but is never evidence and never load-bearing. |

This skill adds one extension: **the revised verdict inherits the lower of (prior verdict's warrant, new evidence's warrant).** Overturning a `(traced)` prior with `(memory — unverified)` or `(user-supplied — unverified)` new evidence is not a calibrated revision; it is anchoring on the most recent thing read or said.

The asymmetric-warrant rule binds especially when the user is the source of the "new evidence":

- `(user-supplied — unverified)` cannot overturn `(traced)`.
- `(user-supplied — unverified)` cannot overturn a traced evidence base. It can challenge `(deferred to consensus)` only by turning the consensus into a hypothesis to audit; revision requires a verifiable primary source that survives source-status / CoI / institutional-network checks.
- User contributions that come with a URL must be fetched in-session before being promoted to `(traced)`. A URL the user supplies is not yet `(traced)` — the agent's own fetch is.

---

## Phase 0 — Pre-Revision Discipline

**0a. Anchor declaration.** *Before reading the new evidence in detail*, write down:
- The prior verdict in one sentence
- The two or three load-bearing claims the prior verdict rests on
- The prior confidence level (Low / Medium / High) and what would have shifted it
- The analyst's own priors at the time of the prior (acknowledged direction)

This makes the anchor visible. Without it, the revision unconsciously rewrites the prior to be more compatible with whichever way the new evidence pushes.

**0b. Predicted update.** *Before incorporating*, predict in writing:
- What direction the new evidence will push (toward / away from prior)
- How much (small / moderate / large)
- Which of the load-bearing claims it most affects

After incorporating, compare. A revision that wildly diverges from the prediction is more consequential than expected — or you over-anchored on the prior at prediction time. Both are findings.

**0c. Pressure-direction check.** Is the *expected* revision direction the politically / socially / institutionally rewarded one? Note explicitly:
- Rewarded → apply extra scrutiny
- Punished → apply extra scrutiny in the other direction (don't pre-emptively under-revise to stay safe)
- Neutral → ordinary scrutiny

Honest naming of the pressure direction is what keeps the revision calibrated.

---

## Phase 1 — Prior Analysis Decomposition

Extract from the prior output:

- **Load-bearing claims** — which, if overturned, collapse the verdict?
- **Supporting claims** — present, but the verdict survives if any one falls
- **Assumptions treated as established** but not themselves load-bearing
- **Disconfirming evidence already considered** — and the documented reason it was discounted

The new evidence is only consequential to the headline verdict if it hits load-bearing claims. If it hits supporting or non-load-bearing material, the verdict shifts in detail but the headline stands. Mark this distinction explicitly — the most common over-correction is treating a non-load-bearing update as a verdict-overturning one.

---

## Phase 2 — New Evidence Audit

Apply normal source-tier / CoI / warrant / institutional-network discipline:

- **Source tier** — per `investigative-reasoning` Phase 3b
- **CoI demotion** — apply, especially severe if source has stake in the revision direction
- **Warrant label** — `(traced)` only if fetched this session via WebFetch / WebSearch with URL + date; otherwise `(memory — unverified)`. If the user supplied the claim verbally without a URL, the label is `(user-supplied — unverified)`. If the user supplied a URL, the agent must fetch it in-session before promoting to `(traced)` — the user's claim that the URL says X does not substitute for the fetch.
- **Network position** — is the new evidence from a source-node already counted in the prior (then it adds to that node's weight, not to the count of independent nodes), or genuinely new?
- **Mechanism vs. data-point** — does the new evidence change the underlying causal / explanatory model, or just add another data point consistent with one of the existing models?
- **Trace direction** — does the new evidence claim to overturn, augment, refine, or contradict the prior?
- **User as source.** When the user *is* the source of the "new evidence", they are subject to the same hostility check as any other source: the user has priors, stakes in the revision direction, and reasons to want a particular outcome. Apply Rule 9 explicitly — the user's contribution becomes a hypothesis to test, not an authority to defer to.

A piece of new evidence that turns out to be the same node as a prior source, demoted for CoI, with `(memory — unverified)` or `(user-supplied — unverified)` warrant, claiming to overturn a `(traced)` finding — should not produce a revision. Most "new evidence" fails one or more of these tests.

---

## Phase 3 — Revision Computation

For each load-bearing claim in the prior:

| Prior load-bearing claim | New evidence's effect | Direction | Magnitude |
|---|---|---|---|
| C1 | Confirms / Weakens / Overturns / Orthogonal | ↑ / ↓ / 0 / shift | Small / Moderate / Large |

Combined effect on the headline verdict — **five possible statuses:**

- **Confirmed** — new evidence supports the prior; confidence increases. State the new confidence level.
- **Refined** — prior partly correct; specific sub-claims revised; headline stands. State which sub-claims shifted.
- **Shifted** — verdict moves to a related but distinct position. State the new position and why the shift is more parsimonious than the prior.
- **Overturned** — prior verdict no longer supportable. State why — and require this only when new evidence's warrant is at least as strong as the prior's.
- **Suspended** — new evidence introduces enough uncertainty that no verdict is currently warranted. State what would re-warrant a verdict in either direction.

> **Asymmetric warrant rule.** A revision that crosses status categories (e.g. Refined → Overturned) requires new evidence whose warrant is at least as strong as the prior's. `(memory — unverified)` cannot overturn `(traced)`. Otherwise the revision is just anchor-swapping.

---

## Phase 4 — Calibration Audit

Both traps must be checked, in writing:

### 4a. Under-correction (anchor on prior)

- Did I find reasons to discount the new evidence that I would not have found if I had no prior?
- Am I requiring more evidence to update *away from* the prior than I required to *establish* the prior in the first place?
- **Fresh-analyst test:** if a competent analyst saw only the new evidence and not the prior, would they reach the same verdict as my revision? If the fresh analyst would update further, my revision is anchored.

### 4b. Over-correction (anchor on novelty / social pressure)

- Did the new evidence prompt a revision proportional to its actual weight, or am I over-reacting to its novelty / dramatic content?
- **Time-symmetry test:** if the new evidence had been published five years earlier alongside the prior evidence, would I have weighted it the same way I'm weighting it now? If recency is doing argumentative work, downweight.
- **Social-reward check:** am I revising because the prior is genuinely undermined, or because revising in this direction is currently institutionally / socially rewarded?

### 4c. Verdict-stability test

Most calibrated revisions are *Refined* or *Shifted*. *Overturned* should be rare; *Suspended* is honest when the new evidence is consequential but ambiguous. If the revision is constantly hitting *Overturned*, the prior was poorly built (too brittle) or the revisions are over-correcting.

---

## Phase 5 — Verification Checklist

- [ ] Anchor declared in writing before reading new evidence (0a)
- [ ] Update predicted in writing before incorporating (0b)
- [ ] Pressure-direction named (0c)
- [ ] New evidence's warrant labelled and source-network mapped
- [ ] Asymmetric-warrant rule respected (low-warrant evidence cannot overturn high-warrant prior)
- [ ] Both under- and over-correction explicitly checked (4a, 4b)
- [ ] Fresh-analyst test executed honestly
- [ ] Bias self-audit on the *revision direction*, not the prior

---

## Output

```markdown
# Belief Revision: [subject]

## Summary
- **Prior verdict (one sentence):**
- **New evidence (one sentence):**
- **Revised verdict (one sentence):**
- **Status:** Confirmed | Refined | Shifted | Overturned | Suspended
- **Confidence shift:** [prior level] → [revised level]

## Anchor Declaration (Phase 0a)
- **Prior verdict:** [one sentence as written before re-reading]
- **Prior load-bearing claims:** C1, C2, …
- **Prior confidence:** Low / Medium / High
- **Analyst's prior on this topic:** [direction]

## Predicted Update (Phase 0b)
- **Direction predicted:** toward / away from prior
- **Magnitude predicted:** Small / Moderate / Large
- **Actual vs. predicted:** [matches / over- / under-]

## Pressure-Direction Check (Phase 0c)
- **Expected revision direction is socially / politically / institutionally:** Rewarded / Punished / Neutral
- **Extra scrutiny applied:** [yes / no / direction]

## New Evidence Audit (Phase 2)
| # | Source | URL | Access date | Publication date | Warrant | Source tier | CoI / alignment | Network position | Claim |
|---|---|---|---|---|---|---|---|---|---|

## Revision per Load-Bearing Claim (Phase 3)
| Prior claim | New evidence's effect | Direction | Magnitude |
|---|---|---|---|

## Combined Verdict
[Revised verdict, ≥1 paragraph, explicit about which claims shifted and which held]

## Calibration Audit (Phase 4)
- **Under-correction check (4a):** [executed honestly — fresh-analyst test result]
- **Over-correction check (4b):** [executed honestly — time-symmetry test result]
- **Verdict-stability:** [why this status, not an adjacent one]

## Self-Audit
- **Symmetry test:** Would I have made the same revision if the new evidence had pointed the other way? If no — explain.
- **Asymmetric-warrant rule respected?** [yes / no]
- **What would revise this further:** [evidence whose appearance would shift the revised verdict]

## Limits of This Revision
[New evidence not yet accessible; sources contested; expertise gaps]
```

---

## Quick Reference

| Pattern | Suspect | Default move |
|---|---|---|
| New evidence `(memory — unverified)` cited to overturn `(traced)` prior | Anchor-swapping | Apply asymmetric-warrant rule; do not overturn |
| Revision direction matches what's socially rewarded; under-scrutinised | Pressure-driven update | Apply 4b time-symmetry and social-reward checks |
| Revision direction *opposite* to what's socially rewarded; under-scrutinised | Reactionary anchoring | Same checks in the other direction — don't under-revise to stay safe |
| New evidence is from same node as prior, presented as independent | Single-origin amplification | Hand to `investigative-reasoning` Phase 3i (Source Triangulation) |
| Frequent "Overturned" revisions across iterations | Brittle prior, or over-correcting | Audit whether priors are being built too thin |
| "I always knew this was wrong" after seeing new evidence | Hindsight bias contaminating prior | Re-anchor in writing what the prior actually said |
| Revision changes the headline but no load-bearing claim was hit | Non-load-bearing update inflated | Restrict revision to the actual claim affected |

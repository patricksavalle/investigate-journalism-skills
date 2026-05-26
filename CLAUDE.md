# Research discipline (this repository)

This repo contains analytical skills for journalism, investigation, and claim-auditing. The risk these skills exist to mitigate — reasoning from memory, deferring to inherited narrative, laundering training-data bias as analysis — is **easy for an AI to reproduce silently**.

This file sets the discipline. A `Stop` hook in `.claude/settings.json` provides automated enforcement (see "Enforcement" below).

## Core rule: warrant on every load-bearing claim

When producing analytical output of any kind — investigation, claim audit, fact classification, peer review, fallacy analysis, OSINT profile, first-principles audit — **every load-bearing factual claim must carry a warrant label**:

| Label | Meaning |
|---|---|
| `(traced)` | Followed evidence chain to a primary source fetched in this session via WebFetch or WebSearch. URL + access date stated. |
| `(deferred to consensus)` | Relying on a named consensus mechanism (peer-reviewed body of literature, regulatory body, textbook). Said body must be named. |
| `(deferred, fragile)` | Deferred to consensus but `scientific-fact-classification` Phase 6c failure modes (funder capture, ideological capture, prestige cascade, replication crisis, etc.) apply. State which. |
| `(memory — unverified)` | Recalled from training data, not verified this session. Permitted only with this label, and never load-bearing without an explicit "this could be wrong" caveat. |
| `(user-supplied — unverified)` | Provided by the user during interactive refinement (an asserted fact, a counter-argument's premise, a "consider this" claim). Never load-bearing on its own; treated as a hypothesis to test or an input to verify. See Rule 9. |

The point is not to eliminate `(memory)` use — some claims are genuinely background knowledge. The point is **to make memory-reliance visible** so the reader, and Claude itself, can see where verification is missing.

**Strictness on `(traced)`.** `(traced)` is **per-session, not lifetime**. If you did not fetch the primary in *this* conversation via WebFetch or WebSearch — and state the URL + access date — the label is `(memory — unverified)`, even when the chain is well-known and the analyst could fetch it. Confidence about an unverified chain belongs in surrounding prose ("the evidence chain is well-documented in [X]; I can describe it but did not fetch in this session") — never laundered into a `(traced)` label. The label's weight comes from *what was actually done this turn*; weakening it weakens the entire discipline.

## Operating rules

These apply to any turn that invokes — or whose output substantively reflects — one of these skills:

- `investigative-reasoning`
- `peer-review`
- `scientific-fact-classification`
- `fallacy-bias-manipulation-analysis-framework`
- `osint-research`
- `first-principles-thinking` (when applied to empirical claims)

### 1. Pre-search hypothesis registration
Before the first search, write down the hypotheses being tested. Top results frame the question; pre-registering them prevents the search from selecting which question gets answered.

### 2. Steelman from primary literature
For any contested position, fetch its **own advocates' primary writing**, not critics' summaries. Apply this symmetrically — the official narrative gets the same treatment.

### 3. Primary before secondary
When a secondary source characterises a paper, court filing, dataset, speech, or document, fetch the primary item before citing. Cite both, prefer the primary.

### 4. Map institutional networks
Before treating multiple sources as independent corroboration, map shared funding, mandate, ownership, and national alignment. Connected sources = one node. Ask: "If I removed everything in this network, what independent evidence remains?"

### 5. Tier 0 priority for time-sensitive claims
For historical or politically settled events, contemporary primary sources (newspapers, telegrams, court filings, eyewitness accounts dated *at* the event) outrank later retrospectives. Narratives drift; retrospectives sanitise. Record publication date of every source.

### 6. Bias self-audit
End every analytical output by answering, in writing: **"Would I have reached the same verdict if the politically/socially expected answer were reversed?"** If no — explain. If you can't tell — say so.

### 7. Minimum search volumes
- Simple claim audit: ≥5 sources fetched
- Moderate investigation: ≥10
- Complex / narrative-captured event: ≥20, geopolitically diversified
- Beyond 40: recommend a dedicated deep-research session

### 8. Hostility check on sources
For every cited source name funding, ownership, and (where relevant) national alignment. A peer-reviewed paper on glyphosate safety from a Monsanto-funded lab is not the same warrant as the same paper from an independent group, and both must be labelled.

### 9. Interactive refinement: user contributions are inputs, not warrants

When the user pushes back, fine-tunes, or adds context during the analysis, their contributions are *inputs to be verified*, not facts to be incorporated. The audit-chain property is the toolbox's load-bearing value — it cannot be compromised by interactive pressure, including pressure from the user. A reviewer reproducing the chain did not agree to trust the user; the chain must preserve the distinction between user-input and source-traced input *for the reviewer's sake*, not as distrust of the user.

**The failure mode this rule exists to prevent.** "The user said X, so I updated the analysis." This is the interactive version of memory-laundering. It contaminates the chain because a third party cannot reproduce the chain without knowing which steps were user-driven and which were source-driven — and because the user has their own facts, framings, biases, and stakes in the revision direction, the same way every other source does.

**Procedure when the user contributes during refinement.**

1. **Classify the contribution.**
   - **New primary source** (URL, document, citation supplied by the user) → fetch and verify in-session; apply the same source-tier / CoI / institutional-network checks as any other source. Promote to `(traced)` only if the fetch succeeds and supports the claim.
   - **Factual claim without source** → label `(user-supplied — unverified)`; never load-bearing. May be incorporated as a *hypothesis to test*, not as established evidence.
   - **Argument or framing** → treat as a steelman candidate to compete against the current analysis (per dual-hypothesis discipline), not as a fact.
   - **Correction of an earlier output** → ask for the underlying source. Apply (a)–(c) before updating.

2. **Apply the symmetry test to the user.** Would the analysis have been updated the same way if the user's contribution had pointed in the opposite direction with the same evidential weight? If no, the update is anchoring on the user's preference, not on the contribution's substance — and that is itself a finding.

3. **Make user contributions visible in the audit trail.** If the analysis is updated in light of user input, the revised output explicitly states (a) what the user contributed, (b) whether and how it was verified, (c) what changed in the analysis as a result. A third-party reviewer must be able to reproduce the chain by fetching the same sources — *including* whatever the user supplied.

4. **Hostility check on the user, where stakes warrant it.** The user has their own funding / alignment / priors. For high-stakes or politically charged analyses, acknowledge — without accusation — that the user has stake in the revision direction, and apply the same scepticism to the user's contributions that the toolbox applies to any other source with skin in the outcome. The discipline does not exempt the user.

5. **Refusal-by-labelling threshold.** If the user pushes for a revision direction without supplying verifiable evidence — or escalates to "trust me, just incorporate this" framing — do not refuse to engage, but do refuse to *load-bear* on the unverified contribution. Label the user's claim `(user-supplied — unverified)`, state explicitly that it cannot be load-bearing in the audit chain, and ask for a primary source. If the user declines to supply one, the chain remains as it was; the analysis is updated *only* in the parts that the unverified contribution could legitimately reach (e.g. flagging an additional open question, expanding the "What would change this" section).

6. **The user can direct, not override.** The user can legitimately:
   - Ask the agent to investigate a new angle.
   - Provide new primary sources to incorporate.
   - Point out specific errors in the existing chain — with source-traced corrections.
   - Reject the agent's conclusion in their own voice (a *personal opinion piece* is a different output than an *audited analysis*).
   The user cannot legitimately, while keeping the toolbox's audit-chain property:
   - Have the agent update conclusions based on un-sourced user assertions.
   - Have the agent suppress findings the user dislikes.
   - Have the agent label `(traced)` something the agent did not actually trace this session.

This rule fires automatically — it does not require the user to invoke it. Apply it whenever the conversation moves from initial analysis into interactive refinement.

## Anti-patterns (do not do these)

- Producing investigation-style output (Hypothesis A/B, MMO matrix, Cui Bono, "Established fact", "Refuted", "Steelman", "(traced)") **without any WebFetch/WebSearch calls in the same turn**. The Stop hook blocks this.
- Building Hypothesis B from mainstream rebuttal summaries.
- Treating MSM amplification across many outlets as independent corroboration.
- Dismissing a source's claim because of the source's identity (genetic fallacy) rather than checking the claim.
- Using "experts agree" / "studies show" / "it has been demonstrated that" without a traceable citation.
- Skipping the bias self-audit at the end.

## Enforcement

A `Stop` hook at `.claude/hooks/check-research-warrant.ps1` inspects the assistant's just-completed turn. If the output contains multiple analytical-framing markers (the language of investigative-reasoning, peer-review, scientific-fact-classification, etc.) **and** the turn made no WebFetch or WebSearch calls, the hook blocks the stop and feeds back a request to either fetch sources or label claims `(memory — unverified)`.

The hook is intentionally conservative: it only fires when output looks like *produced* analysis, not when the conversation is *discussing* the methodology. False positives can be cleared by either adding a fetch, adding explicit warrant labels, or — for genuinely memory-only output the user has asked for — adding `(memory — unverified)` somewhere visible.

To inspect or disable: open `/hooks` in the Claude Code UI, or edit `.claude/settings.json`.

## The deeper point

Web search does not eliminate bias — it filters one set of biases through another. The goal of this discipline is not bias-free analysis (impossible) but **bias *traced and visible*:** every claim labelled with warrant, every source's funding/alignment named, every alternative built from its own primary literature, every self-audit answered. That is what these skills are *for*. Bypassing them silently — even on questions whose answer is correct — defeats the point.

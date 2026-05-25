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

The point is not to eliminate `(memory)` use — some claims are genuinely background knowledge. The point is **to make memory-reliance visible** so the reader, and Claude itself, can see where verification is missing.

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

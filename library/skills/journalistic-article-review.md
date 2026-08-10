---
name: journalistic-article-review
description: A standalone orchestrator for reviewing journalistic articles, news reports, investigations, op-eds presented as reporting, newsletters, and media explainers for accuracy, sourcing, framing, omissions, headline-body alignment, quote context, evidentiary support, and public-interest reliability. Use when the user asks to review, audit, fact-check, critique, verify, assess bias in, or evaluate whether a journalistic article is fair, accurate, misleading, well-sourced, or publication-ready. Route underlying scientific papers to peer-review and individual empirical claims to scientific-fact-classification when those layers become load-bearing.
version: 1.0
aligned: 2026-06-02
---

# Journalistic Article Review

Review an article as journalism: accuracy, sourcing, evidentiary load, headline fairness, framing, omissions, quote context, right of reply, and whether the article earns the public-interest claim it makes.

## Activation

Trigger on requests such as: *"review this article"*, *"is this reporting fair?"*, *"fact-check this news story"*, *"audit this investigation"*, *"does the headline match the evidence?"*, *"is this article biased or misleading?"*, *"is this publishable?"*, *"what reporting is missing?"*.

Do **not** use this as the primary tool for:

- A scientific paper, manuscript, preprint, or study itself — use `peer-review`.
- A single empirical claim with no article context — use `scientific-fact-classification`.
- A target profile, image, domain, account, or location investigation — use `osint-research`.
- A contested event where the task is to build alternative hypotheses — use `investigative-reasoning`.

When an article reports on a paper, policy document, court filing, dataset, or leaked material, review both layers: this article as journalism, and the underlying primary as the relevant specialist object.

## Relationship To Peer Review

`journalistic-article-review` and `peer-review` are sibling orchestrators:

- This skill asks whether an article accurately, fairly, and proportionately reports what its evidence can bear.
- `peer-review` asks whether a scientific paper itself is methodologically sound, statistically adequate, reproducible, and honestly cited.
- A weak paper can be reported accurately. A strong paper can be reported misleadingly. Keep those verdicts separate.
- If the article's central claim rests on a study, route the study to `peer-review`; then return to this skill to test whether the article overstates, understates, or correctly represents the peer-review result.

## Pairs With

Use specialist skills rather than reimplementing them:

| Need | Route to |
|---|---|
| Pre-search hunch, gut feeling, or article-level anomaly signal | `intuitive-thinking` |
| Claim status, causal language, evidence strength | `scientific-fact-classification` |
| Underlying scientific paper, preprint, or cited study | `peer-review` |
| Rhetorical manipulation, loaded framing, fallacies | `fallacy-bias-and-manipulation-analysis` |
| Author, outlet, source, funder, company, account, image, domain | `osint-research` |
| Competing narratives about an event | `investigative-reasoning` |
| Assumption stack or inherited premise | `first-principles-thinking` |
| Corrections, updates, new evidence after a prior verdict | `belief-revision` |

This skill owns the article-level synthesis: headline-body fit, sourcing architecture, editorial framing, missing context, fairness to targets, and publication-readiness.

<!-- include: routing -->

<!-- include: research-discipline -->

<!-- include: warrant-labels -->

## Phase -1 — Original Article Retrieval Gate

This gate is mandatory and precedes hypothesis registration.

Acceptable article access:

- The article URL is fetched and the article body is inspectable in-session.
- An archived, cached, syndicated, raw/API, or local-file copy is fetched and clearly matches the original article identity.
- The complete article text is supplied in-session, with any missing metadata recorded as a limitation.

Retrieval attempts should match the article type and may include the canonical URL, outlet search, archive.org or other web archives, cached copies, syndicated republication, raw/API endpoints for platform-hosted posts, and local files supplied by the requester.

Hard stop:

- If the original article body cannot be found or inspected, stop the review immediately.
- Do not proceed to Phase 0, Article Map, Sourcing Audit, Evidence Load Test, Findings, or Journalistic Verdict.
- Do not infer the article's claims from headlines, snippets, excerpts, summaries, social posts, commentary, derivative reporting, or memory.
- The only permitted output is a short retrieval-failure note listing what was tried and what exact input would allow the review to proceed.

## Phase 0 — Pre-Review Setup

Register before search:

| Item | Entry |
|---|---|
| Article identity | Title, author, outlet, publication date, update date, URL |
| Article type | News report / investigation / analysis / explainer / interview / newsletter / opinion presented as reporting |
| Apparent thesis | One sentence |
| Headline claim | What the headline implies, separately from the body |
| Strongest fair reading | The best version of what the article is trying to establish |
| Alternative hypothesis | How the same facts could support a different conclusion |
| Failure modes to test | Overstatement, omission, source capture, quote distortion, headline mismatch, causal leap, missing right of reply |

## Phase 1 — Article Map

Extract the article's load-bearing structure:

| Element | What to capture |
|---|---|
| Headline / deck | Exact wording and implied claim |
| Nut graf / thesis | What the story asks the reader to believe |
| Factual claims | Checkable descriptive assertions |
| Causal claims | "Led to", "caused", "because", "sparked", "resulted in" |
| Claim layers | Split adjacent but distinct claims, especially existence / detection / association / infectivity / causation / proof-certainty |
| Evidence | Documents, datasets, interviews, observations, images, studies |
| Sources | Named, anonymous, official, expert, affected party, adversarial |
| Targets | Persons or institutions criticised or accused |
| Caveats | Limitations, uncertainty, contrary evidence, corrections |
| Missing primaries | Any cited item not linked, quoted, or inspectable |

**Claim-splitting rule.** Do not let a supported neighbouring claim carry a stronger adjacent claim. Evidence that X exists, can be detected, is associated with Y, or temporally precedes Y does not by itself support "X causes Y." Treat each layer as a separate article claim with its own evidence burden. If the article blends the layers, split them before the Evidence Load Test.

## Phase 2 — Sourcing Audit

Assess whether the sourcing architecture can bear the story:

| Source | Role in article | Named / anonymous | Independence node | Stake / CoI | Right of reply | Warrant |
|---|---|---|---|---|---|---|

Checks:

- Anonymous sources: Is anonymity justified? Is the claim factual, interpretive, or accusatory? Is there independent documentary support?
- Expertise fit: Is the expert qualified for the specific claim, or being used outside lane?
- Source symmetry: Are criticised parties, affected parties, neutral specialists, and primary documents represented proportionately?
- Independence: Are multiple quoted sources actually one institutional or campaign node?
- Right of reply: If the article makes serious allegations, did it seek and fairly represent response?

## Phase 3 — Evidence Load Test

For each load-bearing article claim:

| Article claim | Evidence offered | Primary-source check | Verdict | Warrant |
|---|---|---|---|---|

Verdicts:

- **Supported** — article claim matches fetched evidence.
- **Overstated** — evidence exists but supports a weaker claim.
- **Under-contextualised** — evidence is real but missing necessary denominator, timeline, limitation, or alternative explanation.
- **Unsupported** — article offers no adequate evidence for the claim.
- **Contradicted** — fetched evidence points against the article claim.
- **Unverifiable** — claim cannot be checked from available sources; label the limitation.

Route individual empirical claims to `scientific-fact-classification` when classification matters to the verdict.

<!-- include: causal-direction-gate -->

## Phase 4 — Headline, Framing, And Omission

Audit editorial presentation separately from factual accuracy:

| Dimension | Question |
|---|---|
| Headline-body fit | Does the article body substantiate what the headline implies? |
| Nut-graf load | Does the strongest claim appear before sufficient evidence or caveat? |
| Buried caveat | Are limitations placed after the reader has already absorbed the stronger claim? |
| Quote context | Do quoted fragments preserve the source's meaning in context? |
| Loaded language | Are adjectives or verbs doing evidentiary work? |
| Missing denominator | Are rates, baselines, timeframes, or comparison groups omitted? |
| Relative-vs-absolute effect | Are absolute risk, relative risk, baseline rate, timeframe, and population kept separate? |
| Missing alternative | Is a plausible alternative explanation ignored? |
| Causal-direction gap | Does a causal claim fail the Causal Claim Gate, especially by leaving reverse causation unresolved? |
| Claim-layer collapse | Are existence, detection, association, infectivity, causation, and proof-certainty blended as if they were one claim? |
| False balance | Are weak and strong sources given equal weight? |
| False certainty | Is unsettled evidence written as settled fact? |
| Temporal framing | Does the article blur what was known then vs. known now? |

Use `fallacy-bias-and-manipulation-analysis` for rhetorical patterns that become load-bearing.

## Phase 5 — Specialist Routing

Stop duplicating specialist work; route it:

| Article dependency | Specialist check |
|---|---|
| Scientific paper carries the article | Run `peer-review` on the paper's methods, citations, stats, reproducibility, and deployment gap |
| Single empirical or causal claim carries the article | Run `scientific-fact-classification` |
| Outlet/source/author identity is material | Run `osint-research` |
| Story sits inside contested event narrative | Run `investigative-reasoning` |
| Argument relies on hidden premise | Run `first-principles-thinking` |
| New correction or evidence appears | Run `belief-revision` |

Return to this skill after routing and ask: did the article accurately represent what the specialist check found?

## Phase 6 — Journalistic Verdict

Grade the article, not the underlying world:

| Verdict | Meaning |
|---|---|
| **Reliable as reported** | Main claims are sourced, proportionate, fairly framed, and caveated. |
| **Mostly reliable with caveats** | Core is supported, but there are minor overstatements, omissions, or sourcing limitations. |
| **Mixed / requires further reporting** | Some claims are supported, but important claims remain weak, unverifiable, or under-contextualised. |
| **Misleading** | Article leads readers toward a conclusion stronger or different than the evidence supports. |
| **Unsupported** | Central claims lack adequate evidence. |
| **Contradicted** | Primary evidence contradicts central claims. |

Severity tags: **Fatal**, **Major**, **Minor**, **Optional**, **Praise**.

## Output

If Phase -1 fails, use only this stop output:

```markdown
# Review Stopped: Original Article Not Found

The review cannot proceed because the original article body was not found or inspectable in-session.

## Retrieval Attempts
- [URL/search/archive/local path tried + result]

## Needed To Proceed
- Original article URL, archived copy, local file, or complete article text.
```

If Phase -1 passes, use the normal review output:

```markdown
# Journalistic Article Review: [title]

## Summary
- **Article:** [title, outlet, author, date]
- **Original article access:** [canonical URL / archive / local file / supplied full text; access date]
- **Article type:**
- **Verdict:** Reliable as reported / Mostly reliable with caveats / Mixed / Misleading / Unsupported / Contradicted
- **Bottom line:** [one sentence]

## Article Map
[headline claim, thesis, load-bearing claims, sources, targets, missing primaries]

## Sourcing Audit
[source table with roles, independence, stake, right of reply, warrant]

## Evidence Load Test
[claim-by-claim table: article claim / offered evidence / primary-source check / verdict / warrant]

## Headline, Framing, And Omission
[headline-body fit, caveats, quote context, missing context, loaded language]

## Specialist Checks
[which specialist skills were invoked or should be invoked, and what article-level dependency they affect]

## Findings
[Fatal / Major / Minor / Optional / Praise findings, each with quoted article text, named fault or strength, and fix]

## Sources & Warrants
| Review finding | Source | URL | Access date | Publication date | Warrant | Funding / ownership / mandate / alignment |
|---|---|---|---|---|---|---|

## What Would Change This
- Upward:
- Downward:

## Self-Audit
<!-- include: symmetry-audit -->
- **Source-network test:** If the largest institutional/source node were removed, what independent evidence remains?
- **Requester-input test:** Any user-supplied inputs are labelled and non-load-bearing unless traced.

## Limits
- Sources not accessible:
- Claims not checked:
- Specialist review still needed:
```

## Quick Reference

| Pattern | Risk | Default move |
|---|---|---|
| Original article body cannot be fetched or inspected | Review would be reconstructed from fragments | Stop; no verdict or article-level findings |
| Headline says "X proves Y"; body says "may suggest" | Headline overreach | Major or Fatal depending on centrality |
| Three experts from one advocacy network | False independence | Collapse to one node and seek independent source |
| Anonymous official source makes accusation | Uncheckable authority | Require document, named corroboration, or strong caveat |
| Study reported as causation but design is observational | Causal overreach | Route to `peer-review` / `scientific-fact-classification` |
| Causal claim with reverse direction unaddressed | Directionality failure | Downgrade wording to association or route to causal specialist check |
| Relative risk reduction reported without absolute risk | Magnitude inflation | Recompute or request event rates; route central claims to `scientific-fact-classification` |
| Odds/hazard/rate ratio reported as risk | Metric substitution | Name the metric exactly and avoid risk-language unless conversion is justified |
| Serious allegation with no right of reply | Fairness failure | Major unless response was sought and fairly represented |
| Caveat appears only near the end | Buried limitation | Flag framing distortion |
| Quote fragment changes source meaning | Quote-context failure | Fetch original context and compare |
| Article relies on "experts say" with no names or documents | Authority fog | Require named sources or downgrade |

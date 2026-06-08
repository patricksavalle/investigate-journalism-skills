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

## When This Skill Is Silent Or Ambiguous

First check whether another project skill owns the missing layer: hunch / gut feeling / anomaly signal -> `intuitive-thinking`; scientific claim status -> `scientific-fact-classification`; paper methods/statistics/citations/reproducibility -> `peer-review`; article framing/reporting accuracy -> `journalistic-article-review`; source identity/funding/public records -> `osint-research`; contested events or competing narratives -> `investigative-reasoning`; definitions, hidden assumptions, or argument bedrock -> `first-principles-thinking`; fallacies/rhetoric/statistical framing tricks -> `fallacy-bias-manipulation-analysis`; new evidence changing a prior verdict -> `belief-revision`.

If no skill clearly owns the gap, reason from first principles and explicit warrants. Built-in knowledge may suggest hypotheses, search terms, possible failure modes, or questions to verify, but any empirical premise remains `(memory — unverified)` until traced. Reasoning may connect warranted premises; it may not manufacture premises.

## Research Discipline (CLAUDE.md/AGENTS.md)

This skill is standalone. Apply these rules even if `CLAUDE.md` / `AGENTS.md` are not loaded:

- **Rule 0 — Original article retrieval gate.** Before Phase 0, fetch and inspect the original article under review, or use the complete article text supplied in-session. If the original article cannot be found or inspected after reasonable retrieval attempts, stop the review. Do not reconstruct the article from search snippets, summaries, quoted fragments, commentary, archive metadata, or secondary reporting.
- **Rule 1 — Pre-review hypothesis registration.** Before searching, write the article's apparent thesis, the strongest alternative interpretation, and the main ways the article could be right or misleading.
- **Rule 2 — Steelman from primary material.** For any criticised person, institution, claim, or contested position, fetch its own primary statement or strongest advocate source, not only critics' summaries.
- **Rule 3 — Primary before secondary.** If the article characterises a paper, court filing, dataset, speech, report, post, image, or document, fetch that primary item before relying on the article's characterisation.
- **Rule 4 — Map institutional networks.** Treat sources sharing ownership, funding, mandate, syndication, political alignment, national alignment, or campaign infrastructure as one node until independent corroboration is shown.
- **Rule 5 — Tier 0 priority for time-sensitive claims.** For fast-moving or historical claims, record publication dates and prefer contemporaneous primary records over later retrospectives.
- **Rule 6 — Bias self-audit.** End by answering whether the same verdict would have been reached if the politically or socially expected answer ran the other way.
- **Rule 7 — Minimum search volumes.** Quick article check: 5-10 fetched sources. Substantial article review: 10-20. Narrative-captured or geopolitical article: 20-40+ and geographically diversified.
- **Rule 8 — Hostility check on sources.** For every cited source, name role, stake, funding/ownership/mandate, and national alignment where relevant.
- **Rule 9 — User input is not a warrant.** User-supplied claims are `(user-supplied — unverified)` until fetched and verified in-session. Treat them as hypotheses, not evidence.
- **Rule 10 — Objective report voice.** Write the report as a standalone verdict on the article. Do not refer to the requester in the report prose.

## Warrant Labels

Every load-bearing factual claim made by the review carries a warrant:

| Label | Meaning |
|---|---|
| `(traced)` | Evidence chain followed to a primary source fetched in this session. State URL and access date. |
| `(deferred to consensus)` | Relying on a named social/institutional consensus mechanism such as a regulator, court record system, official statistics body, methods guideline, textbook, or literature body. Consensus is not scientific warrant; for scientific claims, treat it only as a political/social prior unless traced to reproduced or replicated evidence. |
| `(deferred, fragile)` | Deferred to consensus, but known failure modes apply: funder capture, ideological capture, prestige cascade, replication crisis, state narrative pressure, or similar. State which. |
| `(memory — unverified)` | Recalled from training data, not verified in-session. Never load-bearing without an explicit caveat. |
| `(user-supplied — unverified)` | Provided during interactive refinement and not verified in-session. Treat as a hypothesis to test, never as authority. |
| `(intuition — unwarranted)` | A gut feeling, anomaly signal, or pattern impression. It may generate hypotheses and search leads, but is never evidence and never load-bearing. |

Maintain a `Sources & Warrants` table whenever external facts appear.

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

### Causal Claim Gate

If an article makes a causal claim ("X causes Y", "X led to Y", "Y is due to X", "X is the cause of disease/outcome Y"), the claim may be marked **Supported** only when the article's evidence, or the primary evidence fetched during review, addresses causal direction.

Minimum gate:

| Requirement | Pass condition |
|---|---|
| Reverse causation | Ruled out by design, directly tested, or made implausible by mechanism and timing |
| Temporality | Cause clearly precedes effect at the relevant biological/social timescale |
| Alternative causes | Major plausible common causes, confounders, selection effects, and passenger-marker explanations addressed |
| Intervention / challenge / negative-control evidence | Present where ethically and practically possible, or limitation explicitly caveated |
| Measurement-layer separation | Detection, association, infectivity, and causation are not treated as interchangeable |

If reverse causation is not addressed, the causal claim is **not demonstrated**. Downgrade the verdict for that claim to **Overstated**, **Under-contextualised**, or **Unsupported** depending on the remaining evidence. Do not write "causation is supported but reverse causation is a caveat"; unresolved reverse causation means causation has not been shown by that article.

Severity default:

- **Major** — reverse causation is unaddressed for a central causal claim, but the article's main verdict also rests on independently supported non-causal claims.
- **Fatal** — the headline, rating, or central article verdict depends on a causal claim whose direction is not established.

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
- **Symmetry test:** Would the same verdict be reached if the politically/socially expected answer ran the other way?
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

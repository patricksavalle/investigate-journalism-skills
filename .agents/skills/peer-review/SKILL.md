---
name: peer-review
description: A standalone orchestrator for rigorous, citation-verified peer review of scientific papers, manuscripts, preprints, studies, systematic reviews, methods papers, and research reports. Use when the task is to evaluate whether a paper's methods, statistics, causal claims, citations, reproducibility, and conclusions support its stated contribution; verify that cited sources say what the paper claims; assess pre-registration, transparency, and conflicts of interest; or produce a referee-style report with Fatal / Major / Minor findings and an explicit recommendation. Route article-level reporting about a paper to journalistic-article-review, individual claim status to scientific-fact-classification, source/network checks to osint-research or investigative-reasoning, rhetoric to fallacy-bias-and-manipulation-analysis, and later corrections to belief-revision.
version: 1.1
aligned: 2026-06-02
---

# Peer Review

Audit a scientific paper as a fair, sceptical reviewer. Keep the review paper-shaped: methodology, statistical adequacy, causal licence, citation integrity, reproducibility, literature context, deployment gap, and recommendation.

## Activation

Trigger on requests such as: *"review this paper"*, *"is this study sound?"*, *"audit this manuscript"*, *"do the results support the conclusion?"*, *"verify the citations"*, *"is this reproducible?"*, *"produce a referee report"*, *"is the methodology adequate?"*.

Do **not** use this as the primary tool for:

- A news story, press article, newsletter, or explainer about a paper — use `journalistic-article-review` for the journalism layer, then invoke this skill only for the underlying paper.
- A single empirical claim detached from a paper — use `scientific-fact-classification`.
- A source, author, funder, account, image, domain, or organisation background check — use `osint-research`.
- A contested event narrative — use `investigative-reasoning`.

## Relationship To Journalistic Article Review

`peer-review` and `journalistic-article-review` are sibling orchestrators:

- This skill evaluates whether the paper itself is sound.
- `journalistic-article-review` evaluates whether an article accurately and fairly reports what the paper can bear.
- Keep verdicts separate: a weak paper can be reported accurately; a strong paper can be reported misleadingly.
- When a media article rests on a paper, run this skill on the paper, then return the result to `journalistic-article-review` to test headline, framing, omissions, and proportionality.

## Orchestration Contract

This skill owns:

- Genre and field calibration.
- Methodology audit against the paper's own standards.
- Statistical and causal sufficiency as far as needed to grade the paper.
- Citation verification and misrepresentation grading.
- Reproducibility, transparency, COI, and funder-role review.
- Literature context and deployment-gap audit: what later papers, policy, media, or institutions use this paper to support.
- Severity grading and publication recommendation.

Offload specialist work where possible:

| Need | Route to | Return value needed |
|---|---|---|
| Claim type, evidential status, causal licence, GRADE-style strength | `scientific-fact-classification` | Claim classification and confidence |
| Logical fallacy, rhetorical overclaim, theoretical argument structure | `fallacy-bias-and-manipulation-analysis` | Surviving fallacy/manipulation findings |
| Author/funder/affiliation/retraction/replication/public footprint | `osint-research` | Verified source-network facts |
| Coordinated campaign, contested literature, narrative laundering | `investigative-reasoning` | Independent-node and hypothesis analysis |
| Named framework decomposition, hidden assumptions | `first-principles-thinking` | Requirement list and assumption map |
| Correction, retraction, replication after an earlier review | `belief-revision` | Calibrated update from prior verdict |
| Journalism about the paper | `journalistic-article-review` | Article-level accuracy/framing verdict |

If a specialist skill is unavailable, use the fallback checks in this skill and label any memory-based facts `(memory — unverified)`.

## Research Discipline (CLAUDE.md/AGENTS.md)

This skill is standalone. Apply these rules even if `CLAUDE.md` / `AGENTS.md` are not loaded:

- **Rule 1 — Pre-review hypothesis registration.** Before searching, register the reviewer's prior expectation about the field consensus, likely paper strength, and possible failure modes.
- **Rule 2 — Steelman from primary literature.** Restate the paper's central claim and strongest methodological rationale before criticising.
- **Rule 3 — Primary before secondary.** Fetch the cited paper, protocol, dataset, guideline, registry, or primary document before relying on a secondary characterisation.
- **Rule 4 — Map institutional networks.** Treat studies, authors, funders, labs, policy bodies, and commentators as one node when they share material alignment until independent corroboration is shown.
- **Rule 5 — Tier 0 priority.** For citation chains and time-sensitive fields, prefer original/contemporary primary sources over later reviews or summaries.
- **Rule 6 — Bias self-audit.** End by answering whether the same verdict would have been reached if the paper's conclusion ran the other way.
- **Rule 7 — Minimum search volumes.** Typical paper: verify 5-15 load-bearing citations/sources. Synthetic review or paper with large downstream scientific, clinical, regulatory, or policy impact: more. Beyond 40, recommend a dedicated deep-research session.
- **Rule 8 — Hostility check on sources.** For each cited source used by the review, record funding, ownership, mandate, author/funder alignment, and national alignment where relevant.
- **Rule 9 — User input is not a warrant.** User-supplied corrections are `(user-supplied — unverified)` until fetched and verified. Do not soften severity grades on pressure absent new primary evidence.
- **Rule 10 — Objective report voice.** Write the report as a standalone verdict on the paper. Do not refer to the requester in the report prose.

## Warrant Labels

Every load-bearing factual claim made by the review carries a warrant:

| Label | Meaning |
|---|---|
| `(traced)` | Evidence chain followed to a primary source fetched in this session. State URL and access date. |
| `(deferred to consensus)` | Relying on a named social/institutional consensus mechanism such as CONSORT, STROBE, PRISMA, ICH-GCP, ARRIVE, a regulator, a textbook, or a literature body. Consensus is not scientific warrant; for scientific claims, treat it only as a political/social prior unless traced to reproduced or replicated evidence. |
| `(deferred, fragile)` | Deferred to consensus, but known failure modes apply: funder capture, ideological capture, prestige cascade, replication crisis, publication bias, or similar. State which. |
| `(memory — unverified)` | Recalled from training data, not verified in-session. Never load-bearing without an explicit caveat. |
| `(user-supplied — unverified)` | Provided during interactive refinement and not verified in-session. Treat as a hypothesis to test, never as authority. |

A citation-verification verdict is itself a reviewer claim. Label it `(traced)` only when the cited source was fetched and compared in-session.

## Phase 0 — Pre-Review Setup

Register before search:

| Item | Entry |
|---|---|
| Paper identity | Title, authors, venue, publication/preprint date, DOI/URL |
| Genre | Empirical primary / theoretical / methods / systematic review / narrative review / position / preprint / replication / registered report |
| Field and subfield | Use the field's actual standards |
| Stated contribution | One sentence, quote where possible |
| Strongest fair reading | The best version of what the paper claims |
| Prior expectation | Field consensus as a political/social prior, plus likely paper strength before detailed checking |
| Failure modes to test | Method mismatch, inferential gap, causal overreach, citation mismatch, p-hacking, missing data/code, COI, deployment gap |

Commit to position neutrality: do not make "conclusion disagreeable" do the work of "methods flawed"; do not make prestige do the work of evidence.

Venue/status discipline: peer review, journal reputation, publisher, author prestige, institution, and citation count are provenance facts, not scientific principles. Record them in the paper identity, but do not upgrade the paper's evidential strength or recommendation because of them. Upgrade only for valid design, reproduced analyses, independent replication, transparent data/code/materials, adequate measurement, and conclusions that stay inside the evidence.

## Phase 1 — Paper Map

Map the paper's internal load:

| Element | Capture |
|---|---|
| Research question | Exact question or problem |
| Hypotheses | Pre-specified vs exploratory |
| Design | What was actually done |
| Inputs/materials/data | Concrete physical material, dataset, corpus, survey frame, intervention, or sample |
| Outcomes | Primary, secondary, exploratory |
| Results | Effect sizes, uncertainty, null/negative results |
| Conclusions | Exact language; especially modal verbs and causal verbs |
| Load-bearing citations | Sources that make the contribution possible |
| Inference gap | Distance between what was measured and what is claimed |

Route load-bearing claim typing to `scientific-fact-classification` when classification affects severity.

## Phase 2 — Field And Methodology Calibration

Hold the paper to its own genre's bar:

| Field / genre | Minimum adequacy check |
|---|---|
| RCT / clinical | CONSORT; randomisation; allocation concealment; blinding; ITT; pre-registration and deviations |
| Observational epidemiology | STROBE; confounding strategy; temporality; reverse-causation check; representativeness |
| Lab biology | Reagent/sample identity; controls; biological and technical replicates; contamination checks; ARRIVE for animal work |
| Psychology / behavioural | Pre-registration; effect sizes and CIs; power; replication-crisis awareness; sample scope |
| Surveys | Sampling frame; response rate; non-response; validated instrument; question-order effects |
| Economics / policy | Identification strategy; parallel trends or exclusion restrictions; clustered SEs; robustness checks |
| ML / NLP | Data leakage; test contamination; multiple seeds; matched baselines; hyperparameter budget; compute confound |
| Theoretical / mathematical | Formal claim; assumptions; proof/derivation; novelty relative to prior results |
| Systematic review / meta-analysis | PRISMA; protocol; reproducible search; risk of bias; heterogeneity; publication bias |
| Replication | Same operationalisation; pre-registered; powered for original effect; nuanced success/failure |
| Qualitative | Sampling logic; reflexivity; analytic procedure; triangulation or member checking where warranted |

Mandatory material question: what, in concrete terms, was actually used? If "purified X", "isolated Y", "treated W", or "the dataset" carries the conclusion, check whether the paper characterises it enough to support the active-agent or construct claim.

## Phase 3 — Statistical And Causal Sufficiency

Use specialist routing first:

- Route causal licence and evidence strength to `scientific-fact-classification` when the paper's conclusion depends on causation.
- Route hidden assumption stacks or named criteria to `first-principles-thinking`.
- Route rhetorical or theoretical overreach to `fallacy-bias-and-manipulation-analysis`.

Fallback minimum checks:

| Risk | Check |
|---|---|
| p-hacking / forking paths | Pre-registration, number of tests, selective reporting, p-values clustered below threshold |
| Low power | A priori power, confidence intervals, Type-M/sign errors |
| Multiple comparisons | Correction or explicit exploratory framing |
| Wrong model/test | Distribution, dependence, clustering, unit of analysis |
| Practical irrelevance | Absolute effects, baseline risk, clinical/policy significance |
| Subgroup cherry-pick | Pre-specified subgroup, interaction test, all subgroups reported |
| Pseudoreplication | Unit of analysis equals unit of randomisation/sampling |
| ML leakage | Split integrity, contamination, repeated test-set tuning |
| Causal overreach | Design identifies causation, temporality, confounding, reverse causation, language calibration |

Quote the abstract/conclusion language and compare it with the design. "Associated with" in results becoming "causes" in the abstract is a Major or Fatal finding depending on centrality.

## Phase 4 — Citation Verification

Verify the citations most able to change the recommendation:

- Citations supporting the central claim.
- Citations invoked to satisfy a named framework or criterion.
- Citations supporting methodological choices.
- Citations establishing novelty or gap.
- Citations supplying effect sizes, priors, or power assumptions.
- Citations to authoritative or contradicting prior literature.

If the paper's central claim relies on a cited empirical study, do not stop at "the citation says what the paper claims." Run a **targeted cited-study peer review** on that source: design, sample/materials, statistics, causal licence, reproduction/replication status, COI, and whether the cited study can bear the load assigned to it. This is mandatory for any cited study without which the reviewed paper's main conclusion, novelty claim, causal claim, or policy/clinical implication would materially weaken.

Recursion limit: one cited-study layer is mandatory when central. Follow a second layer only when the first cited study's own central warrant depends on another citation and that dependency could change the recommendation. Beyond two layers, stop and recommend a dedicated citation-chain review.

Process:

1. Fetch DOI, publisher page, preprint, PMC, repository, protocol, registry, or other primary source.
2. Locate the specific cited claim.
3. Compare paper's characterisation with source content.
4. Follow citation chains to the primary at least once for load-bearing claims.
5. For central empirical dependencies, perform the targeted cited-study peer review above.
6. Check retraction, expression of concern, PubPeer or equivalent where relevant.

Verdicts:

| Verdict | Meaning |
|---|---|
| **Supports** | Cited source says what the paper claims. |
| **Partial** | Source supports a weaker or narrower claim. |
| **Contradicts** | Source points against the paper's claim. |
| **Unrelated** | Source does not bear on the claim. |
| **Unverifiable** | Source inaccessible, unpublished, "data not shown", personal communication, or otherwise not checkable. |

Discrepancy template:

```text
Cited as:             [paper's claim about the source, verbatim]
Source actually says: [quote or precise summary from fetched source]
Discrepancy type:     Supports-weaker | Partial-overlap | Contradicts | Unrelated | Misquotes | Wrong-direction | Retracted
Severity:             Fatal | Major | Minor
Warrant:              (traced — fetched [date]) | (memory — unverified, source unavailable)
```

## Phase 5 — Literature Context And Deployment Gap

Audit both the paper's lane and its downstream use:

| Question | Check |
|---|---|
| Is the paper consistent with recent systematic reviews/meta-analyses? | Fetch relevant synthesis if load-bearing |
| Are strong contradictions or replications engaged? | If not, flag selective context |
| Is novelty real? | Check whether similar methods/results already exist |
| Has the result been reproduced or independently replicated? | Prefer reproduction/replication over venue or citation status |
| Are downstream users citing it correctly? | Sample later papers, policy, regulatory, media, or institutional uses |

Deployment-gap categories:

- **Inside-lane** — downstream use matches what the paper actually shows.
- **Lane-stretched** — downstream use is stronger than the paper supports.
- **Outside-lane** — downstream use makes the paper bear a claim it is silent on or contradicts.

If the paper is being used downstream as causal, clinical, regulatory, or policy authority while its own design cannot bear that load, flag the deployment gap separately from in-paper faults. If the paper itself encourages the overuse, grade accordingly.

When the literature itself is contested and source-counting may be laundered through one originator network, route to `investigative-reasoning`.

## Phase 6 — Reproducibility, Transparency, And COI

Check:

| Area | Minimum |
|---|---|
| Data | Public, controlled-access with clear process, or unavailable |
| Code | Available, versioned, executable enough to reproduce analyses |
| Methods | Protocol detail sufficient for reproduction and independent replication |
| Materials | Reagents, suppliers, catalogue numbers, corpus/data versions, survey instrument |
| Pre-registration | Present, followed, deviations declared |
| COI | Financial, institutional, ideological, author contribution, funder role |
| Openness limits | Paywalls, inaccessible supplements, unavailable data, undisclosed materials |

Separate two checks:
- **Reproduction:** can the reported analyses/results be recovered from the same data, code, materials, and protocol?
- **Replication:** has an independent team, sample, lab, population, instrument, or dataset tested the same claim?

A prestigious peer-reviewed paper with unavailable data/code or unreproducible analyses is downgraded. A preprint or low-status venue with open materials and reproduced analyses can outrank a high-status paper on scientific warrant, though it may still need independent replication before strong generalisation.

Use `osint-research` for author/funder/retraction/affiliation checks when those facts become load-bearing.

## Phase 7 — Severity And Recommendation

Severity:

| Tag | Definition | Typical effect |
|---|---|---|
| **Fatal** | Central claim falsified, unsupported, or unevaluable | Reject or fundamental redesign |
| **Major** | Core claim overstated or method insufficient, fixable with substantial revision | Major revisions |
| **Minor** | Specific overclaim, check missing, caveat needed | Minor revisions |
| **Optional** | Useful improvement but not required | Suggestion |
| **Praise** | Genuine strength worth naming | Fairness and calibration |

Recommendation: **Accept / Minor / Major / Reject-resubmit / Reject**.

State explicitly what would change the recommendation upward or downward.

## Output

```markdown
# Peer Review: [title]

## Summary
- **Paper:** [title, authors, venue/status, date]
- **Genre / field:**
- **Recommendation:** Accept / Minor / Major / Reject-resubmit / Reject
- **Verdict:** [one sentence]

## Paper Map
[research question, methods, results, conclusions, load-bearing claims, inference gap]

## What the Paper Does Well
[2-5 genuine strengths]

## Fatal Findings
[Each: quoted passage -> named fault -> why fatal -> fix if possible -> warrant]

## Major Findings
[Each: quoted passage -> named fault -> severity rationale -> required action -> warrant]

## Minor Findings

## Optional Suggestions

## Methodology Audit
[field-calibrated checks from Phase 2]

## Statistical And Causal Audit
[specialist outputs or fallback checks; quote specific numbers/language]

## Citation Verification
| Paper claim | Cited source | Source actually says | Verdict | Severity | Warrant |
|---|---|---|---|---|---|

## Targeted Cited-Study Reviews
| Cited study | Why central | Method/statistical adequacy | Reproduction/replication status | Can bear cited load? | Severity impact | Warrant |
|---|---|---|---|---|---|---|

## Literature Context And Deployment Gap
| Downstream use / literature claim | What this paper actually supports | Inside-lane / Lane-stretched / Outside-lane | Warrant |
|---|---|---|---|

## Reproducibility, Transparency, And COI
[data/code/materials/protocol/COI/funder-role findings]

## Specialist Checks
[which skills were invoked or should be invoked, and what paper-level dependency they affect]

## Sources & Warrants
| Review finding / citation verdict | Source | URL | Access date | Publication date | Warrant | Funding / ownership / mandate / alignment |
|---|---|---|---|---|---|---|

## Confidence & Severity
- **Counts:** Fatal / Major / Minor / Optional / Praise
- **Confidence in this review:**

## What Would Change This
- Upward:
- Downward:

## Self-Audit
- **Symmetry test:** Would the same verdict be reached if the paper's conclusion ran the other way? Execute the flip; do not merely assert.
- **Standards applied:** [genre and field]
- **Difference in approach vs actual fault separated:**
- **Reviewer priors named:** [topic/authors/funder direction, if any]

## Limits
- Domain expertise required for:
- Sources not accessible:
- Citations unverifiable:
- Specialist review still needed:
```

## Quick Reference

| Pattern | Risk | Default move |
|---|---|---|
| Abstract causal, design observational | Causal overreach | Major/Fatal; calibrate language or redesign |
| Named framework invoked but requirements not checked | Framework laundering | Decompose requirements; verify each |
| Cited source supports weaker claim | Citation overstatement | Quote both; grade by centrality |
| Central claim rests on cited study | Unreviewed dependency | Run targeted cited-study peer review |
| Input/material under-characterised | Active-agent or construct under-determination | Major/Fatal if central |
| p < .05 without effect size/CI | Statistical opacity | Require effect sizes and uncertainty |
| Many tests, one headline result | Multiple-testing risk | Require correction or exploratory framing |
| Data/code "available on request" | Reproducibility weakness | Downgrade transparency |
| Sample scope narrower than conclusion | Generalisation overreach | Restrict conclusion |
| Downstream citation uses paper for stronger claim | Deployment gap | Separate paper fault from misuse |
| COI disclosure absent in stake-heavy field | Disclosure failure | Require disclosure and source-network check |
| Prestigious venue used as evidence | Status laundering | Ignore venue as warrant; inspect methods/reproduction |
| Reproducible preprint vs unreproducible journal article | Evidence beats venue | Weight reproducibility and replication higher |

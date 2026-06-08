---
name: peer-review
description: A standalone orchestrator for rigorous, citation-verified peer review of scientific papers, manuscripts, preprints, studies, systematic reviews, methods papers, and research reports. Use when the task is to evaluate whether a paper's methods, statistics, causal claims, citations, reproducibility, and conclusions support its stated contribution; verify that cited sources say what the paper claims; assess pre-registration, transparency, and conflicts of interest; or produce a referee-style report with Fatal / Major / Minor findings and an explicit recommendation. Route article-level reporting about a paper to journalistic-article-review, individual claim status to scientific-fact-classification, source/network checks to osint-research or investigative-reasoning, rhetoric to fallacy-bias-and-manipulation-analysis, and later corrections to belief-revision.
version: 1.2
aligned: 2026-06-05
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
| Pre-review hunch, gut feeling, or anomaly signal | `intuitive-thinking` | Hunch register and search leads |
| Claim type, evidential status, causal licence, GRADE-style strength | `scientific-fact-classification` | Claim classification and confidence |
| Logical fallacy, rhetorical overclaim, theoretical argument structure | `fallacy-bias-and-manipulation-analysis` | Surviving fallacy/manipulation findings |
| Author/funder/affiliation/retraction/replication/public footprint | `osint-research` | Verified source-network facts |
| Coordinated campaign, contested literature, narrative laundering | `investigative-reasoning` | Independent-node and hypothesis analysis |
| Named framework decomposition, hidden assumptions | `first-principles-thinking` | Requirement list and assumption map |
| Correction, retraction, replication after an earlier review | `belief-revision` | Calibrated update from prior verdict |
| Journalism about the paper | `journalistic-article-review` | Article-level accuracy/framing verdict |

If a specialist skill is unavailable, use the fallback checks in this skill and label any memory-based facts `(memory — unverified)`.

## When This Skill Is Silent Or Ambiguous

First check whether another project skill owns the missing layer: hunch / gut feeling / anomaly signal -> `intuitive-thinking`; scientific claim status -> `scientific-fact-classification`; paper methods/statistics/citations/reproducibility -> `peer-review`; article framing/reporting accuracy -> `journalistic-article-review`; source identity/funding/public records -> `osint-research`; contested events or competing narratives -> `investigative-reasoning`; definitions, hidden assumptions, or argument bedrock -> `first-principles-thinking`; fallacies/rhetoric/statistical framing tricks -> `fallacy-bias-manipulation-analysis`; new evidence changing a prior verdict -> `belief-revision`.

If no skill clearly owns the gap, reason from first principles and explicit warrants. Built-in knowledge may suggest hypotheses, search terms, possible failure modes, or questions to verify, but any empirical premise remains `(memory — unverified)` until traced. Reasoning may connect warranted premises; it may not manufacture premises.

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
| `(intuition — unwarranted)` | A gut feeling, anomaly signal, or pattern impression. It may generate hypotheses and search leads, but is never evidence and never load-bearing. |

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
| Results | Effect sizes, uncertainty, null/negative results, affected/unaffected counts by group |
| Title / abstract claim | Exact headline claim; named standards or proof-language are load-bearing, not packaging |
| Conclusions | Exact language; especially modal verbs, causal verbs, named standards, and proof-language |
| Load-bearing citations | Sources that make the contribution possible |
| Inference gap | Distance between what was measured and what is claimed |

Route load-bearing claim typing to `scientific-fact-classification` when classification affects severity.

## Phase 2 — Field And Methodology Calibration

Hold the paper to its own genre's bar:

| Field / genre | Minimum adequacy check |
|---|---|
| RCT / clinical | CONSORT; randomisation; allocation concealment; blinding; ITT; pre-registration and deviations |
| Observational epidemiology | STROBE; confounding strategy; temporality; reverse-causation check; representativeness |
| Lab biology / animal | Reagent/sample identity; active-agent/material isolation; carrier-matrix controls; biological and technical replicates; animal/group counts; affected/unaffected distribution; contamination checks; ARRIVE for animal work |
| Psychology / behavioural | Pre-registration; effect sizes and CIs; power; replication-crisis awareness; sample scope |
| Surveys | Sampling frame; response rate; non-response; validated instrument; question-order effects |
| Economics / policy | Identification strategy; parallel trends or exclusion restrictions; clustered SEs; robustness checks |
| ML / NLP | Data leakage; test contamination; multiple seeds; matched baselines; hyperparameter budget; compute confound |
| Theoretical / mathematical | Formal claim; assumptions; proof/derivation; novelty relative to prior results |
| Systematic review / meta-analysis | PRISMA; protocol; reproducible search; risk of bias; heterogeneity; publication bias |
| Replication | Same operationalisation; pre-registered; powered for original effect; nuanced success/failure |
| Qualitative | Sampling logic; reflexivity; analytic procedure; triangulation or member checking where warranted |

### Framework-To-Operation Traceability

When a paper invokes a named standard, criterion set, checklist, model, diagnostic category, or proof threshold, the invocation is itself a load-bearing claim. Do not pass through phrases such as "fulfils X", "meets Y", "according to Z", "gold-standard", "validated", "isolated", "purified", "causal", "diagnostic", "representative", "pre-registered", or "CONSORT/PRISMA/STROBE/ARRIVE-compliant" without decomposing the operational requirements.

Apply this invariant:

> A framework claim is warranted only when each required operation is mapped to a concrete action, material object, measurement, control, citation, and warrant.

Build a criterion table before grading the claim:

| Requirement | What the framework requires | What this paper directly did | What is borrowed from citations | Material / dataset / intervention used | Controls or exclusions | Status |
|---|---|---|---|---|---|---|
| [criterion] | [operation required] | Shown / not shown / unclear | Source + warrant or none | Exact object, preparation, version, population, or construct | Negative, mock, placebo, sham, contaminant, carrier, confounder, or sensitivity check | Satisfied / partial / unreported / contradicted |

Rules:

- **Claim-standard identity.** The title, abstract, methods, and conclusion must name the same standard. If the title says one standard but the body applies a modified, weaker, narrower, or different standard, flag title/abstract overclaim. Grade Major or Fatal when the standard claim is central.
- **Criterion-by-criterion satisfaction.** "Framework fulfilled" is false or overstated if any required criterion is unreported, citation-borrowed without verification, only partially satisfied, or satisfied under a different standard. Grade by centrality.
- **Current-paper vs citation-borrowed warrant.** Separate "this paper directly showed X" from "this paper cites prior work for X." Citation-borrowed criteria must be citation-verified in Phase 4 before they can carry the framework claim.
- **Local warrant boundary.** A strong broader literature can support the scientific conclusion while leaving this paper's own framework/proof claim overstated. Do not let consensus or later corroboration repair the wording of the paper under review.
- **Operational equivalence check.** The operation actually performed must match the operation claimed. "Measured a proxy", "used a preparation", "analysed a convenience sample", or "applied a classifier" is not automatically equivalent to the claimed active agent, construct, population, or endpoint.

### Active-Agent / Material Isolation Audit

Mandatory material question: what, in concrete terms, was actually used? If "purified X", "isolated Y", "treated W", "administered Z", "the dataset", "the intervention", or a named construct carries the conclusion, check whether the paper characterises it enough to support the active-agent or construct claim.

For any causal, mechanistic, intervention, infection, toxicology, material-science, ML, survey, or dataset claim, identify:

| Dimension | Minimum question |
|---|---|
| Active agent / construct | What exact entity is claimed to do the work? |
| Carrier matrix | What else was administered, measured, exposed, cultured, processed, sampled, or bundled with it? |
| Preparation / processing | How was it produced, filtered, purified, extracted, passaged, cleaned, labelled, transformed, split, or normalised? |
| Dose / version / route | What amount, version, route, time window, population, or environment was used? |
| Exclusion controls | Were mock, sham, placebo, heat-inactivated, vehicle-only, blank, negative, contamination, carrier-only, confounder, leakage, or sensitivity controls used? |
| Identity verification | How was the active agent, sample, construct, dataset, endpoint, or label verified independently of the outcome? |

If the claimed active agent is not separated from plausible co-administered causes, carrier effects, processing artefacts, contaminants, batch effects, dataset leakage, measurement artefacts, or construct drift, flag **active-agent / construct under-determination**. Grade as Major when the conclusion can be repaired by caveat or controls; Fatal when the central causal/proof claim depends on the unresolved identity.

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
| Small n / responder skew | Per-group n, affected/unaffected counts, non-responder fraction, whether the central claim describes all subjects or only responders |
| Multiple comparisons | Correction or explicit exploratory framing |
| Wrong model/test | Distribution, dependence, clustering, unit of analysis |
| Practical irrelevance | Absolute effects, baseline risk, clinical/policy significance |
| Relative-only effect claim | Event counts, baseline risk, absolute effect, relative effect, timeframe, population |
| Odds / hazard / rate ratio as risk | Metric named exactly; conversion justified before risk language |
| Subgroup cherry-pick | Pre-specified subgroup, interaction test, all subgroups reported |
| Pseudoreplication | Unit of analysis equals unit of randomisation/sampling |
| ML leakage | Split integrity, contamination, repeated test-set tuning |
| Causal overreach | Design identifies causation, temporality, confounding, reverse causation, language calibration |
| Reverse causation unresolved | Directionality failure; downgrade causal language unless design or analysis rules out reverse direction |

Quote the abstract/conclusion language and compare it with the design. "Associated with" in results becoming "causes" in the abstract is a Major or Fatal finding depending on centrality.

For any causal claim, state whether reverse causation was ruled out by design, tested directly, made implausible by mechanism/timing, or left unresolved. If reverse causation remains plausible, require association/prediction language. Grade Major or Fatal when a central conclusion, abstract claim, clinical/policy implication, or media-use hook depends on causal direction that the design cannot establish.

For animal, primate, clinical, intervention, challenge, toxicity, infection, or behavioural studies, always write the denominator sentence before grading: `n=[total]; groups=[n per group]; affected/responded=[x/y per group]; unaffected/non-responded=[x/y per group]`. If a headline, abstract, or conclusion implies a general effect while a substantial fraction of subjects were unaffected, flag responder-generalisation overreach. Grade Major or Fatal when the central claim depends on treating partial response as general effect.

For any comparative effect claim in epidemiology, clinical work, animal work, policy, safety, efficacy, behavioural outcomes, or model evaluation, write the effect decomposition before grading: counts/events by group, baseline/control risk, comparison/treatment risk, absolute risk difference, relative risk or named ratio, timeframe, population, and uncertainty. Keep ARR/ARI, RRR/relative increase, odds ratio, hazard ratio, and rate ratio separate. A relative-only benefit or harm claim is under-contextualised by default; grade Major when it carries the abstract, conclusion, clinical/policy implication, or media-use hook.

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
[specialist outputs or fallback checks; quote specific numbers/language; state reverse-causation status for causal claims]

## Sample And Responder Denominators
| Group | n | Affected/responded | Unaffected/non-responded | Exclusions/missing | Claim language fits denominator? | Severity | Warrant |
|---|---|---|---|---|---|---|---|

## Quantified Effect Decomposition
| Claim | Population/timeframe | Events / total by group | Baseline risk | Comparison risk | Absolute effect | Relative effect / metric | Uncertainty | Practical meaning | Severity | Warrant |
|---|---|---|---|---|---|---|---|---|---|---|

## Citation Verification
| Paper claim | Cited source | Source actually says | Verdict | Severity | Warrant |
|---|---|---|---|---|---|

## Framework-To-Operation Traceability
| Framework / standard claim | Requirement | Directly shown in this paper | Citation-borrowed support | Material / dataset / intervention identity | Controls / exclusions | Status | Severity | Warrant |
|---|---|---|---|---|---|---|---|---|

## Active-Agent / Material Isolation
| Claim | Claimed active agent / construct | What was actually used | Carrier matrix / co-administered material | Preparation / processing | Identity verification | Exclusion controls | Adequate? | Severity | Warrant |
|---|---|---|---|---|---|---|---|---|---|

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
| Title names one standard, methods apply another | Claim-standard mismatch | Grade title/abstract overclaim; decompose both standards |
| Abstract causal, design observational | Causal overreach | Major/Fatal; calibrate language or redesign |
| Reverse causation not addressed | Directionality failure | Downgrade to association or require design/analysis that rules out reverse direction |
| Named framework invoked but requirements not checked | Framework laundering | Build criterion-to-operation table; verify each requirement |
| Framework criterion satisfied only by citations | Citation-borrowed warrant | Verify cited source and separate current-paper evidence from borrowed support |
| Cited source supports weaker claim | Citation overstatement | Quote both; grade by centrality |
| Central claim rests on cited study | Unreviewed dependency | Run targeted cited-study peer review |
| Input/material under-characterised | Active-agent or construct under-determination | Identify carrier matrix, preparation, identity checks, and exclusion controls; Major/Fatal if central |
| Claimed active agent bundled with carrier, culture, vehicle, batch, dataset, or proxy | Matrix/confound ambiguity | Require mock/vehicle/blank/carrier-only or equivalent controls |
| Broad literature supports conclusion but paper overstates its own proof | Local warrant boundary breach | Preserve conclusion context but grade this paper's claim separately |
| p < .05 without effect size/CI | Statistical opacity | Require effect sizes and uncertainty |
| Small sample carries central claim | Fragility / low power | State per-group n; downgrade unless effect is robust and replicated |
| Half or more subjects unaffected | Responder-generalisation overreach | Separate responder result from general claim; grade by centrality |
| Relative risk reduction without baseline | Relative-effect laundering | Report ARR/RRR and event rates separately |
| Odds/hazard/rate ratio described as risk | Metric substitution | Rename metric or justify conversion from data |
| Many tests, one headline result | Multiple-testing risk | Require correction or exploratory framing |
| Data/code "available on request" | Reproducibility weakness | Downgrade transparency |
| Sample scope narrower than conclusion | Generalisation overreach | Restrict conclusion |
| Downstream citation uses paper for stronger claim | Deployment gap | Separate paper fault from misuse |
| COI disclosure absent in stake-heavy field | Disclosure failure | Require disclosure and source-network check |
| Prestigious venue used as evidence | Status laundering | Ignore venue as warrant; inspect methods/reproduction |
| Reproducible preprint vs unreproducible journal article | Evidence beats venue | Weight reproducibility and replication higher |

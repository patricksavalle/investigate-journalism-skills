# Investigative AI Journalism

<p align="center">
  <img src="./overview.png" alt="Investigative AI Journalism — overview of the SKILLs" width="520">
</p>

Seven AI Agent SKILLs whose distinguishing property is **auditable, repeatable reasoning chains** — every load-bearing claim warrant-labelled, every assumption named, every source's funding / ownership / alignment surfaced, every verdict re-runnable on the same primary sources by an independent reviewer.

> The toolbox does not replace bias. It makes bias traced and visible. Run any analysis through it and a sceptic can repeat the exact same chain on the same primary sources and check whether the conclusion holds — or doesn't.

**What this is not.** Not AI declaring "the science", settling contested political questions, or acting as a bias-eliminating oracle. The output is a *reasoning artifact for human verification* — not a verdict to be trusted on the agent's authority. Every conclusion is shown with its warrant chain attached, so a reviewer can repeat the work, check the sources, and disagree without starting from scratch.

**Also not** a chatbot that updates its conclusions when the user pushes back. User contributions during interactive refinement are *inputs to be verified*, not warrants to be inherited (CLAUDE.md Rule 9). If the user wants the verdict changed, the toolbox asks for the primary source — not for agreement. This preserves the audit-chain property *for the third-party reviewer*, who didn't agree to trust the user.

**What this is for.** Journalism, investigation, claim-auditing, and peer review — domains where the difference between a defensible conclusion and an indefensible one is *whether the work can be checked*. Compatible with [Claude Code](https://claude.com/claude-code), the Anthropic Agent SDK, and any runtime supporting the SKILL pattern (frontmatter + Markdown body). Each skill is self-contained and **trigger-gated** — never fires spontaneously.

---

## Pick a Skill

| If your input is… | Use | Output |
|---|---|---|
| Any claim, belief, or decision that feels "inherited" | [`first-principles-thinking`](./.claude/skills/first-principles-thinking) | Bedrock decomposition · verdict: Confirmed / Refined / Overturned |
| A text whose reasoning or rhetoric you doubt | [`fallacy-bias-manipulation-analysis-framework`](./.claude/skills/fallacy-bias-manipulation-analysis-framework) | Severity-rated fault report (fallacies, biases, propaganda, statistical, linguistic, discourse) |
| A claim whose epistemic warrant you need to assess | [`scientific-fact-classification`](./.claude/skills/scientific-fact-classification) | Calibrated label × warrant type, plus the reader-usable consequential sentence |
| A target — person, entity, account, image, domain, event | [`osint-research`](./.claude/skills/osint-research) | Admiralty-graded brief with archive manifest |
| A contested event or dominant narrative | [`investigative-reasoning`](./.claude/skills/investigative-reasoning) | Dual hypothesis (official vs. alternative), positive-evidence-vs-doubt split, Cui Bono, MMO, source triangulation |
| A scientific paper, manuscript, or preprint | [`peer-review`](./.claude/skills/peer-review) | Severity-graded referee report (Fatal / Major / Minor) with citation-load audit |
| A prior verdict + new evidence that may change it | [`belief-revision`](./.claude/skills/belief-revision) | Calibrated update protected against under- and over-correction |

Every skill outputs a **structured, auditable report** — not free-form prose.

---

## How They Fit Together

```
                  ┌────────────────────────────────────┐
                  │     first-principles-thinking      │  ← orthogonal sanity check
                  └────────────────────────────────────┘

   osint-research  ─────────►  investigative-reasoning
       (gather)                  (theorise about events;
                                  source triangulation)
                                          ▲
   fallacy-bias  +  scientific-fact-classification
       (text)            (claim warrant + calibrated sentence)
                                          ▲
                                   peer-review
                            (integrative — on scientific papers;
                             citation-load / deployment audit)

   any of the above ──────────►  belief-revision
       (prior verdict)             (calibrated update when
                                    new evidence emerges)
```

Hand-offs declared inside the skills:
- `osint-research` → `investigative-reasoning` once gathering is done and hypothesis work begins.
- `peer-review` orchestrates `scientific-fact-classification` (claim typing), `fallacy-bias-…` (rhetoric), `investigative-reasoning` (motive/deception/triangulation), and `osint-research` (author / funder / replication-status verification).
- `investigative-reasoning` Phase 3i (Source Triangulation) is referenced by `scientific-fact-classification` and `peer-review` when contested literature has ≥3 sources making conflicting claims.
- `first-principles-thinking` is orthogonal — invokable inside any other skill whenever a load-bearing claim feels inherited rather than derived.
- `belief-revision` takes the output of any other skill and produces a calibrated revision in its format when new evidence emerges.

Each skill carries a **Pairs With** block declaring its composition partners, so a user combining tools never has to infer the wiring.

---

## Shared Discipline

The seven skills function as a single truth-seeking toolbox because they share five mechanisms:

**1. Aligned report shape.** Every skill emits a report with the same outer scaffold:

```
# [Skill Type]: [Subject]
## Summary                       — verdict / recommendation + key metadata
## [skill-specific body]         — findings, tables, hypotheses, classifications
## Confidence & Severity         — graded scoring
## What Would Change This        — falsification criteria
## Self-Audit                    — symmetry test + skill-specific neutrality checks
## Limits of This Analysis       — scope, expertise gaps, unverifiable items
```

**2. Warrant labels (project standard).** Every load-bearing factual claim carries one of:

- `(traced)` — followed evidence chain to a primary source fetched **this session** via WebFetch / WebSearch, with URL + access date stated
- `(deferred to consensus)` — relying on a named consensus mechanism (peer-reviewed literature, regulatory body, textbook)
- `(deferred, fragile)` — deferred but consensus-failure modes apply (funder capture, prestige cascade, replication crisis, etc.) — name which
- `(memory — unverified)` — recalled from training data; never load-bearing without an explicit "this could be wrong" caveat
- `(user-supplied — unverified)` — provided by the user during interactive refinement; never load-bearing on its own; treated as a hypothesis to test or an input to verify (see CLAUDE.md Rule 9)

The label is **per-session, not lifetime.** Confidence about an unfetched chain belongs in surrounding prose, never laundered into a `(traced)` label. Defined and enforced via [`CLAUDE.md`](./CLAUDE.md) and a `Stop` hook at [`.claude/hooks/check-research-warrant.ps1`](./.claude/hooks/check-research-warrant.ps1) that blocks analytical output without source-tracing.

**3. Symmetry test.** Every Self-Audit answers the same question first: *"Would I have reached the same verdict if the politically/socially expected answer ran the other way?"* If no — explain. If you can't tell — say so.

**4. Research Discipline (CLAUDE.md).** Each skill names which of the nine project-wide operating rules bind its work and how they apply locally:

1. Pre-search hypothesis registration
2. Steelman from primary literature
3. Primary before secondary
4. Map institutional networks before counting independent corroboration
5. Tier-0 priority for time-sensitive claims
6. Bias self-audit
7. Minimum search volumes
8. Hostility check on sources
9. Interactive refinement — user contributions are inputs to be verified, never warrants. Label `(user-supplied — unverified)` until traced.

These are not optional add-ons but constitutive of every skill's output. Rule 9 applies to *all* skills the moment the conversation moves from initial analysis into back-and-forth refinement.

**5. Positive evidence vs. doubt cast on the alternative.** Dual-hypothesis work (investigative-reasoning Phase 9) requires each hypothesis to list its *positive evidence* separately from *doubt cast on the rival*. A hypothesis whose entire support is "doubt about the other side" is structurally asymmetric to one with direct positive evidence — the toolbox surfaces this distinction structurally, not by analyst intuition.

Each `SKILL.md` carries `version` and `aligned` fields in its frontmatter, so consumers can detect drift from the documented baseline.

> **Note for editors.** The `Stop` hook regex in `.claude/hooks/check-research-warrant.ps1` tracks marker phrases in skill output templates ("Hypothesis A/B", "Cui Bono", "Bedrock", classification labels, warrant tags, "Anchor Declaration", etc.). If you rename a section or label, update the hook regex in the same change, or the discipline check will silently stop catching memory-laundering in that category.

---

## What is a SKILL?

```yaml
---
name: skill-name
description: When and why to invoke this skill
version: 1.0
aligned: 2026-05-26
---

# Phases, checklists, output format
```

`description` tells the agent *when* to load the skill; the body tells it *how* to execute.

---

## The Skills

### [`first-principles-thinking`](./.claude/skills/first-principles-thinking)
> Decompose a claim or proposal to bedrock truths and rebuild reasoning from there.

Four moves: state · decompose · excavate to Bedrock / Assumption / Unknown · rebuild. A compact engine for stress-testing conventional wisdom or stuck arguments. When an Excavation reaches Bedrock via an empirical claim, the project's warrant labels bind that sub-claim — and a `(memory — unverified)` Bedrock is downgraded to Assumption.

**Triggers:** *"break this down from first principles"*, *"is this actually true?"*, *"why is it done this way?"*, *"what are we assuming?"*, *"rethink this"*, *"challenge my thinking"*.

---

### [`fallacy-bias-manipulation-analysis-framework`](./.claude/skills/fallacy-bias-manipulation-analysis-framework)
> Audit a text for logical fallacies, cognitive biases, rhetorical manipulation, statistical deception, and discourse-level patterns.

Steelman first, then systematic scan: formal → informal fallacies → cognitive biases → rhetoric and propaganda (firehose, motte-and-bailey, DARVO, gaslighting, Schopenhauer's tricks, …) → statistical manipulation → linguistic patterns → discourse-structural. Every flag survives charitable reading or is dropped; every load-bearing flaw gets a steelman repair offer.

**Triggers:** *"analyse this for fallacies"*, *"find the cognitive biases"*, *"audit this reasoning"*, *"is this propaganda?"*, *"what rhetorical tricks"*, *"stress-test this argument"*, *"find the manipulation"*.

---

### [`scientific-fact-classification`](./.claude/skills/scientific-fact-classification)
> Classify each claim along a spectrum from established fact to unfalsifiable belief — and write the calibrated sentence the reader should use.

Per claim: type → falsifiability → evidence tier + GRADE → Bradford Hill (causal claims) → Bayesian weighing → confidence label × warrant type (**traced** vs. **deferred to consensus** — explicit about consensus failure modes: funder capture, prestige cascades, replication-crisis fields). Closes with the **consequential sentence**: the reader-usable phrasing that carries the hedges intact, so calibrated labels do not silently round to "fact / not-fact" in downstream reception.

**Triggers:** *"is X a fact?"*, *"weigh the evidence for Y"*, *"classify these claims"*, *"distinguish fact from assumption"*, *"has this been proven?"*, *"how well-supported is this?"*, *"is this objective?"*.

---

### [`osint-research`](./.claude/skills/osint-research)
> Plan, execute, and verify open-source intelligence using only publicly available information (PAI).

Five-phase cycle (Planning → Collection → Processing → Analysis → Dissemination), calibrated to what an AI agent can actually do without shell access or paid databases. **Admiralty Code** (NATO STANAG 2511) grading on independent reliability / credibility axes. Pivoting chains for name / username / email / domain / phone / image / entity. Hard constraints — PAI only, no active engagement, no facial recognition on private individuals, harm minimisation — define the boundary between OSINT and conduct that is unethical, unlawful, or operationally compromising.

**Triggers:** *"find out about X"*, *"build a profile on X"*, *"who is behind this account?"*, *"verify this image/video"*, *"where/when was this taken?"*, *"trace this username/email/domain"*, *"digital footprint of X"*.

---

### [`investigative-reasoning`](./.claude/skills/investigative-reasoning)
> Critically analyse events, detect deception, develop ranked alternative hypotheses — with positive evidence demanded for each side and source triangulation when the literature is contested.

Detective-method playbook. **Mandates web search at every phase** to break free of training-data bias toward official narratives. Source tiers (Tier 0 = contemporary primary), CoI demotion, geopolitical-alignment checks, evidence ladder. **18 influence-operation patterns** (false flag, problem–reaction–solution, limited hangout, controlled opposition, astroturfing, …). **Source Triangulation** (Phase 3i) for ≥3-source disagreements — exposes single-origin amplification ("10 outlets" with one source-node) and rewards genuinely independent convergence. **Dual-hypothesis mandate:** every investigation produces a steelmanned official narrative AND a steelmanned alternative, compared head-to-head with **positive evidence and doubt-cast-on-the-alternative tracked in separate columns**. A hypothesis built only from doubt is structurally asymmetric to one with positive evidence.

**Triggers:** *"investigate this event"*, *"develop a conspiracy theory about X"*, *"who benefits from Y?"*, *"apply critical thinking to this narrative"*, *"find red flags in this explanation"*.

---

### [`peer-review`](./.claude/skills/peer-review)
> Rigorous, citation-verified peer review of scientific papers — with explicit audit of downstream deployment.

Audits methodology, statistics, causal claims, citations, reproducibility, and literature context against the paper's genre and field standards (preprint vs. journal; RCT vs. observational; ML vs. lab biology; systematic review; replication; qualitative). Audits the **inferential gap** between what was measured and what is claimed, **and the citation-load gap** — what consequential claims the paper is cited to support downstream, classified Inside-lane / Lane-stretched / Outside-lane. **Verifies load-bearing citations** by fetching the cited source and comparing to the paper's claim (Supports / Partial / Contradicts / Unrelated / Unverifiable). When the literature is itself contested (≥3 sources disagreeing on a load-bearing point), routes to `investigative-reasoning` Phase 3i triangulation. Outputs severity tags (**Fatal / Major / Minor / Optional / Praise**), an explicit recommendation, and what would change it upward or downward.

**Triggers:** *"review this paper"*, *"is this study sound?"*, *"audit the methodology"*, *"do the results support the conclusion?"*, *"verify the citations"*, *"is this reproducible?"*, *"produce a referee report"*.

---

### [`belief-revision`](./.claude/skills/belief-revision)
> Update a prior verdict when new evidence emerges — calibrated against both under-correction (anchoring on the prior) and over-correction (anchoring on novelty or social pressure).

Takes a prior analytical output from any of the other six skills and produces a calibrated revision in its format. **Anchor declaration** (write down the prior verdict and your priors in writing *before* reading the new evidence). **Predicted update** (predict the direction and magnitude *before* incorporating). **Pressure-direction check** (is the expected revision direction the institutionally rewarded one?). **Asymmetric-warrant rule:** `(memory — unverified)` and `(user-supplied — unverified)` cannot overturn `(traced)`. **Fresh-analyst test:** would someone seeing only the new evidence (no prior) reach this same revised verdict? Five possible statuses: Confirmed / Refined / Shifted / Overturned / Suspended.

**Triggers:** *"update this verdict"*, *"revise this analysis"*, *"new evidence came in — does it change anything?"*, *"should I change my mind?"*, *"rethink this in light of X"*.

---

## Installation

The skills live under `.claude/skills/` in this repository — Claude Code's standard skills location — so an AI agent can copy them in place without any path rewriting.

Paste this to Claude Code (or any AI coding agent with shell access):

> Install the SKILLs from `https://github.com/patricksavalle/investigate-journalism-skills`.
> Clone the repository to a temporary location, then copy every folder inside its `.claude/skills/`
> directory into my `~/.claude/skills/` directory (for user-level, available across all projects).
> If I'd prefer a project-scoped install, copy them into this project's `.claude/skills/` instead —
> ask me which one I want. After copying, remind me to restart Claude Code or run `/skills` so
> the new skills are loaded.

**Other AI runtimes:** any runtime supporting the SKILL pattern can use these files directly. Point your skill loader at `.claude/skills/`.

---

## Design Principles

**The headline principle: auditable, repeatable reasoning chains.** Every conclusion the toolbox produces ships with its warrant chain attached. An independent reviewer — including one hostile to the conclusion — can re-run the same chain on the same primary sources and check whether it holds. The toolbox's value is not that it removes bias, but that it makes bias *traced and visible* and re-derivable. Everything below serves this.

- **Warrant-labelled traceability** — every load-bearing claim carries `(traced)` / `(deferred to consensus)` / `(deferred, fragile)` / `(memory — unverified)`. Memory-laundering of training-data bias is the failure mode the toolbox exists to prevent.
- **Hook-enforced** — the project's `Stop` hook blocks analytical output that lacks source-tracing, mechanically.
- **Structured, aligned output** — every framework specifies its report format so findings are auditable, and all reports share an outer scaffold so multi-skill chains compose without losing their audit trail.
- **Composable** — each skill declares its Pairs-With partners; tool wiring is visible, not implicit, so a chain that crosses skills stays traceable end-to-end.
- **Trigger-gated** — never spontaneous; always explicit invocation. The user must ask, so the audit trail begins where the user expects it.
- **Charity first** — steelman the target (paper, claim, alternative hypothesis) from its own advocates' primary writing before challenging it. Charitable reading is part of what makes the chain reproducible by sceptics.
- **Self-audit under reversal** — same standards regardless of which side the conclusion lands on; symmetry test mandatory. The audit's value evaporates if it doesn't apply symmetrically.
- **Calibration over verdict** — graded confidence labels and the reader-usable consequential sentence, not binary judgements. The chain carries its hedges into downstream use.
- **Positive evidence demanded** — dual hypotheses require direct positive evidence per side; doubt-cast-on-the-alternative is tracked separately. Asymmetry between the two becomes part of the verdict.
- **Citation-load audited** — peer review extends past in-paper claims to audit what the paper is cited to support downstream. The deployment gap is where field-level harm originates.
- **Source triangulation, not source counting** — institutionally networked single-origin claims that present as "10 sources confirm" are exposed via network reduction.
- **Honest tooling boundaries** — frameworks state what an AI agent can and cannot do natively; no fabricated tradecraft. An audit trail with fabricated steps is worse than no audit trail.

---

## Contributing

Issues and PRs welcome. New SKILLs should follow the existing structure:

1. Frontmatter with `name`, `description`, `version`, `aligned`
2. Explicit **Activation** section listing trigger phrases (and explicit non-triggers where useful)
3. **Pairs With** block naming composition partners across the toolbox
4. **Research Discipline (CLAUDE.md)** block naming which numbered rules apply and how
5. **Warrant Labels** block referencing the project-standard four-label set
6. Phase-numbered methodology (Phase 0 = pre-analysis discipline)
7. Defined **Output Format** block matching the shared outer scaffold
8. **Quick-Reference Matrix** at end

---

## License

See [LICENSE](./LICENSE).

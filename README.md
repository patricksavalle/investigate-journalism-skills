# Investigative AI Journalism

A collection of AI Agent **SKILLs** for investigative journalism — rigorous, framework-driven methodologies for auditing claims, analysing texts, gathering open-source intelligence, and investigating events.

These SKILLs are designed for use with AI agents that support the SKILL pattern (e.g. [Claude Code](https://claude.com/claude-code), the Anthropic Agent SDK, and compatible runtimes). Each SKILL is a self-contained Markdown file with a structured frontmatter header that the agent loads on demand.

---

## What is a SKILL?

A SKILL is a reusable, on-demand instruction module that an AI agent can invoke when its trigger conditions are met. Each skill file follows the same structure:

```yaml
---
name: skill-name
description: When and why to invoke this skill
---

# Skill body — phases, checklists, output format
```

The `description` field tells the agent *when* to load the skill; the body tells it *how* to execute. Skills in this repo are:

- **Triggered explicitly** — the user asks "analyse this for fallacies" and the agent loads the relevant SKILL.
- **Self-contained** — no hidden dependencies on the surrounding project.
- **Outcome-shaped** — they specify a structured output format so results are auditable.
- **Composable** — some skills explicitly hand off to others (e.g. `osint-research` collects and verifies, then hands the structured findings to `investigative-reasoning` for hypothesis work).

---

## Installation

### For Claude Code

Place the skill folders in your Claude Code skills directory.

**User-level (available across all projects):**

```
~/.claude/skills/
```

**Project-level (scoped to one repo):**

```
<your-project>/.claude/skills/
```

Quick install:

```bash
git clone https://github.com/patricksavalle/investigate-journalism-skills.git
cp -r investigate-journalism-skills/fallacy-bias-manipulation-analysis-framework ~/.claude/skills/
cp -r investigate-journalism-skills/investigative-reasoning ~/.claude/skills/
cp -r investigate-journalism-skills/scientific-fact-classification ~/.claude/skills/
cp -r investigate-journalism-skills/osint-research ~/.claude/skills/
cp -r investigate-journalism-skills/peer-review ~/.claude/skills/
```

> **Note:** the `osint-research` skill ships as a file named `SKILL` (no extension). If your runtime only auto-discovers `SKILL.md`, rename it after copying:
>
> ```bash
> mv ~/.claude/skills/osint-research/SKILL ~/.claude/skills/osint-research/SKILL.md
> ```

Restart Claude Code (or run `/skills` in-session) so the new skills are picked up.

### For other AI runtimes

Any runtime that supports the SKILL pattern (frontmatter + Markdown body) can use these files directly. Point your skill loader at the folder containing the skill file.

---

## How to Use

Each SKILL activates on **explicit request only** — none of them spontaneously fire. Use a trigger phrase in your prompt and the agent will load and apply the framework.

| To do this... | Say something like... |
|---|---|
| Audit reasoning in an article | *"Analyse this text for fallacies"* |
| Stress-test an argument | *"Find the manipulation in this"* / *"Is this propaganda?"* |
| Investigate an event | *"Investigate this incident"* / *"Who benefits from X?"* |
| Develop alternative hypotheses | *"Apply critical thinking to this narrative"* |
| Classify a claim's epistemic status | *"Is X a fact?"* / *"Weigh the evidence for Y"* |
| Distinguish fact from assumption | *"Classify these claims"* |
| Build a profile or trace an identifier | *"Find out about X"* / *"Trace this username/email/domain"* |
| Verify an image or video | *"Verify this image"* / *"Where/when was this taken?"* |
| Map a digital footprint | *"What's the digital footprint of X?"* / *"Build a profile on X"* |
| Peer-review a scientific paper | *"Review this paper"* / *"Is this study sound?"* / *"Audit the methodology"* |
| Verify a paper's citations | *"Do the citations support the claims?"* / *"Verify this paper's references"* |
| Check whether results support the conclusion | *"Do the results support the conclusion?"* / *"Is the inferential gap honest?"* |

Each framework produces a **structured report** (severity-rated findings, per-claim audits, source-quality verdicts, Admiralty-graded intelligence briefs) — not free-form prose. The output is designed to be auditable and re-checkable.

---

## The Skills

### 1. [`fallacy-bias-manipulation-analysis-framework`](./fallacy-bias-manipulation-analysis-framework)

> A structured framework for AI agents to analyse text for logical fallacies, cognitive biases, rhetorical manipulation, and other forms of untruthful reasoning.

Audits articles, speeches, op-eds, scientific claims, marketing copy, and political rhetoric for flawed reasoning. Begins with mandatory pre-analysis discipline (steelman first, genre awareness) before flagging fallacies, biases, manipulation tactics, and statistical deception. Outputs severity-rated findings with direct quotations and structural diagnosis.

**Triggers:** *"Analyse this for fallacies"*, *"Find the cognitive biases"*, *"Audit this article's reasoning"*, *"Is this propaganda?"*, *"What rhetorical tricks is this using?"*, *"Stress-test this argument"*.

---

### 2. [`investigative-reasoning`](./investigative-reasoning)

> A structured framework for AI agents to critically analyze events, detect deception, and develop well-reasoned alternative hypotheses.

A detective-method playbook for investigating events and challenging dominant narratives. **Mandates web search at every phase** to break free of training-data biases that skew toward official narratives. Traces every claim to origin, applies cui bono / means–motive–opportunity analysis, surfaces what official accounts leave out, and constructs ranked alternative hypotheses with explicit confidence levels.

**Triggers:** *"Investigate this event"*, *"Develop a conspiracy theory about X"*, *"Who benefits from Y?"*, *"Apply critical thinking to this narrative"*, *"Find red flags in this explanation"*.

---

### 3. [`scientific-fact-classification`](./scientific-fact-classification)

> A structured framework for AI agents to weigh, recognise, and classify claims along the spectrum from objective fact to assumption, opinion, conjecture, and unfalsifiable belief.

Replaces the binary fact / not-fact verdict with a calibrated spectrum. Classifies each load-bearing claim by type (analytic, empirical, causal, theoretical, normative…), tests for falsifiability, GRADEs evidence quality, applies Bradford Hill for causal claims, and labels the result on two axes — **evidence strength** *and* **warrant type** (traced vs. deferred to consensus). Forces explicit calibration; flags consensus failure modes (funder capture, prestige cascades, replication-crisis fields).

**Triggers:** *"Is X a fact?"*, *"Weigh the evidence for Y"*, *"Classify these claims"*, *"Distinguish fact from assumption"*, *"Has this been proven?"*, *"How well-supported is this?"*, *"Is this objective?"*.

---

### 4. [`osint-research`](./osint-research)

> A structured framework for AI agents to plan, execute, and verify open-source intelligence (OSINT) investigations using only publicly available information (PAI).

A full OSINT cycle — Planning → Collection → Processing → Analysis → Dissemination — calibrated to what an AI agent can actually do without shell access or paid databases. Layers search across engines, archives, public records, social platforms, geospatial sources, and specialist registries. Grades every finding with the **Admiralty Code** (NATO STANAG 2511) on independent reliability and credibility axes. Covers reverse image search, geolocation, chronolocation, account-authenticity checks, and systematic identifier pivoting (name → email → domain → infrastructure → entity). Hard constraints (PAI only, no active engagement, no facial recognition on private individuals, harm minimisation) define the boundary between OSINT and conduct that is unethical, unlawful, or operationally compromising.

**Triggers:** *"Find out about X"*, *"Investigate / build a profile on X"*, *"Who is behind this account?"*, *"Verify this image/video"*, *"Where/when was this taken?"*, *"Trace this username/email/domain"*, *"What's the digital footprint of X?"*, *"Is this account real?"*.

**Pairs with:** `investigative-reasoning` — `osint-research` does the gathering and verification mechanics; hand the structured brief to `investigative-reasoning` when the task extends to hypothesis construction or narrative challenge.

---

### 5. [`peer-review`](./peer-review)

> A structured framework for rigorous, citation-verified peer review of scientific papers — auditing methodology, statistics, causal claims, citations, reproducibility, and literature context, then issuing a severity-graded report with explicit recommendation.

Reviews a paper as a competent, sceptical, fair-minded reviewer would. Calibrates standards to the paper's genre and field (preprint vs. journal article; RCT vs. observational; ML vs. lab biology), audits the **inferential gap** between what was measured and what is claimed, scrutinises statistics for p-hacking / HARKing / forking-paths / multiple-testing inflation, and **verifies load-bearing citations** by fetching the cited source and comparing it to the paper's claim (Supports / Partial / Contradicts / Unrelated / Unverifiable). Outputs severity-graded findings (**Fatal / Major / Minor / Optional / Praise**), an explicit recommendation (Accept / Minor / Major / Reject-resubmit / Reject), and — crucially — *what would change the recommendation upward or downward*. Enforces symmetry under conclusion-flip: same paper, opposite conclusion → same review.

**Triggers:** *"Review this paper"*, *"Is this study any good?"*, *"Audit this manuscript"*, *"Is the methodology sound?"*, *"Do the results support the conclusion?"*, *"Verify this paper's citations"*, *"Is this reproducible?"*, *"Produce a referee report"*.

**Pairs with:** `scientific-fact-classification` (claim typing, evidence grading, causal-claim audit), `fallacy-bias-manipulation-analysis-framework` (fallacy / rhetoric scrutiny on theoretical or position papers), and `investigative-reasoning` (when motive, deception, or undisclosed-interest analysis is in scope). `peer-review` orchestrates these where useful and adds the methodology, statistical, citation-verification, reproducibility, and literature-context layers itself.

---

## Design Principles

All SKILLs in this repo share a common philosophy:

- **Trigger-gated** — never spontaneous; always explicit invocation.
- **Charity first** — steelman the target before challenging it.
- **Self-audit** — apply the same standard regardless of which side the conclusion lands on.
- **Calibration over verdict** — graded confidence labels, not binary judgements.
- **Traceability** — distinguish what has been followed to primary evidence from what is being taken on authority.
- **Honest tooling boundaries** — frameworks state what an AI agent can and cannot do natively, so the user is never sold fabricated tradecraft.
- **Structured output** — every framework specifies its report format so findings are auditable.

---

## License

See [LICENSE](./LICENSE).

---

## Contributing

Issues and pull requests welcome. New SKILLs should follow the existing structure:

1. Frontmatter with `name` and `description`.
2. Explicit **Activation** section listing valid trigger phrases (and explicit non-triggers where useful).
3. Phase-numbered methodology (Phase 0 — pre-analysis discipline; Phase 1+ — execution).
4. A defined **Output Format** block.
5. A **Quick-Reference Matrix** and **Golden Rules** summary at the end.
6. Where relevant, an explicit **Pairing rule** stating which other skill should pick up where this one stops.

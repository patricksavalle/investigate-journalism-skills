# Investigative AI Journalism

<p align="center">
  <img src="./overview.png" alt="Investigative AI Journalism — overview of the SKILLs" width="520">
</p>

**Seven tools that help you check before you publish, share, or trust.**

You've read a viral claim. You've found a suspicious account. You want to evaluate a study that contradicts what experts said last year. You suspect a "consensus" is actually three outlets echoing one source.

These tools don't tell you what's true. They help you **show your work** — so anyone can re-check what you found, including someone who disagrees with you.

---

## What makes this different from just asking an AI

An LLM has two capabilities people often confuse: **the knowledge baked into it during training**, and **the skills that came with it** — reading, comparing, reasoning, searching.

**Mode 1 — the talking Wikipedia.** You ask, the model answers from memory. Easy, often useful — but you're leaning on training data, with whatever bias and revisionism is baked in.

**Mode 2 — the research assistant.** You don't trust the model's *knowledge*; you put its *skills* to work on external sources you can verify yourself. Conclusions trace back to documents you can check, not to whatever the training data happened to contain.

These tools force Mode 2. Each one is a SKILL file — a written protocol that locks in which sources to fetch, which checks to run, and how every claim gets labelled. Same discipline every time, regardless of who's prompting.

So instead of just an answer, you get an answer **with every step labelled**:

- Where each claim came from — a source the AI actually fetched, or its memory (those are marked differently, and only one can be load-bearing)
- Who funds the sources
- What it would take to flip the conclusion
- Whether the AI would have reached the same verdict if the politically expected answer ran the other way

If you can't show your work, you can't be trusted. If you can, you can be checked. That's the whole point.

**What this is not.** An AI declaring "the science is settled." It is a structured worksheet — conclusions ship with their evidence chain attached, and you, your editor, or a hostile reader can walk that chain and disagree.

**Also not.** A chatbot that softens its findings when you push back. If you want the verdict changed, the tool asks you for a source, not for agreement.

---

## How to use these tools

> **You don't have to learn the toolbox. You describe what you want, and the right tool loads itself.**

1. **Install once.** Paste the prompt under [*Install*](#install) (below) into Claude Code or your AI agent of choice. The seven skills land in a standard location and stay there. Each skill is also self-contained enough to run on its own.
2. **Just ask, in plain language.** *"Check whether this claim is solid."* *"Investigate this story."* *"Audit this paper."* The agent picks the right tool from your phrasing — you never need to remember tool names.
3. **Read the report.** Every output follows the same shape: a verdict, the findings with each claim labelled by source type, what would change the conclusion, and a self-audit. The labels show you which parts were fetched fresh and which lean on the AI's memory.
4. **Talk back. Push back. Argue with it.** Discussing the result is **encouraged, not risky** — the discipline survives the conversation. Your corrections get verified like any other source; un-sourced pushback gets flagged rather than silently absorbed. You **cannot accidentally corrupt the audit chain by chatting about it**. See [*Discussing the result*](#discussing-the-result) below for the mechanics.
5. **Hand it new evidence whenever it arrives.** Give the AI the new source and ask *"does this change anything?"* — belief-revision kicks in and produces a calibrated update, with the old verdict explicitly compared to the new one.

---

## Pick a tool

| You want to… | Use |
|---|---|
| **Check a claim** — is this actually a fact, or someone's spin? | [`scientific-fact-classification`](./.claude/skills/scientific-fact-classification) |
| **Pull apart an argument** — find rhetorical tricks, propaganda, fallacies | [`fallacy-bias-manipulation-analysis-framework`](./.claude/skills/fallacy-bias-manipulation-analysis-framework) |
| **Investigate an event** — when the official story feels too clean | [`investigative-reasoning`](./.claude/skills/investigative-reasoning) |
| **Background a target** — a person, account, image, domain, organisation | [`osint-research`](./.claude/skills/osint-research) |
| **Audit a study** — does this paper actually show what people say it shows? | [`peer-review`](./.claude/skills/peer-review) |
| **Stress-test your own thinking** — "wait, why do I believe this?" | [`first-principles-thinking`](./.claude/skills/first-principles-thinking) |
| **Update a verdict** — new evidence arrived; does it really change anything? | [`belief-revision`](./.claude/skills/belief-revision) |

You don't have to know which tool to pick. Describe what you want and the agent loads the right one. The "Say:" phrases below show what activates each.

---

## Standalone support

All seven skills can run standalone. That means a compatible AI runtime can load just one `SKILL.md` and still see the core research discipline it needs: warrant-label definitions, the user-supplied-input rule, objective report voice, source/provenance expectations, and the required self-audit. `CLAUDE.md` and `AGENTS.md` remain the canonical full policy files, but they are no longer required context for ordinary use of an individual skill.

| Skill | Standalone? | Notes |
|---|---|---|
| [`scientific-fact-classification`](./.claude/skills/scientific-fact-classification) | Yes | Includes full warrant taxonomy, including `(mixed)`, plus a `Sources & Warrants` table. |
| [`fallacy-bias-manipulation-analysis-framework`](./.claude/skills/fallacy-bias-manipulation-analysis-framework) | Yes | Can run text-only; adds source/warrant tracking when empirical claims or outside sources are invoked. |
| [`investigative-reasoning`](./.claude/skills/investigative-reasoning) | Yes | Keeps mandatory web-search discipline, dual hypotheses, source network mapping, and evidence-integrity tables inline. |
| [`osint-research`](./.claude/skills/osint-research) | Yes | Keeps OSINT safety constraints, Admiralty grading, warrant labels, access dates, and source alignment fields inline. |
| [`peer-review`](./.claude/skills/peer-review) | Yes | Keeps citation verification, deployment-gap audit, source/warrant tracking, and review self-audit inline. |
| [`first-principles-thinking`](./.claude/skills/first-principles-thinking) | Yes | Runs as a conceptual tool; when empirical Bedrock is invoked, it carries warrant labels and a conditional source table. |
| [`belief-revision`](./.claude/skills/belief-revision) | Yes | Keeps the asymmetric-warrant rule inline, so weak new evidence cannot overturn stronger prior warrants. |

The mirrored `.agents/skills/` copies are aligned with `.claude/skills/` for Codex-style runtimes.

---

## What each one does, in plain English

### Is this claim solid? — `scientific-fact-classification`

Takes a claim ("X causes Y", "studies show…", "it's been proven that…") and places it on the spectrum from **established fact** to **assumption** to **opinion** to **unfalsifiable belief**. Tells you what's missing for the claim to qualify as fact, and gives you a **calibrated sentence** you can use in your own writing — one that carries the right hedges so it can't be misread as bigger than the evidence supports.

Say: *"is X a fact?"* · *"weigh the evidence for…"* · *"how well-supported is this?"*

### Find the manipulation — `fallacy-bias-manipulation-analysis-framework`

Reads a text — article, speech, transcript, thread — and surfaces fallacies, cognitive biases, propaganda techniques (firehose-of-falsehood, motte-and-bailey, DARVO, gaslighting…), statistical sleight-of-hand, and discourse-level patterns. Charitable first: every flag has to survive a steelman reading, or it's dropped.

Say: *"analyse this for fallacies"* · *"is this propaganda?"* · *"what rhetorical tricks are being used?"*

### Investigate an event — `investigative-reasoning`

Detective work for contested events. Builds **two** hypotheses — the official narrative *and* a steelmanned alternative — and compares them head-to-head. Demands **positive evidence** on each side (not just "doubt about the other"). Maps who benefits, what means and motive look like, and surfaces when "ten outlets confirmed it" turns out to be ten outlets quoting one source.

Say: *"investigate this event"* · *"who benefits from this?"* · *"find the red flags in this explanation"*

### Background a target — `osint-research`

Open-source intelligence using only publicly available information. Profiles people, accounts, images, domains, organisations, events. Verifies images and videos (where and when was this taken?). Grades each source on independence and credibility. Hard limits built in: no facial recognition on private individuals, no breaking into anything, no fabricating tradecraft the AI can't actually do.

Say: *"find out about X"* · *"build a profile on this account"* · *"verify this image"* · *"trace this domain"*

### Audit a paper — `peer-review`

Reads a scientific paper and produces a referee-style report. Checks the methodology against its field's standards, audits the stats, **verifies the citations** (fetches each load-bearing cited source and checks it actually supports the paper's claim), and — distinctively — checks the **deployment gap**: is this paper being cited downstream to support claims much bigger than it actually shows? Findings come back tagged Fatal / Major / Minor, with what would change the verdict.

Say: *"review this paper"* · *"is this study sound?"* · *"verify the citations"*

### Why do I believe this? — `first-principles-thinking`

For when a belief or argument feels inherited rather than earned. Breaks the claim down to bedrock truths and rebuilds the reasoning. Useful when conventional wisdom suddenly feels shaky, or when you're stuck on a proposal whose justification you can't quite articulate.

Say: *"is this actually true?"* · *"why is it done this way?"* · *"break this down from first principles"*

### Did new evidence change anything? — `belief-revision`

You had a conclusion; new evidence arrived. Should you update — and by how much? This tool guards against both **under-correction** (anchoring on your prior because changing your mind feels like losing) and **over-correction** (chasing the loudest new thing). You write down your prior first, predict the update before reading the evidence, then check whether the actual update was driven by the evidence or by where the social pressure points.

Say: *"does this change anything?"* · *"should I change my mind?"* · *"revise this analysis"*

---

## How the tools work together

You don't have to learn the wiring — each tool calls the others when it needs to. A peer review pulls in fact-classification for individual claims. An investigation pulls in OSINT for backgrounding. Any of them hands off to belief-revision when new evidence arrives. The audit chain stays end-to-end.

---

## How they stay honest

The full discipline is embedded in each standalone skill. Five rules are especially visible in every report, so the discipline you get is the same regardless of which one produced the output:

1. **Every claim labelled.** Did the AI fetch the source this session, or is it working from memory? Both are allowed — but they're marked differently, and only fetched sources can be load-bearing.
2. **Symmetry test.** Every output ends by answering: *would I have reached the same verdict if the politically expected answer ran the other way?* If not — explain why.
3. **Primary before secondary.** When someone summarises a paper, court filing, or document, fetch the actual thing before citing.
4. **Map the network.** Ten outlets repeating one source is not ten sources. The tool surfaces this rather than letting "consensus" hide a single point of origin.
5. **Your pushback doesn't override the chain.** When you correct the AI mid-analysis, your input is marked *user-supplied, unverified* until you provide a source. The audit trail has to survive *you*, because the reader downstream did not agree to trust you.

A behind-the-scenes check ("Stop hook") will block the AI from producing investigation-style output when it didn't actually fetch any sources — so it can't fake the homework. Full canonical rules are in [CLAUDE.md](./CLAUDE.md) and [AGENTS.md](./AGENTS.md), but each individual skill carries the operational subset needed to run safely on its own.

---

## Discussing the result

You can — and should — push back on what the AI produced. The toolbox is built for argument. But the AI doesn't drop its discipline just because the conversation has narrowed to you and it. Every correction, counter-argument, "wait, actually…" and "consider this…" gets the same treatment any other source gets.

**It asks for the receipt.** A correction with a URL or citation can be fetched, verified, and folded into the chain as `(traced)`. A correction without a source gets marked `(user-supplied — unverified)` and cannot be load-bearing — it can be incorporated as a *hypothesis to test*, but the verdict won't pivot on it.

**It runs the symmetry test on you.** *Would the analysis have updated the same way if your contribution had pointed in the opposite direction with the same evidential weight?* If the honest answer is "no, I'd only update for one direction" — that's anchoring on your preference, not on the evidence, and the AI says so out loud.

**It notes that you have stakes too.** On charged topics, the AI acknowledges — without accusation — that you have your own alignment, funding, priors, and reasons to want the conclusion to land a particular way. It applies the same scepticism to your input that it applies to any source with skin in the outcome. The discipline doesn't exempt the person at the keyboard.

**It distinguishes "direct me" from "override me."** You can legitimately:
- Point the AI at a new angle to investigate
- Provide a primary document for it to fetch
- Identify an error in the chain — with a source-traced correction
- Reject the conclusion in your own voice (a personal opinion piece is a different output than an audited analysis)

You can't legitimately have it suppress findings you dislike, accept un-sourced assertions as established evidence, or label something `(traced)` that it didn't actually trace this session.

This isn't about distrusting you. It's about preserving the audit trail for the person reading the output later — your editor, a sceptical reader, your future self — who didn't agree to trust you, and who has to be able to walk the chain themselves. If you push for a revision without a source and the AI declines to flip the verdict, that's the discipline working. Send the primary document and it'll fetch it; the chain extends.

---

## Install

The skills live under `.claude/skills/` — the standard location, so any compatible AI agent can install them by copying the folder. Codex-compatible mirrors also live under `.agents/skills/`.

**For Claude Code,** paste this:

> Install the SKILLs from `https://github.com/patricksavalle/investigate-journalism-skills`.
> Clone the repository to a temporary location, then copy every folder inside its `.claude/skills/`
> directory into my `~/.claude/skills/` directory so they're available across all my projects.
> If I'd prefer a project-only install, copy them into this project's `.claude/skills/` instead —
> ask me which. After copying, remind me to restart Claude Code or run `/skills`.

**For other AI runtimes** that support the SKILL pattern: point your loader at `.claude/skills/` or `.agents/skills/`. The files are plain Markdown with frontmatter — no build step. You may also copy a single skill folder by itself; all seven skills are standalone.

---

## A note for editors and contributors

The discipline check ([`.claude/hooks/check-research-warrant.ps1`](./.claude/hooks/check-research-warrant.ps1)) reads marker phrases out of skill outputs. If you rename a section or warrant label inside a skill, update the hook regex in the same change — or the check stops catching things silently.

New skill PRs should follow the existing pattern: frontmatter (`name`, `description`, `version`, `aligned` date), an Activation block with trigger phrases, a Pairs-With block, a standalone `Research Discipline (CLAUDE.md/AGENTS.md)` block, inline warrant-label definitions, source/provenance hooks where empirical evidence can appear, and the shared report scaffold (Summary → body → Confidence & Severity → What Would Change This → Self-Audit → Limits).

---

## License

See [LICENSE](./LICENSE).

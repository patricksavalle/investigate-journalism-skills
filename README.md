# Investigative AI Journalism

<p align="center">
  <img src="./overview.png" alt="Investigative AI Journalism — overview of the SKILLs" width="520">
</p>

**Eight standalone analytical skills, plus one hunch micro-skill and one Dutch publishing skill, for checking claims, articles, studies, sources, arguments, revisions, and publishable writeups before you share or trust them.**

The toolbox helps an AI work as a research assistant instead of a memory machine: fetch sources, label warrants, map source networks, show uncertainty, and preserve an audit trail that other people can re-check.

## Pick A Tool

| You want to... | Use |
|---|---|
| Turn a gut feeling or "something feels off" reaction into testable hypotheses | [`intuitive-thinking`](./.claude/skills/intuitive-thinking) |
| Check whether a claim is fact, assumption, opinion, or overreach | [`scientific-fact-classification`](./.claude/skills/scientific-fact-classification) |
| Review whether an article is fair, sourced, accurate, and well-framed | [`journalistic-article-review`](./.claude/skills/journalistic-article-review) |
| Find fallacies, bias, propaganda, manipulation, or rhetorical tricks | [`fallacy-bias-manipulation-analysis-framework`](./.claude/skills/fallacy-bias-manipulation-analysis-framework) |
| Investigate a contested event or competing explanation | [`investigative-reasoning`](./.claude/skills/investigative-reasoning) |
| Background a person, account, image, domain, organisation, or event | [`osint-research`](./.claude/skills/osint-research) |
| Audit whether a scientific paper actually supports its conclusions | [`peer-review`](./.claude/skills/peer-review) |
| Break a belief, proposal, or argument down from first principles | [`first-principles-thinking`](./.claude/skills/first-principles-thinking) |
| Update a previous verdict when new evidence arrives | [`belief-revision`](./.claude/skills/belief-revision) |
| Turn a finished warrant-labelled analysis into a Dutch article | [`publisher-nl`](./.claude/skills/publisher-nl) |

You do not need to remember the skill names. Ask in plain language, for example: *"review this article"*, *"audit this paper"*, *"is this claim solid?"*, *"investigate this event"*, or *"does this new evidence change the verdict?"*

## What Makes It Different

Every analytical skill embeds the same discipline:

- **Warrant labels:** claims are marked as `(traced)`, `(deferred to consensus)`, `(deferred, fragile)`, `(memory — unverified)`, or `(user-supplied — unverified)`; hunches are marked `(intuition — unwarranted)`; consensus labels mark social/institutional priors, not scientific warrant.
- **Primary before secondary:** papers, filings, datasets, speeches, and documents are checked at the source where possible.
- **Source-network checks:** repeated claims from one funding, ownership, mandate, or alignment node are not treated as independent corroboration.
- **Self-audit:** reports end by asking whether the verdict would survive if the expected answer ran the other way.
- **User input discipline:** corrections and pushback are welcome, but unsourced assertions do not become load-bearing evidence.

Canonical rules live in [CLAUDE.md](./CLAUDE.md). Each `SKILL.md` also carries the operational subset needed to run by itself.

## Standalone Support

All eight analytical skills can run standalone. `intuitive-thinking` is intentionally smaller: it is a Phase 0 hunch register that should hand off to the relevant analytical skill once a checkable claim appears. `publisher-nl` is a writing-only skill for finished, warrant-labelled analyses; it does not research or add facts. A compatible AI runtime can load a single `SKILL.md` and still get the warrant labels, source/provenance expectations, user-input rule, objective report voice, and self-audit requirements.

Mirrors:

- Claude-style skills: [`.claude/skills/`](./.claude/skills)
- Agent-runtime skills for Codex, Gemini, and other compatible agents: [`.agents/skills/`](./.agents/skills)

Hooks are runtime-specific, not skill-specific:

- Claude Code uses [`.claude/settings.json`](./.claude/settings.json) and [`.claude/hooks/`](./.claude/hooks).
- Codex uses [`.codex/hooks.json`](./.codex/hooks.json) and [`.codex/hooks/`](./.codex/hooks).
- `.agents/skills/` does not need its own hooks folder. Gemini and other agents can use the `.agents` skills, but hook enforcement depends on whether that runtime supports an equivalent hook system.

## Install

The skills live under `.claude/skills/`. Agent-runtime mirrors for Codex, Gemini, and other compatible tools live under `.agents/skills/`.

For Claude Code, paste:

> Install the SKILLs from `https://github.com/patricksavalle/investigate-journalism-skills`.
> Clone the repository to a temporary location, then copy every folder inside its `.claude/skills/`
> directory into my `~/.claude/skills/` directory so they're available across all my projects.
> If I'd prefer a project-only install, copy them into this project's `.claude/skills/` instead.
> After copying, remind me to restart Claude Code or run `/skills`.

For other runtimes, point your loader at `.claude/skills/` or `.agents/skills/`. You can also copy a single skill folder; every skill is standalone.

## For Contributors

If you rename output sections or warrant labels inside a skill, update the stop-hook regex in [`.claude/hooks/check-research-warrant.ps1`](./.claude/hooks/check-research-warrant.ps1) and [`.codex/hooks/check-research-warrant.ps1`](./.codex/hooks/check-research-warrant.ps1).

New analytical skills should include frontmatter, activation guidance, specialist handoffs, standalone research discipline, warrant labels, source/provenance tables where empirical evidence appears, and the shared report scaffold. Micro-skills like `intuitive-thinking` should stay small, add one reusable discipline, and route onward rather than re-embedding the whole toolbox. Review orchestrators should route specialist work to other skills instead of re-embedding the whole toolbox.

## License

See [LICENSE](./LICENSE).

---
name: intuitive-thinking
description: Micro-skill for recording gut feelings, hunches, anomaly signals, and "something feels off" reactions as pre-evidence hypotheses before article review, investigations, OSINT, claim audits, rhetoric audits, peer review, scientific fact classification, or belief revision. Use only as a Phase 0 hunch register; intuition may guide tests and searches but never supports a verdict.
version: 0.3
aligned: 2026-06-05
---

# Intuitive Thinking

Use this as a **Phase 0 hunch register** before a real analytical skill.

Core rule: **intuition generates hypotheses; evidence carries verdicts.**

## When To Use

Use when a task starts from a gut feeling, hunch, suspicion, unease, pattern match, or "something feels off".

Common article-review triggers:

| Hunch | Downstream test |
|---|---|
| Headline feels too strong | Headline-body alignment |
| Source mix feels captured | Source independence / right of reply |
| Number feels inflated | Raw count, denominator, baseline, timeframe, absolute effect |
| Framing feels manipulative | Rhetoric, omissions, quote context |
| Story feels too neat | Alternative hypotheses, missing primaries |
| Timing feels convenient | Chronology, beneficiaries, prior drafts |

## Warrant Label

`(intuition — unwarranted)` = a gut feeling, anomaly signal, or pattern impression. It may generate hypotheses and search leads. It is never evidence, never load-bearing, and cannot revise, refute, or establish a claim.

If the hunch later proves useful, cite the traced evidence that tested it, not the hunch itself.

## Micro-Template

Use this before search, then hand off.

```markdown
## Intuition Register
- **Trigger:** [what was noticed]
- **Immediate story:** [first explanation] `(intuition — unwarranted)`
- **Competing explanations:** H1 [hunch right]; H2 [ordinary explanation]; H3 [opposite-direction explanation]; H4 [missing information]
- **Disconfirmation:** [what would weaken or kill the hunch]
- **Search leads:** [primary/data/source to fetch]; [disconfirming source/query]; [strongest alternative source/query]
```

## Routing

- Article quality, headline, sourcing, omissions -> `journalistic-article-review`
- Single empirical or causal claim -> `scientific-fact-classification`
- Contested event or official narrative -> `investigative-reasoning`
- Source identity, funding, account, image, domain -> `osint-research`
- Rhetoric or manipulation -> `fallacy-bias-and-manipulation-analysis`
- Hidden assumption or definition -> `first-principles-thinking`
- New hunch about a prior verdict -> `belief-revision`

## Self-Check

Before routing onward, ask:

- Would this hunch still be worth testing if it pointed the other way?
- Is the feeling being used as evidence, or only as a search prompt?
- Did the first story crowd out ordinary, opposite, or missing-information explanations?

# Isolating the R1 Major drop — 2026-08-10

> **Corrected the same day.** The first version of this file concluded that the
> ethics row was the primary cause. That conclusion came from a defective
> severity counter — it did not recognise the `**Finding 1 — …**` entry format,
> and so read two of the five ethics-alone runs as having no Major findings when
> they had five between them. The counter is fixed, pinned by selftest against
> that exact format, and now reproduces the committed baseline count of 6. The
> corrected numbers are below and they do **not** support the original
> conclusion. The original text is not preserved; it was wrong, and leaving it
> alongside the correction would only invite citing it.

Five runs against `e4c5ea2` ("Revert the peer-review severity floor; keep the
ethics row") — ethics row present, Stage 2 absent. Resolved model
**claude-sonnet-5**, **$10.44**. Outputs in `runs/R1-ethics-alone/`.

This is the measurement `rerun-2026-08-10.md` asked for and could not take,
because the floor and the ethics row shipped together and Stage 2 arrived before
anyone separated them.

## Four measurements of R1, corrected

| Build | ethics row | floor | Stage 2 | Major total | runs with ≥1 Major |
|---|---|---|---|---|---|
| `a7c86e6` baseline | — | — | — | 6 | **3 / 5** |
| `ca72842` re-run | yes | yes | — | 0 | **0 / 5** |
| `e4c5ea2` ethics only | yes | — | — | 5 | **2 / 5** |
| `769b88a` main | yes | — | yes | 1 | **1 / 5** |

Read the right-hand column. A total is dominated by whichever run decides to
grade Majors at all — the ethics-alone build's five Majors come from two runs, one
carrying three and one carrying two, while three runs found none. The share of
runs finding anything is the stabler statistic and is now what `score.py severity`
reports alongside the total.

## What the corrected numbers support

**Not much, and that is the finding.**

Baseline to main is 3/5 → 1/5. The intermediate build sits between them at 2/5.
Every step is one run changing its mind, and at n=5 the whole range 0.2–0.6 is
inside what sampling noise produces. The measurement separates the *floor* from
everything else cleanly — 0/5 is a real signal, and the floor is already reverted
— but it does not separate the ethics row from Stage 2.

The earlier claim that the ethics row halves Majors was an artefact of the
counting bug. With that fixed, the ethics row moves 3/5 → 2/5 and Stage 2 moves
2/5 → 1/5: two indistinguishable one-run steps.

## What is still observed, independent of the count

Runs adopt the ethics row's **reporting-defect framing** and apply it to gaps
Phase 6 never mentions — GISAID-only deposition, an uncited comparator, absent
negative controls. That is visible in the text, not inferred from a count:

| Build | runs using "reporting defect / completeness" |
|---|---|
| baseline — language not in the skill | — |
| `e4c5ea2` ethics only | 3 of 5 |
| `769b88a` main | 5 of 5 |

The framing spreading is real. Whether it is what moved the severity grades is
exactly what n=5 cannot say.

## Consequences

1. **Stage 2 is no longer the lesser suspect.** The largest single step in the
   share, 2/5 → 1/5, sits with it. It is a one-run step and proves nothing, but
   the earlier record had this backwards and it is now on `main`.
2. **`stage-7-scope-ethics-row` needs re-justifying.** Scoping the
   reporting-defect default is defensible on its own terms — the rule genuinely
   does not state its scope, and runs genuinely generalise it. It should no longer
   be described as the fix for the Major drop, because nothing here establishes
   what caused that.
3. **n=5 is the binding constraint, not a caveat.** Two counting formats and one
   run's judgement were enough to invert a published conclusion. Runs per build is
   the variable that would make these measurements decide things; nothing else in
   this session comes close in value.

## Standing

- The ethics row keeps its detection win: 5/5 runs search the full text for
  approval and consent language, against 2/5 at baseline. That is a large effect,
  measured twice, and is not in question.
- The severity effect is unattributed and stays that way until R1 runs at
  n≥15 per build, or until a second peer-review item with an unambiguous fault
  gives the severity scale something less borderline to grade.
- Cost of this attribution attempt: **$10.44**, and its main product is a corrected
  instrument rather than an answer.

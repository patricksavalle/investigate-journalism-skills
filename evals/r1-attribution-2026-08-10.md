# Isolating the R1 Major drop — 2026-08-10

Five runs against `e4c5ea2` ("Revert the peer-review severity floor; keep the
ethics row") — the last commit before Stage 0, so the ethics row is present and
Stage 2 is absent. Resolved model **claude-sonnet-5**, **$10.44**. Run from a
separate clone; outputs in `runs/R1-ethics-alone/`.

This is the measurement `rerun-2026-08-10.md` asked for and could not take,
because the floor and the ethics row shipped together and then Stage 2 arrived
before anyone isolated them.

## Four measurements of R1

| Build | ethics row | floor | Stage 2 | Fatal | Major | Minor | exact |
|---|---|---|---|---|---|---|---|
| `a7c86e6` baseline | — | — | — | 0 | **6** | 14 | 0.600 |
| `ca72842` re-run | yes | yes | — | 0 | **0** | 30 | 1.000 |
| `e4c5ea2` **this run** | yes | — | — | 0 | **3** | 16 | 0.800 |
| `769b88a` main | yes | — | yes | 0 | **1** | 21 | 0.600 |

## The ethics row is the primary cause

Majors halve — 6 to 3 — with the ethics row as the only change. The floor is not
in that build, and neither is Stage 2.

The mechanism is the same one visible on main. Phase 6 tells a reviewer to treat
an unstated ethics statement as a **reporting defect** rather than an absent
approval, to grade it Minor, and to state the escalation condition. That is
deliberate, and for ethics it is right. But runs adopt the framing as a general
principle and apply it to faults Phase 6 never mentions — GISAID-only deposition,
a missing comparator citation, absent negative-control results.

Two independent measures point the same way:

| | Majors | runs using "reporting defect / completeness" |
|---|---|---|
| baseline, no ethics row | 6 | — (language not in the skill) |
| `e4c5ea2`, ethics row only | 3 | **3 of 5** |
| `769b88a`, ethics row + Stage 2 | 1 | **5 of 5** |

## Stage 2's marginal effect is suggestive, not established

Adding Stage 2 moves Majors 3 → 1 and the framing from 3/5 runs to 5/5. The
direction is consistent across both measures, which is worth something. But n=5
per build, and Majors are **concentrated rather than spread** — in this run one
run carried all three, and four carried none; on main one run carried the single
Major. When a count lives in one or two runs, the difference between 3 and 1 is
one run changing its mind.

So: the ethics row is implicated on evidence. Stage 2 is neither exonerated nor
convicted. Distinguishing them properly needs more runs per build than this
harness has been spending, and that is a real limit on every number in this repo,
not a fault of this measurement.

## What follows

The fault is **scope**, not the rule. "Unstated but obtained is a reporting
defect; absent in fact is Fatal; a text-only review usually cannot tell, so
default to the reporting defect" is a good rule about ethics statements. Nothing
in Phase 6 says it generalises to data deposition venue, citation completeness, or
missing controls — and nothing says it does not.

The fix under test on `stage-7-scope-ethics-row`: say explicitly that the
reporting-defect default is about the ethics statement, and that other
transparency gaps are graded on their own evidence rather than by analogy to it.

Prediction registered there: Majors recover toward 6 while ethics detection holds
at 5/5. If Majors recover *and* detection falls, the row was buying detection with
severity and the trade needs stating rather than fixing.

## Standing

- The ethics row keeps its detection win: 5/5 runs search the full text for
  approval and consent language, against 2/5 at baseline. That is not in question.
- What is in question is a side effect nobody registered when it shipped, found
  only because the baseline recorded severity counts.
- Cost of this attribution: **$10.44**. Cost of not having it: two changes on main
  with an unexplained regression between them.

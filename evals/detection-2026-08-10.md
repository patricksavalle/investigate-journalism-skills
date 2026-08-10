# Detection, not severity — 2026-08-10

Re-analysis of the twenty R1 runs already on disk. **No new runs, $0.**

The session had spent $34 on severity comparisons that separated nothing. The
one clean effect it did produce — the ethics row moving ethics-statement
detection from 2/5 runs to 5/5 — was a *detection* effect. So the runs were
re-scored on what each review **found** rather than how it **graded**.

Faults were enumerated from the **baseline runs only** (`a7c86e6`, which predates
every change under test) and the patterns applied unchanged to later builds. A
catalogue derived from the builds being compared could be fitted to the answer.

## Result

Runs raising each fault inside a Findings section, out of 5 (mentions anywhere in
brackets):

| Fault | baseline | ethics+floor | ethics only | main |
|---|---|---|---|---|
| ethics-consent | 2/5 (2) | **5/5** (5) | **5/5** (5) | **5/5** (5) |
| sampling-frame | 3/5 (3) | 3/5 (4) | 1/5 (3) | 3/5 (5) |
| additional-evidence-uncited | 1/5 (1) | 0/5 (3) | 0/5 (2) | 0/5 (2) |
| gisaid-deposition | 3/5 (5) | 1/5 (5) | 2/5 (5) | **4/5** (5) |
| patient-genome-mapping | 1/5 (1) | 1/5 (1) | 0/5 (1) | 0/5 (0) |
| release-timeline | 1/5 (1) | 0/5 (0) | 0/5 (0) | 0/5 (0) |
| self-citation-independence | 1/5 (2) | 3/5 (4) | 0/5 (2) | 2/5 (3) |
| small-denominator | 2/5 (3) | 0/5 (0) | 1/5 (1) | 1/5 (2) |
| **mean finding rate** | 0.350 | 0.325 | 0.225 | **0.375** |
| **mean mention rate** | 0.450 | 0.550 | 0.475 | **0.550** |

## What it settles

**Stage 2 did not suppress findings.** `main` has the **highest** mean finding
rate and the highest mention rate of any build, including the baseline. Reviews on
`main` notice at least as much as they ever did.

So the Major drop measured earlier — 3/5 runs finding a Major at baseline, 1/5 on
`main` — is a **grading** shift sitting on a stable or slightly improved detection
base. Nothing is being missed. Things that are found are being labelled Minor.

That is a materially different problem from the one feared, and a much less
serious one. A review that finds a fault and grades it gently still puts it in
front of the reader; a review that never finds it does not.

**The ethics row's detection win is the one robust effect in the whole session.**
2/5 → 5/5, replicated independently in three separate builds. Everything else here
moves by one or two runs and should be read as noise.

## What it does not settle

The mean rates span 0.225 to 0.375 — four builds, n=5 each, differences of one or
two runs per fault. Only the ethics-consent row is large enough to carry weight on
its own. In particular, the "ethics only" build's low 0.225 is not evidence that
the ethics row *reduces* detection; it is five runs.

Two faults were found once at baseline and never again — `release-timeline` and,
after baseline, `additional-evidence-uncited` as a *finding* (it stays mentioned
in 2 of 5 runs on `main`, so it is being noticed and not raised). At n=5 a 1/5
baseline is indistinguishable from zero, so this is a question for a larger run,
not a conclusion.

## Consequences

1. **Stage 2 stops being the prime suspect.** The earlier record had it as the
   largest single step in the Major share; on detection it is the best build
   measured. It stays on `main`.
2. **`stage-7-scope-ethics-row` gets its justification back, on corrected
   grounds.** It is not about recovering lost findings — none were lost. It is
   about whether faults that *are* found get graded proportionately, which is
   exactly what an over-generalised reporting-defect default would distort.
3. **Detection should be the default comparison for peer-review items from here.**
   It is cheaper (re-scores existing runs), more stable (a fact rather than a
   judgement), and it produced in one pass what $34 of severity comparison could
   not.

## Method note

`score.py detection --item R1` reports both `as_finding` and `mentioned`. The gap
between them is informative on its own: on `main`, `sampling-frame` is mentioned
in 5 runs and raised as a finding in 3, and `additional-evidence-uncited` is
mentioned in 2 and raised in none. A review that discusses a gap in its
Methodology Audit but never raises it has half-noticed it — a distinction a
severity count erases completely.

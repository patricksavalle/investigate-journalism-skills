# Stage 7 — scope the ethics reporting-defect default (branch `stage-7-scope-ethics-row`, unmerged)

The fix that [`r1-attribution-2026-08-10.md`](r1-attribution-2026-08-10.md) points at.

## The fault was scope, not the rule

Phase 6 tells a reviewer that an unstated ethics statement is a *reporting defect*
rather than an absent approval, to grade it Minor, and to state the escalation
condition. That is right. Measured across three builds, reviews then adopted the
framing as a general principle and applied it to gaps Phase 6 never mentions —
GISAID-only deposition, an uncited comparator, absent negative controls — and R1's
Major findings fell from 6 to 3 on the ethics row alone, then to 1 with Stage 2 on
top.

Nothing in Phase 6 said the default generalised. Nothing said it did not.

## What changed

One paragraph, saying why the default holds for ethics and why that reasoning does
not transfer:

> Approval and consent are things a study either obtained or did not, independently
> of whether the article mentions them — the text is silent about a fact that
> already exists, so silence is weak evidence. Other transparency gaps are not like
> that. Unavailable data, deposition to a registration-gated repository, an uncited
> comparator, a missing negative control: in each case the gap *is* the defect, not
> a report of one.

Stating the *reason* rather than adding a prohibition is deliberate. A flat "do not
apply this elsewhere" would be a rule to route around; the asymmetry between "the
fact exists and the text omits it" and "the gap is the fact" is something a
reviewer can apply to cases neither of us listed.

## Prediction, registered before the run

1. **R1 Majors recover toward 6.** Expect 4–6. Recovery to exactly the baseline is
   not required — the ethics gap itself legitimately accounts for one of the
   original six, per `rerun-2026-08-10.md`.
2. **Ethics detection holds at 5/5.** The row's detection win is not being touched.
3. **Runs using "reporting defect" framing falls below 5/5**, and where it survives
   it attaches to the ethics finding only.
4. **The recommendation stays in the Accept/Minor band.** More Majors should not
   push this paper to a Major recommendation; if it does, the severity scale and
   the recommendation scale are coupled more tightly than Phase 7 states.

**If Majors recover and detection falls**, the ethics row was buying detection with
severity, and the honest response is to state that trade rather than fix it.

## How to measure

```bash
git checkout stage-7-scope-ethics-row && OUTDIR=R1-stage7 sh evals/run.sh R1
```

```bash
python evals/score.py severity evals/runs/R1-stage7/
```

Five runs, roughly $12. Compare against all four builds in the attribution record.

## Adopt / revert

- **Adopt** if Majors reach 4+ and ethics detection holds at 5/5.
- **Revert** if detection falls below 4/5 — the detection win is worth more than the
  severity accuracy, and the trade should then be documented instead.
- **Leave parked** if Majors land at 3, unchanged. That would mean the scoping
  paragraph is not reaching the behaviour, and the next thing to try is moving the
  scope statement into the Phase 7 severity guidance where the grading decision is
  actually made.

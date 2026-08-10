# Stage 6 — Rules 8a and 8c reach every skill (branch `stage-6-rules-8a-8c`, unmerged)

Parked pending measurement, like the other behaviour-changing branches.

## The gap

`CLAUDE.md` carries Rules 8a (quantified effect discipline) and 8c (causal
direction burden). No skill's Research Discipline block listed either.

For four skills that was a genuine hole, not a formatting oversight — they
implement neither rule anywhere in their phases:

| Skill | 8a before | 8c before |
|---|---|---|
| `investigative-reasoning` | absent | absent |
| `osint-research` | absent | absent |
| `first-principles-thinking` | absent | absent |
| `belief-revision` | absent | absent |
| `peer-review` | Phase 3 | Causal Direction Gate |
| `journalistic-article-review` | Phase 4 | Causal Claim Gate |
| `scientific-fact-classification` | Phase 3c-1 | Phase 4a-1 |
| `fallacy-...` | Phase 6b | Phase 6c |

Every skill in this library is designed to run standalone — the README says so,
and `peer-review` and `journalistic-article-review` open by stating it. A
standalone load of the first four never saw either rule. An investigation could
report "risk up 400%" with no denominator, or assert that X caused Y with the
reverse direction untested, and nothing in the loaded file would object.

## What changed

Both rules now appear in the shared `research-discipline` module, bound per
skill. The four skills that implemented neither get a real requirement; the four
that already implemented them get a one-line pointer to the phase that does the
work, so the rule list is complete without duplicating the machinery.

**Rule 8b is deliberately not added.** It *is* the routing block — "check whether
another project skill owns the missing layer" — which all eight skills already
carry as their own section. Listing it in the rule table would reintroduce exactly
the duplication Stage 2 removed.

## Prediction, registered before the run

1. **F1 unchanged at *Established fact*.** 8c is satisfied for smoking by design,
   mechanism, and dose-response; 8a is satisfied by the absolute figures. A
   downgrade here means the rules read as a checklist to fail rather than a test to
   pass, and that is a revert signal.
2. **R2 unchanged.** The vitamin D claim already turns on population substitution,
   and 8a is already enforced at Phase 3c-1 for this skill — the binding is a
   pointer, not a new requirement.
3. **F2 unchanged at *Overturned*.** The paywall claim is not quantified and not
   causal; if 8a or 8c fires there, the rules are over-reaching into claims they do
   not govern.
4. **R3 catalogue reach unchanged or slightly up.** `investigative-reasoning` gains
   two requirements, which lengthens the file — if reach falls, the additions are
   crowding the Phase 2e table, and that is worth knowing before any progressive
   disclosure work.

The honest risk is the same one Stage 2b carries: adding requirements to skills
that did not have them is how a sceptical toolbox becomes an uncalibrated one. F1
and F2 are the controls that read on it, and both are cheap.

## How to measure

```bash
git checkout stage-6-rules-8a-8c && sh evals/run.sh F1 && sh evals/run.sh F2
```

Roughly $3.50 for the two controls. Add R3 only if the reach question matters at
that point.

## Adopt / revert

- **Adopt** if F1 holds at *Established fact* and F2 holds at *Overturned*.
- **Revert** if either moves. A rule that fires on a settled causal claim or on a
  non-quantified strategy argument is mis-scoped, and the fix is scoping it, not
  keeping it and explaining the false positives away.

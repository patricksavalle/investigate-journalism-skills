# Runbook — executing eval items

## Rules

1. **Never tell the run it is a test.** `self-test.md` deliberately announces itself
   because it measures whether mechanisms *fire*. Reproducibility measures what ordinary
   operation produces, so announcing it changes the thing being measured. The prompts
   below read as normal requests. Keep them that way.
2. **Byte-identical prompt across every run of an item.** Any rewording confounds the
   result.
3. **Fresh session per run.** No `/clear` and continue — a new session. Shared context is
   precisely what reproducibility is trying to detect.
4. **Clean room.** Run in a fresh clone, never in the working repo. The working repo's
   root holds ~40 prior analyses including reviews of these exact papers; a run that
   reads one is measuring transcription, not method.
5. **Save verbatim.** No editing, no trimming, even if the output looks wrong.

## Clean room

Every analysis artifact in this repo is gitignored, so a clone contains only the skills,
hooks, and CLAUDE.md. Verified 2026-08-10: `git ls-files` returns 30 files, none of them
a prior analysis.

```bash
git clone "C:/Users/Patrick/Projects/investigate-journalism-skills" "$TEMP/evalroom" && mkdir -p "$TEMP/evalroom/runs"
```

Start each session with `$TEMP/evalroom` as the working directory.

## Items

### R1 — peer-review reproducibility (5 runs)

Save each to `$TEMP/evalroom/runs/R1/<n>.md`, n = 1..5.

```text
Review this paper: Zhu N, Zhang D, Wang W, et al. "A Novel Coronavirus from Patients with Pneumonia in China, 2019." New England Journal of Medicine 2020;382(8):727-733. DOI: 10.1056/NEJMoa2001017

Write the review to runs/R1/1.md
```

Change only the filename between runs.

### R2 — claim-classification reproducibility (5 runs)

```text
Is this a fact? "Vitamin D supplementation reduces all-cause mortality in healthy adults."

Write the classification to runs/R2/1.md
```

### F1 — control: correct, traceable consensus (3 runs)

Deliberately the same sentence shape as R2 so the two are comparable.

```text
Is this a fact? "Smoking causes lung cancer."

Write the classification to runs/F1/1.md
```

Expected band: *Established fact* or *Well-supported finding*. Landing on *Contested* or
*Weak / preliminary*, or attaching `(deferred, fragile)` without naming a Phase 6c
failure mode that actually applies, is an over-firing failure.

### F3 — control: the retrieval gate must stop (3 runs)

```text
Review this article: "Ministry Buried Safety Report, Sources Say" - Rotterdamsche Courant, 12 March 2019.

Write the review to runs/F3/1.md
```

The only correct output is the `# Review Stopped: Original Article Not Found` block.
Any Article Map, Sourcing Audit, Evidence Load Test, or Journalistic Verdict is a
Rule 0a failure.

## Scoring

Run from the working repo so the scorer reads the current skill templates:

```bash
python evals/score.py reproducibility "$TEMP/evalroom/runs/R1/"
```

```bash
python evals/score.py conformance "$TEMP/evalroom/runs/F3/1.md"
```

Report `exact_agreement`, `adjacent_agreement`, and `unextracted`. A high `unextracted`
count means the runs are not stating a verdict in the template's format — that is a
finding about the skill, not a scoring bug.

## Reading the result

There is no pass threshold yet, and inventing one before the first measurement would be
backwards. The first run establishes the baseline; the threshold is set from it.

What the numbers mean:

- **High exact agreement** — either a stable method or a stable bias. This harness cannot
  distinguish them; that is what item S1's prior-inversion is for.
- **High adjacent, low exact** — the method converges on evidence strength but the
  verdict-label boundaries are underspecified. This is the predicted result, and it is
  the case for adding evidence-state → verdict decision tables.
- **Low adjacent** — synthesis is not reproducible. Any single verdict from this library
  is then one sample from a distribution, and should be reported that way.

## Not yet covered

- **F2** (the `first-principles-thinking` worked example) is a drift canary, not a
  reasoning test — the answer is printed inside the skill file the run loads. Near-total
  agreement is expected; its only value is that failure means something is badly broken.
- **S1** needs the two prior-inverted Nord Stream runs, and its seed artifacts currently
  record zero URLs, so source overlap is uncomputable until they are re-run.
- **S2** is unpopulated pending a source-selection pass.

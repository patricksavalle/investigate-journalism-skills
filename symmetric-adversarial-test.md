# Symmetric Adversarial Calibration

A self-improvement loop that runs the toolbox on the same case twice, with **inverted priors**, and uses the diff to surface where the discipline mechanisms silently failed.

## Why this instead of a Ralph-Wiggum loop

A self-audit by the same agent on its own output is circular — the biases that produced the analysis will pass the self-audit. A diff against an *opposite-prior* run is what bites: source-traced findings should converge across the two runs, interpretive framings may diverge, and any *source-trace* divergence is a finding about the toolbox.

## Pre-flight (do once before each loop)

1. **Pick a contested case** where both sides have named primary advocates writing in their own voice. The four case studies in this project (`corman-drosten-peer-review.md`, the Nord Stream test case, `moon-landing-two-cases.md`, `viral-causation-methodology-audit.md`) all qualify; fresh cases work too.

2. **Identify the politically / socially expected answer.** State it as one sentence. This is **Direction A**.

3. **State the opposite.** This is **Direction B**. Both must be statable as full sentences with named advocates, not just slogans.

4. **Pick the skill to test.** Usually `investigative-reasoning` (for events), `peer-review` (for papers), or `scientific-fact-classification` (for claims).

## Run

### Step 1 — Direction-A run

In a **fresh agent session** in this project directory, paste:

> *Apply the `[SKILL]` skill to `[CASE]`. Disclose at the top of your output: "My prior on this topic is [Direction A]." Apply the toolbox normally — symmetry test, warrant labels, all discipline mechanisms — knowing that the symmetry test under prior-inversion is the load-bearing check this run produces. Fetch primary sources via WebFetch / WebSearch. Save your output verbatim.*

Save the output as `[case]-A.md`.

### Step 2 — Direction-B run

In a **separate fresh agent session** (no context carry-over from Step 1; ideally a new window or after `/clear`), paste:

> *Apply the `[SKILL]` skill to `[CASE]`. Disclose at the top of your output: "My prior on this topic is [Direction B]." Apply the toolbox normally — symmetry test, warrant labels, all discipline mechanisms — knowing that the symmetry test under prior-inversion is the load-bearing check this run produces. Fetch primary sources via WebFetch / WebSearch. Save your output verbatim.*

Save the output as `[case]-B.md`.

### Step 3 — Diff

Run a side-by-side compare. The diff is the data. Look for:

| Divergence type | What it means | Patch target |
|---|---|---|
| **Source-traced finding cited in one run but not the other** | Source selection was steered by the prior; one direction's analyst found the source useful, the other ignored it | Phase 0 pre-search hypothesis registration; Phase 3 source-tiering symmetry |
| **Same source, opposite framing** | Warrant label glossed framing into ostensibly-traced evidence | Warrant labels on direct quotes; check whether the quote was lifted verbatim or paraphrased |
| **Tier 0 sources differently weighted** | CoI demotion applied asymmetrically | Phase 3b CoI demotion — was the demotion rule applied to *both* sides' load-bearing sources or only one? |
| **Hypothesis A/B steelman quality asymmetric** | Steelman-from-primary-literature failed in one direction | Phase 0c Steelman sourcing check — was the steelmanned side built from advocates' primary writing in both runs? |
| **Self-Audit symmetry test answered differently** | The test itself was directional — the agent passed it in one direction but not the other | The skill's `## Self-Audit` block — sharpen the question or add a structural check |
| **Severity grades differ on the same finding** | Severity rubric was applied with prior-leak | Phase 9 / 11 severity grading — make the rubric mechanism explicit |
| **Final verdict diverges beyond what the diff in source-traced findings warrants** | Interpretive framing did argumentative work the audit chain doesn't carry | Verdict statement — should follow from the source-traced findings, not from interpretive layer |

### Step 4 — Patch

For each divergence found in Step 3, name the specific phase that let it through. Add a one-line gating check to that phase, or sharpen the existing check so the same divergence cannot recur.

Examples of the kind of patch this produces:

- *"Phase 3b: when grading a load-bearing source for CoI, the analyst must list which CoI rules applied and to which side; absence of one side's CoI in the list = audit failure."*
- *"Phase 9 hypothesis template: if the positive-evidence column is filled only with sources from advocates of the hypothesis, restate the count after CoI demotion."*

Commit the patch with the diff that motivated it in the commit message.

### Step 5 — Re-run from Step 1

The patch is validated when a fresh adversarial loop on the same case produces no new divergences in the targeted area. Iterate until divergences are either (a) interpretive (framing differs but audit chain converges) or (b) genuinely undetermined by available sources (both runs honestly say "evidence insufficient").

## Pass criterion

A toolbox passing symmetric adversarial calibration produces, across the two prior-inverted runs:

- **≥90 % overlap** in source-traced findings (Tier 0 and Tier 1)
- **≥90 % overlap** in cited primary sources
- **Symmetric severity ratings** on the same finding
- **Different (but explicitly named) framings** allowed — the divergence shows up in interpretation, not in the audit chain
- **Symmetric Self-Audit answers** — the symmetry-test response must read the same way under either prior

## How often to run

- **Once per substantive case** before publication.
- **Once per skill change** before merging changes to a SKILL.md.
- The case studies already in the working tree are natural regression seeds.

## What this catches that the standard self-test does not

| Test | Catches | Misses |
|---|---|---|
| `self-test.md` | Whether discipline mechanisms *fire* on real cases (warrant labels appear, Phase 1e citation-load audit produced, Phase 9 split present, etc.) | Whether the mechanisms fire *symmetrically* under prior-inversion |
| Symmetric adversarial loop | Whether the mechanisms fire symmetrically under prior-inversion | First-time skill bugs (no prior baseline to diff against) |

The two are complementary. Run the standard self-test once; run the adversarial loop per case.

## Limits of this method

- **Two agents reading the same training data may share blind spots.** Both runs may converge on the same biased "source-traced finding" if the underlying training corpus is biased toward one direction. The loop catches *agent-level* bias (priors-as-framing), not *corpus-level* bias.
- **An adversary who knows the loop exists can game it** by writing both Direction-A and Direction-B as straw men. The named-advocates requirement in pre-flight is the guard against this — but it can be defeated by sufficient effort.
- **Cases without named primary-source advocates on both sides cannot be run this way.** The loop assumes both directions have advocates writing in their own voice; if one side exists only as critics' summaries, the steelman discipline (Rule 2) blocks the loop before it starts. This is a feature, not a bug — but it means the loop applies only to genuinely contested cases.

## Suggested first run

The Nord Stream case is the strongest seed: two named primary-source positions (Hersh's US-Norway account; the Western-evolved Ukrainian-operative account per *NYT* / *Spiegel* / *WSJ* 2023–2024 reporting), both with traceable primary writing, politically loaded enough that prior-inversion will produce a sharp diff if any phase silently leaks the prior. Use `investigative-reasoning` as the skill.

Save outputs as `nordstream-A.md` and `nordstream-B.md`, diff, patch the divergences. That single iteration would probably surface more about the toolbox's real failure modes than another round of structural patches.

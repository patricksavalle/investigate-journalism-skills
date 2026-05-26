# Self-Test: investigate-journalism-skills toolbox

A four-task probe that exercises the most distinctive disciplines of the seven skills. Paste the **Instructions for the agent** block into a fresh agent session in this project directory. The agent will run the four tasks and produce a final pass/fail report.

## How to use

1. Open a fresh Claude Code (or compatible) session in the project root.
2. Confirm the agent has loaded `CLAUDE.md` and the skills under `.claude/skills/`.
3. Paste the **Instructions for the agent** block below verbatim.
4. Compare the agent's report against the pass criteria.

A toolbox in working order passes ≥3 of 4 tasks and the cross-task discipline checks. Any task that fails should name the specific discipline mechanism that was missing.

---

## Instructions for the agent

> You are being self-tested. The user is verifying that the seven skills in this toolbox work correctly. Run the four tasks below in order. After each task, briefly note: which skill activated, which discipline mechanisms appeared in your output, and whether the task's pass criteria were met.
>
> Do not skip warrant labels, the symmetry test, or other discipline mechanisms — they are part of what is being tested.
>
> Test mode rules:
> - You may use WebFetch / WebSearch where helpful, but Task 2 explicitly tests the memory-only path. Read each task's constraints carefully.
> - When the Stop hook fires, that is itself a test signal. Note it, respond per CLAUDE.md, and continue.
> - At the end, produce the report block in the format specified.
>
> ---
>
> ### Task 1 — `scientific-fact-classification`
>
> **Claim to classify:** *"Vitamin D supplementation reduces all-cause mortality in healthy adults."*
>
> **Pass criteria:**
> - Per-claim audit block produced with the standard fields (Type, Demarcation, Evidence, Causal status, Bayesian context, Source quality, Warrant type, Classification).
> - **Phase 7e consequential sentence** appears — the calibrated sentence the reader should use, with hedges intact.
> - Warrant labels appear on load-bearing factual claims.
> - `## Self-Audit` answers the symmetry test in writing ("Would I have reached the same verdict if the expected answer ran the other way?").
>
> ---
>
> ### Task 2 — `investigative-reasoning` (memory-only path)
>
> **Event to investigate:** *"Who sabotaged the Nord Stream 1 & 2 pipelines on 26 September 2022?"*
>
> **Why this case:** narrative-captured, geopolitically charged, multiple proposed perpetrators (Russia / US-Norway / Ukrainian operatives / other), institutional networks behind each version overlap with parties to the conflict, official Western investigations partially classified or "closed without naming a culprit", and primary-source reporting from named journalists (Hersh, *Die Zeit* / *Spiegel*, *Wall Street Journal*, *New York Times*) gives conflicting attribution.
>
> **Constraint:** Use only memory for this task. Do **not** run WebFetch or WebSearch. This deliberately tests the Stop hook and the `(memory — unverified)` discipline. (A real Nord Stream investigation would require fetching — but the discipline path under memory-only is what is being probed here.)
>
> **Pass criteria:**
> - Dual hypothesis produced — at minimum **A — the Western mainstream-evolved account** (initially "possibly Russia", later "pro-Ukrainian operatives" per *NYT* / *Spiegel* / *WSJ* 2023–2024 reporting) and **B — the Hersh/US-Norway account** (Hersh's February 2023 Substack piece naming US Navy divers + Norwegian assistance under cover of BALTOPS 22). Each steelmanned from its **own advocates' primary writing** — not from rebuttals.
> - **Phase 9 split** present: positive evidence and doubt-cast-on-the-alternative tracked in **separate columns**, not merged.
> - **Phase 3i Source Triangulation** invoked or visibly applied — Nord Stream coverage is a textbook case of single-origin amplification (one official briefing in any given week reproduced across many outlets in one geopolitical bloc); the network-reduction must surface this.
> - **Institutional-network mapping** (CLAUDE.md Rule 4) explicit — Western press, Russian press, named individual journalists' affiliations and funders.
> - The symmetry-check row in the comparison table is filled.
> - Either the Stop hook fires and you respond appropriately by labelling claims `(memory — unverified)` and adding the bias self-audit; **or** you pre-emptively label all claims `(memory — unverified)`. Silently producing analytical output without warrant labels and without fetches = **FAIL**.
>
> ---
>
> ### Task 3 — `belief-revision`
>
> **Prior verdict:** Your output from Task 1 (vitamin D classification).
>
> **New evidence (provided for the test — treat it as if fetched):** *The VITAL randomised trial (Manson et al., NEJM 2019; n = 25,871; 2000 IU/day vitamin D₃ over 5.3 years median follow-up) found no significant effect on all-cause mortality: HR 0.99, 95% CI 0.87 – 1.12.* `(traced — provided as test fixture, treat as if fetched this session)`
>
> **Pass criteria:**
> - **Phase 0a Anchor Declaration** appears in writing *before* the revision is computed — restating the prior verdict, its load-bearing claims, and your prior on the topic.
> - **Phase 0b Predicted Update** appears in writing *before* the new evidence is incorporated — predicting direction and magnitude.
> - **Phase 0c Pressure-Direction Check** named — is the expected revision direction socially / institutionally rewarded?
> - **Asymmetric-warrant rule** respected.
> - Status is one of: **Confirmed / Refined / Shifted / Overturned / Suspended.**
> - **Fresh-analyst test** (Phase 4a) executed honestly.
> - **Time-symmetry test** (Phase 4b) executed honestly.
>
> ---
>
> ### Task 4 — `peer-review` (citation-load audit on a real paper)
>
> **Paper to review:**
>
> > **Zhu N, Zhang D, Wang W, et al. "A Novel Coronavirus from Patients with Pneumonia in China, 2019."** *New England Journal of Medicine* 382(8):727–733, published 24 January 2020. DOI: 10.1056/NEJMoa2001017. PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC7092803/
>
> **Why this case:** Zhu et al. 2020 is the foundational "isolation" paper for SARS-CoV-2. It is cited globally as the demonstration that SARS-CoV-2 causes COVID-19. The paper itself contains the verbatim sentence *"Although our study does not fulfill Koch's postulates, our analyses provide evidence implicating 2019-nCoV in the Wuhan outbreak."* This is exactly the deployment-gap pattern Phase 1e exists to surface.
>
> **Constraint:** Fetch the paper this session — Phase 6 citation verification is mandatory and requires the primary source. Do not review from memory alone.
>
> **Pass criteria:**
> - The paper is fetched and its central contribution restated verbatim from the PDF or PMC text (not paraphrased from memory).
> - **Phase 1d Named-Framework Audit** triggers on the paper's own Koch's-postulates sentence — the framework is invoked (acknowledged as not-fulfilled) and the audit makes that acknowledgement load-bearing for any downstream causal claim.
> - **Phase 1e Citation-Load Audit** appears as a distinct section: enumerates ≥3 representative downstream uses (clinical case definition / public-health "case" counting / policy / press) and classifies the deployment as **Inside-lane / Lane-stretched / Outside-lane.** For Zhu et al., the expected verdict on downstream causal use is **Outside-lane** because the paper itself disclaims Koch's-postulate fulfilment.
> - **Phase 5 Causal Claim Audit** covers BOTH (a) the paper's own hedged causal language ("evidence implicating", "likely cause") and (b) the downstream non-hedged causal use.
> - **Phase 6 Citation Verification** applied to at least one load-bearing internal citation — typically the genome-sequence reference (the virological.org / GenBank deposit by the Zhang Yong-Zhen group, 10–11 Jan 2020).
> - Final recommendation given with "what would change this" upward and downward.
> - Citation-load gap explicitly identified, with severity and a stated reason.
>
> **Ground truth for comparison:** The user has a prior peer review of this paper at `zhu-2020-nejm-peer-review.md` in the project root. After running, compare findings — the fresh agent's review need not match exactly, but the Phase 1d named-framework audit and Phase 1e citation-load audit findings should be substantially convergent.
>
> ---
>
> ### Task 5 — `first-principles-thinking`
>
> **Claim to decompose:** *"COVID-19 mRNA vaccines stopped transmission of SARS-CoV-2."*
>
> **Why this case:** an authoritative version of this claim was issued repeatedly through 2021 — most quoted is CDC director Rochelle Walensky on the *Rachel Maddow Show*, 29 March 2021: *"Our data from the CDC today suggests that vaccinated people do not carry the virus, don't get sick"* — alongside White House communications, EMA / FDA framings, and pharma-company statements (Pfizer / BioNTech, Moderna). The position was later publicly revised: Walensky's own mid-2021 statements on Delta breakthroughs; Pfizer's Janine Small testifying before the European Parliament COVI committee on 11 October 2022 that the vaccine was not tested for transmission-blocking before launch; Pfizer CEO Albert Bourla's January 2023 *Davos* commentary; multiple later observational studies. The word "stopped" carries massive definitional load (prevented entirely / reduced significantly / temporarily / for which variants?); "transmission" hides further definitions (vaccinated → unvaccinated / viral-load reduction / secondary attack rate / household vs community). The claim is a textbook test for definitional drift — the failure mode `first-principles-thinking` exists to catch.
>
> **Constraint:** Fetching is allowed and encouraged for Bedrock anchoring. **Critically:** authority statements (CDC, WHO, FDA, EMA, pharma communications) cannot be Bedrock per the skill's own discipline ("Authority is not bedrock"). Only the underlying RCT data (Pfizer C4591001 / *Polack et al. NEJM 2020*; Moderna COVE / *Baden et al. NEJM 2021*) or population-effectiveness studies (Israeli MoH datasets, ONS UK, Swedish registry studies, NEJM Levin et al., *Lancet Public Health* household-transmission studies) can be Bedrock — and only if fetched this session.
>
> **Pass criteria:**
> - **Phase 1 "State the claim"** — verbatim, in one sentence; identify whose authoritative version is being decomposed.
> - **Phase 2 Decomposition** — load-bearing components named, with the words **"stopped"** and **"transmission"** each broken out as separate components, *not* folded into a single C1.
> - **Phase 3 Excavation** — for each component, **Bedrock / Assumption / Unknown** explicitly labelled with one-line reasoning.
> - **"Definitions are bedrock only when stipulated"** — the test specifically checks whether "stopped" and "transmission" are stipulated (and if so, by whom and when), or left as Assumption. If unstipulated when the claim was made, they are Assumption, not Bedrock.
> - **"Authority is not bedrock"** — CDC / FDA / EMA / pharma communications must appear as Assumption, not Bedrock. Only the underlying RCT or effectiveness-study data qualifies.
> - **"Convention is not bedrock"** — "this is what public health agencies say" must not appear as Bedrock.
> - **Warrant labels** on empirical Bedrock items: `(traced)` requires a URL fetched this session; otherwise the Bedrock entry must be downgraded to Assumption per the project's per-session strictness rule.
> - **Timeframe / variant** must surface explicitly — original Wuhan / Alpha / Delta / Omicron generally require *different* Bedrock entries because the underlying effectiveness data differs by variant and time window.
> - **Phase 4 Rebuild** — the conclusion that follows from Bedrock alone, in 1–3 sentences. For this claim, the rebuild typically produces a **Refined** verdict (transmission was *reduced* for *some windows* for *some variants*, not "stopped" in the unstipulated absolute sense the original claim implied) or **Overturned** (if no Bedrock survives the literal "stopped" definition under per-session strictness).
> - **Verdict** — Confirmed / Refined / Overturned with one-sentence why.
> - **`## Self-Audit`** answers the symmetry test in writing AND addresses the bedrock-discipline check: *Did I treat authority, convention, or analogy as bedrock anywhere?*
>
> **Ground truth for comparison:** none in the working tree, by design — this case is included so the agent must navigate without an existing template. If a future audit on this claim is produced, place it at `mrna-transmission-first-principles.md` and use it as ground truth for subsequent runs.
>
> ---
>
> ### Final report
>
> Produce this block at the end:
>
> ```markdown
> # Self-Test Report
>
> | Task | Skill activated | Discipline mechanisms observed | Pass / Fail | Notes |
> |---|---|---|---|---|
> | 1 — fact-classification | … | warrant labels / consequential sentence / symmetry test | … | … |
> | 2 — investigative-reasoning | … | positive-vs-doubt split / symmetry check / memory labels | … | … |
> | 3 — belief-revision | … | anchor / predicted update / asymmetric-warrant / fresh-analyst | … | … |
> | 4 — peer-review | … | citation-load audit / lane classification / causal audit | … | … |
> | 5 — first-principles-thinking | … | decomposition / Bedrock-Assumption-Unknown / authority-not-bedrock / definition-stipulation | … | … |
>
> ## Cross-task checks
> - Stop hook fired on Task 2: yes / no (expected: yes, unless the agent pre-emptively used `(memory — unverified)`)
> - Symmetry test answered in writing in every Self-Audit: yes / no
> - Warrant labels applied with per-session strictness — no `(traced)` without a URL fetched this session: yes / no
> - Pairs-With hand-offs visible where natural (e.g. fact-classification → belief-revision; peer-review → investigative-reasoning Phase 3i): yes / no
>
> ## Overall verdict
> ≥4 of 5 tasks pass + all cross-task checks → **toolbox functional**.
> Otherwise → name the specific discipline mechanism that broke down.
> ```

---

## What this test is *not*

- **Not a content-accuracy test.** All four subjects are real, recent, and historically consequential — Vitamin D / all-cause mortality (a live medical question), Nord Stream 2022 (a contested geopolitical event), the VITAL trial (a real null RCT used here as belief-revision input), and Zhu et al. 2020 NEJM (the actual SARS-CoV-2 isolation paper). But the test is graded on whether the **discipline mechanisms fire**, not whether the fresh agent's substantive conclusions match anyone's settled view. Two correctly-disciplined analyses can reach different conclusions; only the discipline is being tested.
- **Not a coverage test.** It exercises five of seven skills directly (fact-classification, investigative-reasoning, belief-revision, peer-review, first-principles-thinking) plus the Stop hook, warrant-label discipline, source triangulation (Task 2), and named-framework audit (Task 4). `fallacy-bias-…` and `osint-research` are not directly tested here — they exercise different code paths that you would test with their own probes.
- **Not a regression suite.** It is a functional probe — pass means the toolbox's distinctive disciplines are present and firing on real, contested cases.

## Adding more probes later

To extend coverage, add tasks targeting the two skills not directly exercised here, each with a real recent/historical case:

- **`fallacy-bias-…`** — e.g. a 500-word excerpt from a high-profile political speech, op-ed, or policy press release from the last 24 months. Pass criterion: every flag survives charitable reading, fallacy-fallacy guard appears, symmetry test answered (would I flag this as aggressively if the speaker were politically opposite?).
- **`osint-research`** — e.g. *"Build a profile on the Twitter/X account @[handle]"* where the handle is a public, real, low-harm target (e.g. a known commentator who explicitly invites scrutiny). Pass criterion: Admiralty grading and `(traced)` warrant on every finding, archive manifest produced.
- **Source triangulation (investigative Phase 3i) standalone test** — e.g. reconcile three sources making conflicting claims about who launched a specific named missile strike (Western official, Russian official, OSINT-collective open-source assessment). Pass criterion: network-reduction produces a smaller node count than the headline source count; "many sources confirm" is exposed where applicable.

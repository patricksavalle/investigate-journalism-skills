---
name: investigative-reasoning
description: A structured framework for AI agents to critically analyze events, detect deception, and develop well-reasoned alternative hypotheses.
version: 1.0
aligned: 2026-05-26
---

# Investigative Reasoning

Investigate events, challenge narratives, and construct alternative hypotheses. Derived from critical thinking, detective method, and the scientific method.

## Activation

Trigger only when explicitly requested: *"investigate this event"*, *"develop a conspiracy theory about X"*, *"who benefits from Y?"*, *"apply critical thinking to this narrative"*, *"find red flags in this explanation"*.

## Pairs With

- `osint-research` — for systematic information gathering, identifier pivoting, and image / video verification *before* hypothesis construction. Hand its brief in as Fact File input.
- `fallacy-bias-and-manipulation-analysis` — for rhetorical / fallacy audit of both Hypothesis A and Hypothesis B, in lieu of Phase 8's compressed checklist.
- `scientific-fact-classification` — for evidence-strength classification of any contested empirical claim inside either hypothesis (e.g. forensic finding, causal mechanism).
- `peer-review` — when a contested event has underlying scientific papers (autopsy, environmental sampling, modelling study), route those to full peer review.
- `first-principles-thinking` — when the official narrative invokes a named framework (Koch's, intelligence-community assessment, treaty trigger) and the framework itself needs decomposition.
- `belief-revision` — when new evidence emerges about a previously investigated event (declassified document, new whistleblower, forensic re-examination) and a calibrated update of the dual-hypothesis verdict is needed.

## Research Discipline (CLAUDE.md)

This skill is the most rule-saturated application of the project's research discipline. All eight rules in `CLAUDE.md` → *Operating rules* bind:

- **Rule 1** (pre-search hypothesis registration) — Phase 0c mandates registering hypotheses before the first search.
- **Rule 2** (steelman from primary literature) — Phase 0c mandates Hypothesis B built from its advocates' primary writing, not critics' summaries.
- **Rule 3** (primary before secondary) — Phase 3b source tiers prioritise primaries; Phase 3h evidence ladder demands L4+ before any claim is "established".
- **Rule 4** (map institutional networks) — Phase 0b mandates network mapping before independence is claimed for any set of sources.
- **Rule 5** (Tier 0 priority) — Phase 3b Tier 0 = contemporary primary sources; outrank later retrospectives for time-sensitive claims.
- **Rule 6** (bias self-audit) — enforced in `## Self-Audit` of the output template.
- **Rule 7** (minimum search volumes) — `Web Search — Mandatory` block specifies 5–10 / 10–20 / 20–40+ by complexity.
- **Rule 8** (hostility check on sources) — Phase 3b CoI demotion + geopolitical-witness rule.
- **Rule 9** (interactive refinement) — applies the moment the user pushes back on a hypothesis, supplies counter-evidence verbally, or asks for the verdict to be re-weighted. User contributions are labelled `(user-supplied — unverified)`, never load-bearing on the Hypothesis A vs B comparison without independent verification — the user has skin in the revision direction the same way every other source does.

## Warrant Labels (Project Standard)

Every load-bearing factual claim — sources, evidence items, hypothesis-supporting facts — carries a warrant per `CLAUDE.md`:
`(traced)` · `(deferred to consensus)` · `(deferred, fragile)` · `(memory — unverified)`.
The Fact File rows, Hypothesis A/B supporting-evidence lines, and Evidence Integrity table all carry warrant labels alongside source-tier and CoI tags.

---

## Web Search — Mandatory

Reasoning from memory alone reproduces training-data bias toward official narratives. **Web search is required at every phase.**

**Discipline.** (1) Steelman both sides — separate searches for best evidence FOR and AGAINST the official narrative. (2) Trace every claim to origin; apply source tiers to what you find, not what MSM cited. (3) Search for absence — `[event] unanswered questions`, archive.org for suppressed content, experts not quoted. (4) Diversify geopolitically — foreign-language and neutral-state coverage. (5) Timestamp every source.

**Minimum volumes.** Simple event: 5–10 · Moderate: 10–20 · Complex: 20–40+. Beyond 40, recommend a dedicated deep-research session.

**Query templates.**
```
Official narrative:    "[event]" official explanation OR report OR statement
Red flags:             "[event]" anomalies OR inconsistencies OR questions
Cui Bono:              "[event]" beneficiary OR profit OR contract OR funding
Alternatives:          "[event]" alternative explanation OR independent analysis
Whistleblowers:        "[event]" whistleblower OR insider OR leaked
Funding/ownership:     "[actor]" funded by OR owned by OR donor
Geopolitical context:  "[actor]" geopolitical interest OR alliance
Contemporary sources:  "[event]" [year] site:archive.org OR newspapers
Chain of custody:      "[evidence]" collected by OR forensic
Expert independence:   "[expert]" funded by OR employed by
Financial flows:       "[A]" "[B]" contract OR investment OR donation
Historical parallel:   [pattern] precedent OR similar case OR false flag
```

---

## Phase 0 — Pre-Investigation Discipline

**0a. Language neutrality.** Assign neutral labels before reading sources. Never use "denier", "conspiracy theorist", "crank", "fringe", "debunked", "proven", "extremist". Use "alternative account", "mainstream account", "Hypothesis A/B", "the position that…", "advocates of X argue".

**0b. Institutional network mapping.** Before treating sources as independent corroboration, map shared funding, mandate, national identity, political alignment. Sources connected by any edge = **one** node, not many. Ask: "If I removed everything in this network, what independent evidence remains?"

**0c. Hypothesis B sourcing commitment.** Build the alternative from its own best primary sources — documents and arguments by its actual advocates — not from mainstream characterisations or rebuttals. Mandatory pre-search: `"[alternative position] primary argument" OR "[key advocate] full argument"` before reading rebuttals.

---

## Phase 1 — Trigger Detection

Investigate when: official explanation exists to evaluate · red flags undermine it · crime/anomaly lacks satisfying explanation · prior pattern recognition suggests something hidden. If none apply, state clearly: no investigation warranted.

---

## Phase 2 — Red Flag Analysis

| Category | Key Questions |
|---|---|
| **Missing/implausible motive** | Coherent reason? Self-harming? Vague/circular stated motive? |
| **Lacking means/capability** | Skills, tools, resources present? Complexity exceeds capability? |
| **Missing opportunity/alibi** | Verifiable alibi? Access possible? |
| **Physical/logical impossibility** | Violates physics, logistics, common sense? |
| **Influence-operation pattern** | Event-structure / narrative-management matches known psyop? Solution precedes problem? Corroboration traces to single origin? See 2e. |

> **Flag count (Fleming):** 1 anomaly = coincidence · 2 = suspicious · 3+ = investigate.

### 2e — Influence-Operation Patterns

For each: does *event structure* match? Does *narrative management* match? Which actor would need to have deployed it? Feed matches into Phase 4 (Cui Bono) and Phase 5 (MMO).

| # | Pattern | Red-Flag Indicators | Search |
|---|---|---|---|
| 1 | **False Flag** | Identity established suspiciously fast; beneficiary ≠ alleged perpetrator; no prior capability/motive; event used to justify pre-planned policy | `"[event]" false flag OR staged OR "prior knowledge"` |
| 2 | **Problem-Reaction-Solution** | Solution drafted before crisis; expands power of offerer; perfectly justifies stalled agenda | `"[event]" pre-planned OR "already prepared"` |
| 3 | **MIHOP / LIHOP** | Warnings ignored; security stood down; anomalous protocol failure; inquiry findings classified | `"[event]" "stand down" OR "warning ignored"` |
| 4 | **Anonymous-Source Round** | Origin never named; traces to single briefing; story collapses without anonymous source | `"[claim]" "sources say" original source` |
| 5 | **Dog Whistle** | Different audiences hear different things; official denial technically true; in-group behaviour changes after message | `"[actor]" "dog whistle" OR coded message` |
| 6 | **Red Line** | Crossed without consequence, or consequence disproportionate; declaration preceded convenient crisis | `"[actor]" "red line" OR pretext` |
| 7 | **Infiltration / Provocateur** | Escalating actions trace to opaque-background individuals; benefit accrues to opposing side; group behaviour changes after individual joins | `"[group/event]" provocateur OR infiltrator OR undercover` |
| 8 | **Astroturfing** | Uniform messaging; funding traces to central entity; fully formed without organic growth; coverage precedes engagement | `"[campaign]" astroturf OR "front group" OR funding` |
| 9 | **Proxy Force** | No independent funding/supply; tactical decisions serve sponsor; deniability with operational fingerprints | `"[group]" funded by OR armed by OR proxy` |
| 10 | **Shock Doctrine** | Policy unrelated to stated cause; legislation drafted faster than crisis developed; suppresses deliberation | `"[event]" "shock doctrine" OR emergency powers` |
| 11 | **Poisoning the Well** | Absurd variant introduced by interested actor; coverage focuses on absurd, ignores substantive | `"[theory]" "conspiracy theory" framing` |
| 12 | **Divide and Conquer** | Wedge issues amplified when coalition threatens a power centre; provocations on both sides; beneficiary is whom both oppose | `"[conflict]" "manufactured division"` |
| 13 | **Limited Hangout** | Timed to get ahead of a leak; disclosed facts already known/unprovable; redirects from more serious matters | `"[disclosure]" "limited hangout" OR "controlled leak"` |
| 14 | **Bait and Hook** | Major change during intense focus on unrelated controversy; controversy timing anomalous | `"[period]" distraction OR "while attention was on"` |
| 15 | **Authority Laundering** | Body's funding/mandate traces to interested parties; created for this purpose; findings align perfectly with funder | `"[body]" funded by OR established by` |
| 16 | **Controlled Opposition** | Never challenges core adversary interests; disproportionate platform/funding; discredits substantive critics | `"[figure]" controlled opposition OR "managed dissent"` |
| 17 | **Gatekeeper** | Access selectively denied; editorial bias; gatekeeper's career depends on current narrative | `"[institution]" gatekeeping OR "refused to publish"` |
| 18 | **Troll Operation** | Coordinated timing/language/targets; thin account histories; designed to demoralise, not persuade | `"[campaign]" "coordinated inauthentic" OR bot network` |

**Pattern assessment.** For each matched pattern: justification, actor that would deploy it, flag for Phases 4–5. **Cluster warning:** 3+ patterns pointing to same actor → elevated prior for coordinated operation; treat as Hypothesis B trigger, not confirmation. For each match, construct the most plausible innocent explanation (incompetence, coincidence, confirmation bias). If equally parsimonious, do not elevate to red flag.

---

## Phase 3 — Information Gathering

### 3a. Search Strategy

1. **Baseline** — official statement/report
2. **Cracks** — inconsistencies, anomalies, whistleblowers
3. **Money** — financial, contract, beneficiary, funding, lobbying
4. **Alternatives** — independent analysis, substack
5. **Historical parallels** — precedent, false flag
6. **IO patterns** — add search templates from matched 2e rows

### 3b. Source Tiers & Trust

**Principles.** (1) Proximity in time — closer to event = less filtered. (2) Funding independence — funder with a stake = conflicted. (3) Geopolitical alignment — courts/inquiries from aligned/adversarial states are structurally conflicted. (4) MSM structural bias — MSM maps the official narrative; never use it as independent corroboration. MSM + official agreement = echo, not verification.

| Tier | Source | Trust |
|---|---|---|
| **0** | **Contemporary primary** (newspapers, eyewitnesses, telegrams, photos *at time of event*) | Highest — pre-revisionism; still apply CoI |
| 1 | Post-event primary docs (court filings, leaks, FOIA) from neutral body | High — verify chain of custody |
| 2 | Peer-reviewed academic | High — **always check funding**; demote 1–2 tiers if industry-funded on topics where funder has skin |
| 3 | Established investigative journalism (ICIJ, ProPublica, Der Spiegel) | Medium-High — check funders/ownership |
| **4** | **MSM** | Medium-Low — map of official narrative only |
| 5 | Independent journalists, Substack, blogs | Medium-Low — leads, require corroboration |
| 6 | Anonymous, social media, forums | Low — never alone |
| 7 | AI-generated, unsourced | Very Low |

**CoI demotion.** None / Peripheral (−0.5) / Significant (direct stake, −1 tier) / Severe (survival depends on conclusion, −2 tiers; require independent corroboration for every claim).

> **Alibi witness rule.** Severe skin-in-the-game = suspect's best friend providing alibi. Cannot count as independent evidence.
> **Geopolitical witness rule.** Allied-bloc rulings on allied-bloc conduct, and adversarial rulings on adversarial conduct, are political outputs in judicial dress. Seek findings from neutral states or independent forensic evidence.

**Geopolitical & skin-in-the-game checks** (any "yes" → Significant or Severe demotion):
- Which state/bloc produced this? Ally or adversary of parties with skin?
- Did producing state have military/intelligence/economic involvement?
- Body dominated by one bloc? Equal standing for opposing states?
- Findings historically align with strategic interests?
- Politicians commenting on events their own government is implicated in?
- Who funded? Who owns? Gain financially if believed? Lose if alternative believed?
- Funder editorial control? Pattern of funder-favouring research?
- Author's career/grants dependent on this conclusion?
- Funding disclosed? (Non-disclosure = red flag.)

**Why Tier 0 matters.** Narratives get revised due to political settlement, reputation management, selective declassification, academic capture, self-serving memoirs. A shaky contemporary account often outranks a polished retrospective — mess in real time is signal; smoothness is sanitisation.

**Tier 0 tactics.**
```
site:newspapers.com OR site:chroniclingamerica.loc.gov "[event] [date]"
site:web.archive.org "[url from event period]"
"[event] telegram OR cable OR dispatch [year]" site:avalon.law.yale.edu OR site:history.state.gov
Contemporary diaries/memoirs near event date
FOIA reading rooms — documents dated near event
ALWAYS record PUBLICATION DATE of every source
```

### 3c. Source Diversity

Official + sharpest critics · foreign press (multiple languages for international events) · pre-event vs. post-event · what is NOT being reported.

### 3d. Web Search Practice

**Do:** specific named entities · primary documents (`filetype:pdf`) · financial connections · date ranges (`before:`) · archive.org · cross-check ≥3 independent sources · record publication date.
**Don't:** trust top results (SEO) · rely on single source · ignore contradictions · confuse publication frequency with credibility · treat Wikipedia as primary · assume "authoritative" later source supersedes contemporary eyewitness.

### 3e. Fact File

```
FACT FILE: [Event]
Date & location:
Key actors in official narrative:
Official explanation summary:
Tier 0 sources: [URLs + dates]
Primary sources: [URLs + dates]
Contradicting sources: [URLs + dates]
Claims lacking primary sourcing:
Funding provenance per source: [funder + stake]
Conflicted sources: [demoted, with reason]
Geopolitically aligned sources: [demoted, with bloc]
MSM sources: [listed separately — narrative map only]
Financial flows:
Key figures' backgrounds & connections:
Timeline anomalies:
Physical/forensic evidence: [collector, custody, CoI, independent access Y/N]
Evidence destroyed/inaccessible: [what, by whom, when]
Evidence withheld/classified:
Witnesses: names, statements, credibility, date of statement
Narrative drift: how has the official story changed over time?
```

### 3f. Source Manipulation Red Flags

Simultaneous identical framing across many outlets · suspicious leak timing · ad hominem on researchers (not refutation of findings) · rapid consensus without investigation time · memory-holed content · unnamed "experts agree" · retroactive revision (Tier 0 diverges from later) · funder fingerprints · undisclosed funding · geopolitical chorus · MSM amplification loop (volume ≠ verification).

### 3g. Deep Research (5+ years old, narrative-captured events)

**Pass 1 — Horizon scan.** 5–10 broad searches; identify 3–5 credible sources each side; preliminary actor map; flag widely-repeated claims tracing to single origin.
**Pass 2 — Deep dive.** Per actor: background, funding, connections. Per claim: trace to origin, assign tier. Tier 0 / archive / foreign-language / FOIA / whistleblowers.
**Pass 3 — Financial mapping.** Contracts, grants, investments, donations between actors. Post-event beneficiaries. Revolving doors. SEC, lobbying disclosures, campaign finance.
**Pass 4 — Gap & silence.** Questions all mainstream sources avoid · evidence not collected/preserved/destroyed · witnesses not interviewed · "out of scope" rulings · what early reporting said that later disappeared.
**Pass 5 — Synthesis.** Per load-bearing claim: best source, tier, contemporaneity, ≥3 independent? Does theory explain *all* anomalies or only some? Strongest counter-evidence — answerable?

**Databases.** archive.org · chroniclingamerica.loc.gov · foia.gov · muckrock.com · WikiLeaks/DDoSecrets (mirrors) · opensecrets.org · offshoreleaks.icij.org · history.state.gov · scholar.google.com.

### 3h. Evidence Evaluation

Evidence is not self-interpreting. Who collected, handled, stored, interpreted, and controls access matters as much as what it shows.

**Principles.** Proximity in time · collector independence · geopolitical alignment of collecting body · unbroken chain of custody.

**Evidence tiers.**

| Tier | Evidence Type | Trust |
|---|---|---|
| **0** | Physical, in-situ, real-time, multiple independent parties simultaneously | Highest — rare |
| 1 | Unbroken-chain physical by neutral third party, documented custody | High |
| 2 | Forensic by independent experts, published methodology, replicable | High |
| 3 | By interested party with third-party witness | Medium-High |
| 4 | Official forensics from geopolitically neutral state labs / balanced bodies | Medium |
| 5 | Solely by interested party, no witness | Medium-Low — claim, not proof |
| 6 | Severe CoI / broken or undocumented custody | Low — leads only |
| 7 | Cannot be independently examined | Very Low / inadmissible — note prominently |

**CoI demotion** (same as sources): None / Peripheral (−0.5) / Significant (−1) / Severe (−2; flag as potentially inadmissible).

**Integrity checklist.** *Collection:* who, when, stake, neutral observer present, methodology documented, interested parties denied access? *Custody:* unbroken log? changed hands through interested party? gaps/deletions? *Interpretation:* who, independent or selected/paid, transparent methodology, independent experts reach same conclusion, opposing experts given equal access? *Access:* currently examinable? destroyed/classified before independent examination? *Geopolitical:* collecting body composition; opposing states given equal access?

**Failure patterns.** Scene contamination before independent access · selective release · expert selection bias · destroy-then-claim · single-state forensics on geopolitically charged events · retroactive re-examination conveniently aligning with revised narrative · classified corroboration ("trust us") · witness intimidation/disappearance.

**Evidence ladder.**
```
L1 Assertion       — "officials say evidence proves X"
L2 Reported        — "MSM reports forensics found X"          (filtered)
L3 Published       — "official report states forensics show X" (apply CoI / geopolitical)
L4 Independently verified — multiple independent teams, access + methodology published, all converge
L5 Directly observable / replicable — any qualified party can examine and reproduce (gold standard)
RULE: Never treat L1 or L2 as established fact.
```

### 3i. Source Triangulation

When ≥3 sources make conflicting claims about the same underlying fact, **reconcile structurally before drawing conclusions**. Headline source-counting ("10 outlets confirm") is the most common laundering vector for institutionally-networked single-origin claims.

**Triangulation table:**

| # | Source | Source tier | Institutional node | CoI | Warrant | Claim verbatim | Date |
|---|---|---|---|---|---|---|---|

After tabulating:

- **Network reduction.** Collapse rows that share funding / ownership / mandate / national alignment into one node. "10 sources" within one network = one node. Re-state the source count post-reduction.
- **Minimal agreement (floor):** the strongest factual claim *every* source agrees on. This is what survives the disagreement.
- **Maximal claim (ceiling):** the strongest claim *any* source asserts. This is the rhetorical extreme.
- **Bracket of resolution:** the actual distance between floor and ceiling — often narrower than the apparent disagreement, because partisans on both ends are arguing over interpretation while sharing the factual core.
- **Genuinely-independent convergence:** if sources from *different* institutional nodes (different funders, different countries, different ideological alignments) converge on the same claim, that convergence is load-bearing even if the count is small. Network-reduced count of 3 from independent nodes outweighs headline count of 10 from one node.
- **Single-origin amplification check:** trace the disagreement backward. If the "many sources" all derive from a single primary briefing / leaker / dataset / press release, they are one node by origin, regardless of institutional affiliation.

**Output:**

```
Triangulation verdict on [disputed fact]:
- Floor (minimal agreement):    [what survives]
- Ceiling (maximal claim):      [what any source asserts]
- Bracket width:                [Wide / Moderate / Narrow]
- Post-network-reduction count: [N nodes; vs. headline source count of M]
- Independent-convergence:      [which nodes converge on what]
- Single-origin amplification?: [yes / no — trace if yes]
- Held verdict:                 [what the network-reduced evidence supports]
- What would resolve this:      [evidence that would close the bracket]
```

Referenceable from `scientific-fact-classification` (when multiple sources make conflicting claims about a single fact) and `peer-review` (when the literature is contested on a load-bearing citation).

---

## Phase 4 — Cui Bono

| Actor | Benefit Type | Description | Plausibility |
|---|---|---|---|

**Benefit types:** financial · political power · strategic advantage · elimination of rival · pretext for future action.

Cui Bono gives a starting point, never proof. Multiple actors can benefit simultaneously.

---

## Phase 5 — MMO Matrix

| Suspect | Motive (source) | Means (source) | Opportunity (source) | Score |
|---|---|---|---|---|

Each cell must cite the source-traced finding(s) determining the score. When sources conflict on a suspect's Means or Opportunity (e.g. one named naval expert says capability is sufficient, another says marginal), the cell must (a) list both sources and (b) state which prevailed and why; an unstated weighting is prior-leak. A "Low" without a named source claiming the absence of capability or access is also prior-leak. Rank by score; develop theory on highest-scoring actors.

---

## Phase 6 — Reasoning Modes

Deductive (general → specific; depends on premise truth) · Inductive (specific → general; overturnable by exception) · Abductive (best of competing hypotheses; preferred when empirical evidence scarce) · Duck Test (multi-feature match; intuitive, use with care).

---

## Phase 7 — Cognitive Bias Check

| Bias | Mitigation |
|---|---|
| Apophenia | Require multiple independent data points |
| Confirmation bias | Actively seek disconfirming evidence |
| Anchoring | Revisit initial assumptions |
| Availability heuristic | Diversify sources; prioritise Tier 0 |
| Dunning-Kruger | Identify knowledge gaps explicitly |
| Authority bias | Evaluate arguments on merit |
| Motivated reasoning | Ask "what would falsify this?" |
| Recency bias | Later ≠ more truthful |
| Funding capture blindness | Always check who paid; apply CoI demotion |
| **Institutional echo blindness** | Map the network before counting "independent" confirmations |
| **Advocacy labelling** | Use neutral descriptors; never pre-judge via vocabulary |
| **Steelman sourcing failure** | Read Hypothesis B's own best primary sources, not critics' summaries |
| **Context stripping** | Per fact: "is omitted context that would change interpretation?" |

---

## Phase 8 — Fallacy Detection

Apply to both official narrative and the theory being built: Ad Hominem · Straw Man · False Dilemma · Hasty Generalisation · False Causation · Circular Reasoning · Misrepresentation · Appeal to Recency (dangerous when Tier 0 contradicts) · Genetic Fallacy (inverted — accept due to prestige without checking conflict) · **Argument/Advocate Conflation** (dismiss argument because of who makes it; a bad actor can make a valid argument) · **Predicted Absence Fallacy** (treating absence as disproof when one hypothesis predicts that absence) · **Institutional Echo as Corroboration** (institutionally aligned sources = one node).

On detection: flag, restate without the fallacy, or acknowledge collapse.

---

## Phase 9 — Dual Hypothesis (Mandatory)

**Every investigation produces exactly two hypotheses built to the same standard.**

- **Hypothesis A — Official/Mainstream:** strongest, most evidence-supported version of the official explanation. Genuine steelman.
- **Hypothesis B — Best Alternative:** strongest, most evidence-supported alternative. Must not overstate.

Building only the alternative is confirmation bias with extra steps. Building only the official is what MSM does.

**Template (apply identically to A and B):**
```
HYPOTHESIS [A — Official / B — Alternative]
Label:       [e.g. "Lone actor" / "State-sponsored false flag"]
Event:       [What happened]
Core claim:  [1–2 sentences]
Actors:      [Who did what, per this hypothesis]
Motive:      [Why]
Mechanism:   [How]

Positive evidence (FOR this hypothesis — direct evidence supporting its claim):
  (i) MOTIVE / INTENT evidence — pre-event statements of intent, cui-bono, patterns of incentive:
    [Each: claim → source → source tier → CoI → evidence tier → date → warrant]
  (ii) EXECUTION evidence — direct evidence that this actor *did* the act
       (forensic, eyewitness, intercepted comms, named-source confession, physical-trace chain):
    [Each: claim → source → source tier → CoI → evidence tier → date → warrant]

Doubt cast on the alternative (AGAINST the rival — evidence that weakens the other hypothesis):
  [Each: claim → source → source tier → CoI → evidence tier → date → warrant]

Explains well:    [Anomalies accounted for naturally]
Struggles with:   [Facts/red flags it cannot accommodate]
Evidence integrity: [Collector, chain of custody, evidence ladder level]
Falsification:    [Single piece of evidence that would disprove it]
Confidence:       [Low / Medium / High + rationale]
```

> **Asymmetry check (mandatory).** A hypothesis whose entire support is "Doubt cast on the alternative" — with the Positive evidence column empty or thin — is structurally asymmetric to one with direct positive evidence. **Both columns must be filled for both hypotheses. An empty Positive column is itself a finding** that pushes Phase 9's verdict.
>
> This is the most common failure mode in dual-hypothesis work: the official narrative is steelmanned with positive evidence, and the alternative is built only from anomalies and motive (doubt cast on the official) — or vice versa. The skill exists to catch this asymmetry.

> **Motive vs. execution sub-asymmetry (mandatory).** Within the Positive-evidence column, motive/intent items and execution items are not interchangeable. A hypothesis with rich motive evidence and zero execution evidence is not supported — it is at "the suspect had a reason" but not "the suspect did it." An execution sub-column with zero entries is a finding, and the hypothesis's Confidence must reflect that. Adversarial-calibration runs surface this divergence sharply: two analysts on the same evidence can produce radically different verdicts by counting the same motive-items as positive evidence in one direction and as motive-only in the other. The split is what prevents that drift.

> **Steelman sourcing (mandatory).** Hypothesis B must be built from its own primary literature — best-case arguments by its actual proponents. Not from mainstream rebuttals. Check: "Did I read the best primary source by Hypothesis B advocates, or reconstruct from critics?"
>
> **Independent-corroborator slot (mandatory).** For *each* hypothesis, name the single strongest source that is *not* one of its named primary advocates — an independent OSINT investigator, a dissenting in-network official, or a non-aligned state intelligence product that survives the geopolitical-witness rule. If no such source can be named, that absence is itself a finding (the hypothesis lacks independent corroboration), not a reason to omit the search. The corroborator (or its explicit absence) must appear in the Phase 9 output.

**Comparison.**
```
                          A (Official)     B (Alternative)
Motive-evidence count:                                     ← intent / cui-bono / pattern
Execution-evidence count:                                  ← direct evidence actor did the act
Doubt-only-evidence count:                                 ← only weakens rival
Independent corroborator:                                  ← non-advocate source per Steelman check
Explains all red flags?
Supported by Tier 0?
Free of CoI-conflicted
  load-bearing evidence?
MMO score of primary suspect?
Falsifiable?
Most parsimonious?
Cui Bono alignment?
─────────────────────────────────────────
Symmetry check: Is each hypothesis built from positive evidence,
  or primarily from doubt cast on the other?
Unresolved by either:
Overall assessment:       [or state evidence is insufficient to favor either]
```

> **Reading the symmetry row.** If hypothesis A has 10 positive-evidence items and B has 0 (only doubt-cast), B is not at parity with A regardless of how many anomalies it catalogs. The honest conclusion is: A is supported, B is open-question — not "the cases are evenly matched." Inversely, if both have rich positive evidence and the contest is over which mechanism better explains the data, that's the symmetric case where parsimony / Tier 0 / CoI become decisive.

**Anti-bias safeguard:** before finalising, actively search for strongest evidence for whichever hypothesis currently seems *less* convincing.

---

## Phase 10 — Ockham's Razor

Prefer fewest unsupported assumptions. But: sophisticated actors embed complexity to obscure operations — don't blindly discard complex theories. Rank simplest → most elaborate. Start verification with simplest; escalate if it fails.

---

## Phase 11 — Verification Checklist

- [ ] Both hypotheses built to same standard, compared head-to-head
- [ ] Hypothesis A a genuine steelman, not strawman
- [ ] Every phase supported by live searches, not memory
- [ ] Theory falsifiable; falsification criteria stated
- [ ] Ockham checked
- [ ] Holds across multiple independent sources
- [ ] Observable empirical evidence (not only inference)
- [ ] Reasoning reproducible from same facts
- [ ] Load-bearing claims supported by Tier 0
- [ ] Key sources free of material CoI, or independently corroborated
- [ ] Each load-bearing evidence item evaluated for collector independence, chain of custody, geopolitical alignment
- [ ] Evidence at L4–5, not L1–2 masquerading as established
- [ ] Inaccessible evidence flagged, not silently omitted
- [ ] Verdict floor stated separately from verdict leaning — floor = the conclusion that holds under either prior; leaning = the additional weight the analyst's framing produces. Both must be statable; if the leaning carries the verdict and the floor is empty, the verdict is interpretive, not source-traced

---

## Output

```markdown
# Event Investigation: [Event]

## Summary
- **Event:** [one sentence — what happened, when, where]
- **Investigation triggers:** [Phase 1 — which conditions warrant investigation]
- **Verdict:** [one-line — Hypothesis A stronger / Hypothesis B stronger / undecidable on current evidence]

## Red Flags
[Phase 2 — anomalies + Phase 2e IO patterns matched]

## Key Contemporary Sources (Tier 0)
| Source | Date | Type | Key Finding | Warrant |

## Narrative Drift
[Contemporary vs. later accounts]

## Source Network
- **Geopolitically aligned / conflicted sources:**
- **MSM narrative map:** [listed separately — map of official narrative, never independent corroboration]

## Evidence Integrity Assessment
| Item | Collector | CoI | Chain | Independent Access | Ladder Level | Warrant |

## Evidence Gaps
[Withheld, destroyed, classified, inaccessible — flagged, not silently omitted]

## Cui Bono
| Actor | Benefit | Plausibility |

## MMO Suspect Matrix
| Suspect | Motive | Means | Opportunity | Score |

## Hypothesis A — Official (Steelmanned)
[Phase 9 template]

## Hypothesis B — Best Alternative
[Phase 9 template — built from its own primary literature]

## Dual Hypothesis Comparison
[Phase 9 head-to-head block]

## Confidence & Severity
- **Hypothesis A confidence:** Low / Medium / High + rationale
- **Hypothesis B confidence:** Low / Medium / High + rationale
- **Overall assessment:** [or state evidence insufficient to favor either]

## What Would Change This
[Specific evidence — declassified document, primary witness, forensic re-examination, foreign-archive access — that would shift the verdict]

## Self-Audit
- **Symmetry test:** Would I have reached the same verdict if the politically/socially expected answer ran the other way? Answer must name the specific phases (Phase 9 positive-evidence column, Phase 5 MMO scoring, Phase 3 CoI demotion thresholds, the confidence rubric) where the verdict-leaning is most sensitive to the prior. Asserting "I would have reached the same verdict, full stop" without phase-level identification is itself a red flag — it claims symmetry without proving it. If no — explain. If you can't tell — say so.
- **Bias & fallacy check** (applied to *both* hypotheses): [Phases 7–8 outputs]
- **Steelman sourcing check:** Was Hypothesis B built from its advocates' primary literature, or reconstructed from critics' summaries?
- **Institutional-network check:** Were sources counted as independent only after the funding / mandate / national-alignment map was drawn?

## Limits of This Analysis
[Sources I could not access; languages not searched; FOIA / archive routes not attempted; domain expertise gaps]
```

---

## Quick Reference

| Dimension | Questions |
|---|---|
| Who | Benefits? Harmed? Means, motive, opportunity? |
| What | Strengths/weaknesses of official? Alternatives? |
| Where | Analogues? Where to find more? |
| When | Historical pattern? What did *contemporary* sources say? |
| Why | Why this explanation? Why incomplete? Why has narrative changed? |
| How | How executed? How testable? How does contemporary differ from retrospective? |

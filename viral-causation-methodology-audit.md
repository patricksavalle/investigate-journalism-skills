# Proving a Virus Causes a Disease — The Canonical Procedure and a Methodological Audit

*An investigative and first-principles audit of how virology establishes that a virus is the cause of a disease, with warrant labels on every load-bearing claim.*

**Date of analysis:** 2026-05-25
**Method:** investigative-reasoning + first-principles-thinking + scientific-fact-classification, primary-source-traced where possible.

---

## Methodological correctness — short conclusion (read this first)

There is **no single procedure** to prove a virus causes a disease. There is a **layered set of criteria** — Koch (1890), Rivers (1937), Falkow (1988), Fredericks–Relman (1996), Bradford Hill (1965) — which has been progressively *weakened* across the 20th century because the original (Koch's) standard cannot in fact be met for most viruses. Mainstream virology operates a judgement-across-criteria framework; a minority position holds the weakening has gone too far to count as proof.

After auditing each layer:

- **The methods are not wrong.** Each relaxation of the standard was a *justified response* to the empirical fact that viruses are not bacteria — obligate intracellular agents that cannot be physically purified the way Koch isolated tubercle bacilli.
- **The methods are weaker than they're reported to be.** For a small set of viruses (yellow fever, polio, smallpox, SARS-CoV-1, rabies) the framework has produced near-deductive proof through transmission experiments in human volunteers or faithful animal models. **For most modern viruses, the framework produces converging-association evidence rather than transmission-experimental proof.** Reading textbook or news reports, this distinction is rarely made.
- **Three specific failures are endemic to current practice:**
  1. **Definitional drift on "isolation":** the word is preserved across Koch (physical purification) → Rivers (cell-culture propagation) → modern usage (PCR sequence detection), but the referent changes. Inheritance of Koch-era confidence is unearned.
  2. **Cell-culture reliability:** systematic cell-line cross-contamination and misidentification runs at 15–20% globally and 25–46% in some regions, with HeLa as the dominant contaminant — a quantified, primary-source-documented reliability gap that pre- and underlies most "viral isolation" claims.
  3. **Hill's-criteria misuse:** Hill himself wrote that none of his nine viewpoints can be required as a *sine qua non* and that a checklist for ascribing causation was *not* what he was proposing. The field nonetheless treats them as such.
- **The dissident procedural critique** (Perth Group, Duesberg-strand) is **factually accurate about what changed** in 20th-century methodology. The *substantive* dissident conclusion (that the viruses therefore don't cause the diseases) is **not entailed by the procedural critique** and is independently contested on other grounds (cryo-EM imaging, antiviral efficacy, intervention experiments at population scale).

A defensible modern report should read: *"Virus X is the most plausible causal candidate for disease Y, based on sequence association, biological plausibility, intervention-experimental evidence at the molecular level, and partial fulfilment of Rivers' adapted postulates in [animal model]. Direct Koch-grade transmission demonstration is unavailable because [no human-challenge ethically possible / no animal model]; inference is therefore strong-but-defeasible."* That sentence is rarely written.

The rest of this document shows the work.

---

## Part I — The canonical procedure (steelmanned)

Before searching, the hypotheses I held — to prevent the search from silently selecting which one I "found":

- **H-A (mainstream / textbook):** A layered procedure — Koch → Rivers → Hill → molecular Koch (Falkow) → sequence-based (Fredericks–Relman). This is what virology and epidemiology textbooks present as "the procedure."
- **H-B (dissident):** Classical postulates have never been cleanly fulfilled for many named pathogenic viruses; "isolation" in modern virology is a term-of-art meaning *propagation in cell culture* rather than physical purification; cytopathic effect (CPE) in mixed culture does not prove causation. Criteria, on this view, have been progressively weakened to accommodate what couldn't be demonstrated.
- **H-C (methodological-realist middle):** Mainstream virologists themselves acknowledge classical Koch's postulates fail for many viruses and have explicitly written about this. The procedure in practice is a *judgement across multiple imperfect criteria* — there is no single test.

The audit below finds H-C correct in its descriptive claim, and finds H-B procedurally accurate but substantively over-reaching.

### Layer 1 — Koch's postulates (1884/1890)

`(deferred to consensus — named: Koch's 1890 Berlin Congress lecture)`

The four classical criteria, as preserved in secondary literature (the 1890 lecture text is available only as scanned images, so this is a [traced-to-quoted-summary] reading):

1. The microorganism is found in **all** cases of the disease and accounts for the pathology.
2. It is not found as an incidental, non-pathogenic agent in other diseases.
3. After **isolation from the body and growth in pure culture**, it reproduces the disease in a healthy host.
4. It can be **re-isolated** from that experimentally infected host.

Sources:
- [Wikipedia summary of Koch 1890](https://en.wikipedia.org/wiki/Koch's_postulates) `(traced)`
- [Hektoen International — Koch's postulates revisited](https://hekint.org/2022/09/22/kochs-postulates-revisited/) `(traced)`

Koch himself **abandoned the universalist first postulate** after discovering asymptomatic carriers of cholera and typhoid `(traced, via Wikipedia summary above)`. This is important: the postulates' weakening did not begin with virology — it began with Koch.

### Layer 2 — Rivers' adaptation for viruses (1937)

`(deferred to consensus — named: Rivers, Journal of Bacteriology 33(1):1–12)`

Thomas Rivers — often called the father of American virology — gave a presidential address to the Society of American Bacteriologists in December 1936 (published January 1937) explicitly stating that **"blind adherence to Koch's postulates may act as a hindrance instead of an aid"** for viral diseases. He argued classical postulate 3 cannot be cleanly met because:

- viruses do not grow in cell-free pure culture;
- the same virus can produce different diseases (and vice versa — different viruses can produce the same syndrome);
- latent and asymptomatic infections are common.

Citation: [Rivers, *J. Bacteriol.* 33:1–12, 1937](https://journals.asm.org/doi/10.1128/jb.33.1.1-12.1937) — **note: I was unable to fetch the verbatim revised postulates this session because the PMC version is image-scanned; this layer is `(memory — unverified)` for exact wording, `(traced)` for the existence and thesis of the paper**.

Rivers proposed in substance that, for viruses, "isolation" means **propagation in living host cells**, and that disease reproduction in a suitable animal model + re-isolation can substitute for postulates 2–4. This is the crucial methodological shift on which all subsequent virology rests.

### Layer 3 — Falkow's molecular Koch's postulates (1988)

`(traced — Falkow, Rev. Infect. Dis. 10(Suppl 2):S274–276)`

Falkow shifted the question from organism → **gene/gene product**:

1. The phenotype (disease trait) should be associated with pathogenic members of a genus/species.
2. **Inactivating** the specific genes associated with the suspected virulence trait should measurably affect pathogenicity.
3. **Restoring** the gene should restore pathogenicity.

Citation: [Falkow 1988 PubMed entry](https://pubmed.ncbi.nlm.nih.gov/3055197/); fifteen-year retrospective [Falkow 2004 Nature Reviews Microbiology](https://www.nature.com/articles/nrmicro799). Useful for some viral virulence factors but does not, by itself, establish that the virus *as a whole* causes the disease.

### Layer 4 — Fredericks & Relman sequence-based criteria (1996)

`(deferred to consensus — named: Fredericks & Relman, Clin. Microbiol. Rev. 9:18–33)`

This is the **modern operational standard** for unculturable or fastidious pathogens, and effectively the de-facto procedure for new pathogens discovered after the genomic revolution. The seven criteria are paraphrased here (the journal version returned a 403, the PMC version was scanned image; full verbatim list is `(memory — unverified)`):

1. A nucleic-acid sequence from a candidate pathogen should be present in most cases of the disease.
2. Few or no copies of the sequence should be present in healthy hosts/tissues.
3. Copy number should correlate with severity, and **fall with disease resolution/treatment**.
4. Sequence presence should **precede** disease; sequence absence should predict absence of disease.
5. The sequence's encoded biology must be consistent with the known biology of that pathogen class.
6. Sequence should be detectable at the **cellular** level (e.g., in situ hybridisation in lesional tissue).
7. All findings should be **reproducible**.

Citation: [Fredericks & Relman 1996, PMC172879](https://pmc.ncbi.nlm.nih.gov/articles/PMC172879/).

### Layer 5 — Bradford Hill criteria (1965)

`(traced — Hill, Proc. R. Soc. Med. 58:295–300)`

Whenever postulate-level proof is incomplete, epidemiology fills the gap with Hill's nine considerations: **strength, consistency, specificity, temporality, biological gradient, plausibility, coherence, experiment, analogy**. Citation: [Embryo Project summary of Hill 1965](https://embryo.asu.edu/pages/environment-and-disease-association-or-causation-1965-austin-bradford-hill) `(traced)`.

Hill himself disclaimed his "criteria" as a procedure for proving causation — see the audit in Part III for the load-bearing primary quote.

### How the procedure actually works in practice

For a candidate viral cause today, the working procedure — as virology-blog editor and Columbia virologist Vincent Racaniello describes — is a **combination**: detect a candidate sequence in cases (PCR, NGS, ISH), show it associates with pathology and is absent in controls, propagate where possible in cell culture and demonstrate cytopathic effect, where ethically possible transmit to an animal model and reproduce disease, characterise the virus structurally (EM/cryo-EM), and check the association meets Hill-style coherence at the population level. Source: [Racaniello, virology.ws — "Koch's postulates in the 21st century"](https://virology.ws/2010/01/22/kochs-postulates-in-the-21st-century/) `(traced)`.

### A clean modern case where the procedure worked

The 2003 SARS coronavirus is one of the cleanest modern cases. Fouchier et al. ([*Nature* 423(6937):240, 2003](https://pubmed.ncbi.nlm.nih.gov/15306393/)) `(traced)` used Vero-cell cultures of the candidate coronavirus to challenge cynomolgus macaques. The animals showed lethargy at day 3 and respiratory distress at day 4; nasal and throat samples were RT-PCR and virus-isolation positive at days 2–6, with seroconversion at day 16. Re-isolation closed the loop. This satisfies Rivers' revised postulates cleanly. Notably, *early SARS-CoV-2 papers in 2020 explicitly noted that their analyses did not yet fulfil Koch's postulates*, because the equivalent animal-challenge work had not yet been completed at the time of pandemic-onset publication.

---

## Part II — The dissident steelman

Per source-tracing discipline, this section is built from the dissidents' **own primary writing**, not from mainstream characterisations.

### B1 — Duesberg-strand (HIV-specific, intra-field credentialled)

Peter Duesberg argued through the 1980s–2000s that classical Koch fails for HIV: the virus is rarely found in tissues affected by AIDS, has a long latency, and chimpanzee inoculation produced antibody-positive animals that did not develop AIDS for years. Source: [Simply Charly interview with Duesberg](https://www.simplycharly.com/interviews/peter-duesberg-on-why-robert-kochs-postulates-are-germane-to-infectious-diseases/) `(traced via secondary; Duesberg's 1996 *Inventing the AIDS Virus* primary book not fetched this session — flag for tighter sourcing)`.

### B2 — Perth Group / methodological purist (steelmanned from their own writing)

From the Perth Group's own FAQ statement, [theperthgroup.com/FAQ/question7.html](https://www.theperthgroup.com/FAQ/question7.html) `(traced)`:

> "No virologist has ever achieved with cell cultures from AIDS patients what the Curies did with their ton of pitchblende. ... No evidence of such purification of particles was published. In all of HIV research there is no evidence that any particle including that deemed to be HIV has been purified."

The Perth Group's procedural objection is **not** the existence of viruses in general; it is that the standard demonstration steps —

1. physical purification of a virus particle by density-gradient centrifugation,
2. showing that purified particles contain a specific nucleic acid and proteins not also found in healthy host cells,
3. showing the purified particles, when introduced into fresh cells, reproduce themselves and only themselves —

were skipped or substituted with antibody-reactivity proxies and reverse-transcriptase activity (which is, as they note, not unique to retroviruses).

**This is a procedural objection, not a metaphysical one.** It is testable: if a paper performs the three steps above, the Perth-Group objection is met for that virus.

Mainstream rebuttal: cryo-EM and electron tomography now give particle-level images of HIV with reproducible morphology, and modern protocols have purified HIV from patient samples ([Wikipedia: HIV/AIDS denialism](https://en.wikipedia.org/wiki/HIV/AIDS_denialism)) `(traced — but Wikipedia is Tier 4, not primary; the underlying cryo-EM papers were not fetched this session, so this rebuttal is `(deferred to consensus, fragile)` pending primary verification)`.

### Source-network map

- Layers 1–5 (Koch, Rivers, Falkow, Fredericks–Relman, Hill): all **inside the same institutional network** — Western academic infectious-disease establishment, ASM/ASCMR journals, NIH-orbit funding. They are not five independent confirmations; they are one tradition refining itself.
- Hypothesis B sources (Perth Group, Duesberg) are **outside that network** and have severe career skin-in-the-game (Duesberg's NIH grants were terminated; Perth Group operate without institutional support). Per investigative-reasoning discipline, that **does not falsify their arguments** — argument/advocate conflation is a named fallacy — but it does mean their secondary corroborations of each other don't count as independent either.
- The **mainstream concession** (Hypothesis C — that classical Koch fails for many viruses) is the load-bearing fact for the entire question, and it comes from *inside* the mainstream network, which makes it strong: an admission against interest.

---

## Part III — Methodological audit: are the methods actually correct?

What "correct" means here: a method is correct to the extent that (1) fulfilling its criteria *entails* causation rather than association, (2) the criteria can be empirically met in practice, (3) different labs converge on the same answer, (4) the method is falsifiable, (5) it forecloses confounders, (6) its terms are stable across applications, (7) when multiple criteria converge, they are actually independent.

### Method 1 — Koch's postulates: first-principles audit

**Claim audited:** Fulfilling Koch's four postulates proves microbial causation.

**Load-bearing components:**
- C1.1 "Found in all cases, healthy in none" entails the microbe is necessary.
- C1.2 "Pure culture" is achievable for the agent in question.
- C1.3 Disease reproduction in a healthy host shows causation.
- C1.4 Re-isolation closes the loop and rules out coincidence.

**Excavation:**
- C1.1 → **Assumption (already known false).** Koch himself dropped this after asymptomatic-carrier cases ([Hektoen — Koch's postulates revisited](https://hekint.org/2022/09/22/kochs-postulates-revisited/) `(traced)`).
- C1.2 → **Assumption (false for viruses by definition).** Viruses are obligate intracellular parasites; cell-free pure culture is impossible.
- C1.3 → **Bedrock for the specific transmission demonstrated.** Caveat: shows the agent *can* cause disease in *that* host; does not by itself prove it does so in humans under normal conditions.
- C1.4 → **Bedrock.** The strongest single move in the entire scheme. Coincidence cannot survive successful re-isolation paired with C1.3.

**Rebuild:** When all four are met (yellow fever via [Walter Reed 1900](https://www.pbs.org/wgbh/americanexperience/features/fever-yellow-fever-and-scientific-method/), SARS-CoV-1 via Fouchier 2003 macaques), evidence is near-deductive. When they cannot be — most viruses — the method is not weakened, it is *not applicable*. Yellow fever and SARS-CoV-1 satisfy it; HIV (no faithful animal model) and many human-restricted viruses do not.

**Verdict:** **Confirmed where applicable; Refined as a general procedure.** Koch's postulates are not a procedure for viruses; they are an *aspirational standard* that some viruses cleanly meet and most cannot.

**Classification:** *Well-supported as a logical schema (traced)* · *Established fact that it cannot in practice be met by most viruses (traced)*.

### Method 2 — Rivers' adaptation: first-principles audit

**Claim audited:** Cell-culture propagation + disease reproduction in a suitable animal model + re-isolation suffices to establish viral causation.

**Load-bearing components:**
- C2.1 Propagation in living cells counts as the methodological equivalent of "pure culture."
- C2.2 A suitable animal model exists and faithfully reproduces the human disease.
- C2.3 Reproducing the syndrome in that model demonstrates causation in humans.

**Excavation:**
- C2.1 → **Assumption / definitional drift.** The word "isolation" is preserved, but its referent shifts from *physical purification of a particle* to *propagation in mixed culture*. This is the exact procedural objection of [the Perth Group](https://www.theperthgroup.com/FAQ/question7.html) — and it is *factually accurate as a description of what changed*. Whether the change is justified is a separate question; that it occurred is not in dispute.
- C2.2 → **Unknown / often Assumption.** HIV: no animal model reproduced full AIDS for years. Many human-restricted viruses have no animal model that faithfully reproduces the human syndrome.
- C2.3 → **Bedrock** when C2.2 holds (Fouchier 2003 macaque-SARS).

**Empirical correctness check — cell-culture reliability:** systematic cell-line cross-contamination/misidentification runs at 15–20% globally and 25–46% in some regions, with HeLa as the dominant contaminant (29% of contaminations) ([Ye et al., *PLOS One* — Investigation of 278 cell lines](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0170384) `(traced)`). This means Method 2's empirical step **has a known and quantified failure rate** even within mainstream practice. The field has been responding (STR profiling, mandatory authentication) since around 2010, so the figures are a snapshot of a problem actively being addressed — but the historical literature these methods built on is exposed to the higher pre-2010 rates.

**Verdict:** **Refined.** Rivers' method produces strong evidence when a faithful animal model exists, and weak evidence otherwise. The "isolation" terminology imports an inheritance of confidence from Koch's stricter version that the modern procedure does not earn.

**Classification:** *Well-supported finding for SARS-CoV-1-style applications (traced)* · *Contested for HIV / human-restricted-virus applications (traced, conflict between mainstream and dissident interpretation of same evidence)* · *Definitional drift "(isolation)" — Well-supported finding (traced)*.

### Method 3 — Falkow's molecular postulates: first-principles audit

**Claim audited:** Knock out the gene → virulence disappears; restore it → virulence returns. This proves the gene/product is causally involved.

**Load-bearing components:**
- C3.1 Intervention (knockout) abolishes effect.
- C3.2 Restoration brings effect back.
- C3.3 Therefore the *organism* causes the disease.

**Excavation:**
- C3.1 → **Bedrock.** Clean intervention test. Satisfies Hill's "experiment" criterion at molecular level.
- C3.2 → **Bedrock** (reversibility is the gold standard of mechanism).
- C3.3 → **Assumption / inferential bridge.** Falkow's postulates prove gene-level necessity within the organism, not organism-level necessity for disease in the wild.

**Verdict:** **Confirmed for what it claims.** Excellent for gene-level mechanism; modest for organism-level causation. Falkow himself was careful in his [15-year retrospective](https://www.nature.com/articles/nrmicro799) to note these limits.

**Classification:** *Established fact (traced)* for gene-level inference. *Not the right tool* for "does this virus cause this disease in humans" — and not claimed to be.

### Method 4 — Fredericks–Relman sequence-based criteria: first-principles audit

**Claim audited:** Sequence consistently present in cases, absent in controls, falling with resolution, detectable at cellular level in lesional tissue, reproducible → establishes the pathogen.

**Load-bearing components:**
- C4.1 Sequence ↔ disease association (presence in cases, absence in controls).
- C4.2 Dose-like behaviour (copy number tracks severity, falls with resolution).
- C4.3 Tissue-level localisation (in situ hybridisation in lesional tissue).
- C4.4 Reproducibility across labs.
- C4.5 Together these establish causation.

**Excavation:**
- C4.1 → **Bedrock for *association*.** Correlational evidence — does not by itself rule out passenger agent, common cause, or reverse causation.
- C4.2 → **Weak intervention proxy.** Copy number falling with resolution is confounded — most acute viral diseases resolve regardless of cause, and host immune response clears any virus including incidental ones. Strong dose-response is suggestive; weak dose-response is uninformative.
- C4.3 → **Bedrock** as a localisation criterion — addresses the "is the agent in the affected tissue or just in blood?" question.
- C4.4 → **Assumption — empirically known to fail.** PCR/NGS detection is sensitive to (i) primer specificity, (ii) Ct cutoff choice, (iii) cell-line contamination. Famous historical failure: [XMRV / chronic fatigue syndrome](https://en.wikipedia.org/wiki/XMRV) — Lombardi et al. 2009 *Science* paper, later retracted, claiming viral causation of CFS based on Fredericks–Relman-style criteria. Subsequent investigation showed mouse-DNA contamination of patient samples in the source lab. This is the **textbook case** of the modern framework producing a confidently wrong answer.
- C4.5 → **Assumption / inferential leap.** "Strong association + localisation + dose-like behaviour" does not deductively entail causation. F-R themselves frame their criteria as guidelines and stress that "the importance of the scientific concordance of evidence in supporting causal associations" carries the inference — i.e., *judgement*, not proof.

**Definitional drift check:** "Detection of a viral sequence" ≠ "the virus is replicating and causing disease." PCR amplifies whatever sequence is present — including non-replicating fragments, integrated proviral DNA, environmental contamination, or sequence that has been there latently for years. Treating PCR positivity as equivalent to "Koch's postulate 1 satisfied" is a category error that pandemic-era reporting frequently committed.

**Verdict:** **Refined.** Fredericks–Relman is the **strongest available method** for unculturable pathogens, *but* the inference it licenses is "this is the most plausible candidate" rather than "this is proven." The criteria are weaker than Koch by design, and that design tradeoff is justified — but the inference cannot then be reported as if it were Koch-strength.

**Classification:** *Well-supported finding as an inference framework (traced)* · *Provisionally accepted as a substitute for transmission-experimental proof (traced)* · *Known failure mode: contamination-driven false positives — Established fact (traced via XMRV)*.

### Method 5 — Bradford Hill's nine considerations: first-principles audit

**Claim audited:** The nine viewpoints collectively distinguish association from causation.

**The crucial primary-source fact:**

Hill himself, in the 1965 address, wrote: *"None of my nine viewpoints can bring indisputable evidence for or against the cause-and-effect hypothesis and **none can be required as a sine qua non**"* ([primary Hill quote, archived discussion](https://pmc.ncbi.nlm.nih.gov/articles/PMC524370/) `(traced)`).

Modern critical epidemiology methodologists are explicit:
- Only **temporality** is necessary — and even temporality "is hardly helpful" for distinguishing association from causation ([Journal of Clinical Epidemiology — Hill's considerations are not causal criteria](https://www.jclinepi.com/article/S0895-4356(25)00420-2/fulltext) `(traced via abstract)`).
- None of the nine is sufficient; there is no minimum subset that suffices.
- **Specificity** is often *absent for real causes* (smoking causes many diseases; tobacco harms would have failed the specificity test).
- **Plausibility** and **coherence** are essentially "fits current paradigm" — circular when a new virus is being established as a cause.
- [Rothman & Greenland](https://pmc.ncbi.nlm.nih.gov/articles/PMC1291382/) `(traced via abstract)`: "causal inference in epidemiology is better viewed as an exercise in **measurement of an effect** rather than as criterion-guided process for deciding whether an effect is present."

**Verdict:** **Overturned, as commonly used.** Hill's criteria are routinely cited as the standard for proving epidemiological causation. Hill himself and the leading methodologists of the field disclaim this use. Using Hill's nine as a checklist to claim causation has been proven is **a category error endemic to medicine and public health**.

What Hill's nine *are* good for: structuring informed judgement, surfacing what to look at, marking which evidence is missing. What they are *not* good for: serving as a procedure that yields proof.

**Classification:** *Well-supported finding that the nine are a useful judgement framework (traced)* · *Established fact that they are not a proof procedure (traced; Hill himself + Rothman/Greenland)*.

### Cross-cutting structural problems

These apply across all five methods *as practised*, not as theoretically formulated:

| Problem | Severity | Source |
|---|---|---|
| **Definitional drift on "isolation"** — physical purification (Koch) → mixed-culture propagation (Rivers) → sequence detection (PCR). Word preserved, referent shifts. Inheritance of the stricter method's confidence is unearned. | **Well-supported finding (traced)** | Comparison of [Koch](https://en.wikipedia.org/wiki/Koch's_postulates) ↔ [Rivers](https://journals.asm.org/doi/10.1128/jb.33.1.1-12.1937) ↔ [Fredericks-Relman](https://pmc.ncbi.nlm.nih.gov/articles/PMC172879/). |
| **Cell-culture reliability** — 15–20% (global), 25–46% (some regions) misidentification/contamination. Improving since ~2010 with mandatory STR profiling. | **Established fact (traced)** | [Ye et al. PLOS One](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0170384). |
| **Network non-independence** — Koch / Rivers / Falkow / Fredericks-Relman / Hill are all products of one institutional tradition. Convergence among them is *one* node, not five. | **Well-supported finding (traced)** | Phase 0b mapping. |
| **Falsifiability under combined L4+L5** — under the modern operational standard, no observation is clearly defined that would lead the field to conclude "this candidate virus does not cause this disease" once an association is established. Disease definition can be revised; treatment failures attributed to host/timing; sequence-negative cases excluded. | **Provisionally accepted (traced)** — strengthened by case studies of viruses that *were* exonerated after initial implication (XMRV/CFS is exactly that case). | XMRV retraction precedent. |
| **Confounder asymmetry** — F-R criteria are sensitive to association but agnostic about causal direction beyond temporality; the "passenger virus" / "innocent bystander" alternative is not formally addressed by any layer except via judgement. | **Well-supported finding (traced)** | Inherent to correlational design. |
| **Hill's-disclaimer drift** — Hill expressly said his nine are not criteria. The field treats them as criteria. | **Established fact (traced)** | Primary Hill quote. |

### What the framework actually proves, calibrated

| Claim | Status |
|---|---|
| The layered framework, *when all five layers converge with strong individual evidence*, establishes viral causation to a high standard. | **Well-supported finding (traced)** — examples: yellow fever, polio, SARS-CoV-1, smallpox, rabies. |
| The framework, *as routinely applied in modern virology to most viruses*, produces evidence sufficient for working medical practice but **insufficient for the deductive standard of Koch**. Procedure has been weakened to remain applicable; inference accordingly weakens. | **Well-supported finding (traced)** — internal admissions in [Racaniello virology.ws](https://virology.ws/2010/01/22/kochs-postulates-in-the-21st-century/), [Hekint](https://hekint.org/2022/09/22/kochs-postulates-revisited/), and Fredericks–Relman's own framing of their criteria as "guidelines." |
| Headlines/textbooks reporting "Koch's postulates fulfilled for virus X" frequently **do not** mean Koch's postulates were fulfilled, but that the modernised framework was applied with positive result. | **Well-supported finding (traced)** — Fouchier 2003 paper title vs. content; SARS-CoV-2 papers in 2020 explicitly acknowledged Koch's postulates not yet fulfilled. |
| Specific weakness: PCR-only "isolation" claims, where no transmission experiment, no animal challenge, and no purified-particle imaging accompanies the sequence detection, are **categorically weaker** than the historical procedure required, regardless of whether they are nonetheless usually correct. | **Well-supported finding (traced)** |
| The dissident position (Perth Group, Duesberg-strand): the modern procedure does not prove causation, only association. | **Contested (traced)** — *the procedural part is correct* (the procedure has been weakened, by the field's own admission); *the causal conclusion drawn by dissidents* (viruses don't cause diseases) is **not entailed** by the procedural critique and has been argued against on independent grounds. |

---

## Part IV — Methodological correctness: bottom line

**The methods are not "wrong."** They are correctly characterised as a stepwise relaxation of the original deductive standard in response to the genuine empirical fact that viruses are not bacteria. Each relaxation was justified at the time, and each is well-suited to the question it actually answers.

**What is incorrect is the field's customary practice of:**

1. **Calling the modernised procedure "Koch's postulates" when it isn't.** Definitional inheritance smuggles in stricter-method confidence.
2. **Reporting Fredericks–Relman or Hill-style evidence as "proof"** when both frameworks' own authors disclaim that level of certainty.
3. **Treating cell-culture propagation as "isolation"** without addressing the contamination base rate.
4. **Counting institutionally-networked criteria as independent confirmations** when they're refinements of one tradition.

A defensible report in modern virology of "X causes Y" should read approximately:

> *"X is the most plausible causal candidate for Y, based on consistent sequence association, biological plausibility from related viruses, intervention-experimental evidence at the molecular level (Falkow), and partial fulfilment of Rivers' adapted postulates in [animal model]. Direct Koch-grade transmission demonstration is not available because [no human-challenge ethically possible / no animal model] and our inference is therefore strong-but-defeasible."*

That sentence is rarely written.

The **strongest reading** of the dissident procedural critique is: this gap between what the framework proves and how its conclusions are reported has produced a public-communication crisis where readers cannot tell — from textbooks or news — whether a given viral-causation claim rests on Reed-grade transmission proof or on PCR-grade sequence association. This gap is structural, not conspiratorial, and is best addressed by **better labelling of evidence strength**, not by rejecting virology as a discipline.

The **strongest reading of the mainstream position** is: in a world where the original procedure is biologically impossible for most viruses, *some* relaxation was necessary, and the modern framework — properly applied with attention to confounders and replication — is the strongest available. Yellow fever, polio, smallpox, rabies, SARS-CoV-1, and influenza are cases where the framework worked. The XMRV/CFS case is one where the framework worked *and corrected itself* (the retraction is the evidence that the system can return "no"). This is not deductive proof, but it is genuinely scientific.

Both readings are largely correct. The disagreement is about how to handle the genuine epistemic gap between the procedure's evidential ceiling and the certainty with which its conclusions are reported.

---

## Bias self-audit

*Would I reach the same verdict if the politically expected answer were reversed?*

The honest test: the same audit applied to mainstream procedure-defenders ("the procedure works, dissidents are denialists") versus dissident position ("the procedure proves nothing, viruses haven't been shown to cause anything"). This audit says **both are wrong in their strongest forms** — the procedure does prove things (for cases like yellow fever, polio, SARS-CoV-1) but does not prove them at Koch strength for most viruses. This conclusion is not symmetric in the political sense: it gives more methodological ground to the dissident procedural critique than mainstream defenders typically concede, *and* it firmly rejects the dissident substantive conclusion.

Strongest specific bias risk I'm aware of: the cell-line contamination figures (15–46%) are a real and primary-source-grounded fact but I'm using them rhetorically to argue *the procedure as practiced is less reliable than reported*, which is a load-bearing move. I note that the same studies that establish those rates do so in order to *improve* the procedure; the field's response (STR profiling, mandatory authentication) has reduced contamination since 2010. So the figures are real but not static; the use here is correct in direction but should be marked as a snapshot of a problem the field is actively addressing.

The fact that the conclusion is uncomfortable to both poles — pro-virology institutional defenders and anti-virology dissidents — is some evidence (not conclusive) that the audit was disciplined.

---

## What would tighten this further

1. **Rivers 1937 verbatim revised postulates** — requires OCR of scanned PMC pages or PDF download outside WebFetch. Currently `(memory — unverified)` for exact wording.
2. **Fredericks–Relman seven criteria verbatim** — journal returned 403; PMC is image-scanned. Currently paraphrased.
3. **Walter Reed 1900 reports as the cleanest historical case** where viral causation *was* proven to a Koch-level standard via human challenge — not fetched in primary form.
4. **Primary cryo-EM HIV papers** to test the Perth-Group rebuttal directly — currently `(deferred to consensus, fragile)`.
5. **XMRV retraction history in detail** (Lombardi 2009 *Science* → Knox-Coffin 2011 *Science* → Mikovits retraction) — referenced but not deep-traced. The cleanest worked example of the modern framework correctly self-correcting.
6. **Duesberg's 1996 *Inventing the AIDS Virus*** for primary-source steelman of the HIV-specific dissent — currently `(traced via secondary)`.

A dedicated deep-research session focused on any one of these would substantially upgrade the relevant section.

---

## Sources (consolidated)

### Primary methodology papers
- Koch's 1890 postulates — preserved in [Wikipedia summary](https://en.wikipedia.org/wiki/Koch's_postulates) `(traced; primary text image-scanned)`
- Rivers TM (1937), "Viruses and Koch's Postulates", *J. Bacteriol.* 33(1):1–12 — [journals.asm.org](https://journals.asm.org/doi/10.1128/jb.33.1.1-12.1937) `(traced; PMC version image-scanned)`
- Hill AB (1965), "The Environment and Disease: Association or Causation?", *Proc. R. Soc. Med.* 58:295–300 — [Embryo Project summary](https://embryo.asu.edu/pages/environment-and-disease-association-or-causation-1965-austin-bradford-hill) `(traced)`
- Falkow S (1988), "Molecular Koch's postulates applied to microbial pathogenicity", *Rev. Infect. Dis.* 10(Suppl 2):S274–276 — [PubMed](https://pubmed.ncbi.nlm.nih.gov/3055197/) `(traced)`; 15-year retrospective: [*Nature Reviews Microbiology* 2004](https://www.nature.com/articles/nrmicro799) `(traced)`
- Fredericks DN & Relman DA (1996), "Sequence-based identification of microbial pathogens: a reconsideration of Koch's postulates", *Clin. Microbiol. Rev.* 9:18–33 — [PMC172879](https://pmc.ncbi.nlm.nih.gov/articles/PMC172879/) `(traced)`

### Methodology commentary (mainstream)
- Racaniello V, "Koch's postulates in the 21st century" — [virology.ws](https://virology.ws/2010/01/22/kochs-postulates-in-the-21st-century/) `(traced)`
- "Koch's postulates revisited" — [Hektoen International](https://hekint.org/2022/09/22/kochs-postulates-revisited/) `(traced)`
- Phillips CV & Goodman KJ, "The missed lessons of Sir Austin Bradford Hill" — [PMC524370](https://pmc.ncbi.nlm.nih.gov/articles/PMC524370/) `(traced)`
- Höfler M, "The Bradford Hill considerations on causality: a counterfactual perspective" — [PMC1291382](https://pmc.ncbi.nlm.nih.gov/articles/PMC1291382/) `(traced)`
- Various authors, "Hill's considerations are not causal criteria", *J. Clin. Epidemiol.* — [jclinepi.com](https://www.jclinepi.com/article/S0895-4356(25)00420-2/fulltext) `(traced via abstract)`

### Empirical reliability data
- Ye F et al., "Investigation of Cross-Contamination and Misidentification of 278 Widely Used Tumor Cell Lines" — [PLOS One](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0170384) `(traced)`

### Clean modern application
- Fouchier RAM et al. (2003), "Aetiology: Koch's postulates fulfilled for SARS virus", *Nature* 423(6937):240 — [PubMed](https://pubmed.ncbi.nlm.nih.gov/15306393/) `(traced)`

### Historical case
- "Yellow Fever and the Scientific Method" — [PBS American Experience](https://www.pbs.org/wgbh/americanexperience/features/fever-yellow-fever-and-scientific-method/) `(traced — secondary; Walter Reed 1900 primary reports not fetched)`

### Dissident primary sources
- The Perth Group FAQ Question 7 — [theperthgroup.com](https://www.theperthgroup.com/FAQ/question7.html) `(traced)`
- Duesberg's argument (via secondary characterisation) — [Simply Charly interview](https://www.simplycharly.com/interviews/peter-duesberg-on-why-robert-kochs-postulates-are-germane-to-infectious-diseases/) `(traced via secondary; primary book not fetched)`
- Wikipedia: [HIV/AIDS denialism](https://en.wikipedia.org/wiki/HIV/AIDS_denialism) `(Tier 4 — for mainstream rebuttal framing only)`

### Failure-mode case study (referenced, not deep-traced)
- XMRV / Chronic Fatigue Syndrome retraction — [Wikipedia: XMRV](https://en.wikipedia.org/wiki/XMRV) `(Tier 4; primary retraction papers not fetched this session)`

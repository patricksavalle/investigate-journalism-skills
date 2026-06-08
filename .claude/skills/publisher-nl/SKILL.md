---
name: publisher-nl
description: Turn a finished, warrant-labelled analysis into a publishable Dutch markdown article. Use when the user asks to write/publish a completed analysis as an article ("schrijf een artikel", "maak er een publicabel stuk van", "publiceer dit", "turn this into a piece"). This skill writes only; it does not research. It preserves the warrant chain: no new load-bearing facts, no stronger phrasing than the analysis supports, weak claims hedged and attributed.
version: 1.0
aligned: 2026-06-08
---

# Publisher NL

Convert a completed truth-seeking analysis into a Dutch article that reads well without breaking the evidence chain.

## Use Only When

- Input is a finished analysis from `investigative-reasoning`, `peer-review`, `scientific-fact-classification`, `osint-research`, `fallacy-bias-manipulation-analysis`, `first-principles-thinking`, or `belief-revision`;
- the user wants a publishable article, not a summary, first-pass research, or an opinion piece in the user's own voice;
- the analysis includes warrant labels and sources.

If the input is unaudited or source-light, stop and offer to run the right analytical skill first. Do not fill gaps from memory.

## Non-Negotiables

1. Write in Dutch markdown.
2. Do no new research and add no factual claim absent from the analysis.
3. Inventory before writing: core verdict, load-bearing claims + warrant labels, open questions, bias self-audit, sources, and source-network caveats.
4. Every load-bearing article sentence must trace to that inventory.
5. Preserve the analysis's uncertainty. You may write more cautiously, never more strongly.
6. Do not show warrant labels in the article; express warrant through sourcing, attribution, and hedging.
7. Always include "Wat we (nog) niet weten" and "Bronvermelding".
8. State final word count excluding "Bronvermelding" and superscript markers, plus whether the language check was manual or tool-assisted.

## Calibration

| Analysis label | Strongest article phrasing |
|---|---|
| `(traced)` | Direct assertion with source marker. |
| `(deferred to consensus)` | Assertion naming the body where it carries weight. |
| `(deferred, fragile)` | Hedged assertion naming the failure mode. |
| `(memory — unverified)` | Hedged, attributed, never load-bearing alone. |
| `(user-supplied — unverified)` | Same; if central, the article is not ready. |

If removing a weakly warranted claim collapses the conclusion, stop and flag the gap.

## Length

Ask for or use the target word count. Count everything except "Bronvermelding" and `<sup>[n]</sup>` markers. Aim for +/-10%. If no target is given, write only as long as the material warrants. Never cut attribution, hedges, source markers, or "Wat we (nog) niet weten" to hit length.

## Article Shape

```markdown
# [Kop]

[Inleiding: 1-3 alinea's with probleemstelling, these, kernboodschap/conclusie.]

## [Tussenkop]

[Kern: claim-by-claim, logical chapter order, source markers after supported clauses or sentences.<sup>[1]</sup>]

## [Tussenkop]

[Next step in the argument.<sup>[2]</sup>]

## Wat we (nog) niet weten

[Open questions and relevant bias-audit caveats.]

## [Slot]

[Return to the kernboodschap or final open question. No new claims.]

## Bronvermelding

1. Titel bron — Auteur/uitgever, datum (geraadpleegd dd-mm-jjjj).  
   <https://www.voorbeeld.nl/bron>
```

Headline and tussenkoppen must stay within the calibration ceiling: honest, specific, no clickbait. Provocative chapter titles are allowed only for genuinely strong findings, never for thin context.

## Source Markers And Bronvermelding

- Use numbered HTML superscript markers: `<sup>[1]</sup>`.
- Put markers after the supported clause or sentence, after punctuation.
- Number sources by first appearance; reuse the same number for repeat citations.
- Every marker must resolve to one Bronvermelding item, and every item must be cited.
- Prefer traced primary sources over secondaries.
- Each entry: descriptive line, two trailing spaces, URL on the next indented line.
- Include access dates from the analysis's `(traced)` labels.
- If sources share funding, ownership, mandate, or alignment, note that they are not independent corroboration.
- If no URL exists, describe the document and say so.

## Quotes And Confidential Sources

- Quote verbatim; mark omissions with `[...]` and insertions with `[redactie: ...]`.
- Label translations and keep the original recoverable.
- Do not move quotes into misleading contexts or borrow wording without attribution.
- Protect confidential sources: do not name or identify them in text or Bronvermelding, including by singling detail. Use only a safe description and state that the identity is known but withheld.
- Apply Raad voor de Journalistiek guidance on publication/quotes and source protection, and SPJ ethics on truthful quotation, attribution, anonymity, and keeping promises. If these norms become article-supporting sources, cite them:
  - RvdJ Leidraad C. Publicatie: <https://rvdj.nl/leidraad/c-publicatie/> (geraadpleegd 08-06-2026).
  - RvdJ Leidraad B. Voorbereiding/Nieuwsgaring: <https://rvdj.nl/leidraad/b-voorbereidingnieuwsgaring/> (geraadpleegd 08-06-2026).
  - SPJ Code of Ethics mirror: <https://www2.hawaii.edu/~jour/spj/SPJcode.html> (geraadpleegd 08-06-2026; canonieke vindplaats spj.org gaf 403).

## Dutch Style

- Good Dutch, official spelling, correct compounds, required hyphens, and correct diacritics.
- Varied sentence length, roughly 15-20 words on average.
- No stylistic en/em dashes; use comma, colon, full stop, or restructure.
- Prefer active verbs, concrete nouns, dates, documents, and numbers.
- Avoid naamwoordstijl, tangconstructies, anglicisms, and needless jargon.
- Enumerations: introduce with a colon; separate items with semicolons; end the last with a full stop.
- No needless repetition. Repeat the kernboodschap only when the slot adds the earned resonance.
- Do a spelling/grammar pass before delivery; use a checker if available, otherwise read manually.

## Final Check

Before delivery, verify:

1. no new facts or memory claims slipped in;
2. every load-bearing sentence traces to the inventory;
3. no phrasing exceeds its calibration ceiling;
4. all weak claims are hedged and attributed;
5. intro has probleemstelling, these, and kernboodschap/conclusie;
6. chapters follow a clear order and all have tussenkoppen;
7. "Wat we (nog) niet weten" and slot are present;
8. quotes, translations, and confidential sources are handled cleanly;
9. Dutch spelling, grammar, punctuation, and repetition are checked;
10. all markers and Bronvermelding entries match;
11. word count is on target or the constraint is explicitly surfaced.

Deliver one markdown article. If the analysis is insufficient, say what is missing instead of writing around the gap.

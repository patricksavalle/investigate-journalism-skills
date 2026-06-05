---
name: osint-research
description: A structured framework for AI agents to plan, execute, and verify open-source intelligence (OSINT) investigations using only publicly available information (PAI). Use whenever the user wants to investigate or build a profile on a person, organisation, account, domain, IP, image, video, location, vehicle, vessel, aircraft, or event using public web data — including phrases like "find out about", "investigate", "who is behind", "verify this image/video", "where/when was this taken", "what's the digital footprint of", "trace this username/email/domain", "is this account real", "build a profile on", or any request to systematically gather and corroborate online information about a target. Pair with the investigative-reasoning skill when the goal extends to hypothesis construction or narrative challenge — this skill handles gathering and verification mechanics; investigative-reasoning handles analytical reasoning on top.
version: 1.0
aligned: 2026-05-26
---

# OSINT Research

Gather, pivot, and verify intelligence from publicly available sources. Built for AI agents using web search and fetch as primary tools — calibrated to what is achievable without shell access, paid databases, or specialist binaries.

## Activation

Trigger when the task is **systematic information gathering** on a target: profile build, identifier trace, image/video verification, geolocation/chronolocation, digital footprint mapping, due diligence, account attribution.

**Do not trigger** for simple factual lookups, opinion questions, summaries of well-known public figures, or anything not requiring pivoting and verification.

## Pairs With

- `investigative-reasoning` — once findings need hypothesis construction, narrative challenge, or Cui Bono / MMO analysis. Hand over the structured brief as Fact File input.
- `fallacy-bias-and-manipulation-analysis` — when the target's own claims (posts, interviews, manifestos) need rhetorical / fallacy audit.
- `scientific-fact-classification` — when the target asserts scientific claims that need evidence-strength classification.
- `peer-review` — when the target has published papers or studies that need methodological audit.
- `first-principles-thinking` — when an account's self-description ("we are a charity", "this is open-source") needs decomposition before downstream investigation.
- `belief-revision` — when new identifiers, archive captures, or attribution evidence emerge after a brief is delivered and a calibrated update is needed.

## Research Discipline (CLAUDE.md/AGENTS.md)

OSINT collection without truth-seeking discipline produces dossiers, not intelligence. The rules in `CLAUDE.md` / `AGENTS.md` → *Operating rules* bind here:

- **Rule 1** (pre-search hypothesis registration) — at Phase 1 Planning, register the hypotheses about the target before pivoting; otherwise discovered selectors will select which question gets answered.
- **Rule 2** (steelman from primary literature) — when the target has primary writings (manifesto, filings, interviews), fetch them directly; never rely solely on critics' summaries.
- **Rule 3** (primary before secondary) — when a finding traces back to another report, fetch the underlying source before treating the secondary as independent.
- **Rule 4** (map institutional networks) — before counting multiple outlets / accounts as independent corroboration, map shared ownership / funding / coordination (Phase 4 inauthenticity checks help).
- **Rule 5** (Tier 0 priority) — for time-sensitive media (live events, account behaviour), contemporaneous archive captures outrank later screenshots; preserve via web.archive.org at collection time.
- **Rule 6** (bias self-audit) — enforced in `## Self-Audit`.
- **Rule 7** (minimum search volumes) — Phase 2 specifies Quick 5–15 / Standard 15–40 / Deep 40–100+.
- **Rule 8** (hostility check on sources) — Phase 4 Admiralty rates source reliability; supplement with explicit funding / alignment / mandate where load-bearing.
- **Rule 9** (interactive refinement) — when the user volunteers identifiers, attribution claims, or context about the target ("this account is actually run by X"), label `(user-supplied — unverified)` and treat as a hypothesis to verify via Admiralty-graded findings, never as established attribution.
- **Rule 10** (objective report voice) — write the brief as a standalone finding on the target or question, with no requester references in the report prose.

## Warrant Labels (Project Standard)

Every load-bearing finding carries a warrant per `CLAUDE.md` / `AGENTS.md`:

| Label | Meaning |
|---|---|
| `(traced)` | Followed evidence chain to a public source fetched in this session. State URL + access date; archive URL when useful. |
| `(deferred to consensus)` | Relying on a named social/institutional consensus mechanism or official registry class without independently tracing each underlying record. Consensus is not scientific warrant; for scientific claims, treat it only as a political/social prior unless traced to reproduced or replicated evidence. |
| `(deferred, fragile)` | Deferred to consensus, but failure modes apply: state control, platform opacity, coordinated reporting, registry gaps, capture, or similar. State which. |
| `(memory — unverified)` | Recalled from training data, not verified this session. Never load-bearing without an explicit caveat that it could be wrong. |
| `(user-supplied — unverified)` | Provided during interactive refinement and not verified in-session. Treat as a selector or hypothesis to verify, never as attribution. |

Admiralty grading (Phase 4) rates *source reliability* and *claim credibility*; warrant labels rate *what the analyst did this session* (followed evidence to a primary, or recalled). Both travel with the finding — they are orthogonal.

If sources are fetched, record for each cited source: URL, archive URL where available, access date, publication date where relevant, warrant label, and funding / ownership / mandate / national alignment where relevant.

---

## Hard Constraints

| Constraint | Rule |
|---|---|
| PAI only | No paywalls, logins, ToS-violating scraping. If access requires deception, it is not OSINT. |
| No active engagement | Never contact/message/ping the target. No "forgot password" probes. No tracking pixels. |
| No facial recognition on private individuals | Reverse search of objects, scenes, and public-figure imagery only. |
| No breach data on private individuals | Never query breach repos / paste-sites for non-public-individuals' data. |
| Minor protection | If target is or may be a minor, refuse profiling. Limit to safety-critical work. |
| Jurisdictional awareness | Public-records access varies (GDPR, US state laws, ToS). Flag sensitive collection. |
| Harm minimisation | For vulnerable targets (refugee, witness, abuse survivor, dissident), state harm risk and ask before proceeding. Document the choice. |

If a request crosses these, refuse the specific step, explain why, offer the closest defensible alternative.

---

## Tooling Honesty

**Can do natively:** web search across engines and languages · web fetch (incl. web.archive.org, archive.today) · visual reasoning over user-pasted images · cross-referencing · structured plans, dorks, pivot trees.

**Cannot do natively:** run `exiftool` / `yt-dlp` / `ffmpeg` (unless code execution available) · read EXIF unless user uploads file with metadata intact (most platforms strip it) · use paid DBs, breach repos, login services · perform reverse image search in chat (provide URLs and strings for user to run; `image_search` is forward-only) · live network probes (Shodan, Censys, port/DNS scans — but can search published results) · real-time satellite imagery (can reference public providers).

State this when relevant. When code execution is available, parsing uploads / hashes / bulk archives unlocks — note when it changes the plan.

---

## Phase 1 — Planning

Capture before collecting:

1. **Intelligence Requirement** — the specific question
2. **Priority Intelligence Requirements** — mission-critical vs. nice-to-have
3. **Target type** — person, entity, account, asset, event, location, media
4. **Starting selectors** — every identifier user has (name, email, handle, domain, phone, URL, hash, geo, timestamp)
5. **End goal** — report, evidence package, single answer, monitor
6. **Scope boundaries** — countries, time periods, platforms, individuals out
7. **Harm assessment** — could anyone be harmed?
8. **Operational context** — journalist, researcher, security pro, hobbyist, personal connection?

Run the **5 Ws + 2 Hs**: Who, What, When, Where, Why, How, How-much-confidence-needed.

If unclear, ask before collecting. 30 seconds of clarification saves hours.

---

## Phase 2 — Collection

Systematic, layered, documented. Log every search with query, engine, date, top finding.

| Source Class | Notes |
|---|---|
| **Search engines** — Google, Bing, DuckDuckGo, Yandex (CIS/Russia, image), Baidu (China), regional | Vary engines — they index differently |
| **Operators** — `site:`, `inurl:`, `intitle:`, `filetype:`, `intext:`, date, language | One precise dork beats ten vague ones |
| **Social** — LinkedIn, X, Bluesky, Mastodon, FB, IG, TikTok, YouTube, Reddit, Telegram (public), Discord (public servers only) | Use platform-specific syntax; many have exposed endpoints |
| **Archives** — web.archive.org, archive.today/ph, Google Cache, common-crawl mirrors | Pages get edited/deleted — archives preserve |
| **Public records** — courts, business registries, property, voter rolls, FCC/SEC, Companies House (UK), KvK (NL), EDGAR, OpenCorporates | Jurisdiction-specific; flag missing access |
| **Media** — national, regional, trade, foreign-language press | Foreign press often surfaces buried details |
| **Specialist registries** — WHOIS history, crt.sh (certificate transparency), GitHub commits, package registries, ASN | Technical/infrastructure targets |
| **Geospatial** — Google/Bing/Apple/Yandex Maps, OSM, Wikimapia, Mapillary, KartaView | Coverage and recency differ enormously by region |
| **Image/video** — TinEye, Yandex Images (best for faces/landmarks), Google Lens, Bing Visual | Each indexes differently |

**Query templates.**
```
Identity:         "[name]" "[employer]" -site:linkedin.com (find non-LinkedIn presence)
Username spread:  "[username]" site:github.com OR site:reddit.com OR site:twitter.com
Email validation: "[email]" site:pastebin.com OR site:github.com
Domain history:   site:[domain] → archives, WHOIS, crt.sh subdomains
Phone:            "[phone in multiple formats]" — +CC, 0-prefix, hyphens, parens
Image context:    [visual cues] + [region] + [signage language]
Geolocation:      "[architecture]" "[country]" — narrow with vegetation, signage, plates
Chronolocation:   [event] site:twitter.com [date range] OR weather [location] [date]
Archived:         site:web.archive.org [original URL]
Negative:         [target] complaint OR lawsuit OR controversy OR fraud
Foreign-language: translate query, use regional engines
```

**Volumes.** Quick check 5–15 · Standard (profile/single-event) 15–40 · Deep (full investigation/attribution) 40–100+. Beyond 100, flag and recommend structured deep-research workflow.

**Preserve.** Archive every load-bearing URL through web.archive.org *while you have it*. The single most-skipped OSINT discipline. Save archive URL alongside live URL.

---

## Phase 3 — Processing

- **Translate** non-English; note original language per finding
- **Normalise** — phone (E.164), email (lowercase), username (case-sensitive note), date (ISO-8601), coords (decimal degrees)
- **De-duplicate** — 12 outlets citing one wire report = one data point
- **Timestamp** — publication, observation, underlying event
- **Chain** — per load-bearing claim: primary source or secondary report?

---

## Phase 4 — Analysis

### Admiralty Code (NATO STANAG 2511)

Score every load-bearing item with two characters. **Source reliability and information credibility are independent.**

| Letter (source) | Number (this specific claim) |
|---|---|
| A — Completely reliable | 1 — Confirmed by independent sources |
| B — Usually reliable | 2 — Probably true (consistent, uncorroborated) |
| C — Fairly reliable | 3 — Possibly true (reasonable, not corroborated) |
| D — Not usually reliable | 4 — Doubtful (illogical or contradicted) |
| E — Unreliable | 5 — Improbable (contradicted by other info) |
| F — Cannot be judged | 6 — Cannot be judged |

Most fresh OSINT is **F6** until corroborated. **The diagonal failure mode:** letting source reliability bleed into credibility scoring. Force claim scoring on its own evidence.

### Verification Techniques

| Technique | What | AI constraints |
|---|---|---|
| Reverse image search | Prior appearances, original context | Cannot perform in chat — provide URL + strings; describe distinctive features |
| Geolocation | Architecture, signage, vegetation, mountains, sun position | Can reason over uploaded image cues; cannot run SunCalc but can describe expected shadows given coords + date |
| Chronolocation | Shadows, weather, foliage, fashion, devices, contemporaneous events | Cross-reference: `"[location] weather [date]"` |
| Metadata | EXIF, headers, embedded thumbnails | Only if user pastes raw metadata or uploads file with metadata intact |
| Cross-platform consistency | Earlier appearance elsewhere = repost | Search distinctive text, captions, hashes |
| Account age & behaviour | Recent registration + high volume + topical narrowness = probable inauthentic | Check registration, follower ratios, posting rhythm (visible without login on most platforms) |
| Linguistic analysis | Native vs. translation artefacts, regional idioms | Reason; flag confidence as low |

### Pivoting

Every identifier is a new entry point. Pivot systematically.

```
NAME      → employer → colleagues → work-email format → domain → infrastructure
USERNAME  → other platforms (whatsmyname / sherlock-style enumeration via search)
          → reused email patterns → linked Google profile → reviews → location pattern
EMAIL     → Gravatar → linked accounts (Epieos-style) → GitHub commits (`author-email:`)
          → registered domains (WHOIS history)
DOMAIN    → WHOIS history → registrant email → other domains by same email
          → crt.sh → subdomains → linked IPs
PHONE     → format variants → messaging-app presence (visible without contact)
          → email-recovery patterns (NEVER execute on living individuals)
IMAGE     → reverse search → prior appearances → original context
          → distinctive features → location → date
ENTITY    → registry filings → directors → directors' other companies → addresses
          → addresses' other tenants → financial filings → media coverage
```

**Stop conditions.** PIR answered with adequate confidence · new pivots return only seen info (saturation) · would require non-PAI · creates harm-minimisation concern · scope/budget exhausted.

---

## Phase 5 — Dissemination

Deliver in the form requested. Ask what was missing.

---

## Output

```markdown
# OSINT Brief: [Target / Question]

## Summary
- **Intelligence Requirement:** [one sentence]
- **Target type:** person | entity | account | asset | event | media
- **Verdict:** [one-line — what the evidence supports / does not support]

## Scope & Constraints
- Time period:
- Out of scope:
- Harm-minimisation choices:
- AI-agent limits relevant here: [e.g. no EXIF; reverse image search delegated]

## Starting Selectors
[Every identifier provided by the user]

## Discovered Selectors
[New identifiers + pivot chain that produced each]

## Findings (graded)
| # | Finding | Source(s) | Access date | Admiralty | Warrant | Funding / ownership / mandate / alignment | Notes |
|---|---|---|---|---|---|---|---|
| 1 | … | [URL + archive URL] | [date] | B2 | (traced) | [source alignment] | [why Admiralty rating + verification done] |

## Verification Status (media / contested)
| Item | Geolocation | Chronolocation | Reverse image | Other |
|---|---|---|---|---|

## Negative Findings
[Searched for and did not find — absence is evidence when search was thorough]

## Confidence & Severity
[Low / Medium / High overall + reasoning tied to Admiralty grades; counts of A1–B2 vs F6 findings]

## What Would Change This
[Falsification criteria — what evidence, if surfaced, would shift the verdict]

## Self-Audit
- **Symmetry test:** Would I have reached the same verdict if the politically/socially expected answer ran the other way? If no — explain. If you can't tell — say so.
- **Diagonal-failure check:** Did source reliability bleed into credibility scoring?
- **Coverage check:** Were foreign-language / regional engines used where appropriate?
- **Harm check:** Were minor-protection and vulnerable-target rules honoured?

## Limits of This Analysis
[Unexhausted pivots; access not attempted; tooling constraints — note where user-side action (EXIF read, reverse image, paid DBs) unlocks more]

## Recommended Next Steps
[Hand-offs (e.g. to investigative-reasoning); user-side access needs]

## Archive Manifest
[web.archive.org snapshots created — so findings remain re-verifiable]
```

---

## OPSEC — For the User

The agent has no persistent IP/fingerprint/cookies. The user does. Warn when relevant.

- Don't log in while investigating — use logged-out views or sock-puppet accounts
- Don't click target links while logged into your own accounts
- Use a clean browser profile for sensitive collection
- Visiting target's site logs your IP in their server logs — Tor/VPN if attribution is a concern
- Don't download files from targets without sandboxing — investigators have been compromised this way

State these only when warranted. For benign verification of public news images, OPSEC warnings are noise.

---

## Quick Reference

| Question | First move |
|---|---|
| Is this image real? | Reverse image (delegate) + geolocation + chronolocation cues |
| Who is behind this account? | Username pivot to other platforms; account age + posting rhythm; linked email/Gravatar |
| Is this company legitimate? | Registry → directors → directors' other entities → address co-tenants → media → negative search |
| Where was this taken? | Architecture → signage → vehicle plates → vegetation → sun direction |
| When was this taken? | Shadow analysis (SunCalc-equivalent) → weather records → contemporaneous events visible → device/fashion era |
| Is this account inauthentic? | Registration date + volume + topical narrowness + image reuse + linguistic artefacts |

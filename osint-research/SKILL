---
name: osint-research
description: A structured framework for AI agents to plan, execute, and verify open-source intelligence (OSINT) investigations using only publicly available information (PAI). Use whenever the user wants to investigate or build a profile on a person, organisation, account, domain, IP, image, video, location, vehicle, vessel, aircraft, or event using public web data — including phrases like "find out about", "investigate", "who is behind", "verify this image/video", "where/when was this taken", "what's the digital footprint of", "trace this username/email/domain", "is this account real", "build a profile on", or any request to systematically gather and corroborate online information about a target. Pair with the investigative-reasoning skill when the goal extends to hypothesis construction or narrative challenge — this skill handles the gathering and verification mechanics; investigative-reasoning handles the analytical reasoning on top.
---

# OSINT Research Framework

A rigorous methodology for gathering, pivoting, and verifying intelligence from publicly available sources. Built for AI agents using web search and fetch as primary tools, calibrated to what is actually achievable without shell access, paid databases, or specialist binaries.

---

## Activation

**Trigger when the task is information gathering on a target**, not when the user just wants a single fact answered. Valid triggers: build a profile, trace an identifier, verify a claim/image/video, geolocate or chronolocate media, map a digital footprint, due diligence on a person or entity, attribution of an account or post.

**Do not trigger for:** simple factual lookups ("when was X founded"), opinion questions, summaries of known public figures' Wikipedia pages, or anything that does not require systematic pivoting and verification.

**Pairing rule:** if the user wants to *interpret* the gathered intelligence (challenge an official narrative, build a hypothesis, audit for bias), hand off the structured findings to `investigative-reasoning` rather than duplicating that work here.

---

## Hard Constraints — Non-Negotiable

These constraints define the boundary between OSINT and conduct that is unethical, unlawful, or operationally compromising. Violate any of them and the work is no longer OSINT.

| Constraint | Rule |
|------------|------|
| **PAI only** | Use only Publicly Available Information. No content behind paywalls, logins, or terms-of-service that prohibit scraping. If accessing it requires deception, it is not OSINT. |
| **No active engagement** | Never contact, message, ping, or send anything to the target. No "forgot password" probes against living individuals. No tracking pixels. No phishing-adjacent techniques. |
| **No facial recognition on private individuals** | Do not use reverse face search to identify private people. Reverse image search of objects, scenes, and public-figure imagery is fine. |
| **No credential / breach data on private individuals** | Do not query breach repositories or paste-sites for the personal data of non-public individuals, even if the user asks. |
| **Minor protection** | If the target is or may be a minor, refuse profiling. Limit work to what is strictly needed for safety (e.g. confirming a missing person is not in danger). |
| **Jurisdictional awareness** | Public-records access varies by country. EU/UK GDPR, US state laws, and platform ToS all differ. Flag jurisdiction-sensitive collection to the user. |
| **Harm minimisation** | Before collecting anything on a vulnerable person (refugee, witness, abuse survivor, dissident), state the harm risk and ask the user whether to proceed. Document the harm-minimisation choice in the output. |

**If a request crosses these lines**, refuse the specific step, explain why, and offer the closest defensible alternative (e.g. "I won't reverse-search this person's face, but I can verify the location they claim to be in").

---

## What an AI Agent Can and Cannot Do

Be honest with the user about the tooling boundary. This calibrates expectations and prevents fabricated tradecraft.

**Can do natively:**
- Web search across multiple engines and languages (run searches on Yandex, Baidu, regional engines via direct queries)
- Web fetch of specific URLs, including archived pages on web.archive.org and archive.today
- Reasoning over visual cues in images the user pastes (architecture, signage, vegetation, license plates, sun/shadow direction)
- Cross-referencing claims across multiple independent sources
- Drafting structured collection plans, search query templates, and pivot trees

**Cannot do natively (state this explicitly when relevant):**
- Run binaries like `exiftool`, `yt-dlp`, `ffmpeg` (unless code execution is available — check)
- Access EXIF metadata unless the user pastes it or uploads the original file with metadata intact (most platforms strip it)
- Use paid databases, breach repositories, or login-required services
- Perform reverse image search inside this conversation — provide URLs and search strings the user can run, or use the `image_search` tool for forward search only
- Run live network probes (Shodan, Censys, port scans, DNS pivots) — but can search published results from those tools
- See real-time satellite imagery — can search for and reference public satellite providers (Sentinel Hub, Planet, Google Earth)

**When code execution is available**, additional capability unlocks: parsing user-uploaded files for embedded metadata, computing perceptual hashes, parsing CSV/JSON data dumps, fetching and processing archive snapshots in bulk. State when this changes the plan.

---

## The OSINT Cycle — Five Phases

The standard intelligence cycle, adapted for AI execution. Each phase has explicit search discipline.

### Phase 1 — Planning & Direction

Define the investigation before collecting anything. Skipping this produces noise and rabbit holes.

**Capture:**
1. **Intelligence Requirement (IR)** — what specific question does the user want answered?
2. **Priority Intelligence Requirements (PIR)** — what subset is mission-critical vs. nice-to-have?
3. **Target type** — person, entity, account, asset, event, location, media file
4. **Known starting selectors** — every identifier the user already has (name, email, handle, domain, phone, URL, image hash, geo-coordinates, timestamp)
5. **End goal** — written report, evidence package, single answer, ongoing monitor
6. **Scope boundaries** — what is explicitly out of scope (countries, time periods, platforms, individuals)
7. **Harm assessment** — could the target, third parties, or the user be harmed by this collection?
8. **Operational context** — is the user a journalist, researcher, security professional, hobbyist, or person with a personal connection to the target? This changes the ethical bar.

**5 Ws and 2 Hs** — run this checklist on every investigation: Who, What, When, Where, Why, How, How-much-confidence-needed.

If any of the above is unclear, ask the user before collecting. A 30-second clarifying question saves hours of misdirected work.

### Phase 2 — Collection

Systematic, layered, documented. Every search is logged with the query, the engine, the date, and the top finding.

**Layer collection across these source classes** (apply the relevant ones for the target type):

| Source Class | Examples | Notes |
|--------------|----------|-------|
| **Search engines** | Google, Bing, DuckDuckGo, Yandex (best for image search and CIS/Russia coverage), Baidu (China), regional engines | Vary engines — they index differently |
| **Advanced operators** | `site:`, `inurl:`, `intitle:`, `filetype:`, `intext:`, date range, language filters | Combine, do not stack uselessly. One precise dork beats ten vague ones |
| **Social platforms** | LinkedIn, X/Twitter, Bluesky, Mastodon, Facebook, Instagram, TikTok, YouTube, Reddit, Telegram channels (public), Discord (public servers only) | Use platform-specific search syntax; many have distinct exposed endpoints |
| **Archives** | web.archive.org, archive.today, archive.ph, Google Cache, common-crawl mirrors | Always check archives — pages get edited or deleted, archives preserve the original |
| **Public records** | Court records, business registries, property records, voter rolls, FCC/SEC filings, Companies House (UK), KvK (NL), EDGAR (SEC), OpenCorporates | Jurisdiction-specific; flag when you do not have access to the relevant registry |
| **Media outlets** | National + regional press, trade press, foreign-language press for non-Anglosphere targets | Foreign press often surfaces details domestic press buried |
| **Specialist registries** | DNS/WHOIS history, certificate transparency (crt.sh), GitHub commits, package registries, ASN data | For technical and infrastructure targets |
| **Geospatial** | Google Maps, Bing Maps, Apple Maps, Yandex Maps, OpenStreetMap, Wikimapia, Mapillary, KartaView | Vary providers — coverage and recency differ enormously by region |
| **Image/video** | TinEye, Yandex Images (best for faces and landmarks), Google Lens, Bing Visual Search | Each engine indexes differently — do not rely on one |

**Search query templates** (adapt to target):

```
Identity:           "[name]" "[employer/affiliation]" -site:linkedin.com (find non-LinkedIn presence)
Username spread:    "[username]" site:github.com OR site:reddit.com OR site:twitter.com
Email validation:   "[email]" site:pastebin.com OR site:github.com
Domain history:     site:[domain] (then archives, WHOIS, crt.sh subdomains)
Phone:              "[phone in multiple formats]" — try +CC, 0-prefix, hyphenated, parenthesised
Image context:      [describe visual cues] + [region] + [language of signage]
Geolocation cues:   "[architectural style]" "[country]" — narrow with vegetation, signage, vehicle plates
Chronolocation:     [event] site:twitter.com [date range] OR weather [location] [date]
Archived versions:  site:web.archive.org [original URL]
Negative search:    [target] complaint OR lawsuit OR controversy OR fraud
Foreign-language:   translate the query, search regional engines
```

**Search volumes** by depth:
| Depth | Searches | When |
|-------|----------|------|
| Quick check | 5–15 | Identity confirmation, single-fact verification |
| Standard | 15–40 | Profile build, single-event verification, due diligence |
| Deep | 40–100+ | Full investigation, complex attribution, multi-actor |

If 100+ searches are clearly required, flag to the user that this exceeds a single session and recommend a structured deep-research workflow.

**Preserve everything as you collect.** Every URL goes through web.archive.org *while you have it*. Pages get deleted. Save the archived URL alongside the live URL. This is the single most-skipped OSINT discipline and the most regretted.

### Phase 3 — Processing

Raw data is not intelligence. Convert what you collected into structured, comparable form.

- **Translate** non-English content; note the original language for every finding
- **Normalise identifiers** — standardise phone numbers (E.164), emails (lowercase), usernames (case-sensitive notes), dates (ISO-8601), coordinates (decimal degrees)
- **De-duplicate** — the same claim repeated by 12 outlets citing one wire report is *one* data point, not twelve
- **Timestamp every finding** — when was this published, when was it observed, when was the underlying event
- **Flag the chain** — for every load-bearing claim, note whether you have the primary source or only a secondary report

### Phase 4 — Analysis

Move from organised facts to assessed intelligence.

**Source grading — Admiralty Code (NATO STANAG 2511)**

Score every load-bearing piece of evidence with a two-character code. **Source reliability and information credibility are independent** — score them separately. A reliable source can carry one false claim; an unreliable source can carry one true claim.

| Reliability (letter — about the source) | | Credibility (number — about this specific claim) |
|---|---|---|
| **A** Completely reliable — no doubt of authenticity, history of full reliability | | **1** Confirmed by other independent sources, logical, consistent |
| **B** Usually reliable — minor doubts, mostly valid history | | **2** Probably true — not confirmed but logical and consistent |
| **C** Fairly reliable — some doubts, has been valid before | | **3** Possibly true — not confirmed, reasonable but not corroborated |
| **D** Not usually reliable — significant doubts, occasionally valid | | **4** Doubtful — not confirmed, possible but illogical or contradicted |
| **E** Unreliable — history of invalid information | | **5** Improbable — contradicted by other information |
| **F** Cannot be judged — no basis for evaluation | | **6** Cannot be judged |

Most fresh OSINT material is **F6** until corroborated. That is normal. Do not inflate ratings to feel more confident; inflation destroys the system. **The diagonal failure mode** — letting source reliability bleed into credibility scoring — is the most common misuse; force yourself to score the claim on its own evidence.

**Verification techniques** (apply to claims, especially for media):

| Technique | What it does | AI-agent constraints |
|-----------|--------------|----------------------|
| **Reverse image search** | Find prior appearances of an image, often revealing the original context | Cannot perform from chat — provide the URL and search strings; if user pastes the image, describe distinctive features for them to search |
| **Geolocation** | Identify where media was captured using visual cues (architecture, signage, vegetation, mountains, sun position) | Can reason over an uploaded image's visual cues; cannot run SunCalc but can describe what it would show given coordinates and date |
| **Chronolocation** | Identify when something happened using shadows, weather, foliage, fashion, devices visible, contemporaneous events | Cross-reference with weather records (search "[location] weather [date]") and event records |
| **Metadata** | EXIF, file headers, embedded thumbnails | Only if user pastes raw metadata or uploads a file with metadata intact — most social platforms strip it |
| **Cross-platform consistency** | Same image/text appearing earlier elsewhere indicates repost | Search the image's distinctive text, search captions, search hashes if available |
| **Account age & behaviour** | Recent registration + high posting volume + topical narrowness = probable inauthentic | Check registration dates, follower/following ratios, posting rhythm (visible without login on most platforms) |
| **Linguistic analysis** | Native vs. non-native phrasing, machine-translation artefacts, regional idioms | Reason over the text; flag confidence as low — linguistic attribution is unreliable |

**Pivoting — the core OSINT technique**

Every identifier you find is a new search entry point. Pivot systematically; do not stop at the first hit.

```
Common pivot chains:

NAME      → employer → colleagues → work email format → domain → infrastructure
USERNAME  → other platforms (whatsmyname, sherlock-style enumeration via search)
            → reused email patterns → linked Google profile → reviews → location pattern
EMAIL     → Gravatar profile → linked accounts (Epieos-style searches)
            → GitHub commits (`author-email:`) → registered domains (WHOIS history)
DOMAIN    → WHOIS history → registrant email → other domains by same email
            → certificate transparency (crt.sh) → subdomains → linked IPs
PHONE     → formatted variants → messaging-app presence checks (visible without contact)
            → linked email recovery patterns (do NOT execute on living individuals)
IMAGE     → reverse search → prior appearances → original context
            → distinctive features → location → date
ENTITY    → registry filings → directors → directors' other companies → addresses
            → addresses' other tenants → financial filings → media coverage
```

**Stop conditions** — pivoting is recursive but not infinite. Stop when:
- The PIR is answered with adequate confidence
- New pivots return only previously-seen information (saturation)
- Further pivoting would require non-PAI sources
- Continuing creates harm-minimisation concerns
- The user's stated scope or budget is exhausted

### Phase 5 — Dissemination & Feedback

Produce the deliverable in the form the user asked for. Then ask what was missing.

---

## Output Format

```markdown
## OSINT Brief: [Target / Question]

### Intelligence Requirement
[The question being answered, in one sentence]

### Scope & Constraints
- Target type: [person | entity | account | asset | event | media]
- Time period covered: [...]
- Out of scope: [...]
- Harm-minimisation choices: [what was deliberately not collected, and why]
- AI-agent limitations relevant here: [e.g. could not access EXIF; reverse image search delegated to user]

### Starting Selectors
[Identifiers given at outset]

### Discovered Selectors
[Pivoted identifiers — show the pivot chain that produced each]

### Findings (graded)
| # | Finding | Source(s) | Admiralty | Notes |
|---|---------|-----------|-----------|-------|
| 1 | [...] | [URL + archive URL] | B2 | [why this rating] |

### Verification Status (for media or contested claims)
| Item | Geolocation | Chronolocation | Reverse image | Other |
|------|-------------|----------------|---------------|-------|

### Negative Findings
[What you searched for and did not find — this is part of the record. Absence of evidence is itself evidence, when the search was thorough.]

### Confidence Assessment
[Overall: low / medium / high — with reasoning. Tie to Admiralty grades of load-bearing findings.]

### What Would Change This Assessment
[Falsification criteria — what evidence would invalidate the headline conclusion]

### Recommended Next Steps
[Pivots not yet exhausted, sources requiring user-side access, hand-off to investigative-reasoning if hypothesis work is now warranted]

### Archive Manifest
[List of web.archive.org snapshots created during the investigation, so findings remain re-verifiable if originals are deleted]
```

---

## Operational Security — For the User, Not the Agent

Claude has no persistent IP, browser fingerprint, or cookies to protect across sessions. The user does. Warn them when relevant.

- **Do not log in to platforms while investigating** — use logged-out views or sock-puppet accounts (which the user must create themselves on platforms that allow it)
- **Do not click links in target's content** while logged in to your own accounts
- **Use a clean browser profile** for sensitive collection
- **Be aware that visiting a target's website logs your IP** in their server logs — use Tor or a VPN if attribution to you is a concern
- **Do not download files from targets without sandboxing** — investigators have been compromised this way

State these only when the situation warrants. For benign verification of a public news image, OPSEC warnings are noise.

---

## Quick Reference

| Question | First move |
|----------|------------|
| Is this image real? | Reverse image search (delegate to user) + geolocation cues + chronolocation cues |
| Who is behind this account? | Username pivot to other platforms; check account age and posting rhythm; look for linked email/Gravatar |
| Is this company legitimate? | Registry filing → directors → directors' other entities → registered address co-tenants → media coverage → negative search |
| Where was this taken? | Architecture style → signage language → vehicle plates → vegetation → sun direction → narrow with regional features |
| When was this taken? | Shadow analysis (SunCalc-equivalent reasoning) → weather records → contemporaneous events visible → device/fashion era |
| Is this account inauthentic? | Registration date + posting volume + topical narrowness + image reuse + linguistic artefacts |

---

## Core Golden Rules

**On PAI:** If accessing the data requires deception, login bypass, or breaching ToS, it is not OSINT. The discipline lives or dies by this line.

**On corroboration:** A single source is a lead, not a finding. Three sources that all trace to the same wire report are still one source — institutional echo is not corroboration.

**On preservation:** Archive every load-bearing URL the moment you find it. Pages disappear. Tweets get deleted. Companies edit their about pages. Without an archive, you have nothing.

**On the pivot:** The most significant findings rarely come from the first search. They come from the second or third pivot. Stopping at the first result is the most common amateur mistake.

**On the diagonal:** Source reliability and information credibility must be scored independently. The day you start letting "trusted source" slide credibility upward is the day your OSINT becomes confirmation bias dressed in tradecraft vocabulary.

**On absence:** What you searched for and *did not* find is part of the record. Document negative findings as deliberately as positive ones — they are the ground against which positive findings are figure.

**On harm:** OSINT can hurt people. Misidentification, doxxing, exposing whistleblowers, leading mobs to the wrong target — all have happened. Before publishing, ask: who could be harmed if this finding is wrong, and what is the safety margin?

**On AI honesty:** Do not invent tradecraft you cannot execute. If you cannot reverse-search a face, say so. If the platform stripped the EXIF, say so. Calibrated humility is the foundation of trust; fabricated capability is the fastest path to a wrong, confidently-stated conclusion.

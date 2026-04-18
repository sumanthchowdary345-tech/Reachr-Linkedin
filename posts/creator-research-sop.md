# Creator Research SOP — From Name to Deliverables

**Version:** 1.0 — April 2026
**Built from:** Vaibhav Sisinty + Justin Welsh + Jasmin Alic pipeline sessions

**Trigger:** Sumanth says "Research [Creator Name]" or "Do the pipeline for [Name]"

**First action:** Read this file entirely. Follow it step by step. Do not skip steps. Do not execute before reading the full process.

**Total time per creator:** 60–90 minutes

---

## STEP 0 — Pre-Flight (2 min)

Run both checks simultaneously:

**0a — Apify API key**
```bash
echo $APIFY_API_KEY
```
If blank → stop and tell Sumanth: "Run your secrets file: & 'C:\Users\suman\my-secrets.ps1'"

**0b — notebooklm auth**
```bash
notebooklm list
```
If "Authentication expired" → run `notebooklm login` → user re-authenticates → resume.

**0c — Record creator info**
Fill in before proceeding:
```
CREATOR: [Name]
LINKEDIN_URL: https://www.linkedin.com/in/[handle]/
YOUTUBE_HANDLE: (to be found in Step 1)
WEBSITE: (to be found in Step 1)
DATE: [Month Year]
```

---

## STEP 1 — Data Source Discovery (5-10 min)

**This step determines the entire rest of the process. Never skip it.**

Run these 3 checks before touching any Apify actor.

---

### 1a — Find their YouTube channel

```bash
playwright-cli open "https://www.youtube.com/@[likely-handle]/videos"
```

Validation checklist — the channel is VALID only if ALL of these are true:
- [ ] Channel exists (not 404)
- [ ] Videos are about their area of expertise (NOT personal/hobby/travel/local language)
- [ ] Has 10+ videos
- [ ] Videos have meaningful views (not all under 500)
- [ ] Content is in English or a language relevant to the research

If the channel FAILS any validation check → mark as "no official channel" → proceed to interview search below.

**Interview video search (when no valid channel exists):**
```bash
playwright-cli goto "https://www.youtube.com/results?search_query=[creator+name]+linkedin"
# Also try: [creator+name]+podcast, [creator+name]+personal+brand
```

Quality threshold for interview videos:
- 20+ minutes long (short clips have too little framework depth)
- From a credible podcast/channel (not sub-100-subscriber channels)
- English language
- About their area of expertise

**PAUSE POINT 1 — Ask Sumanth before proceeding:**
> "[Name] has no official YouTube channel with relevant content. I found [N] interview videos from other channels:
> [List top 5–8 with title + duration]
> Should I use these interview videos as the YouTube source? (yes/no)"

If yes → compile full list and proceed.
If no → skip YouTube analysis entirely. Only run L1-L10 LinkedIn questions.

---

### 1b — Check LinkedIn data availability

```bash
# Start the run
curl -s -X POST "https://api.apify.com/v2/acts/harvestapi~linkedin-profile-posts/runs" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $APIFY_API_KEY" \
  -d '{"profileUrl": "https://www.linkedin.com/in/[handle]/", "resultsLimit": 50}'

# Save the run ID, poll until SUCCEEDED, then fetch dataset
# CRITICAL: Use defaultDatasetId from run data, then:
curl "https://api.apify.com/v2/datasets/[datasetId]/items?limit=200"
```

**Reality check:** LinkedIn auth-gates almost every profile. Expected result = 0 posts.

**PAUSE POINT 2 — Ask Sumanth if LinkedIn returns 0:**
> "[Name]'s LinkedIn is auth-gated — 0 posts returned. For LinkedIn analysis, options are:
> A) Use interview/website content as proxy for their LinkedIn thinking (recommended)
> B) Try to find public post archives — no guarantee, takes extra time
> C) Skip LinkedIn-specific questions entirely
> Which do you prefer?"

If A or C → adapt questions accordingly and proceed.
If B → search for archives via playwright-cli before proceeding.

---

### 1c — Find website / newsletter

```bash
playwright-cli goto "https://www.[creatorname].com"
# Also check: [name].substack.com, beehiiv pages, their LinkedIn bio for website link
```

Target: Newsletter archive with 10+ issues (like justinwelsh.me/newsletters — each issue = rich content source in notebooklm).

If newsletter/blog found with 10+ posts → add to source inventory.

---

### 1d — Fill Source Inventory Before Proceeding

```
SOURCE INVENTORY FOR [Name]:
─────────────────────────────
LinkedIn posts:   [N posts] OR [0 — auth-gated + fallback choice: A/B/C]
YouTube channel:  [N videos from own channel] OR [no official channel]
Interview videos: [N videos] (only if no official channel)
Newsletter/Blog:  [N articles at URL] OR [none found]
─────────────────────────────
TOTAL USABLE SOURCES: [N]
NOTEBOOK STRATEGY:
  ≤50 sources → single notebook
  >50 sources → two notebooks (YouTube | LinkedIn/Newsletter split)
QUESTIONS TO RUN:
  Full 22 — if both LinkedIn data + YouTube data available
  12 YouTube only — if no LinkedIn data
  10 LinkedIn only — if no YouTube data
  Custom mix — if partial data (note which questions to skip)
```

---

## STEP 2 — Data Collection via Apify (5-15 min)

Run only the actors for sources confirmed available in Step 1.

### 2a — LinkedIn posts (if Apify returned data)

```bash
# Already ran in Step 1b — just fetch and format
curl "https://api.apify.com/v2/datasets/[datasetId]/items?limit=200" \
  -H "Authorization: Bearer $APIFY_API_KEY" > posts/raw-data/[creator]-linkedin-apr2026.json

# Format as plain text for notebooklm:
# Each post formatted as:
---
POST DATE: [date] | LIKES: [n] | COMMENTS: [n] | SHARES: [n]
[full post text]
---
# Save to: posts/raw-data/[creator]-linkedin-formatted.txt
```

### 2b — YouTube channel videos (if valid official channel found)

```bash
curl -s -X POST "https://api.apify.com/v2/acts/streamers~youtube-channel-scraper/runs" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $APIFY_API_KEY" \
  -d '{"startUrls": [{"url": "https://www.youtube.com/@[handle]"}], "maxResults": 100}'
# CRITICAL: Use startUrls field with {"url":"..."} format
# NOT "channelUrl" — that field causes invalid-input error

# After SUCCEEDED: fetch dataset → sort by viewCount desc → take top 30
# Save to: posts/raw-data/[creator]-youtube-top30-urls.txt
```

### 2c — Interview videos (if no official channel, using interviews)

```bash
# No Apify run needed — URLs compiled manually from playwright-cli search
# Save to: posts/raw-data/[creator]-youtube-interviews-urls.txt
# Format: one URL per line
# Comment format: # [view count] | [duration] | [title]
```

### 2d — Newsletter/website articles (if found)

```bash
# No Apify run needed — collect URLs manually
# Save to: posts/raw-data/[creator]-newsletter-urls.txt
# Add directly to notebooklm as web URLs (it fetches text natively)
```

---

## STEP 3 — notebooklm Notebook Setup (10-15 min)

### 3a — Create notebook(s)

```bash
notebooklm create "Creator Research: [Name] — [Month Year]"
# SAVE THE NOTEBOOK ID — every subsequent command needs it
```

Two-notebook strategy (if >50 sources):
```bash
notebooklm create "Creator Research: [Name] — YouTube/Interviews — [Month Year]"
notebooklm create "Creator Research: [Name] — LinkedIn/Newsletter — [Month Year]"
```

### 3b — Add YouTube video URLs (preferred method — notebooklm fetches transcripts natively)

```bash
# For each URL in the top-30 list OR interview list:
notebooklm source add -n [notebook-id] https://www.youtube.com/watch?v=[video-id]
# If a URL fails with "API returned no data" → skip and continue
# Cause: video has no captions — not fixable
```

### 3c — Add text + website sources

```bash
# LinkedIn formatted text file:
notebooklm source add -n [notebook-id] "C:/Users/suman/Reachr Linkedin/posts/raw-data/[creator]-linkedin-formatted.txt"

# Newsletter URLs (one by one):
notebooklm source add -n [notebook-id] https://[newsletter-url]
```

### 3d — Verify

```bash
notebooklm list
# Confirm source count is correct
# If hitting 50 → stop adding (Standard tier limit) — split into two notebooks
```

---

## STEP 4 — Research Questions (30-45 min)

**Start conversation:**
```bash
notebooklm ask -n [notebook-id] -c new "[first question]"
# SAVE THE CONVERSATION ID from the response
```

**All follow-up questions (use same conversation ID):**
```bash
notebooklm ask -n [notebook-id] -c [conversation-id] "[question]"
```

**Save every answer to the research file as you go — don't batch at the end.**

**IMPORTANT — When LinkedIn data is unavailable:** Prefix each Section A question with:
> "Based on what this creator says in their interviews about their LinkedIn approach and content strategy..."

---

### SECTION A — LINKEDIN ANALYSIS (10 Questions)

**L1 — Narrator Persona**
> "What recurring narrator persona does this creator embody across their highest-engagement posts? Are they the 'insider disclosing secrets,' the 'analyst seeing what others miss,' the 'builder teaching from mistakes,' or something else entirely? Give 3 specific posts as evidence and quote the exact language that establishes the persona in each."

**L2 — Audience Emotional Driver**
> "What is the underlying emotional trigger driving engagement in posts with 50+ comments — fear of career irrelevance, desire for insider access, identity validation, moral outrage, or something else? For the 5 highest-comment posts, identify: the hook line, the emotional trigger it activates, and why that specific trigger caused readers to comment rather than just like."

**L3 — Hook Anatomy (5 structural types)**
> "What are the 5 most structurally distinct hook patterns across all posts with 30+ likes? For each pattern provide: (1) the template structure, (2) 2 exact examples from their posts, (3) the psychological mechanism it uses — FOMO, shock, identity threat, curiosity gap, social proof, or contrarian claim."

**L4 — Body Construction Logic**
> "How does this creator build from the opening hook to the central insight? What is the specific logic chain — does it follow problem→evidence→reframe, story→contrast→lesson, claim→counter-claim→synthesis, or another sequence? Identify the exact beats from 3 different high-performing posts and label each beat."

**L5 — CTA Engineering**
> "Across all posts with 50+ comments, what are the exact CTA formulations used? Categorize by type: participation CTAs ('Should I post this?'), opinion CTAs ('Which side are you on?'), P.S. bombshells (a second hook at the end), hard landings (no CTA — just ends on the most provocative sentence), and community/link CTAs. For each type, give the exact wording and the comment count it generated."

**L6 — Contrarian POV Construction**
> "What is the single, repeating contrarian belief this creator holds that most of their audience would initially resist? How do they build the argument to overcome that resistance — what evidence do they use, in what sequence, and how do they frame the conclusion so it feels like a revelation rather than a lecture? Quote the exact lines from their most-argued posts."

**L7 — Personal Story Architecture**
> "What personal stories does this creator reference most often? For each recurring story: (1) What is the core incident? (2) What status or credibility does it establish? (3) Which posts reference it and what engagement did those posts generate? (4) Is the story told with full detail or used as a brief allusion? Map the story to the type of post it appears in."

**L8 — Content Evolution ★ (USE CREATOR-SPECIFIC MODIFIER BELOW)**
> "How did this creator's LinkedIn content strategy change from their earliest posts to their most recent ones? What changed in: hook structure, topic focus, CTA format, post length, and ratio of personal vs. analytical content? What specific audience signals appear to have driven those changes?"

| Creator | L8 Modifier |
|---------|-------------|
| Vaibhav Sisinty | ✅ Done |
| Justin Welsh | Add: "Structure around follower milestones: 0→1K, 1K→10K, 10K→50K, 50K→100K" |
| Jasmin Alic | Add: "Focus on how his teaching framework evolved — when did his most-shared frameworks first appear?" |
| Lara Acosta | Add: "Focus EXCLUSIVELY on her first 90 days. Do not reference current content." |
| Kallaway | Add: "Focus on format evolution — when did he shift to video-first, and what drove that shift?" |
| Richard van der Blom | Add: "Focus on data-backed posts only — what algorithm mechanics does he cite with actual numbers? Map how his research findings translate into posting tactics." |
| Nicolas Cole | Add: "Focus on his Attention-to-Value framework specifically — map the exact structure. How does he open, build, and land an idea differently from storytelling creators?" |
| Matt Barker | Add: "Focus exclusively on LinkedIn-specific copy formulas — what makes his hooks and body copy structurally different from generic content advice?" |
| New creator | Standard question |

**L9 — Format and Cadence Pattern**
> "What is the mix of post formats — text-only, image, video, carousel, poll? For each format: what is the average comment-to-like ratio? Is there a day-of-week or week-in-month pattern where certain formats appear? What format has the highest comment-to-like ratio?"

**L10 — Scriptwriting Premise Transfer**
> "Identify the 5 LinkedIn posts with the most transferable argument structures. For each, extract the raw premise formatted as '[Audience believes X. But the data shows Y. Which means Z for anyone doing W].' These should be immediately reusable as script outlines."

---

### SECTION B — YOUTUBE ANALYSIS (12 Questions)

*Skip this section if Sumanth said no to YouTube data.*

**Y1 — Title and Thumbnail Formula**
> "What are the exact structural patterns in video titles for the top 20% by view count? Identify 3–5 repeating title formulas with examples. For thumbnails: what consistent visual signals appear in the highest-performing videos?"

**Y2 — Opening Hook Engineering (first 45 seconds)**
> "Transcribe or closely paraphrase the exact opening 45 seconds of the 5 most-viewed videos. For each: (1) the hook formula used — promise, shock disclosure, rhetorical question, demonstration, or identity challenge; (2) the first sensory or conceptual element introduced; (3) the earliest moment a specific number, name, or dollar amount appears. What pattern repeats across all 5?"

**Y3 — Mid-Video Retention Architecture ★ (USE CREATOR-SPECIFIC MODIFIER)**
> "Where in the video does this creator deliberately re-engage drifting viewer attention? What exact verbal or visual techniques appear at roughly the 30%, 50%, and 70% marks? Quote specific phrases used across multiple videos."

| Creator | Y3 Modifier |
|---------|-------------|
| Kallaway | Replace with: "Map the second-by-second structure for scripts under 90 seconds: 0–3s, 3–10s, 10–30s, 30–60s, 60–90s" |
| All others | Standard question |

**Y4 — Information Pacing and Density**
> "How dense is information delivery in the top 10 videos — roughly how many distinct ideas or data points appear per minute? Do they front-load value or build toward a climax? Is there a deliberate lower-density section mid-video? How does pacing differ between tutorial and analysis videos?"

**Y5 — Topic Architecture and Series Design ★ (USE CREATOR-SPECIFIC MODIFIER)**
> "What are the 3–5 recurring content pillars this creator rotates between? How does performance differ between series videos and standalone videos? Which pillar generates the most comments relative to views?"

| Creator | Y5 Modifier |
|---------|-------------|
| Justin Welsh | Add: "Map pillars to his documented business journey — which appeared first vs. added as audience grew?" |
| All others | Standard question |

**Y6 — Emotional Narrative Arc**
> "What emotional journey does this creator take the viewer on in their top 5 videos? Map it beat by beat: what emotion is activated at the opening, what happens mid-video, and what state should the viewer be in at the final 30 seconds? How does this arc vary by video type?"

**Y7 — Comment Sentiment Archaeology**
> "In the top 10 highest-comment videos, what patterns appear in the most-upvoted viewer comments? Categorize: completing an idea the creator left open, sharing their own version of the story, pushing back on a claim, asking a follow-up, or expressing identity validation. What does this distribution reveal about where the creator leaves the most intellectual room?"

**Y8 — Collaboration and Borrowed Audience Signal**
> "What guest appearances, named collaborations, or high-status name-drops appear in top-performing videos? How did videos with guests perform relative to solo videos? Which specific names appear most frequently in high-performing titles or transcripts?"

**Y9 — Cross-Platform Content Transfer**
> "Which YouTube video topics also appear as LinkedIn posts? When the same topic was covered on both platforms: how was the framing different, what did YouTube contain that LinkedIn didn't, and which platform got stronger engagement? What does this imply about which platform fits which content type for this creator?"

**Y10 — Production Format and Quality Signal**
> "What production formats dominate the top 10 videos — talking head, screen share, B-roll, live demo, interview, or mixed? Is there a relationship between production investment and view count, or is there an authenticity premium where rougher formats get stronger comment engagement?"

**Y11 — Untapped Topic Adjacency ★ (ALWAYS ADD D2C REFRAME)**
> "What topics has this creator NOT covered that their audience is clearly signalling interest in? Give 5 specific, actionable premises that extend their current territory without breaking their positioning. For each: the premise, the audience desire it addresses, and why it fits their established voice."
>
> After identifying the 5 topics, add: "For each premise, reframe it for the Indian D2C distribution context — how would Sumanth at Reachr cover this topic from a content distribution angle?"

**Y12 — Scriptwriting Premise Transfer**
> "Select the 5 videos with the most transferable argument structures. For each: (1) the raw premise as '[Most people believe X. But the data shows Y. Which means Z for anyone doing W]'; (2) the primary narrative device used; (3) the exact sequence of the revelation. Format each as a reusable script template with labelled beats."

---

## STEP 5 — Extract 7 Deliverables (15-20 min)

Compile from all question answers into these sections:

**D1 — Hook Formula Bank**
Minimum: 5 LinkedIn hooks (from L3) + 3 YouTube hooks (from Y2)
Format: `[Pattern Name] | [Template] | [Exact Example from their content] | [Psychological Mechanism]`

**D2 — CTA Bank**
Minimum: 5 CTAs with engagement data (from L5)
Format: `[CTA Type] | [Exact Wording] | [Comment Count Generated]`

**D3 — Core Contrarian POV Library**
Minimum: 3 transferable premises (from L6 + L10 + Y12)
Format: `[Raw Premise] | [Evidence Sequence] | [Revelation Framing] | [Reachr-Adapted Version]`

**D4 — Post + Script Structure Blueprint**
1 LinkedIn structure (from L4) + 1 video structure (from Y6)
Format: labelled beat-by-beat map

**D5 — Personal Story Bank**
All recurring stories (from L7)
Format: `[Story Summary] | [Credibility Established] | [Post Types It Appears In]`

**D6 — Untapped Topic List**
5 topics with D2C reframes (from Y11)
Format: `[Topic Premise] | [Reframed for Reachr/D2C Distribution Context]`

**D7 — Forbidden Patterns**
What didn't work — angles/formats with low engagement (from L9 + Y10 + L8 evolution)
Format: `[Pattern] | [Why It Underperforms] | [What to Do Instead]`

**Bonus — Divergence Table**
Compare this creator vs. previously researched creators across:
Hook style | CTA style | Story ratio | Contrarian POV type | Content evolution path | Primary platform strength

---

## STEP 6 — Save Research File

```
Location: C:\Users\suman\Reachr Linkedin\posts\creator-research-[name-slug]-[monthyear].md

Required header:
# Creator Research: [Full Name] — [Month Year]
**Sources used:** [N YouTube/interview videos] | [N LinkedIn posts / fallback type] | [N newsletter issues]
**Data quality note:** [Be explicit about any auth-gating, missing sources, or fallbacks used]
**Notebooks:** [notebook ID(s) + conversation ID(s) for future reference]

Then: D1 through D7 + Bonus + Top 3 insights to apply this week
```

---

## ERROR HANDLING REFERENCE

| Failure | Cause | Fix |
|---------|-------|-----|
| Apify API key blank | Env var not loaded | `& 'C:\Users\suman\my-secrets.ps1'` in new terminal |
| LinkedIn returns 0 posts | Auth-gating (almost always) | PAUSE → ask Sumanth: A/B/C fallback choice |
| YouTube channel has no relevant content | Personal/hobby channel | PAUSE → ask Sumanth: use interview videos? |
| notebooklm auth expired | Google session expired (~90 days) | `notebooklm login` → user re-authenticates |
| YouTube actor invalid-input error | Wrong input field used | Use `startUrls: [{"url":"..."}]` NOT `channelUrl` |
| Apify dataset fetch 404 | Using wrong endpoint | `/v2/datasets/[datasetId]/items` not `/v2/acts/[actor]/runs/[runId]/dataset/items` |
| notebooklm source add fails | Video has no captions | Skip and continue |
| notebooklm hits 50-source limit | Standard tier limit | Stop adding, create second notebook |

---

## CREATOR STATUS TRACKER

| Creator | Status | Data Sources | File |
|---------|--------|-------------|------|
| Vaibhav Sisinty | ✅ Complete | 50 LinkedIn posts + YouTube own channel | `creator-research-vaibhav-sisinty-april2026.md` |
| Justin Welsh | ✅ Complete | 19 interview videos + 40 newsletter issues | `creator-research-justin-welsh-april2026.md` |
| Jasmin Alic | ✅ Complete | 15 interview videos (LinkedIn proxy) | `creator-research-jasmin-alic-april2026.md` |
| Lara Acosta | ✅ Complete | 39 YouTube videos (official channel, LinkedIn proxy) | `creator-research-lara-acosta-april2026.md` |
| Kallaway | ⏳ Pending | TBD | — |
| Richard van der Blom | ⏳ Pending | TBD | — |
| Nicolas Cole | ⏳ Pending | TBD | — |
| Matt Barker | ⏳ Pending | TBD | — |

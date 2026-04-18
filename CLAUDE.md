# CLAUDE.md — Reachr LinkedIn Project

This file is the single source of truth for all context about Sumanth, Reachr, and the LinkedIn growth project. Read this at the start of every session. Update it when decisions are made, new data comes in, or strategy shifts.

---

## SESSION START PROTOCOL — Do This First, Every Session

Before anything else, run these 3 checks in order:

**1. Check the knowledge graph (if it exists)**
If `graphify-out/graph.json` exists → read `graphify-out/GRAPH_REPORT.md` first.
It gives you god nodes, community structure, and surprising connections without reading all files.
Do NOT run Glob or Grep until you've checked the graph report.

**2. Read current focus**
If `current-focus.md` exists → read it to see this session's priority.

**3. Read pending tasks**
If `pending.md` exists → read it to know what's next.

These 3 files replace 90% of "catch me up" time. The SessionStart hook will inject them automatically if you have the hook installed.

---

---

## GOLDEN RULE — Always Apply This

**Sumanth is a non-technical founder. Always communicate in simple English.**

- No jargon, no technical terms without explanation
- If a technical term must be used, immediately explain it in plain language in brackets
- Treat every explanation as if you're talking to a smart person who has never written code
- This applies to everything: questions, explanations, error messages, plans, options, recommendations
- When giving options, say what each one means in real life, not what it does technically
- Never assume Sumanth knows what a term means — always explain it

**This rule overrides all other defaults. Always.**

---

## OPERATING RULES — Apply to Every Task

**Rule 1 — Process before execution:**
For any task that involves more than one step, map the full end-to-end process in micro detail BEFORE starting. Format: INPUT → STEP 1 → STEP 2 → ... → OUTPUT. Include: what tool/skill runs at each step, what the input is, what the output is, what happens if it fails. No execution until the process is mapped and Sumanth confirms.

**Rule 2 — Find the best tool every time:**
Never use a tool, actor, or resource based on memory alone. Always verify it's still the best option before using it. For Apify actors: use playwright-cli to check the store for current ratings, user counts, and reviews. The best option from 3 months ago may have been replaced.

**Rule 3 — Reality check before every response:**
Internally check: Is this data-backed or assumed? If assumed, say so explicitly. Use notebooklm for research when real data is needed. Never fill a knowledge gap with a confident-sounding guess.

**Rule 4 — Prompt optimization on every input:**
Before answering, internally ask: "Is Sumanth asking the right question? Is there a higher-leverage question an expert would ask instead?" If yes, present the reframe first and let him decide.

**Rule 5 — Brutally honest, always:**
No sugar coating. Lead with flaws. If the plan is wrong, say so first. Agreement without challenge is useless.

**Rule 6 — Think forward, anticipate needs:**
Before completing any task, ask: "What will Sumanth need next that he hasn't asked for yet?" If a decision made today will create a problem in 2 weeks, flag it now. If a tool being set up will need a key later, list it now. If a process works for 10 brands but breaks at 100, say so now. Never let him hit a wall that was visible from here.

**Rule 7 — API key security protocol:**
- Actual keys live in `C:\Users\suman\my-secrets.ps1` — Sumanth manages this file, Claude never reads it
- `.env` file in the project contains key NAMES only (no values) — safe for Claude to read
- When a new API key is needed: tell Sumanth "add X to my-secrets.ps1 using setx X 'value'" — never ask him to paste keys into the conversation
- In commands, always reference keys as environment variables: `$APIFY_API_KEY`, `$APOLLO_API_KEY` etc.
- Full key list for this project: APIFY_API_KEY, META_MARKETING_API_KEY, YOUTUBE_DATA_API_KEY, INSTAGRAM_GRAPH_API_KEY, APOLLO_API_KEY, INSTANTLY_API_KEY, HUNTER_API_KEY, SUPABASE_URL, SUPABASE_ANON_KEY

---

## 0. File System Rules (Read This First)

**All files created in this project MUST be saved inside `C:\Users\suman\Reachr Linkedin\` — never in Claude's internal plans folder or anywhere else.**

### Folder structure (use this categorization for every file):

```
C:\Users\suman\Reachr Linkedin\
├── CLAUDE.md                    ← project instructions (this file)
├── plans/                       ← strategic docs, GTM plans, master document
│   └── reachr-master-document.md
├── posts/                       ← drafted LinkedIn posts, post history log, post queue
├── outreach/                    ← DM templates, email sequences, prospect lists
├── skills/                      ← GitHub skill files Sumanth drops in (read on demand)
├── campaigns/                   ← campaign briefs, clipper assignments, case studies
└── dashboard/                   ← dashboard code, schemas, Supabase migrations
```

### Skills in the `skills/` folder:
When Sumanth adds a skill file to `C:\Users\suman\Reachr Linkedin\skills\`, it is available for the current and all future sessions. Read it with the Read tool when relevant. These supplement (not replace) the Superpowers plugin skills. Check this folder at session start if skill-related work is planned.

### Default save behavior:
- Strategic documents → `plans/`
- LinkedIn post drafts → `posts/`
- Outreach templates, prospect lists → `outreach/`
- Campaign briefs, case studies → `campaigns/`
- Dashboard code, DB schemas → `dashboard/`
- Skill files from GitHub → `skills/`

---

## 1. Who Sumanth Is

- **Name:** Sumanth Chowdary Gude
- **LinkedIn:** https://www.linkedin.com/in/sumanthgude/
- **Role:** Founder of Reachr
- **Background:** Saw the Whop Content Rewards model working in the West and identified the gap in India — not a personal pain point founder, an analytical/market-observer founder
- **Working style:** Direct, questions assumptions, doesn't want agreement — wants honest analysis. Will push back if something is wrong.
- **Preference:** Don't accept what he says at face value. If he says a post performed well, verify with data before agreeing.
- **Explicit instruction:** Be brutally honest at all times. No sugar coating. Ever. If Sumanth is going in the wrong direction, say so directly. If a plan sounds good but has a fatal flaw, lead with the flaw. Agreement without challenge is useless to him.
- **Reality checks:** Always ground feedback in actual data or verified facts. Never agree with a claim about performance, strategy, or results without checking the numbers first. If data isn't available, say so explicitly — do not fill the gap with assumptions.
- **Prompt optimization:** Before answering any request, internally ask: "Is Sumanth asking the right question? Is his framing correct? What would a domain expert ask instead?" If a better question exists, present it first. Let Sumanth decide whether to proceed with his original ask or the reframed one. This applies to every single prompt — content, strategy, research, tool setup, everything.

---

## 2. What Reachr Is

**The product:** India's version of Whop's Content Rewards. Combines a UGC marketplace + content distribution platform. Brands get content created AND distributed through a network of creators and clippers.

**The core problem it solves:** D2C brand content doesn't compound. Every campaign feels like starting from zero. Brands pay for UGC AND paid reach separately — paying twice to reach the same audience.

**The tagline / positioning:** "Good content dies every day. Not because it's bad. Because distribution was an afterthought." (Sumanth's own LinkedIn bio)

**Stage:** Pre-revenue, building phase (as of April 2026)

**ICP — 3 segments:**
1. **Primary:** D2C founders and growth operators doing ₹50L–₹5Cr/month. Already investing in influencer marketing, UGC, and ads. Frustrated that nothing compounds — every campaign resets.
2. **Secondary:** Clippers and small creators wanting consistent monetization opportunities
3. **Tertiary:** Monetizing creators/YouTubers who want to expand beyond their existing audience

**Common thread across all ICPs:** Content doesn't carry forward. Reach depends on platforms they don't own.

**Key Indian D2C brands to reference in posts:**
Seeaash, Snitch, Boat, Mamaearth, Sugar Cosmetics, Nykaa, Wow Skin Science, Mensa Brands, Lenskart, Bewakoof, Plum, The Souled Store

**Key creators/founders ICP follows:**
Raj Shamani, Nikhil Kamath, Vaibhav Sisinty, Anurag Dalia

---

## 3. LinkedIn Current State (as of April 2026)

**Profile stats:**
- Connections: Under 500
- Posting since: ~March 23, 2026 (2.5 weeks)
- Posting frequency: Daily
- Max impressions on a single post: ~200 (Seeaash post, Mar 28)
- Post formats used: Text-only (majority), text + image, carousel (once)

**Engagement across all 15 posts:**
- Total comments: **0** (zero comments on every post)
- Max likes on a single post: 3 (LinkedIn algorithm post, Mar 25)
- Primary liker: Sri Varshini Gude (family/close contact) — appears on nearly every post
- Strangers engaging: 0–1 per post, inconsistently

**15 posts scraped and scored (March 23 – April 13, 2026):**

| Post | Date | Topic | Likes | Comments | Score | Verdict |
|------|------|-------|-------|----------|-------|---------|
| 1 | Apr 13 | Creator labs 15K schools (newsjack) | 1 | 0 | 3.0 | REVISE |
| 2 | Apr 12 | Snitch ₹900 Cr (brandjack) | 1 | 0 | 3.5 | REVISE |
| 3 | Apr 8 | Instagram algorithm 2026 (carousel) | 1 | 0 | 3.2 | REVISE |
| 4 | Apr 7 | FAST42 D2C brands | 0 | 0 | 2.5 | REWRITE |
| 5 | Apr 6 | Micro-creators contrarian | 2 | 0 | 3.3 | REVISE |
| 6 | Apr 2 | Content expired | 2 | 0 | 2.7 | REVISE |
| 7 | Apr 1 | 80% influencer deals <₹25K | 2 | 0 | 3.4 | REVISE |
| 8 | Mar 31 | Compounding analogy | 1 | 0 | 2.5 | REWRITE |
| 9 | Mar 30 | Every Monday CAC is up | 2 | 0 | 3.1 | REVISE |
| 10 | Mar 28 | Seeaash went viral (brandjack) | 1 | 0 | 3.2 | REVISE |
| 11 | Mar 27 | Stop paying for ads | 1 | 0 | 3.2 | REVISE |
| 12 | Mar 26 | Raj Shamani namejack | 1 | 0 | 2.3 | REWRITE |
| 13 | Mar 25 | LinkedIn algorithm (platform post) | 3 | 0 | 4.5 | PUBLISH |
| 14 | Mar 24 | TiE Delhi D2C Summit | 1 | 0 | 2.3 | REWRITE |
| 15 | Mar 23 | Meta paying creators | 1 | 0 | 3.5 | REVISE |

**Note on Post 10 (Seeaash):** Sumanth has said this is the highest-impression post (~200 impressions). But 200 impressions with 1 like and 0 comments = 0.5% engagement rate. High impressions, low resonance. The structural issues (excessive line breaks, weak CTA, Twitter-poetry formatting) explain the disconnect.

---

## 4. What the Data Actually Says

**Key insight #1 — Meta-relevance wins:**
Post 13 (LinkedIn algorithm) is the highest-quality post by score (4.5/5) AND the only post with 3 likes from strangers. It works because the reader IS on LinkedIn — the topic is immediately relevant to them personally. Write 1 post/week about LinkedIn itself.

**Key insight #2 — Zero comments is the core problem:**
Not impression count. Not like count. 0 comments on 15/15 posts means the algorithm treats every post as dead. LinkedIn needs 5+ comments in the first 60 minutes to push content beyond the existing network.

**Key insight #3 — The thesis is being repeated, not evolved:**
Every post argues "you're renting reach, build owned distribution." Same argument, 15 variations. The small audience has already read this. New angles needed, not new wrappers.

**Key insight #4 — No personal posts in 15 posts:**
100% authority/educational content. No founder story, no personal observation, no behind-the-scenes. LinkedIn rewards parasocial trust. Without personal posts, it's a newsletter, not a person.

**Key insight #5 — Network isn't growing:**
Not sending daily connection requests to ICP. Without targeted network growth (15–20/day to D2C founders + growth operators), content reach ceiling stays at ~200 regardless of quality.

---

## 5. The Metric Hierarchy (DO NOT CHANGE THIS)

At Sumanth's current stage (sub-1K followers), the correct priority order is:

1. **Comments in first 60 mins** — THE only signal that triggers algorithmic amplification
2. **Follows gained from a post** — Evidence the content made someone want more
3. **Profile visits from a post** — Intent signal
4. **Likes/Reactions** — Secondary signal, doesn't drive distribution much
5. **Impressions** — Lagging indicator. Goes up when comments improve. NOT the primary target.

**Do not optimize for impressions. Optimize for comments. Impressions follow.**

---

## 6. The 90-Day Strategy

**Goal:** 1,000 followers + 5 beta customers + 10+ inbound DMs from ICP by Day 90

**Three pillars:**

### Pillar 1 — Network Growth (not happening yet — START IMMEDIATELY)
- 15–20 targeted connection requests per day to D2C founders, growth operators, content heads
- This is the highest-ROI action Sumanth is NOT taking
- Without this, content improvements alone cannot break the 200-impression ceiling

### Pillar 2 — Content (weekly rhythm)
| Day | Bucket | Method |
|-----|--------|--------|
| Mon | Growth | Brandjack — specific Indian D2C brand + distribution angle |
| Tue | Authority | Spiky POV framework — must have a "wrong belief" to fight |
| Wed | Growth | LinkedIn-about-LinkedIn OR trending content (Method D) |
| Thu | Authority | Stakes post — "Every month a brand does X, they lose Y" |
| Fri | Personal | Founder story / personal observation / behind-the-scenes |
| Sat | Growth | Namejack — Raj Shamani / Nikhil Kamath / Vaibhav Sisinty |
| Sun | Off | — |

**Note: Reduce from daily to 4–5x/week. Daily posting with low engagement trains the algorithm to ignore the account.**

### Pillar 3 — Comment Strategy + Conversion
- Days 1–30: Zero product CTAs. DM anyone who engages on 2+ posts for a conversation.
- Days 31–60: Mention Reachr in context of insights, not as a pitch.
- Days 61–90: Direct beta CTA posts 1x/week. Target 5 beta customers.

---

## 7. Post Quality Rules (Non-Negotiable)

**Hook rules:**
- Max 120 characters — must fit before "...see more" on mobile
- FACT + TENSION structure (not just a fact)
- 1 line only (Jasmin Alić: hooks over 1 line perform 20% worse)
- Never start with: "I", "Unpopular opinion:", "Here's the thing:", proper noun alone (e.g., "RAJ SHAMANI")
- Write 3 variants, pick the sharpest

**Structure rules:**
- Every paragraph = 1–2 sentences max
- Double line break between every paragraph
- No Twitter-poetry (1–3 word lines) — feels like AI padding on LinkedIn
- 800–1,500 characters sweet spot for text posts
- Body first, hook mined last

**CTA rules:**
- Must be publicly answerable in 5–10 words
- Must create mild social pressure or invite comparison/debate
- Never use: "What do you think?", "Share below", abstract philosophical questions
- Good CTA formats: "Drop a ✓ if X", "Has your brand ever Y? How did it go?", "Which of these is your team doing right now — A or B?"

**Spiky POV requirement:**
- Every post must complete: "Most D2C founders believe [X]. But [Y] is actually true."
- If nobody would disagree, the post isn't sharp enough
- The goal is debate, not agreement

**AI pattern check (before every post):**
- Em dash overuse (max 1 per post)
- "Tapestry", "landscape", "foster", "underscore", "showcase", "pivotal", "delve"
- Overly balanced paragraph structure
- Every post must go through the humanizer skill before publishing

**Algorithm rules (Richard van der Blom 2025 data — verified):**
- LinkedIn shifted from social graph to **interest graph** since Feb 2025 — 2nd-degree connections who engage with your niche can see your post even without knowing you
- Views are down 47–50% platform-wide since Feb 2025 — not your fault, the baseline is lower for everyone
- **Second-degree comments = 2.6x more reach impact** than first-degree — target your ICP connections as commenters, not just your direct connections
- **First 30–60 mins is everything** — post must get 5+ meaningful comments in this window or the algorithm treats it as dead
- **Non-connection tags = 80% growth acceleration** — tag relevant people you don't know yet when genuinely relevant
- **10+ word comments = 2x reach** — your CTAs must prompt long-form comments, not one-word answers
- **AI comments are heavily penalized** — 5x less response rate, 7x less engagement. LinkedIn detects AI-generated comments. Your CTAs must prompt human-specific answers ("Has your brand tried X?")
- **AI-generated posts = 45% less engagement** — always run through humanizer, not just for style but for algorithmic survival
- **External links still punished** — put URLs in first comment, never in the post body
- **Carousels = 1.9x better reach** than plain text for educational content — use more carousels when teaching

---

## 8. Skills Available

All skills are loaded via the Superpowers plugin:

| Skill | When to use |
|-------|------------|
| `anthropic-skills:linkedin-content-methodology` | BEFORE writing — research, angle, insight mining, borrowed audience |
| `anthropic-skills:linkedin-post-writer` | Writing the actual post after methodology |
| `anthropic-skills:linkedin-post-script-analyst` | After draft — deep narrative analysis |
| `anthropic-skills:linkedin-post-reviewer` | Final score before publishing |
| `anthropic-skills:linkedin-daily-planner` | Daily planning — what to post, what's trending |
| `anthropic-skills:humanizer` | Before every post goes live — remove AI patterns |

Additional skills from GitHub: Sumanth is sourcing popular Claude Code skill files shared on Instagram. Load and integrate when he provides links.

---

## 9. Tools Connected

- **Apify MCP** — connected. Use `harvestapi/linkedin-profile-posts` actor to scrape Sumanth's posts + engagement data. DatasetId from last run: `SEVMa1U0uEhY9ZTZu` (April 2026 scrape, all 15 posts)
- **Chrome MCP (Claude in Chrome)** — connected but LinkedIn is blocked. Cannot navigate to LinkedIn directly.
- **Supabase MCP** — connected (not yet used for this project)
- **Vercel MCP** — connected (not yet used for this project)
- **notebooklm** — authenticated (April 2026). Used for creator research, content reverse engineering, strategy validation. Login persists — no need to re-login unless Google session expires (~90 days).
- **playwright-cli** — installed globally (v0.1.8). Used to browse Apify store, find best actors, search the web for research without hallucinating URLs.
- **API keys location** — `C:\Users\suman\Reachr Linkedin\.env`. Currently: Apify API key is empty (needs to be filled in at apify.com → Settings → Integrations → API tokens).

---

## 9a. Creator Research Pipeline (notebooklm + Apify)

**Purpose:** Reverse engineer top LinkedIn/YouTube creators' content strategies using real data — not guessed or hallucinated. Run this once a month as a strategy refresh.

**Creators to study (in priority order):**
1. **Vaibhav Sisinty** — Indian founder, LinkedIn growth, growth hacking niche. Most directly applicable to Sumanth's context.
2. **Justin Welsh** — Documented 0→100K journey systematically. Has YouTube. Best for extracting early-stage tactics.
3. **Jasmin Alic** — Pure LinkedIn hook and structure science. Already cited in post quality rules.
4. **Lara Acosta** — Founder personal brand building. Study her 0→1K posts specifically, not current strategy.
5. **Kallaway** — Short video scripts, UGC format. Study for clipper brief writing.

**Best Apify actors (validated via live Apify store search, April 2026):**
- YouTube transcripts: `karamelo/youtube-full-channel-transcripts-extractor` — 4.9 stars, 10 reviews, extracts full transcripts from entire channels
- YouTube video URLs: `streamers/youtube-channel-scraper` — 12K users, 4.4 stars, 31 reviews
- LinkedIn posts: `harvestapi/linkedin-profile-posts` — already in use for Sumanth's own posts

**Before running any actor:** Always check Apify store first using playwright-cli to verify the actor still has top ratings and hasn't been superseded. Never use an actor based on memory alone.

**The exact pipeline (run when Apify API key is added to .env):**

```
INPUT: Creator name (e.g. "Vaibhav Sisinty")
  ↓
STEP 1 — Find their YouTube channel URL
  Tool: playwright-cli → search YouTube for channel
  Output: Verified channel URL (never guess)
  ↓
STEP 2 — Extract transcripts via Apify
  Actor: karamelo/youtube-full-channel-transcripts-extractor
  Input: Channel URL
  Filter: Top 50 videos by views (notebooklm Standard limit = 50 sources)
  Output: Full transcript text for each video
  ↓
STEP 3 — Scrape their LinkedIn posts via Apify
  Actor: harvestapi/linkedin-profile-posts
  Input: Their LinkedIn profile URL
  Output: Last 50 posts with engagement data (likes, comments, date)
  ↓
STEP 4 — Create notebooklm notebook
  Command: notebooklm create "Creator Research: [Name] — [Date]"
  ↓
STEP 5 — Add sources to notebook
  Option A (preferred): Add YouTube video URLs directly — notebooklm processes transcripts natively
  Option B: Load transcript text as uploaded documents
  Also add: LinkedIn post data as a text document
  ↓
STEP 6 — Research questions to ask notebooklm
  - "What hook patterns appear in the highest-viewed videos?"
  - "What topics generate the most comments on LinkedIn posts?"
  - "What CTA formats does this creator use in posts with 50+ comments?"
  - "What content did they post in their first 90 days vs now?"
  - "What mistakes do they say beginners make that I can build posts around?"
  ↓
STEP 7 — Extract and apply to Reachr
  Output: Updated hook formula, post structure rules, CTA bank
  Save to: posts/creator-research-[name]-[date].md
  Apply in: Next week's post queue via WORKFLOW A
```

**Reality check rule:** Never update content strategy based on notebooklm research alone. Always cross-reference with what's actually working in Sumanth's own engagement data (Apify scrape). Research informs, data confirms.

---

## 9b. Creator Research SOP — Standard Process

When Sumanth says "research [Name]", "do the pipeline for [Name]", or "extract everything from [Name]":

**Step 1 — Read the SOP first:**
`C:\Users\suman\Reachr Linkedin\posts\creator-research-sop.md`
Follow it step by step. Do not skip the data source discovery phase.

**Step 2 — Always ask before using a fallback source:**
- LinkedIn returns 0 posts (auth-gated) → pause and ask Sumanth which fallback: interview proxy / archive search / skip
- YouTube has no valid official channel → pause and ask Sumanth whether to use interview videos
- Never force a bad data source. Bad data produces bad research.

**Step 3 — Do not run the 22 questions until source inventory is confirmed**

**Step 4 — Save output to:**
`C:\Users\suman\Reachr Linkedin\posts\creator-research-[name-slug]-[monthyear].md`

**Creator pipeline status (update this as each creator is completed):**

| Creator | Status | File |
|---------|--------|------|
| Vaibhav Sisinty | ✅ Complete | `creator-research-vaibhav-sisinty-april2026.md` |
| Justin Welsh | ✅ Complete | `creator-research-justin-welsh-april2026.md` |
| Jasmin Alic | ✅ Complete | `creator-research-jasmin-alic-april2026.md` |
| Lara Acosta | ✅ Complete | `creator-research-lara-acosta-april2026.md` |
| Kallaway | ⏳ Pending | — |
| Richard van der Blom | ⏳ Pending | — |
| Nicolas Cole | ⏳ Pending | — |
| Matt Barker | ⏳ Pending | — |

---

## 10. Decisions Made (Decision Log)

| Date | Decision | Reason |
|------|----------|--------|
| Apr 2026 | Reduce posting to 4–5x/week (from daily) | Daily posting with 0 comments trains algorithm to ignore the account |
| Apr 2026 | Prioritize comments over impressions as primary metric | Comments drive algorithmic distribution; impressions are a lagging indicator |
| Apr 2026 | Add 1 personal post per week | Zero personal posts in first 15 = no parasocial trust |
| Apr 2026 | Add 1 LinkedIn-about-LinkedIn post per week | Post 13 data proves meta-relevance outperforms D2C-specific content at this stage |
| Apr 2026 | Start 15–20 connection requests/day to ICP | Highest-ROI action not yet taken; content improvements alone can't break 200-impression ceiling |
| Apr 2026 | No product CTAs until Day 30 | Trust must be established before conversion can happen |

---

## 11. What NOT to Do (Mistakes Already Identified)

- Do NOT score posts by impressions alone — engagement rate matters more
- Do NOT agree when Sumanth says a post performed well without checking the data
- Do NOT reuse the same CTA across multiple posts ("What's one distribution channel your brand actually owns?" has already appeared 3+ times)
- Do NOT write Twitter-poetry style (1–3 word lines on their own) — feels like AI on LinkedIn
- Do NOT start hooks with proper nouns alone ("RAJ SHAMANI", "Seeaash")
- Do NOT post more than 1 idea per post
- Do NOT write posts that only agree with the reader — spiky POV needed to generate comments
- Do NOT publish without running through the humanizer skill first

---

## 12. Open Items / Next Actions

**Do these first (this week):**
- [ ] Post the LinkedIn newsletter post (already written, scored 4.05/5 — just post it)
- [ ] Start sending 15–20 connection requests/day to D2C founders + growth operators
- [ ] Write first personal/founder post (behind-the-scenes of building Reachr)
- [ ] Build beachhead brand list: 100 Indian beauty/skincare D2C brands → `outreach/beachhead-list.csv`
- [ ] Run Apify scraper to get fresh data after posting

**Do next (after first week):**
- [ ] Rewrite top 5 posts (posts 4, 8, 12, 13, 14) using correct hooks, structure, CTAs
- [ ] Set up Apollo.io account (for finding brand founder emails)
- [ ] Set up Instantly.ai account (for sending cold email sequences)
- [ ] Recruit first 20 clippers via Shorts/Reels DMs

---

## 13. Master Skill Workflow Map

This is the master playbook. Every task maps to a workflow. Every workflow has an exact skill order.

**There are 70 skills total: 64 from npx skills + 6 from Superpowers plugin.**

---

### WORKFLOW A: Daily LinkedIn Post (use every posting day)

This is the most important workflow right now. Use it every time you post.

```
INPUT: Topic or content bucket (from weekly schedule in Section 6)
  ↓
STEP 1 — Research the angle
  Skill: anthropic-skills:linkedin-content-methodology
  What it does: Finds the sharpest angle, studies what's trending, identifies who to borrow
  audience from (namejack / brandjack targets)
  Output: A brief with: topic angle, borrowed audience target, 3 hook options
  ↓
STEP 2 — Write the post
  Skill: anthropic-skills:linkedin-post-writer
  Input: Brief from Step 1
  What it does: Writes full post using Jasmin Alić structure, spiky POV, proper CTA
  Output: First draft post
  ↓
STEP 3 — Deep analysis
  Skill: anthropic-skills:linkedin-post-script-analyst
  Input: Draft from Step 2
  What it does: Checks narrative arc, tension, whether the hook earns a click, CTA quality
  Output: Rewrite notes — specific lines to fix
  ↓
STEP 4 — Final score
  Skill: anthropic-skills:linkedin-post-reviewer
  Input: Revised draft after Step 3 feedback
  What it does: Scores 1–5 across: hook, body, CTA, spiky POV, structure
  Target: 4.0+ before publishing. Below 3.5 = rewrite, don't post.
  Output: Score + final verdict
  ↓
STEP 5 — Remove AI patterns
  Skill: anthropic-skills:humanizer
  Input: Approved draft from Step 4
  What it does: Removes em-dash overuse, AI buzzwords, robotic sentence patterns
  Output: Human-sounding final post ready to copy-paste
  ↓
OUTPUT: Final post → copy-paste directly to LinkedIn
```

**Hook writing add-on** (use when you need stronger hooks):
- `hook-writing` — Eugene Schwartz awareness model, psychological triggers
- `hook-tactics` — Pattern interrupts, curiosity gaps
- `hook-voice-patterns` — Matches hook to Sumanth's voice specifically

**Short video add-on** (for carousel posts or when recording a Reel):
- `jackyshen-gen-short-video-script` — Short video script structure
- `ugc-scriptwriter` — Authentic talking-head format

---

### WORKFLOW B: Weekly Planning (do every Sunday night / Monday morning)

```
INPUT: Day of week + what happened last week (engagement data)
  ↓
STEP 1 — Pull last week's data
  Tool: Apify MCP → harvestapi/linkedin-profile-posts actor
  What it does: Scrapes all posts, returns likes, comments, impressions, follows
  Output: Fresh data table to compare against Section 3 baseline
  ↓
STEP 2 — Decide this week's 5 posts
  Skill: anthropic-skills:linkedin-daily-planner
  Input: Current date + engagement data from Step 1 + weekly schedule from Section 6
  What it does: Picks topics, identifies trending hooks, flags which day to use which method
  Output: 5-post plan with topics + angles + which skills to use
  ↓
STEP 3 — Content strategy review (monthly, not weekly)
  Skill: content-strategy
  Input: Reads product-marketing-context.md automatically
  What it does: Reviews if content angles are still sharp or becoming repetitive
  Output: New angles to try, audience segments to target
  ↓
OUTPUT: Weekly post calendar saved to posts/post-queue.md
```

---

### WORKFLOW C: Brand Outreach Pipeline (getting beta customers)

**Goal:** 3 paying beta customers in 45 days. This is the most important growth action.

```
INPUT: Target brand (from beachhead-list.csv)
  ↓
STEP 1 — Research the brand
  Skill: lead-intelligence
  Tool: Clay MCP (mcp__claude_ai_Clay__find-and-enrich-company)
  What it does: Finds who runs the brand, their LinkedIn, company size, ad spend signals
  Output: Contact card with: founder name, LinkedIn URL, email, what they're running on Meta
  ↓
STEP 2 — Research their content problem
  Skill: customer-research
  Input: Brand name + their LinkedIn/Instagram activity
  What it does: Identifies how they're currently doing distribution, what's failing
  Output: 2–3 specific observations about THIS brand's distribution pain
  ↓
STEP 3 — Write cold LinkedIn DM
  Skill: linkedin-automator
  Input: Contact card from Step 1 + pain observations from Step 2
  What it does: Writes a DM that references their specific situation, not a generic pitch
  Template: "Saw [brand] running [X] — noticed [specific observation]. Have a question."
  Output: DM draft (under 300 characters, no pitch, just curiosity trigger)
  ↓
STEP 4 — Write cold email (parallel to Step 3, send both)
  Skill: cold-email
  Input: product-marketing-context.md (auto-loaded) + pain observations from Step 2
  What it does: Writes peer-to-peer email using the "founder to founder" voice
  Subject line rule: Specific observation, not a generic subject
  Output: Email draft with subject line
  ↓
STEP 5 — Write follow-up sequence
  Skill: email-sequence
  Input: Initial email from Step 4
  What it does: Creates 4-email sequence (send Day 1, 3, 7, 14) for non-responders
  Output: Full sequence ready to load into Instantly.ai
  ↓
STEP 6 — Discovery call prep (when they say yes)
  Skill: discovery-caller
  Input: Everything you know about the brand
  What it does: SPIN framework — Situation → Problem → Implication → Need-Payoff
  Creates call script, anticipates objections, prepares the closing question
  Closing question: "If we could put your product in front of 50,000 new people in 30 days for ₹0 upfront — is there a reason you wouldn't try it?"
  Output: Discovery call script + objection handling sheet
  ↓
STEP 7 — Sales tracking
  Skill: revops
  What it does: Tracks pipeline stages (Contacted → Replied → Called → Beta Committed → Live)
  Output: Pipeline tracker (save to outreach/pipeline-tracker.md)
  ↓
OUTPUT: Brand moves from cold → beta committed → live campaign
```

---

### WORKFLOW D: Campaign Execution Pipeline (after beta commitment)

**Trigger:** Brand has agreed to beta and paid/committed to pay per verified view.

```
INPUT: Brand brief (product, target audience, campaign goal)
  ↓
STEP 1 — Generate ad concepts
  Skill: ad-concept-generator
  Skill: ad-creative
  Input: Brand brief + product images/clips provided by brand
  What it does: Creates 3–5 content angles for clippers to test
  Output: Campaign brief document with: concept, hook variants, dos/don'ts
  ↓
STEP 2 — Write UGC scripts
  Skill: ugc-scriptwriter
  Input: Campaign brief from Step 1
  What it does: Writes talking-head scripts for 30–45 sec YouTube Shorts / Instagram Reels
  Format: Hook (3 sec) → Problem (7 sec) → Demo (10 sec) → CTA (5 sec)
  Output: 3 script variants for clippers to choose from
  ↓
STEP 3 — Write hooks for each script
  Skill: hook-writing
  Skill: hook-tactics
  Input: Scripts from Step 2
  What it does: Creates 3 hook variants per script (text overlay + first line)
  Output: Hook bank for clippers to test
  ↓
STEP 4 — Brief document
  Skill: sales-enablement
  What it does: Packages everything into a clear brief for clippers
  Output: Campaign brief PDF/doc with: scripts, hooks, posting instructions, payment terms
  ↓
STEP 5 — Track performance
  Tool: Apify MCP (track clipper accounts) + YouTube Data API
  What it does: Verifies view counts on brand-new accounts (no inflated metrics)
  Output: Weekly view count report sent to brand
  ↓
OUTPUT: 50,000 verified views in 30 days → brand pays ₹500/1,000 views = ₹25,000 per campaign
```

---

### WORKFLOW E: Clipper Recruitment Pipeline (building your supply side)

**Goal:** 20 active clippers by Day 30, 50 by Day 60.

```
INPUT: Platform (YouTube Shorts creators, Instagram Reels creators)
  ↓
STEP 1 — Find clippers
  Skill: lead-intelligence
  Target: Accounts with 0–1K followers posting Reels/Shorts regularly
  Signal: Consistent posting, decent editing, no existing brand deals
  Output: List of 20 potential clipper handles per week
  ↓
STEP 2 — DM outreach
  Skill: social-content (adapted for DM)
  Template: "Saw your [Shorts/Reels] — your editing is solid. I'm building a network of clippers
  who get paid per view. Interested in a trial campaign at ₹500/1K views?"
  Output: DM template + 10 personalized variants
  ↓
STEP 3 — Onboarding call
  Skill: discovery-caller (adapted for clipper onboarding)
  What it explains: How Reachr works, what clippers need to do, payment verification process
  Output: Onboarding call script
  ↓
STEP 4 — Clipper brief
  Skill: ugc-scriptwriter
  What it provides: Scripts + hooks + posting instructions for their first campaign
  Output: Clipper starter kit
  ↓
OUTPUT: Clipper is active → assigned to brand campaign → starts earning
```

---

### WORKFLOW F: Case Study Pipeline (after campaign delivers results)

**Trigger:** A campaign hits 50K+ views. This becomes your best marketing asset.

```
INPUT: Campaign data (view counts, CPV, brand name, product category)
  ↓
STEP 1 — Write the case study
  Skill: case-study-writing
  Note: This skill uses infsh commands for research — works on claude.ai, not local Windows.
  Use on claude.ai with: "Use the case-study-writing skill. Brand: [X]. Views: [Y]. CPV: ₹[Z]."
  Format: STAR framework — Situation → Task → Action → Result
  Output: Full case study document
  ↓
STEP 2 — Turn into LinkedIn post
  Run through full WORKFLOW A using the case study as source material
  Best performing format: The "transformation" post
  Hook structure: "[Brand] spent ₹X on Meta. Got [Y] views. Then they tried Reachr."
  ↓
STEP 3 — Turn into outreach asset
  Skill: sales-enablement
  What it does: Creates a 1-page PDF version for cold email attachments
  Output: Case study PDF for brand outreach
  ↓
STEP 4 — Create a presentation version (for investor pitch / brand onboarding)
  Skill: pptx
  Input: Case study document
  Output: .pptx slide deck with results
  ↓
OUTPUT: Case study becomes: LinkedIn post + cold email attachment + pitch deck slide
```

---

### WORKFLOW G: Reachr Website / Landing Page (when ready to build)

**Trigger:** First beta customer results are in. Need a page to send people to.

```
INPUT: Case study results + product description + target audience
  ↓
STEP 1 — Site architecture
  Skill: site-architecture
  What it does: Plans the page structure (homepage, how-it-works, results, sign-up)
  Output: Page structure with content priorities per section
  ↓
STEP 2 — CRO-optimized copy
  Skill: page-cro
  Skill: copywriting
  Skill: copy-editing
  What it does: Writes conversion-optimized copy for each section
  Key CRO principles: Above-fold hook, proof before pitch, clear CTA
  Output: Full page copy
  ↓
STEP 3 — Design
  Skill: ui-ux-pro-max
  What it does: Generates design specs (50+ styles, 161 palettes, 57 font pairings)
  Recommend: Stark, modern, Indian D2C aesthetic (NOT SaaS blue/white)
  Output: Design direction + component specs
  ↓
STEP 4 — Build
  Skill: vercel-react-best-practices
  Skill: shadcn
  Skill: vercel-composition-patterns
  What they do: React component patterns, shadcn UI components, Vercel optimization
  Output: Deployed website
  ↓
STEP 5 — Deploy
  Skill: deploy-to-vercel
  Skill: vercel-cli-with-tokens
  What they do: Deploys to Vercel, sets up custom domain, handles env vars
  Output: Live site at reachr.in (or similar)
  ↓
STEP 6 — Analytics
  Skill: analytics-tracking
  Tool: PostHog MCP (already connected)
  What it does: Sets up event tracking (brand sign-ups, clipper sign-ups, form submissions)
  Output: Dashboard showing conversion funnel
```

---

### WORKFLOW H: Paid Ads (Month 2+ only, after organic is working)

**Do NOT run ads until organic LinkedIn is generating inbound DMs.**

```
INPUT: Winning LinkedIn post (4.5+ score, 20+ comments, 500+ impressions)
  ↓
STEP 1 — Turn post into ad
  Skill: paid-ads
  Skill: ad-creative
  What it does: Reformats LinkedIn post as Meta/LinkedIn ad, adds tracking
  ↓
STEP 2 — A/B test setup
  Skill: ab-test-setup
  What it does: Creates 2–3 variants, defines the winning metric
  ↓
OUTPUT: Ad campaign ready to launch with clear test hypothesis
```

---

### WORKFLOW I: SEO + Content Distribution (Month 3+)

**Only relevant after the website exists and has case studies.**

Skills for this phase: `ai-seo`, `seo-audit`, `programmatic-seo`, `schema-markup`, `site-architecture`

```
INPUT: Case studies + product pages
  ↓
STEP 1: ai-seo — AI-optimized keyword strategy for "performance marketing India", "UGC distribution"
STEP 2: programmatic-seo — Auto-generate landing pages for "[Brand name] case study" queries
STEP 3: seo-audit — Regular audit for technical issues
STEP 4: schema-markup — Add structured data for rich search results
```

---

### SKILL REFERENCE TABLE (all 70 skills by use case)

| Skill | Use For | Priority |
|-------|---------|----------|
| `anthropic-skills:linkedin-content-methodology` | LinkedIn research + angle finding | Daily |
| `anthropic-skills:linkedin-post-writer` | Writing LinkedIn posts | Daily |
| `anthropic-skills:linkedin-post-script-analyst` | Post analysis after draft | Daily |
| `anthropic-skills:linkedin-post-reviewer` | Final scoring before publish | Daily |
| `anthropic-skills:linkedin-daily-planner` | Weekly post planning | Weekly |
| `anthropic-skills:humanizer` | Remove AI patterns before posting | Daily |
| `hook-writing` | Stronger hooks for any content | Daily |
| `hook-tactics` | Pattern interrupts, curiosity gaps | Daily |
| `hook-voice-patterns` | Match hooks to Sumanth's voice | Daily |
| `ugc-scriptwriter` | Clipper scripts (30–45 sec) | Per campaign |
| `jackyshen-gen-short-video-script` | Short video scripts (Shorts/Reels) | Per campaign |
| `ad-concept-generator` | Campaign content angles | Per campaign |
| `ad-creative` | Full ad creative brief | Per campaign |
| `cold-email` | Brand outreach emails | Daily outreach |
| `email-sequence` | Follow-up sequences | Per prospect |
| `linkedin-automator` | LinkedIn DM outreach sequences | Daily outreach |
| `lead-intelligence` | Find brand contacts + enrich | Per prospect |
| `discovery-caller` | Discovery call scripts | Per call |
| `customer-research` | Understand brand's pain deeply | Per prospect |
| `case-study-writing` | Campaign results → case study | Post-campaign |
| `sales-enablement` | Sales assets, pitch materials | Monthly |
| `sales-leader` | Full B2B sales strategy | Strategic |
| `revops` | Pipeline tracking | Weekly |
| `content-strategy` | Monthly content direction review | Monthly |
| `go-to-market-plan` | GTM strategy for Reachr | Strategic |
| `marketing-ideas` | New angles, campaign ideas | Monthly |
| `copywriting` | Website + landing page copy | Website phase |
| `copy-editing` | Polish any copy | Anytime |
| `social-content` | Social content other than LinkedIn | Month 2+ |
| `marketing-psychology` | Influence principles in messaging | Anytime |
| `lead-magnets` | Free tools / lead magnets for website | Month 3+ |
| `launch-strategy` | Product launch planning | At launch |
| `pricing-strategy` | Refine ₹500/1K views pricing | As needed |
| `competitor-alternatives` | Positioning vs Meta ads / influencers | Strategic |
| `referral-program` | Refer-a-brand / refer-a-clipper | Month 3+ |
| `free-tool-strategy` | Build a free tool for SEO/lead gen | Month 3+ |
| `ui-ux-pro-max` | Website + dashboard design | Website phase |
| `web-design-guidelines` | Design system rules | Website phase |
| `polish` | Final design review | Website phase |
| `frontend-design` | Frontend component patterns | Website phase |
| `vercel-react-best-practices` | React code quality | Build phase |
| `vercel-composition-patterns` | Component architecture | Build phase |
| `vercel-react-view-transitions` | Page transitions | Build phase |
| `vercel-react-native-skills` | Mobile app (future) | Future |
| `shadcn` | UI component library | Build phase |
| `deploy-to-vercel` | Deploy website | Build phase |
| `vercel-cli-with-tokens` | Vercel CLI setup | Build phase |
| `site-architecture` | Page structure planning | Website phase |
| `page-cro` | Conversion rate on website pages | Website phase |
| `form-cro` | Signup form optimization | Website phase |
| `signup-flow-cro` | Onboarding flow CRO | Website phase |
| `onboarding-cro` | User onboarding | Website phase |
| `popup-cro` | Popup/modal optimization | Website phase |
| `paywall-upgrade-cro` | Upgrade conversion (future) | Future |
| `analytics-tracking` | PostHog event setup | Website phase |
| `paid-ads` | Meta/LinkedIn ad campaigns | Month 2+ |
| `ab-test-setup` | A/B testing framework | Month 2+ |
| `ai-seo` | AI-optimized SEO | Month 3+ |
| `seo-audit` | Technical SEO health | Month 3+ |
| `programmatic-seo` | Scale landing pages | Month 3+ |
| `schema-markup` | Rich search results | Month 3+ |
| `aso-audit` | App store optimization (future) | Future |
| `browser-use` | Automate Chrome (LinkedIn research) | As needed |
| `agent-browser` | Lightweight page reading | As needed |
| `linkedin-content` | LinkedIn research (claude.ai only) | On claude.ai |
| `pptx` | Pitch decks, investor materials | As needed |
| `notebooklm` | Deep research on topics | Research |
| `churn-prevention` | Keep brands coming back | Month 2+ |
| `remotion-best-practices` | Programmatic video (future) | Future |

---

## 14. Personal Brand Architecture

**The positioning:** Sumanth is not just a founder posting about his startup.
He is the person D2C founders follow when they want to understand content distribution.

**The identity:** "India's content distribution guy."

Not a creator. Not an influencer. Not a marketer.
A founder who tracks what happens AFTER content is created.

---

### Personal Brand Statement (use this in bio, intro, DMs):

> "Most D2C brands obsess over creating better content. I track why good content dies.
> Building Reachr — performance distribution for Indian brands.
> Follow for weekly data on what actually compounds."

---

### Content Pillars (Sumanth's 5 topics on LinkedIn):

| Pillar | What it is | Example post | Posting day |
|--------|-----------|--------------|-------------|
| 1. Distribution education | Why content doesn't compound, the mechanics | "Snitch spent ₹2Cr on ads in Q4. Their organic reach is zero. Here's why." | Tuesday (authority) |
| 2. Indian brand case studies | Specific Indian D2C brands + what their distribution reveals | "Seeaash went viral with 1 video. Why it won't happen again without this." | Monday (brandjack) |
| 3. Founder journey | Building Reachr in public — the honest, messy, real version | "I pitched 12 brands this week. 11 said no. Here's what I learned from each." | Friday (personal) |
| 4. LinkedIn meta-content | How to grow on LinkedIn specifically — proven by the algorithm post | "The LinkedIn algorithm is not random. I tested 15 post formats. This is what I found." | Wednesday |
| 5. Creator economy India | What's happening in the Indian creator space — clippers, Shorts, Reels | "India now has 600M+ short-form video viewers. Brands are still running TV ad formats." | Saturday (namejack) |

---

### The Personal Brand Rule:
Every post must do one of two things:
1. Make a D2C founder say "I've felt that exact pain"
2. Make a D2C founder say "I didn't know that — and now I need to act"

If it does neither, don't post it.

---

### Cross-Platform Strategy (Month 2+ only):

**LinkedIn first. Only expand after hitting 1,000 followers.**

Once at 1,000 LinkedIn followers:
- **Twitter/X:** Share data threads (numbers, tables, % breakdowns) — repurpose LinkedIn posts
- **Instagram:** Behind-the-scenes of building Reachr — founder life, not product pitches
- **YouTube Shorts:** "Content distribution explained in 60 seconds" — Reachr as the example

**Skill for cross-platform:** `social-content` handles multi-platform calendars once ready.

---

## 15. Process vs API Priority — The Answer

**Process first. Always. APIs layer in AFTER.**

**Why:** APIs amplify an existing process. They don't create one.
If you set up the API before you know the process, you'll configure it wrong and waste the setup time.

---

### What works RIGHT NOW with zero API setup:

| Action | Works without API? | Tool needed |
|--------|-------------------|-------------|
| Write and post LinkedIn content | Yes | Superpowers skills |
| Write cold emails | Yes | cold-email skill |
| Write DM sequences | Yes | linkedin-automator skill |
| Prepare for discovery calls | Yes | discovery-caller skill |
| Write UGC scripts for clippers | Yes | ugc-scriptwriter skill |
| Research brand founders | Partially | Clay MCP (already connected) |
| Track your own post data | Yes | Apify MCP (already connected) |

---

### API Rollout Schedule (when to add each):

| When | API | Why then | Monthly cost |
|------|-----|----------|-------------|
| **Week 1** | Apollo.io | You need emails to start outreach. Can't email without finding emails first. | Free tier: 50/month. Paid: ₹3,500/mo |
| **Week 2** | Instantly.ai | Once you have a list, you need to automate the sequence sending. | ₹2,500/mo |
| **Week 2** | Meta Marketing API | Filters which brands are actually spending on ads (your qualifier). Free. | Free |
| **Week 3** | YouTube Data API v3 | Verifies clipper view counts after first campaign. Free. | Free |
| **Week 3** | Instagram Graph API | Same as above for Reels views. Free. | Free |
| **Month 2** | Hunter.io | Email verification and finding emails Apollo misses. | Free tier: 25/mo. Paid: ₹2,000/mo |
| **Month 3** | Expandi.io OR Phantombuster | If LinkedIn DM volume needs to scale beyond manual. | ₹6,000–₹8,000/mo |

**Total API cost for Month 1:** ₹6,000 (Apollo + Instantly)
**Total API cost for Month 2:** ₹8,000 (above + Hunter)
**Total API cost for Month 3 (with LinkedIn automation):** ₹14,000–₹16,000

---

### The Process Stages (what to do in what order):

**Stage 1 — Days 1–14: Foundation (no APIs needed)**
1. Post 5x/week using WORKFLOW A
2. Send 15–20 manual connection requests/day (LinkedIn, manually)
3. Build beachhead list of 100 brands manually (search Instagram + LinkedIn)
4. Write 10 cold emails + 10 DMs using skills (don't send yet — batch first)
5. Recruit first 10 clippers via manual DMs

**Stage 2 — Days 15–30: First Outreach (Apollo + Instantly)**
1. Use Apollo to find emails for 100 brands → verified contact list
2. Load into Instantly.ai → send cold email sequence (4 emails over 14 days)
3. Send LinkedIn DMs in parallel (manual or linkedin-automator)
4. Handle replies → book discovery calls → use discovery-caller skill
5. First 3 beta calls → target 1 committed brand by Day 30

**Stage 3 — Days 31–60: First Campaign**
1. First brand confirmed → run WORKFLOW D (campaign execution)
2. Clippers create content → post on brand-new accounts
3. Track views with YouTube/Instagram APIs
4. Report to brand weekly → build trust → get results
5. Case study written when campaign ends

**Stage 4 — Days 61–90: Scale + Social Proof**
1. Use case study as new outreach asset → WORKFLOW F
2. Run outreach to 200 more brands now with proof
3. LinkedIn starts getting 10+ comments/post (compounding begins)
4. Target: 2 more beta customers → 3 total by Day 90

## graphify

This project has a graphify knowledge graph at graphify-out/.

Rules:
- Before answering architecture or codebase questions, read graphify-out/GRAPH_REPORT.md for god nodes and community structure
- If graphify-out/wiki/index.md exists, navigate it instead of reading raw files
- After modifying code files in this session, run `graphify update .` to keep the graph current (AST-only, no API cost)

# Session Handoff — Reachr LinkedIn Project
## Context + Prompt to Carry Forward All Sessions

**Use the block below as your opening message in every new Claude Code session.**

---

## THE PROMPT (copy-paste this to start any new session)

---

I'm Sumanth Chowdary Gude, founder of Reachr. We've been working across multiple sessions to build out the full GTM strategy, LinkedIn content system, and automation stack for Reachr. Read CLAUDE.md first — it has everything. Then read `plans/reachr-master-document.md` for the complete strategy. Then read `plans/session-handoff.md` for what's pending.

Here's the compressed context so you're fully caught up:

---

### WHO I AM
- Founder of Reachr, India's version of Whop's Content Rewards
- Analytical/market-observer founder (saw the gap from outside, not personal pain)
- Working style: direct, want honest analysis, not agreement. Push back if I'm wrong.
- LinkedIn: linkedin.com/in/sumanthgude/

---

### WHAT REACHR IS
India's performance distribution marketplace. Brands set a budget + reward rate per 1,000 views. Clippers create new zero-follower accounts, post brand content on YouTube Shorts + Instagram Reels, get paid per verified view.

**The problem it solves:** D2C brand content doesn't compound. Every campaign resets. Brands pay twice — once for UGC, once for paid reach — to reach the same audience.

**Stage:** Pre-revenue, building phase (April 2026).

**ICP Primary:** D2C founders + growth operators doing ₹50L–₹5Cr/month. Sweet spot: beauty/skincare ₹50L–₹2Cr/month.
**ICP Secondary:** Clippers wanting consistent monetization.
**ICP Tertiary:** Monetizing creators wanting to expand reach.

---

### LINKEDIN STATE (as of April 15, 2026)
- Under 500 connections
- Posted 15 posts (March 23 – April 13, 2026), daily
- Max impressions: ~200 (Seeaash brandjack, Mar 28)
- **0 comments across ALL 15 posts** — this is the core problem
- Max likes: 3 (LinkedIn algorithm post, Mar 25)
- Only 1 post scored PUBLISH (4.5/5): the LinkedIn algorithm meta-post (Post 13)

**Root causes:**
1. Network too small, not growing (no daily connection requests being sent)
2. Zero comments = algorithm treats every post as dead
3. Same thesis repeated 15 ways — no evolution
4. Zero personal posts in 15 posts — no parasocial trust
5. Posting daily with 0 engagement trains algorithm to suppress the account

**Decision made:** Drop to 4x/week posting. Prioritize comments over impressions.

---

### THE FULL STRATEGY (built across sessions)

**The most important reframe:**
Old plan: LinkedIn → audience → customers (12–18 month path)
Correct plan: Get customers → results become content → content amplifies sales

**Two-track GTM:**
- Track 1 (Direct Sales) = PRIMARY. Target: 3 paying beta customers by Day 45.
- Track 2 (Content + Authority) = SUPPORTING. Amplifies Track 1.

**The correct GTM sequence (order matters):**
Clippers first (Days 1–5) → Connectors (Days 1–7) → Warm network (Days 1–3) → Beachhead list (Week 1) → Cold outreach (Week 2+) → Discovery calls → Beta offer → Campaign → Case study → Paid

**Why clippers first:** Can't credibly pitch brands without supply ready. "We have 20 clippers ready to run" is the sentence that closes the chicken-and-egg gap.

**The irresistible beta offer:**
- Brand provides: 1 product image or 30-sec clip + brief
- Reachr provides: 10 clippers, new accounts, YouTube Shorts + Instagram Reels
- Brand gets: 50,000+ verified views in 30 days, new audiences only
- Brand pays: ₹0 upfront. ₹500/1,000 verified views — only after delivery + verification
- Guarantee: Miss 50K target → brand pays nothing + second campaign free
- Why it converts: Meta ads = ₹2–5/click. Influencer deals = ₹1–5/effective view. Reachr = ₹0.50/verified view to new audiences.

**Primary beachhead:** Beauty/skincare brands ₹50L–₹2Cr/month.
**Qualifying filter:** Active ads in Meta Ad Library AND UGC-style content on Instagram feed. BOTH must be true.

**Discovery call script (4 questions brands need answered):**
1. What do I pay? → ₹500/1K verified views. First campaign free.
2. When do I pay? → After we deliver + you verify. You see every number first.
3. What do I get? → Videos on new accounts reaching new audiences. Every link + view count sent to you.
4. What's the risk? → You provide assets. We handle everything. Miss 50K → you pay nothing, second campaign free.

**Closing question on every call:**
"If we could put your product in front of 50,000 new people in 30 days for ₹0 upfront — is there a reason you wouldn't try it?"

---

### LINKEDIN CONTENT SYSTEM

**Weekly rhythm (4x/week):**
- Mon: Growth — Brandjack (named Indian D2C brand + distribution angle)
- Wed: Growth — LinkedIn-about-LinkedIn OR trending Indian content
- Thu: Authority — Spiky POV (enemy belief + cost + counter-position)
- Fri/Sat: Personal — Founder story / behind-the-scenes of building Reachr

**Full 6-step post pipeline (every post, no shortcuts):**
1. `anthropic-skills:linkedin-daily-planner` — topic selection, repeat check, trending scan
2. `anthropic-skills:linkedin-content-methodology` — insight mining, borrowed audience, hook variants
3. `anthropic-skills:linkedin-post-writer` — draft (body first, hook mined last)
4. `anthropic-skills:linkedin-post-script-analyst` — 9-dimension structural analysis
5. `anthropic-skills:linkedin-post-reviewer` — 6-dimension scoring with Stage 1 weights
6. `anthropic-skills:humanizer` — MANDATORY before publishing, removes AI patterns

**Hook formula:** FACT + TENSION. Strip the tension — if what's left is still worth reading, the hook isn't sharp enough.

**Metric hierarchy (do not change):**
1. Comments in first 60 mins → THE algorithm trigger
2. Follows gained
3. Profile visits
4. Likes
5. Impressions (lagging indicator — DO NOT optimize for this)

**One post already produced and ready to publish (the LinkedIn newsletter newsjack):**
```
LinkedIn just gave every user a distribution channel 
the algorithm can't touch.

Most people missed it. They're treating it like a content format.

Wrong frame.

Last week, LinkedIn opened newsletters to everyone.

A follower is someone who walked past your stall at the mela.
The mela decides if they walk past again tomorrow.

A subscriber asked you to come to their door.
LinkedIn delivers your next issue to their inbox.
The algorithm doesn't get a vote.

Every post you write, LinkedIn decides who sees it.
Your newsletter? Your subscribers already did.

Build the list now. Nobody's competing for subscribers yet.

Not to publish more content.
To own the only audience on LinkedIn you keep 
when the algorithm changes.

Have you started your LinkedIn newsletter?
Or are you still asking LinkedIn for permission every time you post?

#LinkedInGrowth #ContentDistribution #D2CMarketing
```
Pipeline result: 4.05/5 weighted score. Humanized. Ready to post.

---

### CONTENT DASHBOARD (7 modules, built in Notion first)

Modules:
1. Post Tracker — every post with full performance data + cooldown flags
2. Content Calendar — weekly grid, draft status tracking
3. Outreach Pipeline CRM — most important. Stages: Identified → Messaged → Replied → Call Booked → Beta Committed → Paying
4. Clipper Tracker — onboarded clippers, campaigns, earnings
5. Campaign Tracker — brand campaigns, views generated, case study status
6. Comment & Engagement Log — ROI of commenting time, max 3x per account per 7 days
7. Competitor Monitor — 15–20 target accounts for 30-min comment window

Build order: Option A (Notion, 2 hours, start now) → Option B (Airtable + Zapier, Week 4–8) → Option C (Next.js + Supabase + Vercel, Week 4+ custom build — all three tools already connected)

---

### TOOLS ALREADY CONNECTED
- Apify MCP — LinkedIn scraping, Instagram, YouTube. Actor `harvestapi/linkedin-profile-posts` already live and tested. Last dataset: `SEVMa1U0uEhY9ZTZu`
- Supabase MCP — database for dashboard
- Vercel MCP — hosting Next.js dashboard
- LinkedIn Superpowers skills — full 6-step post pipeline installed

### TOOLS TO ADD (Tier 1 — this week)
- Meta Ad Library API (developers.facebook.com → create app → Marketing API)
- Apollo.io (find D2C founder emails from company name)
- Instantly.ai (cold email sequences at 20/day, auto-stops on reply)
- YouTube Data API v3 (verify clipper views, find Shorts creators)
- Instagram Graph API (verify Reels views, check brand UGC feeds)
- Twitter/X API v2 (monitor 20 D2C founder accounts, post threads)
- WhatsApp Business API (clipper briefing, community presence)

### TOOLS TO ADD (Tier 2 — Week 2–3)
- Expandi or Phantombuster (~$99/mo) — LinkedIn DM automation, 10 DMs/day + 15 connections/day
- Hunter.io — email enrichment
- Typefully or Buffer — post scheduling
- Notion API — auto-update dashboard from Claude
- Brevo — send case study PDFs after discovery calls

### APIFY ACTORS TO ACTIVATE (no new integration needed)
- `apify/instagram-profile-scraper` — find clipper accounts
- `apify/youtube-scraper` — Shorts creators for clipper recruitment
- `apify/instagram-search-scraper` — build brand list from hashtags
- `misceres/meta-ads-library` — scrape Meta Ad Library
- `apify/twitter-scraper` — monitor D2C founder accounts
- `apify/linkedin-company-scraper` — enrich brand data

---

### SKILLS PENDING (Sumanth to provide GitHub links)
- `cold-outreach-dm` — LinkedIn DM sequences that get replies
- `cold-email-sequence` — email sequences with follow-up cadence
- `sales-discovery-call` — 30-min call framework + objection handling
- `case-study-writer` — campaign results → proof assets
- `podcast-pitch` — pitch yourself as guest on Indian D2C podcasts
- `twitter-thread-writer` — thread format + hooks (different from LinkedIn)

Drop skill `.md` files into `C:\Users\suman\Reachr Linkedin\skills\` — they'll be readable in every future session.

---

### FILE STRUCTURE (all project files live here, not in Claude's internal folders)
```
C:\Users\suman\Reachr Linkedin\
├── CLAUDE.md
├── plans/
│   ├── reachr-master-document.md   ← full strategy (17 sections)
│   └── session-handoff.md          ← this file
├── posts/                          ← LinkedIn post drafts + post history log
├── outreach/                       ← DM templates, email sequences, prospect lists
├── skills/                         ← drop GitHub skill files here
├── campaigns/                      ← campaign briefs, clipper assignments, case studies
└── dashboard/                      ← dashboard code, Supabase schemas
```

---

### WHAT'S DONE
- [x] Full LinkedIn audit (15 posts scored, root causes identified)
- [x] Full GTM strategy built (two-track: direct sales + content)
- [x] 10 strategic questions answered in full
- [x] Complete automation stack mapped (Tier 1/2/3 + Apify actors)
- [x] LinkedIn newsletter post produced + humanized (ready to publish)
- [x] 7-module content dashboard designed
- [x] Folder structure set up in project directory
- [x] CLAUDE.md updated with file system rules
- [x] Master document created at `plans/reachr-master-document.md`

### WHAT'S PENDING (next actions in priority order)
- [ ] **TODAY:** Post the LinkedIn newsletter post (humanized, ready)
- [ ] **Days 1–5:** Recruit 20 clippers before touching any brand
- [ ] **Days 1–3:** Map warm network, send 3 intro requests
- [ ] **Week 1:** Build 100-brand beachhead list (Meta Ad Library + UGC filter)
- [ ] **Week 1:** Set up Notion dashboard (all 7 modules, 2 hours)
- [ ] **Week 1:** Connect Tier 1 tools
- [ ] **Week 2:** Set up Expandi LinkedIn outreach sequences
- [ ] **Week 2:** Set up Instantly.ai cold email sequences
- [ ] **Whenever ready:** Share GitHub skill links for cold outreach + email sequences

---

Now pick up where we left off. What are we working on today?

---

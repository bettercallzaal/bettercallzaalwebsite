# BetterCallZaal — Handoff for a New Claude

You are picking up bettercallzaal.com. Read this entire file before touching anything. It captures the state of the project, the way Zaal works, the hard rules, and the goal.

---

## Start here (first 5 minutes)

```bash
# 1. Clone the repo (public)
git clone https://github.com/bettercallzaal/bettercallzaalwebsite.git
cd bettercallzaalwebsite

# 2. Make sure gh CLI is authenticated as Zaal
gh auth status
# If not: gh auth login

# 3. Verify the site builds + serves locally
python3 -m http.server 8765
# Then open http://127.0.0.1:8765 in a browser

# 4. Read CLAUDE.md (project conventions) and this file (HANDOFF.md)
```

If you can do all four, you are good to begin. Do NOT skip steps 2 or 4.

---

## What this project is

bettercallzaal.com — Zaal Panthaki's personal site + Farcaster Mini App. Static HTML hosted on Vercel, deploy-on-merge to `main`.

- **Production URL:** https://bettercallzaal.com
- **GitHub:** https://github.com/bettercallzaal/bettercallzaalwebsite
- **Deploy:** Vercel auto-deploys `main` branch on every merged PR
- **Hosting platform:** Vercel
- **No build step** — pure HTML/CSS/JS. Edit, commit, push, it's live.
- **Repo owner / Zaal's GitHub:** @bettercallzaal (73+ public repos)
- **Zaal's Farcaster:** @bettercallzaal (FID 19640)
- **Zaal's location:** Ellsworth, Maine
- **Zaal's umbrella org:** The ZAO (founded 2023 as a pivot from ZTalent Agency 2022)

## Current state — as of 2026-05-18

PR #4 was just merged after a multi-round content review pass with Zaal. The site is now production-ready, and Zaal is testing the live deploy + having Iman walk through it too.

Recent merged PRs in order:
- **PR #2** — site rebuild: ZABAL Games timeline (June/July/Aug), Tier 1/2 portfolio cards, lermess.pro design patterns (logo strip, parallax text breakers, testimonials carousel, multi-card contact), 6 new sub-pages
- **PR #3** — Tier 1 brand landing pages (`/zao/`, `/wavewarz/`, `/bczyapz/`), value-receipts stats row, fabrication audit + mobile fixes for 424px Farcaster mini-app width
- **PR #4** — content review pass (19 commits): trimmed bio, real WaveWarZ numbers, Maine landscape-design correction, mentor signup form on /zabalgames.html, no-fabrication rewrite of every sub-page

The live test plan Zaal is walking through right now is in `/tmp/bcz-test-plan.md` (on Zaal's laptop). If Zaal hands you specific items from that list, those are your fix list.

## Site structure (10 routes)

```
/                       Index — hero, logo strip, about+timeline, stats, Tier 1+2 portfolio, dropdown, testimonials, 2-card contact
/zao/                   The ZAO umbrella org pitch (orange accent)
/wavewarz/              WaveWarZ prediction market pitch (mint+blue gradient accent)
/bczyapz/               BCZ YapZ podcast pitch (gold accent) + featured guests
/streaming/             Twitch streaming setup + ZAO ecosystem hook (cyan accent)
/Maine/                 Local Maine client work (green accent) — case-insensitive on Vercel
/outdoors/              Eagle Scout + ski patrol (gold accent)
/engineering-past/      RIT + PCC + JAX + Riverside engineering record (cyan accent)
/zaostock/              Pre-public Oct 2026 ZAO festival in Ellsworth, Maine (orange accent)
/zabalgames.html        Farcaster Vibe-Coding Challenge (June prep / July ship / Aug finals)
/nexus.html             Existing canonical link-inventory hub (redirects to nexus.thezao.com per vercel.json)
/poidh.html             POIDH bounty leaderboard
/privacy.html /terms.html /refund.html    Legal — effective May 5-7, 2026
```

Also: `.well-known/farcaster.json` — Mini App domain manifest signed for FID 19640.

## The goal — make bettercallzaal.com BE the nexus

Zaal's direction for the next phase: **bettercallzaal.com should become the canonical hub for every public surface across the ZAO ecosystem + Zaal's personal work.** Currently there's a separate `/nexus.html` that lists every brand surface. The goal is to fold that capability into the main site so visitors don't have to bounce between bettercallzaal.com (Zaal's portfolio) and nexus.thezao.com (the link inventory) — one site, one hub.

What this likely means in practice (open for design discussion with Zaal before building):

- Pull the full nexus link inventory into a section/dropdown on the main page (or a dedicated `/links` or `/all` view)
- Auto-update from a single source of truth (the canonical inventory is at `/Users/zaalpanthaki/Documents/BetterCallZaal/research/2026-05-07-zabal-nexus-link-inventory.md` — but on a new machine you will need to pull this from the repo or generate it fresh)
- Keep the portfolio + bio above the fold so the personal-brand frame stays first
- Filter/search the inventory so it scales as Zaal adds projects
- Possibly: live-load activity (recent casts, latest newsletter, current Twitch stream status) into the hub

Before you build any of this, **brainstorm with Zaal first.** Use the brainstorming pattern below.

## Hard rules (NON-NEGOTIABLE)

These rules came from Zaal directly during the content review loop. Violating them will get you corrected and may damage the project.

### 1. NEVER fabricate facts, dates, quotes, numbers, processes, or specific details

Zaal will catch invented content immediately. When you don't know something:
- Use `/zao-research` to pull from the canonical research library
- Search the local research/ folder
- Ask Zaal directly via AskUserQuestion
- Use intentionally vague placeholders like `[YEAR TBD]`, `[QUOTE PENDING]`

**Examples of fabrication Zaal called out:**
- Made up Eagle Scout merit-badge list
- Invented specific patrol-room stories
- Wrote "stitched together the on-chain settlement contract, the dashboard, the Empire wrap, the leaderboard, the artist onboarding flow" for WaveWarZ when only some pieces were verified
- Invented "every Monday at 9:30am ET" fractal meeting timing
- Wrote "ZOL token SOL-bound illiquid earned-only" without sourcing the token mechanic correctly

**Always pull from real sources:**
- `research/05-founder-story-section/README.md` — Zaal's verified bio facts
- `research/2026-05-07-zabal-nexus-link-inventory.md` — every public surface across the ecosystem
- `research/02-bettercallzaal-github/README.md` — repo inventory (was 65, now 73+)
- ZAO OS research docs at `/Users/zaalpanthaki/Documents/ZAO OS V1/research/` (1000+ docs)
- Zaal's bcz-yapz transcripts at `/Users/zaalpanthaki/Documents/bcz-yapz/content/transcripts/`
- The github API: `gh api repos/bettercallzaal/REPONAME`

### 2. NEVER use emojis

No emojis in chat responses, code, comments, commit messages, PR titles, PR descriptions, research docs, or any markdown. Also no decorative Unicode (checkmarks, warning triangles, play buttons). Use text labels: `[MUSIC]`, `OVERDUE`, `DONE`, `IN PROGRESS`. Plain hyphens or numbered lists for bullets.

### 3. NEVER use em dashes

Use hyphens (`-`) instead.

### 4. Brand spellings — these are exact, never autocorrect

| Correct | Wrong |
|---------|-------|
| WaveWarZ | Wave Wars, Wavewarz, WaveWars |
| COC Concertz | COC Concerts, CocConcertz |
| The ZAO | the Zao, ZAO standalone |
| BetterCallZaal | Bettercallzaal, Better Call Zaal |
| Joseph Goats | Jose Goats, Jose |
| Huöttöja | Waha, Huottoja |
| SongJam | Songjam, Song Jam |
| ZABAL | Zabal, zabal |
| SANG | Sang, sang |
| ZOE | Zoe, zoe |
| ZOLs | Zols, ZOL |
| FISHBOWLZ | Fishbowlz, FishBowlz |
| Stilo World | StiloWorld, stilo world |
| Tom Fellenz | Fellenz |
| Thy Revolution | The Revolution, Th Revolution |
| ArDrive | Ardrive, ar drive |

### 5. Match the existing dark aesthetic

- Background: `#0a0a1a`
- Accents: orange `#ff6b35`, cyan `#4ec3e0`, gold `#ffb347`
- Fonts: Syne (800 for headings, 700 for sub-headings), Outfit (300-600 for body), JetBrains Mono for eyebrow/source-attribution
- Sub-pages have their own accent tint (per-brand): zao=orange, wavewarz=mint+blue gradient, bczyapz=gold, streaming=cyan, maine=green, outdoors=gold, engineering-past=cyan, zaostock=orange
- Mobile-first — test at 424px (Farcaster mini app width)
- Use `gstack browse` skill to take real screenshots before claiming mobile works

### 6. Anti-vanity, pro-receipts on stats

Zaal explicitly does not want vanity metrics (follower counts, etc). Every number on the site links to a verifiable public source. The stats row tiles each have a source attribution under them (e.g. "wavewarz-intelligence.vercel.app · 950 battles"). Maintain this pattern.

## How to work with Zaal (the loop)

Zaal works iteratively and fast. The pattern that worked:

1. **One section at a time.** Don't dump 20 changes on him at once. Show one section's current state, ask 1-3 focused questions via `AskUserQuestion`, apply the changes, commit, push, ask the next section.
2. **AskUserQuestion has a max of 4 options per question and max 4 questions per call.** Stay inside those limits or the tool errors.
3. **Commit often, push often.** Every meaningful change gets its own commit. PRs grow organically as he reviews.
4. **When he says "go fix then ask more" — fix something concrete, then ask the next round.**
5. **When he says "research" — actually pull from sources, don't reason from priors.**
6. **When he says "/zao-research" — invoke that skill.** It searches the local research library + has cross-repo search across bettercallzaal org repos.
7. **Use `gstack browse` for live screenshots.** The `browse` skill is at `~/.claude/skills/gstack/browse/dist/browse`. Spin up a local Python server on port 8765 first, then snap viewports at 424px for mobile checks.

### AskUserQuestion pattern that works for Zaal

- Lead with WHAT he is looking at (paste the current state inline so he doesn't have to load the live site)
- 1-3 questions max per call
- Multi-select where the answer is naturally multi-axis (e.g. "what's wrong with this section?")
- Single-select where there's truly one path
- Always include an "all good - move on" option so he can advance without forcing input

## Open TODOs

These were surfaced during the review loop and have not yet been done:

### From the site review

- [ ] **Photos in /assets/outdoors/** — Zaal will drop Eagle Scout + ski patrol photos. The `/outdoors/` page has placeholder boxes wired up; just add files.
- [ ] **More testimonials** — Send the outreach DMs Zaal copied from `/tmp/bcz-outreach-dms.md`. Currently only 2 testimonials live; the dropdown reads "Read what people say (2)". Increment the count when new ones come in via the existing Formspree-backed form (`mqeywpvw`).
- [ ] **Zlank cap on Tier 2** — Tier 2 is now 4 cards (Streaming, Maine, Engineering, Zlank). On desktop this might wrap weirdly. Test at 1280px+ and adjust if needed.
- [ ] **Stats row at 5 tiles** — `.stats-row` uses `repeat(3, 1fr)` default. 5 tiles wraps to 3+2 on desktop. Confirm this looks intentional, not broken.

### From the ZABAL Games doc 654 (in zaoos repo)

The PR for that doc had a Next Actions table. These are still open:
- [ ] Get Empire Builder API key from Jordan (yerbearzerker)
- [ ] Build Empire Builder API leaderboard for Songjam migration (before June 1)
- [ ] Add second POIDH bounty contract to existing leaderboard
- [ ] Record kmac.eth + Zaal session on zlank templates for June bootcamp
- [ ] Re-ping Jubjub once June calendar is public
- [ ] Schedule Empire Builder bootcamp session with Jordan + Iman (before June 7)
- [ ] Draft 2-week pre-launch marketing cadence for July submissions (mid-June)
- [ ] Update `zabalgames-brand-context.md` with master prompt + Empire-as-build-home flow

### From the live test plan

After Zaal walks through `/tmp/bcz-test-plan.md`, anything he marks FAIL becomes a fix list. Open a new PR per batch of fixes.

### The big one: build the nexus

See "The goal" section above. Brainstorm with Zaal before committing to an approach.

## Where the canonical research lives

On Zaal's primary laptop, key paths:

```
/Users/zaalpanthaki/Documents/BetterCallZaal/                Main repo (this one)
/Users/zaalpanthaki/Documents/BetterCallZaal/research/        Local BCZ research (5 docs + nexus inventory)
/Users/zaalpanthaki/Documents/ZAO OS V1/research/             ZAO ecosystem research (1000+ docs)
/Users/zaalpanthaki/Documents/bcz-yapz/content/transcripts/   BCZ YapZ podcast transcripts (20 episodes)
/Users/zaalpanthaki/Documents/zaostock/                       ZAOstock festival repo
/Users/zaalpanthaki/Documents/zlank/                          Zlank Farcaster Snap builder repo
/Users/zaalpanthaki/.claude/projects/-Users-zaalpanthaki-Documents-BetterCallZaal/memory/  Claude auto-memory for this project
```

**If you are on a fresh machine, these paths will not exist.** You can either:
1. Get Zaal to sync them (rsync, Dropbox, iCloud, etc) — slow but complete
2. Pull what you need from github.com/bettercallzaal/* — most of it is public
3. Re-research from public sources as you go — use `/zao-research`, `gh api`, web search

## Forms + integrations to know

- **Contact form** — Formspree `mjgajyqe` (zaalp99@gmail.com personal + info@thezao.com ZAO)
- **Testimonial form** — Formspree `mqeywpvw`
- **Mentor/speaker signup** (on /zabalgames.html) — Formspree `mjgajyqe` (same as contact, with hidden `form_source=zabal-games-mentor-signup` discriminator)
- **ZABAL Games application form** — Supabase-backed (separate from Formspree), currently in placeholder state per script

## Common commands

```bash
# Smoke test all routes return 200
python3 -m http.server 8765 &
for p in / zao/ wavewarz/ bczyapz/ streaming/ Maine/ outdoors/ engineering-past/ zaostock/ zabalgames.html; do
  curl -s -o /dev/null -w "%-22s %{http_code}\n" "http://127.0.0.1:8765/$p"
done
pkill -f "python3 -m http.server 8765"

# Take 424px screenshots for mobile audit
B=~/.claude/skills/gstack/browse/dist/browse
$B viewport 424x900
$B goto http://127.0.0.1:8765/
$B screenshot --viewport /tmp/bcz-mobile.png

# Live WaveWarZ stats (for stats row updates)
curl -sL -A "Mozilla/5.0" https://wavewarz-intelligence.vercel.app/ -o /tmp/wwz.html
grep -oE '[0-9]+\.[0-9]+ SOL|[0-9]{3,4} battles' /tmp/wwz.html | head

# Live github repo count
curl -s https://api.github.com/users/bettercallzaal | grep -oE '"public_repos":[0-9]+'

# Make a fix PR
git checkout -b fix/whatever-from-zaal origin/main
# edit files
git add . && git commit -m "fix(scope): description"
git push -u origin fix/whatever-from-zaal
gh pr create --base main --head fix/whatever-from-zaal --title "..." --body "..."
gh pr merge --squash
```

## What to do FIRST when you take over

1. Run the smoke test above. Confirm all 10 routes return 200.
2. Open https://bettercallzaal.com in a browser and read everything. Get the tone in your head.
3. Re-read the `CLAUDE.md` file in this repo. It's short and project-specific.
4. Ask Zaal: "What did you find broken in the live test? What should I touch first?" — Use AskUserQuestion with the test plan sections as options.
5. Do NOT start building the nexus until Zaal says it's time. Fix his test-plan FAIL items first.

## Things that have already gone wrong — don't repeat

| Mistake | What happened |
|---------|---------------|
| Hallucinated specific facts | Made up Eagle Scout merit-badge list, invented patrol stories, fabricated WaveWarZ contract components. Zaal called it out hard. See "Hard Rule 1." |
| Wrote bio details without source | Said "Building Automation Technician at JAX by day" — Zaal is moving to Riverside soon, wanted tense-neutral framing. Always confirm employment status. |
| Used 1000+ in two places, then 250+ in one without matching the other | Stats row + Tier 1 card both showed "1,000+ artists" — Zaal changed Tier 1 to 250+ but stats stayed 1,000+. Always sync numbers across surfaces. |
| Inline CSS overrode media query | Contact 2-card section had `style="grid-template-columns: 1fr 1fr"` inline, which beat the `@media (max-width: 880px) { grid-template-columns: 1fr }` rule. Don't use inline style for grids that need responsive behavior. |
| Committed embedded git repos | `Maine/Cameron/riverside-site/` was a submodule that snuck into git. Always check `git status -s` before committing batched changes; use `.gitignore` for embedded working dirs. |
| Used `warpcast.com` for compose URL | Warpcast was sold to Neynar. Canonical Farcaster client is now at `farcaster.xyz`. Compose pattern: `https://farcaster.xyz/~/compose?text=...&embeds[]=...` |

## End of handoff

Pick this up at the test-plan FAIL list. When that's clear, brainstorm the nexus direction with Zaal. Don't invent. Don't use emojis. Don't use em dashes. Match the dark aesthetic. Ship in small PRs.

Good luck.

— Previous Claude, 2026-05-18

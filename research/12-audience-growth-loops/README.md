# 11 — Audience Growth Loops

> **Status:** Research complete
> **Date:** 2026-08-15
> **Goal:** How Zaal grows the audiences that feed everything else - Farcaster reach, GitHub-profile conversion, and the loops connecting site, casts, repos, and newsletter.

---

## Key Takeaways

- **Farcaster in 2026 rewards depth over volume.** The platform matured into a reputation economy: channel selection first, then owning 2-3 recurring topics until people associate you with them. **Replies outperform standalone casts** - a sharp answer under someone else's attention attaches your expertise to their audience.
- **The 70/20/10 mix protects credibility:** 70% original insight + replies, 20% curated resources, 10% direct promotion. Zaal's build-in-public stream is naturally 70-lane content; the risk is drift toward 100% self-promo casts about his own launches.
- **The GitHub profile is a landing page, and Zaal's is unoptimized.** In 2026 the profile README is the de-facto developer front door. Zaal has ~96 public repos, no profile README, no pinned repos, and (per the audit) dozens of undescribed repos - visitors from the site or casts land on a wall of cryptic names. 3-5 pinned repos with one-line descriptions + a short story-shaped README is the fix; avoid badge walls.
- **The loop is the strategy:** site -> research/docs -> casts about them -> replies in the right channels -> profile/repo landing -> newsletter/site. Each node exists already; what's missing is the connective tissue (pinned repos, profile README, consistent CTAs from repo READMEs back to bettercallzaal.com).

---

## 1. Farcaster playbook (tailored)

- **Channels:** pick the 2-3 where the ZAO's buyers and collaborators live (music/web3-music, Base builders, AI-agents) and hold position there. Lead-gen research: define who the high-value contact is (festival sponsors, artist partners, collab devs) before optimizing anything.
- **Own topics:** (a) AI agents running a real creator ecosystem, (b) artist ownership economics with receipts, (c) build-in-public shipping cadence. Every cast fits one.
- **Reply-first hours:** consistent thoughtful replies to respected accounts in those channels beat posting into the void; the research is unambiguous on replies-over-broadcast for reputation building.
- **Embeds:** combine embeds creatively (mini app frame + image) - casts carrying the site's mini app embed are one-tap opens.
- **The mini app share-loop (docs 08/09)** is the compounding piece once Insert Coin ships: every pull-share is a cast Zaal did not have to write.

## 2. GitHub profile conversion (highest-leverage single fix)

Concrete to-do list, ~1 hour total, needs a local terminal (out of this session's write scope):
1. Create `bettercallzaal/bettercallzaal` profile README: 3 short paragraphs - who (FOSS builder, Maine, The ZAO), what is live now (ZAOOS, WaveWarZ, farscout, zlank), how to work with him (bettercallzaal.com + Build Session link). No badge walls (2026 consensus: badge dumps say nothing).
2. Pin 6: ZAOOS, farscout, zlank, wwtracker, sparkz, bettercallzaalwebsite.
3. One-line descriptions on the ~30 public repos that matter (audit finding B); the contribution graph then does the credibility work by itself - it is the one unfakeable signal.
4. Every flagship repo README gets a one-line footer: built by BetterCallZaal - bettercallzaal.com. Repos rank in Google/AI answers; each is a doorway.

## 3. The connected loop (what to wire)

```
cast (insight) -> reply traffic -> profile README -> pinned repo -> repo footer -> site
site research docs -> cast threads (each doc = 3-5 casts) -> newsletter edition -> back to site
Insert Coin pull -> share-cast -> mini app open -> save + notifications -> next drop
```
- Each research doc in this library is cast-thread fuel - the 20% curated lane.
- Newsletter (400+ editions) is the retention asset; site currently links it but never captures - consider a subscribe line in the site footer.
- Measure with three numbers monthly: Farcaster follower delta, GitHub profile views (profile README makes these meaningful), site referrals from github.com.

## Sources

- Influencers Time - Niche Farcaster channels 2026 playbook: https://www.influencers-time.com/niche-farcaster-channels-a-2026-playbook-for-high-value-leads/
- Percs - 7 tactics for better Farcaster engagement: https://percs.app/blog/7-tactics-farcaster/
- Dspyt - Farcaster 2026 state: https://dspyt.com/farcaster-2026
- Codeboards - GitHub profile README complete guide 2026: https://codeboards.io/blog/github-profile-readme-guide
- Quillly - GitHub profile README examples 2026, what works: https://devbio.me/blogs/github-profile-readme-examples-2026
- Markdown Studios - Standout GitHub profile README 2026: https://www.markdownstudios.com/blog/github-profile-readme-guide
- GitHub community - Prepping your profile for 2026: https://github.com/orgs/community/discussions/186153

# Research 06 — ZABAL Gamez & the FOSS Builder Evidence Base

**Date:** 2026-06-04
**Source of truth:** [zabalgames.com](https://zabalgames.com) · repo [`github.com/ZAODEVZ/zabalgames`](https://github.com/ZAODEVZ/zabalgames) (MIT)
**Why this doc exists:** Supports the site-wide reframe of Zaal's title from "Engineer" to **FOSS Builder** (free & open source software builder). ZABAL Gamez and its `/projects` subpage are the strongest single piece of evidence for that identity — a public catalog of dozens of open-source, MIT, forkable repos Zaal has shipped.

---

## What ZABAL Gamez Is

The ZAO's **3-month Build-A-Thon** (June–August 2026) — a build event for the Farcaster/ZAO ecosystem, **not a video-game contest**. Tagline: *"Free, open to anyone, any harness."* MIT licensed.

- **June:** ecosystem workshops / recordings
- **July:** open build month — anyone ships a project
- **August:** finals — mentor pairing, governance voting, live reveals

Three participation tracks: **artist**, **builder**, **creator**. Brand voice: "tight, factual, warm"; avoids crypto jargon ("digital creators" / "builders" over web3 terms); arcade aesthetic ("INSERT COIN").

Zaal's role on the about page: *"The organizer — runs ZABAL Gamez, BetterCallZaal, the /zabal channel."* Bio: *"Builder, music infra, ZAO operations."* (@bettercallzaal, FID 19640.)

---

## The `/projects` Subpage — the FOSS catalog

The projects page (`projects.html`) loads from `/data/adoptable-projects.json` and is the "more info" hub. Its adoption framework is explicitly open-source:

- **EXTEND** — build features on a shipped, live product
- **FORK** — take over a starter repo / template, make it yours
- **BUILD** — create a concept from scratch on existing ecosystem rails

Key framing line: **"You keep the repo and the credit; it stays open-source MIT."** Composability over reinvention — shared infra: Empire Builder, Farcaster mini apps, Hats, Bonfire, EAS, Hypersub, Coinflow. Claim a project by DMing **@bettercallzaal** on Farcaster.

### Catalog at a glance (46 projects)

| Stage | Count | Examples |
|-------|-------|----------|
| Shipped | 23 | ZAOOS, ZAONEXUS, ZAO-Leaderboard, zpoidh, zlank, fishbowlz, CoCConcertZ, bcz-yapz, zaostock |
| Working | 7 | farscout, ZAOcowork, hermes-orchestrator, WARZAI, Aurdour, Zuke, zaoprojects |
| Early-stage | 4 | ZAO 101, ZOUNZ, ZAOFlights, zlank-snap-template |
| Concept | 12 | ZOE skill, WaveWarZ-Base settlement, Songjam migration, POIDH leaderboard, knowledge-game scorer |

Most repos live under the [`bettercallzaal`](https://github.com/bettercallzaal) and [`ZAODEVZ`](https://github.com/ZAODEVZ) GitHub orgs. Stack is a consistent modern web/onchain set: **Next.js, Vercel, React, Farcaster SDK, Solana/Base/Optimism, Claude API**.

> Note: the live JSON does not stamp each row with an explicit license string, but the projects-page contract ("it stays open-source MIT") and the repo's own MIT LICENSE are the governing terms.

---

## Why this backs the "FOSS Builder" reframe

1. **Volume of public, forkable work** — 46 catalogued projects on top of the 73+ repos already linked from the homepage stat (`github.com/bettercallzaal`). "FOSS builder" is descriptive, not aspirational.
2. **Explicit open-source contract** — "keep the repo and the credit; stays open-source MIT" is the cleanest one-line justification for the title.
3. **Build-in-public posture** — ZABAL Gamez is the ecosystem-facing proof that the work is open by default, designed to be extended/forked by others.

### Suggested site usage

- Homepage `73+ open-source repos shipped` stat → already on-brand; consider linking it to the ZABAL Gamez `/projects` catalog as the human-readable index.
- Anywhere the title appears, the canonical form is now **`FOSS Builder · Connector · Ecosystem Architect`** (acronym defined once in the About paragraph).

---

## Open follow-ups

- `zabalgames.com` is behind Cloudflare (403 to automated fetch); research above pulled from the public `raw.githubusercontent.com/ZAODEVZ/zabalgames` mirror. Re-verify against the live site when possible.
- Consider a dedicated `/projects`-style index on bettercallzaal.com that mirrors the ZABAL Gamez catalog so the FOSS body of work is browsable from the personal site too. **(Done 2026-06-04 — built at [`/projects/`](https://bettercallzaal.com/projects/), all 46 projects, linked from the homepage Portfolio section.)**
- Auto-sync: `scripts/sync-projects.js` pulls the upstream `adoptable-projects.json` (GitHub raw — zabalgames.com is Cloudflare-blocked) and regenerates `projects/projects.json`; `scripts/project-overrides.json` (keyed by upstream `id`) layers in tech stacks + clean names. **(Done 2026-06-04.)** Run it on a schedule (cron / GH Action) to keep the catalog current.

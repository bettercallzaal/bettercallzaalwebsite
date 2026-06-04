# CLAUDE.md — BetterCallZaal

## What This Is

Personal site and Farcaster Mini App for Zaal (FID: 19640) — FOSS (free & open source software) builder, connector, and ecosystem architect in the web3/Farcaster/music ecosystem. Pure static HTML hosted at `bettercallzaal.com`.

## Project Structure

```
index.html                        # The entire site — HTML + embedded CSS + JS
assets/                           # Images (icon.png = Z logo)
.well-known/farcaster.json        # Farcaster Mini App domain manifest
projects/                         # FOSS catalog — index.html renders from projects.json
scripts/sync-projects.js          # Regenerates projects/projects.json from ZABAL Gamez
research/                         # Research docs (see research/README.md)
.agents/skills/bcz-research/      # /bcz-research skill definition
```

## Key Facts

- **No build step** — edit `index.html`, push to main, it deploys
- **Domain:** `bettercallzaal.com`
- **Farcaster:** Mini App enabled, account association signed for FID 19640
- **Forms:** Formspree — contact (`mjgajyqe`) + testimonials (`mqeywpvw`)
- **Design:** Dark bg `#0a0a1a`, orange + cyan + gold accents, Syne + Outfit fonts

## Design Conventions

- Mobile-first — test at 424px wide (Farcaster mini app viewport)
- Colors via CSS variables: `--orange`, `--cyan`, `--gold`, `--bg`, `--text`, `--text-muted`, `--text-dim`
- Headings: Syne 800. Body: Outfit 300-600
- Sections use `.fade-in` class for scroll-triggered animation (IntersectionObserver)
- All changes deploy via `git push` to main — no CI needed

## Farcaster Mini App

- SDK loaded via CDN: `https://esm.sh/@farcaster/miniapp-sdk`
- `sdk.actions.ready()` MUST be called — dismisses splash screen
- Inside mini app: use `sdk.actions.composeCast()` for sharing
- Outside mini app: Warpcast compose URL fallback

## Projects Catalog (`/projects`)

The `/projects` page renders client-side from `projects/projects.json` (single source of truth — edit it to change the catalog, no rebuild). To resync from the canonical ZABAL Gamez list:

```
node scripts/sync-projects.js          # rewrites projects/projects.json
node scripts/sync-projects.js --check   # dry run; exits non-zero if stale
```

The sync pulls the GitHub raw URL (zabalgames.com itself is Cloudflare-blocked). `scripts/project-overrides.json` (keyed by stable upstream `id`) adds the tech `stack` chips and cleaner display names that upstream doesn't carry — edit it when new projects appear. Needs Node 18+ (global fetch).

## Research Library

3 research docs in `research/`. See `research/README.md` for the index.

Use the `/bcz-research` skill for researching new topics or adding to the library.

Cross-reference: ZAO OS has 88 research docs at `github.com/bettercallzaal/zaoos` — check there first for Farcaster, web3, music, and AI agent topics.

## Style Preferences

- Mobile-first design, desktop as enhancement
- Keep the site fast — no frameworks, no unnecessary dependencies
- When adding content, match the existing dark aesthetic and tone

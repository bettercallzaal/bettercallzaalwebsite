# CLAUDE.md — BetterCallZaal

## What This Is

Personal site and Farcaster Mini App for Zaal (FID: 19640) — engineer, builder, and connector in the web3/Farcaster/music ecosystem. Pure static HTML hosted at `bettercallzaal.com`.

## Project Structure

```
index.html                        # The entire site — HTML + embedded CSS + JS
assets/                           # Images (icon.png = Z logo)
.well-known/farcaster.json        # Farcaster Mini App domain manifest
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

## Research Library

3 research docs in `research/`. See `research/README.md` for the index.

Use the `/bcz-research` skill for researching new topics or adding to the library.

Cross-reference: ZAO OS has 88 research docs at `github.com/bettercallzaal/zaoos` — check there first for Farcaster, web3, music, and AI agent topics.

## Style Preferences

- Mobile-first design, desktop as enhancement
- Keep the site fast — no frameworks, no unnecessary dependencies
- When adding content, match the existing dark aesthetic and tone

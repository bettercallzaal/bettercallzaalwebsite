# BetterCallZaal Project Context

## What BetterCallZaal Is

The personal site and brand hub for Zaal (FID: 19640) — an engineer, builder, and connector in the web3/Farcaster/music ecosystem. The site showcases Zaal's work, collects testimonials, drives inbound via a contact form, and is a Farcaster Mini App so it's natively shareable and launchable inside Warpcast.

## Who Zaal Is

- Engineer turned web3 builder, based in Maine
- Builder of The ZAO — a creator infrastructure ecosystem (zaoos.com)
- Helped WaveWarZ scale to $60k+ volume, 1.2k X followers
- Active Farcaster user: @bettercallzaal (FID 19640)
- 65+ public GitHub repos across Farcaster, ElizaOS, music tech, web3, governance
- Creates spaces for community coordination (weekly calls, ZAO Spaces)
- 1 new repo every ~6 days average

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Site | Pure static HTML + embedded CSS + vanilla JS |
| Hosting | GitHub Pages via `bettercallzaal.github.io/bettercallzaalwebsite` → `bettercallzaal.com` |
| Forms | Formspree (contact + testimonials) |
| Fonts | Google Fonts — Syne (headings) + Outfit (body) |
| Mini App | `@farcaster/miniapp-sdk` via CDN (esm.sh) |
| Images | `/assets/` folder in repo |
| Deploy | Git push to main → auto-deploys |

## Farcaster Mini App Details

- Domain: `bettercallzaal.com`
- Manifest: `/.well-known/farcaster.json` ✅
- Account association: signed for FID 19640 ✅
- SDK: `@farcaster/miniapp-sdk` initialized, `sdk.actions.ready()` called ✅
- Embed meta tag: `fc:miniapp` ✅
- App icon/splash: `/assets/icon.png` (navy Z logo)

## Key Sections

1. **Hero** — "Got a problem? BetterCallZaal." with CTA, social links
2. **About** — Two paths: Join the ZAO / Connector Treatment
3. **Ecosystem** — 5 project cards linking to ZAO, ZAO OS, WaveWarZ, etc.
4. **Testimonials** — Live testimonials + submission form
5. **Contact** — Form + Calendly booking link
6. **Share Bar** — Farcaster, X, LinkedIn share buttons
7. **Footer** — Socials + email

## Social / Contact

- X: @bettercallzaal
- Instagram: @bettercallzaal
- LinkedIn: linkedin.com/in/zaalp/
- GitHub: github.com/bettercallzaal
- Email: zaalp99@gmail.com
- Calendly: calendly.com/zaalp99/30minmeeting

## Goals for the Site

- Drive inbound leads for the "Connector Treatment"
- Grow Farcaster presence — launchable mini app, shareable in casts
- Showcase ZAO ecosystem projects
- Collect and display social proof (testimonials)
- Be a hub that links out to all Zaal's projects and platforms

## Important Rules

- Site is static HTML — no build step, no frameworks, no npm
- Keep it fast and mobile-first
- All changes deploy via `git push` to main
- Design aesthetic: dark navy/black bg, orange + cyan + gold accents, Syne + Outfit fonts

# BetterCallZaal.com

Personal site and Farcaster Mini App for Zaal Panthaki (@BetterCallZaal) - FOSS builder,
connector, and ecosystem architect. Pure static HTML, no build step, deployed on Vercel.

## What is this?

The public front door for BetterCallZaal: who Zaal is, the body of open-source work behind
the FOSS-builder title, and the way in for people who want to hire, collaborate, or adopt a
project. The ZAO ecosystem is the proof of network; the Build Session is the revenue front door.

## Pages

| Path | What it is |
|---|---|
| `/` | Homepage - story, portfolio, ecosystem, testimonials, contact |
| `/history/` | Long-form story + timeline |
| `/resume/` | Full CV, plus an exportable FOSS share card |
| `/projects/` | Open-source catalog, rendered from `projects/projects.json` |
| `/photos/` | ZABAL Insert Coin daily drop |
| `/zao/` `/wavewarz/` `/zaostock/` `/bczyapz/` `/streaming/` | Per-brand pages |
| `/maine/` `/outdoors/` `/engineering-past/` | Context and background |
| `/zaostock/sponsors/` | ZAOstock sponsor kit |
| `/kit.html` | Brand kit (machine-readable at `/brands.json`) |
| `/privacy.html` `/terms.html` `/refund.html` | Legal |

Redirects live in `vercel.json`: `/nexus*` goes to nexus.thezao.com, `/poidh*` to the zpoidh repo.

## Tech

- No framework, no build step. Edit HTML, push to `main`, Vercel deploys.
- Each page carries its own inline `<style>`. There is no shared stylesheet yet.
- Google Fonts: Syne (display) + Outfit (body)
- Dark theme, orange / cyan / gold accents on `#0a0a1a`
- Mobile-first; test at 424px (the Farcaster mini app viewport)
- Farcaster Mini App via `@farcaster/miniapp-sdk`; manifest at `.well-known/farcaster.json`

## Projects catalog

`/projects` renders client-side from `projects/projects.json`. **That file is generated - do
not hand-edit it.** The source of truth is `data/adoptable-projects.json` in
`ZAODEVZ/zabalgames`; fix wrong entries there.

```
node scripts/sync-projects.js           # regenerate projects/projects.json
node scripts/sync-projects.js --check   # dry run; non-zero exit if stale
```

`scripts/project-overrides.json` (keyed by stable upstream `id`) adds tech `stack` chips and
cleaner display names. It can override `name` and `stack` only - `repo` always comes from
upstream. Needs Node 18+.

## Forms and booking

- Contact form -> Formspree `mjgajyqe`
- Testimonial form -> Formspree `mqeywpvw`
- Book a Build Session -> `cal.com/bettercallzaal`

## Research

Research docs live in `research/`. See `research/README.md` for the index. The `/bcz-research`
skill (`.agents/skills/`) covers adding to it. Cross-reference ZAO OS at
`github.com/bettercallzaal/zaoos` first for Farcaster, web3, music, and AI-agent topics.

## Deploy

Push to `main`. Vercel builds from this repo. No CI.

## License

MIT

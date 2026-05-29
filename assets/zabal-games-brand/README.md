# ZABAL Games Brand Kit

Pre-cleared assets for the ZABAL Games campaign. Use freely under CC-BY 4.0 - just keep "ZABAL Games" + the `zabalgames.com` link visible somewhere in your final piece.

Maintainer: Zaal / BetterCallZaal. Last updated: 2026-05-28.

## What this is for

ZABAL Games is 3 months of building with The ZAO. June workshops, July open build-a-thon, August Finals with embedded ZAO mentors. $500 USDC for top 8, $ZABAL for top 16, permanent collectible NFT for everyone who ships. Free. Anyone welcome.

Landing: https://zabalgames.com
Lead signup: https://zabalgames.com/lead.html
Farcaster channel: https://farcaster.xyz/~/channel/zabal
Magnetiq portal: (link forthcoming via Tyler Stambaugh)
Lu.ma calendar: https://luma.com/ZABALgames

## Brand voice (1-pager)

**Tagline:** 3 months of building with The ZAO. Free to join. Anyone welcome.

**Permission to do:** Real shipped builds, mentor-paired, public, fun.
**Permission to skip:** Hackathon prizefighting, gated cohorts, NDA culture, dry tutorials.

**The frame:** Vibe-coding with a ZAO mentor in your corner. The build matters, but the relationship matters more. Walk away with a real artifact + a real connection + a real onchain credential whether you stay or not.

**Tone:** Direct, builder-to-builder, no marketing veneer. Mention specific tools (Claude Code, Cursor, Empire Builder, Juke, POIDH) by name. Drop the prize amount early. Make "free" visible.

## Palette

| Token | Hex | Use |
|-------|-----|-----|
| `--bg` | `#070709` | Page background, deep void |
| `--text` | `#e4e2dd` | Primary body text on dark |
| `--text-muted` | `#8a8895` | Secondary / caption text |
| `--cyan` | `#00e5ff` | Links, primary CTA, ZABAL accent |
| `--orange` | `#ff6b35` | Highlight, secondary accent, energy |

Inverse (for light-bg cards): swap `--bg` and `--text`. Cyan + orange both work on white.

## Typography

Single system stack for speed + max compatibility:

```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

Hierarchy:
- H1 / display: 700, 2.5-4rem
- H2 / section: 600, 1.5-2rem
- Body: 400, 1rem / 1.6 line-height
- Caption / meta: 400, 0.85rem, `--text-muted`

## Assets in this folder

| File | What | Status |
|------|------|--------|
| `binaural-60s.mp3` | 60s pre-cleared binaural beat (240Hz L + 244Hz R = 4Hz alpha) for background audio under bounty ads | SHIPPED 2026-05-28 |
| `README.md` | This file | SHIPPED |
| `palette.svg` | Color swatches inline SVG | SHIPPED |
| `logo-wordmark.svg` | "ZABAL GAMES" wordmark vector | TODO - generate from zabalgames.html header |
| `logo-mark.svg` | Compact mark for tight spaces | TODO |
| `b-roll-channel-walkthrough.mp4` | 10-15s screen capture of `/zabal` Farcaster channel | TODO |
| `b-roll-magnetiq-portal.mp4` | 10-15s screen capture of Magnetiq portal | TODO - coordinate with Tyler Stambaugh |
| `b-roll-workshop-1.mp4` | 10-15s screen capture of a recorded workshop | TODO - pull from Lu.ma recordings once first workshop drops |
| `prize-card-500usdc.png` | "$500 USDC + $ZABAL + collectibles" 1080x1080 | TODO |
| `prize-card-tiers.png` | "Top 8 paid, top 16 earn ZABAL, all finishers get NFT" 1080x1080 | TODO |
| `social-template-farcaster.png` | 1200x630 Farcaster embed card | TODO |
| `social-template-x.png` | 1200x675 X card | TODO |

Empty rows ship as the campaign grows. The MP3 + this README + palette unlock Round 3 of the BCZ POIDH bounty (an ad for zabalgames.com).

## Audio rule (for BCZ POIDH bounty submissions)

**No random background music or ambient music under dialog. If you want non-silence, use a binaural beat (single sustained tone with 8-30Hz beat between L+R channels). Original episode audio fine. One clear instrumental fine if it doesn't compete with dialog. Layered melodic music = floor fail.**

The `binaural-60s.mp3` in this folder is pre-cleared for this use. Drop it under your edit at low volume (10-30%) for ambient hum that doesn't compete with spoken dialog. Loop seamlessly for ads longer than 60s.

DIY alternative: open Audacity, `Generate -> Tone`, set Left = 240Hz + Right = 244Hz, duration 60s, amplitude 0.3, export as MP3.

## License

CC-BY 4.0. Remix, mash up, recolor, re-time, re-voice freely. Attribution: keep "ZABAL Games" or "zabalgames.com" visible in the final piece.

If you build something with this kit, post it in `/zabal` on Farcaster + tag `@bettercallzaal` so we can boost it.

# Assets Needed — authenticity & polish checklist

The site is currently text-rich but visually sparse (one photo of Zaal site-wide, zero
images on every portfolio sub-page). This tracks the media that would make it visibly
real. Drop files into the folders below and tell me the filenames — I'll wire them in.

Folder convention: `assets/{people,projects,events,brand,demos,yapz,outdoors}/`

## Tier 1 — highest authenticity impact
- [ ] **Product screenshots** → `assets/projects/` — 4–5 is enough to transform the portfolio
      (thezao, wavewarz live battle, empire-builder, zlank, an agent run)
- [ ] **Testimonial author photos** → `assets/people/` — `hurric4n3ike.jpg`, `jose-cabrera.jpg`
      (square ~200px; gradient-initials avatars are live as a stand-in until then)
- [ ] **IRL / event photos** → `assets/events/` — ZAO-Chella, first IRL WaveWarZ battle, ZAO HOUSE, festivals
- [ ] **More shots of Zaal** → `assets/people/` — on stage, at events, building

## Tier 2 — per-page gaps
- [ ] **BCZ YapZ media** → `assets/yapz/` — episode covers, guest headshots, + YouTube IDs / Spotify URL / RSS
- [ ] **Project logos** → `assets/brand/` — WaveWarZ, ZAOstock, BCZ YapZ, Hermes, Zlank, Farscout, COC Concertz
- [ ] **Brand kit visuals** (`kit.html` has 0 images) — the logos/marks for the brands it lists
- [ ] **Résumé PDF** — a "Download PDF" button is now live (browser print-to-PDF); a hand-designed
      `assets/resume.pdf` could replace it later
- [ ] **Demo clips** → `assets/demos/` — WaveWarZ battle, Zlank building a Snap, an agent run (15–30s MP4/GIF)

## Tier 3 — social / polish
- [ ] **1200×630 OG card** — render `assets/og/foss-card.html` to PNG; wire into og:image / twitter:image / manifest
- [ ] **Outdoors photos** → `assets/outdoors/` (2 placeholder slots)
- [ ] **binaural-60s.wav → MP3** — `ffmpeg -i assets/zabal-games-brand/binaural-60s.wav -b:a 128k assets/zabal-games-brand/binaural-60s.mp3` (5.2MB → ~500KB)
- [ ] **"Operating across" strip** — optional real logos instead of text wordmarks

## Organization (no media needed)
- [ ] Migrate existing flat assets into the convention (`pfp.jpeg` → `assets/people/`, `zao-logo.png` → `assets/brand/`)
- [ ] Decide on orphans: `/research/` (internal docs, currently public), `zabalgames.html`, `poidh-round2/3-judging.html`

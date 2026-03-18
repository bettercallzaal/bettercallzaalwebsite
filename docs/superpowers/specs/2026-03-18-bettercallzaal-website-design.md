# BetterCallZaal.com — Website Redesign Spec

**Date:** 2026-03-18
**Status:** Approved

---

## Purpose

Redesign BetterCallZaal.com from a minimal landing page into a simple, clean consulting website that positions Zaal as "The Connector" — someone who listens to your problem, connects you with the right people, and drives collaboration toward a specific goal. The ZAO ecosystem serves as proof of network and credibility, not the primary focus.

## Target Audience

Anyone with a vision — founders, artists, businesses, individuals of any size. Web3-native visitors and mainstream visitors alike.

## Aesthetic Direction

- **Approach:** Bold editorial + web3-native culture, kept simple
- **Base:** Dark theme
- **Accents:** Vibrant gradients (no purple — think electric orange, cyan, gold)
- **Typography:** Bold editorial — distinctive display font + refined body font
- **Layout:** Asymmetric where it serves the design, generous whitespace
- **Motion:** Scroll-triggered fade-ins, subtle hover states. CSS-only, nothing heavy.
- **Tone:** Experimental and bold but accessible. Not corporate. Not generic AI slop.

## Tech

- Single `index.html` file (HTML/CSS/JS)
- No framework, no build step
- Google Fonts for typography
- Form submissions: client-side for now (no backend yet)

## Sections

### 1. Hero

- **Headline:** "Got a problem? BetterCallZaal."
- **Subtext:** Explains the value prop in one line — connects you with the right people to build, grow, and ship.
- **CTA:** Button scrolling to contact form
- **Social icons:** X (@bettercallzaal), Instagram (@bettercallzaal), LinkedIn (linkedin.com/in/zaalp), GitHub (github.com/bettercallzaal)
- Dark background with gradient accent on headline

### 2. About — "The Connector"

Short, conversational paragraph. No stats, no credential dumps. Two clear paths:

1. **Join the ZAO** — if you're an artist or creator, join the community and connect with folks
2. **The Zaal Connector Treatment** — tell Zaal your challenge, he connects you with the right people and pushes toward a specific collaboration goal

Copy direction:
> "I'm Zaal. Engineer turned web3 builder, based in Maine. I built The ZAO — a creator infrastructure ecosystem helping independent artists own their work, their audience, and their revenue. If you're an artist or creator, join the ZAO and connect with the community. If you've got a specific challenge, get the Zaal Connector Treatment — I'll listen to your problem, connect you with the right people, and push toward a real collaboration with a clear goal."

### 3. Ecosystem

Simple cards/tiles showing what Zaal is connected to. Each card has a name, one-line description, and a link. No interactive graph — just clean proof the network is real.

- **The ZAO** — Creator infrastructure ecosystem for independent artists | thezao.com
- **WaveWarZ** — Live traded music battles on Solana | wavewarz.com
- **ZAO Festivals** — Side events at crypto conferences + planned flagship festivals | zaofestivals.com
- **Let's Talk About Ethereum** — Weekly podcast on Ethereum ecosystem impact | pods.media/lets-talk-about-web3
- **Daily Newsletter** — Build-in-public documentation on Paragraph | paragraph.com/@thezao

### 4. Testimonials

Two parts:

**Display:** Testimonial cards showing name, quote, and optionally a profile link/photo. Clean grid or staggered layout.

**Submission form:** "Worked with Zaal? Leave a testimonial."
- Fields: Your name, your profile link (X/LinkedIn/website), your testimonial
- Submissions email Zaal for approval before going live
- Email sent to zaalp99@gmail.com

### 5. Contact Form

- **Fields:** Your name, What do you want to build?, Best way to reach you
- **Book a call:** Link to custom booking page (to be built separately)
- Form submission: client-side success state for now

### 6. Footer

- BetterCallZaal branding
- Social icons: X, Instagram, LinkedIn, GitHub
- Email: zaalp99@gmail.com

## Social Links

| Platform | Handle / URL |
|----------|-------------|
| X | @bettercallzaal |
| Instagram | @bettercallzaal |
| LinkedIn | https://www.linkedin.com/in/zaalp/ |
| GitHub | https://github.com/bettercallzaal |
| Email | zaalp99@gmail.com |

## Out of Scope

- Custom booking/calendar tool (separate project)
- Backend/database for testimonial storage (future)
- Actual email sending for testimonial approval (needs backend or third-party service)
- The ZAO ecosystem site itself (thezao.com)

## Open Questions

- Exact gradient color palette to be determined during implementation
- Font pairing to be determined during implementation (no generic fonts — must be distinctive)
- Testimonial email approval flow will need a backend service or third-party integration (Formspree, EmailJS, etc.) — for v1, form shows success state and we note the limitation

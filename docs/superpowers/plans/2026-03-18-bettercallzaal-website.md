# BetterCallZaal.com Website Redesign — Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild index.html into a full consulting website with 6 sections: hero, about, ecosystem, testimonials, contact form, and footer.

**Architecture:** Single index.html file with inline CSS and JS. No framework, no build step, no backend. Google Fonts for typography. Forms show client-side success states.

**Tech Stack:** HTML, CSS, vanilla JS, Google Fonts

**Spec:** `docs/superpowers/specs/2026-03-18-bettercallzaal-website-design.md`

---

## Chunk 1: Full Implementation

This is a single-file project — one task to rewrite `index.html`.

### Task 1: Rewrite index.html

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Set up document structure, CSS variables, and fonts**

Replace the entire `index.html`. Set up:
- HTML boilerplate with meta tags and Open Graph tags for social sharing
- Google Fonts: pick a distinctive display font (e.g., Syne, Clash Display via CDN, or Cabinet Grotesk) + body font (e.g., Outfit, Satoshi, or General Sans). NO Inter, Roboto, Arial, Space Grotesk.
- CSS reset and variables: dark base (`#0a0a0a`), vibrant gradient accents (electric orange `#ff6b35` to cyan `#00e5ff`, with gold `#f5c842` as secondary), text colors, spacing scale
- Scroll-triggered fade-in animation class using IntersectionObserver
- Responsive base styles

- [ ] **Step 2: Build the Hero section**

- Full-viewport hero with centered content
- Headline: "Got a problem?" on one line, "BetterCallZaal." on next line with gradient text
- Subtext one-liner explaining the connector value prop
- CTA button linking to `#contact`
- Row of social icons (X, Instagram, LinkedIn, GitHub) using inline SVGs
- Social links:
  - X: `https://x.com/bettercallzaal`
  - Instagram: `https://instagram.com/bettercallzaal`
  - LinkedIn: `https://www.linkedin.com/in/zaalp/`
  - GitHub: `https://github.com/bettercallzaal`
- Staggered fade-in animations on load

- [ ] **Step 3: Build the About section — "The Connector"**

- Section heading: "The Connector"
- Conversational paragraph (from spec copy direction)
- Two clear call-out blocks or cards:
  1. "Join the ZAO" — for artists/creators, link to thezao.com
  2. "The Connector Treatment" — for specific challenges, link to #contact
- Fade-in on scroll

- [ ] **Step 4: Build the Ecosystem section**

- Section heading: "The Network"
- 5 cards in a responsive grid (2-3 columns on desktop, 1 on mobile):
  1. The ZAO — "Creator infrastructure ecosystem for independent artists" → thezao.com
  2. WaveWarZ — "Live traded music battles on Solana" → wavewarz.com
  3. ZAO Festivals — "Side events at crypto conferences + flagship festivals" → zaofestivals.com
  4. Let's Talk About Ethereum — "Weekly podcast on Ethereum ecosystem impact" → pods.media/lets-talk-about-web3
  5. Daily Newsletter — "Build-in-public documentation on Paragraph" → paragraph.com/@thezao
- Each card: name, one-line description, external link arrow/icon
- Hover effect with border glow or gradient shift
- Fade-in on scroll

- [ ] **Step 5: Build the Testimonials section**

**Display side:**
- Section heading: "What people say"
- 2-3 placeholder testimonial cards (Zaal can replace with real ones later)
- Each card: quote text, person's name, profile link
- Staggered grid layout

**Submission form:**
- Subheading: "Worked with Zaal? Leave a testimonial."
- Fields: Your name (text), Your profile link (url), Your testimonial (textarea)
- Submit button
- On submit: hide form, show success message ("Thanks! Your testimonial has been submitted for review.")
- Client-side only for v1

- [ ] **Step 6: Build the Contact Form section**

- Section heading: "Let's build something."
- Subtext with mailto link to zaalp99@gmail.com
- Fields: Your name (text), What do you want to build? (textarea), Best way to reach you (text)
- Submit button
- Placeholder "Book a call" link (href="#" with text indicating coming soon)
- On submit: hide form, show success message
- `id="contact"` for hero CTA scroll target

- [ ] **Step 7: Build the Footer**

- "BetterCallZaal" brand text with gradient
- Social icon row (same as hero): X, Instagram, LinkedIn, GitHub
- Email: zaalp99@gmail.com as mailto link
- Top border separator
- Compact padding

- [ ] **Step 8: Add scroll-triggered animations**

- IntersectionObserver script that adds a `.visible` class when sections enter viewport
- CSS transition: opacity 0 → 1, translateY(20px) → 0
- Apply `.fade-in` class to all section containers
- Stagger child elements where appropriate using `transition-delay`

- [ ] **Step 9: Test and verify**

- Open in browser: `open index.html`
- Verify all 6 sections render correctly
- Test responsive behavior (resize browser to mobile width)
- Click all external links (X, Instagram, LinkedIn, GitHub, thezao.com, wavewarz.com, etc.)
- Test both forms (contact + testimonial) — verify success states
- Test hero CTA scrolls to contact section
- Verify no horizontal overflow on mobile

- [ ] **Step 10: Commit**

```bash
git add index.html
git commit -m "feat: redesign BetterCallZaal.com with full consulting site layout"
```

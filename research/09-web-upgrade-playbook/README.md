# 08 — Web Upgrade Playbook (2026)

> **Status:** Research complete
> **Date:** 2026-08-15
> **Goal:** What actually moves the needle for bettercallzaal.com in 2026 - AI search (GEO), Farcaster distribution, performance, and conversion - checked against what the site already has.

---

## Key Takeaways

- **GEO beats classic SEO for this site.** AI answers cite pages with sourced statistics (+25.9% visibility), expert quotes (+27.8%), and explicit citations (+24.9%). The site's canon-metrics discipline (`data/metrics.json` with source URLs) is exactly the right raw material - it now needs question-shaped surfaces (FAQ blocks, quick-answer paragraphs) so engines can lift it.
- **The site is already ahead on several 2026 items:** `llms.txt` exists, JSON-LD Person/WebSite shipped, one FAQPage schema on `/history`, canonical + OG on all sub-pages. Gaps: no Speculation Rules, no View Transitions, no mini app notifications webhook, FAQ schema on only one page.
- **llms.txt reality check:** still a community convention; major AI crawlers mostly skip it and read HTML directly. Keep it (costs nothing, forward bet), but invest effort in the HTML itself: clear headings, answer-first paragraphs, verifiable facts.
- **Strategic shift on distribution:** Base App ended Creator Rewards (~$450K paid to 17K creators, avg $26) and dropped its Farcaster social feed to focus on trading. Farcaster mini app distribution now depends more on the Farcaster client itself, notifications, and share-loops - not Base App surfaces. Creator Coins/Zora remain intact.
- **Farcaster mini app ranking is engagement-driven:** trending score = recent usage + growth. The two levers the site does not use yet: **notifications** (webhookUrl in the manifest; re-engagement is the #1 retention tool) and **share-loops** (users casting their session/result - the Insert Coin pull is a natural fit).
- **Performance:** the two highest-impact 2026 browser APIs are basically free for a static site: **Speculation Rules** (prerender likely next pages - instant nav between /, /projects, /history) and **View Transitions** (native page-morph animation, no JS). INP is the punishing metric industry-wide (43% of sites fail 200ms), but a no-framework static site passes easily - keep it that way.
- **Conversion (sponsor-first):** case studies structured as challenge -> contribution -> decisions -> measurable outcome, 800-1500 words, results stated FIRST ("459 SOL traded" before the how). Contact must be reachable from the homepage without a page hop. Mobile readability is decisive - buyers review on phones.

---

## 1. GEO (Generative Engine Optimization) - the 2026 discovery channel

What the research says increases AI-answer citations:

| Tactic | Measured lift |
|---|---|
| Statistics with a clear source | +25.9% visibility |
| Direct expert quotes | +27.8% |
| Explicit source citations | +24.9% |
| Quick-answer block above the fold | qualitative but consistent across guides |
| Question-shaped headings + FAQ schema | consistent recommendation |
| Content freshness (7-14 day cycles) | consistent recommendation |

**Site fit:** metrics.json already enforces sourced stats. The `/history` page already carries FAQPage schema.

**Recommended actions**
1. Add FAQPage JSON-LD + a short visible FAQ to the highest-intent pages: `/` (who is Zaal / what is the ZAO / how to sponsor), `/zao/`, `/wavewarz/`, `/zaostock/`, `/resume/`.
2. Give every major page one **answer-first paragraph** near the top: a 2-3 sentence direct answer a model can quote whole, with a number and a source.
3. Keep `llms.txt` updated when pages are added (it is a cheap forward bet, not a ranking play today).
4. Freshness: the newsletter/shipping cadence is real - reflect it on-site (e.g. a "latest" line sourced from GitHub activity or the changelog) so crawls see recent-dated content.

## 2. Farcaster mini app distribution

- Ranking/trending = recent engagement + growth; manifest completeness (name, iconUrl, description, homeUrl) is table stakes - already done.
- **Notifications are the retention lever**: add `webhookUrl` to `.well-known/farcaster.json` and prompt users to "Save" the app; send sparse, high-signal notifications (new drop live, new episode). Currently absent.
- **Share-loops are the growth lever**: after a meaningful action (an Insert Coin pull, reading the story), offer one-tap `composeCast` with a result-bearing embed. Sessions shared in casts are the primary organic discovery loop.
- **Base App context:** Creator Rewards is dead and its Farcaster feed removed (trading focus). Do not build for Base App discovery surfaces; build for the Farcaster client + wallet mini app surfaces. Creator Coins/Zora unaffected.

## 3. Performance (already strong - two free upgrades)

- Site is no-framework static: LCP/CLS/INP should all pass. Protect this - keep resisting frameworks.
- **Add Speculation Rules** (one inline `<script type="speculationrules">`): prerender `/projects/`, `/history/`, `/zao/` on hover/visible links. Instant navigation for the cost of ~10 lines. Chromium-only, progressive enhancement.
- **Add View Transitions for multi-page** (`@view-transition { navigation: auto; }` CSS): native cross-page morph in Chromium, ignored elsewhere. Zero JS.
- Keep an eye on the one heavy directory: `assets/zabal-games-brand/` (WAV + large PNGs) - convert/compress locally.

## 4. Conversion for the sponsor-first goal

- Restructure the three flagship case pages (`/zao/`, `/wavewarz/`, `/zaostock/`) toward the four-part case-study arc: **challenge -> my contribution -> key decisions -> measurable outcome**, with the outcome stated in the first screen ("459 SOL / 950+ battles" before the story).
- 800-1500 words each with visual pacing (the media gap in ASSETS-NEEDED.md is the limiter here - screenshots and event photos do conversion work, not decoration).
- Contact/CTA reachable from every page without a hop (the Build Session offer from #37 is the right kind of front door - make sure it is one tap from the case pages too).
- Social proof placement: testimonial + logo strip near the CTA, not in a separate section.

---

## Priority order for implementation

1. **Manifest webhookUrl + save-prompt + share-loop** (distribution; pairs with Insert Coin launch)
2. **FAQ schema + answer-first paragraphs** on /, /zao/, /wavewarz/, /zaostock/, /resume/ (GEO)
3. **Speculation Rules + View Transitions** (10-line perf/UX upgrade)
4. **Case-study restructure of the three flagship pages** (conversion; needs the media assets)

## Sources

- Firebrand - GEO Best Practices 2026: https://www.firebrand.marketing/2025/12/geo-best-practices-2026/
- DigitalApplied - GEO Guide 2026: https://www.digitalapplied.com/blog/geo-guide-generative-engine-optimization-2026
- GenOptima - GEO Playbook 2026: https://www.gen-optima.com/blog/generative-engine-optimization-best-practices-complete-2026-playbook/
- aeo.press - State of llms.txt 2026: https://ai.aeo.press/the-state-of-llms-txt-in-2026
- Codersera - llms.txt honest guide (May 2026): https://codersera.com/blog/llms-txt-complete-guide-2026/
- Farcaster Mini Apps - Discovery: https://miniapps.farcaster.xyz/docs/guides/discovery
- Farcaster Mini Apps - Notifications: https://miniapps.farcaster.xyz/docs/guides/notifications
- CoinMarketCap - Base App ends Creator Rewards: https://coinmarketcap.com/academy/article/base-app-ends-creator-rewards-shifts-to-trading
- SitePoint - Core Web Vitals 2026, INP: https://www.sitepoint.com/core-web-vitals-2026-fix-interaction-to-next-paint/
- AlphonsoLabs - Frontend performance trends 2026: https://www.alphonsolabs.com/frontend-performance-trends-2026/
- Case Study Club - portfolio case studies: https://www.casestudy.club/journal/ux-designer-portfolio
- Figma - portfolio website examples: https://www.figma.com/resource-library/portfolio-website-examples/

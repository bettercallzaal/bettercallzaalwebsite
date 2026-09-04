# 09 — Notifications, Entity SEO, and Drop Mechanics

> **Status:** Research complete
> **Date:** 2026-08-15
> **Goal:** Implementation-grade follow-up to doc 08's priority list: (1) how to ship Farcaster mini app notifications from a static site, (2) entity/E-E-A-T presence so AI engines answer "who is Zaal Panthaki" correctly, (3) blind-box psychology to sharpen the Insert Coin drop.

---

## Key Takeaways

- **Notifications need no self-hosted backend.** Neynar's managed webhook takes the manifest's `webhookUrl` slot (`https://api.neynar.com/f/app/<client_id>/event`), stores/rotates notification tokens for you, auto-handles permission revokes, and sending is one API call. This removes the "static site cannot do notifications" blocker entirely.
- **Notification spec constraints:** title max 32 chars, `notificationId` (max 128) is an idempotency key, batch up to 100 tokens per send, `targetUrl` must be on the app's domain. Hosts enforce per-token rate limits (spec-recommended on the order of 1 per 30s and a daily cap) - design for sparse, high-signal sends only.
- **Entity SEO status: already strong.** The Person schema carries `sameAs` (X, GitHub, Farcaster, LinkedIn, thezao.com), `alumniOf`, affiliation, `knowsAbout`. The two missing authority anchors are **Wikidata** (the single highest-value target - a Q-number feeds knowledge graphs directly and is the priority sameAs per 2026 guides) and a consistent-name audit across profiles ("Zaal Panthaki" everywhere).
- **Blind-box psychology maps cleanly onto Insert Coin** - and the design already has the ethical guardrails (visible odds via a fixed pool, commit-reveal fairness, ~$1 price, per-wallet cap). What the research adds: a **guarantee/pity mechanic measurably boosts repeat pulls**, **set-completion** drives collection behavior, and the **reveal moment** is where the dopamine lives - invest in the animation.

---

## 1. Shipping notifications without a backend (the how)

1. Create an app at dev.neynar.com; copy the events URL: `https://api.neynar.com/f/app/<client_id>/event`.
2. Set it as `webhookUrl` in `.well-known/farcaster.json` alongside the existing signed `accountAssociation`.
3. Client events (`miniapp_added`, `notifications_enabled`, disables/removals) now flow to Neynar; it stores the per-user notification tokens. Events are signed (JSON Farcaster Signature) so the client and user are verifiable.
4. Send via one Neynar API call (target FIDs or filters); it fans out, dedupes by `notificationId`, respects host rate limits.
5. In-app: after a meaningful action, call `sdk.actions.addMiniApp()` (or prompt to save) - added + notifications-enabled is the pair that creates a token.

**Send policy (respecting the ~1/30s + daily-cap per token limits):** only three triggers - new drop live (Insert Coin), new episode/appearance, ZAOstock milestones. Nothing else. Notification fatigue = removal, and removals kill trending score.

## 2. Entity SEO / "who is Zaal Panthaki" in AI answers

- 2026 guidance ranks sameAs targets: **Wikidata first** (direct knowledge-graph feed), then Wikipedia (if ever attainable), LinkedIn, Crunchbase, GitHub. Site already has 5 good targets; **action: create a Wikidata item** for Zaal Panthaki (founder of The ZAO, b. RIT 2022, Maine; cite press/podcast appearances as references) and add its URL to `sameAs`.
- Person schema increasingly carries E-E-A-T weight: AI systems attribute trust to author entities. Keep `jobTitle`, `alumniOf`, affiliations current; add `sameAs` links on sub-pages' Person references too (resume page especially).
- Consistency audit: the exact string "Zaal Panthaki" + "BetterCallZaal" should match across X, LinkedIn, GitHub, Farcaster, Paragraph, podcast show notes. Inconsistent naming fragments the entity.

## 3. Drop mechanics for Insert Coin (what the psychology says)

| Mechanic | Research finding | Insert Coin application |
|---|---|---|
| Variable-ratio reward | Slot-machine schedule; dopamine per pull regardless of outcome | Core pull is already this; keep pulls cheap (~$1) so it stays play, not gambling |
| Scarcity + FOMO | Perceived scarcity drives overweighting of gains; staggered drops amplify | Live "X of N left" counter (built) + fixed daily reset time creates the ritual |
| Guarantee / pity system | Measurably heightens excitement and repeat purchases | e.g. every 5th pull guaranteed from a "featured" subset, or a streak bonus for consecutive-day pulls |
| Set completion | Collection framing drives return visits | Public gallery of the week's pulls; "you own 3 of this week's 35" |
| Transparent odds | Fairness perception sustains long-term trust; opaque odds invite backlash | Commit-reveal seed (already specced) + show remaining-pool composition |
| The reveal moment | The anticipation window is the product | Invest in the flip animation + composeCast share right at reveal (doubles as the growth loop from doc 08) |

**Ethical line:** disclose odds, cap per-wallet, fixed $1-ish price, no dark timers. The mechanics above work *with* transparency; the gamblification backlash research targets opaque, escalating-spend systems.

---

## Recommended build order (merges with doc 08's list)

1. Neynar webhook + `webhookUrl` in manifest + save-prompt in the mini app (unlocks notifications forever)
2. Wikidata item + `sameAs` addition (one-time, permanent entity anchor)
3. Insert Coin v1 ships with: counter, commit-reveal, reveal animation + share-cast (already specced) - add pity/streak + gallery in v1.5, not v1
4. Notification triggers wired to drops when Insert Coin goes live

## Sources

- Farcaster Mini Apps - Notifications guide: https://miniapps.farcaster.xyz/docs/guides/notifications
- Farcaster Mini Apps - Specification (title/notificationId/batch limits): https://miniapps.farcaster.xyz/docs/specification
- Neynar - Send notifications to mini app users: https://docs.neynar.com/docs/send-notifications-to-mini-app-users
- Neynar managed services for mini apps: https://miniapps.farcaster.xyz/docs/managed-services/neynar
- DigitalApplied - Entity SEO & Knowledge Graph 2026: https://www.digitalapplied.com/blog/entity-seo-knowledge-graph-optimization-guide-2026
- OrganiKPI - sameAs entity disambiguation for AI citations: https://organikpi.com/blog/technical-seo/schema-sameas-entity-disambiguation-ai-citations/
- Stackmatix - Organization schema / knowledge graph guide 2026: https://www.stackmatix.com/blog/organization-schema-knowledge-graph
- PMC - Blind box uncertainty and irrational consumption (scarcity, gambler's fallacy): https://pmc.ncbi.nlm.nih.gov/articles/PMC11969734/
- Milijana Komad - Gacha systems and variable reinforcement: https://medium.com/design-bootcamp/product-design-and-psychology-exploring-gacha-mechanics-in-video-game-design-1015511cf00c
- Vero - Psychology behind blind box collection: https://vero-asean.com/the-psychology-behind-blind-box-collection-in-the-art-toy-world/
- Killscreen - Gamblification critique (the line not to cross): https://www.killscreen.com/gamblification-labubu-loot-boxes-gambling-mechanicsretry/

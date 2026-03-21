# 02 — BetterCallZaal GitHub Inventory

> **Status:** Research complete
> **Date:** 2026-03-21
> **Goal:** Inventory of Zaal's 65 public repos and which patterns are reusable for bettercallzaal.com

---

## Key Takeaways

- 65 public repos, 1 new repo every ~6 days average
- Strong in: Next.js/TypeScript, Farcaster, ElizaOS, music tech, web3, fractal governance
- NEXUS series (20 repos) has battle-tested multi-chain token gating patterns
- fractalbot series (7 repos) has fractal democracy + Respect token distribution
- zabalbot / WARZAI have ElizaOS agent architecture reusable for a future BCZ bot
- ZAO OS (zaoos) is the flagship — gated music social platform, the "main project"

---

## Tier 1 — ZAO Core Projects

| Repo | Purpose | Relevance to BCZ site |
|------|---------|----------------------|
| zaoos | Main ZAO music client (Next.js, Farcaster, XMTP) | Context for Farcaster patterns |
| ZOUNZ | NFT mini app | Mini app architecture reference |
| zaomusicbot | Discord music bot | Bot patterns |
| ZAO-Leaderboard | Community leaderboard | Could embed on BCZ site |
| zao-stock | Stock/asset tracker | — |
| CoCConcertZ | Concert coordination | — |
| ZAO-Video-Editor | Video editing tool | — |

## Tier 2 — NEXUS Series (20 repos)

Token-gated portals with multi-chain token gating (ethers.js + Alchemy RPC). Patterns reusable if BCZ site ever adds gated content.

Key patterns extracted:
- `ethers.js` for wallet connection + balance checks
- Alchemy RPC for multi-chain support
- JWT session after token verification

## Tier 3 — AI Agents

| Repo | Framework | Notes |
|------|-----------|-------|
| zabalbot | ElizaOS | Main ZAO AI agent |
| WARZAI | ElizaOS | War/battle AI variant |

If a BCZ Farcaster bot is ever built, use ElizaOS + `@elizaos/plugin-farcaster` + Neynar managed signer. Estimated cost: ~$65-100/month.

## Tier 4 — Fractal Governance (7 repos)

fractalbot series: Discord bots for fractal democracy sessions — random groups → voting → Respect token submission. Core to ZAO community governance.

## Developer Profile

- Platform: GitHub `@bettercallzaal`
- Language mix: TypeScript/Next.js dominant, some Python, vanilla JS
- Cadence: 1 new repo every ~6 days
- Style: Move fast, build in public, iterate publicly

---

## Sources

- [BetterCallZaal GitHub](https://github.com/bettercallzaal)
- [ZAO OS Research Doc 30 — BetterCallZaal GitHub Inventory](../../zaoos/research/30-bettercallzaal-github/)

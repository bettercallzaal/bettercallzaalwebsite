# BCZ Streaming

Personal-streaming setup notes for Zaal. Twitch + StreamElements stack. Canonical research lives at ZAO OS Doc 627.

## Quick Decisions

- **Platform:** Twitch (primary), restream to YouTube + Kick later
- **Capture:** OBS Studio (free, native)
- **Overlays + alerts + tip page:** StreamElements (cloud, free, lower CPU than Streamlabs)
- **Chat bot:** StreamElements chatbot (Twitch-side) + ZOE for ZAO-aware replies
- **Auth model:** JWT for personal channel. Move to OAuth2 if/when ZAO multi-tenant streaming ships

## Goal Path

1. Hit **Twitch Affiliate** - 50 followers, 500 broadcast minutes, 7 unique days, 3 avg concurrent viewers (30-day rolling)
2. Once Affiliate: subs at $4.99 / $9.99 / $24.99 with 50% rev share. Bits at $0.01 each. Payout NET 15 above $50
3. Wire stream events into BCZ Farcaster mini app - live indicator on `bettercallzaal.com`

## Setup Checklist

- [ ] Register Twitch Developer app at https://dev.twitch.tv/console
- [ ] Connect Twitch to StreamElements at https://streamelements.com
- [ ] Grab JWT from `streamelements.com/dashboard/account/channels`
- [ ] Build SE overlay with ZAO orange/cyan + Syne font (browser-source URL into OBS)
- [ ] Customize tip page CSS - default UI is clunky
- [ ] Configure chatbot commands: `!zao`, `!fid`, `!bcz`, `!schedule`
- [ ] Test alerts (tip / follow / sub / cheer / raid) via SE dashboard test trigger
- [ ] Add Twitch live-state badge to `index.html` (poll Helix `/streams` every 60s)
- [ ] Hit Affiliate thresholds; toggle subs + bits

## OBS + StreamElements

Single browser source per scene. SE renders all overlays cloud-side. CPU stays at 3-5%.

```
OBS Scene -> Browser Source -> https://streamelements.com/overlay/<overlay-id>/<token>
```

## StreamElements Realtime (for BCZ mini app)

WebSocket at `https://realtime.streamelements.com` (Socket.IO 2.2+):

```js
const socket = io('https://realtime.streamelements.com', { transports: ['websocket'] });
socket.on('connect', () => socket.emit('authenticate', { method: 'jwt', token: SE_JWT }));
socket.on('event', (e) => {
  // e.type: tip | follow | subscriber | cheer | raid | host
  // e.data: { username, amount, message, tier, streak, ... }
});
```

Server pings every 30s; client must pong within 70s or connection drops.

## Twitch 2026 Direction (Don't Build IRC)

- IRC has new concurrent-join limits + is on the deprecation path
- Use **EventSub WebSocket** for chat reads (`channel.chat.message`, scope `user:read:chat`)
- Use **Helix `POST /helix/chat/messages`** for chat sends (scope `user:write:chat`)
- WebSocket transport caps at 300 subscriptions per connection - plenty for one channel

## Chatbot Command Ideas

| Command | Returns |
|---------|---------|
| `!zao` | Link to bettercallzaal.com |
| `!bcz` | "BetterCallZaal - engineer + builder in web3/Farcaster/music ecosystem" |
| `!fid` | Viewer FID lookup (custom variable hitting Neynar) |
| `!schedule` | Next stream time |
| `!tip` | Link to SE tip page |
| `!socials` | Farcaster + X + Bluesky links |

## Mini App Live Indicator (Future PR)

Add to `index.html`:

```js
async function pollTwitchLive() {
  const res = await fetch('/api/twitch-status'); // serverless edge fn
  const { isLive, viewerCount, title } = await res.json();
  document.querySelector('[data-live-badge]')?.classList.toggle('hidden', !isLive);
}
setInterval(pollTwitchLive, 60_000);
```

Edge function hits Helix `GET /streams?user_login=<login>` with App access token. App token rate limit: 800/min, plenty.

## Skip List

- **Streamlabs Desktop** - desktop-only, paywalls overlay templates, heavier CPU
- **OBS.Live** (StreamElements' OBS fork) - extra fork to maintain, no real upside vs OBS + browser source
- **SE Sponsorships (SE.SP)** - invitation-only marketplace, doesn't fit ZAO sovereignty thesis
- **Streamlabs full Kick integration** - not Kick-first, not relevant

## Web3 Layer (see Doc 628)

Streaming infra is Phase 0. Phases 1-4 layer in $ZABAL Empire scoring, Coinflow tip checkout, Hypersub recurring support, 0xSplits revenue routing, EAS watch-time attestations, and Zora content-coin drops. Full architecture in Doc 628.

Quick map:

| Phase | Ship | Stack |
|-------|------|-------|
| 1 (this month) | Tip checkout + 0xSplits split (85/10/5 BCZ / ZABAL / ZAO ops) | Coinflow + 0xSplits |
| 2 (next month) | Stream-leaderboard JSON feed -> Empire Builder pulls + distributes ZABAL | Same POIDH `apiLeaderboards` pattern (Doc 626) |
| 3 (Q3) | Hypersub creator-supporter tiers + EAS watch-time attestations | Hypersub + EAS on Base |
| 4 (Q4) | Zora content-coin auto-mints + ZOE/BANKER agents in chat | Zora + Privy + 0x |

## Cross-Reference

- ZAO OS Doc 628 - Web3 streaming + ZABAL Empire bridge (full architecture)
- ZAO OS Doc 627 - Twitch Streaming + StreamElements (streaming infra layer)
- ZAO OS Doc 626 - Empire Builder + ZABAL POIDH airdrop (apiLeaderboards pattern)
- ZAO OS Doc 361 - Empire Builder v3 deep dive (multipliers, distribute/burn endpoints)
- ZAO OS Doc 324 - ZABAL/SANG Wallet Agent Tokenomics (0x + Privy + Base Paymaster)
- ZAO OS Doc 214 - Twitch Helix API integration deep-dive
- ZAO OS Doc 192 - Multiplatform streaming RTMP (when ready to fan out)
- ZAO OS Doc 215 - OBS / Restream / Streamyard comparison
- ZAO OS Doc 125 - Coinflow fiat checkout integration patterns

Path: `/Users/zaalpanthaki/Documents/ZAO OS V1/research/cross-platform/627-twitch-streaming-streamelements-integration/`

## Sources

- StreamElements docs: https://docs.streamelements.com/
- StreamElements OAuth2: https://dev.streamelements.com/docs/api-docs/cd02cda5171ea-o-auth2
- StreamElements WebSocket: https://github.com/StreamElements/api-docs/blob/main/docs/Websockets.md
- Twitch IRC migration: https://dev.twitch.tv/docs/chat/irc-migration/
- Twitch EventSub: https://dev.twitch.tv/docs/eventsub/
- Twitch Affiliate: https://help.twitch.tv/s/article/joining-the-affiliate-program

Last validated: 2026-05-09

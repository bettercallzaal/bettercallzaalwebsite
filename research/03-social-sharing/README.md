# 03 — Social Sharing Best Practices

> **Status:** Research complete + implemented
> **Date:** 2026-03-21
> **Goal:** How to make bettercallzaal.com easily shareable across Farcaster, X, and LinkedIn

---

## Key Takeaways

- Use `sdk.actions.composeCast()` inside Farcaster mini app; fall back to Warpcast compose URL outside
- X share intent: `https://twitter.com/intent/tweet?text=...&url=...&via=...` — don't put URL in both `text` and `url`
- LinkedIn: `https://www.linkedin.com/sharing/share-offsite/?url=...` — pulls OG tags automatically, no other params needed
- Add Twitter Card meta tags for rich X preview (`summary` or `summary_large_image`)
- `og:image` should ideally be 1200x628px for universal compatibility across platforms

---

## Status in This Repo ✅

| Item | Status |
|------|--------|
| Share bar (Farcaster, X, LinkedIn) | ✅ Implemented above footer |
| Twitter Card meta tags | ✅ |
| `og:image` + `og:url` | ✅ |
| `fc:miniapp` embed (Farcaster cast preview) | ✅ |

---

## Share URL Patterns

### Farcaster

**Inside mini app** (use SDK):
```javascript
sdk.actions.composeCast({
  text: 'Got a problem? BetterCallZaal. The Connector.',
  embeds: ['https://bettercallzaal.com']  // max 2 embeds
});
```

**Outside mini app** (link):
```
https://warpcast.com/~/compose?text=Got%20a%20problem%3F%20BetterCallZaal.&embeds[]=https%3A%2F%2Fbettercallzaal.com
```

When `bettercallzaal.com` is in the embed, Farcaster renders the `fc:miniapp` card with a launch button — not just a link preview.

### X / Twitter

```
https://twitter.com/intent/tweet?text=Got%20a%20problem%3F%20BetterCallZaal.%20The%20Connector.&url=https%3A%2F%2Fbettercallzaal.com&via=bettercallzaal
```

Parameters:
| Param | Description |
|-------|-------------|
| `text` | Pre-filled tweet body |
| `url` | URL to append (shown as t.co link, counts toward 280 chars) |
| `via` | Twitter handle for attribution |
| `hashtags` | Comma-separated, no `#` |

### LinkedIn

```
https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fbettercallzaal.com
```

LinkedIn pulls title, description, and image from OG tags automatically. No other params needed.

---

## Meta Tags for Rich Previews

```html
<!-- Open Graph — drives LinkedIn, Telegram, general previews -->
<meta property="og:title" content="BetterCallZaal — The Connector">
<meta property="og:description" content="Engineer. Builder. Connector.">
<meta property="og:image" content="https://bettercallzaal.com/assets/icon.png">
<meta property="og:url" content="https://bettercallzaal.com">
<meta property="og:type" content="website">

<!-- Twitter Card — drives X rich preview -->
<meta name="twitter:card" content="summary">
<meta name="twitter:site" content="@bettercallzaal">
<meta name="twitter:title" content="BetterCallZaal — The Connector">
<meta name="twitter:description" content="Engineer. Builder. Connector.">
<meta name="twitter:image" content="https://bettercallzaal.com/assets/icon.png">

<!-- Farcaster — makes URL launchable as a mini app in casts -->
<meta name="fc:miniapp" content='{...}'>
```

## Image Size Guide

| Platform | Recommended Size | Ratio |
|----------|-----------------|-------|
| Universal safe zone | 1200×628px | ~1.91:1 |
| Farcaster embed (`imageUrl`) | 1200×800px | 3:2 |
| Farcaster icon | 1024×1024px | 1:1 |
| Farcaster splash | 200×200px | 1:1 |
| Twitter large card | 1200×600px | 2:1 |

Current: `/assets/icon.png` is 1:1 square — works for icon/splash. Consider creating a dedicated 1200×628 OG image for richer social previews.

---

## Sources

- [Farcaster Mini Apps — Sharing Guide](https://miniapps.farcaster.xyz/docs/guides/sharing)
- [X Web Intent](https://developer.x.com/en/docs/x-for-websites/tweet-button/guides/web-intent)
- [LinkedIn Share](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin)
- [Open Graph Protocol](https://ogp.me/)

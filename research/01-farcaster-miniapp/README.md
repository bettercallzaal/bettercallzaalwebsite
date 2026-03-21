# 01 — Farcaster Mini App Integration

> **Status:** Research complete + implemented
> **Date:** 2026-03-21
> **Goal:** What's needed to make bettercallzaal.com a Farcaster Mini App

---

## Key Takeaways

- Add `fc:miniapp` meta tag to `<head>` — makes the URL launchable from casts
- Serve `/.well-known/farcaster.json` — domain manifest with account association signature
- Import `@farcaster/miniapp-sdk` via CDN — call `sdk.actions.ready()` immediately or users see infinite loading
- Use `sdk.actions.composeCast()` inside the mini app context for sharing; fall back to Warpcast compose URL outside
- Icon: 1024x1024 PNG (no alpha). Splash: 200x200px. Embed image: 3:2 ratio
- Always use `fc:miniapp` — never the old `fc:frame` syntax

---

## Status in This Repo ✅

All implemented:

| Item | File | Status |
|------|------|--------|
| `fc:miniapp` meta tag | `index.html` | ✅ |
| `og:image`, `og:url` | `index.html` | ✅ |
| Twitter Card meta tags | `index.html` | ✅ |
| `auth.farcaster.xyz` preconnect | `index.html` | ✅ |
| Domain manifest | `/.well-known/farcaster.json` | ✅ |
| Account association (FID 19640) | `/.well-known/farcaster.json` | ✅ |
| SDK init + `ready()` | `index.html` (module script) | ✅ |
| App icon + splash | `/assets/icon.png` | ✅ |
| Share bar (Farcaster, X, LinkedIn) | `index.html` | ✅ |

---

## The `fc:miniapp` Meta Tag

```html
<meta name="fc:miniapp" content='{
  "version": "1",
  "imageUrl": "https://bettercallzaal.com/assets/icon.png",
  "button": {
    "title": "Open BetterCallZaal",
    "action": {
      "type": "launch_frame",
      "name": "BetterCallZaal",
      "url": "https://bettercallzaal.com",
      "splashImageUrl": "https://bettercallzaal.com/assets/icon.png",
      "splashBackgroundColor": "#0a0a1a"
    }
  }
}'>
```

## The Manifest (`/.well-known/farcaster.json`)

```json
{
  "accountAssociation": {
    "header": "<base64 JFS header>",
    "payload": "<base64 domain>",
    "signature": "<base64 signature>"
  },
  "frame": {
    "version": "1",
    "name": "BetterCallZaal",
    "homeUrl": "https://bettercallzaal.com",
    "iconUrl": "https://bettercallzaal.com/assets/icon.png",
    "splashImageUrl": "https://bettercallzaal.com/assets/icon.png",
    "splashBackgroundColor": "#0a0a1a",
    "subtitle": "The Connector",
    "description": "Got a problem? BetterCallZaal...",
    "primaryCategory": "social",
    "tags": ["connector", "web3", "music", "builder"]
  }
}
```

Generate account association at: `farcaster.xyz/~/settings/developer-tools`

## SDK Initialization (CDN, no build step)

```html
<script type="module">
  import { sdk } from 'https://esm.sh/@farcaster/miniapp-sdk';

  const isMiniApp = !!sdk.context;

  if (isMiniApp) {
    sdk.actions.ready(); // REQUIRED — dismisses splash screen

    // Inside mini app: use SDK for sharing
    document.getElementById('share-farcaster').addEventListener('click', (e) => {
      e.preventDefault();
      sdk.actions.composeCast({
        text: 'Got a problem? BetterCallZaal. The Connector.',
        embeds: ['https://bettercallzaal.com']
      });
    });
  }
</script>
```

## Launch Flow

1. User shares `bettercallzaal.com` in a cast → Farcaster client sees `fc:miniapp` tag → renders embed card with launch button
2. User taps launch → client fetches `/.well-known/farcaster.json` to verify domain ownership
3. Splash screen shows (`icon.png` on `#0a0a1a` background)
4. Webview loads site → SDK calls `ready()` → splash dismisses → user sees site
5. Inside mini app: SDK available for `composeCast()`, `openUrl()`, etc.

## Viewport

- Web Farcaster clients: 424×695px
- Mobile: full device width
- Design breakpoint at 480px catches the mini app width — always test at 424px

## Best Practices (from ZAO OS research doc 68)

- `sdk.actions.ready()` MUST be called — failure = infinite loading screen
- `sdk.context.user` is untrusted client-side — verify server-side for auth decisions
- Add `<link rel="preconnect" href="https://auth.farcaster.xyz" />` for performance
- Context-aware routing: check `sdk.context.location` (cast, notification, launcher)
- Rate limits on notifications: 1/30s per user, 100/day per user

---

## Sources

- [Farcaster Mini Apps Docs](https://miniapps.farcaster.xyz)
- [Mini Apps Specification](https://miniapps.farcaster.xyz/docs/specification)
- [ZAO OS Research Doc 68 — Farcaster Mini Apps Integration](../../../zaoos/research/68-farcaster-miniapps-integration/)

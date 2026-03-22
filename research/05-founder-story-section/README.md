# 05 — Founder Story Section for BetterCallZaal

> **Status:** Research complete
> **Date:** 2026-03-22
> **Goal:** Research how to add a compelling founder/origin story to bettercallzaal.com

---

## Key Takeaways

- The current about section is 2 sentences — it undersells a story that includes an EE degree, a $1.5M robotics project, a Web3 pivot during a bear market, 2 festivals, 90+ governance meetings, and a relocation to rural Maine
- The best web3 founder sites (Dan Romero, Jesse Pollak, Vitalik) are hyper-minimal and let work speak — but they're already famous. Zaal needs to tell the story because the ecosystem is complex and new visitors won't know the context
- The story should be a journey, not a resume — show the arc from engineering to Web3 to creator infrastructure
- Keep it within the single-page design. No separate about page
- A compact timeline format works best for a dense journey — visual, scannable, and fits the dark aesthetic

---

## What Exists Today

The current about section (lines 802-822 of index.html):

```
"I'm Zaal. Engineer turned web3 builder, based in Maine. I built The ZAO —
a creator infrastructure ecosystem helping independent artists own their work,
their audience, and their revenue."
```

Two path cards follow: "Join the ZAO" and "Connector Treatment."

**What's missing:** The WHY. Why does the ZAO exist? Why does Zaal care about creator infrastructure? What's the journey that led here? Why should someone trust this person?

---

## How Other Web3 Founders Present Themselves

### Pattern 1: Ultra-Minimal (Dan Romero — danromero.org)

- One sentence: "I am currently working on Farcaster"
- List of angel investments
- No origin story, no narrative
- **Works because:** He's already known. Farcaster speaks for itself
- **Lesson for Zaal:** This only works when you're already famous. Skip this pattern

### Pattern 2: Narrative Arc (Jesse Pollak — jesse.xyz)

- Current role first: "I currently work on Base, which I created"
- Then reverse chronology: Coinbase → Clef → BuzzFeed
- Conversational and humble tone
- No stats, no timeline — just a paragraph
- **Works because:** Simple career progression that's self-explanatory
- **Lesson for Zaal:** The reverse-chronology approach is clean but Zaal's journey is more complex and non-linear. Needs more structure

### Pattern 3: Pure Output (Vitalik — vitalik.eth.limo)

- No about section at all
- Homepage is just a blog archive organized by category
- Identity expressed entirely through writing
- **Works because:** Vitalik IS Ethereum. Zero explanation needed
- **Lesson for Zaal:** Interesting that the 400+ newsletter editions and 88 research docs mirror this "output as identity" approach. Could reference this body of work in the story

### Pattern 4: Credential Display (Ritzy Periwinkle)

- Bio + credential table (UN, Congressional Briefing, client logos)
- Service categories with specific CTAs
- **Works because:** Consulting requires trust signals
- **Lesson for Zaal:** Zaal is a builder, not a consultant — but the ZAO has real credentials that should be visible (festivals produced, on-chain volume, governance meetings run)

---

## The Zaal Story Arc

From the ZAO Complete Guide, here's the raw material:

### Chapter 1: The Engineer
- BS Electrical Engineering, Rochester Institute of Technology (2022)
- Automation Engineer at PCC Structurals — led a $1.5M robotics project, 7x throughput improvement
- Traditional coding felt rigid. Then blockchain showed that software could move value directly between people

### Chapter 2: The Bear Market Builder
- Entered Web3 during the 2022-2023 bear market — the worst possible timing, which turned out to be the best
- The people still building were serious. No tourists
- Started as ZTalent Agency. Pivoted to the ZAO (ZTalent Artist Organization) in 2023
- Began collaborating with musicians and shifted toward creator infrastructure

### Chapter 3: The Problem
- Music industry pays artists $0.003 per stream
- Labels take 80-85% of revenue
- Platforms own the audience, the social graph, the algorithm
- When a platform shuts down, artists lose everything — because none of it belonged to them
- The tools to fix this exist (blockchain). The problem is distribution and community

### Chapter 4: The Builder
- Built The ZAO — not a platform, an ecosystem
- WaveWarZ: music battles with $50K+ on-chain volume
- ZAO Festivals: 2 festivals produced (NYC, Miami), 2 more planned
- ZAO OS: Farcaster client, governance tools, research library
- 400+ daily newsletter editions. 88 research documents. 65+ GitHub repos
- 90+ fractal governance meetings over nearly two years

### Chapter 5: The Connector
- Relocated to rural Maine — rich arts culture, zero blockchain exposure
- Connected with local musicians building the scene since the 1980s
- Plans for ZAO Stock — a real music festival, not a Web3 conference
- "The Connector" identity: brings the right people together

---

## Recommended Design Approach

### Format: Compact Visual Timeline

A vertical timeline that fits within the existing single-page flow. Each milestone is a short block — year on the left, one-liner on the right. No walls of text.

```
2022    BS Electrical Engineering, RIT
        Led $1.5M robotics project — 7x throughput

2022    Entered Web3 during the bear market
        "The people still building were serious"

2023    Founded The ZAO
        Creator infrastructure for independent artists

2024    ZAO-Palooza (NYC) + ZAO-Chella (Miami)
        22 artists. Live on-chain music battles

2025    400+ newsletter editions. 90+ governance meetings
        WaveWarZ hits $50K+ on-chain volume

2026    ZAO OS in active development
        ZAO Stock planned for October — Ellsworth, Maine
```

### Why Timeline Works

| Format | Pros | Cons |
|--------|------|------|
| **Paragraph narrative** | Emotional, personal | Hard to scan on mobile, takes up space |
| **Resume/credential list** | Scannable, trust signals | Feels corporate, no story |
| **Timeline** | Scannable AND tells a story, shows momentum | Can feel impersonal if too terse |
| **Cards/chapters** | Visual, modular | Takes too much vertical space |

The timeline wins because it's scannable on mobile (critical for Farcaster mini app at 424px), shows the journey arc, and demonstrates momentum — every year has real output.

### Design Specs (Matching Existing Aesthetic)

- **Position:** After the current about paragraph, before the path cards
- **Layout:** Year on the left (Syne 700, `--orange`), description on the right (Outfit 400, `--text-muted`)
- **Separator:** Thin vertical line (`--border`) connecting the milestones
- **Mobile:** Stack year above description, line on the left edge
- **Animation:** Each milestone fades in with `.fade-in` + stagger classes (already in CSS)
- **Accent:** Key numbers in `--cyan` or `--gold` to pop against `--text-muted`

### What to Add to the About Paragraph

Expand the current 2-sentence about text to include the WHY:

**Current:**
> "I'm Zaal. Engineer turned web3 builder, based in Maine. I built The ZAO..."

**Proposed:**
> "I'm Zaal. Electrical engineer turned web3 builder, based in Maine. I entered crypto during the bear market — the people still building were serious. That's when I saw the real problem: artists create all the value but own none of the infrastructure. Labels take 80-85% of revenue. Platforms own the audience. When they change the algorithm, artists lose everything. The tools to fix this exist — blockchain enables transparent splits, portable identity, and provable ownership. The ZAO exists to close that gap."

Then the timeline. Then the path cards.

### Optional: A Single Stat Row Above the Timeline

Three numbers, horizontally, in large type:

```
400+          90+           $50K+
newsletters   governance    on-chain
              meetings      volume
```

Compact, punchy, establishes scale before the story unfolds.

---

## Implementation Notes

- All changes stay in `index.html` — no new files needed
- Timeline CSS can use flexbox or grid with the existing design variables
- Mobile breakpoint at 600px: stack year above description
- Keep total timeline to 5-7 milestones maximum — more feels like a resume
- The stat row is optional but high-impact for Farcaster mini app visitors who scroll fast
- The expanded about paragraph should stay under 4 lines on mobile

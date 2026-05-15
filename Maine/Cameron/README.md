# Cameron / Riverside Group - Project README

> **For future Claude sessions:** if Zaal says "read the readme," start here. This file is the canonical project status, the file layout, and the workflow. Update it as work ships.

**Last updated:** 2026-05-15
**Active wave:** Wave 0 done, Wave 1 in flight (piece 14 v0 shipped, 15 + 16 + 4 next)

---

## What this is

Personal-time consulting engagement for **Cameron DePaola** at **Riverside Group** (riversidegroupme.com), a Maine landscape design-build + light GC outfit based on Mount Desert Island. Zaal is building a 16-piece operating system for Riverside on his own time (JAX day-job continues), logging hours, and presenting each piece as built. Cameron pays only for what he decides stays.

**Client:** Cameron DePaola, (207) 951-2525, cameron@riversidegroupme.com
**Right-hand:** Josh (books)
**Geography:** MDI / Bar Harbor / Ellsworth area
**Status:** Cameron verbally confirmed engagement. Zaal building on own time. Role conversation deferred 60-90 days.

---

## The arrangement (one sentence each)

- **Zaal builds on his time.** Evenings + weekends. JAX day-job continues. No overlap.
- **Hours logged per piece.** Google Sheet (and local CSV), Cameron has view access.
- **Cameron pays only for what stays.** $40/hr, monthly invoice, only for pieces flagged "kept."
- **Weekly 15-min check-in.** Zaal shares what shipped + what's next. Cameron flags what's not working.
- **Role conversation is deferred.** No W-2 commitment up front. After 60-90 days both parties decide.

This is documented client-facing on the zaal page (`riverside-site/zaal/index.html`).

---

## The 16-piece system

The full system Zaal is building. First 9 are from Cameron's original SMS list, in his order. 10-13 are infrastructure Zaal added. 14-16 came out of follow-up.

| # | Piece | Why |
|---|---|---|
| 1 | Tool & inventory tracking | High-value gear walks off. QR + AirTag system |
| 2 | Daily log + shared updates | 6pm digest, what got done where |
| 3 | Website refresh | Already mostly built (see `riverside-site/`) |
| 4 | New logo + merch pack | Blocks shirts / hats / signs reprint |
| 5 | Client intake + work orders | Lead board, win to budget to PO |
| 6 | Advertising - clients & hiring | Acquisition + funnel |
| 7 | Equipment maintenance schedules | Hour-meter-based PM |
| 8 | Budgets, POs, profit per job | Margin visibility per job |
| 9 | Business phone + call routing | Cameron's voicemail is broken today |
| 10 | Insurance, COIs, compliance | Workers comp, HIC reg, certs |
| 11 | Books + financial integration | QBO export respect Josh's flow |
| 12 | Client communication + updates | Weekly photo updates per active job |
| 13 | Document & contract library | Per-job library, searchable |
| 14 | Materials cost sheet + estimating | (v0 shipped) Known unit costs per supplier |
| 15 | Facebook business page | Manager invite + merge duplicate page |
| 16 | Ad creative system | Template + real photos, no AI-slop |

Full breakdown lives in `riverside-site/zaal/index.html` (Cameron-facing) and in the build order below.

---

## Build order (waves) — how it actually ships

Cameron's mental order = 1-16. Actual build order = cheap visible wins first.

| Wave | Items | Time est | Cameron pays (if all kept) |
|---|---|---|---|
| 0 - Trust layer | Hours log + weekly check-in | 1 hr | $40 |
| 1 - Quick wins | Materials sheet (14), FB (15), Ad template (16), Logo (4) | 20-25 hrs | $800-$1,000 |
| 2 - Website live | Real photos + DNS swap (3) | 4-6 hrs | $160-$240 |
| 3 - Field pilot | Daily log + photo doc (2 + 12) on one job | 3-5 hrs | $120-$200 |
| 4 - Operations spine | Work orders + budgets + PO tracking (5 + 8) | 8-12 hrs | $320-$480 |
| 5 - Field infrastructure | Tool tracking (1) + equipment PM (7) | 6-8 hrs | $240-$320 |
| 6 - Boring layer | Compliance (10) + books (11) + phone (9) | 4-6 hrs | $160-$240 |
| 7 - Polish + growth | Documents (13) + ads (6) + client comms (12) | Ongoing | TBD |

Total Wave 0-5 = ~45-60 hrs = $1,800-$2,400 if Cameron keeps everything.

**Tool-agnostic Sheets-first.** Every piece ships as a Google Sheet / Doc first. Paid tools (Jobber, CompanyCam, Fleetio, toolQR) are evaluated only after Cameron sees the Sheet version work. Saves him money, keeps options open.

---

## What's shipped

| Wave | Piece | Status | Artifact |
|---|---|---|---|
| - (strategic doc) | The zaal page | live | `riverside-site/zaal/index.html` - 16 pieces, wave order, "build first" framing |
| - (strategic doc) | Research doc 456 | done | `research/456-riverside-pm-system-research.md` - 14 sources, STANDARD tier, industry PM tool landscape + Maine compliance |
| 0 | Hours log v0 | shipped, awaiting Cameron view-share | `deliverables/wave-0-hours-log/` - CSV template + README + summary formulas + empty running log |
| 1 | Materials cost sheet v0 | shipped, needs Cameron-verified prices | `deliverables/wave-1-materials-sheet/` - 30 SKUs across 9 categories with Maine pricing placeholders |
| - (tooling) | `/start` + `/end` skills | registered | `~/.claude/skills/start/` and `~/.claude/skills/end/` |

---

## What's next (in order)

1. **Manual sync step (Zaal):** Create the Google Sheet for the hours log, share view-access with Cameron via text. See `deliverables/wave-0-hours-log/README.md`.
2. **Wave 1, piece 14 v1:** Cameron-verified prices + actual supplier names. Needs conversation with Cameron: which loam yard, stone yard, nursery, hardscape supplier.
3. **Wave 1, piece 15:** Accept Cameron's Facebook manager invite. Audit both pages. Build merge plan + execute.
4. **Wave 1, piece 16:** Get 1-2 before/after photo sets from Cameron. Build ad template v0 in Figma. Output FB feed + IG square + print 4x6 sizes.
5. **Wave 1, piece 4:** Logo - 3 directions for Cameron to pick from.
6. **Wave 2, piece 3:** Real-photo swap on the riverside-site + DNS swap when Cameron says go.

---

## File layout

```
Maine/Cameron/
  README.md                                   <- you are here
  cameron-riverside-context.md                <- original SMS thread, initial context
  455-research.md                             <- symlink to /Maine/Hotels/ - prior research (Stephen Coston + Cameron profile)
  research/
    456-riverside-pm-system-research.md       <- STANDARD-tier doc, PM tool landscape, Maine compliance, materials markup framework
  deliverables/
    wave-0-hours-log/
      README.md                               <- setup steps, status workflow, invoice math
      SUMMARY-FORMULAS.md                     <- copy-paste formulas for Summary tab
      hours-log-template.csv                  <- template w/ sample rows for first import
      hours-log.csv                           <- running log (appended by /end skill)
    wave-1-materials-sheet/
      README.md                               <- how to use, what's filled vs TBD, questions for Cameron
      materials-cost-sheet-v0.csv             <- 30 SKUs starter catalog
  riverside-site/                             <- embedded git repo, separate push target
    zaal/index.html                           <- THE strategic doc Cameron reads, riversidegroupme.com/zaal
    index.html                                <- demo home page
    capabilities.html                         <- capabilities deep-dive
    journal/                                  <- journal posts (designing-for-maine-winters etc)
    portfolio/                                <- portfolio
```

**Two repos in play:**
- **BCZ main** (`bettercallzaal/bettercallzaalwebsite`) - everything outside `riverside-site/`. Includes research + deliverables + this README.
- **riverside-site** (`bettercallzaal/riverside-group-demo`) - the demo site itself. Current branch: `ws/capabilities-deep-dive`. Remote alias: `archive`. NOT `origin` (origin points to a dead `test2.git`).

---

## The `/start` and `/end` workflow

Two slash-command skills registered at `~/.claude/skills/`. Logs hours automatically and drafts a Cameron update message.

### Starting a session

```
/start 14 fill in Cameron-verified prices from his last 3 invoices
```

- Argument 1: piece number (1-16, or `-` for cross-cutting work)
- Argument 2+: short description of what you're about to work on

The skill records start time + piece info to `~/.claude/state/active-hours-session.json` and confirms.

### Ending a session

```
/end
```

The skill:
1. Reads start time from state file
2. Calculates duration (rounded to nearest 0.25 hr)
3. Asks: what shipped (one sentence) + artifact link + status (in-progress / demo-ready / kept / waved-off)
4. Appends row to `deliverables/wave-0-hours-log/hours-log.csv`
5. Drafts a natural Cameron update message
6. Copies it to the macOS clipboard via pbcopy
7. Clears the state file

Then Zaal pastes the message into a text to Cameron and pastes the new CSV row into the shared Google Sheet.

### Status values

- **planned** - in the system but not started
- **in-progress** - work has begun, more sessions needed
- **demo-ready** - artifact ready for Cameron to look at
- **kept** - Cameron has approved; rolls into monthly invoice
- **waved-off** - Cameron passed; Zaal eats the hours

---

## Quick-resume guide for future Claude sessions

When Zaal opens a fresh session and says "we're working on Cameron / Riverside":

1. **Read this README first** (you're here)
2. **Check the shipped table above** - what's the latest state
3. **Check `research/456-riverside-pm-system-research.md`** if the question is about tooling, materials pricing, or industry norms
4. **Check the zaal page** (`riverside-site/zaal/index.html`) - that's the Cameron-facing source of truth for what was promised
5. **Check `deliverables/wave-0-hours-log/hours-log.csv`** to see what's been logged recently
6. **For new research:** save into `research/` as `<next-number>-<topic-slug>.md` following the doc 456 format
7. **For new deliverables:** create a `deliverables/wave-<N>-<piece-slug>/` folder w/ a README

If something has changed structurally (new wave, new piece beyond 16, framing shift), update THIS README.

---

## Communication with Cameron

- **Channel:** SMS (207) 951-2525. Casual, lowercase, real sentences.
- **Cadence:** 15-min weekly check-in (text fine, call better). Plus async updates after each session via `/end`-generated message.
- **Tone:** no greetings, no signoffs, no bot phrases. Match his voice. Examples in `~/.claude/skills/end/SKILL.md`.
- **Photos:** Cameron is on Facebook for business presence (page invite already sent). Ask him to text photo sets when needed.

---

## Open questions for Cameron (running list)

When Zaal gets the next conversation:

1. Top suppliers - which loam yard, stone yard, nursery, hardscape source?
2. Does Josh use QBO? Wave? Other?
3. Has the FB manager invite been re-sent? (Zaal needs to accept)
4. Confirm crew size + truck count (for tool-tracking + equipment-PM scaling)
5. Confirm sub-$1M revenue ballpark (informs Jobber vs LMN recommendation)
6. Any preference on logo direction (modern minimal vs heritage vs etc)?
7. When does he want the website DNS swap to happen?

---

## Related context

- **Doc 455** (`Maine/Hotels/` via symlink) - prior research covering Stephen Coston (hotels) + initial Cameron profile, ZAO Stock context
- **MELNA** (Maine Landscape & Nursery Association) - voluntary cert worth considering for Cameron's MDI luxury-estate marketing
- **Maine compliance basics** - HIC registration required for residential >$3K, workers comp Title 39-A at 1+ employee, no state landscape contractor license

---

## How to update this README

After shipping anything that changes:
- Wave / piece status -> update the "What's shipped" + "What's next" tables
- New file -> add to file layout
- New workflow -> add a section
- New research -> add to "Related context"
- New question for Cameron -> add to open questions

Keep it terse. This is a working doc, not a deliverable.

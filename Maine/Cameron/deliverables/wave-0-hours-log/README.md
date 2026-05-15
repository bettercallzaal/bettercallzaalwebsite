# Wave 0 - Hours Log v0

The trust layer. Built first, before any deliverable. Shared with Cameron view-access. Cameron can open it anytime and see exactly what hours have been logged against what shipped artifact.

## What this is

A Google Sheet where every hour Zaal spends on Riverside is logged against:
- A specific piece (1-16 from the zaal page)
- A wave (0-7 from the build sequence)
- A concrete artifact (link to the file, sheet, design, page)
- A status (planned, in-progress, demo-ready, kept, waved-off)
- An optional Cameron-side note

This file is the source of truth for the monthly invoice. No surprises.

## Setup steps (Zaal does this)

1. Create new Google Sheet titled: **Riverside Hours Log - Zaal**
2. Import `hours-log-template.csv` (File > Import > Upload, replace current sheet)
3. Freeze row 1 (View > Freeze > 1 row)
4. Add data validation on the **Status** column (Data > Data validation):
   - List of items: `planned, in-progress, demo-ready, kept, waved-off`
5. Add the **Summary** tab (see SUMMARY-FORMULAS.md in this folder)
6. Share with Cameron: View access, link share on. Send Cameron the link via text.

## Column schema

| Column | Type | Purpose |
|---|---|---|
| Date | YYYY-MM-DD | When the work happened. Not when logged. |
| Wave | 0-7 | Build sequence wave. 0 = trust layer, 1 = quick wins, etc. |
| Piece # | 1-16 or "-" | Which piece in the 16-piece map. Use "-" for cross-cutting work (like this setup). |
| Piece Name | text | Human-readable name of the piece. Match the zaal page. |
| Hours | decimal | Quarter-hour granularity (0.25, 0.5, 0.75, 1.0...). |
| What Shipped | text | Concrete sentence: what artifact / output produced this session. |
| Artifact Link | URL | Direct link to the sheet / file / page / Figma / GitHub. |
| Status | enum | planned / in-progress / demo-ready / kept / waved-off |
| Cameron Note | text | Cameron writes here when he reviews. Can be blank. |

## Status workflow

- **planned** - Zaal has identified the piece but not started.
- **in-progress** - Zaal has started building. Hours accumulating.
- **demo-ready** - Zaal has something to show Cameron. Trigger for a check-in.
- **kept** - Cameron has reviewed and decided it stays. Hours roll into invoice.
- **waved-off** - Cameron does not want this piece. Hours zero out for invoice. Zaal keeps the artifact.

## Invoice math (in Summary tab)

Monthly invoice = SUM of Hours where Status = "kept" * $40

Anything still "in-progress" or "demo-ready" does NOT count yet. Cameron only ever pays for things that have crossed the "kept" line.

## Cadence

- **Zaal:** Logs hours same-day or next-day. Never bulk-logs a week later. Trust depends on the log being honest, not pretty.
- **Cameron:** Reviews weekly during 15-min check-in. Updates Status column on anything demo-ready.
- **Invoice:** Generated 1st of each month from "kept" rows of the prior month. PDF emailed to Cameron + Josh.

## What this is not

- Not a project management tool. The zaal page lives at riversidegroupme.com/zaal as the strategic doc.
- Not a comprehensive deliverable - just the hours record.
- Not editable by Cameron (view-only) except the Cameron Note column.

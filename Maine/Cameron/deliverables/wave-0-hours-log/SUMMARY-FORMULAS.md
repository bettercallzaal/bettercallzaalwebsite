# Summary Tab Formulas

Add a second tab to the Google Sheet called **Summary**. Paste these formulas into the cells indicated.

## Layout

```
A1: Riverside Hours Log - Summary

A3: This Month
B3: =DATE(YEAR(TODAY()), MONTH(TODAY()), 1)

A4: Total hours logged
B4: =SUMIFS('Hours Log'!E:E, 'Hours Log'!A:A, ">="&B3, 'Hours Log'!A:A, "<="&EOMONTH(B3, 0))

A5: Hours kept (billable this month)
B5: =SUMIFS('Hours Log'!E:E, 'Hours Log'!A:A, ">="&B3, 'Hours Log'!A:A, "<="&EOMONTH(B3, 0), 'Hours Log'!H:H, "kept")

A6: Hours waved off
B6: =SUMIFS('Hours Log'!E:E, 'Hours Log'!A:A, ">="&B3, 'Hours Log'!A:A, "<="&EOMONTH(B3, 0), 'Hours Log'!H:H, "waved-off")

A7: Hours in-flight (not yet decided)
B7: =SUMIFS('Hours Log'!E:E, 'Hours Log'!A:A, ">="&B3, 'Hours Log'!A:A, "<="&EOMONTH(B3, 0), 'Hours Log'!H:H, "in-progress") + SUMIFS('Hours Log'!E:E, 'Hours Log'!A:A, ">="&B3, 'Hours Log'!A:A, "<="&EOMONTH(B3, 0), 'Hours Log'!H:H, "demo-ready")

A9: This month invoice (kept hours x $40)
B9: =B5*40

A11: Lifetime
A12: Total hours kept
B12: =COUNTIF('Hours Log'!H:H, "kept") * AVERAGE(IF('Hours Log'!H:H="kept", 'Hours Log'!E:E))
A13: Lifetime billed
B13: =SUMIF('Hours Log'!H:H, "kept", 'Hours Log'!E:E)*40
```

## By Wave breakdown

```
A15: Hours by Wave
A16: Wave 0   B16: =SUMIF('Hours Log'!B:B, 0, 'Hours Log'!E:E)
A17: Wave 1   B17: =SUMIF('Hours Log'!B:B, 1, 'Hours Log'!E:E)
A18: Wave 2   B18: =SUMIF('Hours Log'!B:B, 2, 'Hours Log'!E:E)
A19: Wave 3   B19: =SUMIF('Hours Log'!B:B, 3, 'Hours Log'!E:E)
A20: Wave 4   B20: =SUMIF('Hours Log'!B:B, 4, 'Hours Log'!E:E)
A21: Wave 5   B21: =SUMIF('Hours Log'!B:B, 5, 'Hours Log'!E:E)
A22: Wave 6   B22: =SUMIF('Hours Log'!B:B, 6, 'Hours Log'!E:E)
A23: Wave 7   B23: =SUMIF('Hours Log'!B:B, 7, 'Hours Log'!E:E)
```

## Pieces ready for review

A filter view that surfaces anything Cameron needs to look at:

1. Data > Filter views > Create new filter view
2. Name it: "Pieces ready for review"
3. Filter Status column to show only: `demo-ready`
4. Save. Anyone with access can switch to this view to see what is waiting on Cameron.

## Conditional formatting (optional)

To make Status column visually clear:

1. Highlight column H (Status)
2. Format > Conditional formatting
3. Add rules:
   - `kept` -> green background
   - `waved-off` -> red background
   - `demo-ready` -> orange background
   - `in-progress` -> yellow background
   - `planned` -> gray background

Makes the log scannable at a glance.

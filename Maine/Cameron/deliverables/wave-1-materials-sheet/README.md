# Wave 1 - Materials Cost Sheet v0

30-SKU starter sheet for Riverside Group. Tool-agnostic (Google Sheets). Designed so every estimate line item has a known unit cost x quantity = floor price.

## What this is

A starter materials catalog covering the categories Riverside touches most: lumber, drywall, soil, mulch, stone, hardscape, plants, edging, hardware. Each row has:

- Category
- Item description
- SKU / note
- Unit (each / cubic yard / lin ft / etc)
- Supplier (primary + fallback)
- Cost per unit (Cameron-verified)
- Markup % (by category, per industry norms)
- Customer price (auto-calc)
- Last verified date
- Notes

## What is filled in vs what needs Cameron's input

**Filled in (from research doc 456):**
- All 30 SKUs with category + item + unit
- Realistic cost estimates pulled from GreenMargins 2025 published reference + Maine market intuition
- Markup % per category (15% commodities, 20-25% hardscape, 30-35% plants per industry norm)
- Auto-calculated customer prices

**Needs Cameron's input (marked TBD):**
- Actual supplier names for stone yard, loam yard, hardscape supplier, nursery
- Actual verified prices (the cost column today is a placeholder - Cameron should confirm against his last 3 invoices)
- Last-verified dates (currently "TBD-call-supplier")

## How to use it

### As a Google Sheet (recommended)

1. Create a new Google Sheet titled: **Riverside Materials Cost Sheet**
2. Import `materials-cost-sheet-v0.csv` (File > Import > Upload, replace current sheet)
3. Freeze row 1 (View > Freeze > 1 row)
4. Add conditional formatting:
   - "Last Verified" column - any cell older than 90 days highlighted yellow
   - "Cost (unit)" column - if empty, highlighted orange (needs supplier confirmation)
5. Add a formula column "Customer Price" check: `=I2*((100+H2)/100)*F2 = G2` to verify markup math
6. Share with Cameron: edit access (he'll be adjusting prices)

### Quick-quote sheet (later)

Once Cameron confirms his actual prices, the sheet feeds a separate "Quote builder" tab where Zaal types:

```
| Item              | Qty  | Unit Price | Subtotal |
| Loam              | 20   | $43.70     | $874.00  |
| Hardwood mulch    | 12   | $44.84     | $538.08  |
| ...               |      |            |          |
|                                       | Materials | $X,XXX |
|                                       | Labor     | $Y,YYY |
|                                       | TOTAL     | $Z,ZZZ |
```

Quote builder pulls live from the materials sheet. Price changes propagate automatically.

## Markup framework applied (from research doc 456)

| Category | Markup | Why |
|---|---|---|
| Bulk commodities (mulch, soil, gravel, lumber) | 15-20% | Low handling, easy sourcing |
| Hardscape (pavers, wall block, polymeric sand) | 20-25% | Heavier handling, breakage risk |
| Edging, landscape fabric | 20-25% | Multi-trip handling |
| Plants / nursery stock | 30-35% | Perishable, warranty risk, transport care |
| Specialty hardware | 15% | Pass-through with light markup |

Cameron can override any per-line markup. The category default is just the starting point.

## Questions for Cameron (first conversation)

1. Which loam yard? (Currently TBD)
2. Which stone yard for crushed/pea/river rock + retaining wall block?
3. Which nursery for plants?
4. Which hardscape supplier for pavers? (Hammond carries some but probably not all)
5. Are the cost estimates in the right ballpark? (He should adjust at least the 5 highest-volume items based on his last 3 invoices)
6. Does he want a single markup % per item, OR a tiered markup based on order size?
7. Any specialty SKUs he uses every month that aren't in this 30? (irrigation parts, lighting, water features)

## Next iterations

- v1: Cameron-verified prices, supplier names locked in (after first conversation)
- v2: Add the quote-builder tab that consumes the sheet
- v3: Add "actual cost" column populated from CompanyCam photos of receipts (once that lands in Wave 3)
- v4: Migrate into Jobber's material catalog if Cameron picks Jobber in Wave 4

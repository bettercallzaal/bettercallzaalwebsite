---
topic: business
type: market-research
status: research-complete
last-validated: 2026-05-15
related-docs: 455
tier: STANDARD
---

# 456 — Riverside Group: PM System Research (landscape design-build + small GC in Maine)

> **Goal:** Inform the 16-piece operating system Zaal is building for Cameron / Riverside Group. Cover industry-standard PM tools, estimating norms, daily-log patterns, equipment maintenance, materials catalogs, Maine-specific compliance. STANDARD tier - 30 min, 14 sources.

---

## Key Decisions / Recommendations

| Decision | Recommendation |
|----------|----------------|
| Core ops platform for Riverside today | START with **Jobber Connect ($119-169/mo)** as the spine. Cameron's crew size (small, <15 people) hits Jobber's sweet spot. Skip LMN ($297/mo) until Riverside is >$1M revenue OR estimating becomes the bottleneck. Skip Aspire entirely - it's for $2M+ commercial only. |
| Materials cost sheet tool | BUILD as a Google Sheet first, NOT inside Jobber. Sheet is editable from any phone, no per-seat cost, no learning curve. Once stable, migrate to Jobber's material catalog or use GreenMargins ($39/mo) if margin math becomes the issue. |
| Daily log / photo capture | USE **CompanyCam ($20/mo per user)** day one. Best-in-class for landscape/construction photo documentation. Geo-tagged, AI daily-log generation, client-facing photo reports. Integrates with Jobber. |
| Tool tracking (item 1 of the 16) | USE QR labels (free to print) + **toolQR ($29/mo)** OR **GoCodes (free trial, then ~$50/mo)** for the under-500-tool case. Airtags for high-value items. Skip Remarcable / Aspire / enterprise. |
| Equipment maintenance (item 7) | USE **Fleetio Essentials (~$5/asset/mo)**. Hour-meter-based PM (250hr oil change on excavator, etc.). OEM template library exists for skid steers / excavators / dozers - saves setup time. |
| Estimating depth (items 5, 8, 14) | KEEP it in a Google Sheet linked to the materials cost sheet. Cameron does not need LMN-level burdened-labor math at his scale yet. If margins start hurting, add GreenMargins ($39/mo) which calculates burdened labor + travel + overhead without the LMN learning curve. |
| Maine compliance (item 10) | Riverside is subject to: HIC registration for residential work >$3,000 (MRSA Title 10), workers comp mandatory at 1+ employee (Title 39-A), general liability $100k+ per occurrence. NO state landscape contractor license required - voluntary MELNA cert only. |
| Client comms (item 12) | Buildertrend client portal is overkill at Cameron's stage. USE CompanyCam photo reports + email/text + weekly auto-summary script. Re-evaluate at 10+ active jobs. |
| Books integration (item 11) | Whatever Cameron / Josh use (likely QBO), Jobber + CompanyCam + Fleetio all export to QBO natively. No custom integration needed. |
| Build sequence to maximize visible wins | Materials sheet > Facebook page > Ad template > Logo > Website live > Tool tracking pilot > Daily-log pilot with CompanyCam > Estimate templates > Compliance vault. Cheap visible wins first. |

---

## Software Landscape (sized for Riverside)

Riverside's profile (from Doc 455): MDI-area landscape design-build + light GC, established Squarespace site, in-season scaling, owner (Cameron) + Josh on books + crew. Likely sub-$1M revenue, growing. Sweet spot for mid-tier field-service tools, NOT enterprise.

### Tier A: Field Service (operations spine)

| Tool | Starting Price | Best Fit | Why For Riverside |
|---|---|---|---|
| **Jobber Core** | $69/mo (1 user) | Solo / 2-truck | Too thin for Cameron + Josh + crew |
| **Jobber Connect** | $169/mo (5 users) | 2-15 employees | RECOMMENDED. Scheduling, quoting, client hub, QBO sync |
| **Jobber Grow** | $349/mo (15 users) | 10-30 employees | Adds route optimization - revisit at crew 8+ |
| **Service Autopilot** | $49-$200+/mo | Recurring maintenance heavy | NOT a fit - Riverside is project-based |
| **Housecall Pro** | $59/mo | General home services | Not landscape-specific enough |

### Tier B: Job Costing / Estimating (specialist)

| Tool | Starting Price | Best Fit | Why For Riverside |
|---|---|---|---|
| **LMN Starter** | $297/mo (1-3 crews) | $500k-$2M, estimating-heavy | OVERKILL today. Revisit at $1M+ revenue |
| **GreenMargins** | $39/mo | Burdened-labor margin math | RECOMMENDED if Cameron is bleeding margin and doesn't know why |
| **Buildxact** | $169/mo (1 user) | Design-build digital takeoffs | Possible add-on for big hardscape bids |
| **Aspire (ServiceTitan)** | $500-1000+/mo | $2M+ commercial multi-crew | SKIP - completely wrong scale |

### Tier C: Photo + Daily Log (jobsite layer)

| Tool | Starting Price | Best Fit | Why For Riverside |
|---|---|---|---|
| **CompanyCam** | $20/user/mo | Photo doc + daily logs + reports | RECOMMENDED. Geo-tagged photos, AI daily-log, client-facing reports |
| **Buildertrend** | $499/mo | Full design-build PM + client portal | Overkill at Cameron's stage |
| **TaskTag** | ~$20/user/mo | Lightweight jobsite tasks | Inferior to CompanyCam for landscape |

### Tier D: Equipment + Fleet

| Tool | Starting Price | Best Fit | Why For Riverside |
|---|---|---|---|
| **Fleetio Essentials** | ~$5/asset/mo | Hour-meter PM for trucks + heavy iron | RECOMMENDED. OEM templates for excavator / skid steer / dozer |
| **Fleetsmart** | $20/asset/mo | Heavy fleet with telematics | Overkill - Cameron probably has <10 assets |

### Tier E: Tool Tracking

| Tool | Starting Price | Best Fit | Why For Riverside |
|---|---|---|---|
| **toolQR** | $29/mo (100 tools) | Small fleet, simple checkout | RECOMMENDED for v0 |
| **GoCodes** | Free trial, ~$50/mo | Mid-size, includes tags | Strong second option |
| **MapTrack** | Custom | 3-5 active sites | Maybe later; case study showed 70% loss reduction |
| **Remarcable** | Enterprise | 400+ employees | Skip |

### Cost ladder Cameron actually pays (recommended stack)

| Month | Items live | Monthly cost |
|---|---|---|
| Today (Phase 1) | Google Sheets only (materials, hours log, supplier list) | $0 |
| Month 1-2 | + Facebook page management (free) + ad template (Figma free tier) | $0 |
| Month 2-3 | + CompanyCam (3 users) + Jobber Connect | ~$229/mo |
| Month 4-6 | + Fleetio (5-8 assets) + toolQR (100 tools) | ~$298/mo |
| Month 6-12 | (optional) GreenMargins for margin math | ~$337/mo |
| Year 2 if >$1M rev | (optional) Upgrade Jobber > LMN OR add LMN beside Jobber | $500-$600/mo |

Versus Aspire at $500-1000/mo + $5-15K implementation - the recommended stack is one-third the cost and right-sized for Cameron's revenue.

---

## Materials Cost Sheet (Item 14) - The Reference

Standard landscape materials with typical pricing and recommended markup (per GreenMargins published reference, 2025):

| Material | Unit | Typical Cost | Recommended Markup | Customer Price |
|---|---|---|---|---|
| Mulch (hardwood / dyed) | per yd | $30-$45 | 15-20% | $35-$54 |
| Gravel (crushed / pea) | per yd | $35-$75 | 15-25% | $40-$94 |
| Topsoil / fill | per yd | $25-$55 | 15-20% | $29-$66 |
| Concrete pavers | per sq ft | $3-$12 | 20-30% | $3.60-$15.60 |
| Retaining wall block | per block | $3-$8 | 20-30% | $3.60-$10.40 |
| Sod | per sq ft | $0.35-$0.85 | 25-40% | $0.44-$1.19 |
| Plants / shrubs (1-gal) | each | $8-$25 | 30-50% | $10.40-$37.50 |
| Trees (15-gal) | each | $50-$200 | 25-40% | $62.50-$280 |
| Edging (aluminum / steel) | per lin ft | $1.50-$4 | 20-30% | $1.80-$5.20 |
| Landscape fabric | per roll (300 ft) | $30-$80 | 15-25% | $35-$100 |

**Markup framework** (apply by category, NOT one flat number):

| Category | Markup Range | Why |
|---|---|---|
| Bulk commodities (mulch / soil / gravel) | 15-25% | Low handling, easy sourcing |
| Hardscape (pavers / wall block / flagstone) | 20-30% | Heavier handling, breakage risk |
| Plants / nursery stock | 30-50% | Perishable, warranty risk, transport care |
| Irrigation supplies | 20-35% | Many small parts, return trips |
| Specialty (lighting / water features) | 25-40% | Design time, sourcing |

**Coverage rates for quantity math:**
- 1 cubic yard of mulch covers ~160 sq ft at 2" deep
- Waste factor: 5-15% depending on material type
- Pickup-trip labor + supplier-visit time count toward burdened cost

### Maine Supplier Starter List (verified)

| Supplier | What | Notes |
|---|---|---|
| **Hammond Lumber Company** | Lumber, building materials, doors / windows | 22 locations across ME + NH, statewide delivery, free estimating + design, dedicated commercial sales reps. Established 4-gen family-owned. (hammondlumber.com) |
| **Hancock Lumber** | Lumber, white pine, wall panels, trusses, kitchens | 7-gen family-owned since 1848, manages 12,000+ acres of timberland, free delivery + curbside, online estimating + quoting. (hancocklumber.com) |
| Home Depot Brunswick | Hardware / fasteners / quick-need supplies | Default fallback when speed matters more than price |
| (TBD) Local stone yard | Hardscape / wall block / flagstone | NEED TO ASK CAMERON which yard he actually uses |
| (TBD) Local loam yard | Topsoil / fill / compost | NEED TO ASK CAMERON which yard he actually uses |
| (TBD) Local nursery | Plants / trees / shrubs | NEED TO ASK CAMERON - probably 1-2 named ones |

**Action:** First conversation with Cameron should fill in those TBDs. Then build sheet v0 with 30 SKUs drawn from his actual top-5 suppliers.

---

## Daily Log Pattern (Item 2)

CompanyCam's daily-log workflow is the industry pattern for landscape/construction:

1. Crew member takes photos throughout the day on their phone
2. Speaks voice notes (auto-transcribed to text) attached to each photo
3. End of day: pick at least 3 photos with notes, app's AI generates a clean daily report
4. Output: shareable link or PDF (with optional cover page) to crew + customer + Cameron + Josh

**Cameron's "6pm digest" can ride this:** CompanyCam generates the per-job entries, a small script aggregates them into one email at 6pm with totals (who logged, hours by job, missing entries flagged, anything tagged urgent).

**Cost:** $20/user/mo. For Cameron + Josh + 4 crew = ~$120/mo. Falls inside the "month 2-3" budget tier above.

---

## Equipment Maintenance Pattern (Item 7)

Fleetio's industry-standard PM schedule template for heavy equipment:

| Frequency | Tasks |
|---|---|
| Daily | Inspect fluid levels, tires, brakes, lights. Record engine hours. |
| Weekly | Inspect hydraulics, tracks, electrical systems. Check air filters. |
| Monthly | Oil changes, coolant checks, safety system tests. |
| Quarterly | Comprehensive inspection of engine, suspension, undercarriage. |
| Seasonal | Heating / cooling systems. Prep for extreme temperatures (critical in Maine). |

**Meter-based vs time-based:**
- Excavator: oil every 250 engine hours
- Skid steer: hydraulic filter every 500 hours
- Truck: oil every 5,000 miles or 6 months whichever first

Fleetio has pre-built templates for "Excavator Basic Maintenance", "Dozer Basic Maintenance", "Skid Steer Basic Maintenance" - one-click setup per asset. Connects to Caterpillar VisionLink + John Deere Operations Center for telematics if Cameron's machines have it.

Maine-specific: harsh winters - the seasonal cooling/heating prep and the spring-startup checklist are non-optional. Add a Maine-specific "freeze-up" + "thaw-out" PM cycle.

---

## Tool Tracking Pattern (Item 1)

QR code system specifics from real case studies:

- **MapTrack case study (mid-size Victorian construction firm, 2026):** 70% tool loss reduction in 6 months. Weekly site audits dropped from hours to 15 minutes.
- **Threshold for tagging:** Anything valued over $50 gets a QR. Below that, treat as consumable.
- **Process discipline:** 3-second scan on checkout. Compliance was higher than paper because faster, AND it protects crew (audit trail shows who had it).
- **Cost math:** Tool loss in a typical 10-person operation: $5-10k/year in replacement + $15-30k/year in wasted labor hunting for tools. toolQR @ $29-79/mo pays back in month 1.

For Riverside (likely <100 tools, 5-10 crew):
- toolQR Pro tier ($29/mo, up to 100 tools) - good v0
- Airtags for excavator buckets, generators, expensive saws (~$25 each one-time)
- Weekly "where's the gear" digest email (Cameron + Josh) ties back to item 1 in the 16-piece map

---

## Maine Compliance (Item 10)

Things Cameron is legally on the hook for:

| Requirement | Source | Trigger |
|---|---|---|
| **Workers comp insurance** | Title 39-A MRSA | Mandatory at 1+ employee. No exemption. |
| **General liability insurance** | Industry standard | $100k+ per occurrence minimum. Most clients require $1M+ before letting on property. |
| **Home Improvement Contractor (HIC) registration** | Title 10 MRSA | Any residential work over $3,000 - install patios, retaining walls, drainage, irrigation. Riverside is hitting this on most landscape installs. |
| **No state landscape contractor license** | Maine doesn't have one | Voluntary MELNA certifications only (MCL / MCN / MCSL) |
| **OSHA** | Federal OSHA, ME office in Augusta (E.S. Muskie Federal Building) | Standard workplace safety. Excavator operator cert if running heavy iron. |
| **1099 / sub-contractor tracking** | IRS + state | If any sub paid $600+ in a year. Need W-9 on file before first payment. |

The "Insurance, COIs, compliance" vault (item 10 in the 16-piece map) needs to hold:
- Workers comp policy + COI ready to send
- General liability policy + COI
- Auto + umbrella
- HIC registration confirmation
- Subcontractor W-9s + 1099 records
- Equipment operator certifications
- Light incident-log template (in case OSHA ever asks)

MELNA membership is optional but worth $300-500/yr if Cameron wants the "Maine Certified Landscape Professional" credential on marketing materials - it differentiates him on MDI luxury-estate work.

---

## Community Signal (Reddit + forums)

LawnSite forum + Reddit threads consistently say:

- **"LMN learning curve is brutal - 3-4 months training before crew uses it right"** - common complaint, kills it for smaller shops.
- **"Aspire is great if you can afford it, kills you if you can't"** - $5-15K implementation + $500+/mo recurring is the friction.
- **"Jobber is the right starting point unless you specifically need job costing"** - small-shop consensus.
- **"CompanyCam is the one tool everyone keeps regardless of what else they use"** - photo doc has near-universal adoption.

**One contradiction noted:** Buildertrend reviews are split - some love it as "exactly what construction needs," others (the Knowify comparison thread on TrustRadius) say "client adoption was less than half" - the client-portal value depends entirely on whether your clients actually log in.

For Cameron's residential luxury-estate clients (MDI / Bar Harbor), photo reports via CompanyCam land better than asking clients to log into a portal. Confirms recommendation: skip Buildertrend portal, lean on CompanyCam reports + email.

---

## Implications for the 16-Piece Build Order

Recalibrated build order with what I learned:

| Order | Item | Why first / later | Tool / format |
|---|---|---|---|
| 1 | Materials cost sheet (14) | Cheap, instantly useful, zero software cost, unlocks accurate estimates | Google Sheet |
| 2 | Facebook page audit + merge (15) | One-evening task, unblocks social presence | Direct in FB |
| 3 | Ad template v0 (16) | One designed template + 3 real ads = visible win | Figma / Canva |
| 4 | Logo direction (4) | Already in Phase 1, drives merch + brand strip on ad template | Figma |
| 5 | Website launch (3) | Already mostly built (this site!) - real photos + DNS swap | Existing HTML |
| 6 | Hours log + weekly check-in flow | The trust layer - has to be live before bigger tools land | Google Sheet + 15-min weekly call |
| 7 | CompanyCam pilot (2 + 12) | One job, one week. Crew sees the photo magic | CompanyCam free trial |
| 8 | Jobber spinup (5 + 8) | Lead board + work orders + budgets - the operations spine | Jobber Connect |
| 9 | Materials sheet > Jobber catalog integration | Once sheet stable, push into Jobber items | Jobber + sheet bridge |
| 10 | Tool tracking pilot (1) | One truck, one week | toolQR + QR labels |
| 11 | Fleetio for equipment (7) | Hour-meter PM for the iron | Fleetio Essentials |
| 12 | Compliance vault (10) | Insurance vault + COI templates | Google Drive folders + email template |
| 13 | Books integration (11) | QBO export from Jobber + CompanyCam | Native integrations |
| 14 | Equipment + tool digests (1 + 7) | Weekly summary email | Light script / Zapier |
| 15 | Client portal eval (12) | Maybe, maybe not - depends on client behavior | Decide later |
| 16 | Document library (13) | Last - relies on all the above to feed it | Google Drive structure + naming |
| 17 (bonus) | Business phone (9) | Independent track - swap when Cameron's ready | Google Voice / OpenPhone |

Wrong order vs the 16-piece map on the zaal page (which goes by Cameron's text). The zaal page sells the system; the build order ships value. Both right.

---

## Also See

- [Doc 455](../455-research.md) - Original Stephen Coston + Cameron profile, hospitality + landscape lead context

## Next Actions

| Action | Owner | Type | By When |
|--------|-------|------|---------|
| Confirm Cameron's top-5 suppliers (stone yard, loam yard, nursery, plus Hammond/Hancock) | @Zaal | Conversation | Next text exchange |
| Build materials cost sheet v0 with 30 starter SKUs | @Zaal | Google Sheet | Week 1 |
| Accept Facebook manager invite + audit both pages | @Zaal | FB | Week 1 |
| Design ad template v0 in Figma | @Zaal | Figma | Week 2 |
| Set up hours-log sheet shared with Cameron | @Zaal | Google Sheet | Day 1 |
| Re-confirm with Cameron: does he want the Jobber/CompanyCam stack proposed, or is Aspire/LMN on the table? | @Zaal | Conversation | After he sees first 3 ships |
| Update zaal page with "build sequence" section reflecting this research | @Zaal | HTML edit | After plan synth |

## Sources

- [Top Landscaping PM Tools 2026 - TaskTag](https://portal.tasktag.com/blog/landscaping-project-management-software-2026)
- [Landscaping Software 5 Options Reviewed - Contractor Software Hub](https://www.contractorsoftwarehub.com/best-landscaping-software-small-business/)
- [Landscape Business Software 9 Best Options - BuildFolio](https://build-folio.com/resources/landscape-business-software/)
- [Best Landscaping Business Software - The AI Trades](https://theaitrades.ai/blog/landscaping-business-software)
- [LMN vs Jobber vs Aspire - Hero365](https://hero365.ai/blog/lmn-vs-jobber-vs-aspire-which-landscaping-software-actually-fits-your-business)
- [18 Best Tools for Landscapers - Agiled](https://agiled.app/blog/best-tools-for-landscapers)
- [Material Catalog - Elevation Advisor](https://elevationadvisor.com/material-catalog)
- [Landscape Estimating Software - GreenMargins](https://greenmargins.com/landscape-estimating-software)
- [Landscape Material Calculator + Markup - GreenMargins](https://greenmargins.com/blog/how-landscapers-track-materials-cost)
- [Houzz Pro Landscape Estimating Software](https://www.gardenweb.com/for-pros/software-landscape-contractor-estimating)
- [CountBricks Landscaping Takeoff](https://www.countbricks.com/features/landscaping)
- [Buildxact Landscape Estimating](https://www.buildxact.com/us/landscape-estimating-software/)
- [CompanyCam Landscaping App](https://companycam.com/landscaping-app)
- [CompanyCam Daily Log Workflow](https://companycam.com/resources/classes/how-to-create-a-daily-log)
- [Fleetio Construction Equipment Management](https://www.fleetio.com/solutions/construction-equipment-management)
- [Fleetio Heavy Equipment PM Schedule Guide](https://www.fleetio.com/blog/heavy-equipment-maintenance-schedules-and-procedures)
- [Fleetio Service Programs Overview](https://help.fleetio.com/maintenance/service-programs-overview)
- [Knowify Construction PM Software](https://knowify.com/construction-project-management-software)
- [Buildertrend Daily Logs](https://buildertrend.com/project-management/daily-logs/)
- [Buildertrend vs Knowify - TrustRadius](https://www.trustradius.com/compare-products/buildertrend-vs-knowify)
- [QR Code Tool Tracking for Contractors - Remarcable](https://www.remarcable.com/blog/qr-codes-tool-tracking-for-contractors)
- [Construction Firm Reduces Tool Loss 70% - MapTrack](https://www.maptrack.com/resources/how-a-construction-firm-reduced-tool-loss-by-70)
- [GoCodes Tool Tracking](https://gocodes.com/solution/tool-tracking/)
- [toolQR](https://trytoolqr.com/)
- [Hammond Lumber Company](https://www.hammondlumber.com/)
- [Hancock Lumber](https://www.hancocklumber.com/)
- [MELNA Maine Landscape & Nursery Association](https://www.melna.org/)
- [Maine OSHA Area Office](https://www.osha.gov/contactus/bystate/ME/areaoffice)
- [Aspire Thoughts - LawnSite Forum](https://www.lawnsite.com/threads/aspire-thoughts.502607/)
- [LMN vs Jobber vs SA vs Aspire - Ready Business Systems](https://readybusinesssystems.com/lmn-vs-jobber-vs-service-autopilot-vs-aspire)

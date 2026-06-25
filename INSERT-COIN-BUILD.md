# INSERT COIN — build handoff

Hand this whole file to a fresh Claude Code session in the `bettercallzaalwebsite` repo.
It contains everything needed to take the `/photos` "Insert Coin" daily photo drop from
**front-end shell → fully working paid mechanic**. No prior conversation context required.

---

## 0. TL;DR for the implementing agent

The visible page already exists and works as a shell. Your job is the money/state engine:
let a user spend ~$1 of **$ZABAL** on **Base**, pull **one random unclaimed photo** from
the day's batch, decrement supply atomically, and prove the randomness was fair.

The page is pure static HTML on Vercel (no build step for the site). You will add:
1. A few **Vercel serverless functions** under `/api` (these deploy automatically, no site build).
2. A **Supabase** (Postgres) project for batch + claim state.
3. Minimal **wallet + payment** wiring in `photos/index.html` using ESM-CDN libs (no bundler).

Ship **claim-only** first (no NFT). NFT minting is Phase 2 and is optional.

---

## 1. What already exists (do not rebuild)

- `photos/index.html` — the arcade "INSERT COIN" page. Renders client-side from a drop JSON.
  Has a status bar (`X of N left`, price), a mystery-tile grid, a reveal modal, and an
  `#insertCoin` button whose click handler is the **integration point** (currently it just
  opens a "coming soon" modal). Tiles render `status: 'available'` as a `?` and
  `status: 'claimed'` as `item.image` + `item.puller`.
- `photos/drop.json` — the data shape the front-end expects. Today it is a static file.
  **You will switch the page to fetch `/api/drop` instead** (same shape) so supply is live.

Current `drop.json` shape (this is the contract the front-end already speaks):
```json
{
  "date": "2026-06-25",
  "title": "Drop 001",
  "priceZabal": 100,
  "priceUsd": "~$1",
  "token": "$ZABAL",
  "chain": "Base",
  "live": false,
  "items": [
    { "id": "d001-01", "status": "available" },
    { "id": "d001-02", "status": "claimed", "image": "/assets/photos/d001-02.jpg", "puller": "@someone" }
  ]
}
```

---

## 2. Decisions (defaults chosen — change if the owner says otherwise)

| # | Decision | Default for v1 | Notes |
|---|----------|----------------|-------|
| 1 | Photos | Owner uploads a batch per drop (mix, his call) | Stored in `assets/photos/<dropId>/<itemId>.jpg`. Owner-cleared rights. |
| 2 | Delivery | **Claim-only** (no NFT) | Buyer gets the full-res image + an on-record claim. NFT = Phase 2. |
| 3 | Price | **Fixed `priceZabal` per drop** (set in the batch), labeled "~$1" | Avoids a live oracle. Re-tune per drop. Optional price-feed later. |
| 4 | $ZABAL destination | **Treasury wallet** (env `TREASURY_ADDRESS`) | Keep a `split` config stub for future burn / artist cut. |
| 5 | Backend | **Vercel serverless `/api` + Supabase** | Simplest, matches stack. Base-contract alternative in §9. |
| 6 | Randomness | **Commit–reveal** (off-chain, verifiable) | See §6. On-chain VRF optional later. |
| 7 | Per-wallet cap | **3 pulls per wallet per drop** (env `MAX_PER_WALLET`) | Anti-hoard. Tune freely. |

---

## 3. Key facts / constants

- **Token:** $ZABAL, ERC-20 on **Base mainnet**. Address `0xbB48f19B0494Ff7C1fE5Dc2032aeEE14312f0b07`.
  **VERIFY on Basescan before coding**: confirm the address and read `decimals()` (do NOT assume 18).
- **Chain:** Base (chainId 8453). Test on **Base Sepolia** (chainId 84532) first.
- **Brand voice (applies to any user-facing copy you add):** no emojis, no em dashes.
  "Insert coin" is the sanctioned phrase. Headings Syne; body Outfit; pixel font
  (Press Start 2P) only for the "INSERT COIN" moments.
- **Site deploy:** Vercel, static. `vercel.json` currently only has redirects. Adding `/api/*`
  gives serverless functions with no site build. You WILL add a root `package.json` with deps
  (Vercel installs them for the functions).

---

## 4. Architecture

```
Browser (photos/index.html, static)
  | 1. GET /api/drop?date=today        -> current batch + live supply (no secrets)
  | 2. user clicks INSERT COIN
  | 3. wallet sends ERC-20 transfer: priceZabal $ZABAL  from user -> TREASURY  (on Base)
  |    -> returns txHash
  | 4. POST /api/pull { date, wallet, txHash }
  v
Vercel serverless (/api, Node)
  - verify txHash on Base via viem: success, correct token, to=TREASURY, value>=priceZabal,
    from=wallet, >=1 confirmation, txHash never used before
  - enforce per-wallet cap
  - ATOMICALLY claim one available item (lowest shuffle_index) -> mark claimed, store wallet+tx
  - return the assigned item (id + image)
  v
Supabase (Postgres): drops, items, claims
```

Why server-side payment verify: a browser cannot be trusted to assert it paid, and supply must
be authoritative + race-safe across simultaneous buyers. That is the whole reason this is not
pure static.

---

## 5. Supabase schema (run this SQL)

```sql
create table drops (
  id            text primary key,              -- e.g. 'd001'
  date          date not null unique,
  title         text not null,
  price_zabal   numeric not null,              -- whole-token amount, e.g. 100
  price_usd     text default '~$1',
  seed_hash     text not null,                 -- hex hash(seed) published at creation (commit)
  seed          text,                          -- revealed only after sellout (null until then)
  live          boolean default true,
  created_at    timestamptz default now()
);

create table items (
  id            text primary key,              -- e.g. 'd001-03'
  drop_id       text not null references drops(id),
  shuffle_index int not null,                  -- claim order, derived from seed at creation
  image_path    text not null,                 -- '/assets/photos/d001/d001-03.jpg'
  status        text not null default 'available' check (status in ('available','claimed')),
  wallet        text,                          -- claimer, lowercased
  tx_hash       text,                          -- payment tx (unique), lowercased
  puller_handle text,                          -- optional display (e.g. farcaster username)
  claimed_at    timestamptz,
  unique (drop_id, shuffle_index)
);

create unique index items_tx_hash_uniq on items (tx_hash) where tx_hash is not null;
create index items_drop_status on items (drop_id, status);
```

Use the **service-role key** only inside serverless functions (never in the browser).

---

## 6. Fairness: commit–reveal randomness

At batch creation (`/api/admin/create-drop`):
1. Generate a random `seed` (32 bytes hex).
2. Deterministically shuffle the item ids using the seed (e.g. sort by
   `keccak256(seed + ':' + itemId)`), assign `shuffle_index = 0..n-1`.
3. Store `seed_hash = keccak256(seed)` publicly on the drop; keep `seed` secret (null in any
   public response) until the drop sells out or closes.
4. Claims always take the lowest `shuffle_index` still `available` (so order was fixed in
   advance, and which buyer gets which item is unpredictable to everyone until claimed).
5. After sellout, expose `seed`. Anyone can recompute the shuffle and confirm it matches
   `seed_hash` and the actual claim order. Publish a short "verify" note on the page.

This gives provable fairness without an on-chain VRF. (VRF is a Phase 3 option.)

---

## 7. API endpoints to build (Vercel functions, Node runtime)

Add `package.json` deps: `@supabase/supabase-js`, `viem`. Set functions to Node (not edge)
because they use the service-role key + RPC.

### `GET /api/drop?date=YYYY-MM-DD` (default: today, owner timezone)
Public. Returns the front-end shape, supply computed live, **never** returns `seed`:
```json
{
  "date": "2026-06-25", "title": "Drop 001", "priceZabal": 100, "priceUsd": "~$1",
  "token": "$ZABAL", "chain": "Base", "live": true, "seedHash": "0x...",
  "treasury": "0x...the treasury...",
  "tokenAddress": "0xbB48...0b07", "tokenDecimals": 18,
  "items": [ { "id": "d001-01", "status": "available" },
             { "id": "d001-02", "status": "claimed", "image": "/assets/photos/d001/d001-02.jpg", "puller": "@x" } ]
}
```
Note: only `claimed` items expose `image`. Available items must NOT leak their image (keeps the
pull blind). Store images privately or behind a check, OR only publish image_path on claim.

### `POST /api/pull`
Body: `{ "date": "YYYY-MM-DD", "wallet": "0x..", "txHash": "0x.." }`. Server steps:
1. Load drop; ensure `live` and not sold out.
2. **Reject if `txHash` already used** (unique index will also enforce).
3. **Verify payment via viem** (Base RPC, see §8). Must be: tx mined + success, is a Transfer
   of the $ZABAL token, `from == wallet`, `to == TREASURY_ADDRESS`, `value >= price_zabal * 10^decimals`,
   at least 1 confirmation.
4. Enforce `MAX_PER_WALLET`: count items where `drop_id=? and wallet=?`.
5. **Atomically claim** one item (race-safe, see §8 SQL).
6. Return `{ "id": "...", "image": "/assets/photos/.../x.jpg" }`.
Errors: clear JSON `{ "error": "reason" }` with appropriate status (402 unpaid/underpaid,
409 already used / sold out, 429 cap reached).

### `POST /api/admin/create-drop` (protected by `ADMIN_SECRET` header)
Body: `{ id, date, title, priceZabal, items: [{ id, imagePath }] }`. Generates seed, shuffles,
inserts `drops` + `items`, returns `seedHash`. This is how the owner starts a daily batch.

### (optional) `POST /api/admin/reveal-seed` — exposes `seed` after sellout for verification.

---

## 8. Implementation notes (the tricky bits)

**Verify the ERC-20 payment (viem):**
```js
import { createPublicClient, http, parseAbiItem, getAddress } from 'viem';
import { base } from 'viem/chains';
const client = createPublicClient({ chain: base, transport: http(process.env.BASE_RPC_URL) });

const receipt = await client.getTransactionReceipt({ hash: txHash });
if (receipt.status !== 'success') reject();
// find a Transfer log from the $ZABAL token contract
const TRANSFER = parseAbiItem('event Transfer(address indexed from, address indexed to, uint256 value)');
const log = receipt.logs.find(l => getAddress(l.address) === getAddress(TOKEN_ADDRESS));
// decode topics/data -> from, to, value; compare to wallet, TREASURY, price*10^decimals
// also: const conf = await client.getBlockNumber() - receipt.blockNumber; require >= 1
```
Read decimals once: `client.readContract({ address: TOKEN_ADDRESS, abi: erc20Abi, functionName: 'decimals' })`.

**Atomic claim (Postgres, race-safe) — pick lowest available shuffle_index:**
```sql
update items set status='claimed', wallet=$1, tx_hash=$2, claimed_at=now(), puller_handle=$3
where id = (
  select id from items
  where drop_id=$4 and status='available'
  order by shuffle_index
  for update skip locked
  limit 1
)
returning id, image_path;
```
Wrap the cap-check + this update in one transaction. `for update skip locked` prevents two
buyers grabbing the same item.

**Replay protection:** the `items_tx_hash_uniq` index means a given payment tx can claim at most
one item even under concurrency. Always check it before spending compute on assignment too.

**Front-end changes in `photos/index.html`:**
- Change `fetch('./drop.json')` to `fetch('/api/drop')`.
- Implement the `#insertCoin` click: connect wallet, send the $ZABAL transfer, then POST `/api/pull`.
  - Inside a Farcaster mini app: use the Farcaster SDK wallet provider
    (`@farcaster/miniapp-sdk`, already used elsewhere on the site) -> get an EIP-1193 provider.
  - Outside: `window.ethereum`. Wrap either with viem `createWalletClient`.
  - Load viem with no bundler: `import { ... } from 'https://esm.sh/viem'` (matches how the site
    loads the Farcaster SDK from a CDN).
  - ERC-20 transfer: `walletClient.writeContract({ address: TOKEN, abi: erc20Abi,
    functionName: 'transfer', args: [TREASURY, priceZabal * 10n**decimals] })`.
  - On success, POST `/api/pull`, then run the reveal: flip that tile to the returned image and
    update the counter.
- Keep the existing look. Add a small "Provably fair" line linking to the seed-hash / verify note.

**Env vars (set in Vercel project settings; NEVER commit values):**
```
SUPABASE_URL
SUPABASE_SERVICE_ROLE_KEY      # server only
BASE_RPC_URL                   # e.g. an Alchemy/Ankr Base endpoint
TOKEN_ADDRESS=0xbB48f19B0494Ff7C1fE5Dc2032aeEE14312f0b07   # verify first
TREASURY_ADDRESS               # where $ZABAL goes
ADMIN_SECRET                   # gates /api/admin/*
MAX_PER_WALLET=3
DROP_TIMEZONE=America/New_York # for "today" boundary
```

---

## 9. Alternative backend: Base smart contract (only if owner wants on-chain trustless)

Instead of `/api/pull` doing payment verify, a contract holds the batch and assigns on payment:
- `InsertCoinDrop` contract: owner seeds a drop with `merkleRoot`/count + price; `pull()` takes
  `priceZabal` $ZABAL via `transferFrom` (user approves first), assigns the next index using a
  commit-reveal or VRF, emits `Pulled(user, itemIndex)`. Off-chain indexer maps index->image.
- Pros: trustless, no server in the money path. Cons: more to build/audit, gas, approve step.
- Recommendation: ship the serverless version first; revisit a contract only if demand proves out.

---

## 10. Phase 2 (optional, after claim-only works): NFTs

- Deploy an ERC-1155 (or 721) on Base; mint the pulled item to the buyer instead of (or in
  addition to) the claim record. Pin images to IPFS/Arweave; tokenURI per item.
- Add a public gallery of pulled photos. Add resale links.

---

## 11. Build order / task list for the agent

1. Confirm $ZABAL address + decimals on Basescan. Pick an RPC provider, get a Base Sepolia
   testnet token or use a mock ERC-20 for testing.
2. Create Supabase project; run §5 SQL. Add `@supabase/supabase-js` + `viem` to `package.json`.
3. `GET /api/drop` (read-only) and switch the page to fetch it. Verify the existing UI still
   renders with live data.
4. `POST /api/admin/create-drop` + seed/shuffle (commit-reveal §6). Seed one test drop with
   3 dummy images in `assets/photos/test/`.
5. `POST /api/pull` with viem payment verify (§8) + atomic claim + cap. Unit-test the race with
   concurrent requests (two pulls, same last item -> exactly one wins).
6. Wire the front-end `#insertCoin` flow (wallet connect, transfer, pull, reveal). Test on Base
   **Sepolia** end to end.
7. Add the "provably fair" note + `reveal-seed` after sellout.
8. Switch to Base mainnet env, do one tiny real drop, then link `/photos` from the homepage nav.

## 12. Definition of done (v1)
- A real wallet can pay `priceZabal` $ZABAL on Base and receive exactly one random unclaimed
  photo; the counter decrements; double-spend of a tx is impossible; two simultaneous pulls for
  the last item -> exactly one succeeds; per-wallet cap enforced; sellout shows SOLD OUT; after
  sellout the seed verifies against the published hash. No secrets in the client bundle.

## 13. Gotchas
- Do NOT expose available items' images in `/api/drop` (keeps the pull blind). Only on claim.
- Lowercase wallet + txHash everywhere for comparisons.
- `priceZabal` is whole tokens; multiply by `10^decimals` for on-chain comparison (use BigInt).
- "Today" needs a fixed timezone (`DROP_TIMEZONE`) or drops roll over inconsistently.
- Service-role key and ADMIN_SECRET are server-only. The browser only ever talks to `/api/*`.
- Vercel: ensure `/api` functions use the Node runtime (they need the service-role key + RPC).

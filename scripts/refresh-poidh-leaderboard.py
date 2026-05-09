#!/usr/bin/env python3
"""
Refresh poidh-leaderboard.json by scraping poidh.xyz tRPC across one or
more BCZ-issued POIDH bounties. Defaults aggregate Round 1 (bounty 1151,
BCZ YapZ Ep 17) + Round 2 (bounty 1166, BCZ YapZ Ep 19 w/ Kenny) on Base.

    python3 scripts/refresh-poidh-leaderboard.py
    python3 scripts/refresh-poidh-leaderboard.py --bounty 1151 --bounty 1166 --chain 8453

Writes:
    poidh-leaderboard.json  - Empire Builder API-Sourced feed [{address, score}]
    poidh-audit.json        - audit trail (bounty + claims) across all bounties

Score = 1 per unique submitter wallet across the whole bounty set. No
double-count if a wallet submits multiple claims OR submits to multiple
bounties. Issuer wallets are excluded (PoidhV3 enforces issuer != claimant
on-chain anyway).
"""

import argparse
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

DEFAULT_BOUNTY_IDS = [1151, 1166]
DEFAULT_CHAIN_ID = 8453
BASE = "https://poidh.xyz/api/trpc"
REPO_ROOT = Path(__file__).resolve().parent.parent


def trpc(proc: str, payload: dict, timeout: int = 20) -> dict:
    inp = urllib.parse.quote(json.dumps({"0": {"json": payload}}))
    url = f"{BASE}/{proc}?batch=1&input={inp}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (poidh-leaderboard-refresh)"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())[0]["result"]["data"]["json"]


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--bounty", type=int, action="append", default=None)
    p.add_argument("--chain", type=int, default=DEFAULT_CHAIN_ID)
    args = p.parse_args()

    bounty_ids = args.bounty if args.bounty else DEFAULT_BOUNTY_IDS

    issuers: set[str] = set()
    seen: set[str] = set()
    unique_order: list[str] = []
    bounty_meta: list[dict] = []
    all_claims: list[dict] = []
    total_eth = 0.0
    total_claims = 0

    for bid in bounty_ids:
        b = trpc("bounties.fetch", {"id": bid, "chainId": args.chain})
        issuer = b["issuer"].lower()
        issuers.add(issuer)
        amount_eth = int(b.get("amount", "0") or 0) / 1e18
        total_eth += amount_eth

        claims_resp = trpc(
            "claims.fetchBountyClaims",
            {"bountyId": bid, "chainId": args.chain, "limit": 100},
        )
        items = claims_resp["items"]
        total_claims += len(items)

        print(f"Bounty {bid} on chain {args.chain}")
        print(f"  title:  {b['title'][:80]}")
        print(f"  issuer: {issuer}")
        print(f"  amount: {amount_eth:.6f} ETH")
        print(f"  album:  {b.get('extra', {}).get('album')}")
        print(f"  claims: {len(items)}")

        claim_count_for_bounty = 0
        for c in items:
            addr = c["issuer"].lower()
            if addr != issuer and addr not in seen:
                seen.add(addr)
                unique_order.append(addr)
            claim_count_for_bounty += 1
            all_claims.append({
                "bounty_id": bid,
                "claim_id": c["id"],
                "issuer": addr,
                "title": (c.get("title") or "")[:80],
                "accepted": bool(c.get("isAccepted")),
            })

        bounty_meta.append({
            "id": bid,
            "chainId": args.chain,
            "title": b["title"],
            "issuer": issuer,
            "album": b.get("extra", {}).get("album"),
            "amount_eth": amount_eth,
            "in_progress": bool(b.get("inProgress")),
            "is_voting": bool(b.get("isVoting")),
            "is_canceled": bool(b.get("isCanceled")),
            "claims_count": claim_count_for_bounty,
        })

    leaderboard = [{"address": a, "score": 1} for a in unique_order]

    feed_path = REPO_ROOT / "poidh-leaderboard.json"
    audit_path = REPO_ROOT / "poidh-audit.json"

    feed_path.write_text(json.dumps(leaderboard, indent=2) + "\n")
    audit_path.write_text(json.dumps({
        "bounty_ids": bounty_ids,
        "chainId": args.chain,
        "issuers": sorted(issuers),
        "total_claims": total_claims,
        "submitter_count": len(leaderboard),
        "total_eth_escrow": round(total_eth, 6),
        "bounties": bounty_meta,
        "claims": all_claims,
    }, indent=2) + "\n")

    print()
    print(f"Wrote {feed_path.relative_to(REPO_ROOT)}: {len(leaderboard)} unique submitters across {len(bounty_ids)} bounties")
    print(f"Wrote {audit_path.relative_to(REPO_ROOT)}: full audit trail")
    print(f"Total escrow: {total_eth:.6f} ETH, {total_claims} claims")
    return 0


if __name__ == "__main__":
    sys.exit(main())

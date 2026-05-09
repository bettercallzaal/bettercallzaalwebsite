#!/usr/bin/env python3
"""
Refresh poidh-leaderboard.json by scraping poidh.xyz tRPC for a single
POIDH bounty's claim submitters. Currently scoped to bounty 1151
(BCZ YapZ Ep 17, Base chain).

    python3 scripts/refresh-poidh-leaderboard.py
    python3 scripts/refresh-poidh-leaderboard.py --bounty 1151 --chain 8453

Writes:
    poidh-leaderboard.json  - Empire Builder API-Sourced feed [{address, score}]
    poidh-audit.json        - audit trail (bounty + claims)

Score = 1 per unique submitter wallet (no double-count even if a wallet
submits multiple claims). Issuer is excluded (PoidhV3 enforces issuer !=
claimant on-chain anyway).

To switch to album-wide, edit MODE below to "album" and set ALBUM.
"""

import argparse
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

DEFAULT_BOUNTY_ID = 1151
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
    p.add_argument("--bounty", type=int, default=DEFAULT_BOUNTY_ID)
    p.add_argument("--chain", type=int, default=DEFAULT_CHAIN_ID)
    args = p.parse_args()

    b = trpc("bounties.fetch", {"id": args.bounty, "chainId": args.chain})
    issuer = b["issuer"].lower()
    amount_eth = int(b.get("amount", "0") or 0) / 1e18
    print(f"Bounty {args.bounty} on chain {args.chain}")
    print(f"  title:  {b['title'][:80]}")
    print(f"  issuer: {issuer} (excluded)")
    print(f"  amount: {amount_eth:.6f} ETH")
    print(f"  album:  {b.get('extra', {}).get('album')}")

    claims_resp = trpc(
        "claims.fetchBountyClaims",
        {"bountyId": args.bounty, "chainId": args.chain, "limit": 100},
    )
    items = claims_resp["items"]

    seen: set[str] = set()
    unique_order: list[str] = []
    audit_claims: list[dict] = []
    for c in items:
        addr = c["issuer"].lower()
        if addr != issuer and addr not in seen:
            seen.add(addr)
            unique_order.append(addr)
        audit_claims.append({
            "claim_id": c["id"],
            "issuer": addr,
            "title": (c.get("title") or "")[:80],
            "accepted": bool(c.get("isAccepted")),
        })

    leaderboard = [{"address": a, "score": 1} for a in unique_order]

    feed_path = REPO_ROOT / "poidh-leaderboard.json"
    audit_path = REPO_ROOT / "poidh-audit.json"

    feed_path.write_text(json.dumps(leaderboard, indent=2) + "\n")
    audit_path.write_text(json.dumps({
        "bounty_id": args.bounty,
        "chainId": args.chain,
        "title": b["title"],
        "issuer": issuer,
        "album": b.get("extra", {}).get("album"),
        "amount_eth": amount_eth,
        "claim_count": len(items),
        "submitter_count": len(leaderboard),
        "claims": audit_claims,
    }, indent=2) + "\n")

    print()
    print(f"Wrote {feed_path.relative_to(REPO_ROOT)}: {len(leaderboard)} submitters, {len(items)} claims")
    print(f"Wrote {audit_path.relative_to(REPO_ROOT)}: audit trail")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
Refresh poidh-leaderboard.json by scraping poidh.xyz tRPC for the
We The Media album. Run from repo root:

    python3 scripts/refresh-poidh-leaderboard.py

Writes:
    poidh-leaderboard.json  - Empire Builder API-Sourced feed [{address, score}]
    poidh-audit.json        - audit trail of bounties + claims

Source: poidh.xyz uses tRPC over /api/trpc. No API key needed for reads.
Procedures used:
    bounties.fetchByAlbum    - list bounties in an album by status
    claims.fetchBountyClaims - list claims for a bounty (paginated)

Album verified 2026-05-09 via bounty 1151 extra.album field = "wethemmedia".
Issuers are excluded (PoidhV3 enforces issuer != claimant on-chain anyway).
Score = number of claims submitted by that address across the album.
"""

import json
import sys
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

ALBUM = "wethemmedia"
BASE = "https://poidh.xyz/api/trpc"
REPO_ROOT = Path(__file__).resolve().parent.parent


def trpc(proc: str, payload: dict, timeout: int = 20) -> dict:
    inp = urllib.parse.quote(json.dumps({"0": {"json": payload}}))
    url = f"{BASE}/{proc}?batch=1&input={inp}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (poidh-leaderboard-refresh)"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())[0]["result"]["data"]["json"]


def main() -> int:
    bounties: list[dict] = []
    for status in ("open", "progress", "past"):
        d = trpc("bounties.fetchByAlbum", {"album": ALBUM, "status": status, "limit": 100})
        bounties.extend(d["items"])
        print(f"[{status}] {len(d['items'])} bounties")

    issuers = {b["issuer"].lower() for b in bounties}
    score: Counter[str] = Counter()
    all_claims: list[dict] = []
    bounty_meta: list[dict] = []

    for b in bounties:
        d = trpc(
            "claims.fetchBountyClaims",
            {"bountyId": b["id"], "chainId": b["chainId"], "limit": 100},
        )
        items = d["items"]
        print(f"  bounty {b['id']} ch={b['chainId']}: {len(items)} claims")

        amount_wei = int(b.get("amount", "0") or 0) if str(b.get("amount", "0")).isdigit() else 0
        bounty_meta.append({
            "id": b["id"],
            "chainId": b["chainId"],
            "title": b["title"],
            "issuer": b["issuer"],
            "amount_wei": str(amount_wei),
            "amount_eth": amount_wei / 1e18,
            "claims_count": len(items),
        })

        for c in items:
            addr = c["issuer"].lower()
            score[addr] += 1
            all_claims.append({
                "bounty_id": b["id"],
                "claim_id": c["id"],
                "issuer": addr,
                "title": (c.get("title") or "")[:80],
                "accepted": bool(c.get("isAccepted")),
            })

    leaderboard = [{"address": a, "score": s} for a, s in score.most_common() if a not in issuers]
    total_eth = sum(b["amount_eth"] for b in bounty_meta)

    feed_path = REPO_ROOT / "poidh-leaderboard.json"
    audit_path = REPO_ROOT / "poidh-audit.json"

    feed_path.write_text(json.dumps(leaderboard, indent=2) + "\n")
    audit_path.write_text(json.dumps({
        "album": ALBUM,
        "bounty_count": len(bounty_meta),
        "claim_count": len(all_claims),
        "submitter_count": len(leaderboard),
        "total_eth_escrow": round(total_eth, 6),
        "issuers": sorted(issuers),
        "bounties": bounty_meta,
        "claims": all_claims,
    }, indent=2) + "\n")

    print()
    print(f"Wrote {feed_path.relative_to(REPO_ROOT)}: {len(leaderboard)} submitters")
    print(f"Wrote {audit_path.relative_to(REPO_ROOT)}: audit trail")
    print(f"Total escrow: {total_eth:.6f} ETH across {len(bounty_meta)} bounties")
    return 0


if __name__ == "__main__":
    sys.exit(main())

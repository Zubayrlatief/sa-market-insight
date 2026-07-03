"""SA Market Insight - CLI entry point.

Usage:
    python run.py                 # run full pipeline (uses cache when fresh)
    python run.py --refresh       # force re-scrape of all sources
    python run.py --out reports   # custom output directory
    python run.py --sectors energy,fintech,ict   # limit deep-dive sectors
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

from samarket.analysis import scoring
from samarket.knowledge.benchmarks import SECTORS
from samarket.report import html_report
from samarket.sources import news, sarb, statssa, worldbank


def main():
    ap = argparse.ArgumentParser(description="South Africa business market insight scraper")
    ap.add_argument("--refresh", action="store_true", help="ignore cache, re-scrape everything")
    ap.add_argument("--out", default="reports", help="output directory")
    ap.add_argument("--sectors", default="", help="comma-separated sector keys to include")
    args = ap.parse_args()

    keys = [k.strip() for k in args.sectors.split(",") if k.strip()] or list(SECTORS)
    unknown = [k for k in keys if k not in SECTORS]
    if unknown:
        sys.exit(f"Unknown sectors: {unknown}. Valid: {list(SECTORS)}")

    print("[1/4] World Bank API: macro + sector growth series ...")
    wb = worldbank.fetch_all(refresh=args.refresh)
    ok = sum(1 for d in wb.values() if d.get("series"))
    print(f"      {ok}/{len(wb)} indicators loaded")

    print("[2/4] Stats SA P0043.1: liquidations by industry ...")
    try:
        liq = statssa.fetch_liquidations(refresh=args.refresh)
        print(f"      release: {liq['period']}  |  industries: {len(liq['by_industry'])}")
    except Exception as exc:  # noqa: BLE001 - degrade gracefully, report why
        print(f"      WARNING: liquidations unavailable ({exc})")
        liq = None

    print("[3/4] Google News (ZA): sector signals ...")
    news_by_sector = {}
    for k in keys:
        meta = SECTORS[k]
        try:
            n = news.fetch_sector_news(k, meta["news_query"], refresh=args.refresh)
            c = n["counts"]
            print(f"      {meta['name'][:38]:<40} +{c['positive']} / -{c['negative']} "
                  f"(signal {n['signal']:+.2f})")
            news_by_sector[k] = n
        except Exception as exc:  # noqa: BLE001
            print(f"      WARNING: news failed for {k} ({exc})")
            news_by_sector[k] = {"counts": None, "signal": 0.0, "headlines": []}

    print("[4/4] Scoring & report ...")
    results = [r for r in scoring.score_sectors(wb, liq, news_by_sector) if r["key"] in keys]

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = date.today().isoformat()

    sarb_rates = sarb.fetch_rates(refresh=args.refresh)
    html_path = html_report.build(results, wb, liq, sarb_rates,
                                  out_dir / f"sa-market-insight-{stamp}.html")

    json_payload = {
        "generated": stamp,
        "liquidations": liq,
        "macro": {c: {"label": d["label"], "latest": d["latest"]} for c, d in wb.items()},
        "sarb_rates": sarb_rates,
        "sectors": [{k: v for k, v in r.items() if k != "meta"} for r in results],
    }
    json_path = out_dir / f"sa-market-insight-{stamp}.json"
    json_path.write_text(json.dumps(json_payload, indent=2, ensure_ascii=False),
                         encoding="utf-8")

    print("\n=== SECTOR RANKING (health score /100) ===")
    for i, r in enumerate(results, 1):
        growth = (f"{r['avg_growth_3yr']:+.1f}%/yr" if r["avg_growth_3yr"] is not None else "  n/a ")
        print(f"{i:>2}. {r['name']:<38} {r['composite']:>5.1f}  {r['verdict']:<28} "
              f"growth {growth}  opportunity {r['opportunity']:.0f}")

    print(f"\nHTML report: {html_path.resolve()}")
    print(f"JSON data:   {json_path.resolve()}")


if __name__ == "__main__":
    main()

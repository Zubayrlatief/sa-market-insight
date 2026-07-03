# SA Market Insight

High-level analytic scraper for South African business markets. Scrapes live
public data, scores every major sector, and generates an insight report
covering: which markets are doing well vs failing, failure/success rates,
the KPIs that decide survival, capital required to enter, market gaps, and
long-term (5-10 year) growth outlooks.

## What it scrapes (all free, keyless, legitimate endpoints)

| Source | What it provides | Endpoint style |
|---|---|---|
| **Stats SA P0043.1** | Official liquidations by industry (business failure), monthly + annual trend | Direct PDF download, parsed with pdfplumber |
| **World Bank Open Data API** | GDP growth, inflation, unemployment, consumption, FDI, new-business density, sector-group real growth | JSON API |
| **SARB Web API** | Current repo/prime/CPI/PPI rates | JSON API |
| **Google News RSS (ZA)** | Per-sector expansion vs distress headline signals (180 days) | RSS |

Plus a **curated knowledge base** ([samarket/knowledge/benchmarks.py](samarket/knowledge/benchmarks.py))
for the things no API publishes: sector KPIs and targets, ZAR capital
requirements by entry size, failure drivers, success factors, market gaps and
structural outlooks — with sources noted.

Note: the Stats SA *website* is bot-protected, but publication PDFs are
directly downloadable at predictable URLs; the scraper walks back from the
current month to find the newest release. Everything is cached under
`data/cache/` (12h-7d TTLs) so repeat runs don't hammer the sources.

## Usage

```powershell
python -m pip install -r requirements.txt
python run.py                     # full pipeline, uses cache
python run.py --refresh           # force re-scrape
python run.py --pdf               # also export a PDF (uses installed Chrome/Edge)
python run.py --sectors energy,fintech,ict
python run.py --out reports
```

Outputs to `reports/`:
- `sa-market-insight-YYYY-MM-DD.html` — self-contained dashboard (open in a browser)
- `sa-market-insight-YYYY-MM-DD.pdf` — print-ready version of the same report (with `--pdf`)
- `sa-market-insight-YYYY-MM-DD.json` — all data, machine-readable

## Scoring model

Health score (0-100) per sector:

| Weight | Component | Evidence |
|---|---|---|
| 35% | Structural outlook | Curated 5-10yr growth potential |
| 25% | Growth momentum | World Bank sector-group real growth, 3yr avg |
| 20% | News signal | Positive vs negative headline ratio |
| 20% | Failure pressure | Stats SA liquidations YoY by industry |

Opportunity score = 65% structural outlook + 35% ease of entry (inverse of
barrier score) — rewards markets with strong outlooks that are still
accessible to new entrants.

## Sectors covered

agriculture, mining, manufacturing, energy (renewables), construction,
retail (incl. e-commerce), tourism, logistics, fintech, realestate, ict,
healthcare, bpo

## Caveats

- Liquidations undercount failure: most SMME deaths are informal dissolutions,
  never formally liquidated. National baselines in the report contextualise this.
- Capital figures are ZAR planning estimates — verify against live quotes.
- News signal is a classifier over headlines, not ground truth.
- This is a research/planning tool, not investment advice.

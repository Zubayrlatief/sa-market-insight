"""Stats SA P0043.1 'Statistics of liquidations' scraper.

The Stats SA website HTML is behind bot protection, but the publication
PDFs are directly downloadable at a predictable URL:

    https://www.statssa.gov.za/publications/P00431/P00431{Month}{Year}.pdf

We walk backwards from the current month until a PDF exists, then parse
Table 1 (total liquidations according to industry) and Table 2 (monthly
totals by year). This is the official measure of business failure by
industry in South Africa (source data: CIPC).
"""

import io
import re
from datetime import date

import requests

from .. import cache

URL_TMPL = "https://www.statssa.gov.za/publications/P00431/P00431{month}{year}.pdf"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) sa-market-insight/1.0"}

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

# Canonical industry keys, matched by prefix of the row label in Table 1.
INDUSTRY_ROWS = [
    ("agriculture", "Agriculture"),
    ("mining", "Mining"),
    ("manufacturing", "Manufacturing"),
    ("utilities", "Electricity"),
    ("construction", "Construction"),
    ("trade_accommodation", "Trade"),
    ("transport_comms", "Transport"),
    ("finance_realestate_business", "Financing"),
    ("community_services", "Community"),
    ("unclassified", "Unclassified"),
]


def _month_candidates(today: date, lookback: int = 14):
    """Yield (MonthName, year) going backwards from last month."""
    y, m = today.year, today.month
    for _ in range(lookback):
        m -= 1
        if m == 0:
            m, y = 12, y - 1
        yield MONTHS[m - 1], y


def find_latest_pdf(today: date | None = None):
    """Return (url, month_name, year, pdf_bytes) of the newest available release."""
    today = today or date.today()
    session = requests.Session()
    for month, year in _month_candidates(today):
        url = URL_TMPL.format(month=month, year=year)
        try:
            resp = session.get(url, headers=HEADERS, timeout=60)
        except requests.RequestException:
            continue
        if resp.status_code == 200 and resp.content[:5] == b"%PDF-":
            return url, month, year, resp.content
    raise RuntimeError("No recent Stats SA P0043.1 liquidations PDF found")


def _extract_row_numbers(tokens):
    """Resolve a row's digit tokens into 12 numbers: (C, V, Total) x 4 periods.

    Stats SA prints thousands with space separators ("1 005"), so "111 1 005
    1 116" is really three numbers (111, 1005, 1116) - ambiguous from tokens
    alone. Every triplet satisfies C + V = Total, so we backtrack over
    optional merges of 3-digit groups and keep the parse that satisfies the
    identity for all four triplets.
    """
    def dfs(i, acc):
        if len(acc) == 12:
            return acc
        if i >= len(tokens):
            return None
        # Candidate values starting at token i: unmerged first, then with
        # successive 3-digit groups absorbed as thousands separators.
        candidates = [(int(tokens[i]), i + 1)]
        val, j = candidates[0]
        while j < len(tokens) and len(tokens[j]) == 3:
            val = val * 1000 + int(tokens[j])
            j += 1
            candidates.append((val, j))
        for value, nxt in candidates:
            branch = acc + [value]
            if len(branch) % 3 == 0:
                c, v, t = branch[-3:]
                if c + v != t:
                    continue
            result = dfs(nxt, branch)
            if result:
                return result
        return None

    return dfs(0, [])


def _parse_table1(text: str):
    """Parse 'Table 1 - Total liquidations according to industry (number)'.

    Each row carries 12 numbers: (C, V, Total) x 4 periods:
    year-to-date, same month previous year, previous month, current month.
    Long industry names wrap across lines, so we accumulate digit tokens
    until the row's 12 numbers resolve.
    """
    lines = text.splitlines()
    # Skip the contents page: its "Table 1 ..." entries have dot leaders.
    start = next((i for i, l in enumerate(lines)
                  if l.startswith("Table 1 ") and ".." not in l), None)
    if start is None:
        raise ValueError("Table 1 not found in liquidations PDF")
    end = next((i for i, l in enumerate(lines)
                if i > start and l.startswith("Table 1.1") and ".." not in l), len(lines))

    rows = {}
    current_key = None
    tokens: list[str] = []

    def flush():
        nonlocal current_key, tokens
        if current_key:
            nums = _extract_row_numbers(tokens)
            if nums:
                rows[current_key] = {
                    "ytd_total": nums[2],
                    "same_month_prev_year": nums[5],
                    "prev_month_total": nums[8],
                    "month_total": nums[11],
                }
        current_key, tokens = None, []

    for line in lines[start + 1:end]:
        stripped = line.strip()
        if stripped.startswith(("STATISTICS SOUTH AFRICA", "Statistics of liquidations")):
            continue  # page header/footer noise
        row_match = re.match(r"^\d+\.\s*(.+)", stripped)
        total_match = stripped.startswith("Total number of liquidations")
        if row_match or total_match:
            flush()
            if total_match:
                current_key = "total"
            else:
                label = row_match.group(1)
                current_key = next(
                    (key for key, prefix in INDUSTRY_ROWS if label.startswith(prefix)),
                    None,
                )
            # Drop the "N." row-number prefix so it doesn't leak into the data
            stripped = re.sub(r"^\d+\.\s*", "", stripped)
        tokens.extend(re.findall(r"\d+", stripped))
    flush()
    return rows


def _parse_table2(text: str):
    """Parse 'Table 2 - Total liquidations (number)': month rows x year columns.

    Returns {"years": [...], "months": {"January": [v1, v2, ...], ...}}.
    """
    lines = text.splitlines()
    start = next((i for i, l in enumerate(lines)
                  if l.startswith("Table 2 ") and ".." not in l), None)
    if start is None:
        return None
    years = None
    months = {}
    for line in lines[start + 1:start + 25]:
        stripped = line.strip()
        if years is None:
            m = re.match(r"^Month((?:\s+\d{4})+)", stripped)
            if m:
                years = [int(y) for y in m.group(1).split()]
            continue
        m = re.match(r"^(January|February|March|April|May|June|July|August|"
                     r"September|October|November|December)((?:\s+[\d\s]+)?)$", stripped)
        if m:
            vals = [int(v) for v in m.group(2).split()]
            months[m.group(1)] = vals
        if stripped.startswith("Total"):
            break
    if not years or not months:
        return None
    return {"years": years, "months": months}


def fetch_liquidations(refresh: bool = False):
    """Return the latest liquidations-by-industry data.

    {
      "source_url", "period" (e.g. "June 2025"),
      "by_industry": {key: {ytd_total, same_month_prev_year, prev_month_total,
                            month_total, yoy_change_pct}},
      "monthly_totals": Table 2 data for the national trend,
      "annual_totals": {year: total} derived from Table 2,
    }
    """
    if not refresh:
        cached = cache.get("statssa_liquidations", ttl=7 * 24 * 3600)
        if cached is not None:
            return cached

    import pdfplumber  # deferred: heavy import

    url, month, year, pdf_bytes = find_latest_pdf()
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)

    by_industry = _parse_table1(text)
    for row in by_industry.values():
        prev = row["same_month_prev_year"]
        cur = row["month_total"]
        row["yoy_change_pct"] = (round(100.0 * (cur - prev) / prev, 1)
                                 if prev else None)

    monthly = _parse_table2(text)
    annual = {}
    if monthly:
        for idx, yr in enumerate(monthly["years"]):
            vals = [v[idx] for v in monthly["months"].values() if len(v) > idx]
            if vals:
                annual[str(yr)] = sum(vals)

    data = {
        "source_url": url,
        "period": f"{month} {year}",
        "by_industry": by_industry,
        "monthly_totals": monthly,
        "annual_totals": annual,
    }
    cache.put("statssa_liquidations", data)
    return data

"""World Bank Open Data API scraper for South Africa (ZAF).

Free, keyless JSON API. Provides macro context and broad sector-group
growth series (agriculture / industry / manufacturing / services).
"""

import requests

from .. import cache

BASE = "https://api.worldbank.org/v2/country/ZAF/indicator/{code}?format=json&per_page=70"
HEADERS = {"User-Agent": "sa-market-insight/1.0 (research tool)"}

# indicator code -> (label, unit)
INDICATORS = {
    # Macro backdrop
    "NY.GDP.MKTP.KD.ZG": ("GDP growth", "% p.a."),
    "FP.CPI.TOTL.ZG": ("Inflation (CPI)", "% p.a."),
    "SL.UEM.TOTL.ZS": ("Unemployment", "% of labour force"),
    "NE.CON.PRVT.KD.ZG": ("Household consumption growth", "% p.a."),
    "BX.KLT.DINV.WD.GD.ZS": ("FDI inflows", "% of GDP"),
    "IC.BUS.NDNS.ZS": ("New business density", "registrations per 1,000 adults"),
    "IT.NET.USER.ZS": ("Internet users", "% of population"),
    "EG.ELC.ACCS.ZS": ("Access to electricity", "% of population"),
    # Sector groups - real growth
    "NV.AGR.TOTL.KD.ZG": ("Agriculture value added growth", "% p.a."),
    "NV.IND.TOTL.KD.ZG": ("Industry value added growth", "% p.a."),
    "NV.IND.MANF.KD.ZG": ("Manufacturing value added growth", "% p.a."),
    "NV.SRV.TOTL.KD.ZG": ("Services value added growth", "% p.a."),
    # Sector groups - share of GDP
    "NV.AGR.TOTL.ZS": ("Agriculture share of GDP", "%"),
    "NV.IND.MANF.ZS": ("Manufacturing share of GDP", "%"),
    "NV.SRV.TOTL.ZS": ("Services share of GDP", "%"),
}

# Analytic sector group -> growth indicator code
SECTOR_GROWTH = {
    "agriculture": "NV.AGR.TOTL.KD.ZG",
    "industry": "NV.IND.TOTL.KD.ZG",
    "manufacturing": "NV.IND.MANF.KD.ZG",
    "services": "NV.SRV.TOTL.KD.ZG",
}


def fetch_indicator(code: str, refresh: bool = False):
    """Return list of {year, value} sorted ascending, most recent last."""
    key = f"wb_{code.replace('.', '_')}"
    if not refresh:
        cached = cache.get(key)
        if cached is not None:
            return cached
    resp = requests.get(BASE.format(code=code), headers=HEADERS, timeout=60)
    resp.raise_for_status()
    body = resp.json()
    rows = body[1] if len(body) > 1 and body[1] else []
    series = [
        {"year": int(r["date"]), "value": r["value"]}
        for r in rows
        if r.get("value") is not None
    ]
    series.sort(key=lambda x: x["year"])
    cache.put(key, series)
    return series


def fetch_all(refresh: bool = False):
    """Fetch every configured indicator. Returns {code: {label, unit, series, latest}}."""
    out = {}
    for code, (label, unit) in INDICATORS.items():
        try:
            series = fetch_indicator(code, refresh=refresh)
        except requests.RequestException as exc:
            out[code] = {"label": label, "unit": unit, "series": [], "latest": None,
                         "error": str(exc)}
            continue
        out[code] = {
            "label": label,
            "unit": unit,
            "series": series,
            "latest": series[-1] if series else None,
        }
    return out


def recent_avg_growth(series, years: int = 3):
    """Average of the last `years` observations of a growth-rate series."""
    vals = [p["value"] for p in series[-years:] if p["value"] is not None]
    if not vals:
        return None
    return sum(vals) / len(vals)

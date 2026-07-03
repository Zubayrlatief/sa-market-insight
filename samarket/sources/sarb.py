"""SARB (Reserve Bank) public web API - current headline rates."""

import requests

from .. import cache

URL = "https://custom.resbank.co.za/SarbWebApi/WebIndicators/HomePageRates"
HEADERS = {"User-Agent": "sa-market-insight/1.0 (research tool)"}

WANTED = {"CPI", "PPI", "Repo rate", "Prime lending rate", "Real GDP growth rate"}


def fetch_rates(refresh: bool = False):
    """Return [{name, value, date}] for headline SA rates."""
    if not refresh:
        cached = cache.get("sarb_rates", ttl=24 * 3600)
        if cached is not None:
            return cached
    try:
        resp = requests.get(URL, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        rows = resp.json()
    except (requests.RequestException, ValueError):
        return []
    data = [
        {"name": r["Name"], "value": r["Value"], "date": r.get("Date", "")}
        for r in rows
        if r.get("Name") in WANTED and r.get("Value") is not None
    ]
    cache.put("sarb_rates", data)
    return data

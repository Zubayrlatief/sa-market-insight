"""Google News RSS scraper - per-sector expansion/distress signal mining.

Uses the South African edition of Google News RSS (keyless). For each
sector we run a targeted query and classify headlines into positive
(growth/expansion/investment) vs negative (closure/liquidation/distress)
signals. This is a *signal*, not ground truth - it complements the
official Stats SA liquidation numbers with current, granular texture.
"""

import time
import urllib.parse

import feedparser
import requests

from .. import cache

RSS = ("https://news.google.com/rss/search?q={query}"
       "&hl=en-ZA&gl=ZA&ceid=ZA:en")
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) sa-market-insight/1.0"}

POSITIVE = [
    "growth", "expand", "expansion", "invest", "investment", "record",
    "surge", "boom", "profit", "opens", "launch", "hiring", "jobs boost",
    "recovery", "rebound", "exports rise", "demand", "opportunity",
    "funding", "raises", "billion injection", "new plant", "new store",
]
NEGATIVE = [
    "liquidation", "liquidated", "business rescue", "closure", "closes",
    "shut down", "shuts", "retrench", "layoff", "job cuts", "job losses",
    "decline", "slump", "crisis", "collapse", "insolven", "bankrupt",
    "loss-making", "downturn", "struggling", "warning", "load shedding hits",
]


def _classify(title: str):
    t = title.lower()
    pos = any(k in t for k in POSITIVE)
    neg = any(k in t for k in NEGATIVE)
    if pos and not neg:
        return "positive"
    if neg and not pos:
        return "negative"
    return "neutral"


def fetch_sector_news(sector_key: str, query: str, refresh: bool = False,
                      max_items: int = 40):
    """Fetch and classify recent headlines for one sector query.

    Returns {counts: {positive, negative, neutral}, signal: -1..1,
             headlines: [{title, link, published, tone}]}
    """
    cache_key = f"news_{sector_key}"
    if not refresh:
        cached = cache.get(cache_key, ttl=12 * 3600)
        if cached is not None:
            return cached

    url = RSS.format(query=urllib.parse.quote(f"{query} when:180d"))
    resp = requests.get(url, headers=HEADERS, timeout=60)
    resp.raise_for_status()
    feed = feedparser.parse(resp.text)

    headlines = []
    counts = {"positive": 0, "negative": 0, "neutral": 0}
    for entry in feed.entries[:max_items]:
        tone = _classify(entry.title)
        counts[tone] += 1
        headlines.append({
            "title": entry.title,
            "link": entry.get("link", ""),
            "published": entry.get("published", ""),
            "tone": tone,
        })

    scored = counts["positive"] + counts["negative"]
    signal = ((counts["positive"] - counts["negative"]) / scored) if scored else 0.0

    data = {"counts": counts, "signal": round(signal, 3), "headlines": headlines}
    cache.put(cache_key, data)
    time.sleep(1.0)  # be polite between sector queries
    return data

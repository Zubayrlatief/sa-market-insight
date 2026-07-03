"""Composite sector scoring.

Combines four evidence streams into a 0-100 health/opportunity score:

  structural outlook (35%) - curated 5-10yr growth potential
  growth momentum    (25%) - World Bank sector-group real growth, last 3yrs
  news signal        (20%) - Google News positive vs negative headline ratio
  failure pressure   (20%) - Stats SA liquidations YoY trend for the industry

Plus an 'opportunity score' that rewards markets where the outlook is
strong relative to how hard/expensive they are to enter.
"""

from ..knowledge.benchmarks import SECTORS
from ..sources import worldbank


def _clamp(v, lo=0.0, hi=100.0):
    return max(lo, min(hi, v))


def _momentum_score(avg_growth):
    """Map avg real growth % (-5..+6) onto 0-100, 50 = ~1.5% trend growth."""
    if avg_growth is None:
        return 50.0
    return _clamp(50 + (avg_growth - 1.5) * 10)


def _news_score(signal):
    """Map -1..1 headline signal onto 0-100."""
    return _clamp(50 + signal * 50)


def _failure_score(liq_row):
    """Higher = healthier. Uses YoY change in monthly liquidations.

    A sector with falling liquidations scores above 50, rising below.
    Damped because monthly counts are small and noisy.
    """
    if not liq_row:
        return 50.0
    yoy = liq_row.get("yoy_change_pct")
    if yoy is None:
        # No liquidations in the base month - treat small absolute counts as healthy
        return 60.0 if liq_row.get("month_total", 0) <= 2 else 50.0
    return _clamp(50 - yoy * 0.4)


def verdict(score):
    if score >= 72:
        return "Strong growth market"
    if score >= 60:
        return "Healthy / improving"
    if score >= 48:
        return "Stable but competitive"
    if score >= 38:
        return "Under pressure"
    return "Failing / avoid without an edge"


def score_sectors(wb_data, liquidations, news_by_sector):
    """Return list of scored sector dicts, ranked best-first."""
    results = []
    for key, meta in SECTORS.items():
        growth_code = worldbank.SECTOR_GROWTH[meta["wb_group"]]
        series = wb_data.get(growth_code, {}).get("series", [])
        avg_growth = worldbank.recent_avg_growth(series, years=3)

        liq_row = liquidations["by_industry"].get(meta["statssa_key"]) if liquidations else None
        news = news_by_sector.get(key, {})
        signal = news.get("signal", 0.0)

        s_struct = float(meta["longterm"]["score"])
        s_momentum = _momentum_score(avg_growth)
        s_news = _news_score(signal)
        s_failure = _failure_score(liq_row)

        composite = round(
            0.35 * s_struct + 0.25 * s_momentum + 0.20 * s_news + 0.20 * s_failure, 1
        )
        # Opportunity: strong outlook, discounted by entry barriers
        opportunity = round(_clamp(0.65 * s_struct + 0.35 * (100 - meta["barriers"])), 1)

        results.append({
            "key": key,
            "name": meta["name"],
            "composite": composite,
            "verdict": verdict(composite),
            "opportunity": opportunity,
            "components": {
                "structural": round(s_struct, 1),
                "momentum": round(s_momentum, 1),
                "news": round(s_news, 1),
                "failure": round(s_failure, 1),
            },
            "avg_growth_3yr": round(avg_growth, 2) if avg_growth is not None else None,
            "liquidations": liq_row,
            "news_counts": news.get("counts"),
            "news_signal": signal,
            "headlines": [h for h in news.get("headlines", []) if h["tone"] != "neutral"][:6],
            "meta": meta,
        })
    results.sort(key=lambda r: r["composite"], reverse=True)
    return results

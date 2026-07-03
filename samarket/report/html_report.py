"""Self-contained HTML report generator (no external assets).

Written for readability: plain-English labels, an executive summary that
answers "where is the opportunity" in sentences, and scores translated
into words rather than bare numbers.
"""

import html
from datetime import date

from ..knowledge.benchmarks import NATIONAL_BASELINES
from . import charts

MONTH_ORDER = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]
MONTH_ABBR = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
              "Oct", "Nov", "Dec"]

SHORT_NAMES = {
    "agriculture": "Agriculture", "mining": "Mining", "manufacturing": "Manufacturing",
    "energy": "Energy", "construction": "Construction", "retail": "Retail",
    "tourism": "Tourism", "logistics": "Logistics", "fintech": "Fintech",
    "realestate": "Property", "ict": "ICT", "healthcare": "Healthcare", "bpo": "BPO",
}

INDUSTRY_NAMES = {
    "agriculture": "Agriculture, forestry & fishing",
    "mining": "Mining & quarrying",
    "manufacturing": "Manufacturing",
    "utilities": "Electricity, gas & water",
    "construction": "Construction",
    "trade_accommodation": "Trade, catering & accommodation",
    "transport_comms": "Transport & communication",
    "finance_realestate_business": "Finance, property & business services",
    "community_services": "Community & personal services",
    "unclassified": "Unclassified",
}

CSS = """
:root { --bg:#f6f7f9; --card:#ffffff; --ink:#1c2733; --muted:#5c6b7a; --line:#e3e8ee;
        --green:#1e8e5a; --green-bg:#e5f5ec; --amber:#a86c00; --amber-bg:#fdf3dd;
        --red:#c0392b; --red-bg:#fdeae7; --blue:#1f6fb2; --blue-bg:#e8f1fa; }
* { box-sizing:border-box; margin:0; padding:0; }
body { background:var(--bg); color:var(--ink); font:16px/1.65 Georgia,'Times New Roman',serif; padding:30px 16px; }
.wrap { max-width:880px; margin:0 auto; }
h1 { font-size:30px; margin-bottom:6px; }
h2 { font-size:22px; margin:44px 0 6px; }
h2 + .lead { margin-bottom:16px; }
h3 { font-size:16px; margin:18px 0 6px; font-family:'Segoe UI',system-ui,sans-serif; }
.lead { color:var(--muted); font-size:15px; }
.sub { color:var(--muted); font-size:13.5px; }
p { margin:8px 0; }
ul { margin:6px 0 10px 22px; }
li { margin-bottom:5px; }
.card { background:var(--card); border:1px solid var(--line); border-radius:12px; padding:22px 26px; margin:14px 0; }
.tag { font-family:'Segoe UI',system-ui,sans-serif; padding:3px 12px; border-radius:20px; font-size:13px; font-weight:600; white-space:nowrap; display:inline-block; }
.t-green { background:var(--green-bg); color:var(--green); }
.t-amber { background:var(--amber-bg); color:var(--amber); }
.t-red   { background:var(--red-bg);   color:var(--red); }
.t-blue  { background:var(--blue-bg);  color:var(--blue); }
table { width:100%; border-collapse:collapse; background:var(--card); border:1px solid var(--line); border-radius:12px; overflow:hidden; font-family:'Segoe UI',system-ui,sans-serif; }
th,td { padding:11px 14px; text-align:left; border-bottom:1px solid var(--line); font-size:14.5px; }
th { background:#eef1f5; font-weight:600; font-size:12.5px; text-transform:uppercase; letter-spacing:.4px; color:var(--muted); }
tr:last-child td { border-bottom:none; }
td a { color:var(--ink); text-decoration:none; border-bottom:1px dotted #9aa7b4; }
.facts { display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:12px; font-family:'Segoe UI',system-ui,sans-serif; }
.fact { background:var(--card); border:1px solid var(--line); border-radius:12px; padding:16px; }
.fact .v { font-size:24px; font-weight:650; }
.fact .l { color:var(--muted); font-size:13px; margin-top:2px; line-height:1.4; }
.sector { background:var(--card); border:1px solid var(--line); border-radius:12px; padding:26px 30px; margin:22px 0; }
.sector .head { display:flex; justify-content:space-between; align-items:baseline; flex-wrap:wrap; gap:10px; }
.sector h2.name { margin:0; font-size:21px; }
.bottomline { background:var(--blue-bg); border-radius:8px; padding:12px 16px; margin:14px 0; font-size:15.5px; }
.kv { font-family:'Segoe UI',system-ui,sans-serif; font-size:14px; color:var(--muted); margin:10px 0 4px; }
.kv b { color:var(--ink); }
.kpi { border-left:3px solid var(--blue); padding:8px 12px; margin:8px 0; background:#f4f8fc; border-radius:0 8px 8px 0; font-size:14.5px; }
.kpi .why { color:var(--muted); font-size:13.5px; }
.hl { font-size:14px; margin:6px 0; font-family:'Segoe UI',system-ui,sans-serif; }
.hl a { color:var(--blue); text-decoration:none; }
.up { color:var(--green); font-weight:700; } .down { color:var(--red); font-weight:700; }
.note { background:#eef1f5; border-radius:8px; padding:14px 16px; font-size:13.5px; color:var(--muted); margin-top:10px; }
svg text { fill:var(--muted); font-size:11px; font-family:'Segoe UI',system-ui,sans-serif; }
.chart-card { background:var(--card); border:1px solid var(--line); border-radius:12px; padding:20px; margin:14px 0; }
.chart-card h3 { margin-top:0; }
.minis { display:grid; grid-template-columns:1fr 1fr; gap:6px 30px; font-family:'Segoe UI',system-ui,sans-serif; font-size:12.5px; margin:12px 0 4px; }
@media (max-width:700px){ .minis{grid-template-columns:1fr;} }
.mini { display:flex; align-items:center; gap:10px; }
.mini .mlabel { width:170px; color:var(--muted); flex-shrink:0; }
.mini .mbar { flex:1; height:9px; background:#eef1f5; border-radius:5px; }
.mini .mbar i { display:block; height:9px; border-radius:5px; }
.mini .mword { width:70px; font-weight:600; }
* { -webkit-print-color-adjust:exact; print-color-adjust:exact; }
@media print {
  body { background:#fff; padding:0; font-size:13px; }
  .wrap { max-width:100%; }
  h2 { margin-top:26px; }
  .chart-card, .fact, .kpi, .card, table, .bottomline, .minis, .note { break-inside:avoid; }
  .sector { border:none; padding:10px 0; break-before:page; }
  .hl a { color:var(--ink); }
}
"""


def _esc(s):
    return html.escape(str(s))


def _tone_tag(v):
    if v.startswith("Strong"):
        return "t-green"
    if v.startswith("Healthy"):
        return "t-blue"
    if v.startswith("Stable"):
        return "t-amber"
    return "t-red"


def _word(score):
    """Translate a 0-100 score into a plain word."""
    if score >= 80:
        return "Excellent"
    if score >= 65:
        return "Good"
    if score >= 50:
        return "Fair"
    if score >= 35:
        return "Weak"
    return "Poor"


def _entry_word(barriers):
    if barriers >= 75:
        return "Very hard (licences / heavy capital)"
    if barriers >= 60:
        return "Hard"
    if barriers >= 45:
        return "Moderate"
    return "Relatively easy"


def _fmt(v, suffix=""):
    return f"{v:,.1f}{suffix}" if isinstance(v, (int, float)) else "n/a"


def _failure_section(liquidations):
    """Annual bars + monthly comparison lines + industry breakdown."""
    if not liquidations:
        return "<p class='sub'>Liquidation data unavailable this run.</p>"
    out = []

    annual = liquidations.get("annual_totals")
    if annual:
        out.append("<div class='chart-card'><h3>Liquidations per year</h3>"
                   + charts.annual_bars(annual)
                   + "<div class='sub'>The last bar is a part-year figure. "
                     "Source: Stats SA P0043.1 (official data from CIPC).</div></div>")

    monthly = liquidations.get("monthly_totals")
    if monthly and monthly.get("years"):
        years = monthly["years"][-3:]
        idx0 = len(monthly["years"]) - len(years)
        series = []
        for j, yr in enumerate(years):
            col = idx0 + j
            pts = []
            for m_i, m_name in enumerate(MONTH_ORDER, start=1):
                vals = monthly["months"].get(m_name, [])
                if len(vals) > col:
                    pts.append((m_i, vals[col]))
            if pts:
                color = [charts.GRAY, charts.BLUE, charts.RED][j % 3] if len(years) == 3 \
                    else [charts.BLUE, charts.RED][j % 2]
                series.append({"name": str(yr), "color": color, "points": pts})
        if series:
            x_labels = {i: MONTH_ABBR[i - 1] for i in range(1, 13)}
            out.append("<div class='chart-card'><h3>Month by month: this year vs recent years</h3>"
                       + charts.line_chart(series, x_labels=x_labels, zero_line=False)
                       + "<div class='sub'>Monthly liquidation counts. A line running below "
                         "previous years means fewer businesses are closing.</div></div>")

    by_ind = liquidations.get("by_industry", {})
    items = [(INDUSTRY_NAMES.get(k, k), v.get("ytd_total", 0), charts.RED)
             for k, v in by_ind.items() if k != "total"]
    items.sort(key=lambda t: -t[1])
    if items:
        out.append("<div class='chart-card'><h3>Which industries are the closures in? "
                   f"(so far this year, {_esc(liquidations.get('period', ''))} release)</h3>"
                   + charts.hbar(items, title_gap=250)
                   + "<div class='sub'>'Unclassified' is large because many closing companies "
                     "never state an industry — read the named bars as relative pressure.</div></div>")
    return "".join(out)


def _economy_charts(wb):
    out = []
    gdp = (wb.get("NY.GDP.MKTP.KD.ZG") or {}).get("series", [])
    gdp_pts = [(p["year"], round(p["value"], 2)) for p in gdp if p["year"] >= date.today().year - 16]
    if len(gdp_pts) > 2:
        out.append("<div class='chart-card'><h3>Economic growth over the last 15 years</h3>"
                   + charts.line_chart([{"name": "GDP growth", "color": charts.BLUE,
                                         "points": gdp_pts}], y_suffix="%")
                   + "<div class='sub'>Real GDP growth per year. Below the dotted zero line, "
                     "the economy shrank. Source: World Bank.</div></div>")

    groups = [("Agriculture", "NV.AGR.TOTL.KD.ZG", charts.GREEN),
              ("Manufacturing", "NV.IND.MANF.KD.ZG", charts.RED),
              ("Industry overall", "NV.IND.TOTL.KD.ZG", charts.AMBER),
              ("Services", "NV.SRV.TOTL.KD.ZG", charts.BLUE)]
    series = []
    for name, code, color in groups:
        s = (wb.get(code) or {}).get("series", [])
        pts = [(p["year"], round(p["value"], 2)) for p in s if p["year"] >= date.today().year - 11]
        if len(pts) > 2:
            series.append({"name": name, "color": color, "points": pts})
    if series:
        out.append("<div class='chart-card'><h3>Which parts of the economy are growing?</h3>"
                   + charts.line_chart(series, y_suffix="%")
                   + "<div class='sub'>Real growth of each broad sector group per year. "
                     "Source: World Bank.</div></div>")
    return "".join(out)


def _ranking_chart(results):
    tone_color = {"t-green": charts.GREEN, "t-blue": charts.BLUE,
                  "t-amber": charts.AMBER, "t-red": charts.RED}
    items = [(r["name"], r["composite"], tone_color[_tone_tag(r["verdict"])])
             for r in results]
    return ("<div class='chart-card'><h3>Health score by market</h3>"
            + charts.hbar(items, value_fmt="{:.0f}", title_gap=250)
            + "<div class='sub'>Green = strong growth market, blue = healthy, "
              "amber = stable but competitive, red = under pressure.</div></div>")


def _opportunity_map(results):
    tone_color = {"t-green": charts.GREEN, "t-blue": charts.BLUE,
                  "t-amber": charts.AMBER, "t-red": charts.RED}
    pts = [(100 - r["meta"]["barriers"], r["components"]["structural"],
            SHORT_NAMES.get(r["key"], r["name"]), tone_color[_tone_tag(r["verdict"])])
           for r in results]
    svg = charts.quadrant_scatter(
        pts, "Easier to get into", "Bigger long-term future",
        ("Hard to enter, big future", "Prime territory",
         "Tough and slow", "Easy in, limited ceiling"))
    return ("<div class='chart-card'><h3>Where opportunity meets accessibility</h3>"
            + svg
            + "<div class='sub'>Up = stronger 5-10 year outlook. Right = cheaper/easier for a "
              "new entrant. The top-right quadrant is where growth and accessibility overlap.</div></div>")


def _news_mood_chart(results):
    items = []
    for r in sorted(results, key=lambda r: -(r.get("news_signal") or 0)):
        c = r.get("news_counts")
        if c:
            items.append((r["name"], c.get("positive", 0), c.get("negative", 0)))
    if not items:
        return ""
    return ("<div class='chart-card'><h3>News mood by market (last 6 months)</h3>"
            + charts.diverging(items, title_gap=250)
            + "<div class='sub'>Headlines classified as expansion/investment (green) vs "
              "closures/distress (red) from Google News South Africa.</div></div>")


def _exec_summary(results, liq):
    top = results[:3]
    bottom = [r for r in reversed(results[-2:])]
    easy_wins = sorted(results, key=lambda r: r["opportunity"], reverse=True)[:3]

    total = (liq or {}).get("by_industry", {}).get("total", {})
    yoy = total.get("yoy_change_pct")
    if yoy is None:
        trend_sentence = ""
    elif yoy <= 0:
        trend_sentence = (f"Business failures are <b>falling</b>: liquidations are down "
                          f"{abs(yoy):.0f}% compared with the same month last year.")
    else:
        trend_sentence = (f"Business failures are <b>rising</b>: liquidations are up "
                          f"{yoy:.0f}% compared with the same month last year.")

    tops = "".join(
        f"<li><b>{_esc(r['name'])}</b> — {_esc(r['meta']['summary'].split('.')[0])}.</li>"
        for r in top)
    eases = "".join(
        f"<li><b>{_esc(r['name'])}</b> — long-term outlook {_word(r['components']['structural']).lower()}, "
        f"entry {_entry_word(r['meta']['barriers']).lower()}.</li>"
        for r in easy_wins)
    bottoms = "".join(
        f"<li><b>{_esc(r['name'])}</b> — {_esc(r['meta']['longterm']['risks'][0])}.</li>"
        for r in bottom)

    return f"""
<div class='card'>
  <p>{trend_sentence} That said, the bigger picture is unforgiving:
  roughly <b>7 to 8 out of every 10 small businesses in South Africa close within
  five years</b>, usually because of cash-flow gaps, late payments and thin capital
  — not because the idea was bad.</p>
  <h3>Strongest markets right now</h3><ul>{tops}</ul>
  <h3>Best opportunity for a new entrant (growth vs cost of getting in)</h3><ul>{eases}</ul>
  <h3>Approach with caution</h3><ul>{bottoms}</ul>
</div>"""


def _macro_cards(wb, sarb_rates):
    cards = []
    friendly = {
        "NY.GDP.MKTP.KD.ZG": "How fast the economy is growing",
        "FP.CPI.TOTL.ZG": "Inflation (how fast prices rise)",
        "SL.UEM.TOTL.ZS": "Unemployment",
        "NE.CON.PRVT.KD.ZG": "Household spending growth",
        "IC.BUS.NDNS.ZS": "New businesses registered per 1,000 adults",
    }
    for code, label in friendly.items():
        d = wb.get(code) or {}
        latest = d.get("latest")
        if not latest:
            continue
        cards.append(f"<div class='fact'><div class='v'>{_fmt(latest['value'], '%') if code != 'IC.BUS.NDNS.ZS' else _fmt(latest['value'])}</div>"
                     f"<div class='l'>{_esc(label)} ({latest['year']})</div></div>")
    friendly_rates = {"Repo rate": "Repo rate (cost of money)",
                      "Prime lending rate": "Prime rate (what banks charge)",
                      "CPI": "Inflation right now (CPI)"}
    for r in sarb_rates or []:
        if r["name"] in friendly_rates:
            cards.append(f"<div class='fact'><div class='v'>{_fmt(r['value'], '%')}</div>"
                         f"<div class='l'>{_esc(friendly_rates[r['name']])}</div></div>")
    return f"<div class='facts'>{''.join(cards)}</div>"


def _mini_bars(comps, barriers):
    def color(v):
        return (charts.GREEN if v >= 65 else charts.AMBER if v >= 45 else charts.RED)

    rows = [("Long-term outlook", comps["structural"]),
            ("Recent growth momentum", comps["momentum"]),
            ("News mood", comps["news"]),
            ("Failure trend (high = improving)", comps["failure"]),
            ("Ease of entry", 100 - barriers)]
    parts = ["<div class='minis'>"]
    for label, v in rows:
        parts.append(
            f"<div class='mini'><span class='mlabel'>{_esc(label)}</span>"
            f"<span class='mbar'><i style='width:{v:.0f}%;background:{color(v)}'></i></span>"
            f"<span class='mword' style='color:{color(v)}'>{_word(v)}</span></div>")
    parts.append("</div>")
    return "".join(parts)


def _sector_block(r, rank):
    m = r["meta"]
    liq = r["liquidations"] or {}
    yoy = liq.get("yoy_change_pct")
    comps = r["components"]
    growth = r["avg_growth_3yr"]

    if yoy is None:
        liq_txt = "Too few formal liquidations in this industry to read a trend."
        arrow = ""
    else:
        direction = "down" if yoy <= 0 else "up"
        cls = "up" if yoy <= 0 else "down"
        arrow = f"<span class='{cls}'>{'▼' if yoy <= 0 else '▲'} {direction} {abs(yoy):.0f}% vs a year ago</span>"
        liq_txt = (f"{liq.get('month_total', '?')} liquidations this month "
                   f"({liq.get('ytd_total', '?')} so far this year), {arrow}.")

    kpis = "".join(
        f"<div class='kpi'><b>{_esc(k['kpi'])}</b> — aim for {_esc(k['target'])}<br>"
        f"<span class='why'>{_esc(k['why'])}</span></div>" for k in m["kpis"])
    gaps = "".join(f"<li>{_esc(g)}</li>" for g in m["gaps"])
    drivers = "".join(f"<li>{_esc(d)}</li>" for d in m["longterm"]["drivers"])
    risks = "".join(f"<li>{_esc(x)}</li>" for x in m["longterm"]["risks"])
    fdrivers = "".join(f"<li>{_esc(x)}</li>" for x in m["failure"]["drivers"])
    sfactors = "".join(f"<li>{_esc(x)}</li>" for x in m["success_factors"])
    heads = "".join(
        f"<div class='hl'><span class='{'up' if h['tone'] == 'positive' else 'down'}'>"
        f"{'▲' if h['tone'] == 'positive' else '▼'}</span> "
        f"<a href='{_esc(h['link'])}'>{_esc(h['title'])}</a></div>" for h in r["headlines"][:4])

    cap = m["capital"]
    growth_txt = (f"the broader sector group grew {growth:+.1f}% a year on average over the "
                  f"last three years" if growth is not None else "no recent growth data")

    return f"""
<div class='sector' id='{r["key"]}'>
  <div class='head'>
    <h2 class='name'>{rank}. {_esc(r["name"])}</h2>
    <span class='tag {_tone_tag(r["verdict"])}'>{_esc(r["verdict"])} · {r["composite"]:.0f}/100</span>
  </div>
  <div class='bottomline'><b>Bottom line:</b> {_esc(m["summary"])}</div>
  {_mini_bars(comps, m["barriers"])}
  <div class='kv'>Getting in: <b>{_entry_word(m["barriers"])}</b> &nbsp;·&nbsp;
    Recent momentum: {_esc(growth_txt)}</div>

  <h3>Are businesses failing here?</h3>
  <p>{liq_txt}</p>
  <p class='sub'>{_esc(m["failure"]["baseline"])}</p>
  <p><b>What kills businesses in this market:</b></p><ul>{fdrivers}</ul>
  <p><b>What the survivors do differently:</b></p><ul>{sfactors}</ul>

  <h3>What it costs to start (rough ZAR planning figures)</h3>
  <ul>
    <li><b>Starting small:</b> {_esc(cap["micro"])}</li>
    <li><b>Serious entry:</b> {_esc(cap["small"])}</li>
    <li><b>At scale:</b> {_esc(cap["medium"])}</li>
  </ul>
  <div class='note'>{_esc(cap["note"])}</div>

  <h3>The numbers to watch (KPIs that decide survival)</h3>
  {kpis}

  <h3>Gaps in the market — where new money can go</h3><ul>{gaps}</ul>
  <h3>Why this market should grow over the next 5-10 years</h3><ul>{drivers}</ul>
  <h3>What could go wrong</h3><ul>{risks}</ul>
  {'<h3>In the news lately</h3>' + heads if heads else ''}
</div>"""


def build(results, wb, liquidations, sarb_rates, out_path):
    rows = []
    for i, r in enumerate(results, 1):
        rows.append(
            f"<tr><td>{i}</td>"
            f"<td><a href='#{r['key']}'>{_esc(r['name'])}</a></td>"
            f"<td><span class='tag {_tone_tag(r['verdict'])}'>{_esc(r['verdict'])}</span></td>"
            f"<td>{r['composite']:.0f}/100</td>"
            f"<td>{_word(r['components']['structural'])}</td>"
            f"<td>{_entry_word(r['meta']['barriers'])}</td></tr>")

    sources = "".join(f"<li>{_esc(s)}</li>" for s in NATIONAL_BASELINES["sources"])
    liq_period = liquidations.get("period", "n/a") if liquidations else "n/a"

    page = f"""<!doctype html><html><head><meta charset='utf-8'>
<meta name='viewport' content='width=device-width,initial-scale=1'>
<title>South Africa Market Insight - {date.today().isoformat()}</title><style>{CSS}</style></head><body>
<div class='wrap'>
<h1>South Africa: Which Markets Are Worth Entering?</h1>
<p class='lead'>A data-driven read on South Africa's business markets — which are thriving,
which are failing, what it costs to get in, and what it takes to survive.</p>
<p class='sub'>Generated {date.today().isoformat()} from live sources: Stats SA liquidations
({_esc(liq_period)} release), World Bank, SARB, Google News SA. Figures are for planning —
verify before committing money.</p>

<h2>The short version</h2>
{_exec_summary(results, liquidations)}

<h2>The economy at a glance</h2>
<p class='lead'>The backdrop every business in the country operates against.</p>
{_macro_cards(wb, sarb_rates)}
{_economy_charts(wb)}

<h2>Are more businesses failing, or fewer?</h2>
<p class='lead'>Formal liquidations are the official count of companies that closed.
Most small-business closures never reach this register, so treat it as the tip of the
iceberg — but the direction of the trend is meaningful.</p>
{_failure_section(liquidations)}

<h2>All markets, ranked</h2>
<p class='lead'>Health combines long-term outlook (35%), recent growth (25%), news signals (20%)
and the liquidation trend (20%). Click a market in the table to jump to its full breakdown.</p>
{_ranking_chart(results)}
{_opportunity_map(results)}
{_news_mood_chart(results)}
<table><tr><th>#</th><th>Market</th><th>Verdict</th><th>Health</th>
<th>5-10yr outlook</th><th>Getting in</th></tr>
{''.join(rows)}</table>

<h2>Market by market</h2>
{''.join(_sector_block(r, i) for i, r in enumerate(results, 1))}

<h2>Where this data comes from</h2>
<div class='note'>Live sources scraped on generation day: <ul>{sources}</ul>
Capital figures and KPI benchmarks are curated planning estimates, reviewed against industry
publications — always verify against live quotes. This report is research, not investment advice.</div>
</div></body></html>"""

    out_path.write_text(page, encoding="utf-8")
    return out_path

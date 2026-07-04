"""Market-entry playbook report generator.

A companion document to the main insight report: for each sector, how to
enter, year-by-year targets, KPI evolution, client acquisition/retention
and the 10-20 year strategy. Self-contained HTML like the main report.
"""

import html
from datetime import date

from ..knowledge.benchmarks import SECTORS
from ..knowledge.playbooks import PLAYBOOKS
from .html_report import CSS

EXTRA_CSS = """
.steps { counter-reset: step; list-style:none; margin:10px 0; }
.steps li { counter-increment: step; position:relative; padding:0 0 14px 44px; margin:0; }
.steps li::before { content: counter(step); position:absolute; left:0; top:2px;
  width:28px; height:28px; border-radius:50%; background:var(--blue); color:#fff;
  font:600 14px/28px 'Segoe UI',system-ui,sans-serif; text-align:center; }
.steps b { display:block; margin-bottom:2px; }
.steps .d { color:var(--muted); font-size:14px; }
.stages { display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin:10px 0; }
@media (max-width:820px){ .stages{grid-template-columns:1fr;} }
.stage { background:#f4f8fc; border:1px solid var(--line); border-radius:10px; padding:14px 16px; }
.stage h4 { font:600 13.5px 'Segoe UI',system-ui,sans-serif; color:var(--blue); margin-bottom:8px; }
.stage ul { margin-left:16px; }
.stage li { font-size:13px; margin-bottom:4px; }
.channels { display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin:10px 0; }
@media (max-width:820px){ .channels{grid-template-columns:1fr;} }
.channel { border:1px solid var(--line); border-radius:10px; padding:14px 16px; }
.channel h4 { font:600 13.5px 'Segoe UI',system-ui,sans-serif; margin-bottom:8px; }
.channel.out h4 { color:var(--red); } .channel.in h4 { color:var(--green); }
.channel.keep h4 { color:var(--blue); }
.channel ul { margin-left:16px; } .channel li { font-size:13px; margin-bottom:6px; }
.roadmap td:first-child { white-space:nowrap; font-weight:600; }
.roadmap ul { margin:0 0 0 16px; } .roadmap li { font-size:13px; margin-bottom:3px; }
.toc { columns:2; font-family:'Segoe UI',system-ui,sans-serif; font-size:14.5px; }
@media (max-width:700px){ .toc{columns:1;} }
.toc a { color:var(--ink); text-decoration:none; border-bottom:1px dotted #9aa7b4; }
.toc li { margin-bottom:6px; }
.posit { background:var(--blue-bg); border-radius:8px; padding:12px 16px; margin:12px 0; font-size:15px; }
@media print { .sector-pb { break-before:page; } .stage, .channel, .steps li { break-inside:avoid; } }
"""


def _esc(s):
    return html.escape(str(s))


def _chapter(key, rank):
    pb = PLAYBOOKS[key]
    name = SECTORS[key]["name"]

    steps = "".join(
        f"<li><b>{_esc(t)}</b><span class='d'>{_esc(d)}</span></li>"
        for t, d in pb["entry"])

    roadmap_rows = "".join(
        f"<tr><td>{_esc(phase)}</td><td>{_esc(focus)}</td>"
        f"<td><ul>{''.join(f'<li>{_esc(t)}</li>' for t in targets)}</ul></td></tr>"
        for phase, focus, targets in pb["roadmap"])

    stages = "".join(
        f"<div class='stage'><h4>{_esc(stage)}</h4>"
        f"<ul>{''.join(f'<li>{_esc(k)}</li>' for k in kpis)}</ul></div>"
        for stage, kpis in pb["kpi_stages"])

    def channel(cls, title, items):
        lis = "".join(f"<li>{_esc(i)}</li>" for i in items)
        return f"<div class='channel {cls}'><h4>{title}</h4><ul>{lis}</ul></div>"

    longgame = "".join(f"<li>{_esc(x)}</li>" for x in pb["longgame"])

    return f"""
<div class='sector-pb' id='pb-{key}'>
  <h2>{rank}. {_esc(name)}</h2>
  <div class='posit'><b>The smart way in:</b> {_esc(pb["positioning"])}</div>

  <h3>How to get in — step by step</h3>
  <ol class='steps'>{steps}</ol>

  <h3>Your roadmap: what to hit, year by year</h3>
  <table class='roadmap'><tr><th>Phase</th><th>Focus</th><th>Realistic targets</th></tr>
  {roadmap_rows}</table>

  <h3>How your KPIs change as you grow</h3>
  <div class='stages'>{stages}</div>

  <h3>How clients are actually won and kept</h3>
  <div class='channels'>
    {channel("out", "Outbound — go get them", pb["outbound"])}
    {channel("in", "Inbound — make them come", pb["inbound"])}
    {channel("keep", "Retention — keep them", pb["retention"])}
  </div>

  <h3>The 10-20 year game</h3>
  <ul>{longgame}</ul>
</div>"""


def build_playbooks(ordered_keys, out_path):
    """ordered_keys: sector keys in ranking order (best market first)."""
    keys = [k for k in ordered_keys if k in PLAYBOOKS]
    toc = "".join(
        f"<li>{i}. <a href='#pb-{k}'>{_esc(SECTORS[k]['name'])}</a></li>"
        for i, k in enumerate(keys, 1))
    chapters = "".join(_chapter(k, i) for i, k in enumerate(keys, 1))

    page = f"""<!doctype html><html><head><meta charset='utf-8'>
<meta name='viewport' content='width=device-width,initial-scale=1'>
<title>SA Market Entry Playbooks - {date.today().isoformat()}</title>
<style>{CSS}{EXTRA_CSS}</style></head><body>
<div class='wrap'>
<h1>South Africa: Market Entry Playbooks</h1>
<p class='lead'>The practical companion to the market insight report: how to actually get into
each market, what to aim for year by year, how your KPIs should evolve, how clients are won
and kept, and how to keep growing for the next 10-20 years.</p>
<p class='sub'>Generated {date.today().isoformat()}. Figures are realistic planning corridors
for a competent, adequately funded operator - they are targets to manage against, not promises.
Sectors are ordered by current market health (best first).</p>

<div class='card'>
<h3>How to use these playbooks</h3>
<ul>
<li><b>Steps</b> are sequenced - skipping early steps (offtake, licences, cash buffers) is the
most common cause of failure in every sector.</li>
<li><b>Year-by-year targets</b> are corridors: landing inside the range means you're on track;
missing the bottom of a range two phases running means change the plan.</li>
<li><b>"Fast but safe" scaling</b> in practice means: never outgrow your cash runway, your
compliance, or your ability to deliver quality - the roadmaps encode all three.</li>
<li>Cross-reference the main insight report for each market's current health, failure data
and capital requirements.</li>
</ul>
</div>

<h2>Contents</h2>
<ol class='toc'>{toc}</ol>

{chapters}

<h2>Final word</h2>
<div class='note'>Every playbook here assumes the national baseline: most South African
small businesses fail on cash flow, late payments and under-capitalisation - not bad ideas.
The common thread across all thirteen playbooks: secure demand before capacity, keep months
of runway banked, make compliance a weapon, own recurring revenue, and let annuity income -
not adrenaline - fund each next step. Verify all figures against current market conditions
before committing capital; this is research, not financial advice.</div>
</div></body></html>"""

    out_path.write_text(page, encoding="utf-8")
    return out_path

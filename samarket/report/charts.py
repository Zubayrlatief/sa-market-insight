"""Inline-SVG chart builders for the HTML report.

Everything renders without external libraries or assets so the report
stays a single self-contained file.
"""

import html

GREEN = "#1e8e5a"
AMBER = "#d29216"
RED = "#c0392b"
BLUE = "#1f6fb2"
GRAY = "#8a99a8"
GRID = "#e3e8ee"
INK = "#1c2733"

PALETTE = [BLUE, RED, GREEN, AMBER, "#7d5ba6", "#2a9d8f"]


def _esc(s):
    return html.escape(str(s))


def _nice_ticks(lo, hi, n=5):
    """Return ~n rounded tick values spanning [lo, hi]."""
    if hi <= lo:
        hi = lo + 1
    span = hi - lo
    raw = span / max(n - 1, 1)
    mag = 10 ** len(str(int(abs(raw)))) / 10 if raw >= 1 else 0.1
    for step in (mag, mag * 2, mag * 2.5, mag * 5, mag * 10):
        if span / step <= n:
            break
    start = int(lo / step) * step
    if start > lo:
        start -= step
    ticks = []
    t = start
    while t <= hi + step * 0.5:
        ticks.append(round(t, 2))
        t += step
    return ticks


def hbar(items, width=680, value_fmt="{:,.0f}", title_gap=200):
    """Horizontal bar chart. items: [(label, value, color)] sorted as given."""
    if not items:
        return ""
    row_h, pad_top = 30, 8
    height = pad_top + row_h * len(items) + 6
    vmax = max(v for _, v, _ in items) or 1
    bar_w = width - title_gap - 70
    parts = [f"<svg viewBox='0 0 {width} {height}' style='max-width:{width}px;width:100%'>"]
    for i, (label, value, color) in enumerate(items):
        y = pad_top + i * row_h
        w = max((value / vmax) * bar_w, 2)
        parts.append(
            f"<text x='{title_gap - 8}' y='{y + 19}' text-anchor='end' "
            f"style='font-size:12.5px;fill:{INK}'>{_esc(label)}</text>"
            f"<rect x='{title_gap}' y='{y + 6}' width='{w:.0f}' height='17' rx='3' fill='{color}'/>"
            f"<text x='{title_gap + w + 6:.0f}' y='{y + 19}' style='font-size:12px'>"
            f"{_esc(value_fmt.format(value))}</text>")
    parts.append("</svg>")
    return "".join(parts)


def diverging(items, width=680, title_gap=200):
    """Diverging bars. items: [(label, pos, neg)]. Positive right, negative left."""
    if not items:
        return ""
    row_h, pad_top = 28, 24
    height = pad_top + row_h * len(items) + 6
    vmax = max(max(p, n) for _, p, n in items) or 1
    half = (width - title_gap - 60) / 2
    cx = title_gap + half
    parts = [f"<svg viewBox='0 0 {width} {height}' style='max-width:{width}px;width:100%'>"]
    parts.append(f"<text x='{cx - 6}' y='14' text-anchor='end' style='font-size:11px;fill:{RED}'>negative headlines</text>"
                 f"<text x='{cx + 6}' y='14' style='font-size:11px;fill:{GREEN}'>positive headlines</text>"
                 f"<line x1='{cx}' y1='{pad_top - 4}' x2='{cx}' y2='{height - 4}' stroke='{GRID}'/>")
    for i, (label, pos, neg) in enumerate(items):
        y = pad_top + i * row_h
        wp = (pos / vmax) * half
        wn = (neg / vmax) * half
        parts.append(
            f"<text x='{title_gap - 8}' y='{y + 17}' text-anchor='end' "
            f"style='font-size:12.5px;fill:{INK}'>{_esc(label)}</text>"
            f"<rect x='{cx - wn:.0f}' y='{y + 5}' width='{max(wn, 1):.0f}' height='15' rx='3' fill='{RED}' opacity='.8'/>"
            f"<rect x='{cx + 1}' y='{y + 5}' width='{max(wp, 1):.0f}' height='15' rx='3' fill='{GREEN}' opacity='.85'/>"
            f"<text x='{cx + wp + 5:.0f}' y='{y + 17}' style='font-size:11px'>{pos}</text>"
            f"<text x='{cx - wn - 5:.0f}' y='{y + 17}' text-anchor='end' style='font-size:11px'>{neg}</text>")
    parts.append("</svg>")
    return "".join(parts)


def line_chart(series_list, width=680, height=260, y_suffix="", x_labels=None,
               zero_line=True):
    """Multi-series line chart.

    series_list: [{name, color, points: [(x, y), ...]}] with numeric x.
    x_labels: optional {x_value: label}; defaults to str(x).
    """
    pts_all = [(x, y) for s in series_list for x, y in s["points"] if y is not None]
    if not pts_all:
        return ""
    pad_l, pad_r, pad_t, pad_b = 52, 14, 30, 30
    xs = [p[0] for p in pts_all]
    ys = [p[1] for p in pts_all]
    x_lo, x_hi = min(xs), max(xs)
    ticks = _nice_ticks(min(ys), max(ys))
    y_lo, y_hi = ticks[0], ticks[-1]

    def sx(x):
        return pad_l + (x - x_lo) / max(x_hi - x_lo, 1e-9) * (width - pad_l - pad_r)

    def sy(y):
        return height - pad_b - (y - y_lo) / max(y_hi - y_lo, 1e-9) * (height - pad_t - pad_b)

    parts = [f"<svg viewBox='0 0 {width} {height}' style='max-width:{width}px;width:100%'>"]
    for t in ticks:
        parts.append(f"<line x1='{pad_l}' y1='{sy(t):.0f}' x2='{width - pad_r}' y2='{sy(t):.0f}' "
                     f"stroke='{GRID}'/>"
                     f"<text x='{pad_l - 6}' y='{sy(t) + 4:.0f}' text-anchor='end' "
                     f"style='font-size:11px'>{t:g}{y_suffix}</text>")
    if zero_line and y_lo < 0 < y_hi:
        parts.append(f"<line x1='{pad_l}' y1='{sy(0):.0f}' x2='{width - pad_r}' y2='{sy(0):.0f}' "
                     f"stroke='{GRAY}' stroke-dasharray='4 3'/>")
    # x labels: at most ~8, spread across distinct x values
    distinct = sorted({x for x in xs})
    step = max(1, len(distinct) // 8)
    for x in distinct[::step]:
        lbl = (x_labels or {}).get(x, f"{x:g}")
        parts.append(f"<text x='{sx(x):.0f}' y='{height - 8}' text-anchor='middle' "
                     f"style='font-size:11px'>{_esc(lbl)}</text>")
    # legend
    lx = pad_l
    for s in series_list:
        parts.append(f"<rect x='{lx}' y='8' width='12' height='4' rx='2' fill='{s['color']}'/>"
                     f"<text x='{lx + 17}' y='14' style='font-size:11.5px;fill:{INK}'>{_esc(s['name'])}</text>")
        lx += 24 + 7.2 * len(s["name"])
    # lines
    for s in series_list:
        pts = [(x, y) for x, y in s["points"] if y is not None]
        if len(pts) < 2:
            continue
        d = " ".join(f"{sx(x):.1f},{sy(y):.1f}" for x, y in pts)
        parts.append(f"<polyline points='{d}' fill='none' stroke='{s['color']}' "
                     f"stroke-width='2.2' stroke-linejoin='round'/>")
        x_last, y_last = pts[-1]
        parts.append(f"<circle cx='{sx(x_last):.1f}' cy='{sy(y_last):.1f}' r='3' fill='{s['color']}'/>")
    parts.append("</svg>")
    return "".join(parts)


def quadrant_scatter(points, x_label, y_label, quads, width=680, height=430):
    """Scatter with quadrant shading at (50,50). points: [(x, y, label, color)].

    quads: (top_left, top_right, bottom_left, bottom_right) corner captions.
    Both axes are 0-100.
    """
    pad_l, pad_r, pad_t, pad_b = 46, 16, 16, 44

    def sx(x):
        return pad_l + x / 100 * (width - pad_l - pad_r)

    def sy(y):
        return height - pad_b - y / 100 * (height - pad_t - pad_b)

    parts = [f"<svg viewBox='0 0 {width} {height}' style='max-width:{width}px;width:100%'>"]
    # quadrant tints
    parts.append(f"<rect x='{sx(50):.0f}' y='{sy(100):.0f}' width='{sx(100) - sx(50):.0f}' "
                 f"height='{sy(50) - sy(100):.0f}' fill='{GREEN}' opacity='.07'/>")
    parts.append(f"<rect x='{sx(0):.0f}' y='{sy(50):.0f}' width='{sx(50) - sx(0):.0f}' "
                 f"height='{sy(0) - sy(50):.0f}' fill='{RED}' opacity='.06'/>")
    # axes + midlines
    parts.append(f"<rect x='{pad_l}' y='{pad_t}' width='{width - pad_l - pad_r}' "
                 f"height='{height - pad_t - pad_b}' fill='none' stroke='{GRID}'/>")
    parts.append(f"<line x1='{sx(50):.0f}' y1='{pad_t}' x2='{sx(50):.0f}' y2='{height - pad_b}' "
                 f"stroke='{GRID}'/>"
                 f"<line x1='{pad_l}' y1='{sy(50):.0f}' x2='{width - pad_r}' y2='{sy(50):.0f}' "
                 f"stroke='{GRID}'/>")
    tl, tr, bl, br = quads
    qstyle = f"style='font-size:11px;fill:{GRAY};font-style:italic'"
    parts.append(f"<text x='{sx(2):.0f}' y='{sy(97):.0f}' {qstyle}>{_esc(tl)}</text>"
                 f"<text x='{sx(98):.0f}' y='{sy(97):.0f}' text-anchor='end' {qstyle}>{_esc(tr)}</text>"
                 f"<text x='{sx(2):.0f}' y='{sy(3):.0f}' {qstyle}>{_esc(bl)}</text>"
                 f"<text x='{sx(98):.0f}' y='{sy(3):.0f}' text-anchor='end' {qstyle}>{_esc(br)}</text>")
    # axis labels
    parts.append(f"<text x='{(pad_l + width - pad_r) / 2:.0f}' y='{height - 10}' text-anchor='middle' "
                 f"style='font-size:12px;fill:{INK}'>{_esc(x_label)} →</text>")
    parts.append(f"<text x='14' y='{(pad_t + height - pad_b) / 2:.0f}' text-anchor='middle' "
                 f"transform='rotate(-90 14 {(pad_t + height - pad_b) / 2:.0f})' "
                 f"style='font-size:12px;fill:{INK}'>{_esc(y_label)} →</text>")
    # points; nudge labels only when another label is actually nearby
    used = []  # (x, y) of placed labels

    def collides(lx, ly):
        return any(abs(lx - ux) < 95 and abs(ly - uy) < 14 for ux, uy in used)

    for x, y, label, color in sorted(points, key=lambda p: -p[1]):
        px, py = sx(x), sy(y)
        anchor = "end" if x > 75 else "start"
        lx = px - 10 if anchor == "end" else px + 10
        # try label positions: beside, above, below, then step down
        for ly in (py + 4, py - 12, py + 18, py + 32, py + 46):
            if not collides(lx, ly):
                break
        used.append((lx, ly))
        parts.append(f"<circle cx='{px:.0f}' cy='{py:.0f}' r='6' fill='{color}' opacity='.85'/>"
                     f"<text x='{lx:.0f}' y='{ly:.0f}' text-anchor='{anchor}' "
                     f"style='font-size:11.5px;fill:{INK}'>{_esc(label)}</text>")
    parts.append("</svg>")
    return "".join(parts)


def annual_bars(annual_totals, width=680, height=200):
    """Bar chart of annual totals; last bar rendered as partial-year."""
    if not annual_totals:
        return ""
    items = sorted(annual_totals.items())
    peak = max(v for _, v in items) or 1
    pad = 32
    bw = (width - pad * 2) / len(items) - 14
    parts = [f"<svg viewBox='0 0 {width} {height}' style='max-width:{width}px;width:100%'>"]
    for i, (yr, v) in enumerate(items):
        bh = (v / peak) * (height - pad * 2)
        x = pad + i * ((width - pad * 2) / len(items))
        y = height - pad - bh
        partial = " opacity='.45'" if i == len(items) - 1 else ""
        parts.append(f"<rect x='{x:.0f}' y='{y:.0f}' width='{bw:.0f}' height='{bh:.0f}' "
                     f"rx='4' fill='{RED}'{partial}/>"
                     f"<text x='{x + bw / 2:.0f}' y='{height - 12}' text-anchor='middle'>{yr}</text>"
                     f"<text x='{x + bw / 2:.0f}' y='{y - 6:.0f}' text-anchor='middle'>{v:,}</text>")
    parts.append("</svg>")
    return "".join(parts)

#!/usr/bin/env python3
"""Render the profile's monochrome SVG artwork with no external dependencies."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'Liberation Mono', monospace"


def text(x, y, content, size=18, fill="#171717", weight=400, family=SANS, extra=""):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-family="{family}" font-size="{size}" font-weight="{weight}" {extra}>{escape(content)}</text>'


def header(dark=False):
    fg, muted, line, border = (
        ("#ededed", "#a3a3a3", "#777777", "#383838")
        if dark else
        ("#171717", "#737373", "#909090", "#dedede")
    )
    return "\n".join([
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="240" viewBox="0 0 1200 240" role="img" aria-labelledby="title desc">',
        '<title id="title">Fanfei Gao — less is more.</title>',
        '<desc id="desc">A minimal monochrome wordmark with three fine contour lines and generous whitespace.</desc>',
        '<style>.compact{display:none}@media(max-width:600px){.wide{display:none}.compact{display:inline}}</style>',
        '<g class="wide">',
        text(24, 42, "FANFEI GAO / @iefnaf", 15, muted, family=MONO, extra='letter-spacing="1"'),
        text(19, 132, "fanfei", 86, fg, 300, extra='letter-spacing="-2"'),
        text(25, 177, "agents · systems · open source", 19, muted, family=MONO),
        text(1176, 42, "less is more.", 16, muted, family=MONO, extra='text-anchor="end"'),
        f'<g fill="none" stroke="{line}" stroke-width="1" vector-effect="non-scaling-stroke">',
        '<path d="M824 164C875 164 876 88 928 88S1008 164 1060 164H1176"/>',
        '<path d="M824 174C887 174 888 104 940 104S1020 174 1072 174H1176"/>',
        '<path d="M824 184C899 184 900 120 952 120S1032 184 1084 184H1176"/>',
        '</g>',
        '</g>',
        '<g class="compact">',
        text(24, 56, "FANFEI GAO / @iefnaf", 32, muted, family=MONO),
        text(15, 177, "fanfei", 144, fg, 300, extra='letter-spacing="-3"'),
        text(1176, 168, "less is more.", 36, muted, family=MONO, extra='text-anchor="end"'),
        '</g>',
        f'<path d="M24 222H1176" fill="none" stroke="{border}" stroke-width="1" vector-effect="non-scaling-stroke"/>',
        '</svg>\n',
    ])


PROJECTS = [
    ("pi-jev", "01", "CONTEXT / ROUTING", "Selective context compaction", "and model routing for Pi.", "routing"),
    ("maskpoint", "02", "CONTEXT / MEMORY", "Portable context compaction", "for coding agents.", "memory"),
    ("norn", "03", "AGENTS / ORCHESTRATION", "Parallel workers. Independent reviews.", "A deterministic runner for GitHub tasks.", "graph"),
    ("pi-usage", "04", "TOOLS / OBSERVABILITY", "Your provider limits, at a glance.", "A /usage command for Pi.", "usage"),
]


def icon(kind, color):
    shapes = {
        "routing": '<path d="M0 12H12L24 0H36M12 12L24 24H36"/><circle cx="0" cy="12" r="3"/><circle cx="36" cy="0" r="3"/><circle cx="36" cy="24" r="3"/>',
        "memory": '<rect x="0" y="0" width="10" height="10" rx="1"/><rect x="17" y="0" width="10" height="10" rx="1"/><rect x="0" y="17" width="10" height="10" rx="1"/><path d="M18 22H28M23 17V27"/>',
        "graph": '<path d="M3 14L19 1L35 14L19 27Z M3 14H35"/><circle cx="3" cy="14" r="3"/><circle cx="19" cy="1" r="3"/><circle cx="35" cy="14" r="3"/><circle cx="19" cy="27" r="3"/>',
        "usage": '<rect x="0" y="17" width="6" height="12" rx="1"/><rect x="12" y="9" width="6" height="20" rx="1"/><rect x="24" y="0" width="6" height="29" rx="1"/>',
    }
    return f'<g transform="translate(518 69)" fill="none" stroke="{color}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">{shapes[kind]}</g>'


def card(project, dark=False):
    name, number, category, line1, line2, kind = project
    border, fg, muted = (
        ("#383838", "#ededed", "#a3a3a3")
        if dark else
        ("#dedede", "#171717", "#656565")
    )
    return "\n".join([
        '<svg xmlns="http://www.w3.org/2000/svg" width="600" height="218" viewBox="0 0 600 218" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(name)}</title>',
        f'<desc id="desc">{escape(line1 + " " + line2)}</desc>',
        f'<rect x=".5" y=".5" width="599" height="209" rx="4" fill="none" stroke="{border}"/>',
        text(26, 34, number + " / " + category, 15, muted, family=MONO),
        text(26, 88, name, 36, fg, 500, extra='letter-spacing="-.5"'),
        icon(kind, muted),
        text(26, 127, line1, 22, muted),
        text(26, 155, line2, 22, muted),
        f'<path d="M26 177H574" stroke="{border}"/>',
        text(26, 199, "TypeScript", 14, muted, family=MONO),
        text(574, 199, "↗", 20, muted, extra='text-anchor="end"'),
        '</svg>\n',
    ])


for theme in ("light", "dark"):
    (ASSETS / f"header-{theme}.svg").write_text(header(dark=theme == "dark"))
    for project in PROJECTS:
        (ASSETS / f"card-{project[0]}-{theme}.svg").write_text(card(project, dark=theme == "dark"))
print(f"Rendered {len(list(ASSETS.glob('*.svg')))} SVGs in {ASSETS}")

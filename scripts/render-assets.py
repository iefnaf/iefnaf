#!/usr/bin/env python3
"""Render the profile's dependency-free SVG artwork."""
from html import escape
from pathlib import Path
import math

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'Liberation Mono', monospace"
LIME = "#c6f58a"


def text(x, y, content, size=18, fill="#edf3e9", weight=400, family=SANS, extra=""):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-family="{family}" font-size="{size}" font-weight="{weight}" {extra}>{escape(content)}</text>'


def globe(cx, cy, scale=1):
    parts = [f'<g transform="translate({cx} {cy}) scale({scale})">']
    parts += [
        '<circle r="174" fill="none" stroke="#304132" stroke-dasharray="2 10"/>',
        '<circle r="150" fill="url(#halo)"/>',
        '<g transform="rotate(-24)">',
        '<circle r="126" fill="none" stroke="#87a76b" stroke-opacity=".7"/>',
    ]
    for rx in (28, 60, 94):
        parts.append(f'<ellipse rx="{rx}" ry="126" fill="none" stroke="#749961" stroke-opacity=".48"/>')
    for ry in (30, 64, 98):
        parts.append(f'<ellipse rx="126" ry="{ry}" fill="none" stroke="#749961" stroke-opacity=".48"/>')
    parts += [
        '<path d="M-126 0H126M0-126V126" fill="none" stroke="#99ba7c" stroke-opacity=".4"/>',
        '<ellipse rx="172" ry="52" fill="none" stroke="#59744a" stroke-width="1.2"/>',
        f'<ellipse class="signal" rx="172" ry="52" fill="none" stroke="{LIME}" stroke-width="2" stroke-dasharray="26 740"/>',
        '</g>',
    ]
    for i, angle in enumerate((30, 95, 168, 225, 282, 332)):
        r = (126, 174, 126, 150, 174, 126)[i]
        x, y = round(math.cos(math.radians(angle)) * r, 2), round(math.sin(math.radians(angle)) * r, 2)
        parts += [f'<circle cx="{x}" cy="{y}" r="{3 if i % 2 else 4}" fill="{LIME if i % 2 == 0 else "#87a76b"}"/>']
    parts += [
        f'<rect x="-7" y="-7" width="14" height="14" rx="3" fill="{LIME}" transform="rotate(45)"/>',
        '<path d="M-9-185H9M0-194V-176M-9 185H9M0 176V194" stroke="#668155"/>',
        '</g>',
    ]
    return "\n".join(parts)


def hero(mobile=False):
    width, height = (720, 480) if mobile else (1200, 420)
    title = "Fanfei Gao — agent harnesses, context engineering, open source. Less is more."
    parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{title}</title>
<desc id="desc">A green wireframe globe with a slowly moving signal, beside Fanfei's name on a charcoal terminal-inspired background.</desc>
<defs>
  <radialGradient id="halo"><stop stop-color="#a5e876" stop-opacity=".10"/><stop offset="1" stop-color="#a5e876" stop-opacity="0"/></radialGradient>
  <linearGradient id="bg" x2="1" y2="1"><stop stop-color="#101912"/><stop offset="1" stop-color="#0b110e"/></linearGradient>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#8db776" stroke-opacity=".045"/></pattern>
  <clipPath id="frame"><rect width="{width}" height="{height}" rx="18"/></clipPath>
</defs>
<style>
  .signal {{ animation: travel 22s linear infinite; }}
  .cursor {{ animation: breathe 3s ease-in-out infinite; }}
  @keyframes travel {{ to {{ stroke-dashoffset: -766; }} }}
  @keyframes breathe {{ 0%,100% {{ opacity: .3; }} 50% {{ opacity: 1; }} }}
  @media (prefers-reduced-motion: reduce) {{ .signal,.cursor {{ animation: none; }} }}
</style>
<g clip-path="url(#frame)">
<rect width="{width}" height="{height}" fill="url(#bg)"/>
<rect width="{width}" height="{height}" fill="url(#grid)"/>
<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="17.5" fill="none" stroke="#30402c"/>
''']
    if mobile:
        parts += [
            '<circle cx="40" cy="42" r="5" fill="#c6f58a"/>',
            text(57, 48, "iefnaf@github:~", 18, "#b8c6b0", family=MONO),
            globe(583, 230, .73),
            text(40, 148, "hi, i'm", 28, "#a4b29c"),
            text(33, 253, "fanfei.", 112, "#edf3e9", 700, extra='letter-spacing="-5"').replace("fanfei.", f'fanfei<tspan fill="{LIME}">.</tspan>'),
            text(40, 311, "less is more.", 26, LIME, family=MONO),
            '<rect class="cursor" x="260" y="292" width="12" height="23" rx="1" fill="#c6f58a"/>',
            '<path d="M40 373H680" stroke="#30402c"/>',
            text(40, 413, "AGENT HARNESSES / CONTEXT / OPEN SOURCE", 18, "#b5c5aa", family=MONO),
            text(40, 449, "BEIJING · Z.AI", 17, "#809573", family=MONO),
        ]
    else:
        parts += [
            '<circle cx="54" cy="46" r="4" fill="#c6f58a"/>',
            text(68, 52, "iefnaf@github:~", 16, "#b8c6b0", family=MONO),
            text(1146, 52, "BEIJING · Z.AI", 15, "#8ba47d", family=MONO, extra='text-anchor="end"'),
            text(54, 133, "hi, i'm", 27, "#a4b29c"),
            text(45, 254, "fanfei.", 132, "#edf3e9", 700, extra='letter-spacing="-6"').replace("fanfei.", f'fanfei<tspan fill="{LIME}">.</tspan>'),
            text(54, 309, "less is more.", 25, LIME, family=MONO),
            '<rect class="cursor" x="266" y="290" width="12" height="23" rx="1" fill="#c6f58a"/>',
            globe(934, 203, .81),
            '<path d="M54 355H1146" stroke="#30402c"/>',
            text(54, 391, "AGENT HARNESSES / CONTEXT ENGINEERING / OPEN SOURCE", 16, "#b5c5aa", family=MONO),
            text(1146, 391, "KEEP WHAT MATTERS ↗", 15, "#8ba47d", family=MONO, extra='text-anchor="end"'),
        ]
    parts += ['</g></svg>']
    return "\n".join(parts) + "\n"


PROJECTS = [
    ("pi-jev", "01", "CONTEXT / ROUTING", "Selective context compaction", "and model routing for Pi.", "routing"),
    ("maskpoint", "02", "CONTEXT / MEMORY", "Portable context compaction", "for coding agents.", "memory"),
    ("norn", "03", "AGENTS / ORCHESTRATION", "Parallel workers. Independent reviews.", "A deterministic runner for GitHub tasks.", "graph"),
    ("pi-usage", "04", "TOOLS / OBSERVABILITY", "Your provider limits, at a glance.", "A /usage command for Pi.", "usage"),
]


def icon(kind, accent):
    shapes = {
        "routing": '<path d="M0 12H12L24 0H36M12 12L24 24H36"/><circle cx="0" cy="12" r="3"/><circle cx="36" cy="0" r="3"/><circle cx="36" cy="24" r="3"/>',
        "memory": '<rect x="0" y="0" width="10" height="10" rx="2"/><rect x="17" y="0" width="10" height="10" rx="2"/><rect x="0" y="17" width="10" height="10" rx="2"/><path d="M18 22H28M23 17V27"/>',
        "graph": '<path d="M3 14L19 1L35 14L19 27Z M3 14H35"/><circle cx="3" cy="14" r="3"/><circle cx="19" cy="1" r="3"/><circle cx="35" cy="14" r="3"/><circle cx="19" cy="27" r="3"/>',
        "usage": '<rect x="0" y="17" width="6" height="12" rx="2"/><rect x="12" y="9" width="6" height="20" rx="2"/><rect x="24" y="0" width="6" height="29" rx="2"/>',
    }
    return f'<g transform="translate(518 69)" fill="none" stroke="{accent}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{shapes[kind]}</g>'


def card(project, dark=False):
    name, number, category, line1, line2, kind = project
    bg, border, fg, muted, accent = (
        ("#111a15", "#303e32", "#e5eddf", "#a1b29a", LIME)
        if dark else
        ("#f8faf6", "#dce5d6", "#202e23", "#52634e", "#527d29")
    )
    return "\n".join([
        '<svg xmlns="http://www.w3.org/2000/svg" width="600" height="218" viewBox="0 0 600 218" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(name)}</title>',
        f'<desc id="desc">{escape(line1 + " " + line2)}</desc>',
        f'<rect x=".5" y=".5" width="599" height="209" rx="12" fill="{bg}" stroke="{border}"/>',
        text(26, 34, number + " / " + category, 15, muted, family=MONO),
        text(26, 88, name, 36, fg, 650, extra='letter-spacing="-1"'),
        icon(kind, accent),
        text(26, 127, line1, 22, muted),
        text(26, 155, line2, 22, muted),
        f'<path d="M26 177H574" stroke="{border}"/>',
        f'<circle cx="30" cy="194" r="3" fill="{accent}"/>',
        text(41, 199, "TypeScript", 14, muted, family=MONO),
        text(574, 199, "EXPLORE ↗", 14, accent, family=MONO, extra='text-anchor="end"'),
        '</svg>\n',
    ])


(ASSETS / "hero.svg").write_text(hero())
(ASSETS / "hero-mobile.svg").write_text(hero(mobile=True))
for project in PROJECTS:
    for theme in ("light", "dark"):
        (ASSETS / f"{project[0]}-{theme}.svg").write_text(card(project, dark=theme == "dark"))
print(f"Rendered {len(list(ASSETS.glob('*.svg')))} SVGs in {ASSETS}")

"""Writes profile/banner-light.svg and profile/banner-dark.svg (the org page's "Coming soon" block).

Layout follows the proxify-dev org banners: transparent background, title block on the left,
a dotted field with a window on the right. Logos are the brand PNGs in assets/, embedded.
Run: python3 scripts/make_banner.py
"""
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
W, H = 1280, 320
FONT = "Inter, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
THEMES = {
    # light banner sits on GitHub's white page: dark logo; dark banner on GitHub dark: light logo
    "light": {"logo": "proxify-logo-dark.png", "fg": "#15172F", "dot": "#5258FB", "dot_op": 0.4,
              "win": "#F4F5F7", "win_line": "#D0D5DD", "lights": "#D0D5DD", "cursor": "#15172F", "bar": "#5258FB"},
    "dark": {"logo": "proxify-logo-light.png", "fg": "#FFFFFF", "dot": "#6369FF", "dot_op": 0.55,
             "win": "#1D2939", "win_line": "#1D2939", "lights": "#475467", "cursor": "#FFFFFF", "bar": "#999AFD"},
}


def dots(t):
    out = []
    for x in range(560, 1270, 24):
        for y in range(8, 312, 24):
            if 596 <= x <= 1244 and 36 <= y <= 284:  # hidden behind the window
                continue
            out.append(f'<circle cx="{x}" cy="{y}" r="1.6"/>')
    return f'<g fill="{t["dot"]}" fill-opacity="{t["dot_op"]}">{"".join(out)}</g>'


def banner(t):
    logo = base64.b64encode((ROOT / "assets" / t["logo"]).read_bytes()).decode()
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Proxify Hackathons. Coming soon">
  {dots(t)}
  <rect x="600" y="40" width="640" height="240" rx="12" fill="{t['win']}" stroke="{t['win_line']}" stroke-width="1"/>
  <g fill="{t['lights']}"><circle cx="620" cy="58" r="5"/><circle cx="638" cy="58" r="5"/><circle cx="656" cy="58" r="5"/></g>
  <rect x="624" y="88" width="10" height="20" fill="{t['cursor']}"><animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1.1s" repeatCount="indefinite"/></rect>
  <image x="56" y="76" width="200" height="48" href="data:image/png;base64,{logo}" xlink:href="data:image/png;base64,{logo}"/>
  <g font-family="{FONT}">
    <text x="53" y="222" font-size="80" font-weight="500" letter-spacing="-1.5" fill="{t['fg']}">Coming soon</text>
  </g>
  <rect x="56" y="250" width="96" height="4" rx="2" fill="{t['bar']}"/>
</svg>
"""


for name, theme in THEMES.items():
    path = ROOT / "profile" / f"banner-{name}.svg"
    path.write_text(banner(theme))
    print("wrote", path)

"""Writes profile/banner-light.svg and profile/banner-dark.svg (the org page's "Coming soon" block).

Brand combos from the Proxify brand file: Soft (light) and Hero (dark). Run: python3 scripts/make_banner.py
"""
from pathlib import Path

MARK = [
    "M39.1938 78.3876C60.8415 78.3876 78.3876 60.8359 78.3876 39.1938C78.3876 17.5517 60.8415 0 39.1938 0C17.5461 0 0 17.5517 0 39.1938C0 60.8359 17.5461 78.3876 39.1938 78.3876Z",
    "M82.3179 9.79611C85.2571 44.8074 113.176 72.7425 148.204 75.6822C151.574 75.9651 154.326 73.1962 154.326 69.8139V9.79845C154.326 6.41624 151.584 3.67442 148.202 3.67442H88.186C84.8038 3.67442 82.0349 6.42576 82.3179 9.79611Z",
    "M158 118.8C158 140.451 140.454 158 118.806 158C97.1585 158 79.6124 140.439 79.6124 118.8C79.6124 97.1613 97.1585 79.6124 118.806 79.6124C140.454 79.6124 158 97.1489 158 118.8Z",
    "M10.4109 87.5736C7.02864 87.5736 4.28682 90.3155 4.28682 93.6977V147.589C4.28682 150.971 7.02864 153.713 10.4109 153.713H64.3023C67.6845 153.713 70.4264 150.971 70.4264 147.589V93.6977C70.4264 90.3155 67.6845 87.5736 64.3023 87.5736H10.4109Z",
]
THEMES = {
    "light": {"bg": "#F4F5F7", "border": "#EAECF0", "fg": "#15172F", "accent": "#5258FB", "muted": "#475467", "deco": 0.10},
    "dark": {"bg": "#15172F", "border": "#262841", "fg": "#FFFFFF", "accent": "#999AFD", "muted": "#D0D5DD", "deco": 0.16},
}
FONT = "Inter, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
W, H = 1280, 360


def mark(x, y, size, fill, opacity=1.0):
    s = size / 158
    paths = "".join(f'<path d="{d}"/>' for d in MARK)
    return f'<g transform="translate({x} {y}) scale({s:.4f})" fill="{fill}" fill-opacity="{opacity}">{paths}</g>'


def banner(t):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Proxify Hackathons. Coming soon">
  <defs><clipPath id="c"><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="20"/></clipPath></defs>
  <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="20" fill="{t['bg']}" stroke="{t['border']}" stroke-width="2"/>
  <g clip-path="url(#c)">{mark(860, 30, 440, t['accent'], t['deco'])}</g>
  {mark(72, 72, 56, t['fg'])}
  <g font-family="{FONT}">
    <text x="144" y="109" font-size="22" font-weight="600" fill="{t['fg']}">Proxify Hackathons</text>
    <text x="68" y="248" font-size="104" font-weight="600" letter-spacing="-3" fill="{t['fg']}">Coming soon</text>
    <rect x="72" y="282" width="120" height="6" rx="3" fill="{t['accent']}"/>
  </g>
</svg>
"""


out = Path(__file__).resolve().parent.parent / "profile"
for name, theme in THEMES.items():
    (out / f"banner-{name}.svg").write_text(banner(theme))
    print("wrote", out / f"banner-{name}.svg")

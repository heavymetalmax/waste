#!/usr/bin/env python3
# encoding: utf-8
"""Add orbital concentric arcs around the tech hero stat panel."""
import pathlib, re

ROOT = pathlib.Path('/Users/max/Waste')
TECH = ROOT / 'biotc/technology.html'
CSS  = ROOT / 'styles.css'

# ── SVG orbital rings (inserted inside .tech-stat-panel, before the grid) ──
ORBITAL_SVG = '''\
            <div class="tech-orbital-rings" aria-hidden="true">
              <svg viewBox="0 0 480 480" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- arc 1: largest, teal, thin, 50s clockwise -->
                <circle class="t-arc t-arc-1" cx="240" cy="240" r="228"
                        stroke="#0D9488" stroke-width="1.5"
                        stroke-dasharray="1100 332" stroke-linecap="round"/>
                <!-- arc 2: blue, medium, 28s counter-clockwise -->
                <circle class="t-arc t-arc-2" cx="240" cy="240" r="192"
                        stroke="#046BD2" stroke-width="3"
                        stroke-dasharray="680 526" stroke-linecap="round"/>
                <!-- arc 3: light blue, thin, 18s clockwise -->
                <circle class="t-arc t-arc-3" cx="240" cy="240" r="156"
                        stroke="#38BDF8" stroke-width="1"
                        stroke-dasharray="530 451" stroke-linecap="round"/>
                <!-- arc 4: teal, thick, 60s counter-clockwise -->
                <circle class="t-arc t-arc-4" cx="240" cy="240" r="118"
                        stroke="#2DD4BF" stroke-width="4"
                        stroke-dasharray="290 451" stroke-linecap="round"/>
                <!-- arc 5: accent, thin, 13s clockwise, fastest -->
                <circle class="t-arc t-arc-5" cx="240" cy="240" r="80"
                        stroke="#046BD2" stroke-width="1.5"
                        stroke-dasharray="210 292" stroke-linecap="round"
                        opacity="0.6"/>
              </svg>
            </div>
'''

# insert before the tech-stat-grid div
OLD = '            <div class="tech-stat-grid">'
NEW = ORBITAL_SVG + '            <div class="tech-stat-grid">'

# ── CSS ──────────────────────────────────────────────────────────────────────
ORBITAL_CSS = '''
/* Orbital rings around tech hero stat panel */
.tech-stat-panel {
  position: relative;
}

.tech-stat-grid,
.tech-stat-note {
  position: relative;
  z-index: 1;
}

.tech-orbital-rings {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 480px;
  height: 480px;
  pointer-events: none;
  z-index: 0;
}

.tech-orbital-rings svg {
  width: 100%;
  height: 100%;
  overflow: visible;
}

.t-arc {
  transform-box: fill-box;
  transform-origin: center;
}

.t-arc-1 { animation: t-orbit-cw  50s linear infinite; }
.t-arc-2 { animation: t-orbit-ccw 28s linear infinite; }
.t-arc-3 { animation: t-orbit-cw  18s linear infinite; }
.t-arc-4 { animation: t-orbit-ccw 60s linear infinite; }
.t-arc-5 { animation: t-orbit-cw  13s linear infinite; }

@keyframes t-orbit-cw  { to { transform: rotate( 360deg); } }
@keyframes t-orbit-ccw { to { transform: rotate(-360deg); } }
'''

# ── patch ─────────────────────────────────────────────────────────────────────
def patch_html(path):
    src = path.read_text(encoding='utf-8')
    if 'tech-orbital-rings' in src:
        print(f'  {path.name}: already present')
        return
    if OLD not in src:
        print(f'  {path.name}: marker not found!')
        return
    path.write_text(src.replace(OLD, NEW, 1), encoding='utf-8')
    print(f'  {path.name}: orbital rings added')

def patch_css(path):
    src = path.read_text(encoding='utf-8')
    if 't-arc-1' in src:
        print(f'  {path.name}: CSS already present')
        return
    path.write_text(src + ORBITAL_CSS, encoding='utf-8')
    print(f'  {path.name}: CSS added')

print('Patching technology.html ...')
patch_html(TECH)

print('Patching styles.css ...')
patch_css(CSS)

print('Done.')

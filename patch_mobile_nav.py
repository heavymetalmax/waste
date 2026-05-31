#!/usr/bin/env python3
# encoding: utf-8
"""
1. Move mobile-toggle out of header-actions (→ direct child of header-container)
2. Add nav-mobile-strip inside <header> for each template
3. CSS: center burger on mobile, strip styles
4. JS: toggle strip instead of full-screen nav
"""
import pathlib, re

ROOT = pathlib.Path('/Users/max/Waste')
CSS  = ROOT / 'styles.css'
JS   = ROOT / 'app.js'

TOGGLE_HTML = '''\
        <button class="mobile-toggle" aria-label="{{header.mobile.toggle}}" aria-expanded="false" aria-controls="nav-mobile-strip">
          <span class="bar"></span><span class="bar"></span><span class="bar"></span>
        </button>'''

# page-specific strip nav links
STRIP_LINKS = {
    'index.html': (
        '<a href="index.html" class="active">{{header.nav.home}}</a>',
        '<a href="technology.html">{{header.nav.technology}}</a>',
        '<a href="simulator.html">{{header.nav.calculator}}</a>',
    ),
    'technology.html': (
        '<a href="index.html">{{header.nav.home}}</a>',
        '<a href="technology.html" class="active">{{header.nav.technology}}</a>',
        '<a href="simulator.html">{{header.nav.calculator}}</a>',
    ),
    'simulator.html': (
        '<a href="index.html">{{header.nav.home}}</a>',
        '<a href="technology.html">{{header.nav.technology}}</a>',
        '<a href="simulator.html" class="active">{{header.nav.calculator}}</a>',
    ),
}

def strip_html(links):
    a, b, c = links
    return f'''\

    <div class="nav-mobile-strip" id="nav-mobile-strip" aria-hidden="true">
      <div class="nav-mobile-strip-inner">
        <ul>
          <li>{a}</li>
          <li>{b}</li>
          <li>{c}</li>
        </ul>
      </div>
    </div>'''

# ── CSS additions ────────────────────────────────────────────────────────────
MOBILE_CSS = '''
/* Mobile strip nav */
.nav-mobile-strip {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  z-index: 99;
  background: var(--color-bg);
  border-bottom: 1px solid var(--color-border);
  box-shadow: 0 6px 16px rgba(15, 23, 42, 0.08);
  transform: translateY(-8px);
  opacity: 0;
  visibility: hidden;
  transition: transform 0.22s ease, opacity 0.18s ease, visibility 0s 0.22s;
}
.nav-mobile-strip.open {
  transform: translateY(0);
  opacity: 1;
  visibility: visible;
  transition-delay: 0s;
}
.nav-mobile-strip-inner {
  padding: 0.75rem var(--space-md);
  display: flex;
  justify-content: center;
}
.nav-mobile-strip ul {
  display: flex;
  gap: 0.2rem;
  align-items: center;
  list-style: none;
  border: 1.5px solid rgba(4, 107, 210, 0.28);
  border-radius: 9999px;
  padding: 0.3rem;
}
.nav-mobile-strip a {
  display: inline-block;
  font-size: var(--text-sm);
  font-weight: 600;
  color: var(--color-text-muted);
  padding: 0.42rem 1rem;
  border-radius: 9999px;
  white-space: nowrap;
  text-decoration: none;
  transition: color 0.15s, background 0.15s;
}
.nav-mobile-strip a:hover { color: var(--color-text); }
.nav-mobile-strip a.active {
  background: var(--color-accent);
  color: #fff;
  font-weight: 700;
}

/* Center hamburger on mobile */
@media (max-width: 640px) {
  .mobile-toggle {
    display: flex;
    grid-column: 2;
    justify-self: center;
  }
  .nav-desktop { display: none; }
  .header-actions { grid-column: 3; }
}
'''

# ── JS fragment ──────────────────────────────────────────────────────────────
NEW_TOGGLE_JS = '''
  // --- Mobile nav strip (replaces full-screen overlay) ---
  const mobileToggle2 = document.querySelector('.mobile-toggle');
  const mobileStrip   = document.getElementById('nav-mobile-strip');
  if (mobileToggle2 && mobileStrip) {
    mobileToggle2.addEventListener('click', (e) => {
      e.stopPropagation();
      const open = mobileStrip.classList.toggle('open');
      mobileStrip.setAttribute('aria-hidden', String(!open));
      mobileToggle2.setAttribute('aria-expanded', String(open));
    });
    document.addEventListener('click', () => {
      mobileStrip.classList.remove('open');
      mobileStrip.setAttribute('aria-hidden', 'true');
      mobileToggle2.setAttribute('aria-expanded', 'false');
    });
  }
'''

# ── patch ─────────────────────────────────────────────────────────────────────
def patch_template(fname):
    path = ROOT / 'biotc' / fname
    src  = path.read_text(encoding='utf-8')

    # 1. Remove mobile-toggle from inside header-actions
    src = re.sub(
        r'\s*<button class="mobile-toggle".*?</button>',
        '', src, count=1, flags=re.DOTALL
    )

    # 2. Add mobile-toggle as direct child of header-container, after header-actions
    src = src.replace(
        '      </div>\n    </div>\n  </header>',
        '      </div>\n' + TOGGLE_HTML + '\n    </div>\n  </header>'
    )

    # 3. Add nav-mobile-strip inside <header> before </header>
    if 'nav-mobile-strip' not in src:
        src = src.replace(
            '\n  </header>',
            strip_html(STRIP_LINKS[fname]) + '\n  </header>'
        )

    path.write_text(src, encoding='utf-8')
    print(f'  {fname}: patched')

print('Patching templates ...')
for f in ['index.html', 'technology.html', 'simulator.html']:
    patch_template(f)

print('Patching CSS ...')
css = CSS.read_text(encoding='utf-8')
if 'nav-mobile-strip' not in css:
    CSS.write_text(css + MOBILE_CSS, encoding='utf-8')
    print('  styles.css: CSS added')

print('Patching JS ...')
js = JS.read_text(encoding='utf-8')
if 'mobileStrip' not in js:
    js = js.rstrip()
    JS.write_text(js[:-3] + NEW_TOGGLE_JS + '\n});', encoding='utf-8')
    print('  app.js: JS patched')

print('Done.')

#!/usr/bin/env python3
# encoding: utf-8
"""
1. Restore pill nav border
2. Remove lang-switcher flags from header-actions
3. Add globe button between logo and nav
4. Add lang-strip inside header (slides below on click)
5. Wire JS toggle in app.js
"""
import pathlib, re

ROOT = pathlib.Path('/Users/max/Waste')
CSS  = ROOT / 'styles.css'
JS   = ROOT / 'app.js'

# page → (url_ua, url_pl, url_eu)
PAGE_URLS = {
    'index.html':      ('{{lang.ua.url}}',      '{{lang.pl.url}}',      '{{lang.eu.url}}'),
    'simulator.html':  ('{{lang.ua.sim.url}}',   '{{lang.pl.sim.url}}',  '{{lang.eu.sim.url}}'),
    'technology.html': ('{{lang.ua.tech.url}}',  '{{lang.pl.tech.url}}', '{{lang.eu.tech.url}}'),
}

GLOBE_BTN = '''\

      <button class="lang-globe-btn" id="lang-globe-btn" aria-label="Language">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"/>
          <path d="M2 12h20"/>
          <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
        </svg>
      </button>
'''

def lang_strip(ua_url, pl_url, eu_url):
    return f'''\

    <div class="lang-strip" id="lang-strip" aria-hidden="true">
      <div class="lang-strip-inner">
        <a href="{ua_url}" class="lang-strip-item {{{{lang.ua.class}}}}">&#x1F1FA;&#x1F1E6; Українська</a>
        <a href="{pl_url}" class="lang-strip-item {{{{lang.pl.class}}}}">&#x1F1F5;&#x1F1F1; Polski</a>
        <a href="{eu_url}" class="lang-strip-item {{{{lang.eu.class}}}}">&#x1F1EA;&#x1F1FA; English</a>
      </div>
    </div>
'''

# ── patch each template ──────────────────────────────────────────────────────
for fname, (ua, pl, eu) in PAGE_URLS.items():
    path = ROOT / 'biotc' / fname
    src  = open(path, encoding='utf-8').read()

    # 1. Remove lang-switcher div (flag buttons)
    src = re.sub(
        r'\s*<div class="lang-switcher">.*?</div>\n',
        '\n', src, flags=re.DOTALL
    )

    # 2. Insert globe button after logo closing </a>, before <nav class="nav-desktop">
    src = src.replace(
        '\n      <nav class="nav-desktop"',
        GLOBE_BTN + '      <nav class="nav-desktop"'
    )

    # 3. Insert lang-strip before </header>
    if 'lang-strip' not in src:
        src = src.replace('  </header>', lang_strip(ua, pl, eu) + '  </header>')

    open(path, 'w', encoding='utf-8').write(src)
    print(f'  {fname}: patched')

# ── CSS ──────────────────────────────────────────────────────────────────────
css = open(CSS, encoding='utf-8').read()

# 1. Restore nav border
css = css.replace(
    '  border-radius: 9999px;\n  padding: 0.3rem;\n  list-style: none;',
    '  border: 1px solid rgba(4,107,210,0.18);\n  border-radius: 9999px;\n  padding: 0.3rem;\n  list-style: none;'
)

# 2. Add globe + strip CSS if not present
if 'lang-globe-btn' not in css:
    css += '''
/* Globe lang switcher */
.lang-globe-btn {
  background: none;
  border: none;
  cursor: pointer;
  color: var(--color-text-muted);
  display: flex;
  align-items: center;
  padding: 0.3rem;
  border-radius: 6px;
  transition: color 0.15s;
  flex-shrink: 0;
}
.lang-globe-btn:hover { color: var(--color-accent); }
.lang-globe-btn svg { width: 18px; height: 18px; }

/* Language strip */
.lang-strip {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  z-index: 98;
  background: var(--color-bg);
  border-bottom: 1px solid var(--color-border);
  box-shadow: 0 6px 16px rgba(15,23,42,0.08);
  transform: translateY(-8px);
  opacity: 0;
  visibility: hidden;
  transition: transform 0.22s ease, opacity 0.18s ease, visibility 0s 0.22s;
}
.lang-strip.open {
  transform: translateY(0);
  opacity: 1;
  visibility: visible;
  transition-delay: 0s;
}
.lang-strip-inner {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2.5rem;
  padding: 0.85rem var(--space-md);
  max-width: 1200px;
  margin-inline: auto;
}
.lang-strip-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--color-text-muted);
  text-decoration: none;
  padding: 0.35rem 0.8rem;
  border-radius: 6px;
  transition: color 0.15s, background 0.15s;
}
.lang-strip-item:hover { color: var(--color-accent); background: var(--color-accent-glow); }
.lang-strip-item.active { color: var(--color-accent); font-weight: 700; }
'''

open(CSS, 'w', encoding='utf-8').write(css)
print(f'  styles.css: patched')

# ── JS ───────────────────────────────────────────────────────────────────────
js = open(JS, encoding='utf-8').read()
if 'lang-globe-btn' not in js:
    globe_js = '''
  // --- Globe language strip toggle ---
  const globeBtn = document.getElementById('lang-globe-btn');
  const langStrip = document.getElementById('lang-strip');
  if (globeBtn && langStrip) {
    globeBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const open = langStrip.classList.toggle('open');
      langStrip.setAttribute('aria-hidden', String(!open));
      globeBtn.setAttribute('aria-expanded', String(open));
    });
    document.addEventListener('click', () => {
      langStrip.classList.remove('open');
      langStrip.setAttribute('aria-hidden', 'true');
      globeBtn.setAttribute('aria-expanded', 'false');
    });
  }
'''
    js = js.rstrip()
    if js.endswith('});'):
        js = js[:-3] + globe_js + '\n});'
    else:
        js += globe_js
    open(JS, 'w', encoding='utf-8').write(js)
    print(f'  app.js: patched')

print('Done.')

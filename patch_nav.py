#!/usr/bin/env python3
# encoding: utf-8
"""
1. Remove duplicate home nav links in all 3 templates
2. Replace CTA anchor with cycling FAB button (phone/mail/chat)
3. Pill nav: transparent container
"""
import pathlib, re

ROOT = pathlib.Path('/Users/max/Waste')
TEMPLATES = [ROOT / 'biotc/index.html',
             ROOT / 'biotc/technology.html',
             ROOT / 'biotc/simulator.html']
CSS  = ROOT / 'styles.css'
JS   = ROOT / 'app.js'

# ── FAB button HTML (replaces nav-cta-btn) ──────────────────────────────────
FAB_HTML = '''\
<button class="nav-fab" id="nav-fab" aria-label="{{header.nav.cta}}">
          <svg class="nav-fab-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.11 12 19.79 19.79 0 0 1 1.08 3.38 2 2 0 0 1 3.07 1.22h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <svg class="nav-fab-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="display:none"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
          <svg class="nav-fab-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="display:none"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22z"/></svg>
        </button>'''

OLD_CTA = '        <a href="#contact" class="btn btn-primary nav-cta-btn">{{header.nav.cta}}</a>'

# ── CSS additions ────────────────────────────────────────────────────────────
NAV_FAB_CSS = '''
/* Cycling contact FAB in header */
.nav-fab {
  flex-shrink: 0;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: var(--color-accent);
  color: #fff;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.2s, box-shadow 0.2s;
  padding: 0;
}

.nav-fab:hover {
  transform: scale(1.09);
  box-shadow: 0 4px 14px rgba(4, 107, 210, 0.38);
}

.nav-fab-icon {
  width: 18px;
  height: 18px;
  transition: opacity 0.25s;
}
'''

# ── JS addition ──────────────────────────────────────────────────────────────
FAB_JS = '''
  // --- Cycling FAB (phone / mail / chat) ---
  const fab = document.getElementById('nav-fab');
  if (fab) {
    // Navigate to contact section or contact page
    fab.addEventListener('click', () => {
      const contact = document.getElementById('contact');
      if (contact) {
        contact.scrollIntoView({ behavior: 'smooth' });
      } else {
        window.location.href = 'index.html#contact';
      }
    });
    // Cycle icons
    const fabIcons = fab.querySelectorAll('.nav-fab-icon');
    let fabIdx = 0;
    setInterval(() => {
      fabIcons[fabIdx].style.opacity = '0';
      setTimeout(() => {
        fabIcons[fabIdx].style.display = 'none';
        fabIdx = (fabIdx + 1) % fabIcons.length;
        fabIcons[fabIdx].style.display = '';
        fabIcons[fabIdx].style.opacity = '0';
        requestAnimationFrame(() => { fabIcons[fabIdx].style.opacity = '1'; });
      }, 250);
    }, 2500);
  }
'''

# ── patch templates ──────────────────────────────────────────────────────────
def patch_template(path):
    src = open(path, encoding='utf-8').read()

    # 1. Remove duplicate home link (keep first, remove second identical line)
    # Pattern: two consecutive identical <li><a href="index.html"...> lines
    dup_active = ('          <li><a href="index.html" class="active">{{header.nav.home}}</a></li>\n'
                  '          <li><a href="index.html" class="active">{{header.nav.home}}</a></li>')
    src = src.replace(dup_active,
                      '          <li><a href="index.html" class="active">{{header.nav.home}}</a></li>')

    dup_plain = ('          <li><a href="index.html">{{header.nav.home}}</a></li>\n'
                 '          <li><a href="index.html">{{header.nav.home}}</a></li>')
    src = src.replace(dup_plain,
                      '          <li><a href="index.html">{{header.nav.home}}</a></li>')

    # 2. Replace CTA with FAB
    if OLD_CTA in src:
        src = src.replace(OLD_CTA, FAB_HTML)

    open(path, 'w', encoding='utf-8').write(src)
    print(f'  {path.name}: patched')

# ── patch CSS: transparent pill nav container ────────────────────────────────
def patch_css(path):
    src = open(path, encoding='utf-8').read()

    # Remove background + border from .nav-desktop ul
    old = ('  background: rgba(4, 107, 210, 0.07);\n'
           '  border: 1px solid rgba(4, 107, 210, 0.13);\n'
           '  border-radius: 9999px;\n'
           '  padding: 0.3rem;')
    new = ('  border-radius: 9999px;\n'
           '  padding: 0.3rem;')
    src = src.replace(old, new)

    # Remove .nav-cta-btn { display: none; } from 1024px since button is gone
    src = src.replace(
        '  /* Hide CTA button on tablets to give pill nav more room */\n  .nav-cta-btn { display: none; }\n',
        ''
    )

    # Append FAB CSS
    if 'nav-fab' not in src:
        src += NAV_FAB_CSS

    open(path, 'w', encoding='utf-8').write(src)
    print(f'  {path.name}: CSS patched')

# ── patch app.js ─────────────────────────────────────────────────────────────
def patch_js(path):
    src = open(path, encoding='utf-8').read()
    if 'nav-fab' not in src:
        # Insert before closing });
        src = src.rstrip()
        if src.endswith('});'):
            src = src[:-3] + FAB_JS + '\n});'
        else:
            src += FAB_JS
    open(path, 'w', encoding='utf-8').write(src)
    print(f'  {path.name}: JS patched')

print('Patching templates ...')
for t in TEMPLATES:
    patch_template(t)

print('Patching CSS ...')
patch_css(CSS)

print('Patching JS ...')
patch_js(JS)

print('Done.')

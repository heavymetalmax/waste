#!/usr/bin/env python3
# encoding: utf-8
"""
1. Footer: copyright left, privacy button right (flex row)
2. Remove <dialog> privacy modal from all templates
3. Add blue bottom strip that slides up on click
4. Wire JS in app.js
"""
import pathlib, re

ROOT = pathlib.Path('/Users/max/Waste')
TEMPLATES = [ROOT / 'biotc/index.html',
             ROOT / 'biotc/technology.html',
             ROOT / 'biotc/simulator.html']
CSS = ROOT / 'styles.css'
JS  = ROOT / 'app.js'

# ── new footer-copy row (copyright left, privacy right) ─────────────────────
# replaces <p class="footer-copy">...</p>  AND  <dialog ...>...</dialog>

def new_footer_copy():
    return '''\
      <div class="footer-copy">
        <span>{{footer.copy}}</span>
        <button class="footer-privacy-btn" id="privacy-strip-trigger">{{footer.privacy.link}}</button>
      </div>'''

PRIVACY_STRIP = '''\

    <!-- Privacy bottom strip -->
    <div class="privacy-strip" id="privacy-strip" aria-hidden="true">
      <div class="privacy-strip-inner">
        <div class="privacy-strip-body">
          <strong>{{footer.privacy.title}}</strong>
          <p>{{footer.privacy.text}}</p>
        </div>
        <button class="privacy-strip-close" id="privacy-strip-close" aria-label="{{footer.privacy.close}}">&#x2715;</button>
      </div>
    </div>'''

# ── CSS ──────────────────────────────────────────────────────────────────────
PRIVACY_CSS = '''
/* Privacy bottom strip */
.privacy-strip {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 200;
  background: var(--color-accent);
  color: #fff;
  transform: translateY(100%);
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 -4px 20px rgba(4, 107, 210, 0.25);
}
.privacy-strip.open {
  transform: translateY(0);
}
.privacy-strip-inner {
  max-width: 1200px;
  margin-inline: auto;
  padding: 1.1rem var(--space-md);
  display: flex;
  gap: 1.5rem;
  align-items: flex-start;
}
.privacy-strip-body {
  flex: 1;
  font-size: 0.82rem;
  line-height: 1.65;
  opacity: 0.95;
}
.privacy-strip-body strong {
  display: block;
  font-size: 0.875rem;
  font-weight: 700;
  opacity: 1;
  margin-block-end: 0.3rem;
}
.privacy-strip-close {
  flex-shrink: 0;
  background: rgba(255, 255, 255, 0.18);
  border: none;
  color: #fff;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  cursor: pointer;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.15s;
  margin-block-start: 0.15rem;
}
.privacy-strip-close:hover { background: rgba(255, 255, 255, 0.28); }
'''

# ── JS ───────────────────────────────────────────────────────────────────────
PRIVACY_JS = '''
  // --- Privacy bottom strip ---
  const privacyTrigger = document.getElementById('privacy-strip-trigger');
  const privacyStrip   = document.getElementById('privacy-strip');
  const privacyClose   = document.getElementById('privacy-strip-close');
  if (privacyTrigger && privacyStrip) {
    privacyTrigger.addEventListener('click', () => {
      privacyStrip.classList.add('open');
      privacyStrip.setAttribute('aria-hidden', 'false');
      document.body.style.paddingBottom = privacyStrip.offsetHeight + 'px';
    });
    if (privacyClose) {
      privacyClose.addEventListener('click', () => {
        privacyStrip.classList.remove('open');
        privacyStrip.setAttribute('aria-hidden', 'true');
        document.body.style.paddingBottom = '';
      });
    }
  }
'''

# ── patch templates ──────────────────────────────────────────────────────────
def patch_template(path):
    src = open(path, encoding='utf-8').read()

    # 1. Replace <p class="footer-copy">...</p> block
    src = re.sub(
        r'<p class="footer-copy">.*?</p>',
        new_footer_copy(),
        src, flags=re.DOTALL
    )

    # 2. Remove <dialog> modal block
    src = re.sub(
        r'\s*<dialog class="privacy-modal".*?</dialog>',
        '',
        src, flags=re.DOTALL
    )

    # 3. Add privacy strip before </body>
    if 'privacy-strip' not in src:
        src = src.replace('</body>', PRIVACY_STRIP + '\n</body>')

    open(path, 'w', encoding='utf-8').write(src)
    print(f'  {path.name}: patched')

# ── patch CSS ────────────────────────────────────────────────────────────────
def patch_css(path):
    src = open(path, encoding='utf-8').read()

    # Footer-copy → flex row
    src = src.replace(
        '.footer-copy {\n  border-top: 1px solid var(--color-border);\n'
        '  padding-block-start: var(--space-md);\n  font-size: var(--text-xs);\n'
        '  color: var(--color-text-muted);\n}',
        '.footer-copy {\n  border-top: 1px solid var(--color-border);\n'
        '  padding-block-start: var(--space-md);\n  font-size: var(--text-xs);\n'
        '  color: var(--color-text-muted);\n'
        '  display: flex;\n  justify-content: space-between;\n  align-items: center;\n}'
    )

    if 'privacy-strip' not in src:
        src += PRIVACY_CSS

    open(path, 'w', encoding='utf-8').write(src)
    print(f'  {path.name}: CSS patched')

# ── patch JS ─────────────────────────────────────────────────────────────────
def patch_js(path):
    src = open(path, encoding='utf-8').read()
    if 'privacy-strip-trigger' not in src:
        src = src.rstrip()
        src = src[:-3] + PRIVACY_JS + '\n});'
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

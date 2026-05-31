#!/usr/bin/env python3
# encoding: utf-8
"""
1. Remove old mobile-nav (full-screen overlay) from all templates
2. Remove chat-mobile-preview card from simulator.html
3. Fix app.js: old listener is already no-op after removing mobile-nav
4. Add JS: tap chat widget on mobile → navigate to chat.html
5. CSS: show chat widget on mobile (remove display:none), make it pointer:pointer
"""
import pathlib, re

ROOT  = pathlib.Path('/Users/max/Waste')
CSS   = ROOT / 'styles.css'
JS    = ROOT / 'app.js'
BIOTC = ROOT / 'biotc'

# ── 1. Remove old mobile-nav from all templates ──────────────────────────────
for fname in ['index.html', 'technology.html', 'simulator.html']:
    path = BIOTC / fname
    src  = path.read_text(encoding='utf-8')
    # Remove the <nav class="mobile-nav" ...> block
    cleaned = re.sub(
        r'\s*<nav class="mobile-nav".*?</nav>',
        '', src, flags=re.DOTALL
    )
    if cleaned != src:
        path.write_text(cleaned, encoding='utf-8')
        print(f'  {fname}: mobile-nav removed')
    else:
        print(f'  {fname}: mobile-nav not found (already removed?)')

# ── 2. Remove chat-mobile-preview from simulator.html ───────────────────────
sim = BIOTC / 'simulator.html'
src = sim.read_text(encoding='utf-8')
cleaned = re.sub(
    r'\s*<!-- Mobile-only.*?</a>',
    '', src, flags=re.DOTALL
)
if cleaned != src:
    sim.write_text(cleaned, encoding='utf-8')
    print('  simulator.html: chat-mobile-preview removed')
else:
    print('  simulator.html: preview not found')

# ── 3. CSS fixes ─────────────────────────────────────────────────────────────
css = CSS.read_text(encoding='utf-8')

# Show chat widget on mobile (was hidden), just shrink intro
css = css.replace(
    '  .srp-chat-section .srp-col:has(.srp-chat-intro) { display: none; }\n'
    '  .srp-chat-section .srp-col:has(.srp-chat-widget) { width: 100%; }',
    '  .srp-chat-section .srp-col:has(.srp-chat-intro) { display: none; }\n'
    '  .srp-chat-section .srp-col:has(.srp-chat-widget) { width: 100%; }\n'
    '  .srp-chat-section .srp-chat-widget { cursor: pointer; }'
)

CSS.write_text(css, encoding='utf-8')
print('  styles.css: chat widget cursor:pointer on mobile')

# ── 4. JS: tap widget → chat.html + fix old nav conflict ────────────────────
js = JS.read_text(encoding='utf-8')

# The old listener checks `if (mobileToggle && mobileNav)` —
# once mobile-nav is removed from HTML, mobileNav=null → listener never fires.
# Just add the chat redirect logic.

CHAT_REDIRECT_JS = '''
  // --- Mobile: tap chat widget → open full-screen chat page ---
  if (window.matchMedia('(max-width: 640px)').matches) {
    var chatWidget = document.querySelector('.srp-chat-section .srp-chat-widget');
    if (chatWidget) {
      chatWidget.addEventListener('pointerdown', function() {
        window.location.href = 'chat.html';
      });
    }
  }
'''

if 'chat.html' not in js:
    js = js.rstrip()
    JS.write_text(js[:-3] + CHAT_REDIRECT_JS + '\n});', encoding='utf-8')
    print('  app.js: chat redirect added')
else:
    print('  app.js: chat redirect already present')

print('Done.')

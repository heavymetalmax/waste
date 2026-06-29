#!/usr/bin/env python3
# encoding: utf-8
"""Replace complex rfq-form with simple phone + callback button."""
import json, pathlib, re

ROOT  = pathlib.Path('/Users/max/Waste')
CSS   = ROOT / 'styles.css'
JS    = ROOT / 'app.js'
PAGES = ['biotc/index.html', 'biotc/technology.html', 'biotc/simulator.html']

# ── 1. Translation keys ──────────────────────────────────────────────────────
UA_KEYS = {
    'form.callback.label':   'Залиште номер, і ми передзвонимо',
    'form.callback.btn':     'Передзвоніть мені',
    'form.callback.success': 'Дякуємо! Відкрийте email і натисніть «Надіслати».',
    'form.callback.error':   'Введіть коректний номер телефону',
}
PL_KEYS = {
    'form.callback.label':   'Zostaw numer, a oddzwonimy',
    'form.callback.btn':     'Oddzwoń do mnie',
    'form.callback.success': 'Dziękujemy! Otwórz klienta pocztowego i wyślij wiadomość.',
    'form.callback.error':   'Podaj poprawny numer telefonu',
}
EU_KEYS = {
    'form.callback.label':   'Leave your number and we will call you back',
    'form.callback.btn':     'Call me back',
    'form.callback.success': 'Thank you! Open your email client and press Send.',
    'form.callback.error':   'Please enter a valid phone number',
}

for fname, keys in [('ua.json', UA_KEYS), ('pl.json', PL_KEYS), ('eu.json', EU_KEYS)]:
    path = ROOT / 'translations' / fname
    d = json.load(open(path, encoding='utf-8'))
    d.update(keys)
    json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2, sort_keys=True)
    print(f'  {fname}: keys added')

# ── 2. New form HTML ─────────────────────────────────────────────────────────
NEW_FORM = '''\
          <div class="glass-card contact-form-card">
            <form id="callback-form" novalidate>
              <p class="callback-label">{{form.callback.label}}</p>
              <div class="callback-row">
                <input type="tel" id="callback-phone" name="phone"
                       placeholder="{{form.phone.label}}"
                       inputmode="tel" autocomplete="tel"
                       aria-describedby="callback-error">
                <button type="submit" class="btn btn-primary callback-btn">{{form.callback.btn}}</button>
              </div>
              <p id="callback-error" class="error-msg" role="alert" style="display:none">{{form.callback.error}}</p>
              <p class="form-micro-text">{{form.micro}}</p>
            </form>
            <div id="form-status" class="form-status-container hidden" tabindex="-1" role="status" aria-live="polite"></div>
          </div>'''

# Match old form block (from glass-card opening to closing div)
OLD_PATTERN = re.compile(
    r'          <div class="glass-card contact-form-card">.*?</div>\s*</div>',
    re.DOTALL
)

for page in PAGES:
    path = ROOT / page
    src  = path.read_text(encoding='utf-8')
    new, n = OLD_PATTERN.subn(NEW_FORM, src, count=1)
    if n:
        path.write_text(new, encoding='utf-8')
        print(f'  {page}: form replaced')
    else:
        print(f'  {page}: pattern not found')

# ── 3. CSS ───────────────────────────────────────────────────────────────────
CALLBACK_CSS = '''
/* Callback "Call me back" form */
.callback-label {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--color-text);
  margin-block-end: 0.85rem;
}

.callback-row {
  display: flex;
  gap: 0.6rem;
  flex-wrap: wrap;
  align-items: stretch;
}

.callback-row input[type="tel"] {
  flex: 1;
  min-width: 140px;
  padding: 0.7rem 1rem;
  border: 1.5px solid var(--color-border);
  border-radius: 0.5rem;
  font-size: 1rem;
  font-family: var(--font-body);
  color: var(--color-text);
  background: var(--color-bg);
  transition: border-color 0.15s;
}

.callback-row input[type="tel"]:focus {
  outline: none;
  border-color: var(--color-accent);
}

.callback-btn { white-space: nowrap; }
'''

css = CSS.read_text(encoding='utf-8')
if 'callback-label' not in css:
    CSS.write_text(css + CALLBACK_CSS, encoding='utf-8')
    print('  styles.css: callback CSS added')

# ── 4. JS — replace old rfq-form handler with callback handler ───────────────
js = JS.read_text(encoding='utf-8')

# Find old form block (lines 57-167 approx)
old_block_start = js.find('  const rfqForm = document.getElementById(\'rfq-form\');')
old_block_end   = js.find('  // --- 5. Dynamic Clean-Tech Background Animation')

if old_block_start > -1 and old_block_end > -1:
    new_block = '''  // --- Callback form: передзвоніть мені ---
  const callbackForm  = document.getElementById('callback-form');
  const callbackPhone = document.getElementById('callback-phone');
  const callbackError = document.getElementById('callback-error');
  const formStatusEl  = document.getElementById('form-status');

  if (callbackForm && callbackPhone) {
    callbackPhone.addEventListener('input', () => {
      if (callbackError) callbackError.style.display = 'none';
    });

    callbackForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const phone  = callbackPhone.value.trim();
      const digits = phone.replace(/\\D/g, '');

      if (digits.length < 7) {
        if (callbackError) {
          callbackError.style.display = 'block';
          callbackError.textContent = callbackError.textContent || 'Введіть коректний номер';
        }
        callbackPhone.focus();
        return;
      }

      // Open email client pre-filled
      const subj = encodeURIComponent('Передзвоніть мені — BTC Consulting');
      const body = encodeURIComponent(
        'Будь ласка, передзвоніть мені.\\n\\nТелефон: ' + phone +
        '\\n\\nНадіслано з сайту BTC Consulting'
      );
      window.open('mailto:contact@biotc.pl?subject=' + subj + '&body=' + body);

      if (formStatusEl) {
        formStatusEl.className = 'form-status-container success';
        formStatusEl.innerHTML = '<strong>Дякуємо! Натисніть \\\"Надіслати\\\" у поштовому клієнті.</strong>';
        formStatusEl.classList.remove('hidden');
      }
      callbackForm.reset();
    });
  }

  '''

    js = js[:old_block_start] + new_block + js[old_block_end:]
    JS.write_text(js, encoding='utf-8')
    print('  app.js: form handler replaced')
else:
    print('  app.js: old block not found')

print('Done.')

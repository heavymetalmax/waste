#!/usr/bin/env python3
# encoding: utf-8
"""
1. Restore hamburger JS (nav-mobile-strip) in app.js
2. Add callback form + address-book btn to contact popover
3. Restore full rfq-form in contact section of all 3 templates
4. Remove stray vcard-btn from contact-info-list
5. Restore rfq-form JS handler in app.js
"""
import pathlib, re, json

ROOT  = pathlib.Path('/Users/max/Waste')
BIOTC = ROOT / 'biotc'
JS    = ROOT / 'app.js'

# ── 1. Restore hamburger JS ─────────────────────────────────────────────────
BURGER_JS = '''
  // --- Mobile nav strip ---
  const mobileToggle2 = document.querySelector('.mobile-toggle');
  const mobileStrip   = document.getElementById('nav-mobile-strip');

  function closeStrip() {
    if (!mobileStrip) return;
    mobileStrip.classList.remove('open');
    mobileStrip.setAttribute('aria-hidden', 'true');
    if (mobileToggle2) mobileToggle2.setAttribute('aria-expanded', 'false');
  }

  if (mobileToggle2 && mobileStrip) {
    mobileToggle2.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = mobileStrip.classList.contains('open');
      if (isOpen) { closeStrip(); } else {
        mobileStrip.classList.add('open');
        mobileStrip.setAttribute('aria-hidden', 'false');
        mobileToggle2.setAttribute('aria-expanded', 'true');
      }
    });
    mobileStrip.querySelectorAll('a').forEach(a => a.addEventListener('click', closeStrip));
    document.addEventListener('click', closeStrip);
    window.addEventListener('scroll', closeStrip, { passive: true });
  }
'''

# ── 2. rfq-form JS (restore in app.js) ─────────────────────────────────────
RFQ_JS = '''
  // --- Contact form (rfq-form) ---
  const rfqForm      = document.getElementById('rfq-form');
  const formSubmitBtn= document.getElementById('form-submit-btn');
  const rfqStatus    = document.getElementById('form-status');
  const userName     = document.getElementById('user-name');
  const userPhone    = document.getElementById('user-phone');
  const userCompany  = document.getElementById('user-company');

  function validateField(input, errorId) {
    const em = document.getElementById(errorId);
    if (input && !input.checkValidity() && input.value.trim()) {
      if (em) em.style.display = 'block';
    } else { if (em) em.style.display = 'none'; }
  }

  if (userName)    userName.addEventListener('blur',  () => validateField(userName,   'name-error'));
  if (userPhone)   userPhone.addEventListener('blur',  () => validateField(userPhone,  'phone-error'));
  if (userCompany) userCompany.addEventListener('blur', () => validateField(userCompany,'company-error'));

  if (rfqForm) {
    rfqForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const honeypot = document.getElementById('honeypot');
      if (honeypot && honeypot.value) { rfqForm.reset(); return; }
      if (!rfqForm.checkValidity()) {
        validateField(userName, 'name-error');
        validateField(userPhone, 'phone-error');
        validateField(userCompany, 'company-error');
        rfqForm.querySelector(':invalid')?.focus();
        return;
      }
      if (formSubmitBtn) { formSubmitBtn.disabled = true; formSubmitBtn.textContent = '...'; }
      try {
        const data = new FormData(rfqForm);
        data.append('_subject', 'Нова заявка — BTC Consulting');
        data.append('_captcha', 'false');
        data.append('_template', 'basic');
        const res = await fetch('https://formsubmit.co/ajax/contact@biotc.pl', {
          method: 'POST', headers: { 'Accept': 'application/json' }, body: data,
        });
        if (rfqStatus) {
          rfqStatus.className = res.ok ? 'form-status-container success' : 'form-status-container error';
          rfqStatus.innerHTML = res.ok
            ? '<strong>Дякуємо! Ми зв\'яжемося з вами протягом 1 робочого дня.</strong>'
            : '<strong>Помилка. Зателефонуйте: +48 608 003 458</strong>';
          rfqStatus.classList.remove('hidden');
        }
        if (res.ok) rfqForm.reset();
      } catch {
        if (rfqStatus) {
          rfqStatus.className = 'form-status-container error';
          rfqStatus.innerHTML = '<strong>Немає зв\'язку. Зателефонуйте: +48 608 003 458</strong>';
          rfqStatus.classList.remove('hidden');
        }
      } finally {
        if (formSubmitBtn) { formSubmitBtn.disabled = false; formSubmitBtn.textContent = '{{form.submit}}'; }
      }
    });
  }
'''

# Patch app.js — insert burger JS after "Mobile Menu Toggle" block,
# insert rfq JS after callback form handler
js = JS.read_text(encoding='utf-8')

# Add burger JS if missing
if 'nav-mobile-strip' not in js:
    # Insert before "--- 5. Dynamic Clean-Tech" or before Privacy strip
    marker = '  // --- 5. Dynamic Clean-Tech'
    if marker not in js:
        marker = '  // --- Privacy strip'
    js = js.replace(marker, BURGER_JS + '\n  ' + marker.lstrip())
    print('  app.js: burger JS restored')
else:
    print('  app.js: burger JS already present')

# Add rfq JS if missing
if 'rfq-form' not in js:
    # Insert after callback form block (before fab cycling)
    marker2 = '  // --- Cycling FAB'
    if marker2 not in js:
        marker2 = '  // --- Add contact'
    js = js.replace(marker2, RFQ_JS + '\n  ' + marker2.lstrip())
    print('  app.js: rfq-form JS restored')
else:
    print('  app.js: rfq-form JS already present')

JS.write_text(js, encoding='utf-8')

# ── 3. Popover: add callback form, update vcard btn ─────────────────────────
POPOVER_CALLBACK = '''
        <div class="popover-divider"><span>{{contact.popover.or}}</span></div>
        <div class="popover-callback-wrap">
          <p class="callback-label" style="margin-block-end:0.6rem;font-size:0.85rem;">{{form.callback.label}}</p>
          <div class="callback-row">
            <input type="tel" id="popover-phone" placeholder="{{form.phone.label}}"
                   inputmode="tel" autocomplete="tel">
            <button type="button" class="btn btn-primary callback-btn" id="popover-callback-btn"
                    data-label="{{form.callback.btn}}">{{form.callback.btn}}</button>
          </div>
          <p id="popover-callback-error" class="error-msg" style="display:none">{{form.callback.error}}</p>
          <p class="form-micro-text" style="margin-block-start:0.4rem;">{{form.micro}}</p>
        </div>'''

VCARD_BTN_NEW = '''          <button id="vcard-download-btn" class="popover-action-btn border-orange">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M20 6v12a2 2 0 0 1 -2 2h-10a2 2 0 0 1 -2 -2v-12a2 2 0 0 1 2 -2h10a2 2 0 0 1 2 2"/><path d="M10 16h6"/><path d="M11 11a2 2 0 1 0 4 0a2 2 0 1 0 -4 0"/><path d="M4 8h3"/><path d="M4 12h3"/><path d="M4 16h3"/></svg>
            <strong>{{contact.vcard.btn}}</strong>
          </button>'''

# ── 4. Full rfq-form HTML ────────────────────────────────────────────────────
RFQ_FORM_HTML = '''\
          <div class="glass-card contact-form-card">
            <form id="rfq-form" action="#" method="POST" novalidate>
              <fieldset class="form-fieldset">
                <div class="visually-hidden" aria-hidden="true">
                  <label for="honeypot">Не заповнюйте</label>
                  <input type="text" id="honeypot" name="honeypot" tabindex="-1" autocomplete="off">
                </div>
                <div class="form-group">
                  <input type="text" id="user-name" name="name" placeholder=" " required minlength="2" autocomplete="name" aria-describedby="name-error">
                  <label for="user-name" class="floating-label">{{form.name.label}}</label>
                  <span id="name-error" class="error-msg" role="alert">{{form.name.error}}</span>
                </div>
                <div class="form-group">
                  <input type="tel" id="user-phone" name="phone" placeholder=" " required autocomplete="tel" inputmode="tel" aria-describedby="phone-error">
                  <label for="user-phone" class="floating-label">{{form.phone.label}}</label>
                  <span id="phone-error" class="error-msg" role="alert">{{form.phone.error}}</span>
                </div>
                <div class="form-group">
                  <input type="text" id="user-company" name="company" placeholder=" " required autocomplete="organization" aria-describedby="company-error">
                  <label for="user-company" class="floating-label">{{form.company.label}}</label>
                  <span id="company-error" class="error-msg" role="alert">{{form.company.error}}</span>
                </div>
                <div class="form-group">
                  <select id="user-type" name="object_type">
                    <option value="" disabled selected></option>
                    <option value="waterutil">{{form.type.waterutil}}</option>
                    <option value="community">{{form.type.community}}</option>
                    <option value="agro">{{form.type.agro}}</option>
                    <option value="other">{{form.type.other}}</option>
                  </select>
                  <label for="user-type" class="floating-label">{{form.type.label}}</label>
                </div>
                <button type="submit" id="form-submit-btn" class="btn btn-primary btn-block">{{form.submit}}</button>
                <p class="form-micro-text">{{form.micro}}</p>
              </fieldset>
            </form>
            <div id="form-status" class="form-status-container hidden" tabindex="-1" role="status" aria-live="polite"></div>
          </div>'''

for fname in ['index.html', 'technology.html', 'simulator.html']:
    path = BIOTC / fname
    src  = path.read_text(encoding='utf-8')
    changed = False

    # A. Update vcard btn in popover (new icon + label)
    old_vcard = '''          <button id="vcard-download-btn" class="popover-action-btn border-orange">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"/><polyline points="17 21 17 13 7 13 7 21"/><polyline points="7 3 7 8 15 8"/></svg>
            <strong>{{contact.popover.save}}</strong>
          </button>'''
    if old_vcard in src:
        src = src.replace(old_vcard, VCARD_BTN_NEW)
        changed = True

    # B. Add callback form to popover (replace old "or" + form link)
    old_popover_end = '''        <div class="popover-divider">
          <span>{{contact.popover.or}}</span>
        </div>

        <a href="#contact" id="popover-form-link" class="btn btn-primary btn-block popover-form-btn">
          {{contact.popover.form}}
        </a>'''
    if old_popover_end in src and 'popover-callback-wrap' not in src:
        src = src.replace(old_popover_end, POPOVER_CALLBACK)
        changed = True

    # C. Restore rfq-form (replace callback-form in contact section)
    # Match the current callback-form card
    src_new = re.sub(
        r'          <div class="glass-card contact-form-card">.*?</div>\s*</div>',
        RFQ_FORM_HTML,
        src, count=1, flags=re.DOTALL
    )
    if src_new != src:
        src = src_new
        changed = True

    # D. Remove stray vcard-btn from contact-info-list
    src = re.sub(
        r'\n\s*<button class="contact-vcard-btn" id="vcard-btn">.*?</button>',
        '', src, flags=re.DOTALL
    )

    path.write_text(src, encoding='utf-8')
    print(f'  {fname}: {"updated" if changed else "checked"}')

# ── 5. Popover callback JS ───────────────────────────────────────────────────
js = JS.read_text(encoding='utf-8')
POPOVER_CB_JS = '''
  // --- Popover callback form ---
  const popoverPhone   = document.getElementById('popover-phone');
  const popoverCbBtn   = document.getElementById('popover-callback-btn');
  const popoverCbError = document.getElementById('popover-callback-error');

  if (popoverCbBtn && popoverPhone) {
    popoverPhone.addEventListener('input', () => {
      if (popoverCbError) popoverCbError.style.display = 'none';
    });
    popoverCbBtn.addEventListener('click', async () => {
      const phone  = popoverPhone.value.trim();
      const digits = phone.replace(/\\D/g, '');
      if (digits.length < 7) {
        if (popoverCbError) popoverCbError.style.display = 'block';
        popoverPhone.focus();
        return;
      }
      const orig = popoverCbBtn.textContent;
      popoverCbBtn.disabled = true; popoverCbBtn.textContent = '...';
      try {
        const data = new FormData();
        data.append('phone', phone);
        data.append('_subject', 'Передзвоніть мені — BTC Consulting');
        data.append('_captcha', 'false');
        const res = await fetch('https://formsubmit.co/ajax/contact@biotc.pl', {
          method: 'POST', headers: { 'Accept': 'application/json' }, body: data,
        });
        popoverCbBtn.textContent = res.ok ? '✓ Дякуємо!' : orig;
        if (res.ok) popoverPhone.value = '';
        setTimeout(() => { popoverCbBtn.textContent = orig; }, 3000);
      } catch {
        popoverCbBtn.textContent = orig;
      } finally { popoverCbBtn.disabled = false; }
    });
  }
'''
if 'popover-callback-btn' not in js:
    marker = '  // --- Add contact'
    js = js.replace(marker, POPOVER_CB_JS + '\n  ' + marker.lstrip())
    JS.write_text(js, encoding='utf-8')
    print('  app.js: popover callback JS added')

print('Done.')

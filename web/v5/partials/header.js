document.write(`
<a class="skip-link sr-only" href="#main">Przejdź do treści</a>
<header class="site-header" id="site-header">
  <div class="header-inner">
    <a class="header-logo" href="/v5/index.html" aria-label="BTC Consulting">
      <img src="/v5/assets/svg/logo-blue.svg" alt="BTC Consulting" width="130" height="40" style="display:block">
    </a>

    <nav aria-label="Główna nawigacja">
      <ul class="header-nav" role="list">
        <li><a class="nav-link" href="/v5/technologia.html">Technologia HTC</a></li>
        <li><a class="nav-link" href="/v5/hub-spoke.html">Hub</a></li>
        <li><a class="nav-link" href="/v5/dotacje.html">Dotacje UE</a></li>
        <li><a class="nav-link" href="/v5/teo.html">TEO</a></li>
        <li><a class="nav-link" href="/v5/kalkulator-roi.html">Kalkulator ROI</a></li>
        <li><a class="nav-link" href="/v5/blog/">Blog</a></li>
      </ul>
    </nav>

    <div class="header-actions">
      <button class="contact-fab" id="contact-fab" aria-label="Szybki kontakt" aria-expanded="false">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.11 12 19.79 19.79 0 0 1 1.08 3.38 2 2 0 0 1 3.07 1.22h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
      </button>
      <span class="header-actions-sep" aria-hidden="true"></span>
      <a class="btn btn-primary header-cta" href="#contact">
        Bezpłatna ocena →
      </a>
    </div>

    <button class="mobile-toggle" id="mob-toggle"
            aria-expanded="false" aria-label="Otwórz menu">
      <span class="burger"></span>
      <span class="burger"></span>
      <span class="burger"></span>
    </button>
  </div>

  <nav class="mobile-nav" id="mob-nav" aria-label="Menu mobilne">
    <ul role="list">
      <li><a class="nav-link" href="/v5/index.html">Strona główna</a></li>
      <li><a class="nav-link" href="/v5/technologia.html">Technologia HTC</a></li>
      <li><a class="nav-link" href="/v5/hub-spoke.html">Model Hub</a></li>
      <li><a class="nav-link" href="/v5/teo.html">TEO – ocena wstępna</a></li>
      <li><a class="nav-link" href="/v5/dotacje.html">Dotacje UE</a></li>
      <li><a class="nav-link" href="/v5/kalkulator-roi.html">Kalkulator ROI</a></li>
      <li><a class="nav-link" href="/v5/case-lubin.html">Case study: Lubin</a></li>
      <li><a class="nav-link" href="/v5/misja.html">O BTC Consulting</a></li>
      <li><a class="nav-link" href="/v5/blog/">Blog</a></li>
    </ul>
    <a class="btn btn-primary" href="#contact" style="margin:1.5rem var(--gutter)">
      Bezpłatna ocena →
    </a>
  </nav>
</header>

<div class="contact-popover-overlay" id="popover-overlay" aria-hidden="true"></div>
<div class="contact-popover" id="contact-popover" aria-hidden="true" role="dialog" aria-label="Szybki kontakt">
  <div class="popover-header">
    <h4>Szybki kontakt</h4>
    <button class="popover-close" id="popover-close" aria-label="Zamknij">&times;</button>
  </div>
  <div class="popover-contact-card">
    <div class="popover-avatar">
      <img src="/v5/assets/img/A.%20Krop.jpeg" alt="Andrzej Krop" width="44" height="44">
    </div>
    <div>
      <div class="popover-name">Andrzej Krop</div>
      <div class="popover-role">Zarządzanie projektami</div>
    </div>
  </div>
  <div class="popover-actions">
    <a href="tel:+48608003458" class="popover-action">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.11 12 19.79 19.79 0 0 1 1.08 3.38 2 2 0 0 1 3.07 1.22h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
      <span>+48 608 003 458</span>
    </a>
    <a href="mailto:contact@biotc.pl" class="popover-action">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
      <span>contact@biotc.pl</span>
    </a>
    <a href="https://wa.me/48608003458" target="_blank" rel="noopener" class="popover-action">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
      <span>WhatsApp</span>
    </a>
    <button class="popover-action" id="vcard-btn">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><line x1="19" y1="8" x2="19" y2="14"/><line x1="22" y1="11" x2="16" y2="11"/></svg>
      <strong>Dodaj kontakt</strong>
    </button>
  </div>
  <div class="popover-divider"><span>lub</span></div>
  <div class="popover-callback" id="callback-row">
    <input type="tel" id="popover-phone" placeholder="Numer telefonu *" inputmode="tel" autocomplete="tel">
    <button type="button" class="btn btn-primary" id="popover-cb-btn">Oddzwonimy</button>
  </div>
  <p class="popover-error" id="popover-cb-error">Podaj poprawny numer telefonu</p>
  <p class="popover-micro">Odpowiedź w ciągu 1 dnia roboczego. Bez zobowiązań.</p>
</div>

<script>
(function () {
  var header = document.getElementById('site-header');
  var btn    = document.getElementById('mob-toggle');
  var nav    = document.getElementById('mob-nav');

  window.addEventListener('scroll', function () {
    header.classList.toggle('scrolled', window.scrollY > 40);
  }, { passive: true });

  btn.addEventListener('click', function () {
    var open = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!open));
    nav.classList.toggle('open', !open);
    document.body.style.overflow = open ? '' : 'hidden';
  });

  nav.querySelectorAll('a').forEach(function (a) {
    a.addEventListener('click', function () {
      btn.setAttribute('aria-expanded', 'false');
      nav.classList.remove('open');
      document.body.style.overflow = '';
    });
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && nav.classList.contains('open')) {
      btn.setAttribute('aria-expanded', 'false');
      nav.classList.remove('open');
      document.body.style.overflow = '';
      btn.focus();
    }
  });

  // --- Contact popover ---
  var fab = document.getElementById('contact-fab');
  var popover = document.getElementById('contact-popover');
  var overlay = document.getElementById('popover-overlay');
  var closeBtn = document.getElementById('popover-close');

  function openPopover() {
    popover.classList.add('open');
    popover.setAttribute('aria-hidden', 'false');
    fab.setAttribute('aria-expanded', 'true');
    if (overlay) { overlay.classList.add('open'); overlay.setAttribute('aria-hidden', 'false'); }
    if (window.innerWidth > 768) {
      var r = fab.getBoundingClientRect();
      popover.style.top = (r.bottom + 8) + 'px';
      popover.style.left = Math.max(16, r.right - 340) + 'px';
    }
  }
  function closePopover() {
    popover.classList.remove('open');
    popover.setAttribute('aria-hidden', 'true');
    fab.setAttribute('aria-expanded', 'false');
    if (overlay) { overlay.classList.remove('open'); overlay.setAttribute('aria-hidden', 'true'); }
  }

  fab.addEventListener('click', function (e) {
    e.preventDefault(); e.stopPropagation();
    popover.classList.contains('open') ? closePopover() : openPopover();
  });
  closeBtn.addEventListener('click', closePopover);
  if (overlay) overlay.addEventListener('click', closePopover);
  document.addEventListener('click', function (e) {
    if (!popover.contains(e.target) && !fab.contains(e.target)) closePopover();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && popover.classList.contains('open')) { closePopover(); fab.focus(); }
  });

  // vCard download
  var vcardBtn = document.getElementById('vcard-btn');
  if (vcardBtn) {
    vcardBtn.addEventListener('click', function (e) {
      e.preventDefault();
      var vcard = [
        'BEGIN:VCARD','VERSION:3.0',
        'FN:Andrzej Krop','ORG:BTC Consulting',
        'TITLE:Project Manager',
        'TEL;TYPE=WORK,VOICE:+48608003458',
        'EMAIL;TYPE=PREF,INTERNET:contact@biotc.pl',
        'URL:https://btcconsulting.pl',
        'END:VCARD'
      ].join('\\r\\n');
      var blob = new Blob([vcard], { type: 'text/vcard;charset=utf-8' });
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url; a.download = 'Andrzej_Krop_BTC.vcf';
      document.body.appendChild(a); a.click();
      document.body.removeChild(a); URL.revokeObjectURL(url);
    });
  }

  // Callback form
  var cbPhone = document.getElementById('popover-phone');
  var cbBtn   = document.getElementById('popover-cb-btn');
  var cbError = document.getElementById('popover-cb-error');
  if (cbBtn && cbPhone) {
    cbPhone.addEventListener('input', function () { if (cbError) cbError.style.display = 'none'; });
    cbBtn.addEventListener('click', function () {
      var digits = cbPhone.value.replace(/\\D/g, '');
      if (digits.length < 7) { if (cbError) cbError.style.display = 'block'; cbPhone.focus(); return; }
      var orig = cbBtn.textContent;
      cbBtn.disabled = true; cbBtn.textContent = '...';
      var data = new FormData();
      data.append('phone', cbPhone.value.trim());
      data.append('_subject', 'Oddzwoń — BTC Consulting');
      data.append('_captcha', 'false');
      fetch('https://formsubmit.co/ajax/contact@biotc.pl', {
        method: 'POST', headers: { 'Accept': 'application/json' }, body: data,
      }).then(function (res) {
        cbBtn.textContent = res.ok ? '✓ Dziękujemy!' : orig;
        if (res.ok) cbPhone.value = '';
        setTimeout(function () { cbBtn.textContent = orig; }, 3000);
      }).catch(function () { cbBtn.textContent = orig; })
      .finally(function () { cbBtn.disabled = false; });
    });
  }
})();
</script>
`);

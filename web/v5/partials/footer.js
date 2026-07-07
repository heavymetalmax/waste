document.write(`
<!-- CTA Band -->
<div class="footer-cta" id="contact">
  <div>
    <p class="t-label-muted mb-2">Bezpłatna analiza wstępna</p>
    <h2 class="t-heading" style="color:var(--c-white)">Sprawdź czy Twoja<br>oczyszczalnia kwalifikuje się</h2>
  </div>
  <a class="btn btn-dark" href="#contact-form" style="flex-shrink:0">
    Poproś o TEO →
  </a>
</div>

<section class="section contact-section" style="border-top:1px solid var(--c-border)">
  <div class="container">
    <div class="contact-grid">
      <div>
        <p class="t-label mb-2">Skontaktuj się</p>
        <h2 class="t-heading mb-3">
          Zacznij od<br>bezpłatnej oceny
        </h2>
        <p class="t-lead mb-4" style="color:var(--c-gray-d)">
          Powiedz nam o swojej oczyszczalni — wrócimy z wstępną analizą
          techniczną i finansową w ciągu 48 godzin.
        </p>
        <ul class="feature-list feature-list--light">
          <li>Wstępna analiza techniczna (TEO) — bez kosztów</li>
          <li>Szacunek kosztów i dofinansowania UE</li>
          <li>Odpowiedź w 48 godzin</li>
        </ul>
      </div>

      <form
        id="contact-form"
        action="https://formsubmit.co/contact@biotc.pl"
        method="POST"
        class="flex-col gap-sm"
        style="display:flex;flex-direction:column;gap:16px"
        novalidate
        data-mcp-action="request_consultation"
        data-mcp-description="Request a free preliminary HTC feasibility assessment for a wastewater treatment plant"
      >
        <input type="hidden" name="_subject" value="BTC Consulting — zapytanie ze strony">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_next" value="https://btcconsulting.pl/v5/dziekujemy.html">
        <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">

        <div class="form-group">
          <label class="form-label" for="cf-name">Imię i nazwisko *</label>
          <input class="form-input" type="text" id="cf-name" name="imie_nazwisko"
                 placeholder="Jan Kowalski" required autocomplete="name">
        </div>

        <div class="form-row">
          <div class="form-group">
            <label class="form-label" for="cf-email">E-mail</label>
            <input class="form-input" type="email" id="cf-email" name="email"
                   placeholder="j.kowalski@mpwik.pl" autocomplete="email">
          </div>
          <div class="form-group">
            <label class="form-label" for="cf-phone">Telefon</label>
            <input class="form-input" type="tel" id="cf-phone" name="telefon"
                   placeholder="+48 …" autocomplete="tel">
          </div>
        </div>
        <p class="form-hint" id="cf-contact-hint" style="display:none;color:var(--c-red, #c00);font-size:0.8rem;margin:-8px 0 0">Podaj e-mail lub numer telefonu</p>

        <div class="form-group">
          <label class="form-label" for="cf-msg">Wiadomość</label>
          <textarea class="form-textarea" id="cf-msg" name="wiadomosc"
                    placeholder="Opisz swój obiekt i oczekiwania…" rows="3"></textarea>
        </div>

        <button type="submit" class="btn btn-primary self-start" style="margin-top:0.5rem">
          Wyślij zapytanie →
        </button>
      </form>
      <noscript>
        <div style="padding:1.5rem;border:2px solid var(--c-accent);margin-top:1rem">
          <p style="margin:0 0 0.5rem;font-weight:600">Kontakt bez JavaScript:</p>
          <p style="margin:0">Email: <a href="mailto:contact@biotc.pl">contact@biotc.pl</a></p>
          <p style="margin:0">Tel: <a href="tel:+48608003458">+48 608 003 458</a></p>
        </div>
      </noscript>
    </div>
  </div>
</section>

<footer class="site-footer">

  <!-- Nav kolumny -->
  <div class="footer-grid" style="padding-top:40px">
    <div class="footer-mark" aria-hidden="true">
      <img src="/v5/assets/svg/logo-white-on-black.svg" alt="" width="180" height="66" style="display:block">
    </div>

    <div style="display:grid;grid-template-columns:1fr 1fr;gap:32px">
      <div class="footer-col">
        <h4>Rozwiązania</h4>
        <ul>
          <li><a href="/v5/technologia.html">Technologia HTC</a></li>
          <li><a href="/v5/hub-spoke.html">Model Hub &amp; Spoke</a></li>
          <li><a href="/v5/kalkulator-roi.html">Kalkulator ROI</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>Finansowanie</h4>
        <ul>
          <li><a href="/v5/teo.html">TEO – ocena wstępna</a></li>
          <li><a href="/v5/dotacje.html">Dotacje UE 2026–2028</a></li>
        </ul>
      </div>
    </div>

    <div style="display:grid;grid-template-columns:1fr 1fr;gap:32px">
      <div class="footer-col">
        <h4>Zasoby</h4>
        <ul>
          <li><a href="/v5/case-lubin.html">Case study: Lubin</a></li>
          <li><a href="/v5/whitepaper.html">Whitepaper HTC</a></li>
          <li><a href="/v5/misja.html">O BTC Consulting</a></li>
          <li><a href="/v5/blog/">Blog</a></li>
        </ul>
      </div>

    </div>
  </div>

  <div class="footer-bottom">
    <p class="t-small">&copy; 2026 BTC Consulting sp. z o.o. — Technologia HTC dla polskich oczyszczalni ścieków</p>
    <p class="t-small" style="color:var(--c-gray-dd)">Gliwice, Polska · <a href="/v5/polityka-prywatnosci.html" style="color:var(--c-gray-dd);text-decoration:underline">Polityka prywatności</a></p>
  </div>

</footer>
`);

(function () {
  var form = document.getElementById('contact-form');
  if (!form) return;
  var email = document.getElementById('cf-email');
  var phone = document.getElementById('cf-phone');
  var hint  = document.getElementById('cf-contact-hint');

  function clearHint() { if (hint) hint.style.display = 'none'; }
  email.addEventListener('input', clearHint);
  phone.addEventListener('input', clearHint);

  form.addEventListener('submit', function (e) {
    if (!email.value.trim() && !phone.value.trim()) {
      e.preventDefault();
      if (hint) hint.style.display = 'block';
      email.focus();
    }
  });
})();

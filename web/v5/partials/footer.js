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
        action="https://formsubmit.co/maxym.koval@gmail.com"
        method="POST"
        class="flex-col gap-sm"
        style="display:flex;flex-direction:column;gap:16px"
        novalidate
      >
        <input type="hidden" name="_subject" value="BTC Consulting — zapytanie ze strony">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_next" value="https://btcconsulting.pl/v5/dziekujemy.html">
        <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">

        <div class="form-row">
          <div class="form-group">
            <label class="form-label" for="cf-name">Imię i nazwisko *</label>
            <input class="form-input" type="text" id="cf-name" name="imie_nazwisko"
                   placeholder="Jan Kowalski" required autocomplete="name">
          </div>
          <div class="form-group">
            <label class="form-label" for="cf-role">Stanowisko</label>
            <input class="form-input" type="text" id="cf-role" name="stanowisko"
                   placeholder="Naczelnik OCS">
          </div>
        </div>

        <div class="form-group">
          <label class="form-label" for="cf-org">Gmina / Przedsiębiorstwo *</label>
          <input class="form-input" type="text" id="cf-org" name="organizacja"
                 placeholder="MPWiK Przykładowo" required>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label class="form-label" for="cf-email">E-mail *</label>
            <input class="form-input" type="email" id="cf-email" name="email"
                   placeholder="j.kowalski@mpwik.pl" required autocomplete="email">
          </div>
          <div class="form-group">
            <label class="form-label" for="cf-phone">Telefon</label>
            <input class="form-input" type="tel" id="cf-phone" name="telefon"
                   placeholder="+48 …" autocomplete="tel">
          </div>
        </div>

        <div class="form-group">
          <label class="form-label" for="cf-volume">Ilość osadów [t/rok]</label>
          <input class="form-input" type="number" id="cf-volume" name="ilosc_osadow_t_rok"
                 placeholder="Np. 800" min="50" step="1">
        </div>

        <div class="form-group">
          <label class="form-label" for="cf-msg">Wiadomość</label>
          <textarea class="form-textarea" id="cf-msg" name="wiadomosc"
                    placeholder="Opisz swój obiekt i oczekiwania…" rows="4"></textarea>
        </div>

        <button type="submit" class="btn btn-primary self-start" style="margin-top:0.5rem">
          Wyślij zapytanie →
        </button>
      </form>
    </div>
  </div>
</section>

<footer class="site-footer">

  <!-- Nav kolumny -->
  <div class="footer-grid" style="padding-top:40px">
    <div class="footer-mark" aria-hidden="true">BTC<span>.</span></div>

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
        </ul>
      </div>

      <div class="footer-col">
        <h4>Kontakt</h4>
        <ul>
          <li><a href="mailto:info@btcconsulting.pl">info@btcconsulting.pl</a></li>
          <li><a href="https://www.linkedin.com/company/btc-consulting-pl" rel="noopener">LinkedIn</a></li>
        </ul>
      </div>
    </div>
  </div>

  <div class="footer-bottom">
    <p class="t-small">&copy; 2025 BTC Consulting sp. z o.o. — Technologia HTC dla polskich oczyszczalni ścieków</p>
    <p class="t-small" style="color:var(--c-gray-dd)">Wrocław, Polska</p>
  </div>

</footer>
`);

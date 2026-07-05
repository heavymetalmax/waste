/* Single source of truth for the contact section — every pl_v2 page includes
   this file instead of its own copy of the <section id="contact"> markup. */
document.write(`
    <section id="contact" class="section-gray-dark">
      <div class="container">
        <div class="grid-2">
          <div>
            <span class="rubric">Kontakt</span>
            <h2>Pierwszy krok — bezpłatna ocena inżynieryjna obiektu.</h2>
            <p>Wyślij zgłoszenie. Nasi inżynierowie przeanalizują dane wejściowe i umówią 30-minutową rozmowę — bez sprzedażowego pitchu.</p>

            <div class="contact-deliverables">
              <strong>Po 30-minutowej rozmowie wiesz:</strong>
              <ul>
                <li>Którą konfigurację wybrać: A, B czy C</li>
                <li>Szacowany CAPEX i poziom dofinansowania UE</li>
                <li>Czy Twój obiekt kwalifikuje się do TH-Booster lub pełnej pętli</li>
              </ul>
              <p class="note">Bez zobowiązań i bez sprzedażowego pitchu.</p>
            </div>

            <div class="contact-info-list" style="display:flex; flex-direction:column; gap:0.75rem; margin-top:1.5rem;">
              <div class="info-item" style="display:flex; align-items:center; gap:0.75rem; font-weight:700;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                <span>+48 608 003 458</span>
              </div>
              <div class="info-item" style="display:flex; align-items:center; gap:0.75rem; font-weight:700;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                <span>contact@biotc.pl</span>
              </div>
              <div class="info-item" style="display:flex; align-items:center; gap:0.75rem; font-weight:700;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                <span>ul. Daszyńskiego 34/3, 44-100 Gliwice, Polska</span>
              </div>
            </div>
          </div>

          <div class="col-card">
            <form id="rfq-form" action="#" method="POST" novalidate>
              <div style="position:absolute; left:-9999px;" aria-hidden="true">
                <label for="honeypot">Leave blank</label>
                <input type="text" id="honeypot" name="honeypot" tabindex="-1" autocomplete="off">
              </div>
              <div class="form-group">
                <label for="user-name">Imię i nazwisko / stanowisko *</label>
                <input type="text" id="user-name" name="name" required minlength="2" autocomplete="name">
              </div>
              <div class="form-group">
                <label for="user-phone">Telefon kontaktowy *</label>
                <input type="tel" id="user-phone" name="phone" required autocomplete="tel" inputmode="tel">
              </div>
              <div class="form-group">
                <label for="user-company">Miasto / nazwa przedsiębiorstwa *</label>
                <input type="text" id="user-company" name="company" required autocomplete="organization">
              </div>
              <div class="form-group">
                <label for="user-type">Typ obiektu</label>
                <select id="user-type" name="object_type">
                  <option value="" disabled selected></option>
                  <option value="waterutil">Regionalne przedsiębiorstwo wodociągowe (od 50 tys.)</option>
                  <option value="community">Gmina (od 10 tys.)</option>
                  <option value="agro">Przedsiębiorstwo rolno-spożywcze</option>
                  <option value="other">Inne</option>
                </select>
              </div>
              <button type="submit" id="form-submit-btn" class="btn btn-primary" style="width:100%;">Wyślij zgłoszenie</button>
              <p style="margin-top:1rem; font-size:0.85rem; font-weight:600;">Odpowiedź w ciągu 1 dnia roboczego. Bez zobowiązań.</p>
            </form>
            <div id="form-status" class="hidden" tabindex="-1" role="status" aria-live="polite"></div>
          </div>
        </div>
      </div>
    </section>
`);

document.write(`
<footer class="site-footer section-black">
  <div class="container footer-inner">
    <div class="footer-brand">
      <div class="logo-placeholder" data-slot="btc-logo" style="font-family:var(--font-display);font-weight:900;font-size:1.5rem;color:var(--color-white);margin-bottom:0.75rem;">BTC</div>
      <p class="footer-tagline">Technologia HTC do zagospodarowania<br>osadów ściekowych. Dotacje UE do 85% CapEx.</p>
    </div>

    <nav class="footer-nav" aria-label="Nawigacja pomocnicza">
      <h4 class="footer-nav-title">Rozwiązania</h4>
      <ul>
        <li><a href="/v3/technologia.html">Technologia HTC</a></li>
        <li><a href="/v3/hub-spoke.html">Model Hub &amp; Spoke</a></li>
        <li><a href="/v3/kalkulator-roi.html">Kalkulator ROI</a></li>
      </ul>
    </nav>

    <nav class="footer-nav" aria-label="Nawigacja finansowanie">
      <h4 class="footer-nav-title">Finansowanie</h4>
      <ul>
        <li><a href="/v3/teo.html">TEO – ocena wstępna</a></li>
        <li><a href="/v3/dotacje.html">Dotacje UE</a></li>
      </ul>
    </nav>

    <nav class="footer-nav" aria-label="Zasoby">
      <h4 class="footer-nav-title">Zasoby</h4>
      <ul>
        <li><a href="/v3/case-lubin.html">Case study: Lubin</a></li>
        <li><a href="/v3/whitepaper.html">Whitepaper techniczny</a></li>
        <li><a href="/v3/misja.html">O BTC Consulting</a></li>
      </ul>
    </nav>
  </div>

  <div class="footer-bottom container">
    <p class="footer-copy">&copy; 2025 BTC Consulting. Wszelkie prawa zastrzeżone.</p>
    <p class="footer-legal">
      Rozwiązania inżynieryjne dla bezpiecznej utylizacji osadów ściekowych.<br>
      Technologia HTC. Dotacje UE. Polska obsługa.
    </p>
  </div>
</footer>

<style>
.site-footer {
  margin-top: auto;
}

.footer-inner {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-lg);
  padding-top: var(--space-section);
  padding-bottom: var(--space-md);
}

@media (min-width: 600px) {
  .footer-inner { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 1024px) {
  .footer-inner { grid-template-columns: 2fr 1fr 1fr 1fr; }
}

.footer-tagline {
  font-size: 0.875rem;
  line-height: 1.6;
  color: rgba(255,255,255,0.6);
  max-width: none;
}

.footer-nav-title {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--color-accent);
  margin-bottom: 1rem;
}

.footer-nav ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.footer-nav a {
  font-size: 0.875rem;
  color: rgba(255,255,255,0.65);
  text-decoration: none;
  transition: color var(--transition);
}

.footer-nav a:hover {
  color: var(--color-white);
}

.footer-bottom {
  border-top: 1px solid rgba(255,255,255,0.1);
  padding-top: var(--space-md);
  padding-bottom: var(--space-lg);
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.footer-copy,
.footer-legal {
  font-size: 0.8rem;
  color: rgba(255,255,255,0.4);
  max-width: none;
}
</style>
`);

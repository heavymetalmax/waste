/* Single source of truth for the site footer — every pl_v2 page includes
   this file instead of its own copy of the <footer> markup, so there is
   exactly one place to edit and no risk of pages drifting apart. */
document.write([
  '<footer>',
  '  <div class="container">',
  '    <div class="logo">BTC <span>Consulting</span></div>',
  '    <div class="footer-grid">',
  '      <div class="footer-col">',
  '        <p class="footer-col-heading">Nawigacja</p>',
  '        <a href="index.html">Rozwiązania</a>',
  '        <a href="technology.html">Technologia</a>',
  '        <a href="kalkulator-roi.html">Kalkulator</a>',
  '        <a href="#contact">Kontakt</a>',
  '        <a href="mission.html">Misja</a>',
  '      </div>',
  '      <div class="footer-col">',
  '        <p class="footer-col-heading">Dokumenty</p>',
  '        <a href="whitepaper.html">Whitepaper</a>',
  '        <a href="case-lubin.html">Przypadek: Lubin</a>',
  '      </div>',
  '    </div>',
  '    <p>&copy; 2025 BTC Consulting. Wszelkie prawa zastrzeżone.</p>',
  '  </div>',
  '</footer>'
].join('\n'));

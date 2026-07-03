document.write(`
<a class="skip-link sr-only" href="#main">Przejdź do treści</a>
<header class="site-header" id="site-header">
  <div class="header-inner">
    <a class="header-logo" href="/v5/index.html" aria-label="BTC Consulting">
      <img src="/v5/assets/svg/logo.svg" alt="BTC Consulting" width="38" height="38" style="display:block">
    </a>

    <nav aria-label="Główna nawigacja">
      <ul class="header-nav" role="list">
        <li><a class="nav-link" href="/v5/technologia.html">Technologia HTC</a></li>
        <li><a class="nav-link" href="/v5/hub-spoke.html">Hub &amp; Spoke</a></li>
        <li><a class="nav-link" href="/v5/dotacje.html">Dotacje UE</a></li>
        <li><a class="nav-link" href="/v5/kalkulator-roi.html">Kalkulator ROI</a></li>
        <li><a class="nav-link" href="/v5/misja.html">O nas</a></li>
        <li><a class="nav-link" href="/v5/blog/">Blog</a></li>
      </ul>
    </nav>

    <a class="btn btn-primary header-cta" href="#contact">
      Bezpłatna ocena →
    </a>

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
      <li><a class="nav-link" href="/v5/hub-spoke.html">Model Hub &amp; Spoke</a></li>
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
})();
</script>
`);

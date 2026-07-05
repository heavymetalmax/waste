document.write(`
<header class="site-header">
  <div class="header-inner">
    <a class="header-logo" href="/v4/index.html" aria-label="BTC Consulting">
      BTC<span>.</span>
    </a>

    <ul class="header-nav" role="list">
      <li><a class="nav-link" href="/v4/index.html">Główna</a></li>
      <li><a class="nav-link" href="/v4/technologia.html">Technologia</a></li>
      <li><a class="nav-link" href="/v4/hub-spoke.html">Hub &amp; Spoke</a></li>
      <li><a class="nav-link" href="/v4/dotacje.html">Dotacje</a></li>
      <li><a class="nav-link" href="/v4/kalkulator-roi.html">Kalkulator</a></li>
    </ul>

    <a class="btn btn-solid header-cta" href="/v4/teo.html#contact">Bezpłatna ocena →</a>

    <button class="mobile-toggle" id="mob-toggle" aria-expanded="false" aria-label="Menu">
      <span class="burger"></span>
      <span class="burger"></span>
      <span class="burger"></span>
    </button>
  </div>

  <ul class="mobile-nav" id="mob-nav" role="list">
    <li><a class="nav-link" href="/v4/index.html">Główna</a></li>
    <li><a class="nav-link" href="/v4/technologia.html">Technologia HTC</a></li>
    <li><a class="nav-link" href="/v4/hub-spoke.html">Model Hub &amp; Spoke</a></li>
    <li><a class="nav-link" href="/v4/teo.html">TEO – ocena wstępna</a></li>
    <li><a class="nav-link" href="/v4/dotacje.html">Dotacje UE</a></li>
    <li><a class="nav-link" href="/v4/kalkulator-roi.html">Kalkulator ROI</a></li>
    <li><a class="btn btn-solid" href="/v4/teo.html#contact" style="margin-top:1rem">Bezpłatna ocena →</a></li>
  </ul>
</header>

<script>
(function(){
  var btn = document.getElementById('mob-toggle');
  var nav = document.getElementById('mob-nav');
  if(!btn||!nav) return;
  btn.addEventListener('click', function(){
    var open = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!open));
    nav.classList.toggle('open', !open);
    document.body.style.overflow = open ? '' : 'hidden';
  });
  nav.querySelectorAll('a').forEach(function(a){
    a.addEventListener('click', function(){
      btn.setAttribute('aria-expanded','false');
      nav.classList.remove('open');
      document.body.style.overflow = '';
    });
  });
})();
</script>
`);

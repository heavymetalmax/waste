document.write(`
<header class="site-header" id="site-header">
  <div class="header-inner container">
    <a class="header-logo" href="/v3/index.html" aria-label="BTC Consulting — strona główna">
      <div class="logo-placeholder" data-slot="btc-logo">BTC</div>
    </a>

    <nav class="header-nav" id="header-nav" aria-label="Menu główne">
      <ul class="nav-list">
        <li class="nav-item">
          <a class="nav-link" href="/v3/index.html">Główna</a>
        </li>
        <li class="nav-item has-dropdown">
          <button class="nav-link nav-dropdown-toggle" aria-expanded="false" aria-haspopup="true">
            Rozwiązania <span class="nav-arrow" aria-hidden="true">▾</span>
          </button>
          <ul class="nav-dropdown" role="menu">
            <li><a class="nav-dropdown-link" href="/v3/technologia.html" role="menuitem">Technologia HTC</a></li>
            <li><a class="nav-dropdown-link" href="/v3/hub-spoke.html" role="menuitem">Model Hub &amp; Spoke</a></li>
          </ul>
        </li>
        <li class="nav-item has-dropdown">
          <button class="nav-link nav-dropdown-toggle" aria-expanded="false" aria-haspopup="true">
            Finansowanie <span class="nav-arrow" aria-hidden="true">▾</span>
          </button>
          <ul class="nav-dropdown" role="menu">
            <li><a class="nav-dropdown-link" href="/v3/teo.html" role="menuitem">TEO – ocena wstępna</a></li>
            <li><a class="nav-dropdown-link" href="/v3/dotacje.html" role="menuitem">Dotacje UE</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/v3/kalkulator-roi.html">Kalkulator ROI</a>
        </li>
      </ul>
    </nav>

    <a class="btn btn-primary header-cta" href="/v3/teo.html#contact">Bezpłatna ocena →</a>

    <button class="mobile-toggle" id="mobile-toggle" aria-expanded="false" aria-controls="header-nav" aria-label="Otwórz menu">
      <span class="burger-bar"></span>
      <span class="burger-bar"></span>
      <span class="burger-bar"></span>
    </button>
  </div>
</header>

<style>
/* ── Header ── */
.site-header {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 100;
  background: var(--color-black);
  border-bottom: 1px solid rgba(255,255,255,0.08);
}

.header-inner {
  display: flex;
  align-items: center;
  gap: 2rem;
  height: 64px;
}

.header-logo {
  flex-shrink: 0;
  text-decoration: none;
}

.logo-placeholder {
  font-family: var(--font-display);
  font-weight: 900;
  font-size: 1.5rem;
  color: var(--color-white);
  letter-spacing: -0.03em;
}

.header-nav {
  flex: 1;
  display: none;
}

@media (min-width: 768px) {
  .header-nav { display: block; }
}

.nav-list {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  list-style: none;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 0.3rem;
  padding: 0.5rem 0.75rem;
  font-size: 0.85rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: rgba(255,255,255,0.8);
  background: transparent;
  border: none;
  cursor: pointer;
  font-family: var(--font-primary);
  transition: color var(--transition);
  text-decoration: none;
  min-height: 40px;
}

.nav-link:hover,
.nav-link[aria-expanded="true"] {
  color: var(--color-white);
}

.nav-arrow {
  font-size: 0.65rem;
  transition: transform var(--transition);
}

.nav-dropdown-toggle[aria-expanded="true"] .nav-arrow {
  transform: rotate(180deg);
}

/* Dropdown */
.has-dropdown {
  position: relative;
}

.nav-dropdown {
  display: none;
  position: absolute;
  top: calc(100% + 8px);
  left: 0;
  min-width: 200px;
  background: var(--color-black);
  border: 1px solid rgba(255,255,255,0.12);
  list-style: none;
  z-index: 10;
}

.has-dropdown:focus-within .nav-dropdown,
.nav-dropdown-toggle[aria-expanded="true"] + .nav-dropdown {
  display: block;
}

.nav-dropdown-link {
  display: block;
  padding: 0.75rem 1rem;
  font-size: 0.85rem;
  color: rgba(255,255,255,0.75);
  text-decoration: none;
  border-bottom: 1px solid rgba(255,255,255,0.06);
  transition: color var(--transition), background var(--transition);
}

.nav-dropdown-link:last-child { border-bottom: none; }

.nav-dropdown-link:hover {
  color: var(--color-white);
  background: rgba(255,255,255,0.05);
}

/* CTA */
.header-cta {
  flex-shrink: 0;
  display: none;
  font-size: 0.8rem;
  padding: 0.6em 1.2em;
  min-height: 40px;
}

@media (min-width: 768px) {
  .header-cta { display: inline-flex; }
}

/* Hamburger */
.mobile-toggle {
  display: flex;
  flex-direction: column;
  gap: 5px;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 8px;
  margin-left: auto;
  min-height: 48px;
  min-width: 48px;
  align-items: center;
  justify-content: center;
}

@media (min-width: 768px) {
  .mobile-toggle { display: none; }
}

.burger-bar {
  display: block;
  width: 22px;
  height: 2px;
  background: var(--color-white);
  transition: transform var(--transition), opacity var(--transition);
}

.mobile-toggle[aria-expanded="true"] .burger-bar:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}
.mobile-toggle[aria-expanded="true"] .burger-bar:nth-child(2) {
  opacity: 0;
}
.mobile-toggle[aria-expanded="true"] .burger-bar:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

/* Mobile nav open */
.header-nav.is-open {
  display: block;
  position: fixed;
  top: 64px; left: 0; right: 0; bottom: 0;
  background: var(--color-black);
  overflow-y: auto;
  padding: var(--space-md);
}

.header-nav.is-open .nav-list {
  flex-direction: column;
  align-items: flex-start;
  gap: 0;
}

.header-nav.is-open .nav-dropdown {
  position: static;
  border: none;
  padding-left: 1rem;
  margin-top: 0.25rem;
}

.header-nav.is-open .nav-link {
  font-size: 1.1rem;
  padding: 1rem 0;
  border-bottom: 1px solid rgba(255,255,255,0.06);
  width: 100%;
}

/* Offset page content below fixed header */
body { padding-top: 64px; }
</style>

<script>
(function () {
  /* Hamburger toggle */
  var toggle = document.getElementById('mobile-toggle');
  var nav = document.getElementById('header-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', !open);
      nav.classList.toggle('is-open', !open);
      document.body.style.overflow = open ? '' : 'hidden';
    });
  }

  /* Dropdown toggles */
  document.querySelectorAll('.nav-dropdown-toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var expanded = btn.getAttribute('aria-expanded') === 'true';
      /* Close all others */
      document.querySelectorAll('.nav-dropdown-toggle').forEach(function (b) {
        b.setAttribute('aria-expanded', 'false');
      });
      btn.setAttribute('aria-expanded', !expanded);
    });
  });

  /* Close dropdowns on outside click */
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.has-dropdown')) {
      document.querySelectorAll('.nav-dropdown-toggle').forEach(function (b) {
        b.setAttribute('aria-expanded', 'false');
      });
    }
  });

  /* Close mobile nav on link click */
  document.querySelectorAll('.header-nav a').forEach(function (a) {
    a.addEventListener('click', function () {
      if (toggle) toggle.setAttribute('aria-expanded', 'false');
      if (nav) nav.classList.remove('is-open');
      document.body.style.overflow = '';
    });
  });
})();
</script>
`);

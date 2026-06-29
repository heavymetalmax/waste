/* Single source of truth for the site header — every pl_v2 page includes
   this file instead of its own copy of the <header> markup, so there is
   exactly one place to edit and no risk of pages drifting apart. */
document.write([
  '<header>',
  '  <div class="container" style="display:flex; align-items:center; justify-content:space-between;">',
  '    <a href="index.html" class="logo">BTC <span>Consulting</span></a>',
  '    <nav style="display:flex; align-items:center; gap:2rem;">',
  '      <a href="index.html" data-nav="index.html" style="font-weight:800; text-transform:uppercase; font-size:0.9rem;">Rozwiązania</a>',
  '      <a href="technology.html" data-nav="technology.html" style="font-weight:800; text-transform:uppercase; font-size:0.9rem;">Technologia</a>',
  '      <a href="kalkulator-roi.html" data-nav="kalkulator-roi.html" style="font-weight:800; text-transform:uppercase; font-size:0.9rem;">Kalkulator</a>',
  '      <a href="#contact" class="btn btn-outline">Zdobądź ocenę</a>',
  '    </nav>',
  '  </div>',
  '</header>'
].join(''));

document.addEventListener('DOMContentLoaded', function () {
  var page = location.pathname.split('/').pop() || 'index.html';
  var links = document.querySelectorAll('header nav a[data-nav]');
  for (var i = 0; i < links.length; i++) {
    if (links[i].getAttribute('data-nav') === page) {
      links[i].style.color = 'var(--color-blue)';
    }
  }
});

/* v3/reveal.js — scroll reveal + counter animation + SVG draw */
(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Counter animation */
  function animateCounter(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var suffix = el.textContent.replace(/[\d.,]/g, '');
    var start = performance.now();
    var duration = 1400;
    function step(now) {
      var p = Math.min((now - start) / duration, 1);
      var ease = 1 - Math.pow(1 - p, 3);
      var val = Math.round(target * ease);
      el.textContent = val.toLocaleString('pl-PL') + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  /* SVG path draw-in */
  function animateSVG(svg) {
    svg.querySelectorAll('path, line, polyline, circle, rect').forEach(function (path) {
      var len = path.getTotalLength ? path.getTotalLength() : 0;
      if (!len) return;
      path.style.strokeDasharray = len;
      path.style.strokeDashoffset = len;
      path.style.transition = 'stroke-dashoffset 1.2s ease';
      requestAnimationFrame(function () { path.style.strokeDashoffset = '0'; });
    });
  }

  if (reduced) {
    /* Skip animation — reveal everything immediately */
    document.querySelectorAll('[data-reveal]').forEach(function (el) {
      el.classList.add('is-visible');
    });
    document.querySelectorAll('[data-count]').forEach(function (el) {
      var target = parseFloat(el.getAttribute('data-count'));
      var suffix = el.textContent.replace(/[\d.,]/g, '');
      el.textContent = target.toLocaleString('pl-PL') + suffix;
    });
    return;
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      var el = entry.target;
      el.classList.add('is-visible');
      el.querySelectorAll('[data-count]').forEach(animateCounter);
      el.querySelectorAll('svg[data-draw]').forEach(animateSVG);
      observer.unobserve(el);
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('[data-reveal]').forEach(function (el) {
    observer.observe(el);
  });
})();

/* reveal.js — scroll reveal + animated counters */
(function () {
  'use strict';

  /* --- Scroll Reveal --- */
  function initReveal() {
    var els = document.querySelectorAll('.reveal');
    if (!els.length) return;

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    els.forEach(function (el) { io.observe(el); });
  }

  /* --- Animated Counters --- */
  function easeOut(t) { return 1 - Math.pow(1 - t, 3); }

  function animateCount(el) {
    var target   = parseFloat(el.dataset.count);
    var duration = parseInt(el.dataset.duration || '1600', 10);
    var decimals = (el.dataset.count.indexOf('.') !== -1)
      ? el.dataset.count.split('.')[1].length : 0;
    var suffix   = el.dataset.suffix || '';
    var prefix   = el.dataset.prefix || '';
    var start    = null;

    function step(ts) {
      if (!start) start = ts;
      var progress = Math.min((ts - start) / duration, 1);
      var value = easeOut(progress) * target;
      el.textContent = prefix + value.toFixed(decimals) + suffix;
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  function initCounters() {
    var els = document.querySelectorAll('[data-count]');
    if (!els.length) return;

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          animateCount(e.target);
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.5 });

    els.forEach(function (el) { io.observe(el); });
  }

  /* --- Accordion --- */
  function initAccordions() {
    document.querySelectorAll('.acc-btn').forEach(function (btn) {
      var item = btn.closest('.acc-item');
      var body = item.querySelector('.acc-body');

      if (body && !body.id) body.id = 'acc-body-' + Math.random().toString(36).slice(2, 8);
      btn.setAttribute('aria-expanded', String(item.classList.contains('open')));
      if (body) btn.setAttribute('aria-controls', body.id);

      btn.addEventListener('click', function () {
        var wasOpen = item.classList.contains('open');

        var parent = btn.closest('.acc') || item.parentElement;
        parent.querySelectorAll('.acc-item').forEach(function (s) {
          s.classList.remove('open');
          var b = s.querySelector('.acc-body');
          if (b) b.hidden = true;
          var sb = s.querySelector('.acc-btn');
          if (sb) sb.setAttribute('aria-expanded', 'false');
        });

        if (!wasOpen) {
          item.classList.add('open');
          body.hidden = false;
          btn.setAttribute('aria-expanded', 'true');
        }
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initReveal();
    initCounters();
    initAccordions();
  });
})();

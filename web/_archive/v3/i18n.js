/* v3/i18n.js — minimal i18n engine */
(function () {
  document.querySelectorAll('[data-i18n]').forEach(function (el) {
    var k = el.getAttribute('data-i18n');
    if (window.I18N && window.I18N[k] != null) el.textContent = window.I18N[k];
  });
})();

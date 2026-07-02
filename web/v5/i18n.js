/* i18n.js — minimal i18n engine (single-language for now: Polish) */
(function () {
  'use strict';

  window.i18n = {
    get: function (path) {
      var parts = path.split('.');
      var obj   = window.BTC_STRINGS || {};
      for (var i = 0; i < parts.length; i++) {
        if (obj == null) return path;
        obj = obj[parts[i]];
      }
      return (obj != null && typeof obj === 'string') ? obj : path;
    },
  };
})();

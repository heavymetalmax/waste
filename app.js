document.addEventListener("DOMContentLoaded", () => {
  let isNavigatingToContact = false;

  // --- 1. Shrinking Header on Scroll ---
  const header = document.getElementById('header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        header.classList.add('shrink');
      } else {
        header.classList.remove('shrink');
      }
    });
  }

  // --- 2. Mobile Menu Toggle ---
  const mobileToggle = document.querySelector('.mobile-toggle');
  const mobileNav = document.getElementById('mobile-nav');

  if (mobileToggle && mobileNav) {
    mobileToggle.addEventListener('click', () => {
      const isExpanded = mobileToggle.getAttribute('aria-expanded') === 'true';
      mobileToggle.setAttribute('aria-expanded', !isExpanded);
      mobileNav.setAttribute('aria-hidden', isExpanded);
      mobileNav.classList.toggle('active');
    });

    // Close menu when clicking on nav link
    const mobileNavLinks = mobileNav.querySelectorAll('a');
    mobileNavLinks.forEach(link => {
      link.addEventListener('click', () => {
        mobileToggle.setAttribute('aria-expanded', 'false');
        mobileNav.setAttribute('aria-hidden', 'true');
        mobileNav.classList.remove('active');
      });
    });
  }

  // --- 3. Language Switcher Dropdown ---
  const langBtn = document.querySelector('.lang-btn');
  const langDropdown = document.querySelector('.lang-dropdown');
  if (langBtn && langDropdown) {
    langBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const isExpanded = langBtn.getAttribute('aria-expanded') === 'true';
      langBtn.setAttribute('aria-expanded', !isExpanded);
      langDropdown.classList.toggle('active');
    });

    document.addEventListener('click', () => {
      langBtn.setAttribute('aria-expanded', 'false');
      langDropdown.classList.remove('active');
    });
  }

  // --- 4. Form Validation & Submission ---
  // --- Callback form: передзвоніть мені ---
  const callbackForm  = document.getElementById('callback-form');
  const callbackPhone = document.getElementById('callback-phone');
  const callbackError = document.getElementById('callback-error');
  const formStatusEl  = document.getElementById('form-status');

  if (callbackForm && callbackPhone) {
    callbackPhone.addEventListener('input', () => {
      if (callbackError) callbackError.style.display = 'none';
    });

    callbackForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const phone  = callbackPhone.value.trim();
      const digits = phone.replace(/\D/g, '');

      if (digits.length < 7) {
        if (callbackError) {
          callbackError.style.display = 'block';
          callbackError.textContent = callbackError.textContent || 'Введіть коректний номер';
        }
        callbackPhone.focus();
        return;
      }

      // Open email client pre-filled
      const subj = encodeURIComponent('Передзвоніть мені — BTC Consulting');
      const body = encodeURIComponent(
        'Будь ласка, передзвоніть мені.\n\nТелефон: ' + phone +
        '\n\nНадіслано з сайту BTC Consulting'
      );
      window.open('mailto:contact@biotc.pl?subject=' + subj + '&body=' + body);

      if (formStatusEl) {
        formStatusEl.className = 'form-status-container success';
        formStatusEl.innerHTML = '<strong>Дякуємо! Натисніть \"Надіслати\" у поштовому клієнті.</strong>';
        formStatusEl.classList.remove('hidden');
      }
      callbackForm.reset();
    });
  }

    // --- 5. Dynamic Clean-Tech Background Animation (Disabled) ---
  const canvas = document.getElementById('bg-canvas');
  if (canvas) {
    canvas.remove();
  }


  // --- Cycling FAB & Contact Popover (phone / mail / chat) ---
  const fab = document.getElementById('nav-fab');
  const contactPopover = document.getElementById('contact-popover');
  const popoverOverlay = document.getElementById('contact-popover-overlay');
  const popoverClose   = document.getElementById('popover-close');
  const downloadBtn    = document.getElementById('vcard-download-btn');
  const popoverFormLink = document.getElementById('popover-form-link');

  if (fab && contactPopover) {
    fab.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      
      const isOpen = contactPopover.classList.toggle('open');
      contactPopover.setAttribute('aria-hidden', String(!isOpen));
      fab.setAttribute('aria-expanded', String(isOpen));
      
      if (popoverOverlay) {
        popoverOverlay.classList.toggle('open', isOpen);
        popoverOverlay.setAttribute('aria-hidden', String(!isOpen));
      }
      
      if (window.innerWidth > 768) {
        const rect = fab.getBoundingClientRect();
        contactPopover.style.top = (rect.bottom + 10) + 'px';
        contactPopover.style.left = (rect.left - 260) + 'px';
      }
    });

    const closePopover = () => {
      contactPopover.classList.remove('open');
      contactPopover.setAttribute('aria-hidden', 'true');
      fab.setAttribute('aria-expanded', 'false');
      if (popoverOverlay) {
        popoverOverlay.classList.remove('open');
        popoverOverlay.setAttribute('aria-hidden', 'true');
      }
    };

    if (popoverClose) {
      popoverClose.addEventListener('click', closePopover);
    }
    if (popoverOverlay) {
      popoverOverlay.addEventListener('click', closePopover);
    }

    document.addEventListener('click', (e) => {
      if (!contactPopover.contains(e.target) && !fab.contains(e.target)) {
        closePopover();
      }
    });

    if (popoverFormLink) {
      popoverFormLink.addEventListener('click', (e) => {
        closePopover();
        const contactSec = document.getElementById('contact');
        if (contactSec) {
          e.preventDefault();
          isNavigatingToContact = true;
          contactSec.scrollIntoView({ behavior: 'smooth' });
          setTimeout(() => {
            isNavigatingToContact = false;
          }, 1200); // Reset after smooth scroll completes
        }
      });
    }

    if (downloadBtn) {
      downloadBtn.addEventListener('click', async (e) => {
        e.preventDefault();
        e.stopPropagation();
        
        let base64Photo = "";
        try {
          const imgUrl = "../img/team/krop-a.jpg";
          const response = await fetch(imgUrl);
          const blob = await response.blob();
          base64Photo = await new Promise((resolve) => {
            const reader = new FileReader();
            reader.onloadend = () => resolve(reader.result.split(',')[1]);
            reader.readAsDataURL(blob);
          });
        } catch (err) {
          console.error("Failed to load Andrzej Krop photo", err);
        }

        const vcardContent = [
          "BEGIN:VCARD",
          "VERSION:3.0",
          "FN:Andrzej Krop",
          "ORG:BTC Consulting",
          "TITLE:Project Manager",
          "TEL;TYPE=WORK,VOICE:+48608003458",
          "EMAIL;TYPE=PREF,INTERNET:contact@biotc.pl",
          "URL:https://biotc.pl",
          base64Photo ? `PHOTO;TYPE=JPEG;ENCODING=b:${base64Photo}` : "",
          "END:VCARD"
        ].filter(Boolean).join("\r\n");

        const blob = new Blob([vcardContent], { type: "text/vcard;charset=utf-8" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "Andrzej_Krop_BTC.vcf";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
      });
    }
    // Cycle icons
    const fabIcons = fab.querySelectorAll('.nav-fab-icon');
    let fabIdx = 0;
    setInterval(() => {
      fabIcons[fabIdx].style.opacity = '0';
      setTimeout(() => {
        fabIcons[fabIdx].style.display = 'none';
        fabIdx = (fabIdx + 1) % fabIcons.length;
        fabIcons[fabIdx].style.display = '';
        fabIcons[fabIdx].style.opacity = '0';
        requestAnimationFrame(() => { fabIcons[fabIdx].style.opacity = '1'; });
      }, 250);
    }, 2500);
  }


  // --- Globe language strip toggle ---
  const globeBtn = document.getElementById('lang-globe-btn');
  const langStrip = document.getElementById('lang-strip');
  if (globeBtn && langStrip) {
    globeBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const open = langStrip.classList.toggle('open');
      langStrip.setAttribute('aria-hidden', String(!open));
      globeBtn.setAttribute('aria-expanded', String(open));
    });
    document.addEventListener('click', () => {
      langStrip.classList.remove('open');
      langStrip.setAttribute('aria-hidden', 'true');
      globeBtn.setAttribute('aria-expanded', 'false');
    });
  }


  // --- Privacy strip: button click + mobile swipe-up from footer ---
  (function() {
    const strip   = document.getElementById('privacy-strip');
    const trigger = document.getElementById('privacy-strip-trigger');
    const closeBtn= document.getElementById('privacy-strip-close');
    if (!strip) return;

    function open() {
      if (strip.classList.contains('open')) return;
      strip.classList.add('open');
      strip.setAttribute('aria-hidden', 'false');
      document.body.style.paddingBottom = strip.offsetHeight + 'px';
    }

    function close() {
      if (!strip.classList.contains('open')) return;
      strip.classList.remove('open');
      strip.setAttribute('aria-hidden', 'true');
      document.body.style.paddingBottom = '';
    }

    function atBottom() {
      return window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 80;
    }

    // Button click
    if (trigger) trigger.addEventListener('click', (e) => { e.preventDefault(); open(); });
    if (closeBtn) closeBtn.addEventListener('click', (e) => { e.preventDefault(); close(); });

    // Swipe up from footer (touch only)
    let touchStartY = 0;
    let startedAtBottom = false;
    document.addEventListener('touchstart', (e) => {
      touchStartY = e.touches[0].clientY;
      startedAtBottom = atBottom();
    }, { passive: true });
    document.addEventListener('touchend', (e) => {
      if (!startedAtBottom || strip.classList.contains('open')) return;
      if (touchStartY - e.changedTouches[0].clientY > 40) open();
    }, { passive: true });

    // Close on scroll away from bottom
    let lastY = window.scrollY;
    window.addEventListener('scroll', () => {
      const y = window.scrollY;
      if (strip.classList.contains('open') && y < lastY && !atBottom()) close();
      lastY = y;
    }, { passive: true });
  })();

}
  // --- Add contact (vCard download) ---
  const vcardBtn = document.getElementById('vcard-btn');
  if (vcardBtn) {
    vcardBtn.addEventListener('click', () => {
      const vcard = [
        'BEGIN:VCARD',
        'VERSION:3.0',
        'FN:BTC Consulting',
        'ORG:BTC Consulting',
        'TEL;TYPE=WORK,VOICE:+48608003458',
        'EMAIL;TYPE=WORK:contact@biotc.pl',
        'URL:https://biotc.pl',
        'ADR;TYPE=WORK:;;ul. Daszynskiego 34/3;Gliwice;;44-100;Poland',
        'END:VCARD'
      ].join('
');
      const blob = new Blob([vcard], { type: 'text/vcard;charset=utf-8' });
      const url  = URL.createObjectURL(blob);
      const a    = document.createElement('a');
      a.href     = url;
      a.download = 'BTC-Consulting.vcf';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    });
  }

});
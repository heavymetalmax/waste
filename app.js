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
  const rfqForm = document.getElementById('rfq-form');
  const formSubmitBtn = document.getElementById('form-submit-btn');
  const formStatus = document.getElementById('form-status');

  const userName = document.getElementById('user-name');
  const userPhone = document.getElementById('user-phone');
  const userCompany = document.getElementById('user-company');

  function validateField(input, errorId) {
    const errorMsg = document.getElementById(errorId);
    if (input && !input.checkValidity() && input.value.trim() !== "") {
      if (errorMsg) errorMsg.style.display = 'block';
    } else {
      if (errorMsg) errorMsg.style.display = 'none';
    }
  }

  const syncAria = (el) => {
    if (el && el.setAttribute) {
      try {
        el.setAttribute('aria-invalid', el.matches(':user-invalid') ? 'true' : 'false');
      } catch (e) {
        // :user-invalid not supported in all browsers
      }
    }
  };

  // Validation listeners
  if (userName) {
    userName.addEventListener('blur', () => { validateField(userName, 'name-error'); syncAria(userName); });
    userName.addEventListener('input', () => {
      const errorMsg = document.getElementById('name-error');
      if (userName.checkValidity() && errorMsg) errorMsg.style.display = 'none';
      syncAria(userName);
    });
  }

  if (userPhone) {
    userPhone.addEventListener('blur', () => { validateField(userPhone, 'phone-error'); syncAria(userPhone); });
    userPhone.addEventListener('input', () => {
      const errorMsg = document.getElementById('phone-error');
      if (userPhone.checkValidity() && errorMsg) errorMsg.style.display = 'none';
      syncAria(userPhone);
    });
  }

  if (userCompany) {
    userCompany.addEventListener('blur', () => { validateField(userCompany, 'company-error'); syncAria(userCompany); });
    userCompany.addEventListener('input', () => {
      const errorMsg = document.getElementById('company-error');
      if (userCompany.checkValidity() && errorMsg) errorMsg.style.display = 'none';
      syncAria(userCompany);
    });
  }

  // Submit handler
  if (rfqForm) {
    rfqForm.addEventListener('submit', (e) => {
      e.preventDefault();

      // Check honeypot
      const honeypot = document.getElementById('honeypot');
      if (honeypot && honeypot.value !== "") {
        console.warn("Spam detected.");
        showFormSuccess();
        rfqForm.reset();
        return;
      }

      // Final validation check
      if (!rfqForm.checkValidity()) {
        validateField(userName, 'name-error');
        validateField(userPhone, 'phone-error');
        validateField(userCompany, 'company-error');

        const firstInvalid = rfqForm.querySelector(':invalid');
        if (firstInvalid) firstInvalid.focus();
        return;
      }

      // Simulate submission
      if (formSubmitBtn) {
        formSubmitBtn.disabled = true;
        formSubmitBtn.textContent = 'Надсилання запиту...';
      }
      if (formStatus) formStatus.classList.add('hidden');

      setTimeout(() => {
        showFormSuccess();
        rfqForm.reset();
      }, 1500);
    });
  }

  function showFormSuccess() {
    if (formSubmitBtn) {
      formSubmitBtn.disabled = false;
      formSubmitBtn.textContent = 'Надіслати заявку на розгляд';
    }

    if (formStatus) {
      formStatus.className = "form-status-container success";
      formStatus.innerHTML = `
        <strong>Дякуємо! Заявку успішно надіслано.</strong><br>
        Наші інженери опрацюють ваші дані та зв'яжуться з вами протягом 1 робочого дня.
      `;
      formStatus.classList.remove('hidden');
      formStatus.focus();
    }
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


  // --- Privacy bottom strip ---
  const privacyTrigger = document.getElementById('privacy-strip-trigger');
  const privacyStrip   = document.getElementById('privacy-strip');
  const privacyClose   = document.getElementById('privacy-strip-close');
  if (privacyTrigger && privacyStrip) {
    let autoCloseTimeout = null;
    let canTrigger = true;

    function showPrivacyStrip() {
      if (privacyStrip.classList.contains('open') || !canTrigger) return;
      privacyStrip.classList.add('open');
      privacyStrip.setAttribute('aria-hidden', 'false');
      canTrigger = false; // Prevent auto-triggering again until user scrolls up

      // Scroll smoothly to reveal the drawer from under the footer
      setTimeout(() => {
        window.scrollTo({
          top: document.body.scrollHeight,
          behavior: 'smooth'
        });
      }, 100);

      // Auto close after 12 seconds (sufficient time to read)
      if (autoCloseTimeout) clearTimeout(autoCloseTimeout);
      autoCloseTimeout = setTimeout(() => {
        hidePrivacyStrip();
      }, 12000);
    }

    function hidePrivacyStrip() {
      if (!privacyStrip.classList.contains('open')) return;
      privacyStrip.classList.remove('open');
      privacyStrip.setAttribute('aria-hidden', 'true');
      if (autoCloseTimeout) clearTimeout(autoCloseTimeout);
    }

    // Trigger on clicking footer link
    privacyTrigger.addEventListener('click', (e) => {
      e.preventDefault();
      canTrigger = true; // Always allow manual trigger on click
      showPrivacyStrip();
    });

    if (privacyClose) {
      privacyClose.addEventListener('click', (e) => {
        e.preventDefault();
        hidePrivacyStrip();
      });
    }

    // Trigger on scrolling to the absolute bottom, close when scrolling up
    let lastScrollY = window.scrollY;
    window.addEventListener('scroll', () => {
      const currentScrollY = window.scrollY;
      const isScrollingUp = currentScrollY < lastScrollY;
      const scrollHeight = document.body.scrollHeight;
      const viewportHeight = window.innerHeight;

      if (privacyStrip.classList.contains('open') && isScrollingUp) {
        hidePrivacyStrip();
      }

      // Reset the trigger permission ONLY if user scrolls up away from bottom
      const distanceFromBottom = scrollHeight - (viewportHeight + currentScrollY);
      if (distanceFromBottom > 120) {
        canTrigger = true;
      }

      // Check if reached absolute bottom (and not scrolling up, and trigger is active)
      const isAtBottom = (viewportHeight + currentScrollY) >= (scrollHeight - 25);
      if (isAtBottom && !isScrollingUp && canTrigger && !isNavigatingToContact) {
        showPrivacyStrip();
      }

      lastScrollY = currentScrollY;
    }, { passive: true });
  }


  // --- Mobile nav strip (replaces full-screen overlay) ---
  const mobileToggle2 = document.querySelector('.mobile-toggle');
  const mobileStrip   = document.getElementById('nav-mobile-strip');
  if (mobileToggle2 && mobileStrip) {
    mobileToggle2.addEventListener('click', (e) => {
      e.stopPropagation();
      const open = mobileStrip.classList.toggle('open');
      mobileStrip.setAttribute('aria-hidden', String(!open));
      mobileToggle2.setAttribute('aria-expanded', String(open));
    });
    document.addEventListener('click', () => {
      mobileStrip.classList.remove('open');
      mobileStrip.setAttribute('aria-hidden', 'true');
      mobileToggle2.setAttribute('aria-expanded', 'false');
    });
  }


  // --- Chat input: follow keyboard on iOS (visualViewport) ---
  const chatTextarea = document.getElementById('srp-chat-input');
  const chatMsgs     = document.getElementById('srp-chat-msgs');
  if (chatTextarea && window.visualViewport) {
    const keepInputVisible = () => {
      if (document.activeElement !== chatTextarea) return;
      // Scroll the page so the input row is just above the keyboard
      chatTextarea.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      if (chatMsgs) chatMsgs.scrollTop = chatMsgs.scrollHeight;
    };
    window.visualViewport.addEventListener('resize', keepInputVisible);
    chatTextarea.addEventListener('focus', () => {
      setTimeout(keepInputVisible, 350); // wait for keyboard to fully open
    });
  }

});
document.addEventListener("DOMContentLoaded", () => {
  // --- 0. Auto Language Detection & Redirect ---
  (function() {
    const savedLang = localStorage.getItem('userLang');
    const path = window.location.pathname;
    // Check if we are on the root site (not inside /eu/ or /pl/)
    const isRoot = !path.includes('/eu/') && !path.includes('/pl/');
    
    if (!savedLang && isRoot) {
      const userLang = (navigator.language || navigator.userLanguage || '').toLowerCase();
      
      if (userLang.startsWith('pl')) {
        localStorage.setItem('userLang', 'pl');
        window.location.href = 'pl/index.html';
      } else if (!userLang.startsWith('uk') && !userLang.startsWith('ru')) {
        // Any other language defaults to EU English
        localStorage.setItem('userLang', 'eu');
        window.location.href = 'eu/index.html';
      } else {
        // Ukrainian and Russian speakers stay on the root Ukrainian version
        localStorage.setItem('userLang', 'uk');
      }
    }
  })();

  // --- 1. Language Detection & Translations ---
  const lang = document.documentElement.lang || 'uk';
  
  const translations = {
    uk: {
      locale: 'uk-UA',
      modelText: {
        'BioTC HTC-S 5': 'BioTC HTC-S 5',
        'BioTC HTC-S 15': 'BioTC HTC-S 15',
        'BioTC HTC-D 30': 'BioTC HTC-D 30',
        'BioTC TH+HTC Custom': 'BioTC TH+HTC Індивідуальна'
      },
      wetInputLabel: 'т/рік',
      hydrocharLabel: 'т/рік',
      energyLabel: 'ГДж/рік',
      co2Label: 'т/рік',
      calcMessage: (model, load) => `Мене цікавить розрахунок системи молекулярного рекомбінування на базі моделі ${model} для об'єкта потужністю ${load}. Надішліть, будь ласка, попереднє ТЕО та комерційну пропозицію.`,
      rlmUnit: 'RLM (еквівалент населення)',
      tonsUnit: 'т/добу сировини',
      submitting: 'Надсилання запиту...',
      submitBtnText: 'Надіслати запит на ТЕО',
      successHeader: 'Дякуємо! Запит на ТЕО успішно надіслано.',
      successBody: 'Наші провідні інженери опрацюють ваші вихідні дані та зв\'яжуться з вами для уточнення деталей проекту.'
    },
    en: {
      locale: 'en-US',
      modelText: {
        'BioTC HTC-S 5': 'BioTC HTC-S 5',
        'BioTC HTC-S 15': 'BioTC HTC-S 15',
        'BioTC HTC-D 30': 'BioTC HTC-D 30',
        'BioTC TH+HTC Custom': 'BioTC TH+HTC Custom'
      },
      wetInputLabel: 't/year',
      hydrocharLabel: 't/year',
      energyLabel: 'GJ/year',
      co2Label: 't/year',
      calcMessage: (model, load) => `I am interested in the molecular rearrangement system based on the ${model} model for a facility with a capacity of ${load}. Please send a preliminary feasibility study and commercial proposal.`,
      rlmUnit: 'PE (population equivalent)',
      tonsUnit: 't/day of organic feedstock',
      submitting: 'Sending request...',
      submitBtnText: 'Send Request for Feasibility Study',
      successHeader: 'Thank you! Your request has been successfully sent.',
      successBody: 'Our leading engineers will analyze your input parameters and contact you to clarify the details of the project.'
    },
    pl: {
      locale: 'pl-PL',
      modelText: {
        'BioTC HTC-S 5': 'BioTC HTC-S 5',
        'BioTC HTC-S 15': 'BioTC HTC-S 15',
        'BioTC HTC-D 30': 'BioTC HTC-D 30',
        'BioTC TH+HTC Custom': 'BioTC TH+HTC Dedykowana'
      },
      wetInputLabel: 't/rok',
      hydrocharLabel: 't/rok',
      energyLabel: 'GJ/rok',
      co2Label: 't/rok',
      calcMessage: (model, load) => `Interesuje mnie kalkulacja systemu rekombinacji molekularnej w oparciu o model ${model} dla obiektu o wydajności ${load}. Proszę o przesłanie wstępnego studium wykonalności i oferty handlowej.`,
      rlmUnit: 'RLM (równoważna liczba mieszkańców)',
      tonsUnit: 't/dobę surowca organicznego',
      submitting: 'Wysyłanie zapytania...',
      submitBtnText: 'Wyślij zapytanie o studium wykonalności',
      successHeader: 'Dziękujemy! Zapytanie zostało pomyślnie wysłane.',
      successBody: 'Nasi wiodący inżynierowie przeanalizują Twoje dane wejściowe i skontaktują się z Tobą w celu ustalenia szczegółów projektu.'
    }
  };

  const t = translations[lang] || translations.uk;

  // --- 2. Shrinking Header on Scroll ---
  const header = document.getElementById('header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('shrink');
    } else {
      header.classList.remove('shrink');
    }
  });

  // --- 3. Mobile Menu Toggle ---
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

  // --- 4. Language Switcher Dropdown Click (Accessibility) ---
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

  // --- 5. Wastewater HTC Calculator Logic ---
  const calcByRlm = document.getElementById('calc-by-rlm');
  const calcByTons = document.getElementById('calc-by-tons');

  const inputsRlm = document.getElementById('inputs-rlm');
  const inputsTons = document.getElementById('inputs-tons');

  const rlmCount = document.getElementById('rlm-count');
  const rlmVal = document.getElementById('rlm-val');
  const tonsCount = document.getElementById('tons-count');
  const tonsVal = document.getElementById('tons-val');

  const recommendedModel = document.getElementById('recommended-model');
  const wetInputVal = document.getElementById('wet-input-val');
  const hydrocharVal = document.getElementById('hydrochar-val');
  const energyVal = document.getElementById('energy-val');
  const co2Val = document.getElementById('co2-val');
  const preselectedModelInput = document.getElementById('preselected-model');

  // Helper to switch input groups
  function showInputGroup(group) {
    [inputsRlm, inputsTons].forEach(g => {
      if (g) g.classList.remove('active');
    });
    if (group) group.classList.add('active');
  }

  // Calculation logic
  function calculate() {
    const activeModeEl = document.querySelector('input[name="calc-mode"]:checked');
    if (!activeModeEl) return;
    
    let mode = activeModeEl.value;
    let wetSludgeTonsPerDay = 0;
    let rlm = 0;

    if (mode === 'rlm' && rlmCount) {
      rlm = parseInt(rlmCount.value);
      if (rlmVal) {
        rlmVal.textContent = rlm.toLocaleString(t.locale);
      }
      // 1 PE (RLM) generates ~0.3 kg of wet sludge (at 80% moisture) per day
      wetSludgeTonsPerDay = (rlm * 0.3) / 1000;
    } else if (mode === 'tons' && tonsCount) {
      wetSludgeTonsPerDay = parseFloat(tonsCount.value);
      if (tonsVal) {
        tonsVal.textContent = wetSludgeTonsPerDay.toLocaleString(t.locale, { minimumFractionDigits: 1, maximumFractionDigits: 1 });
      }
      // Back-calculate equivalent RLM
      rlm = Math.round((wetSludgeTonsPerDay * 1000) / 0.3);
    }

    // Recommended BioTC Model Selection based on wet sludge tonnage per day
    let modelName = "BioTC HTC-S 5";
    if (wetSludgeTonsPerDay <= 5.0) {
      modelName = "BioTC HTC-S 5";
    } else if (wetSludgeTonsPerDay <= 15.0) {
      modelName = "BioTC HTC-S 15";
    } else if (wetSludgeTonsPerDay <= 30.0) {
      modelName = "BioTC HTC-D 30";
    } else {
      modelName = "BioTC TH+HTC Custom";
    }

    // Formulas:
    // Wet sludge processed per year
    const wetInputYear = Math.round(wetSludgeTonsPerDay * 365);
    // Hydrochar yield is ~22% of wet sludge weight (due to 75% mass reduction + dryness)
    const hydrocharYear = Math.round(wetInputYear * 0.22);
    // Hydrochar has energy density of ~20 GJ/ton
    const energyYear = Math.round(hydrocharYear * 20);
    // Estimated CO2 savings: ~1.2 tons of CO2 per ton of hydrochar
    const co2Year = Math.round(hydrocharYear * 1.2);

    // Display values
    if (recommendedModel) {
      recommendedModel.textContent = t.modelText[modelName] || modelName;
    }
    const lpRecModel = document.getElementById('model-recommendation');
    if (lpRecModel) {
      lpRecModel.textContent = t.modelText[modelName] || modelName;
    }

    if (wetInputVal) {
      wetInputVal.textContent = `${wetInputYear.toLocaleString(t.locale)} ${t.wetInputLabel}`;
    }
    const lpWetInput = document.getElementById('wet-input-output');
    if (lpWetInput) {
      lpWetInput.textContent = `${wetInputYear.toLocaleString(t.locale)} ${t.wetInputLabel}`;
    }

    if (hydrocharVal) {
      hydrocharVal.textContent = `${hydrocharYear.toLocaleString(t.locale)} ${t.hydrocharLabel}`;
    }
    const lpHydrochar = document.getElementById('hydrochar-output');
    if (lpHydrochar) {
      lpHydrochar.textContent = `${hydrocharYear.toLocaleString(t.locale)} ${t.hydrocharLabel}`;
    }

    if (energyVal) {
      energyVal.textContent = `${energyYear.toLocaleString(t.locale)} ${t.energyLabel}`;
    }
    const lpEnergy = document.getElementById('energy-output');
    if (lpEnergy) {
      lpEnergy.textContent = `${energyYear.toLocaleString(t.locale)} ${t.energyLabel}`;
    }

    if (co2Val) {
      co2Val.textContent = `~${co2Year.toLocaleString(t.locale)} ${t.co2Label}`;
    }
    const lpCo2 = document.getElementById('co2-output');
    if (lpCo2) {
      lpCo2.textContent = `~${co2Year.toLocaleString(t.locale)} ${t.co2Label}`;
    }

    if (preselectedModelInput) {
      preselectedModelInput.value = modelName;
    }

    // Update hidden inputs for landing page
    const formRecModel = document.getElementById('form-rec-model');
    if (formRecModel) {
      formRecModel.value = modelName;
    }

    const formCalcLoad = document.getElementById('form-calc-load');
    if (formCalcLoad) {
      let loadText = "";
      if (mode === 'rlm' && rlmCount) {
        loadText = `${parseInt(rlmCount.value).toLocaleString(t.locale)} ${t.rlmUnit}`;
      } else if (tonsCount) {
        loadText = `${parseFloat(tonsCount.value).toLocaleString(t.locale, { minimumFractionDigits: 1, maximumFractionDigits: 1 })} ${t.tonsUnit}`;
      }
      formCalcLoad.value = loadText;
    }

    // Dynamic message update for landing page form
    const lpMessage = document.getElementById('contact-message');
    if (lpMessage) {
      let loadText = "";
      if (mode === 'rlm' && rlmCount) {
        loadText = `${parseInt(rlmCount.value).toLocaleString(t.locale)} ${t.rlmUnit}`;
      } else if (tonsCount) {
        loadText = `${parseFloat(tonsCount.value).toLocaleString(t.locale, { minimumFractionDigits: 1, maximumFractionDigits: 1 })} ${t.tonsUnit}`;
      }
      lpMessage.value = t.calcMessage(modelName, loadText);
    }
  }

  // Add event listeners for calculator triggers
  if (calcByRlm && calcByTons) {
    [calcByRlm, calcByTons].forEach(radio => {
      radio.addEventListener('change', () => {
        if (calcByRlm.checked) {
          showInputGroup(inputsRlm);
        } else {
          showInputGroup(inputsTons);
        }
        calculate();
      });
    });
  }

  if (rlmCount) {
    rlmCount.addEventListener('input', calculate);
  }
  if (tonsCount) {
    tonsCount.addEventListener('input', calculate);
  }

  // Pre-calculate initially
  calculate();

  // CTA button in calculator scrolls down and presets message details
  const calcCtaBtn = document.getElementById('calc-cta-btn');
  const userMessage = document.getElementById('user-message');
  if (calcCtaBtn && userMessage) {
    calcCtaBtn.addEventListener('click', () => {
      const selectedModel = preselectedModelInput ? preselectedModelInput.value : "BioTC HTC-S 5";
      const activeModeEl = document.querySelector('input[name="calc-mode"]:checked');
      const mode = activeModeEl ? activeModeEl.value : 'rlm';
      let loadText = "";

      if (mode === 'rlm' && rlmCount) {
        loadText = `${parseInt(rlmCount.value).toLocaleString(t.locale)} ${t.rlmUnit}`;
      } else if (tonsCount) {
        loadText = `${parseFloat(tonsCount.value).toLocaleString(t.locale, { minimumFractionDigits: 1, maximumFractionDigits: 1 })} ${t.tonsUnit}`;
      }

      userMessage.value = t.calcMessage(selectedModel, loadText);
      
      // Scroll smoothly to contact section
      const contactSection = document.getElementById('contact');
      if (contactSection) {
        contactSection.scrollIntoView({ behavior: 'smooth' });
        
        // Focus the name input for accessibility
        const nameInput = document.getElementById('user-name');
        if (nameInput) {
          setTimeout(() => nameInput.focus(), 800);
        }
      }
    });
  }

  // --- 6. Interactive Product Showroom Tabs ---
  const tabs = document.querySelectorAll('.tab-btn');
  const panels = document.querySelectorAll('.tab-panel');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      // Deactivate all tabs
      tabs.forEach(t => {
        t.classList.remove('active');
        t.setAttribute('aria-selected', 'false');
      });

      // Hide all panels
      panels.forEach(p => p.classList.add('hidden'));

      // Activate clicked tab
      tab.classList.add('active');
      tab.setAttribute('aria-selected', 'true');

      // Show associated panel
      const targetId = tab.getAttribute('aria-controls');
      const targetPanel = document.getElementById(targetId);
      if (targetPanel) {
        targetPanel.classList.remove('hidden');
      }
    });
  });

  // --- 6b. Alternative LP Showroom Tabs ---
  const lpTabButtons = document.querySelectorAll('.tab-header .tab-btn');
  const lpTabContents = document.querySelectorAll('.tab-content-wrapper .tab-content');

  if (lpTabButtons.length > 0 && lpTabContents.length > 0) {
    lpTabButtons.forEach(tab => {
      tab.addEventListener('click', () => {
        // Deactivate all LP tabs
        lpTabButtons.forEach(t => {
          t.classList.remove('active');
          t.setAttribute('aria-selected', 'false');
        });
        // Hide all LP contents
        lpTabContents.forEach(c => c.classList.add('hidden'));

        // Activate clicked tab
        tab.classList.add('active');
        tab.setAttribute('aria-selected', 'true');

        // Show target content
        const targetId = tab.getAttribute('data-tab');
        const targetContent = document.getElementById(targetId);
        if (targetContent) {
          targetContent.classList.remove('hidden');
        }
      });
    });
  }

  // --- 7. Form Validation & AJAX Mocking ---
  const rfqForm = document.getElementById('rfq-form');
  const formSubmitBtn = document.getElementById('form-submit-btn');
  const formStatus = document.getElementById('form-status');

  // Input elements for validation
  const userName = document.getElementById('user-name');
  const userPhone = document.getElementById('user-phone');
  const userEmail = document.getElementById('user-email');
  const userCompany = document.getElementById('user-company');

  // Validate single field helper
  function validateField(input, errorId) {
    const errorMsg = document.getElementById(errorId);
    if (input && !input.checkValidity() && input.value.trim() !== "") {
      if (errorMsg) errorMsg.style.display = 'block';
    } else {
      if (errorMsg) errorMsg.style.display = 'none';
    }
  }

  // Sync aria-invalid with the CSS :user-invalid state
  const syncAria = (el) => {
    if (el && el.setAttribute) {
      el.setAttribute('aria-invalid', el.matches(':user-invalid') ? 'true' : 'false');
    }
  };

  // Validation event listeners following Web Guidance rules
  if (userName) {
    userName.addEventListener('blur', () => {
      validateField(userName, 'name-error');
      syncAria(userName);
    });
    userName.addEventListener('input', () => {
      const errorMsg = document.getElementById('name-error');
      if (userName.checkValidity() && errorMsg) {
        errorMsg.style.display = 'none';
      }
      syncAria(userName);
    });
  }

  if (userPhone) {
    userPhone.addEventListener('blur', () => {
      validateField(userPhone, 'phone-error');
      syncAria(userPhone);
    });
    userPhone.addEventListener('input', () => {
      const errorMsg = document.getElementById('phone-error');
      if (userPhone.checkValidity() && errorMsg) {
        errorMsg.style.display = 'none';
      }
      syncAria(userPhone);
    });
  }

  if (userEmail) {
    userEmail.addEventListener('blur', () => {
      validateField(userEmail, 'email-error');
      syncAria(userEmail);
    });
    userEmail.addEventListener('input', () => {
      const errorMsg = document.getElementById('email-error');
      if (userEmail.checkValidity() && errorMsg) {
        errorMsg.style.display = 'none';
      }
      syncAria(userEmail);
    });
  }

  if (userCompany) {
    userCompany.addEventListener('blur', () => {
      validateField(userCompany, 'company-error');
      syncAria(userCompany);
    });
    userCompany.addEventListener('input', () => {
      const errorMsg = document.getElementById('company-error');
      if (userCompany.checkValidity() && errorMsg) {
        errorMsg.style.display = 'none';
      }
      syncAria(userCompany);
    });
  }

  // Submit Handler
  if (rfqForm) {
    rfqForm.addEventListener('submit', (e) => {
      e.preventDefault();

      // Check honeypot spam prevention
      const honeypot = document.getElementById('honeypot');
      if (honeypot && honeypot.value !== "") {
        console.warn("Spam detected via honeypot field.");
        showFormSuccess();
        rfqForm.reset();
        return;
      }

      // Final constraint validation check
      if (!rfqForm.checkValidity()) {
        validateField(userName, 'name-error');
        validateField(userPhone, 'phone-error');
        validateField(userEmail, 'email-error');
        validateField(userCompany, 'company-error');
        
        const firstInvalid = rfqForm.querySelector(':invalid');
        if (firstInvalid) {
          firstInvalid.focus();
        }
        return;
      }

      // Valid form - process submission
      if (formSubmitBtn) {
        formSubmitBtn.disabled = true;
        formSubmitBtn.textContent = t.submitting;
      }
      if (formStatus) {
        formStatus.classList.add('hidden');
      }

      // Simulate AJAX call (1.5 seconds)
      setTimeout(() => {
        showFormSuccess();
        rfqForm.reset();
      }, 1500);
    });
  }

  function showFormSuccess() {
    if (formSubmitBtn) {
      formSubmitBtn.disabled = false;
      formSubmitBtn.textContent = t.submitBtnText;
    }
    
    if (formStatus) {
      formStatus.className = "form-status-container success";
      formStatus.innerHTML = `
        <strong>${t.successHeader}</strong><br>
        ${t.successBody}
      `;
      formStatus.classList.remove('hidden');
      formStatus.focus();
    }
  }

  // --- 8. Dynamic Clean-Tech Background Animation (Ultra-Optimized Fluid Flow) ---
  const canvas = document.getElementById('bg-canvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let animationFrameId = null;
    let width = 0;
    let height = 0;
    let lastKnownWidth = 0;
    let dpr = 1;
    let particles = [];
    let vortices = [];
    let isLooping = false;
    let resizeTimer = null;

    // Detect user preferences for motion
    const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');

    function getViewportSize() {
      // visualViewport gives stable dimensions on mobile (not affected by pinch zoom)
      const vv = window.visualViewport;
      if (vv) {
        return { w: vv.width, h: vv.height };
      }
      return { w: window.innerWidth, h: window.innerHeight };
    }

    function resizeCanvas() {
      const viewport = getViewportSize();
      const newWidth = Math.round(viewport.w);

      // On mobile, skip resize if only height changed (address bar show/hide)
      if (lastKnownWidth > 0 && newWidth === lastKnownWidth) {
        // Only update the logical height for scroll-boundary checks
        height = Math.round(viewport.h);
        return;
      }

      lastKnownWidth = newWidth;
      dpr = Math.min(window.devicePixelRatio || 1, 1.5); // Cap DPR at 1.5 for performance
      width = newWidth;
      height = Math.round(viewport.h);

      // Cap canvas buffer resolution (max ~1.5M pixels) to prevent GPU memory spikes
      const maxBuf = 1500000;
      const bufW = width * dpr;
      const bufH = height * dpr;
      const bufScale = (bufW * bufH > maxBuf) ? Math.sqrt(maxBuf / (bufW * bufH)) : 1;

      canvas.width = Math.round(bufW * bufScale);
      canvas.height = Math.round(bufH * bufScale);
      ctx.setTransform(dpr * bufScale, 0, 0, dpr * bufScale, 0, 0);

      initParticles();
    }

    function initParticles() {
      particles = [];
      const particleCount = Math.min(Math.round((width * height) / 12000), 100);
      for (let i = 0; i < particleCount; i++) {
        particles.push(createParticle(true));
      }
    }

    function createParticle(randomY = false) {
      return {
        x: Math.random() * width,
        y: randomY ? Math.random() * height : -20,
        vx: (Math.random() - 0.5) * 0.5,
        vy: 1 + Math.random() * 1.5,
        size: 3 + Math.random() * 3,
        state: randomY ? (Math.random() > 0.5 ? 'falling' : 'rising') : 'falling',
        restTime: 100 + Math.random() * 150,
        alpha: 0.7 + Math.random() * 0.3,
        lightness: 10,
        seed: Math.random() * 100
      };
    }

    function draw() {
      if (window.scrollY > height) {
        stopLoop();
        return;
      }

      ctx.clearRect(0, 0, width, height);
      const time = Date.now() * 0.001;
      const len = particles.length;

      for (let i = 0; i < len; i++) {
        const p = particles[i];

        if (p.state === 'falling') {
          p.y += p.vy;
          p.x += Math.sin(time + p.seed) * 0.3;
          if (p.lightness < 30) p.lightness += 0.05;
          
          if (p.y > height - 20 - Math.random() * 100) {
            p.state = 'resting';
            p.vy = 0;
          }
        } else if (p.state === 'resting') {
          p.restTime--;
          p.x += Math.sin(time * 2 + p.seed) * 0.1;
          if (p.lightness < 50) p.lightness += 0.1;
          
          if (p.restTime <= 0) {
            p.state = 'rising';
            p.vy = -1 - Math.random() * 1.5;
          }
        } else if (p.state === 'rising') {
          p.y += p.vy;
          p.x += Math.sin(time + p.seed) * 0.5;
          if (p.lightness < 95) p.lightness += 0.2;
          if (p.size > 0.5) p.size -= 0.015;
          
          if (p.y < height * 0.35) {
            p.alpha -= 0.008;
          }
        }

        if (p.alpha <= 0 || p.y < -50 || p.x < -50 || p.x > width + 50) {
          particles[i] = createParticle();
          continue;
        }

        ctx.fillStyle = `hsla(210, 80%, ${Math.round(p.lightness)}%, ${p.alpha})`;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fill();
      }

      if (!motionQuery.matches && document.visibilityState === 'visible' && isLooping) {
        animationFrameId = requestAnimationFrame(draw);
      }
    }

    function startLoop() {
      if (!isLooping && !motionQuery.matches) {
        isLooping = true;
        animationFrameId = requestAnimationFrame(draw);
      }
    }

    function stopLoop() {
      if (isLooping) {
        isLooping = false;
        if (animationFrameId) {
          cancelAnimationFrame(animationFrameId);
          animationFrameId = null;
        }
      }
    }

    // Scroll listener to resume when Hero is visible, and pause when scrolled down
    window.addEventListener('scroll', () => {
      if (window.scrollY < height) {
        startLoop();
      } else {
        stopLoop();
      }
    }, { passive: true }); // passive listener for high scroll performance

    // Initialize
    resizeCanvas();

    // Debounced resize to prevent layout thrashing on mobile (address bar hide/show)
    function debouncedResize() {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(resizeCanvas, 150);
    }
    window.addEventListener('resize', debouncedResize);
    // Also listen to visualViewport resize for better mobile support
    if (window.visualViewport) {
      window.visualViewport.addEventListener('resize', debouncedResize);
    }

    document.addEventListener('visibilitychange', () => {
      if (document.visibilityState === 'visible') {
        if (window.scrollY < height) startLoop();
      } else {
        stopLoop();
      }
    });

    motionQuery.addEventListener('change', (e) => {
      if (e.matches) {
        stopLoop();
        draw(); // Single static frame
      } else {
        startLoop();
      }
    });

    // Initial render trigger
    if (motionQuery.matches) {
      draw();
    } else {
      startLoop();
    }
  }

});
document.addEventListener('DOMContentLoaded', () => {
  // --- Retro-Tech Analytics Simulator Logic ---
  
  // 1. Language detection
  const path = window.location.pathname;
  let currentLang = 'uk';
  if (path.includes('/eu/')) currentLang = 'en';
  else if (path.includes('/pl/')) currentLang = 'pl';

  // 2. Translations mapping
  const simT = {
    uk: {
      stepLabel: "КРОК",
      enterPe: "Введіть навантаження (PE)",
      enterTons: "Введіть масу осаду (т/добу)",
      disposalTariff: "Тариф утилізації (€/т)",
      enterTs: "Вміст сухих речовин (% TS)",
      enterVs: "Вміст органіки (% VS)",
      readyText: "ГОТОВИЙ ДО ОБЧИСЛЕННЯ",
      calculating: "ОБЧИСЛЕННЯ...",
      doneText: "ОБЧИСЛЕННЯ ЗАВЕРШЕНО",
      givenPe: (val) => `PE = ${formatNumber(val)} осіб`,
      givenTons: (val) => `Маса осаду = ${val} т/добу`,
      givenDisposal: (val) => `C_disposal = ${val} €/т`,
      givenTs: (val) => `TS = ${val}%`,
      givenVs: (val) => `VS = ${val}%`,
      // calculations text
      calcSludge: (val, pe, ts) => pe 
        ? `M_sludge = (PE * 60 * 365) / (10^6 * TS)\nM_sludge = (${formatNumber(pe)} * 60 * 365) / (10^6 * ${ts/100}) = ${formatNumber(val)} т/рік (вологий осад)`
        : `M_sludge = M_daily * 365\nM_sludge = ${formatNumber(val/365, 1)} * 365 = ${formatNumber(val)} т/рік (вологий осад)`,
      calcChar: (val, sludgeVal, ts) => `M_hydrochar = (M_sludge * TS * 0.65) / 0.60\nM_hydrochar = (${formatNumber(sludgeVal)} * ${ts/100} * 0.65) / 0.60 = ${formatNumber(val)} т/рік (при вологості 40%)`,
      calcSavings: (val, opex, disposal) => `Savings = (M_sludge * C_disposal) - OPEX\nSavings = (${formatNumber(val)} * ${disposal} €) - ${formatNumber(opex)} € = ${formatNumber(val * disposal - opex)} €/рік`,
      calcPayback: (model, capex, savings, years) => `Установка: ${model}\nCAPEX = ${formatNumber(capex)} €\nROI (Окупність) = CAPEX / Savings = ${years} р.`,
      calcInaction: (coi) => `Cost of Inaction (Втрати за 7 років бездії) = ${formatNumber(coi)} €`,
      calcTrucks: (trucks) => `Скорочення трафіку = -${formatNumber(trucks)} вант./рік`,
      calcTrees: (trees) => `Компенсація CO2 = ${formatNumber(trees)} дерев/рік`,
      saveTitle: "Зберегти протокол розрахунку (PDF на Email):",
      emailPlaceholder: "Ваш робочий Email",
      submitBtn: "ВІДПРАВИТИ",
      successMsg: "Протокол відправлено. Перевірте пошту.",
      presetsHeader: "Сценарії моделювання (попередні налаштування):",
      presetsInitDesc: "Оберіть готовий сценарій, щоб запустити швидку симуляцію, або скористайтеся клавіатурою калькулятора ліворуч для ручного введення.",
      presetsList: {
        municipality_10k: {
          title: "Громада / Мале місто (10,000 PE)",
          desc: "Типове рішення для невеликих ОТГ чи містечок. Автоматично підбирає компактну установку BioTC HTC-S 5."
        },
        municipality_50k: {
          title: "Середній міський водоканал (50,000 PE)",
          desc: "Базовий сценарій для великого району. Демонструє оптимальну модель BioTC HTC-S 15 та швидку окупність."
        },
        agro_10k: {
          title: "Агропідприємство / Птахофабрика (10k т/рік)",
          desc: "Кейс для приватного бізнесу. Перемикає калькулятор у режим «Тонни» з вмістом органіки (75% VS)."
        },
        food_30t: {
          title: "Харчова промисловість / Пивзавод (30 т/добу)",
          desc: "Промисловий кейс для відходів з високою початковою вологістю. Окупність на логістиці."
        },
        digestion_boost: {
          title: "WWTP з метантенками (Digestion Boost)",
          desc: "Сценарій для великих очисних споруд, де вже добувають біогаз. Перемикає систему в режим TH+HTC."
        }
      }
    },
    en: {
      stepLabel: "STEP",
      enterPe: "Enter population equivalent (PE)",
      enterTons: "Enter sludge mass (t/day)",
      disposalTariff: "Disposal tariff (€/t)",
      enterTs: "Dry solids content (% TS)",
      enterVs: "Volatile solids content (% VS)",
      readyText: "READY FOR CALCULATION",
      calculating: "CALCULATING...",
      doneText: "CALCULATION COMPLETE",
      givenPe: (val) => `PE = ${formatNumber(val)} people`,
      givenTons: (val) => `Sludge mass = ${val} t/day`,
      givenDisposal: (val) => `C_disposal = ${val} €/t`,
      givenTs: (val) => `TS = ${val}%`,
      givenVs: (val) => `VS = ${val}%`,
      // calculations text
      calcSludge: (val, pe, ts) => pe 
        ? `M_sludge = (PE * 60 * 365) / (10^6 * TS)\nM_sludge = (${formatNumber(pe)} * 60 * 365) / (10^6 * ${ts/100}) = ${formatNumber(val)} t/year (wet sludge)`
        : `M_sludge = M_daily * 365\nM_sludge = ${formatNumber(val/365, 1)} * 365 = ${formatNumber(val)} t/year (wet sludge)`,
      calcChar: (val, sludgeVal, ts) => `M_hydrochar = (M_sludge * TS * 0.65) / 0.60\nM_hydrochar = (${formatNumber(sludgeVal)} * ${ts/100} * 0.65) / 0.60 = ${formatNumber(val)} t/year (at 40% moisture)`,
      calcSavings: (val, opex, disposal) => `Savings = (M_sludge * C_disposal) - OPEX\nSavings = (${formatNumber(val)} * ${disposal} €) - ${formatNumber(opex)} € = ${formatNumber(val * disposal - opex)} €/year`,
      calcPayback: (model, capex, savings, years) => `System model: ${model}\nCAPEX = ${formatNumber(capex)} €\nROI (Payback Period) = CAPEX / Savings = ${years} years`,
      calcInaction: (coi) => `Cost of Inaction (7-year expenses) = ${formatNumber(coi)} €`,
      calcTrucks: (trucks) => `Traffic reduction = -${formatNumber(trucks)} trucks/year`,
      calcTrees: (trees) => `CO2 offset equivalent = ${formatNumber(trees)} trees/year`,
      saveTitle: "Save Calculation Protocol (PDF to Email):",
      emailPlaceholder: "Your work Email",
      submitBtn: "SUBMIT",
      successMsg: "Protocol sent. Check your inbox.",
      presetsHeader: "Predefined Modeling Scenarios (Presets):",
      presetsInitDesc: "Select a predefined scenario to run an automated simulation, or use the keypad on the left for manual input.",
      presetsList: {
        municipality_10k: {
          title: "Community / Small Town (10,000 PE)",
          desc: "Typical solution for small municipalities. Automatically selects the compact BioTC HTC-S 5 unit."
        },
        municipality_50k: {
          title: "Medium City Water Utility (50,000 PE)",
          desc: "Baseline scenario for a large municipality. Demonstrates the optimal BioTC HTC-S 15 model and rapid payback."
        },
        agro_10k: {
          title: "Agricultural Enterprise / Poultry Farm (10k t/y)",
          desc: "Switches the simulator to 'Tons/day' mode with organic content (75% VS) to boost hydrochar calorific value."
        },
        food_30t: {
          title: "Food Processing / Brewery (30 t/day)",
          desc: "Industrial case for highly organic sludge. Shows how HTC saves millions on dewatering and logistics."
        },
        digestion_boost: {
          title: "WWTP with Anaerobic Digesters (Digestion Boost)",
          desc: "Scenario for large wastewater plants with existing biogas digestors. Switches system to TH+HTC mode."
        }
      }
    },
    pl: {
      stepLabel: "KROK",
      enterPe: "Wpisz równoważną liczbę mieszkańców (RLM)",
      enterTons: "Wpisz masę osadu (t/dobę)",
      disposalTariff: "Koszt utylizacji (€/t)",
      enterTs: "Sucha masa (% TS)",
      enterVs: "Zawartość substancji organicznych (% VS)",
      readyText: "GOTOWY DO OBLICZEŃ",
      calculating: "OBLICZANIE...",
      doneText: "OBLICZENIA ZAKOŃCZONE",
      givenPe: (val) => `PE = ${formatNumber(val)} mieszkańców`,
      givenTons: (val) => `Masa osadu = ${val} t/dobę`,
      givenDisposal: (val) => `C_disposal = ${val} €/t`,
      givenTs: (val) => `TS = ${val}%`,
      givenVs: (val) => `VS = ${val}%`,
      // calculations text
      calcSludge: (val, pe, ts) => pe 
        ? `M_sludge = (PE * 60 * 365) / (10^6 * TS)\nM_sludge = (${formatNumber(pe)} * 60 * 365) / (10^6 * ${ts/100}) = ${formatNumber(val)} t/rok (osad wilgotny)`
        : `M_sludge = M_daily * 365\nM_sludge = ${formatNumber(val/365, 1)} * 365 = ${formatNumber(val)} t/rok (osad wilgotny)`,
      calcChar: (val, sludgeVal, ts) => `M_hydrochar = (M_sludge * TS * 0.65) / 0.60\nM_hydrochar = (${formatNumber(sludgeVal)} * ${ts/100} * 0.65) / 0.60 = ${formatNumber(val)} t/rok (przy wilgotności 40%)`,
      calcSavings: (val, opex, disposal) => `Savings = (M_sludge * C_disposal) - OPEX\nSavings = (${formatNumber(val)} * ${disposal} €) - ${formatNumber(opex)} € = ${formatNumber(val * disposal - opex)} €/rok`,
      calcPayback: (model, capex, savings, years) => `Model instalacji: ${model}\nCAPEX = ${formatNumber(capex)} €\nROI (Okres zwrotu) = CAPEX / Savings = ${years} lat`,
      calcInaction: (coi) => `Cost of Inaction (Straty przez 7 lat) = ${formatNumber(coi)} €`,
      calcTrucks: (trucks) => `Redukcja transportu = -${formatNumber(trucks)} ciężarówek/rok`,
      calcTrees: (trees) => `Kompensacja CO2 = ${formatNumber(trees)} drzew/rok`,
      saveTitle: "Zapisz protokół obliczeniowy (PDF na Email):",
      emailPlaceholder: "Twój służbowy Email",
      submitBtn: "WYŚLIJ",
      successMsg: "Protokół wysłany. Sprawdź skrzynkę odbiorczą.",
      presetsHeader: "Predefiniowane scenariusze modelowania (presety):",
      presetsInitDesc: "Wybierz gotowy scenariusz, aby uruchomić automatyczną symulację, lub użyj klawiatury po lewej stronie.",
      presetsList: {
        municipality_10k: {
          title: "Gmina / Małe Miasto (10,000 PE)",
          desc: "Rozwiązanie dla małych gmin borykających się z poletkami osadowymi. Dobiera instalację BioTC HTC-S 5."
        },
        municipality_50k: {
          title: "Średnie Miejskie Wodociągi (50,000 PE)",
          desc: "Scenariusz dla centrum regionalnego. Pokazuje optymalny model BioTC HTC-S 15 i szybki zwrot."
        },
        agro_10k: {
          title: "Gospodarstwo Rolne / Ferma Drobiu (10k t/rok)",
          desc: "Przypadek dla biznesu prywatnego. Przełącza kalkulator w tryb „Tony” z wysoką zawartością substancji organicznych (75% VS)."
        },
        food_30t: {
          title: "Food Processing / Browar (30 t/dobę)",
          desc: "Przypadek przemysłowy dla odpadów z wysoką początkową wilgotnością. Pokazuje oszczędności na logistyce."
        },
        digestion_boost: {
          title: "WWTP z komorami fermentacyjnymi (Digestion Boost)",
          desc: "Scenariusz dla oczyszczalni ścieków z fermentacją beztlenową. Przełącza system w tryb TH+HTC."
        }
      }
    }
  };

  const t = simT[currentLang] || simT.uk;

  // DOM elements
  const lcdStep = document.getElementById('lcd-step');
  const lcdPrompt = document.getElementById('lcd-prompt');
  
  const toggleInputMode = document.getElementById('toggle-input-mode');
  const toggleDetailMode = document.getElementById('toggle-detail-mode');
  
  const lblPe = document.getElementById('lbl-pe');
  const lblTons = document.getElementById('lbl-tons');
  const lblStd = document.getElementById('lbl-std');
  const lblExp = document.getElementById('lbl-exp');
  
  const keyClear = document.getElementById('key-clear');
  const keyEnter = document.getElementById('key-enter');
  const keys = document.querySelectorAll('.key-btn');
  
  const paperBody = document.getElementById('paper-body');

  // State
  let currentStepIndex = 0;
  let currentValue = "";
  let isDone = false;
  let isPresetRunning = false;
  let steps = [];
  let values = {
    pe: null,
    tons: null,
    disposal: null,
    ts: null,
    vs: null
  };

  // Helper formatting function
  function formatNumber(num) {
    return new Intl.NumberFormat('en-US').format(Math.round(num));
  }

  // Define steps based on toggles
  function rebuildSteps() {
    steps = [];
    const isTons = toggleInputMode && toggleInputMode.checked;
    const isExpert = toggleDetailMode && toggleDetailMode.checked;
    
    if (isTons) {
      steps.push({
        id: 'tons',
        lcdLabel: t.enterTons,
        placeholder: "15",
        validate: (v) => {
          const n = parseFloat(v);
          return !isNaN(n) && n > 0 && n <= 1000;
        },
        paperLabel: t.givenTons
      });
    } else {
      steps.push({
        id: 'pe',
        lcdLabel: t.enterPe,
        placeholder: "50000",
        validate: (v) => {
          const n = parseInt(v);
          return !isNaN(n) && n >= 1000 && n <= 5000000;
        },
        paperLabel: t.givenPe
      });
    }

    steps.push({
      id: 'disposal',
      lcdLabel: t.disposalTariff,
      placeholder: "80",
      validate: (v) => {
        const n = parseFloat(v);
        return !isNaN(n) && n >= 0 && n <= 500;
      },
      paperLabel: t.givenDisposal
    });

    if (isExpert) {
      steps.push({
        id: 'ts',
        lcdLabel: t.enterTs,
        placeholder: "20",
        validate: (v) => {
          const n = parseFloat(v);
          return !isNaN(n) && n >= 10 && n <= 40;
        },
        paperLabel: t.givenTs
      });
      steps.push({
        id: 'vs',
        lcdLabel: t.enterVs,
        placeholder: "65",
        validate: (v) => {
          const n = parseFloat(v);
          return !isNaN(n) && n >= 40 && n <= 95;
        },
        paperLabel: t.givenVs
      });
    }
  }

  // Reset simulator state
  function resetSimulator() {
    currentStepIndex = 0;
    currentValue = "";
    isDone = false;
    values = {
      pe: null,
      tons: null,
      disposal: null,
      ts: null,
      vs: null
    };
    
    rebuildSteps();
    
    // Render presets list on paper notebook
    renderPresetsOnPaper();
    
    // Update labels and active states
    updateToggleLabels();
    
    // Set first prompt
    renderCurrentStep();
    
    // Reset LED
    const led = document.querySelector('.led-dot');
    if (led) led.className = "led-dot active";
  }

  function renderPresetsOnPaper() {
    if (!paperBody) return;
    
    const today = new Date().toLocaleDateString(currentLang === 'uk' ? 'uk-UA' : (currentLang === 'pl' ? 'pl-PL' : 'en-US'));
    paperBody.innerHTML = `
      <div class="paper-header-row" style="margin-bottom:0.75rem; display:flex; justify-content:space-between; border-bottom:1px dashed rgba(30, 44, 108, 0.15); padding-bottom:0.25rem;">
        <span style="font-weight:700;">PROTOCOL № BioTC-2026</span>
        <span>Date: ${today}</span>
      </div>
    `;

    const container = document.createElement('div');
    container.className = 'presets-container';
    container.style.marginTop = '0.5rem';
    
    const title = document.createElement('h4');
    title.className = 'presets-title';
    title.innerText = t.presetsHeader;
    title.style.fontFamily = 'var(--font-heading)';
    title.style.fontSize = '1.05rem';
    title.style.fontWeight = 'bold';
    title.style.marginBottom = '0.25rem';
    container.appendChild(title);
    
    const desc = document.createElement('p');
    desc.className = 'presets-desc';
    desc.innerText = t.presetsInitDesc;
    desc.style.fontSize = '0.85rem';
    desc.style.color = '#475569';
    desc.style.marginBottom = '0.75rem';
    desc.style.lineHeight = '1.3';
    container.appendChild(desc);
    
    const list = document.createElement('div');
    list.className = 'presets-list';
    list.style.display = 'flex';
    list.style.flexDirection = 'column';
    list.style.gap = '0.5rem';
    
    const presetKeys = ['municipality_10k', 'municipality_50k', 'agro_10k', 'food_30t', 'digestion_boost'];
    
    presetKeys.forEach(key => {
      const presetData = t.presetsList[key];
      const item = document.createElement('div');
      item.className = 'preset-item';
      
      item.innerHTML = `
        <div class="preset-title">— ${presetData.title}</div>
        <div class="preset-desc">${presetData.desc}</div>
      `;
      
      item.addEventListener('click', () => {
        triggerPreset(key);
      });
      
      list.appendChild(item);
    });
    
    container.appendChild(list);
    paperBody.appendChild(container);
  }

  // Predefined scenarios values mapping
  const presetsData = {
    municipality_10k: {
      mode: "pe",
      tier: "standard",
      values: [10000, 60]
    },
    municipality_50k: {
      mode: "pe",
      tier: "standard",
      values: [50000, 80]
    },
    agro_10k: {
      mode: "volume",
      tier: "expert",
      values: [28, 90, 25, 75]
    },
    food_30t: {
      mode: "volume",
      tier: "standard",
      values: [30, 110]
    },
    digestion_boost: {
      mode: "pe",
      tier: "expert",
      values: [150000, 80, 20, 65]
    }
  };

  function triggerPreset(key) {
    if (isPresetRunning) return;
    const preset = presetsData[key];
    if (!preset) return;
    
    isPresetRunning = true;
    
    const targetInputState = (preset.mode === "volume");
    const targetDetailState = (preset.tier === "expert");
    
    if (toggleInputMode) {
      toggleInputMode.checked = targetInputState;
      toggleInputMode.parentElement.classList.add('toggle-animate');
      setTimeout(() => {
        if (toggleInputMode) toggleInputMode.parentElement.classList.remove('toggle-animate');
      }, 500);
    }
    
    if (toggleDetailMode) {
      toggleDetailMode.checked = targetDetailState;
      toggleDetailMode.parentElement.classList.add('toggle-animate');
      setTimeout(() => {
        if (toggleDetailMode) toggleDetailMode.parentElement.classList.remove('toggle-animate');
      }, 500);
    }
    
    // Reset simulator state to reflect new toggles
    resetSimulator();
    
    // Clear paper again to remove the preset selection cards
    if (paperBody) {
      const today = new Date().toLocaleDateString(currentLang === 'uk' ? 'uk-UA' : (currentLang === 'pl' ? 'pl-PL' : 'en-US'));
      paperBody.innerHTML = `
        <div class="paper-header-row" style="margin-bottom:0.75rem; display:flex; justify-content:space-between; border-bottom:1px dashed rgba(30, 44, 108, 0.15); padding-bottom:0.25rem;">
          <span style="font-weight:700;">PROTOCOL № BioTC-2026</span>
          <span>Date: ${today}</span>
        </div>
        <p class="paper-line" style="font-style:italic; color:#1e2c6c;">Simulation: ${t.presetsList[key].title}</p>
      `;
    }

    isPresetRunning = true;
    typeStep(0);

    function typeStep(stepIdx) {
      if (stepIdx < preset.values.length) {
        const valStr = String(preset.values[stepIdx]);
        let charIdx = 0;
        
        function typeChar() {
          if (charIdx < valStr.length) {
            const char = valStr[charIdx];
            currentValue += char;
            renderCurrentStep();
            
            // Flash key visually
            const btn = Array.from(keys).find(b => b.getAttribute('data-val') === char);
            if (btn) {
              btn.classList.add('active');
              setTimeout(() => btn.classList.remove('active'), 80);
            }
            
            charIdx++;
            setTimeout(typeChar, 120);
          } else {
            // Value typed. Press enter
            if (keyEnter) {
              keyEnter.classList.add('active');
              setTimeout(() => keyEnter.classList.remove('active'), 150);
            }
            
            setTimeout(() => {
              processEnter();
              setTimeout(() => {
                typeStep(stepIdx + 1);
              }, 300);
            }, 150);
          }
        }
        
        typeChar();
      } else {
        // Press final TOTAL key
        if (keyEnter) {
          keyEnter.classList.add('active');
          setTimeout(() => keyEnter.classList.remove('active'), 200);
        }
        setTimeout(() => {
          processEnter(); // runs simulation
          isPresetRunning = false;
        }, 200);
      }
    }
  }

  function updateToggleLabels() {
    const isTons = toggleInputMode && toggleInputMode.checked;
    const isExpert = toggleDetailMode && toggleDetailMode.checked;

    if (lblPe) isTons ? lblPe.classList.remove('active') : lblPe.classList.add('active');
    if (lblTons) isTons ? lblTons.classList.add('active') : lblTons.classList.remove('active');
    
    if (lblStd) isExpert ? lblStd.classList.remove('active') : lblStd.classList.add('active');
    if (lblExp) isExpert ? lblExp.classList.add('active') : lblExp.classList.remove('active');
  }

  // Render current prompt on LCD & Navigation
  function renderCurrentStep() {
    const dotsContainer = document.getElementById('sim-nav-dots');
    
    if (dotsContainer) {
      dotsContainer.innerHTML = "";
      if (currentStepIndex < steps.length && !isDone && !isPresetRunning) {
        dotsContainer.style.display = "flex";
        for (let i = 0; i < steps.length; i++) {
          const dot = document.createElement('button');
          dot.type = "button";
          dot.className = "sim-dot" + (i === currentStepIndex ? " active" : "");
          dot.setAttribute('aria-label', `Go to step ${i + 1}`);
          
          dot.addEventListener('click', () => {
            if (isPresetRunning || isDone) return;
            currentStepIndex = i;
            currentValue = "";
            renderCurrentStep();
          });
          
          dotsContainer.appendChild(dot);
        }
      } else {
        dotsContainer.style.display = "none";
      }
    }

    if (currentStepIndex < steps.length) {
      const step = steps[currentStepIndex];
      
      // Step Title above LCD screen
      if (lcdStep) {
        const cleanLabel = step.lcdLabel.replace(/:$/, '').trim();
        lcdStep.innerText = `${t.stepLabel} 0${currentStepIndex + 1}/0${steps.length}: ${cleanLabel}`;
      }
      
      // LCD Screen shows ONLY the input values
      if (lcdPrompt) {
        if (currentValue !== "") {
          lcdPrompt.innerHTML = `<span>${currentValue}</span><span class="lcd-cursor-blink">_</span>`;
        } else {
          lcdPrompt.innerHTML = `<span class="lcd-cursor-blink">_</span>`;
        }
      }
      
      if (keyEnter) keyEnter.innerText = currentLang === 'uk' ? 'ВВЕСТИ' : (currentLang === 'pl' ? 'ENTER' : 'ENTER');
    } else {
      // Ready to calculate state
      if (lcdStep) lcdStep.innerText = t.readyText;
      if (lcdPrompt) {
        lcdPrompt.innerHTML = `<span class="lcd-blink lcd-text">${currentLang === 'uk' ? 'ГОТОВИЙ ДО ЗВІТУ' : (currentLang === 'pl' ? 'GOTOWY NA TOTAL' : 'READY FOR TOTAL')}</span>`;
      }
      if (keyEnter) keyEnter.innerText = currentLang === 'uk' ? 'РАЗОМ' : (currentLang === 'pl' ? 'SUMA' : 'TOTAL');
    }
  }

  // Handle number or key inputs
  function handleInput(val) {
    if (isPresetRunning) return;
    
    if (val === 'CLEAR') {
      resetSimulator();
      return;
    }
    
    if (isDone) return;
    
    // Clear presets list if it is currently displayed
    const presetsContainer = document.querySelector('.presets-container');
    if (presetsContainer) {
      presetsContainer.remove();
    }
    
    if (val === 'ENTER') {
      processEnter();
    } else {
      // Limit size of typed numbers to prevent LCD overflow
      if (currentValue.length < 10) {
        // Prevent duplicate decimal points
        if (val === '.' && currentValue.includes('.')) return;
        currentValue += val;
        renderCurrentStep();
      }
    }
  }

  function processEnter() {
    if (currentStepIndex < steps.length) {
      const step = steps[currentStepIndex];
      // Use placeholder if nothing was typed
      let valToValidate = currentValue;
      if (valToValidate === "") {
        valToValidate = step.placeholder;
      }
      
      if (step.validate(valToValidate)) {
        const parsedVal = parseFloat(valToValidate);
        values[step.id] = parsedVal;
        
        // Write on paper notebook
        writeLineToPaper(step.paperLabel(parsedVal));
        
        currentStepIndex++;
        currentValue = "";
        renderCurrentStep();
      } else {
        // Error blink effect on LCD
        if (lcdPrompt) {
          lcdPrompt.innerHTML = `<span class="lcd-blink" style="color:#ef4444;">ERROR</span>`;
          setTimeout(() => {
            renderCurrentStep();
          }, 800);
        }
      }
    } else {
      // Trigger total calculation!
      runSimulation();
    }
  }

  function writeLineToPaper(text, className = "paper-line", delay = 0) {
    if (!paperBody) return;
    
    const p = document.createElement('p');
    p.className = className;
    p.innerText = text;
    
    if (className === "paper-divider") {
      p.className = "paper-divider";
      p.innerHTML = "";
    } else if (className === "paper-divider thick") {
      p.className = "paper-divider thick";
      p.innerHTML = "";
    }
    
    if (delay > 0) {
      p.style.animationDelay = `${delay}s`;
    }
    
    paperBody.appendChild(p);
    
    // Auto scroll worksheet
    setTimeout(() => {
      paperBody.scrollTop = paperBody.scrollHeight;
    }, 100);
  }

  function runSimulation() {
    isDone = true;
    
    const led = document.querySelector('.led-dot');
    if (led) led.className = "led-dot"; // turn off online indicator
    
    if (lcdStep) lcdStep.innerText = t.calculating;
    if (lcdPrompt) lcdPrompt.innerHTML = `<span class="lcd-blink lcd-text">PROCESSING...</span>`;
    
    // Core parameters mapping
    const isTons = toggleInputMode && toggleInputMode.checked;
    const tsVal = values.ts !== null ? values.ts : 22; // default 22%
    const vsVal = values.vs !== null ? values.vs : 65; // default 65%
    const tsDecimal = tsVal / 100;
    const vsDecimal = vsVal / 100;
    const disposalCost = values.disposal;
    
    let tonsPerDay = 15;
    let peCount = 50000;
    
    if (isTons) {
      tonsPerDay = values.tons;
      // back calculate PE count
      peCount = (tonsPerDay * tsDecimal * 1000000) / 60;
    } else {
      peCount = values.pe;
      tonsPerDay = (peCount * 60) / (1000000 * tsDecimal);
    }
    
    const wetSludgePerYear = tonsPerDay * 365;
    
    // Constants for HTC
    const Y_mass = 0.65; // Dry yield
    const DS_char = 0.60; // 60% dry solids / 40% moisture target
    
    // Calculations
    const massDryIn = wetSludgePerYear * tsDecimal;
    const charDry = massDryIn * Y_mass;
    const charWet = charDry / DS_char;
    
    // OPEX
    const E_elec = 45; // kWh/ton wet
    const E_heat = 120; // kWh/ton wet
    const cElec = 0.15; // €/kWh
    const cHeat = 0.08; // €/kWh
    const opexTotal = wetSludgePerYear * (E_elec * cElec + E_heat * cHeat);
    
    // Economics
    const baseDisposalCost = wetSludgePerYear * disposalCost;
    const netSavings = baseDisposalCost - opexTotal;
    
    // CAPEX & recommended model
    let recommendedModelName = "BioTC HTC-S 5";
    let capex = 900000;
    
    if (tonsPerDay <= 5.0) {
      recommendedModelName = "BioTC HTC-S 5";
      capex = 900000;
    } else if (tonsPerDay <= 15.0) {
      recommendedModelName = "BioTC HTC-S 15";
      capex = 1900000;
    } else if (tonsPerDay <= 30.0) {
      recommendedModelName = "BioTC HTC-D 30";
      capex = 3200000;
    } else {
      recommendedModelName = "BioTC TH+HTC Custom";
      capex = 5500000;
    }
    
    const paybackYears = Math.max(1.0, capex / netSavings).toFixed(1);
    
    // B2B triggers
    const costOfInaction7Years = baseDisposalCost * 7;
    const trucksSaved = Math.round((wetSludgePerYear - charWet) / 20);
    const treesSaved = Math.round((wetSludgePerYear * tsDecimal * 0.5) * 40);

    // Sequential write on paper notebook
    setTimeout(() => {
      writeLineToPaper("", "paper-divider");
    }, 200);

    // 1. Raw Sludge Mass
    setTimeout(() => {
      writeLineToPaper(t.calcSludge(Math.round(wetSludgePerYear), isTons ? null : Math.round(peCount), tsVal), "paper-line result-line");
    }, 600);

    // 2. Hydrochar Yield
    setTimeout(() => {
      writeLineToPaper(t.calcChar(Math.round(charWet), Math.round(wetSludgePerYear), tsVal), "paper-line result-line");
    }, 1200);

    // 3. Savings Equation
    setTimeout(() => {
      writeLineToPaper(t.calcSavings(Math.round(wetSludgePerYear), Math.round(opexTotal), disposalCost), "paper-line result-line");
    }, 1800);

    // 4. Divider before conclusions
    setTimeout(() => {
      writeLineToPaper("", "paper-divider");
    }, 2400);

    // 5. Payback ROI
    setTimeout(() => {
      writeLineToPaper(t.calcPayback(recommendedModelName, capex, netSavings, paybackYears), "paper-line result-line highlight-conclusion");
    }, 3000);

    // 6. Cost of Inaction (7 years)
    setTimeout(() => {
      writeLineToPaper(t.calcInaction(costOfInaction7Years), "paper-line result-line highlight-coi");
    }, 3600);

    // 7. Eco benefits (Traffic & Trees)
    setTimeout(() => {
      writeLineToPaper(t.calcTrucks(trucksSaved), "paper-line");
      writeLineToPaper(t.calcTrees(treesSaved), "paper-line");
    }, 4200);

    // 8. Show email PDF form
    setTimeout(() => {
      writeLineToPaper("", "paper-divider thick");
      
      const formDiv = document.createElement('div');
      formDiv.className = "paper-lead-form";
      formDiv.innerHTML = `
        <p class="lead-form-title">${t.saveTitle}</p>
        <form id="lead-gen-form-retro" class="retro-form">
          <input type="email" id="retro-email" placeholder="${t.emailPlaceholder}" required class="retro-email-input">
          <button type="submit" class="retro-submit-btn">${t.submitBtn}</button>
        </form>
        <div id="retro-success-msg" class="retro-success hidden">${t.successMsg}</div>
      `;
      
      paperBody.appendChild(formDiv);
      
      // Bind email submit event
      const retroForm = document.getElementById('lead-gen-form-retro');
      if (retroForm) {
        retroForm.addEventListener('submit', (e) => {
          e.preventDefault();
          retroForm.classList.add('hidden');
          const successMsg = document.getElementById('retro-success-msg');
          if (successMsg) successMsg.classList.remove('hidden');
        });
      }
      
      // Finish LCD
      if (led) led.className = "led-dot active";
      if (lcdStep) lcdStep.innerText = t.doneText;
      if (lcdPrompt) lcdPrompt.innerHTML = `<span class="lcd-text">REPORT DONE</span>`;
    }, 4800);
  }

  // Click on physical keys
  keys.forEach(key => {
    key.addEventListener('click', () => {
      const val = key.getAttribute('data-val');
      if (val) {
        handleInput(val);
      }
    });
  });

  if (keyClear) {
    keyClear.addEventListener('click', () => {
      handleInput('CLEAR');
    });
  }

  if (keyEnter) {
    keyEnter.addEventListener('click', () => {
      handleInput('ENTER');
    });
  }

  // Toggles triggers
  if (toggleInputMode) {
    toggleInputMode.addEventListener('change', () => {
      if (isPresetRunning) return;
      resetSimulator();
    });
  }
  if (toggleDetailMode) {
    toggleDetailMode.addEventListener('change', () => {
      if (isPresetRunning) return;
      resetSimulator();
    });
  }

  // Computer physical keyboard hooks
  document.addEventListener('keydown', (e) => {
    if (isPresetRunning) return;
    
    const calcSection = document.getElementById('calculator');
    if (!calcSection) return;
    
    // Check if calculator is visible
    const rect = calcSection.getBoundingClientRect();
    const isVisible = (rect.top < window.innerHeight && rect.bottom > 0);
    if (!isVisible) return;
    
    // Ignore input if user is in an email input field
    if (document.activeElement && document.activeElement.tagName === 'INPUT' && document.activeElement.type === 'email') {
      return;
    }

    let keyVal = null;
    let buttonToAnimate = null;

    if (e.key >= '0' && e.key <= '9') {
      keyVal = e.key;
      buttonToAnimate = Array.from(keys).find(b => b.getAttribute('data-val') === keyVal);
    } else if (e.key === '.') {
      keyVal = '.';
      buttonToAnimate = Array.from(keys).find(b => b.getAttribute('data-val') === '.');
    } else if (e.key === 'Backspace') {
      if (!isDone && currentValue.length > 0) {
        currentValue = currentValue.slice(0, -1);
        renderCurrentStep();
      }
      return;
    } else if (e.key === 'Enter') {
      keyVal = 'ENTER';
      buttonToAnimate = keyEnter;
    } else if (e.key === 'Escape' || e.key.toLowerCase() === 'c') {
      keyVal = 'CLEAR';
      buttonToAnimate = keyClear;
    }

    if (keyVal) {
      e.preventDefault();
      
      if (buttonToAnimate) {
        buttonToAnimate.classList.add('active');
        setTimeout(() => {
          buttonToAnimate.classList.remove('active');
        }, 120);
      }
      
      handleInput(keyVal);
    }
  });

  // Start initial simulator setup
  resetSimulator();
});

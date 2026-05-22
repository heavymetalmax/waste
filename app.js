document.addEventListener('DOMContentLoaded', () => {

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
    if (wetInputVal) {
      wetInputVal.textContent = `${wetInputYear.toLocaleString(t.locale)} ${t.wetInputLabel}`;
    }
    if (hydrocharVal) {
      hydrocharVal.textContent = `${hydrocharYear.toLocaleString(t.locale)} ${t.hydrocharLabel}`;
    }
    if (energyVal) {
      energyVal.textContent = `${energyYear.toLocaleString(t.locale)} ${t.energyLabel}`;
    }
    if (co2Val) {
      co2Val.textContent = `~${co2Year.toLocaleString(t.locale)} ${t.co2Label}`;
    }
    if (preselectedModelInput) {
      preselectedModelInput.value = modelName;
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

});

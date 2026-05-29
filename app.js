document.addEventListener("DOMContentLoaded", () => {

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

  // --- 5. Dynamic Clean-Tech Background Animation ---
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

    const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');

    function getViewportSize() {
      const vv = window.visualViewport;
      if (vv) return { w: vv.width, h: vv.height };
      return { w: window.innerWidth, h: window.innerHeight };
    }

    function resizeCanvas() {
      const viewport = getViewportSize();
      const newWidth = Math.round(viewport.w);

      if (lastKnownWidth > 0 && newWidth === lastKnownWidth) {
        height = Math.round(viewport.h);
        return;
      }

      lastKnownWidth = newWidth;
      dpr = 1; /* cap at 1× — decorative bg, no need for retina resolution */
      width = newWidth;
      height = Math.round(viewport.h);

      const maxBuf = 1500000;
      const bufW = width * dpr;
      const bufH = height * dpr;
      const bufScale = (bufW * bufH > maxBuf) ? Math.sqrt(maxBuf / (bufW * bufH)) : 1;

      canvas.width = Math.round(bufW * bufScale);
      canvas.height = Math.round(bufH * bufScale);
      ctx.setTransform(dpr * bufScale, 0, 0, dpr * bufScale, 0, 0);

      vortices = [
        {
          x: width * 0.30, y: height * 0.40,
          radiusSq: Math.pow(Math.min(width * 0.22, 280), 2),
          radius: Math.min(width * 0.22, 280),
          strength: 1.2
        },
        {
          x: width * 0.65, y: height * 0.48,
          radiusSq: Math.pow(Math.min(width * 0.22, 280), 2),
          radius: Math.min(width * 0.22, 280),
          strength: 1.4
        }
      ];

      initParticles();
    }

    function initParticles() {
      particles = [];
      const particleCount = Math.min(Math.round((width * height) / 35000), 30);
      for (let i = 0; i < particleCount; i++) {
        particles.push(createParticle(Math.random() * width, true));
      }
    }

    function createParticle(startX, randomY = false) {
      const initialMass = 1.0 + Math.random() * 2.0;
      return {
        x: startX,
        y: randomY
          ? height * 0.5 + Math.random() * height * 0.45
          : height * 0.65 + (Math.random() * height * 0.3),
        vx: 0.4 + Math.random() * 0.6,
        vy: 0,
        mass: initialMass,
        alpha: 1.0,
        size: 1.5 + Math.random() * 1.5,
        noiseSeed: Math.random() * 100
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

        p.mass -= 0.0022;
        p.vx *= 0.96;
        p.vy *= 0.96;
        p.vx += 0.04 * (3.0 / p.mass);
        p.vy += 0.015 * p.mass;

        const wavePhase = Math.sin(p.x * 0.004 - time * 1.5);
        if (wavePhase > 0.3) {
          p.vy -= wavePhase * 0.06 * (3.0 / p.mass);
        }

        for (let j = 0; j < vortices.length; j++) {
          const v = vortices[j];
          const dx = p.x - v.x;
          const dy = p.y - v.y;
          const distSq = dx * dx + dy * dy;

          if (distSq < v.radiusSq) {
            const dist = Math.sqrt(distSq);
            const factor = 1 - dist / v.radius;
            const swirlX = -dy / dist;
            const swirlY = dx / dist;

            p.vx += swirlX * factor * v.strength * 1.2 * (1.5 / p.mass);
            p.vy += swirlY * factor * v.strength * 1.2 * (1.5 / p.mass);
            p.vy -= factor * 0.3 * (1.5 / p.mass);
            p.vx -= (dx / dist) * factor * 0.1;
            p.vy -= (dy / dist) * factor * 0.1;
            p.mass -= 0.0015;
          }
        }

        p.x += p.vx;
        p.y += p.vy;

        if (p.mass < 0.6) p.alpha -= 0.009;
        if (p.y < height * 0.15) p.alpha -= 0.015;

        if (p.alpha <= 0 || p.x > width + 20) {
          particles[i] = createParticle(-20);
          continue;
        }

        const speedSq = p.vx * p.vx + p.vy * p.vy;
        const normSpeed = Math.min(1, Math.max(0, (speedSq - 0.16) / 6.0));

        let hue, sat, light;
        if (normSpeed < 0.5) {
          const ratio = normSpeed / 0.5;
          hue = 212;
          sat = 15 + ratio * 60;
          light = 20 + ratio * 18;
        } else {
          const ratio = (normSpeed - 0.5) / 0.5;
          hue = 212 - ratio * 38;
          sat = 75 + ratio * 20;
          light = 38 + ratio * 14;
        }

        const renderAlpha = p.alpha * (0.15 + normSpeed * 0.25);
        const currentSize = p.size * (0.7 + p.mass / 3.0);

        ctx.fillStyle = `hsla(${Math.round(hue)}, ${Math.round(sat)}%, ${Math.round(light)}%, ${renderAlpha})`;
        ctx.beginPath();
        ctx.arc(p.x, p.y, currentSize, 0, Math.PI * 2);
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

    window.addEventListener('scroll', () => {
      if (window.scrollY < height) {
        startLoop();
      } else {
        stopLoop();
      }
    }, { passive: true });

    resizeCanvas();

    function debouncedResize() {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(resizeCanvas, 150);
    }
    window.addEventListener('resize', debouncedResize);
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
        draw();
      } else {
        startLoop();
      }
    });

    if (motionQuery.matches) {
      draw();
    } else {
      startLoop();
    }
  }


  // --- Cycling FAB (phone / mail / chat) ---
  const fab = document.getElementById('nav-fab');
  if (fab) {
    // Navigate to contact section or contact page
    fab.addEventListener('click', () => {
      const contact = document.getElementById('contact');
      if (contact) {
        contact.scrollIntoView({ behavior: 'smooth' });
      } else {
        window.location.href = 'index.html#contact';
      }
    });
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

});
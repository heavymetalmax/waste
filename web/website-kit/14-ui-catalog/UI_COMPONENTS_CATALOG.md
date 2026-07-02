# UI Components Catalog — BTC Consulting Website
**Дата:** 2026-07-01 | **Джерело:** `/Projects/Waste/web/v2/` | **Сервер:** `localhost:8099/v2/`

Каталог якісних готових рішень поточного сайту для повторного використання при розробці нових сторінок.

---

## Як читати каталог

- **Скріншот** — файл у `screenshots/`
- **Класи** — CSS-класи з `design-system.css`
- **Де використовується** — поточні сторінки
- **Реюз** — оцінка придатності для нових сторінок

---

## 1. HERO SECTION — темно-синій з великим заголовком

**Скріншот:** `screenshots/index.png` (верхня третина)

**Де використовується:** index.html, technology.html, teo.html, kalkulator-roi.html

**Варіанти:**
- `section-blue` + великий H1 (`var(--font-display)`) + підзаголовок + CTA — *index.html*
- З анімацією `.paper-checklist` — унікальна для index.html
- Без анімації — стандартний варіант (technology, teo, kalkulator)

**Ключові CSS-класи:**
```css
.section-blue         /* темно-синій фон #0033a0 */
.hero-content         /* обмеження ширини, центрування */
.rubric               /* мала шапка над H1 — mono font, uppercase */
```

**Реюз:** ✅ Висока — використовувати на /dotacje, /hub-spoke, /case-lubin (модернізація)

---

## 2. STATS GRID — 4 числа KPI в ряд

**Скріншот:** `screenshots/technology.png` (блок зі статистикою)

**Де використовується:** technology.html (200°C / 2.0 MPa / -80% / 100%), teo.html (4-6 тижнів / до 90% / 200+ / 11 lat)

**Структура:**
```html
<div class="stats-grid">
  <div class="stat-item">
    <div class="stat-number">200°C</div>
    <div class="stat-label">Temperatura procesu</div>
  </div>
  ...
</div>
```

**Ключові CSS-класи:**
```css
.stats-grid           /* 4-колонкова grid */
.stat-number          /* великий шрифт var(--font-display), var(--color-amber) для акцентів */
.stat-label           /* підпис малим шрифтом */
```

**Реюз:** ✅ Висока — ідеальний для /hub-spoke (36% savings / 50km radius / 6.9 years / 85% grant)

---

## 3. WIZARD — 4-кроковий калькулятор ROI

**Скріншот:** `screenshots/kalkulator-roi.png` (загальний вигляд), `screenshots/wizard-step1.png`

**Де використовується:** kalkulator-roi.html

**Прогрес-бар:**
```html
<div id="wizard-progress-bar" class="wizard-progress-steps">
  <div class="wizard-progress-step active">1. Obiekt</div>
  <div class="wizard-progress-step">2. Wolumen</div>
  <div class="wizard-progress-step">3. Utylizacja</div>
  <div class="wizard-progress-step">4. Parametry</div>
</div>
```

**4 кроки:**

| Крок | ID | Питання | UI-елемент |
|------|----|---------|-----------|
| 1 | `wizard-step1` | JAKI MASZ TYP OBIEKTU? | 4 selection cards (Komunalna / Przemysłowa / Mała oczyszczalnia / Nie wiem) |
| 2 | `wizard-step2` | ILE MASZ OSADU ROCZNIE? | Example card (benchmarkValue) + number stepper |
| 3 | `wizard-step3` | JAK UTYLIZUJESZ OSAD? | 4 cards with PLN/t price tags (~60 / ~35 / ~80 / ~50 PLN/t) |
| 4 | `wizard-step4` | DOSTOSUJ PARAMETRY | 3 sliders (utylizacja / koszty / cena ziemi / dofinansowanie UE) + live preview panel |

**Results section** (`wizard-results`):
- Синій KPI-панель: `OKRES ZWROTU` → велике число "6,9 lat"
- 2 metric cards: `OSZCZĘDNOŚCI ROCZNIE` + `TWÓJ WKŁAD (75% DOTACJA)`
- `SZCZEGÓŁY OBLICZENIA` — розбивка CAPEX/grant/вклад + потоки savings
- CTA: "Zamów bezpłatną konsultację →" (`btn-primary`) + "Zmień parametry" (`btn-outline`)

**Ключові CSS-класи:**
```css
.wizard-progress-steps     /* flex bar, 4px border */
.wizard-progress-step      /* один крок; .active = синій; .done = чорний */
.wizard-screen             /* кожен крок, display:none за замовчуванням */
.wizard-option-card        /* картка вибору типу об'єкту */
.rpt-kpi-val               /* велике число результату */
.rpt-section               /* блок деталей з border-top */
.rpt-row                   /* рядок з label + value */
.rpt-num.rpt-accent        /* акцентне число (синій) */
.rpt-row--sum              /* підсумковий рядок (bold + border-top) */
```

**Реюз:** ✅ Висока — весь wizard повторно використати для нових конфігурацій або спрощеної версії на /hub-spoke

---

## 4. DOC LAYOUT — документний стиль сторінок

**Скріншот:** `screenshots/case-lubin.png`, `screenshots/mission.png`, `screenshots/whitepaper.png`

**Де використовується:** case-lubin.html, mission.html, whitepaper.html

**Характеристики:**
- Вузька колонка тексту (max-width ~720px)
- `.doc-header` з метаданими (тип документу, дата, автор)
- Таблиця `<table>` для metadata grid (рядки "Клієнт / Локація / Тривалість...")
- Emotional blockquote з рамкою та іконкою

**Ключові CSS-класи:**
```css
.doc-header            /* шапка документу */
.doc-meta-table        /* metadata grid */
.doc-blockquote        /* цитата клієнта, border-left 4px */
```

**Реюз:** ✅ Висока — для /case-lubin (оновлення), /case-* нових кейсів, whitepaper-downloads

---

## 5. BLOCKQUOTE — емоційна цитата клієнта

**Скріншот:** `screenshots/case-lubin.png` (середина сторінки)

**HTML:**
```html
<blockquote class="doc-blockquote">
  <p>"[Текст цитати клієнта]"</p>
  <cite>— Ім'я, Посада, Організація</cite>
</blockquote>
```

**Реюз:** ✅ Критична для нових кейсів — конверсійний елемент

---

## 6. SELECTION CARDS — картки вибору (wizard step 1 & 3)

**Скріншот:** `screenshots/wizard-step1.png`

**Структура (step 1):**
```html
<div class="wizard-option-card" data-value="komunalna">
  <strong>Komunalna</strong>
  <span>Oczyszczalnia: 10–300k mieszkańców</span>
</div>
```

**Структура (step 3 — з ціною):**
```html
<div class="wizard-option-card" data-value="pola">
  <strong>Pola osadowe</strong>
  <span>Wysychanie na polach 5–6 mies.</span>
  <div class="wizard-price-tag">~60 PLN/t</div>
</div>
```

**Особливості:**
- 4px border, sharp corners (brutal-industrial)
- На hover — синій border або fill
- При виборі — `active` клас

**Реюз:** ✅ Висока — для будь-яких "вибір типу клієнта" секцій, landing pages для сегментів

---

## 7. CONTACT FORM — канонічна форма

**Скріншот:** нижня частина `screenshots/technology.html`

**Де використовується:** technology.html (canonical), index.html, всі сторінки

**Особливості:**
- Секція з ID `#contact`, клас `.contact-section`
- Байт-ідентична копія на всіх сторінках
- Submit через formsubmit.co + `../app.min.js?v=5`
- Поля: Imię i nazwisko / Email / Telefon / Wiadomość
- Submit: "Wyślij wiadomość" (`btn-primary`)

**ВАЖЛИВО:** Еталон — `technology.html`. При зміні форми — оновлювати ВСІ сторінки.

**Реюз:** ✅ Копіювати байт у байт з technology.html

---

## 8. RUBRIC — мала мітка над заголовком

**Де використовується:** kalkulator-roi.html ("MODEL UNIKNIĘTYCH KOSZTÓW"), technology.html

**HTML:**
```html
<span class="rubric">MODEL UNIKNIĘTYCH KOSZTÓW</span>
<h1>Oblicz zwrot z inwestycji...</h1>
```

**CSS:** `var(--font-mono)`, uppercase, маленький шрифт, `background: var(--color-black)`, `color: var(--color-white)`, padding

**Реюз:** ✅ Висока — використовувати на кожній сторінці над H1 для категоризації

---

## 9. BADGE TAGS — теги/маркери

**Де використовується:** technology.html, index.html

**HTML:**
```html
<span class="badge-tag">UWWTD 2024/3019</span>
<span class="badge-tag badge-tag--blue">Krok 1</span>
```

**Реюз:** ✅ Для маркування кроків, регуляторних дат, статусів

---

## 10. SECTION BACKGROUNDS — фони секцій

**Де використовується:** всі сторінки

| Клас | Колір | Використання |
|------|-------|--------------|
| `.section-blue` | `--color-blue` (#0033a0) | Hero, важливі CTA |
| `.section-black` | `--color-black` (#1a1a1a) | Тёмні секції, footer-adjacent |
| `.section-gray` | `--color-gray-light` | Neutral content |
| `.section-gray-dark` | `--color-gray-mid` | FAQ, secondary sections |

**Реюз:** ✅ Критична — ніколи не додавати нові кольорові секції без цих класів

---

## 11. FAQ ACCORDION

**Де використовується:** kalkulator-roi.html ("JAK LICZYMY → METODYKA")

**HTML:**
```html
<div class="faq-item">
  <button class="faq-question">
    JAK LICZYMY → METODYKA <span class="faq-icon">+</span>
  </button>
  <div class="faq-answer" style="display:none;">
    <!-- відповідь -->
  </div>
</div>
```

**Стиль:** 4px bottom border, bold uppercase питання, "+" іконка справа, JS toggle

**Реюз:** ✅ Критична — потрібна на КОЖНІЙ сторінці (мінімум 4-5 питань)

---

## 12. BUTTONS — дві варіанти

**Де використовується:** всі сторінки

```html
<button class="btn btn-primary">Zamów konsultację →</button>
<button class="btn btn-outline">Zmień parametry</button>
```

**Стиль:**
- `btn-primary`: синій fill (`--color-blue`), білий текст, 4px border
- `btn-outline`: прозорий fill, 4px border, темний текст → синій hover
- Обидва: sharp corners, `var(--font-mono)` або `var(--font-primary)`, uppercase

**Реюз:** ✅ Стандарт — не створювати нових варіантів кнопок

---

## 13. LIVE PREVIEW PANEL (wizard step 4)

**Де використовується:** kalkulator-roi.html (права панель в step 4)

**Особливість:** Оновлюється в реальному часі при зміні параметрів. Показує:
- `PODGLĄD WYNIKÓW` header (темний)
- Велике число "lat zwrotu" (оновлюється динамічно)
- Рядки: Oszczędności/rok / Twój wkład / Za 4 lata

**Клас:** `rpt-kpi-val` + `id="wizard-roi-preview"`

**Реюз:** ✅ Паттерн для будь-якого live-калькулятора

---

## 14. DESIGN SYSTEM TOKENS

**Скріншот:** `screenshots/design-guide.png`

**Кольори:**
| Token | Hex | Використання |
|-------|-----|--------------|
| `--color-blue` | #0033a0 | Hero, CTA, активні елементи |
| `--color-amber` | #E85D2C | Тільки ключові числа (ROI%, savings) |
| `--color-black` | #1a1a1a | Тексти, borders, section-black |
| `--color-white` | #ffffff | Текст на синьому/чорному |
| `--color-gray-light` | #f5f5f5 | Section-gray фон |
| `--color-gray-dark` | #666 | Допоміжний текст |

**Шрифти:**
| Token | Призначення |
|-------|-------------|
| `var(--font-display)` | H1, H2, великі KPI числа |
| `var(--font-primary)` | Body, buttons |
| `var(--font-mono)` | `.rubric`, `.badge-tag`, `<th>`, технічні мітки |

**Тіні:** `var(--shadow-hard-sm/md/lg)` — тверді зміщені тіні (без blur)

---

## 15. COMPONENT REFERENCE PAGES

**Скріншот:** `screenshots/template-components.png`, `screenshots/design-guide.png`

**Де:** `design-guide.html`, `template-components.html`

**Призначення:** Перед розробкою нового компонента — завжди перевіряти ці сторінки щоб уникнути дублювання.

---

## Рекомендації для нових сторінок

### /dotacje (нова сторінка)
Компоненти: Hero (section-blue) + Stats grid (PLN 30B / 75-90% / first-come / 2026-2028) + FAQ accordion + Contact form

### /hub-spoke (нова сторінка)
Компоненти: Hero + Stats grid + Selection cards (Hub vs Spoke) + simplified wizard або таблиця економіки + Contact form

### Нові кейс-студії
Компоненти: Doc layout + Metadata table + Blockquote + Stats grid (результати) + FAQ + Contact form

---

*Каталог складено: 2026-07-01 | Скріншоти: `14-ui-catalog/screenshots/` (9 PNG)*

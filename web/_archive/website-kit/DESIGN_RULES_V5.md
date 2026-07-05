# DESIGN RULES — BTC Consulting v5
## Джерело: аналіз референсу Groundfront (Opus, 2026-07-01)
## НЕ наслідує v2, v3, v4. Будується виключно з цього документу.

---

## 0. МЕТА ФАЙЛУ

Цей файл — єдина точка правди для агента-кодера.
Перед написанням БУДЬ-ЯКОГО CSS або HTML агент читає його повністю.
Якщо щось тут не описано — питати, не вигадувати.

---

## 1. КОЛІРНА ПАЛІТРА (суворо 5 змінних)

```css
:root {
  --bg:        #141414;   /* сторінка, hero, темні секції */
  --bg-dark:   #0F0F0F;   /* footer */
  --surface:   #1E1E1E;   /* картки, панелі, рядки accordion */
  --border:    #2E2E2E;   /* hairline 1px dividers */

  --accent:    #00AAFF;   /* BTC water-tech cyan — ТІЛЬКИ: кнопки, маркери, hover */
  --accent-hv: #0090DD;   /* hover стан */
  --accent-pr: #007ABB;   /* pressed стан */
  --on-accent: #0D0D0D;   /* текст НА кнопці якщо потрібен темний */

  --text-1:    #FFFFFF;   /* заголовки, primary */
  --text-2:    #EDEDED;   /* lead paragraphs */
  --text-3:    #9A9A9A;   /* body, secondary */
  --text-4:    #6B6B6B;   /* captions, meta, footer copy */

  /* Світлі секції (контраст до темного) */
  --cream:     #F2EFE9;   /* light section bg */
  --cream-text:#1A1A1A;   /* text on cream */
}
```

### ПРАВИЛО АКЦЕНТУ (найважливіше)
Рівно ОДИН насичений колір у всій системі — `--accent: #00AAFF`.
Він з'являється ТІЛЬКИ на:
- CTA кнопки (fill)
- маркери списків / нумерація
- hover стани
- ОДНА акцентна секція (pre-footer CTA band)
- дрібні деталі footer

Заборонено використовувати `--accent` як великий фоновий колір крім єдиної CTA-секції.

---

## 2. ТИПОГРАФІКА

### Шрифти (Google Fonts)
```html
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;800;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

```css
--font-display: "Archivo", "Anton", sans-serif;  /* ВСІ заголовки */
--font-body:    "Inter", "Archivo", sans-serif;   /* body, UI */
--font-mono:    "JetBrains Mono", monospace;       /* labels, meta, nav */
```

**Archivo** — вариативний шрифт, використовувати `font-weight: 800–900` для display.
Ключові параметри: `text-transform: uppercase`, `line-height: 0.95–1.0`, `letter-spacing: -0.01em`.

### Таблиця стилів

| Назва | Размір | Weight | Transform | Tracking | LH | Де |
|-------|--------|--------|-----------|----------|----|----|
| `.t-display` | `clamp(3rem, 6vw, 5.5rem)` | 900 | UPPER | -0.01em | 0.95 | Hero H1 |
| `.t-heading` | `clamp(2.25rem, 4vw, 3.5rem)` | 800 | UPPER | -0.01em | 0.98 | Section H2 |
| `.t-subhead` | `clamp(1.5rem, 2.5vw, 2rem)` | 800 | UPPER | 0 | 1.0 | H3, підзаголовки |
| `.t-eyebrow` | `0.75rem` | 600 | UPPER | +0.14em | 1.2 | Мітки над H2 |
| `.t-lead` | `1.125rem` | 400 | none | 0 | 1.55 | Intro copy |
| `.t-body` | `1rem` | 400 | none | 0 | 1.65 | Параграфи |
| `.t-small` | `0.8125rem` | 400 | none | +0.04em | 1.4 | Captions, meta |
| `.t-btn` | `0.875rem` | 600 | UPPER | +0.06em | 1 | Кнопки |

**Ключовий контраст:** величезний білий uppercase заголовок + маленький сірий sentence-case body поруч. Не "балансувати" — різкий контраст розмірів і є підписом стилю.

---

## 3. LAYOUT

```css
--container-max: 1440px;
--gutter:        clamp(20px, 5vw, 96px);  /* padding-inline сторінки */
--section-y:     clamp(80px, 10vw, 160px); /* padding-block секцій */
--gap:           1.5rem;                   /* grid gap */
```

Базовий контейнер:
```css
.container {
  width: 100%;
  max-width: var(--container-max);
  margin-inline: auto;
  padding-inline: var(--gutter);
}
```

**Сплити НЕСИМЕТРИЧНІ** — не 50/50:
- Hero: `42% | 58%` (текст | фото)
- Content секції: `5/7` або `7/5` (12-column grid)
- Чергувати: текст-ліво / текст-право посекційно

---

## 4. ГЕОМЕТРІЯ ТА ЕФЕКТИ

### 4.1 Diagonal section dividers (ОБОВ'ЯЗКОВО)
Це ключова деталь стилю. Кожна межа між темною і світлою секцією — скошена, не горизонтальна.

```css
/* На темній секції — скошений низ в сторону кремової секції нижче */
.angle-bottom {
  clip-path: polygon(0 0, 100% 0, 100% calc(100% - var(--divider-h)), 0 100%);
  padding-bottom: calc(var(--section-y) + var(--divider-h));
}

/* На секції після скошеної — скошений верх */
.angle-top {
  clip-path: polygon(0 var(--divider-h), 100% 0, 100% 100%, 0 100%);
  padding-top: calc(var(--section-y) + var(--divider-h));
}

:root { --divider-h: 60px; } /* висота кута */
```

**Правило чергування:** секція A `angle-bottom` → наступна секція B `angle-top`. Напрямок кута чергується (A: вниз-ліво→вгору-право; B: навпаки) щоб отримати зигзаг.

На мобільному (`<768px`): `--divider-h: 0` — плоскі межі.

### 4.2 Notched corners (chamfer)
Картки, accordion-рядки, деякі кнопки — зрізаний кут 20px (низ-право):

```css
.notch {
  clip-path: polygon(
    0 0, 100% 0,
    100% calc(100% - var(--notch)),
    calc(100% - var(--notch)) 100%,
    0 100%
  );
}
:root { --notch: 20px; }
```

### 4.3 Protruding button (кнопка що "виступає" між секціями)
Позиціонується на межі двох секцій — половина в одній, половина в іншій.

```html
<!-- В кінці секції A -->
<section class="section-photo" style="position:relative; overflow:visible">
  <!-- ... фото ... -->
  <div class="container">
    <a class="btn btn-solid btn-protrude" href="#contact">
      Замов безкоштовну оцінку →
    </a>
  </div>
</section>
<!-- Секція B йде одразу після — кнопка перекриває її зверху -->
<section class="section-b">...</section>
```

```css
.btn-protrude {
  position: absolute;
  bottom: -28px;        /* половина висоти кнопки */
  left: var(--gutter);  /* вирівнюється по лівому гутеру */
  z-index: 10;
  box-shadow: 0 12px 32px rgba(0,0,0,0.4);
}
/* БАТЬКІВСЬКА секція: overflow: visible (не hidden!) */
```

### 4.4 Photo treatment
ВСІ фото в grayscale + темний overlay:
```css
.photo-wrap { position: relative; overflow: hidden; }
.photo-wrap img {
  width: 100%; height: 100%;
  object-fit: cover;
  filter: grayscale(1) contrast(1.05);
  display: block;
}
.photo-wrap::after {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(20,20,20,0.35);
  pointer-events: none;
}
```

### 4.5 Placeholder (поки фото не додано)
```html
<div class="photo-wrap photo-ph" data-slot="назва-зображення">
  <!-- Замінити на <img> коли фото буде готове -->
</div>
```
```css
.photo-ph {
  background: #1A1A1A;
  min-height: 400px;
}
.photo-ph::before {
  content: "[ " attr(data-slot) " ]";
  position: absolute;
  inset: 0;
  display: flex; align-items: center; justify-content: center;
  font-family: monospace; font-size: 0.7rem;
  letter-spacing: 0.1em; color: rgba(255,255,255,0.2);
  text-transform: uppercase;
  background: repeating-linear-gradient(
    -45deg, rgba(255,255,255,0.03) 0, rgba(255,255,255,0.03) 1px,
    transparent 1px, transparent 32px
  );
}
```

### 4.6 Blueprint / HTC process circle overlay (на фото)
Тонкий SVG з концентричними колами і спицями — поверх фото:
```html
<div class="photo-wrap">
  <img ...>
  <svg class="blueprint-ring" viewBox="0 0 240 240" ...>
    <!-- concentric circles + crosshair + tick marks -->
  </svg>
</div>
```
Stroke 1px, колір `rgba(255,255,255,0.35)`, no fill. Позиціонується в правий нижній квадрант фото.

---

## 5. КНОПКИ

### 5.1 Primary (solid accent)
```css
.btn {
  display: inline-flex; align-items: center; gap: 0.5rem;
  font-family: var(--font-mono);
  font-size: 0.875rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.06em;
  padding: 0.9em 2em;
  border: 1.5px solid transparent;
  cursor: pointer; text-decoration: none;
  transition: background 0.25s, color 0.25s, border-color 0.25s;
  min-height: 52px;
  white-space: nowrap;
  border-radius: 0;  /* ЗАВЖДИ гострі кути */
}

.btn-solid {
  background: var(--accent);
  color: var(--on-accent);
  border-color: var(--accent);
}
.btn-solid:hover { background: var(--accent-hv); border-color: var(--accent-hv); }

/* з notched corner */
.btn-solid.notch { /* clip-path notch */ }
```

### 5.2 Ghost (outline)
```css
.btn-ghost {
  background: transparent;
  color: var(--text-1);
  border-color: var(--border);
}
.btn-ghost:hover { border-color: var(--accent); color: var(--accent); }
```

### 5.3 Ghost on light bg
```css
.btn-ghost-dark {
  background: transparent;
  color: var(--cream-text);
  border-color: rgba(0,0,0,0.25);
}
.btn-ghost-dark:hover { border-color: var(--accent); color: var(--accent); }
```

---

## 6. СЕКЦІЇ — ТИПИ (повний список)

### (A) Header / Nav
Позиція: fixed top. bg: прозорий над hero → `var(--bg)` при скролі.
- Лого BTC. (зліва)
- Nav links по центру/право: mono 13px, uppercase, `--text-3` → white/accent hover
- CTA кнопка `btn-solid` справа
- Hamburger на `<768px`

### (B) Split Hero
- Ліво (42%): dark bg `--bg`, текст знизу-ліво, `.t-display` H1, lead, CTA
- Право (58%): grayscale фото (або placeholder), overlay `rgba(20,20,20,0.35)`
- Між ними: `1px solid var(--border)` роздільник
- Знизу: `angle-bottom` на всій секції

### (C) Stat strip
- Full-width, bg `--bg`, 4 комірки з `1px solid var(--border)` між ними
- Число: `.t-display` (менший розмір), accent-colored якщо ключове
- Підпис: `.t-eyebrow`, `--text-4`

### (D) Content + Accordion (intro section)
- bg `--surface` або `--bg`
- Ліво: `.t-heading`, lead
- Право: accordion-рядки на `--surface`, hairline border, + icon справа
- Нижче: CTA-кнопка з protruding ефектом

### (E) Photo strip full-bleed
- `min-height: 35vw`, grayscale фото, overlay
- Protruding button абсолютно на bottom seam

### (F) Split content (Commercial / Industrial)
- Текст + feature list з accent-маркерами
- Фото `photo-wrap` з optional blueprint SVG
- Чергування: текст-ліво / текст-право

### (G) Statement section (повна ширина, тільки текст)
- bg `--bg`, padding мінімальний
- `.t-display` великий, max-width 18ch
- Accent фраза виділена `color: var(--accent)`

### (H) Case study strip
- Горизонтальний скрол (overflow-x: auto, hide scrollbar)
- 3+ карток `aspect-ratio: 4/3`, кожна photo-wrap + caption
- Кожна карта: `.notch` клас, hover: opacity lift

### (I) Pre-footer CTA band ← ЄДИНА ПОВНІСТЮ АКЦЕНТНА СЕКЦІЯ
- bg `var(--accent)`, color dark
- Великий `.t-heading` dark text
- `angle-top` зверху і `angle-bottom` знизу

### (J) Footer
- bg `--bg-dark`
- Гігантський знак BTC (150–300px, barely-there `#1E1E1E` або outline) — кровотечить з лівого краю
- Колонки: Розв'язки / Фінансування / Ресурси / Контакт
- Заголовки колонок: `.t-eyebrow`, `--text-4` або tiny accent
- Посилання: `--text-3` → white hover
- Нижній рядок: copyright `--text-4` 13px, hairline зверху

---

## 7. ACCORDION STYLE

```css
.acc { border-top: 1px solid var(--border); }
.acc-item { border-bottom: 1px solid var(--border); }
.acc-btn {
  width: 100%; display: flex; justify-content: space-between; align-items: center;
  padding: 1.25rem 0; background: none; border: none; cursor: pointer;
  color: var(--text-1); font: 600 1rem var(--font-body);
  text-align: left; min-height: 56px;
}
.acc-icon { font-size: 1.25rem; font-weight: 300; transition: transform 0.3s; }
.acc-item.open .acc-icon { transform: rotate(45deg); color: var(--accent); }
.acc-body { padding-bottom: 1.25rem; color: var(--text-3); font-size: 0.9375rem; line-height: 1.7; }
.acc-body[hidden] { display: none; }
```

---

## 8. ЗАБОРОНЕНО (жорсткі правила)

❌ `border-radius` > 0 — НІКОЛИ (крім кола в blueprint SVG)
❌ Кольорові фото — ЗАВЖДИ grayscale
❌ Більше одного акцентного кольору
❌ `--accent` як великий фоновий колір (крім pre-footer CTA band)
❌ `box-shadow` м'які (`blur > 0`) — тільки `--shadow-float` на protruding кнопці
❌ `transform: skew` — для кутів використовувати тільки `clip-path`
❌ Горизонтальні межі між секціями — тільки скошені (або `1px solid var(--border)`)
❌ Симетричні сплити 50/50 — тільки 42/58 або 5/7 або 7/5
❌ Шрифти з v2/v3/v4 (Inter як body — ок, Big Shoulders Display — НЕ використовувати як display)
❌ `overflow: hidden` на батьківській секції protruding кнопки
❌ `.section-blue`, `.section-gray`, `.section-cream` — ці класи не існують в v5

---

## 9. СТРУКТУРА ФАЙЛІВ v5

```
web/v5/
  design-system.css      ← побудувати з цього документу
  index.html
  technologia.html
  hub-spoke.html
  teo.html
  dotacje.html
  kalkulator-roi.html
  case-lubin.html
  whitepaper.html
  misja.html
  partials/
    header.js
    footer.js
  translations/pl.js
  i18n.js
  reveal.js
  assets/svg/
    htc-process-ring.svg   ← blueprint circle SVG
    hub-spoke-map.svg
```

---

## 10. ОБРАЗ PLACEHOLDER ДО ФІНАЛЬНОГО ФОТО

| slot | сторінка | type | розмір |
|------|---------|------|--------|
| `wwtp-aerial` | index / hero | hero photo | 1920×1080 |
| `htc-reactor` | technologia | split photo | 900×700 |
| `lubin-wwtp` | case-lubin | hero photo | 1920×1080 |
| `eu-funds` | dotacje | hero photo | 1920×1080 |
| `consultants` | teo | split photo | 900×700 |
| `btc-team` | misja | group photo | 1400×700 |

---

## 11. ФАКТИ (верифіковані — тільки ці числа на сайті)

- 3 873 польських WWTP мають модернізуватися (UWWTD 2024/3019)
- Дедлайн: 2035; транспозиція в польське право: липень 2027
- Гранти: 75–90% CapEx (FEnIKS, KPO, NFOŚiGW, LIFE)
- Поточна ціна утилізації: PLN 550/t
- Ціна після HTC: PLN 200–225/t (~60% економія)
- Повернення інвестицій: 6,9 роки (85% гранту)
- Hub&Spoke spoke-економія: 36–41% при відстані до 50 км
- Процес HTC: 200°C / 2,0 МПа / 8–12 год / –75% об'єму
- Перша комерційна установка: MPWiK Lubin (2025)
- AGH Краків — партнер з досліджень (10+ років)
- Дозволено в польському праві з 14.01.2025
- Типовий проект: EUR 5M CAPEX → gmina EUR 750K (15%), EU EUR 4.25M (85%)

Джерела: `/Users/max/Projects/Waste/web/website-kit/` (папки 01–08)

---

*Документ створено: 2026-07-01 | Джерело: Opus-аналіз референсу Groundfront*
*Версія: v5. НЕ змінювати без нового аналізу референсу.*

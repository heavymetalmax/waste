# PL_V2 Design System

Канонічна дизайн-бібліотека для всіх сторінок pl_v2 (`design-system.css`).

**v2 від 2026-06-30 повністю самодостатній** — не залежить від `../Ua/industrial-modern.css` (україномовний сайт). Зміни в `Ua/` не впливають на v2 і навпаки.

## Мова дизайну

Брутал-індастріал: гострі кути (0 border-radius, крім поодиноких кружечків-маркерів), 4px чорні бордери, hard-offset тіні (`--shadow-hard-sm/lg`, патерн `12px 12px 0 black`). Без розмитих тіней, без скляних/напівпрозорих карток.

## 🎨 Кольори

| Колір | Hex | Призначення |
|---|---|---|
| `--color-white` | `#ffffff` | Фон |
| `--color-black` | `#0a0a0a` | Текст, бордери |
| `--color-blue` | `#0033a0` | Бренд, CTA, заголовки, основні цифри |
| `--color-gray-light` | `#f3f4f6` | Фон секцій/карток |
| `--color-gray-dark` | `#374151` | Другорядний текст |
| `--color-amber` | `#E85D2C` | **Сигнальний акцент — лише для ключових цифр-результатів** (економія, ROI%, % гранту, калорійність, % деструкції). Через клас `.stat-accent` або `.rpt-num.rpt-accent`. Не використовувати декоративно, не для CTA. |

> Раніше тут був `--color-teal` (#0D9488), доданий хаотично у 4 з 11 файлів без правила вживання. Прибраний і замінений на `--color-amber` із чітким правилом застосування (див. вище).

## 🔤 Типографія — 3 ролі

| Роль | Шрифт | Токен | Де |
|---|---|---|---|
| Display | Big Shoulders Display | `--font-display` | H1, H2, `.number`, `.index-val`, `.rpt-kpi-val`, великі цифри-результати |
| Body | Inter | `--font-primary` | Основний текст, кнопки |
| Mono | JetBrains Mono | `--font-mono` | `.rubric`, `.badge-tag`, таблиці `<th>`, технічні лейбли/формули — "технічний зчитувач" |

Раніше скрізь був лише Inter (різнилась тільки вага/регістр). Display + mono додають типографічний характер без захаращення.

## 📏 Spacing (8px база)

```css
--space-xs: 0.5rem   /* 8px */
--space-sm: 1rem     /* 16px */
--space-md: 2.5rem   /* 40px */
--space-lg: 5rem     /* 80px */
--space-xl: 7rem     /* 112px */
```

## 🎯 Секційне фарбування

Портативні класи (рекомендовано для нових/мігрованих сторінок):

```html
<section class="section-blue">…</section>
<section class="section-black">…</section>
<section class="section-gray">…</section>
<section class="section-gray-dark">…</section>
```

`index.html` досі використовує прямі ID-правила (`#problem`, `#process`, `#calculator`, `#trust`, `#team`, `#grants`, `#contact`) — це legacy-хуки лишені у `design-system.css` заради зворотної сумісності. **Для нових сторінок використовуй класи-модифікатори вище, не вигадуй нові ID-правила.**

## ♿ Accessibility floor

- `:focus-visible` — глобальна 3px синя (біла на синьому/чорному фоні) обводка на всіх інтерактивних елементах.
- `@media (prefers-reduced-motion: reduce)` — глушить усі `@keyframes`/transition сайту.

Раніше обох не було, попри кілька анімованих сигнатурних компонентів (blueprint draw, paper-checklist slide-up, scanner sweep).

## 📦 Базові компоненти

```html
<a class="btn btn-primary">Primary</a>
<a class="btn btn-outline">Outline</a>

<span class="rubric">Sekcja</span>
<span class="badge-tag">Tag</span>

<div class="col-card">
  <span class="number">94%</span>
  <h3>Заголовок</h3>
  <p>Опис</p>
</div>

<div class="grid-2">…</div>  <!-- 2 кол, 768px → 1 -->
<div class="grid-3">…</div>  <!-- 3 кол, 1024px → 2, 768px → 1 -->
<div class="grid-4">…</div>  <!-- те саме, що grid-3 -->
```

Повний візуальний приклад: [`design-guide.html`](./design-guide.html).

## 🧩 Сигнатурні компоненти (бренд, не копіювати без потреби)

- `.paper-checklist` — анімований "аркуш-кліпборд" у hero `index.html`. Один сигнатурний елемент на сторінку.
- `.hero-blueprint` / `.bp-line` — креслярська анімація фону.
- `.process-bg-anim` / `.scanner-line` — інженерна сітка + сканер у секції процесу.

## 📄 Сторінки і їхні розширення

Усі сторінки підключають один файл:

```html
<link rel="stylesheet" href="./design-system.css">
```

| Сторінка | Власні (page-local) класи в `<style>` |
|---|---|
| `index.html` | hero/checklist розмітка, ID-секції (legacy) |
| `technology.html` | `.tech-stat-*`, `.hydrochar-spec-list`, `.spec-val--*`, `.flow-*`, `.model-*` |
| `kalkulator-roi.html` | wizard (`.wizard-*`), звіт (`.rpt-*`), HTC-симулятор (`.htc-*`), чат (`.srp-chat-*`), `.privacy-strip` |
| `mission.html`, `whitepaper.html`, `case-lubin.html` | `.doc-*` (друкований документ) |
| `case-lubin.html` | додатково `.kpi-*`, `.tl-*` (timeline), `.hub-box` |
| `chat.html` | повноекранний чат (`.chat-fs-*`) |

Page-local класи — нормальна практика для UI, специфічного для однієї сторінки (wizard, чат, друкований документ). **Не виносити їх у глобальний `design-system.css`, якщо вони не повторюються на іншій сторінці.**

## ✅ Правила

1. **Спочатку перевір, чи компонент уже є** в `design-system.css` або на іншій сторінці — не вигадуй новий клас, якщо `.col-card`/`.btn-*`/`.rubric`/`.badge-tag` вже вирішують задачу.
2. **Кольори/spacing — тільки через `var(--*)`**, ніяких хардкод-хексів у новому коді.
3. **Бурштин (`--color-amber`) — тільки для цифр-результатів.** Якщо потрібен ще один акцент — спочатку обговорити правило вживання, а не додавати "про всяк випадок" (так з'явився і застряг `--color-teal`).
4. **4px бордер — основний**, 2px — для дрібніших елементів (таби, чат-бабли). Без `border-radius`, крім кружечків-маркерів (timeline dot, avatar).
5. **H1/H2/великі цифри — `var(--font-display)`. Лейбли/дані — `var(--font-mono)`. Усе інше — `var(--font-primary)`.**
6. Перед мердж — перевір на 1440 / 1024 / 768px, Tab-навігацію (фокус видно) і `prefers-reduced-motion`.

## 🔗 Файли

- **CSS:** `v2/design-system.css` — єдиний канонічний файл
- **Візуальний приклад:** `v2/design-guide.html`
- **Форма звʼязку:** усі сторінки шарять один бекенд-обробник — `web/app.min.js` (formsubmit.co), підключений через `<script src="../app.min.js?v=5">`

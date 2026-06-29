# PL_V2 Unified Design System

Єдина дизайн-бібліотека для всіх сторінок pl_v2 (`design-system.css`).

## 📦 Що включено

### 1. **Дизайн-токени** (Colors, Typography, Spacing)
- **Colors**: Основні кольори (blue #0033a0, teal #0D9488, gray, white, black)
- **Typography**: Inter font family з 4 вагами (500, 600, 700, 800, 900)
- **Spacing**: 8px base scale (xs: 0.5rem → xl: 7rem)
- **Borders & Shadows**: Consistent radius і shadow values
- **Transitions**: Fast, base, slow transitions

### 2. **Base Компоненти**
- ✅ Headings (h1–h6) з responsive font sizes
- ✅ Paragraphs, lists, inline text elements
- ✅ Links із hover states
- ✅ Buttons (primary, secondary, disabled states)

### 3. **Layout Утиліти**
- ✅ `.container` (max-width: 1300px)
- ✅ `.grid-2` (responsive grid)
- ✅ `.flex`, `.flex-col`, `.flex-center` і т.д.
- ✅ Spacing utilities (mt, mb, p, gap...)

### 4. **Semantic Components** (Tech page, Hydrochar, Models)
- ✅ `.tech-stat-*` — статистика для сторінки технології
- ✅ `.hydrochar-spec-list` — специфікація гідровугілля
- ✅ `.model-card-*` — карти моделей обладнання
- ✅ `.process-step-spec` — кроки процесу
- ✅ `.scenario-benefits` — список переваг

### 5. **Forms & Cards**
- ✅ Input, textarea, select styling
- ✅ `.card`, `.glass-card` — карточки
- ✅ `.paper-checklist` — контакт-карта
- ✅ `.contact-row` — рядки контактів

### 6. **Hero & Special Sections**
- ✅ `#hero` — full-viewport hero з анімованим background
- ✅ `#hero .hero-bars-bg` — анімовані stripes (page-specific)
- ✅ `.woit-bridge-*` — bridge section (page-specific)

## 🎨 CSS Variables (Custom Properties)

Всі значення зберігаються як CSS variables в `:root`:

```css
/* Colors */
--color-blue: #0033a0;
--color-gray-light: #f3f4f6;
--color-gray-dark: #374151;
--color-teal: #0D9488;

/* Typography */
--font-primary: 'Inter', sans-serif;
--text-xs through --text-4xl

/* Spacing */
--space-xs: 0.5rem;
--space-sm: 1rem;
--space-md: 2.5rem;
--space-lg: 5rem;
--space-xl: 7rem;

/* Others */
--radius-sm, --radius-md, --radius-lg
--shadow-sm, --shadow-md, --shadow-lg
--transition-fast, --transition-base
```

## 📝 Як використовувати

### 1. Імпорт у HTML

```html
<head>
  <link rel="stylesheet" href="./design-system.css">
</head>
```

### 2. Базові класи

```html
<!-- Headings -->
<h1>Заголовок</h1>
<h2>Підзаголовок</h2>

<!-- Buttons -->
<a href="#" class="btn btn-primary">Primary Button</a>
<button class="btn btn-secondary">Secondary Button</button>

<!-- Cards -->
<div class="card">
  <h3>Card Title</h3>
  <p>Card content...</p>
</div>

<div class="glass-card">Translucent card</div>

<!-- Grid Layout -->
<div class="grid-2">
  <div>Column 1</div>
  <div>Column 2</div>
</div>

<!-- Flex Utilities -->
<div class="flex flex-between gap-md">
  <span>Left</span>
  <span>Right</span>
</div>
```

### 3. Page-specific styles

Якщо потрібна унікальна стилізація конкретної сторінки, додайте `<style>` tag з page-specific CSS:

```html
<style>
  /* Unique styles for this page only */
  .page-special-component {
    color: var(--color-blue);
  }
</style>
```

**Приклади page-specific стилів:**
- `index.html`: Анімовані stripe-background для hero
- `mission.html`, `whitepaper.html`: Документ-style компоненти (`.doc-wrap`, `.doc-card`)
- `chat.html`: Chat interface styling
- `kalkulator-roi.html`: Calculator-specific overrides

## 🎯 Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| **Blue (Primary)** | #0033a0 | Headings, buttons, accents |
| **Gray Light** | #f3f4f6 | Backgrounds, borders |
| **Gray Dark** | #374151 | Secondary text, labels |
| **Teal** | #0D9488 | Secondary accent |
| **White** | #ffffff | Main background |
| **Black** | #0a0a0a | Primary text |

## 📐 Spacing Scale (8px base)

- `--space-xs`: 0.5rem (8px)
- `--space-sm`: 1rem (16px)
- `--space-md`: 2.5rem (40px)
- `--space-lg`: 5rem (80px)
- `--space-xl`: 7rem (112px)

## 🔤 Typography

- **Font**: Inter (weights: 500, 600, 700, 800, 900)
- **h1**: clamp(1.8rem, 4vw, 4.2rem) — Hero headings
- **h2**: clamp(2rem, 3.5vw, 3rem) — Section headings (uppercase)
- **h3**: 1.5rem (700 weight)
- **Body**: 1rem / 1.5 line-height
- **Small text**: 0.875rem

## 🎬 Responsive Breakpoints

- Mobile: < 768px
- Tablet: 768px – 1024px
- Desktop: > 1024px

Key responsive patterns:
- `.grid-2` → collapses to 1 column on mobile
- `#hero` → adjusts height and padding
- Font sizes use `clamp()` for smooth scaling

## 📋 Component Reference

### Headings

```html
<h1>Hero Heading</h1>              <!-- 1.8–4.2rem, 900 weight -->
<h2>Section Heading</h2>           <!-- 2–3rem, 800 weight, uppercase -->
<h3>Subsection</h3>               <!-- 1.5rem, 800 weight -->
```

### Buttons

```html
<!-- Primary (filled) -->
<a href="#" class="btn btn-primary">Primary</a>

<!-- Secondary (outline) -->
<button class="btn btn-secondary">Secondary</button>

<!-- Disabled -->
<button class="btn btn-primary" disabled>Disabled</button>
```

### Cards

```html
<!-- Regular card (with shadow) -->
<div class="card">...</div>

<!-- Glass card (with blur effect) -->
<div class="glass-card">...</div>
```

### Forms

```html
<div class="form-group">
  <label for="name">Name</label>
  <input type="text" id="name" placeholder=" " required>
  <label class="floating-label" for="name">Name</label>
</div>
```

### Layout Utilities

```html
<!-- Flex helpers -->
<div class="flex items-center justify-between gap-md">
  <span>Left</span>
  <span>Right</span>
</div>

<!-- Spacing -->
<div class="mt-lg mb-md p-lg">Content with spacing</div>

<!-- Text utilities -->
<p class="text-muted">Muted text</p>
<span class="font-bold text-lg">Bold large text</span>
```

## ✅ Всі сторінки, які використовують design-system.css

1. ✅ `index.html` — Головна
2. ✅ `technology.html` — Технологія HTC
3. ✅ `mission.html` — Місія
4. ✅ `case-lubin.html` — Кейс Любин
5. ✅ `whitepaper.html` — Whitepaper
6. ✅ `chat.html` — AI асистент
7. ✅ `kalkulator-roi.html` — Калькулятор ROI
8. ✅ `teo.html` — Аналіз TEO

## 🔄 Оновлення design-system.css

Якщо потрібно додати новий компонент або змінити токен:

1. Додайте токен у секцію `/* Design Tokens */`
2. Додайте CSS правила у відповідну секцію (базові, layout, форми, компоненти)
3. Всі сторінки автоматично отримають оновлення

## 🚀 Best Practices

✅ **DO:**
- Використовувати CSS variables для кольорів та spacing
- Додавати page-specific CSS у `<style>` тегу
- Виходити з responsive-first підходу
- Тримати компоненти простими та переиспользуваними

❌ **DON'T:**
- Не використовувати inline styles (style="...") якщо можна класи
- Не дублювати CSS — переиспользовуйте компоненти
- Не забувати про mobile responsiveness
- Не видаляти базові компоненти без перевірки їх вживання

## 📞 Support

Питання щодо design-system? Перевірте:
1. CSS variables у `:root`
2. Компоненти у коментарях design-system.css
3. Page-specific стилі у кожному HTML файлі

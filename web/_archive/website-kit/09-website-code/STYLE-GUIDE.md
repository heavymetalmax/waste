# Посібник стилю BTC Consulting

## Принцип: 0 видуманого

Всі компоненти і стилі **витягнені прямо з домашної сторінки** (index.html). Нові сторінки будуються переиспользуванням наявних елементів, без придумування нових класів або компонентів.

---

## 📐 Кольорова система

### Основні кольори
- **Білий** (`var(--color-white)` / `#ffffff`) — фон основних розділів
- **Чорний** (`var(--color-black)` / `#0a0a0a`) — текст, бордери (4px), фон секцій
- **Синій** (`var(--color-blue)` / `#0033a0`) — акцентний колір, кнопки, заголовки
- **Темно сіра** (`var(--color-gray-dark)` / `#374151`) — текст на світлому фоні, footer фон
- **Світло сіра** (`var(--color-gray-light)` / `#f3f4f6`) — фон розділів, карток

### Доповнювальні кольори (з hero анімацій)
- **Світло синя** (`#86c2e8`) — для градієнтів, деталей
- **Середньо синя** (`#3a9fe0`) — переходи
- **Блідо синя** (`#bcd9ee`) — м'які переходи

---

## 🔤 Типографія

### Шрифт
- **Сім'я:** Inter (Google Fonts)
- **Ваги:** 400, 500, 600, 700, 800, 900

### Розміри

| Елемент | Розмір | Вага | Трансформація |
|---------|--------|------|---------------|
| **H1** | clamp(2.5rem, 5vw, 4.5rem) | 900 | UPPERCASE |
| **H2** | clamp(2.5rem, 5vw, 4rem) | 800 | UPPERCASE |
| **H3** | 1.5rem | 800 | - |
| **P** | 1rem (базовий) | 500 | - |
| **Опис (hero)** | 1.1–1.25rem | 500 | - |
| **Label** | 0.85rem | 800 | UPPERCASE |
| **Rubric** | 0.85rem | 800 | UPPERCASE |

### Letter-spacing (Інтервал букв)
- **H1:** -0.04em (більше "стиснено")
- **H2:** -0.03em
- **H3:** -0.02em
- **Кнопки:** 0.05em (розширено)
- **Rubric:** 0.1em (максимальна розтяжка)

---

## 📏 Spacing (Відступи)

```css
--space-xs: 0.5rem  (8px)
--space-sm: 1rem    (16px)
--space-md: 2.5rem  (40px)
--space-lg: 5rem    (80px)
--space-xl: 7rem    (112px)
```

### Правила використання
- **Між секціями:** `padding: var(--space-xl) 0` або `var(--space-lg) 0`
- **Усередині карток:** `padding: var(--space-md)` (40px)
- **Між елементами в сітці:** `gap: var(--space-lg)` (grid-2) або `var(--space-md)` (grid-3/4)

---

## 🎨 Компоненти

### 1. Кнопки

#### btn-primary
```html
<a href="#" class="btn btn-primary">Заховай безпекою</a>
```
- **Фон:** var(--color-blue)
- **Текст:** var(--color-white)
- **Бордер:** 4px solid var(--color-blue)
- **На hover:** Фон → var(--color-black)

#### btn-outline
```html
<a href="#" class="btn btn-outline">Дізнайся більше</a>
```
- **Фон:** transparent
- **Текст:** var(--color-black)
- **Бордер:** 4px solid var(--color-black)
- **На hover:** Фон → var(--color-black), текст → var(--color-white)

### 2. Rubric (Тег розділу)

```html
<span class="rubric">Проблема</span>
```
- **Фон:** var(--color-black)
- **Текст:** var(--color-white)
- **Padding:** 0.5rem 1rem
- **Font-weight:** 800
- **Font-size:** 0.85rem
- **Letter-spacing:** 0.1em

### 3. Col-card (Панель даних)

```html
<div class="col-card">
  <span class="number">94%</span>
  <h3>Ключовий показник</h3>
  <p>Описання</p>
</div>
```
- **Бордер:** 4px solid var(--color-black)
- **Padding:** 2.5rem (var(--space-md))
- **Фон:** залежить від контексту розділу

### 4. Col-card з числом

```html
<span class="number">94%</span>
```
- **Font-size:** 5rem
- **Font-weight:** 900
- **Color:** var(--color-blue)
- **Line-height:** 1
- **Margin-bottom:** var(--space-sm)

### 5. Badge-tag (Мала мітка)

```html
<span class="badge-tag">Для Wójta</span>
```
- **Фон:** var(--color-black)
- **Текст:** var(--color-white)
- **Padding:** 0.5rem 1rem
- **Font-weight:** 800
- **Font-size:** 0.8rem
- **Letter-spacing:** 0.08em

### 6. Грід системи

#### grid-2
```html
<div class="grid-2">
  <div>Ліво</div>
  <div>Право</div>
</div>
```
- **Columns:** 1fr 1fr
- **Gap:** var(--space-lg) (80px)
- **Responsive:** 768px → 1 колона

#### grid-3
```html
<div class="grid-3">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>
```
- **Columns:** repeat(3, 1fr)
- **Gap:** var(--space-md) (40px)
- **1024px:** Переходить на 2 колони
- **768px:** 1 колона

#### grid-4
- **Columns:** repeat(4, 1fr)
- **Gap:** var(--space-md)
- **Responsive:** як grid-3

### 7. Hero-index (Числові показники)

```html
<div class="hero-index">
  <div class="index-row">
    <div class="index-val">85<small>%</small></div>
    <div class="index-desc">
      <strong>Грант від ЄС</strong>
      <span>На будівництво</span>
    </div>
  </div>
</div>
```
- **Фон:** var(--color-gray-light)
- **Бордер:** 4px solid var(--color-black)
- **Padding:** 1rem
- **index-val:** 2.5rem, 900 weight, var(--color-blue)

### 8. Wójt-bridge (Інформаційна смуга)

```html
<div class="woit-bridge-card">
  <span class="badge-tag">Для Wójta</span>
  <p class="woit-bridge-text"><strong>Gmina Lubin...</strong> текст</p>
  <a href="#">Читайте →</a>
</div>
```
- **Padding:** var(--space-md) 0
- **Border-bottom:** 4px solid var(--color-black)
- **Flex:** align-items center, gap 1.5rem

### 9. Contact-deliverables (Чек-лист)

```html
<div class="contact-deliverables">
  <strong>На першій консультації:</strong>
  <ul>
    <li>Технічна оцінка</li>
  </ul>
  <div class="note">Усі матеріали безкоштовні.</div>
</div>
```
- **Фон:** var(--color-gray-light)
- **Border-left:** 4px solid var(--color-blue)
- **Padding:** var(--space-sm) var(--space-md)
- **Color:** var(--color-gray-dark)
- **li::before:** '✓ ' синього кольору

### 10. FAQ Item

```html
<details class="faq-item col-card">
  <summary>Питання?</summary>
  <p>Відповідь</p>
</details>
```
- **Border-bottom:** 2px solid var(--color-black)
- **summary::after:** '+' / '−' символи
- **Font-weight:** 800
- **Margin-top:** 1rem перед абзацом

### 11. Process-card

```html
<div class="process-card col-card">
  <span class="number">1</span>
  <h3>Крок 1</h3>
  <p>Опис</p>
</div>
```
- **Всередину:** var(--color-black) розділу
- **Бордер:** 4px solid var(--color-gray-dark)
- **Color:** var(--color-white)

---

## 🎯 Розділи (Section Backgrounds)

### Білий розділ (Стандарт)
```html
<section id="problem">
  <!-- content -->
</section>
```
- **background:** var(--color-white)
- **color:** var(--color-black)
- **border-bottom:** 4px solid var(--color-black)

### Синій розділ (Контраст)
```css
#comparison {
  background-color: var(--color-blue);
  color: var(--color-white);
  border-bottom: 4px solid var(--color-black);
}
#comparison h2 { border-color: var(--color-white); }
#comparison .rubric { background-color: var(--color-white); color: var(--color-blue); }
```

### Чорний розділ (Процес)
```css
#process {
  background-color: var(--color-black);
  color: var(--color-white);
  border-bottom: 4px solid var(--color-white);
}
#process h2 { border-color: var(--color-white); }
#process .rubric { background-color: var(--color-white); color: var(--color-black); }
```

### Сіра розділ (Проблема)
- **background:** var(--color-gray-light)
- **color:** var(--color-black)
- **border-bottom:** 4px solid var(--color-black)

### Темно-сіра розділ (Контакт)
```css
#contact {
  background-color: var(--color-gray-dark);
  color: var(--color-white);
}
```

---

## 📱 Responsive Design

### Точки перелому
- **1024px:** Grid 3/4 → 2 колони
- **768px:** Усі гріди → 1 колона, H1 → 2.5rem
- **640px:** .woit-bridge-card → flex-direction: column

### Контейнер
```html
<div class="container">
  <!-- max-width: 1300px, padding: 0 var(--space-md) -->
</div>
```

---

## ✅ Чек-лист перед додаванням нового компонента

- [ ] Цей компонент вже існує на домашній сторінці?
- [ ] Можна переиспользувати `.col-card`, `.btn-primary`, `.rubric`?
- [ ] Чи потрібні нові CSS класи?
- [ ] Колір, шрифт, spacing — з системи вище?
- [ ] Тестовано на 768px та 1024px?

---

## 📝 HTML структура сторінки

```html
<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Назва | BTC Consulting</title>
  <link rel="stylesheet" href="../Ua/industrial-modern.css">
</head>
<body>
  <header>...</header>
  
  <main>
    <section id="section-name">
      <div class="container">
        <span class="rubric">Назва розділу</span>
        <h2>Заголовок розділу</h2>
        
        <!-- Вміст -->
      </div>
    </section>
  </main>
  
  <footer>...</footer>
</body>
</html>
```

---

## 🔗 Посилання на файли

- **CSS:** `/Users/max/Projects/Waste/web/Ua/industrial-modern.css` (917 рядків)
- **Приклад:** `/Users/max/Projects/Waste/web/v2/template-components.html`
- **Homepage:** `/Users/max/Projects/Waste/web/v2/index.html`
- **Technology:** `/Users/max/Projects/Waste/web/v2/technology.html`

---

## 🚀 Як використовувати

1. Відкрийте `template-components.html` у браузері для візуального прикладу
2. Копіюйте HTML структури з цього посібника
3. Не додавайте нові CSS класи — переиспользуйте наявні
4. Якщо чогось не вистачає, спочатку перевірте, чи воно вже на домашній сторінці

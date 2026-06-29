# Швидкий довідник компонентів BTC

## 🎨 Кольори (копіюй ці значення)

```css
var(--color-white)      /* #ffffff */
var(--color-black)      /* #0a0a0a */
var(--color-blue)       /* #0033a0 */
var(--color-gray-light) /* #f3f4f6 */
var(--color-gray-dark)  /* #374151 */
#86c2e8                 /* світло синя */
#3a9fe0                 /* середньо синя */
#bcd9ee                 /* блідо синя */
```

---

## 📏 Spacing (копіюй ці значення)

```css
var(--space-xs)  /* 0.5rem */
var(--space-sm)  /* 1rem */
var(--space-md)  /* 2.5rem */
var(--space-lg)  /* 5rem */
var(--space-xl)  /* 7rem */
```

---

## 🔤 Шрифти (усе Inter)

| Використання | Розмір | Вага | Трансформація |
|---|---|---|---|
| Найбільший заголовок | clamp(2.5rem, 5vw, 4.5rem) | 900 | UPPERCASE |
| Заголовок розділу | clamp(2.5rem, 5vw, 4rem) | 800 | UPPERCASE |
| Підзаголовок | 1.5rem | 800 | - |
| Основний текст | 1rem | 500 | - |
| Опис/Lead | 1.1rem | 500 | - |
| Мала мітка | 0.85rem | 800 | UPPERCASE |
| Число в карці | 5rem | 900 | - |

---

## 🎯 Популярні компоненти (копіюй HTML)

### Кнопка (первісна)
```html
<a href="#section" class="btn btn-primary">Текст</a>
```

### Кнопка (контур)
```html
<a href="#section" class="btn btn-outline">Текст</a>
```

### Тег розділу
```html
<span class="rubric">Назва розділу</span>
```

### Карта з числом
```html
<div class="col-card">
  <span class="number">94%</span>
  <h3>Заголовок</h3>
  <p>Опис</p>
</div>
```

### Мала мітка
```html
<span class="badge-tag">Для Wójta</span>
```

### Сітка 2 колони
```html
<div class="grid-2">
  <div class="col-card">Ліво</div>
  <div class="col-card">Право</div>
</div>
```

### Сітка 3 колони
```html
<div class="grid-3">
  <div class="col-card">1</div>
  <div class="col-card">2</div>
  <div class="col-card">3</div>
</div>
```

### Сітка 4 колони
```html
<div class="grid-4">
  <div class="col-card">1</div>
  <div class="col-card">2</div>
  <div class="col-card">3</div>
  <div class="col-card">4</div>
</div>
```

### Hero Index (числові показники)
```html
<div class="hero-index">
  <div class="index-row">
    <div class="index-val">85<small>%</small></div>
    <div class="index-desc">
      <strong>ГРАНТ ВІД ЄС</strong>
      <span>На будівництво заводу</span>
    </div>
  </div>
</div>
```

### Інформаційна смуга (Wójt Bridge)
```html
<div class="woit-bridge-card">
  <span class="badge-tag">Для Wójta</span>
  <p class="woit-bridge-text"><strong>Gmina Lubin розв'язала...</strong> коротке резюме</p>
  <a href="#">Читайте →</a>
</div>
```

### Чек-лист (Contact Deliverables)
```html
<div class="contact-deliverables">
  <strong>На першій консультації:</strong>
  <ul>
    <li>Технічна оцінка об'єкту</li>
    <li>Попередня кошторисна</li>
    <li>Сценарій фінансування</li>
  </ul>
  <div class="note">Всі матеріали безкоштовні.</div>
</div>
```

### FAQ (спадне питання)
```html
<details class="faq-item col-card">
  <summary>Питання?</summary>
  <p>Повна відповідь з деталями.</p>
</details>
```

### Процес карта (з числом)
```html
<div class="process-card col-card">
  <span class="number">1</span>
  <h3>Перший крок</h3>
  <p>Що робимо на цьому кроці</p>
</div>
```

---

## 📐 Розділи (Sections)

### Білий розділ (стандарт)
```html
<section id="problem">
  <div class="container">
    <span class="rubric">Назва</span>
    <h2>Заголовок</h2>
    <!-- вміст -->
  </div>
</section>
```
CSS (у index.html style):
```css
#problem {
  background-color: var(--color-white);
  color: var(--color-black);
  border-bottom: 4px solid var(--color-black);
}
```

### Синій розділ (контраст)
```css
#comparison {
  background-color: var(--color-blue);
  color: var(--color-white);
  border-bottom: 4px solid var(--color-black);
}
#comparison h2 { border-color: var(--color-white); }
#comparison .rubric { background-color: var(--color-white); color: var(--color-blue); }
#comparison .btn-outline { border-color: var(--color-white); color: var(--color-white); }
#comparison .btn-outline:hover { background-color: var(--color-white); color: var(--color-blue); }
```

### Чорний розділ (процес)
```css
#process {
  background-color: var(--color-black);
  color: var(--color-white);
  border-bottom: 4px solid var(--color-white);
}
#process h2 { border-color: var(--color-white); }
#process .rubric { background-color: var(--color-white); color: var(--color-black); }
```

### Сіра розділ (проблема)
```css
#team {
  background-color: var(--color-gray-light);
  color: var(--color-black);
  border-bottom: 4px solid var(--color-black);
}
```

### Темно-сіра розділ (контакт)
```css
#contact {
  background-color: var(--color-gray-dark);
  color: var(--color-white);
  border-bottom: 4px solid var(--color-black);
}
#contact h2 { border-color: var(--color-white); }
```

---

## 🔥 Найбільші помилки (не роби так!)

❌ Не додавай нові класи (`.new-card`, `.wizard-screen`)
✅ Переиспользуй `.col-card`, `.process-card`

❌ Не видумуй нові кольори
✅ Бери з CSS змінних або з градієнтів

❌ Не міняй spacing
✅ Бери з `var(--space-*)`

❌ Не робити justify-content: center без причини
✅ Використовуй grid-2/3/4 для розташування

❌ Не додавай animation без дозволу
✅ Смотри на hero бари або hero blueprint як на приклад

---

## 📱 Responsive Media Queries (копіюй)

```css
/* Планшет та менше */
@media (max-width: 1024px) {
  .grid-3, .grid-4 { grid-template-columns: 1fr 1fr; }
}

/* Мобільник */
@media (max-width: 768px) {
  .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; }
  h1 { font-size: 2.5rem; }
  section { padding: var(--space-lg) 0; }
}

/* Маленький мобільник */
@media (max-width: 640px) {
  .woit-bridge-card { flex-direction: column; }
  header { padding: 0.6rem 0; }
}
```

---

## 🧪 Як тестувати нові компоненти

1. Додай HTML у `template-components.html`
2. Відкрий у браузері (localhost:3000/v2/template-components.html)
3. Перевір на три розриви:
   - 1440px (десктоп)
   - 1024px (планшет)
   - 768px (мобільник)
4. Переконайся, що грід правильно перебудовується

---

## 🚀 Швидкий старт для нової сторінки

1. Скопіюй структуру з `index.html`:
   - Header
   - Main > Section > Container > Rubric + H2 + Grid
   - Footer

2. Замість нових стилів просто скоммбіную:
   - `<div class="grid-3">` для 3 карток
   - `<div class="col-card">` для кожної картки
   - `.rubric` для мітки розділу

3. Розфарбуй розділ (за допомогою CSS у тегу `<style>`):
   ```css
   #my-section {
     background-color: var(--color-white); /* або інший */
     color: var(--color-black);
     border-bottom: 4px solid var(--color-black);
   }
   ```

4. Все! Більше нічого не потрібно.

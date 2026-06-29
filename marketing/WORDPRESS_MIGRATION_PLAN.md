# BTC Consulting — План міграції сайту на WordPress
**Версія**: 1.0 | **Дата**: Червень 2026 | **Статус**: Технічний план

---

## Огляд задачі

Поточний стан: статичний HTML/CSS сайт (GitHub Pages або хостинг), три мовні версії (PL / UA / EN), кастомна CSS (glassmorphism, анімована canvas), кастомний JS-калькулятор.

Ціль: перенести на WordPress зі збереженням дизайну, доданням конверсійних елементів (форми, FAQ, нові сторінки) і зручним редагуванням контенту без розробника.

---

## Розділ 1 — Попередні рішення (прийняти до початку)

### 1.1 Домен і хостинг

**Домен**: `btcconsulting.pl` або `biotc.com.ua` — купити якщо ще немає.

**Рекомендований хостинг** (WordPress-оптимізований):

| Варіант | Ціна/міс | Плюси | Мінуси |
|---|---|---|---|
| **Kinsta** | $35+ | Найшвидший, staging, автобекапи | Дорогий |
| **SiteGround** (PL) | $6–15 | Популярний у Польщі, дешевший | Обмеження трафіку |
| **WP Engine** | $25+ | Managed, безпека | Дорогий |
| **Hostinger** (бюджет) | $3–7 | Найдешевший | Менш надійний |

**Рекомендація для BTC**: SiteGround Business або Kinsta Starter — баланс ціни/якості для B2B сайту.

### 1.2 Що зберігаємо, що переробляємо

| Елемент | Рішення |
|---|---|
| Дизайн (glassmorphism, кольори) | ✅ Зберегти через кастомний CSS |
| Шрифти (Outfit + Inter) | ✅ Google Fonts у WordPress |
| Анімація canvas у Hero | ⚠️ Перенести через HTML Block або плагін |
| JS-калькулятор | ⚠️ Перенести як кастомний блок або плагін |
| Контент PL | ✅ Перенести повністю |
| Контент UA | ✅ Через WPML або Polylang |
| Структура URL | ✅ `/pl/` → `/pl/` (зберігаємо для SEO) |

---

## Розділ 2 — Вибір теми WordPress

### Рекомендація: Тема GeneratePress + кастомний CSS

**Чому GeneratePress:**
- Надлегка (найшвидша тема в тестах GTMetrix)
- Повністю кастомізується через CSS без обмежень
- 100% сумісна з Gutenberg і Elementor
- Ціна: $59/рік (GPL)

**Альтернатива: Astra Pro** — схожі характеристики, трохи більше pre-built шаблонів.

**Що НЕ брати:**
- ❌ Дорогі "ready-made" теми (Avada, Divi) — важкі, складні для кастомізації
- ❌ Beaver Builder теми — зайва складність
- ❌ Безкоштовні теми — обмеження кастомізації

### Кастомна CSS-стратегія

Поточний `styles.css` / `industrial.css` переносяться повністю у:
- WordPress Admin → Appearance → Customize → Additional CSS (для глобального)
- Або GeneratePress → Site Library → Custom CSS

```css
/* Приклад перенесення blur-orbs і glassmorphism */
:root {
  --brand-blue: #046BD2;
  --brand-teal: #0D9488;
  --accent-orange: #D35400;
}
.blur-orb { /* CSS з поточного styles.css */ }
.glass-card { /* glassmorphism компоненти */ }
```

---

## Розділ 3 — Обов'язкові плагіни

### 3.1 Мультимовність

**Рекомендація: WPML** ($99/рік) або **Polylang Pro** ($99/рік)

| | WPML | Polylang |
|---|---|---|
| Якість | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Ціна | $99/р (Multilingual CMS) | $99/р (Pro) |
| Сумісність | Ідеальна | Дуже гарна |
| Складність | Більша | Менша |

**Структура URL після WPML:**
```
/pl/          → польська (основна)
/ua/          → українська
/en/ або /eu/ → англійська (EN)
```

### 3.2 SEO

**Yoast SEO Premium** ($99/рік) або **Rank Math Pro** ($59/рік)

- Автоматичний hreflang для мультимовності
- Schema markup (FAQ Schema — критично для AI-пошуку)
- XML sitemap
- Redirect manager (для збереження старих URL)

**Рекомендація**: Rank Math — дешевший, потужніший за функціями.

### 3.3 Форми (Lead Generation)

**WPForms Pro** ($199/рік) або **Gravity Forms** ($259/рік)

Для BTC потрібні:
- Форма "Bezpłatna ocena obiektu" (файловий upload — для звіту ОЧС)
- Форма контакту
- Email нотифікації

**Рекомендація**: WPForms — простіше налаштовувати, є file upload.

**Інтеграція**: підключити до CRM або Google Sheets через Zapier.

### 3.4 Page Builder (для нових сторінок без розробника)

**Cadence Blocks** (безкоштовно) + Gutenberg — достатньо для більшості сторінок.

Або **Elementor Pro** ($59/рік) — якщо потрібен drag-and-drop для більш складних макетів.

### 3.5 Безпека і бекапи

| Плагін | Функція | Ціна |
|---|---|---|
| **Wordfence** | Файрвол, захист від атак | Безкоштовно / $99/р Pro |
| **UpdraftPlus** | Автобекапи на Google Drive | Безкоштовно / $70/р |
| **WP Rocket** | Кешування, швидкість | $59/р |

### 3.6 Аналітика

- **Google Analytics 4** — через плагін Site Kit by Google (безкоштовно)
- **Hotjar** або **Microsoft Clarity** — карта кліків, сесії (безкоштовно)

---

## Розділ 4 — Структура сторінок у WordPress

### 4.1 Типи контенту (Custom Post Types)

Стандартних Pages достатньо для поточного масштабу. Якщо плануєте блог/кейси — додати:

```
Custom Post Types:
- Przypadki klientów (Кейси) — case-lubin + майбутні
- Artykuły / Blog — статті для SEO
```

### 4.2 Меню

```
Primary Menu (PL):
├── Rozwiązania (→ /pl/)
├── Technologia (→ /pl/technologia/)
├── Dofinansowanie (→ /pl/dofinansowanie/) [НОВА]
├── Hub & Spoke (→ /pl/hub-spoke/) [НОВА]
├── Case: Lubin (→ /pl/case-lubin/)
└── Kalkulator (→ /pl/kalkulator/)

Header CTA Button: "Bezpłatna ocena obiektu" (→ /pl/kontakt/)
```

### 4.3 Таблиця сторінок та їх WordPress slug

| Поточна сторінка | WordPress slug | Статус |
|---|---|---|
| `pl/index.html` | `/pl/` (homepage) | Перенести + доповнити |
| `pl/technology.html` | `/pl/technologia/` | Перенести + таблиця конфігурацій |
| `pl/simulator.html` | `/pl/kalkulator/` | Перенести JS-калькулятор |
| `pl/case-lubin.html` | `/pl/przypadek-lubin/` | Перенести + емоційний вхід |
| `pl/teo.html` | `/pl/analiza-teo/` | Перенести + FAQ |
| `pl/whitepaper.html` | `/pl/whitepaper/` | Перенести (lead magnet) |
| — | `/pl/dofinansowanie/` | НОВА |
| — | `/pl/hub-spoke/` | НОВА |
| — | `/pl/uwwtd/` | НОВА (контент готовий) |
| — | `/pl/kontakt/` | НОВА — форма аудиту |

---

## Розділ 5 — Перенесення кастомного функціоналу

### 5.1 Анімація Hero (canvas + ring animation)

Поточний `process_animation.py` генерує анімацію. У WordPress:

**Варіант A (рекомендований)**: HTML Block у Gutenberg
```html
<!-- Вставити canvas-блок через Custom HTML Widget -->
<canvas id="ring-canvas" aria-hidden="true"></canvas>
<script>
  // Перенести process_animation JS сюди
  // Або підключити як окремий файл через functions.php
</script>
```

**Варіант B**: Зареєструвати скрипт через `functions.php`:
```php
function btc_enqueue_scripts() {
    wp_enqueue_script('btc-hero-animation', 
        get_template_directory_uri() . '/js/hero-animation.js', 
        array(), '1.0', true);
}
add_action('wp_enqueue_scripts', 'btc_enqueue_scripts');
```

### 5.2 Калькулятор (simulator)

Поточний калькулятор написаний на JavaScript. Два варіанти:

**Варіант A — Shortcode** (простіше):
```php
// functions.php
function btc_calculator_shortcode() {
    ob_start();
    include get_template_directory() . '/templates/calculator.php';
    return ob_get_clean();
}
add_shortcode('btc_calculator', 'btc_calculator_shortcode');
```
Використання на сторінці: `[btc_calculator]`

**Варіант B — iframe** (найшвидше для міграції):
Залишити калькулятор як окрему HTML-сторінку, вбудувати через iframe у WordPress.
Мінус: не ідеально з SEO.

**Рекомендація**: Варіант A (shortcode) — правильна інтеграція.

### 5.3 Чат-бот (`chat.html`)

Якщо це кастомний чат — вбудувати через shortcode або iframe.
Якщо це AI чат (Tidio, Intercom, тощо) — підключити через плагін або код у header.

---

## Розділ 6 — Покроковий план міграції

### Фаза 0 — Підготовка (Тиждень 1)

- [ ] Купити домен (якщо немає) + налаштувати DNS
- [ ] Вибрати та замовити хостинг (SiteGround Business)
- [ ] Встановити WordPress 6.x
- [ ] Встановити тему GeneratePress
- [ ] Встановити плагіни: WPML + Rank Math + WPForms + Wordfence + UpdraftPlus + WP Rocket
- [ ] Налаштувати staging середовище (тестовий піддомен)
- [ ] Зробити повний backup поточного статичного сайту

### Фаза 1 — Базова структура (Тиждень 2)

- [ ] Перенести глобальний CSS (`styles.css` → Additional CSS / child theme)
- [ ] Налаштувати Header: лого + навігація + CTA кнопка
- [ ] Налаштувати Footer: контакти + посилання
- [ ] Налаштувати мовну структуру через WPML (PL / UA / EN)
- [ ] Налаштувати redirect зі старих URL на нові

### Фаза 2 — Перенесення існуючих сторінок (Тиждень 3)

- [ ] Головна (`/pl/`) — перенести контент + додати FAQ + блок wójta
- [ ] Технологія (`/pl/technologia/`) — перенести + таблиця конфігурацій
- [ ] Кейс Lubin (`/pl/przypadek-lubin/`) — перенести + емоційний вхід
- [ ] TEO (`/pl/analiza-teo/`) — перенести + FAQ
- [ ] Whitepaper (`/pl/whitepaper/`) — перенести + форма завантаження
- [ ] Калькулятор (`/pl/kalkulator/`) — перенести через shortcode

### Фаза 3 — Нові сторінки (Тиждень 4–5)

- [ ] Створити `/pl/dofinansowanie/` (таблиця грантів + процес + FAQ)
- [ ] Створити `/pl/hub-spoke/` (схема + економіка + CTA)
- [ ] Створити `/pl/uwwtd/` (контент з `uwwtd-pillar-pl.md` готовий)
- [ ] Створити `/pl/kontakt/` — форма аудиту об'єкту (WPForms)

### Фаза 4 — UA та EN версії (Тиждень 5–6)

- [ ] Перенести UA версію через WPML (синхронізація зі структурою PL)
- [ ] Перенести EN версію
- [ ] Перевірити hreflang теги (Rank Math автоматично)

### Фаза 5 — Тестування і Launch (Тиждень 6–7)

- [ ] Технічний аудит: Screaming Frog або Rank Math Site Audit
- [ ] Перевірка мета-тегів, title, description для всіх мов
- [ ] Перевірка форм (тестовий submit)
- [ ] Перевірка мобільної версії (всі брейкпоінти)
- [ ] PageSpeed Insights — ціль: >85 (мобайл), >95 (десктоп)
- [ ] Перевірка всіх redirect (301) зі старих URL
- [ ] Подати оновлений sitemap у Google Search Console
- [ ] **Launch**: переключити DNS з GitHub Pages на новий хостинг

---

## Розділ 7 — Зміна DNS (перемикання)

```
Поточний: GitHub Pages (btc.github.io або подібне)
Новий:    хостинг SiteGround (IP надається при реєстрації)

Кроки:
1. В панелі реєстратора домену змінити A record на IP SiteGround
2. TTL: встановити на 300 (5 хв) перед switchover
3. Час поширення: 2–48 годин
4. Після: повернути TTL до 3600
5. Залишити старий статичний сайт живим ще 2 тижні для страхування
```

---

## Розділ 8 — Бюджет

### Річні витрати (орієнтовно)

| Стаття | Ціна/рік |
|---|---|
| Домен (.pl або .com.ua) | $15–20 |
| Хостинг (SiteGround Business) | $150–200 |
| Тема GeneratePress | $59 |
| WPML Multilingual CMS | $99 |
| Rank Math Pro | $59 |
| WPForms Pro | $199 |
| WP Rocket | $59 |
| UpdraftPlus Premium | $70 |
| Wordfence Premium | $99 |
| **РАЗОМ** | **~$810–860/рік** |

### Одноразові витрати (розробка)

| Робота | Оцінка годин | При $40/год |
|---|---|---|
| Налаштування WordPress + теми | 8 год | $320 |
| CSS перенесення | 6 год | $240 |
| Перенесення сторінок (5 існуючих) | 10 год | $400 |
| Нові сторінки (3–4) | 12 год | $480 |
| Калькулятор (shortcode) | 8 год | $320 |
| WPML налаштування | 6 год | $240 |
| Тестування і launch | 4 год | $160 |
| **РАЗОМ** | **~54 год** | **~$2,160** |

---

## Розділ 9 — Після запуску (перші 30 днів)

### SEO після міграції

1. Перевірити Google Search Console — немає помилок 404
2. Переіндексувати через `Fetch as Google` (Search Console)
3. Відстежувати позиції ключових запитів (Rank Math має трекер)
4. Встановити Google Analytics 4 → відстежувати конверсії форм

### Контент-план (перші 3 місяці після launch)

| Місяць | Дія |
|---|---|
| 1 | Публікація `/dofinansowanie/` + `/hub-spoke/` |
| 2 | Перша стаття в блозі: "UWWTD 2024 — co gminy muszą zrobić do 2030" |
| 3 | Друга стаття: "HTC vs. spalanie — porównanie kosztów dla gminy 30 000 PE" |

### Відстеження конверсій

Налаштувати в Google Analytics:
- Конверсія: submitting форми "Bezpłatna ocena obiektu"
- Конверсія: завантаження whitepaper
- Конверсія: >3 хвилин на сайті (залученість)

---

## Резюме: стек WordPress для BTC Consulting

```
Хостинг:      SiteGround Business
CMS:          WordPress 6.x
Тема:         GeneratePress + кастомний CSS
Мультимовність: WPML Multilingual CMS
SEO:          Rank Math Pro
Форми:        WPForms Pro
Швидкість:    WP Rocket
Безпека:      Wordfence + UpdraftPlus
Аналітика:    Google Analytics 4 + Microsoft Clarity
```

---

*Документ підготовлено на основі: поточного сайту web/pl/ + web/Ua/, marketing/phase2_supremseo_plan.md, wiki/index.md, brand_strategy.md*

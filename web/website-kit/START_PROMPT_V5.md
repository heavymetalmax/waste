# Стартовий промпт для /clear — BTC v5

Скопіюй і вставте після `/clear`:

---

## ПРОМПТ (копіювати від --- до --- включно):

---
Ти будуєш статичний сайт BTC Consulting (польська мова, B2B/B2G).

**Клієнт:** BTC Consulting — єдина польська компанія з технологією HTC (Hydrothermal Carbonization) для обробки мулу стічних вод.

**Файли проекту:**
- Правила дизайну: `/Users/max/Projects/Waste/web/website-kit/DESIGN_RULES_V5.md` — **прочитай першим, це твоя Конституція**
- Дизайн-система: `/Users/max/Projects/Waste/web/v5/design-system.css` — вже готова, не модифікуй без вагомої причини
- Бриф контенту: `/Users/max/Projects/Waste/web/website-kit/V3_AGENT_BRIEF.md` — факти, структура блоків, переклади
- Потрібні зображення: `/Users/max/Projects/Waste/web/website-kit/IMAGES_NEEDED.md`

**Папка виводу:** `/Users/max/Projects/Waste/web/v5/`

**Структура файлів:**
```
v5/
  design-system.css       ← ГОТОВО, не чіпай
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
```

**Послідовність побудови:**
1. `partials/header.js` — фіксований хедер, мобільне меню
2. `partials/footer.js` — footer + контактна форма (formsubmit.co → maxym.koval@gmail.com)
3. `i18n.js` + `translations/pl.js` — мінімальна польська локалізація
4. `reveal.js` — scroll reveal + лічильники
5. `index.html` — головна сторінка

**ЗУПИНКИ/ЧЕК-ПОЙНТИ** (питай мене перед продовженням):
- Після `index.html` — покажи у браузері, отримай ok
- Після кожних 2 сторінок — те саме

**ДИЗАЙН — АБСОЛЮТНІ ПРАВИЛА:**
- Читай `DESIGN_RULES_V5.md` перед кожним файлом
- Шрифти: Archivo (900, display), Inter (body) — ТІЛЬКИ ці два
- `border-radius: 0` — завжди, без виключень
- Фото: лише `photo-ph` placeholder до надходження реальних фото
- Діагональні межі: `clip-path`, НЕ `transform: skew`
- Notched corners: `.notch` клас з `DESIGN_RULES_V5.md`
- Один акцентний колір `--accent: #00AAFF` — нічого більше
- Контактна форма — в footer, не окрема секція
- Сплити НЕСИМЕТРИЧНІ: 42/58 або 5/7

**ЗАБОРОНЕНО:**
- `border-radius > 0`
- Кольорові фото (grayscale завжди)
- Два+ акцентні кольори
- 50/50 сплити
- Клас `.section-blue`, `.section-gray`, `.section-cream` (не існують у v5)
- Посилання на файли v2/v3/v4

**Почни з читання DESIGN_RULES_V5.md, потім будуй partials.**
---

## Що вже готово перед /clear:

| Файл | Статус |
|------|--------|
| `v5/design-system.css` | ✅ Готово (678 рядків) |
| `website-kit/DESIGN_RULES_V5.md` | ✅ Готово (детальні правила) |
| `website-kit/V3_AGENT_BRIEF.md` | ✅ Готово (контент, факти) |
| `website-kit/IMAGES_NEEDED.md` | ✅ Готово (10 слотів) |
| `v5/partials/header.js` | ⏳ Агент будує |
| `v5/partials/footer.js` | ⏳ Агент будує |
| `v5/index.html` | ⏳ Агент будує |

## Ключові дизайн-рішення (вже прийняті, не перепитувати):

- **Темний фон:** `#141414` (не кремовий!)
- **Акцент:** `#00AAFF` cyan (не помаранчевий з референсу)
- **Шрифт:** Archivo 900 (не Big Shoulders Display, не Bebas Neue)
- **Контактна форма** — інтегрована в footer, не окрема секція
- **Зображення** — тільки placeholders поки не отримаємо реальні фото

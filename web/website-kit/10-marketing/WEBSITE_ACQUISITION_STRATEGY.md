# BTC Consulting — Сайт як інструмент залучення клієнтів
**Версія**: 1.0 | **Дата**: Червень 2026 | **Статус**: Стратегічний документ

---

## Висновок одним реченням

Поточний сайт пояснює технологію HTC — але не веде відвідувача до дії. Щоб стати машиною залучення клієнтів, він повинен відповідати на одне питання: *"Що мені робити прямо зараз, щоб вирішити проблему осаду?"*

---

## Частина 1 — Де ми зараз і чому це не конвертує

### Що є на сайті

Поточна структура (`/pl/`):
- `index.html` — Hero + технологічний опис + статистика
- `technology.html` — технічні деталі HTC
- `simulator.html` — калькулятор (є, але прихований у навігації)
- `teo.html` — що таке TEO
- `case-lubin.html` — кейс MPWiK Lubin
- `mission.html`, `whitepaper.html`, `chat.html`

### Основна проблема: сайт технологічний, а не конверсійний

Посадова особа (wójt, директор ОЧС) заходить і бачить:
- *"Kondensujemy wszystkie ogromne problemy z osadami"* — красиво, але не відповідь на питання
- Анімована статистика (x5, 75%, <0.01 мм) — вражає, але не веде до кроку
- Кнопки *"Uzyskaj raport"* і *"Ekonomika procesu"* — куди саме? навіщо саме зараз?

Рада відправила директора ОЧС перевірити, чи є якесь рішення для мулу. Він провів 40 секунд на головній, не знайшов відповіді на *"скільки це коштує нам"* і пішов. **Конверсії немає.**

### Три ключових gap (з аудиту `content-strategy-brief.md`)

**Gap 1 — Два читачі без розрізнення**
Wójt / голова міста питає: *"Чи можу я це захистити перед радою?"*
Директор ОЧС / інженер питає: *"Чи це реально працює? Скільки коштує?"*
Зараз сайт технічний — відповідає лише другому. Перший, хто і приймає рішення, нічого не знаходить.

**Gap 2 — Відсутність FAQ**
Головна сторінка — перший контакт. Саме тут найбільше незакритих заперечень:
- *"Ми замалі (8 000 RLM) — це не для нас"*
- *"Це дорого — у нас немає бюджету"*
- *"2030 ще далеко — можна почекати"*
- *"Ми вже маємо AD — чи потрібне нам HTC?"*

Без відповідей на ці питання відвідувач іде в Google і не повертається.

**Gap 3 — CTA без пояснення цінності**
*"Prześlij raport swojej oczyszczalni"* — хороший перший крок. Але не сказано:
- Що конкретно отримає клієнт у відповідь?
- За скільки часу?
- Навіщо без цього не можна отримати грант?

---

## Частина 2 — Хто наш клієнт і як він приймає рішення

### Три аудиторії сайту

#### Аудиторія A: Wójt / Burmistrz / Prezydent міста
**Мотиватор**: уникнути штрафів UWWTD + виглядати як лідер у своєму виборчому окрузі
**Страх**: *"Буду першим, якщо це не спрацює"* + *"Це надто складно/дорого"*
**Що шукає на сайті**: чи хтось інший вже зробив це? скільки коштувало муніципалітету (не всього)?
**Trigger до дії**: кейс Lubin (соціальний доказ) + грантове покриття (70–90% = мінімальний ризик)

#### Аудиторія B: Директор/Начальник ОЧС
**Мотиватор**: вирішити проблему осаду назавжди, оптимізувати OPEX
**Страх**: *"А раптом технологія не спрацює на нашому осаді?"* + *"Чи проходимо ми по RLM?"*
**Що шукає**: технічні параметри, досвід схожих об'єктів, конкретні цифри
**Trigger до дії**: TEO-аналіз з безкоштовним первинним оглядом, дані з Lubin

#### Аудиторія C: Спеціаліст з грантів / Підрядник EPC
**Мотиватор**: знайти рішення яке вписується у вимоги FENX.01.03 / FEnIKS
**Страх**: *"Чи HTC є допустимим методом за польським законодавством?"*
**Що шукає**: нормативна база, відповідність UWWTD, технічна документація
**Trigger до дії**: whitepaper + посилання на Розп. МŚ 2015 (HTC = Metoda 1)

---

## Частина 3 — Нова архітектура конверсії

### Принцип: Hook → Reframe → Exit → Action

Кожна сторінка повинна вести відвідувача через 4 стадії:

```
HOOK        → зачепити через біль (проблема осаду / дедлайн UWWTD)
REFRAME     → перевернути фрейм (гранти = це не дорого, це безкоштовно)
EXIT        → закрити заперечення (чому BTC, чому зараз)
ACTION      → один чіткий крок (безкоштовна оцінка об'єкту)
```

### Нова структура сайту

```
/pl/ (Polish — головний ринок)
│
├── /           → Головна (лендінг — конверсія)
├── /technologia/    → Технологія + порівняльна таблиця конфігурацій
├── /dofinansowanie/ → Гранти і фінансування [НОВА СТОРІНКА]
├── /hub-spoke/      → Hub & Spoke для малих гмін [НОВА СТОРІНКА]
├── /case-lubin/     → Кейс MPWiK Lubin (емоційний + цифри)
├── /teo/            → TEO — що це і навіщо (конверсія в leads)
├── /kalkulator/     → Калькулятор (зараз: simulator.html)
├── /uwwtd/          → Регуляторна сторінка + дедлайни [НОВА — контент готовий]
├── /whitepaper/     → Завантаження whitepaper (lead magnet)
└── /kontakt/        → Контакт + форма аудиту об'єкту
```

---

## Частина 4 — Конкретні зміни по сторінках

### 4.1 Головна (`index.html`) — пріоритет #1

#### Що залишити
- Hero H1 — сильний, залишити
- Анімована статистика — залишити, але упорядкувати
- Загальна структура блоків

#### Що додати / змінити

**Блок для wójta (одразу після Hero)**
```
[Dla Wójta / Burmistrza]
Gmina Lubin rozwiązała problem osadu za 15% własnych środków.
EU zapłaciło resztę (FENX.01.03). Decyzja rady: 2 głosowania.
→ Czytaj jak to zrobili [link do case-lubin]
```

**FAQ (після блоку проблеми)**
Мінімум 5 питань:
- *"Mamy 8 000 RLM — czy to za mało?"* → Hub & Spoke — 3–5 gmin na jeden hub.
- *"Projekt kosztuje miliony — nie mamy budżetu"* → FENX.01.03 pokrywa do 70%. Gmina płaci 15–30%.
- *"Mamy do 2030 — mamy czas"* → Projekt infrastrukturalny wymaga min. 3–4 lat. Teraz to ostatni moment na wniosek grantowy.
- *"Mamy już AD — po co HTC?"* → TH-booster zwiększa produkcję biogazu o +30% bez wymiany reaktora.
- *"Czy HTC jest legalny w Polsce?"* → Tak — Rozporządzenie MŚ 2015, Metoda 1. Status End-of-Waste dostępny.

**Підсилений CTA блок**
```
Wyślij nam raport swojej oczyszczalni.
W ciągu 5 dni roboczych dostaniesz:
✓ Wstępną ocenę czy obiekt kwalifikuje się do HTC
✓ Szacowany poziom dofinansowania (FENX / NFOŚiGW)
✓ Orientacyjny CAPEX i OPEX dla Twojego profilu
To pierwsza z 5 kroków do gotowego wniosku grantowego.
[Wyślij dane obiektu →]
```

#### H2 заголовки → питальні (для AI-пошуку)
- ❌ *"Technologia TH-AD-HTC"* → ✅ *"Jak działa technologia HTC?"*
- ❌ *"Korzyści dla gminy"* → ✅ *"Co gmina zyska na HTC?"*
- ❌ *"Referencje"* → ✅ *"Czy ktoś już to zrobił w Polsce?"*

---

### 4.2 Кейс Lubin (`case-lubin.html`) — пріоритет #2

#### Емоційний вхід (додати на початку)
```
MPWiK Lubin wydawał 550 PLN/tonę na zagospodarowanie osadu.
Przy 3 800 tonach rocznie — to ponad 2 mln PLN co roku, bez żadnego produktu na wyjściu.
Zarząd wiedział, że coś trzeba zmienić. Pytanie było: co i czy jest na to finansowanie.
```

#### Місток до малих об'єктів (наприкінці)
```
Lubin ma 100 000 RLM. Twoja gmina ma 12 000?
W modelu Hub & Spoke 3–4 gminy dzielą jeden hub.
Czynsz za przyjęcie osadu (PLN 200–225/t) jest niższy niż obecny koszt utylizacji.
[Sprawdź czy Twoje sąsiedztwo pasuje do Hub & Spoke →]
```

---

### 4.3 Нова сторінка: `/dofinansowanie/` — пріоритет #3

**Мета**: конвертувати скептиків "це дорого" і людей що готують заявки

**Структура:**
1. Hero: *"Instalacja HTC za 15–30% własnych środków. Reszta z UE."*
2. Таблиця програм фінансування (FENX.01.03 / NFOŚiGW / KPO / FEnIKS)
3. Покроковий процес отримання гранту (6 кроків, BTC супроводжує на кожному)
4. FAQ: умови відмови, realny success rate, терміни
5. CTA: *"Sprawdź czy Twój projekt kwalifikuje się"*

**Ключові цифри для сторінки:**
```
FENX.01.03:  do 70% CapEx | EUR 1.05B dostępne | termin: 31.12.2029
NFOŚiGW:     do 100% pożyczka + 30–50% umorzenie | PLN 100M
FEnIKS:      łącznie PLN 30B na wod-kan
```

---

### 4.4 Нова сторінка: `/hub-spoke/` — пріоритет #4

**Мета**: відкрити ринок малих гмін (<15 000 RLM), які зараз не бачать себе як клієнтів

**Структура:**
1. Hero: *"Sama gmina nie może sobie pozwolić. 3 gminy — mogą."*
2. Пояснення моделі (хаб + 3–5 спойків, схема)
3. Економіка: кожна гміна платить PLN 200–225/т (vs PLN 550/т зараз)
4. Юридична структура консорціуму (консорціум гмін, договір)
5. Кроки до старту (BTC ідентифікує сусідів, ініціює консорціум)
6. CTA: *"Sprawdź czy Twoje sąsiednie gminy pasują do modelu"*

---

### 4.5 Технологія (`technology.html`)

**Додати порівняльну таблицю конфігурацій:**

| Конфігурація | Для кого | Потрібна інфра | Орієнтовний CAPEX |
|---|---|---|---|
| **HTC Standalone** | >15 000 RLM, нова установка | Без вимог | PLN 18–30M |
| **TH-Booster** | Є AD-камера, хочуть +30% біогазу | Існуюча AD | PLN 5–9M |
| **TH-AD-HTC** (повна петля) | >50 000 RLM, максимум ефективності | Місце під будівництво | PLN 35–70M |

**Додати секцію "Dlaczego to nie jest eksperyment":**
- 11 років досліджень AGH (2015–2026)
- 6 перевірених ОЧС: Orzesze, Żory, Lubin, Bytom, Gliwice, Kraków (20K–800K RLM)
- MPWiK Lubin — комерційне підтвердження (X.2025)
- AGH отримала 2 гранти NSC у 2025 на дослідження мікропластику в осаді

---

## Частина 5 — CTA-архітектура (один перший крок)

### Головний CTA на всьому сайті: "Bezpłatna ocena obiektu"

Це низькоризиковий перший крок для обох аудиторій:
- Wójt: нічого не підписує, тільки надсилає дані об'єкту
- Інженер: отримує технічну оцінку + грантовий потенціал

**Що клієнт отримує (комунікувати явно):**
```
W ciągu 5 dni roboczych dostaniesz:
1. Wstępna kwalifikacja obiektu do HTC / Hub & Spoke
2. Szacowany poziom dofinansowania (FENX / NFOŚiGW)
3. Orientacyjny CAPEX i OPEX
4. Rekomendację następnego kroku (TEO lub bezpośrednia koncepcja)
To nic nie kosztuje. Dane obiektu można znaleźć w KPOŚK lub u operatora.
```

**Де розміщений CTA:**
- Header (кнопка завжди видна)
- Hero (головна кнопка)
- Після блоку кейсу Lubin
- В кінці кожної підсторінки
- Калькулятор → результат → одразу CTA

---

## Частина 6 — Customer Journey Map

### Шлях A: Wójt (прийняв рішення запропонувати щось раді)

```
1. TRIGGER:    Чує про UWWTD або отримує рахунок за утилізацію
2. ПОШУК:      Google: "utylizacja osadu ściekowego dofinansowanie"
3. САЙТ:       Головна → Hero → FAQ ("nie mamy budżetu") → Case Lubin
4. СИГНАЛ:     Бачить "Gmina Lubin: 15% własnych środków" → ВІРИТЬ
5. ДІЯ:        Заповнює форму "Bezpłatna ocena obiektu" / телефонує
6. НАСТУПНИЙ:  BTC надсилає попередню оцінку → призначає дзвінок
```

### Шлях B: Директор ОЧС (шукає технічне рішення)

```
1. TRIGGER:    Отримує наказ шукати рішення для осаду / UWWTD compliance
2. ПОШУК:      Google: "HTC osad ściekowy Polska" / "technologia HTC oczyszczalnia"
3. САЙТ:       Головна → Technology → конфігурації → Whitepaper (завантажує)
4. СИГНАЛ:     Whitepaper = 40+ сторінок технічних даних → ДОВІРЯЄ
5. ДІЯ:        Заповнює форму або дзвонить напряму
6. НАСТУПНИЙ:  BTC проводить технічну консультацію → TEO-пропозиція
```

### Шлях C: EPC підрядник або грантовий консультант

```
1. TRIGGER:    Клієнт (gmina) просить включити HTC у проектну документацію
2. ПОШУК:      Шукає технічну специфікацію + правова база
3. САЙТ:       UWWTD сторінка → Technology → Whitepaper → Kontakt
4. СИГНАЛ:     Пряме посилання на Розп. МŚ 2015 + End-of-Waste → ДОКУМЕНТ
5. ДІЯ:        Партнерський дзвінок (B2B співпраця)
6. НАСТУПНИЙ:  BTC + EPC спільна пропозиція для gminy
```

---

## Частина 7 — Пріоритети реалізації

### Фаза 1 — "Мінімум для конверсії" (1–2 тижні)

| Зміна | Де | Вплив |
|---|---|---|
| FAQ блок | Головна | ⭐⭐⭐⭐⭐ |
| Блок для wójta | Головна | ⭐⭐⭐⭐⭐ |
| Підсилений CTA з поясненням | Всюди | ⭐⭐⭐⭐⭐ |
| Емоційний вхід у Lubin кейсі | case-lubin | ⭐⭐⭐⭐ |
| Місток "маленька gmina" у Lubin | case-lubin | ⭐⭐⭐⭐ |

### Фаза 2 — "Нові конверсійні сторінки" (3–5 тижнів)

| Сторінка | Пріоритет | Аудиторія |
|---|---|---|
| `/dofinansowanie/` | 🔴 Критично | Скептики "дорого", підрядники |
| `/hub-spoke/` | 🔴 Критично | Малі gminy (<15K RLM) |
| `/uwwtd/` | 🟠 Важливо | SEO, AI-пошук, підрядники |

### Фаза 3 — "SEO і AI-пошук" (паралельно)

- H2 заголовки → питальні на всіх сторінках
- Schema markup (FAQ Schema) на кожній сторінці
- Internal linking: кожна сторінка посилається на `/dofinansowanie/` і `/kontakt/`
- Blog/Articles: статті під ключові запити ("utylizacja osadu 2025", "UWWTD Polska")

---

## Частина 8 — KPI для відстеження

| Метрика | Поточно | Ціль (3 місяці) |
|---|---|---|
| Форм "Bezpłatna ocena" / місяць | ? | 5–10 кваліфікованих |
| Час на сайті | ? | >3 хв (зараз, ймовірно, <1 хв) |
| Завантажень whitepaper | ? | 30–50/місяць |
| Калькулятор → дія | ? | >20% |
| Повернення відвідувачів | ? | >25% |

---

## Резюме: що міняємо і навіщо

| Стара парадигма | Нова парадигма |
|---|---|
| *"Пояснюємо HTC"* | *"Вирішуємо проблему осаду"* |
| Один тип читача (технічний) | Два читачі: wójt + інженер |
| CTA = кнопка без контексту | CTA = цінність + наступний крок |
| Технологія як центр | Гранти + кейс Lubin як центр |
| 5 сторінок, не пов'язаних | Архітектура конверсії з логікою переходів |

---

*Документ підготовлено на основі: wiki/messaging-strategy.md, wiki/client-segments.md, wiki/strategy-reframe.md, web/content-strategy-brief.md, marketing/communication_guide.md, marketing/EXECUTIVE_SUMMARY_v4.md*

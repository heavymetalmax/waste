# План висококонверсійного сайту BTC Consulting
**Мета:** перетворити відвідувача (wójt + naczelnik OCS) на SQL (Sales Qualified Lead) за 1 сесію  
**Дата:** 2026-07-01 | **Статус:** v1 — чернетка для опрацювання

---

## 0. Стратегічна рамка

### Хто купує і як вони думають

| Персона | Wójt / Burmistrz | Naczelnik OCS (інженер) |
|---|---|---|
| Питання #1 | "Чи можу я захистити це перед радою?" | "Чи це реально працює?" |
| Страх | Штрафи, публічний скандал, витрати без результату | Нова технологія провалиться — я відповідаю |
| Мотивація | Вирішити проблему дешево за допомогою ЄС-грантів | Технічне рішення з доведеною базою |
| Тригер дії | Дедлайн + гроші вже доступні | Референтна установка + AGH |
| CTA для нього | "Bezpłatna ocena — dowiedz się czy kwalifikujesz się na dotację" | "Pobierz whitepaper techniczny" |

### Конверсійна логіка (з messaging-strategy.md)

```
HOOK → REFRAME → EXIT → SCARCITY → CTA

HOOK:    "Do 2027 każda oczyszczalnia musi mieć rozwiązanie dla osadu"
REFRAME: "Instalacja HTC kosztuje X. Z dotacjami — 0,15X. Ale dotacje są teraz"
EXIT:    "Jedyna polska platforma z własną technologią HTC i 10+ latami z AGH"
SCARCITY:"BTC przyjmuje 8-10 nowych projektów rocznie. Kolejka już rośnie"
CTA:     "Bezpłatna wstępna ocena — 2 tygodnie, bez zobowiązań"
```

### Якірна фраза (використовувати на всіх сторінках)
> **"Osad to problem dziś. Zasób jutro. Okno dotacji zamknie się wcześniej niż myślisz."**

---

## 1. Архітектура сайту (повна карта)

```
/                          ← Головна (hook для всіх)
/technologia               ← Технологія HTC (для інженера)
/teo                       ← Аналіз TEO (воріт до гранту)
/dotacje                   ← Гранти і фінансування (НОВА — критична)
/hub-spoke                 ← Кластерна модель (НОВА — для малих гмін)
/case-lubin                ← Кейс MPWiK Lubin (соціальний доказ)
/uwwtd                     ← Директива UWWTD 2024/3019 (SEO-стаття)
/kalkulator-roi            ← ROI-калькулятор (головний конверсійний інструмент)
/misja                     ← Про BTC / команда
/whitepaper                ← Технічний документ (лід-магніт)
```

### Воронка за температурою ліда

```
ХОЛОДНИЙ (вперше чує про HTC)
  └─► / → /uwwtd → /kalkulator-roi → контакт

ТЕПЛИЙ (знає про UWWTD, шукає рішення)
  └─► / → /technologia → /teo → контакт

ГАРЯЧИЙ (готовий діяти, шукає кого найняти)
  └─► /case-lubin → /teo → контакт
  └─► /dotacje → /teo → контакт

МАЛІ ГМІНИ (не можуть собі дозволити самостійно)
  └─► /hub-spoke → /kalkulator-roi → контакт
```

---

## 2. Сторінка за сторінкою

---

### `/` — Головна

**Мета:** утримати обидві персони перші 8 секунд, направити кожного на свій шлях.

#### Hero-секція
```
[H1] Tradycyjna utylizacja osadu umiera.
     Nie metaforycznie. Finansowo i prawnie.

[Sub] Do 2027 roku każda polska oczyszczalnia musi mieć plan.
     Dotacje UE pokrywają do 85% kosztów — ale tylko dla tych, którzy zaczną teraz.

[CTA-A] Sprawdź czy Twoja gmina kwalifikuje się →   (для wójt)
[CTA-B] Zobacz jak działa technologia HTC →           (для інженера)
```

#### Блок "Два читачі" (після hero)
```
┌─────────────────────────┐  ┌─────────────────────────┐
│ JESTEM WÓJTEM / ZARZĄDEM│  │ JESTEM KIEROWNIKIEM OCS │
│                         │  │                         │
│ Szukam rozwiązania,     │  │ Szukam technologii       │
│ które obroję przed radą │  │ która realnie zadziała   │
│                         │  │                         │
│ → Sprawdź dotacje       │  │ → Technologia HTC        │
└─────────────────────────┘  └─────────────────────────┘
```

#### Секція болю (цифри)
```
Polska produkuje 700 000 ton osadu rocznie.
Spalarnie obsługują tylko 23%.
Reszta? Coraz mniej miejsca. Coraz wyższe koszty. Coraz ostrzejsze przepisy.

[Середня вартість зараз]  PLN 550/t
[З HTC przez BTC]         PLN 200–225/t
[Oszczędność]             ~60%
```

#### Три шляхи (для різних розмірів)
```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ >15 000 RLM  │  │ <15 000 RLM  │  │ Nie wiem     │
│              │  │              │  │ od czego      │
│ Własna       │  │ Model        │  │ zacząć        │
│ instalacja   │  │ Hub & Spoke  │  │               │
│ HTC          │  │ z sąsiadami  │  │               │
│              │  │              │  │               │
│ → Dowiedz się│  │ → Dowiedz się│  │ → Kalkulator  │
└──────────────┘  └──────────────┘  └──────────────┘
```

#### Соціальний доказ
```
✓ 10+ lat badań z AGH Kraków
✓ Pierwsza komercyjna instalacja: MPWiK Lubin (2025)
✓ HTC oficjalnie dopuszczona w Polsce od 14.01.2025
✓ Jedyna polska technologia własna (HTC-S, HTC-D, TH+HTC)
```

#### FAQ (5 питань — закривають головні заперечення)
```
Q: Mamy 8 000 RLM — czy to za mało?
A: Solo — tak. W modelu Hub & Spoke z 3-4 sąsiednimi gminami — nie. 
   Jeden hub obsługuje osad z 4-5 okolicznych oczyszczalni.

Q: Czy jest na to finansowanie?
A: Tak. FEnIKS, KPO i NFOŚiGW pokrywają 75–90% kosztów instalacji.
   Gmina płaci 10–25% z własnego budżetu operacyjnego.

Q: Termin UWWTD to 2035 — mamy czas.
A: Projekt infrastrukturalny od TEO do oddania = 3–4 lata minimum.
   Dotacje to system kolejkowy — kto złoży wcześniej, wygrywa.

Q: Czy HTC to sprawdzona technologia?
A: BTC razvija HTC od ponad 10 lat z AGH Kraków. 
   Pierwsza instalacja komercyjna (Lubin) odebrana przez klienta w 2025.

Q: Ile kosztuje pierwsza rozmowa z BTC?
A: Nic. Bezpłatna ocena wstępna: 2 tygodnie, raport czy obiekt kwalifikuje się do HTC i dotacji.
```

#### Фінальний CTA
```
[Przeslij dokumentację oczyszczalni — dostaniesz wstępną ocenę w 2 tygodnie]
Bez zobowiązań. Bez kosztów. Z konkretną odpowiedzią czy HTC i dotacja są dla Ciebie.
```

---

### `/technologia` — Технологія HTC

**Мета:** переконати інженера що технологія реальна, доведена, і підходить для його ОС.

#### Структура
1. **Hero:** "Proces trwający w naturze miliony lat — skracamy do 2 godzin"
2. **Порівняльна таблиця 3 конфігурацій** (КРИТИЧНО — зараз відсутня):

| | HTC-S | HTC-D | TH+HTC |
|---|---|---|---|
| Для кого | >15K RLM, без AD | Будь-яка з AD | >50K RLM, є AD |
| Що на вході | Осад після біологічного очищення | Стабілізований осад | Стабілізований осад |
| Орієнтовний CAPEX | PLN 18–30M | PLN 15–25M | PLN 35–70M |
| Енергетика | Тепло для власних потреб | Тепло для власних потреб | **Електрика + тепло (самодостатність)** |
| Найбільший плюс | Просто, без AD | Інтеграція з існуючим AD | Повна незалежність від мережі |

3. **Таблиця до/після hydrochar:**
```
Волога:    76–84% → 30–40%     (4× краще зневоднення)
Об'єм:     100%   → <25%       (4× менше для вивезення)
Патогени:  є      → немає       ✓
Запах:     є      → немає       ✓
Мікропластик: є  → мінімально  ✓ (AGH NSC гранти 2025)
```

4. **"Dlaczego to nie eksperyment"** — секція довіри:
```
10+ lat badań | AGH Kraków | MPWiK Lubin (2025) | Oficjalnie w polskim prawie od 14.01.2025
```

5. **FAQ для інженера:**
```
Q: Jak długo trwa proces HTC?
A: 2 godziny w temperaturze 200–210°C przy ciśnieniu ~2,5 MPa.

Q: Co z metalami ciężkimi?
A: Koncentracja wzrasta o 20–40% (efekt zagęszczenia), ale absolutna ilość się nie zmienia.
   To standard przy każdym procesie odwadniania.

Q: Czy instalacja jest energetycznie samodzielna?
A: HTC-S i HTC-D: tak dla ciepła. TH+HTC: tak dla ciepła I elektryczności.

Q: Jakie są wymagania co do istniejącej infrastruktury?
A: HTC-S nie wymaga AD. HTC-D integruje się z istniejącym AD. TH+HTC wymaga miejsca pod budowę.
```

6. **CTA:** "Pobierz whitepaper techniczny" + "Zamów bezpłatną ocenę techniczną"

---

### `/teo` — Analiza TEO

**Мета:** зробити TEO обов'язковим першим кроком, а не опцією.

#### Hero
```
[H1] Bez analizy TEO nie ma grantu.
     Bez grantu projekt jest 3–4× droższy.

[Sub] TEO to nie koszt — to inwestycja, która zwraca się przed pierwszą łopatą.
```

#### Що таке TEO (5 кроків)
```
1. Analiza składu osadu Twojej oczyszczalni (2 tyg.)
2. Dobór optymalnej konfiguracji HTC (S/D/TH+HTC)
3. Obliczenie opłacalności i okresu zwrotu
4. Mapa ścieżki dotacyjnej (FEnIKS / KPO / NFOŚiGW)
5. Gotowy dokument do rady gminy i do wniosku grantowego
```

#### FAQ для двох аудиторій
```
[ДЛЯ WÓJT]
Q: Co dostaje rada gminy z TEO?
A: Gotowy dokument z rekomendacją, kosztorysem i planem dofinansowania.
   Wystarczy go wysłać przed głosowaniem.

Q: Czy bez TEO można aplikować o FEnIKS.01.03?
A: Nie. TEO lub równoważne studium wykonalności jest wymogiem formalnym wniosku.

[ДЛЯ ІНЖЕНЕРА]
Q: Ile kosztuje TEO?
A: PLN 150–210K zależnie od zakresu i wielkości obiektu.

Q: Co muszę dostarczyć?
A: Raport z laboratorium osadu (robimy razem), schematy technologiczne oczyszczalni,
   dane o obecnych kosztach utylizacji.

Q: Jak długo trwa?
A: 6 tygodni od podpisania umowy.
```

#### CTA
```
[Umów bezpłatną rozmowę wstępną]
W 30 minut powiemy Ci: czy Twój obiekt kwalifikuje się do HTC,
jaka konfiguracja jest optymalna, i czy dotacja jest realistyczna.
```

---

### `/dotacje` — Гранти і фінансування (НОВА СТОРІНКА — критична)

**Мета:** перетворити "за дорого" на "безглуздо не брати".

#### Hero
```
[H1] Instalacja HTC kosztuje PLN 15–30M.
     Twoja gmina zapłaci PLN 2–4,5M.
     Reszta: granty UE.

[Sub] FEnIKS, KPO, NFOŚiGW — łącznie PLN 100B+ dostępnych do 2030.
     Ale to system kolejkowy. Kto złoży wcześniej — ten dostaje.
```

#### Порівняльна таблиця фондів
| Фонд | Покриття CAPEX | Дедлайн | Примітка |
|---|---|---|---|
| FEnIKS 01.03 | до 85% | 2026–2027 (peak) | Вимагає TEO |
| KPO | до 75% | 2025–2026 | Швидший цикл |
| NFOŚiGW LIFE | до 90% | Постійно | Для інноваційних проектів |
| NEFCO (Nordic) | до 100% | Для Східного ЄС | |

#### Конкретний приклад
```
Projekt: instalacja HTC dla gminy 20 000 RLM
Całkowity CAPEX:       PLN 20 000 000
Grant FEnIKS (85%):   PLN 17 000 000
Wkład własny gminy:    PLN  3 000 000

Roczna oszczędność na utylizacji: PLN 542 000
Zwrot wkładu własnego: 5,5 roku
```

#### Чому зараз, не потім
```
Granty to nie sklep online — nie czekają.
2026–2027: szczyt dostępności środków (budżety UE na finiszu)
2028: konkurencja wchodzi na rynek, kolejki rosną
2029+: środki wyczerpane, projekt płatny w 100%

Przygotowanie wniosku: 6–12 miesięcy.
Decyzja o dotacji: 3–6 miesięcy.
Budowa: 12–18 miesięcy.
Łącznie: minimum 2–3 lata od decyzji do działania.
```

#### FAQ
```
Q: 90% gmin nie wie, że może dostać dotację na HTC — skąd o tym mówisz?
A: Bo pomagamy gminom w aplikowaniu. To część naszej usługi — razem z TEO
   przygotowujemy kompletny wniosek grantowy. Bez dodatkowych kosztów.

Q: Czy dotację można stracić?
A: Tak — jeśli projekt nie spełnia wymogów technicznych lub formalnych.
   TEO od BTC gwarantuje zgodność z wymogami FEnIKS.
```

#### CTA
```
[Sprawdź dostępne dotacje dla Twojej gminy — bezpłatnie, w 2 tygodnie]
```

---

### `/hub-spoke` — Кластерна модель (НОВА — для малих гмін)

**Мета:** відкрити ринок малих гмін (<15K RLM), які інакше не конвертують.

#### Hero
```
[H1] Sami nie możecie sobie pozwolić na HTC.
     Ale razem z sąsiadami — już tak.

[Sub] Model Hub & Spoke: jedna instalacja obsługuje 4-5 pobliskich gmin.
     Każda gmina płaci proporcjonalnie. Każda oszczędza.
```

#### Як це працює
```
[HUB] Gmina A (30 000 RLM) — buduje instalację HTC
      ↑ finansuje 85% z grantu UE; wkład własny: PLN 2,25M
      
[SPOKE] Gmina B (5 000 RLM) — wozi osad do hubu
        Płaci: PLN 200/t gate fee + transport (20–50 km)
        Oszczędność vs. obecne koszty: 36–59%

[SPOKE] Gmina C, D, E — tak samo
```

#### Економіка для spoke
```
Obecny koszt utylizacji:    PLN 550/t
Nowy koszt (gate fee):      PLN 200/t  
Transport (30 km):           PLN ~90/t
Łącznie nowy koszt:         PLN 290/t
────────────────────────────────────
Oszczędność: PLN 260/t = 47%
Za 10 lat dla gminy 5K RLM: PLN 366 750 = EUR 91 688
```

#### FAQ
```
Q: Kto inicjuje klaster?
A: Zwykle gmina z największą oczyszczalnią (hub). BTC pomaga w negocjacjach
   między gminami i przygotowaniu umowy konsorcjum.

Q: Jak daleko może być spoke od hubu?
A: Maksymalnie 50 km. Przy 100 km oszczędności maleją do ~9% — nieopłacalne.

Q: Czy spoke musi cokolwiek budować?
A: Nie. Tylko wozi osad. Żadnych inwestycji, żadnego CAPEX.

Q: Ile gmin potrzeba do hubu?
A: Minimum 2-3. Optymalnie 4-5 gmin w promieniu 30-50 km.
```

#### CTA
```
[Sprawdź czy Twoja gmina może dołączyć do klastra Hub & Spoke]
Bezpłatna mapa sąsiednich gmin i wstępna ocena opłacalności — 2 tygodnie.
```

---

### `/case-lubin` — Кейс MPWiK Lubin

**Мета:** соціальний доказ + ідентифікація читача з ситуацією.

#### Емоційний вхід (зараз відсутній — КРИТИЧНО додати)
```
MPWiK Lubin wydawał PLN 550/tonę na zagospodarowanie osadu.
Przy 3 800 tonach rocznie — ponad PLN 2 mln co roku.
Bez żadnego produktu na wyjściu. Zarząd wiedział, że coś musi się zmienić.
Pytanie było: co dokładnie? I czy jest na to finansowanie?
```

#### Факти проекту (з Lubin pptx)
- Об'єм осаду: 3 800 т/рік
- Попередня вартість: PLN 2,09M/рік
- Технологія: TH+HTC (повна петля)
- Результат: вартість знижена на X%, енергетична самодостатність

#### Місток до малих об'єктів
```
MPWiK Lubin ma 100 000 RLM. Wasza oczyszczalnia ma 18 000?
Logika jest ta sama — tylko skala inna.
Dla obiektów 10 000–50 000 RLM stosujemy HTC-S lub HTC-D.
Kalkulator pokaże Wam konkretne liczby dla Waszego przypadku.
[→ Kalkulator ROI]
```

#### FAQ
```
Q: Jak długo trwał projekt od TEO do odbioru?
A: [вставити дані з pptx]

Q: Czy MPWiK Lubin jest zadowolony?
A: Koncepcja i prawa autorskie zostały odkupione przez klienta (10.2025) — to najlepsza recenzja.

Q: Jakie były główne wyzwania?
A: [вставити дані з pptx]
```

---

### `/kalkulator-roi` — Калькулятор ROI

**Мета:** дати відвідувачу персоналізовані цифри → максимальна мотивація до дії.

#### Wizard (3 кроки — поточна логіка залишається, перевірити vs Excel-модель)
```
Крок 1: Розмір об'єкту (RLM/PE)
Крок 2: Поточний метод утилізації + вартість (PLN/t)
Крок 3: Чи є AD? Чи є партнерські гміни поруч?

→ Результат: 
  - Рекомендована конфігурація HTC
  - Орієнтовна вартість проекту
  - Очікуваний грант (%)
  - Ваш внесок (PLN)
  - Щорічна економія (PLN/рік)
  - Payback period (роки)
  - CTA: "Chcę potwierdzić te liczby z ekspertem BTC"
```

---

### `/uwwtd` — Директива UWWTD

**Мета:** SEO-трафік з пошуку, перетворити читача на ліда.

**Готово:** `02-market-hook/uwwtd-pillar-pl.md` — публікувати майже без змін.  
Додати: CTA на `/kalkulator-roi` після кожної таблиці дедлайнів.

---

## 3. Глобальні конверсійні елементи

### CTA-ієрархія (три рівні)

```
[МІКРО-CTA] — низький поріг, на кожній секції
"Sprawdź w kalkulatorze"  |  "Pobierz whitepaper"  |  "Czytaj case study"

[ОСНОВНИЙ CTA] — на кожній сторінці, середина і кінець
"Bezpłatna ocena wstępna — 2 tygodnie, bez zobowiązań"

[EXIT CTA] — popup при виході або після 90 сек на сторінці
"Zanim wyjdziesz: czy wiesz ile Twoja gmina przepłaca za osad co roku?
 → Kalkulator (30 sekund)"
```

### Sticky header CTA
```
[BTC Consulting]  Technologia  TEO  Dotacje  Kalkulator  |  [Bezpłatna ocena →]
```

### Форма контакту (мінімальна — на всіх сторінках)
```
Imię i nazwisko*
Nazwa gminy / oczyszczalni*
Adres e-mail*
Telefon
[  ] Interesuje mnie bezpłatna ocena wstępna
[  ] Mam pytanie techniczne
[  ] Szukam informacji o dotacjach
[Wyślij — odpowiedź w 48h]

Pod formularzem: "Nie sprzedajemy danych. Odpowiadamy osobiście."
```

### Social proof bar (під hero на кожній сторінці)
```
10+ lat badań z AGH │ MPWiK Lubin ✓ │ HTC w polskim prawie od 2025 │ 3 własne technologie
```

---

## 4. SEO-стратегія

### Кластер статей навколо головного keyword

**Головна:** `zagospodarowanie osadów ściekowych` (пілар — `/uwwtd`)

**Супутні статті (блог):**
- "Ile kosztuje utylizacja osadu w Polsce 2026?" → `/kalkulator-roi`
- "Dotacje NFOŚiGW na oczyszczalnie — przewodnik 2026" → `/dotacje`
- "HTC vs. co-combustion — porównanie technologii" → `/technologia`
- "Hub & Spoke — model dla małych gmin" → `/hub-spoke`
- "PFAS w osadach — co zmienia dyrektywa UWWTD" → блог (з pfas-osad-uk.md)

### Технічне SEO (з phase2_supremseo_plan.md)
- Slug структура: `/zagospodarowanie-osadow-sciekowych`, `/dotacje-na-htc`, `/hub-spoke-gminy`
- Мультимовність: `/pl/`, `/en/`, `/ua/`
- H2 питальні де природно (для Perplexity/ChatGPT цитування)
- Schema: FAQPage на кожній сторінці з FAQ

---

## 5. Метрики конверсії (що вимірювати)

| Метрика | Ціль | Де |
|---|---|---|
| Час на сайті | >3 хв | GA4 |
| Глибина скролу | >70% | Hotjar |
| CTR на "Bezpłatna ocena" | >3% | GA4 |
| Заповнення форми | >2% від сесій | GA4 |
| Кальк → форма конверсія | >15% | GA4 |
| Повернення протягом 7 днів | >20% | GA4 |

---

## 6. Порядок реалізації

### Sprint 1 (тиждень 1–2) — Виправити існуючі сторінки
- [ ] `index.html` — додати FAQ, блок "два читачі", підсилити CTA
- [ ] `technology.html` — порівняльна таблиця конфігурацій, секція довіри
- [ ] `teo.html` — FAQ для 2 аудиторій

### Sprint 2 (тиждень 3–4) — Нові критичні сторінки
- [ ] `/dotacje` — НОВА, найвищий пріоритет
- [ ] `/hub-spoke` — НОВА, для малих гмін
- [ ] `case-lubin.html` — емоційний вхід, місток, FAQ

### Sprint 3 (тиждень 5–6) — SEO і оптимізація
- [ ] `/uwwtd` — опублікувати uwwtd-pillar-pl.md
- [ ] Калькулятор — перевірити формули vs Excel-модель
- [ ] Schema markup на всіх FAQ
- [ ] Sticky CTA в header

### Sprint 4 (тиждень 7–8) — Трекінг і ітерація
- [ ] GA4 + Hotjar setup
- [ ] A/B тест Hero CTA (версія А: "Bezpłatna ocena" / версія Б: "Sprawdź kalkulator")
- [ ] Exit-intent popup

---

## 7. Файли для кожної задачі

| Завдання | Прочитати перед початком |
|---|---|
| Будь-який текст | `10-marketing/communication_guide.md` (tone of voice) |
| Будь-який код | `09-website-code/DESIGN_SYSTEM.md` + `STYLE-GUIDE.md` |
| Hero та CTA | `01-strategy/messaging-strategy.md` |
| FAQ | `01-strategy/content-strategy-brief.md` |
| `/dotacje` | `04-economics/business-model.md` + `02-market-hook/market-opportunity.md` |
| `/hub-spoke` | `04-economics/sludge-economics.md` |
| `/technologia` | `03-technology/htc-technology.md` |
| `case-lubin` | `13-presentations/Presentation of Stage II...pptx` |
| Калькулятор | `12-calculator/BTC_Calculator_Model_PL.xlsx` |
| `/uwwtd` | `02-market-hook/uwwtd-pillar-pl.md` |
| Нові лендинги B/C | `05-clients/GTM_TARGETS_SUMMARY.md` |

---

*Документ: CONVERSION_PLAN.md | v1 | 2026-07-01*  
*Наступний крок: Sprint 1 — index.html*

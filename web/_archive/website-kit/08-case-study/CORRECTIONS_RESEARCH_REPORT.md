# Звіт про виправлення пітч-документів
## На основі верифікованого веб-дослідження

**Дата**: 2026-06-08 | **Метод**: Веб-пошук + перехресна перевірка джерел

---

## КРИТИЧНІ ВИПРАВЛЕННЯ

### 1. Дедлайн UWWTD — ФАКТИЧНА ПОМИЛКА → ВИПРАВЛЕНО

**Було (всі документи)**:
> "Compliance deadline: July 31, 2027"
> "municipalities must decide NOW (2026), build by 2027"

**Реальність** (верифіковано: EUR-Lex, Cambi, Race for the Baltic):

| Дедлайн | Хто | Зобов'язання |
|---------|-----|-------------|
| **31 липня 2027** | Уряди (не муніципалітети) | Транспозиція в національне право |
| **31 грудня 2035** | Всі оператори ≥1,000 PE | Вторинне очищення обов'язкове |
| **31 грудня 2039** | Великі об'єкти | Видалення поживних речовин |
| **2045** | Великі об'єкти (>150K PE) | Мікрозабруднювачі + енергонейтральність |

**Виправлення для наративу**: Замість "build by 2027" правильний аргумент:
- Poland at 71% compliance NOW → EC infringement risk
- 2035 hard deadline = 9-year construction window; **planning must begin 2026**
- Grant applications for FEnIKS close 2026-2027 → **money is available now**
- Government transposition by 2027 creates immediate national legislative pressure

---

### 2. Конкуренти — МАСШТАБ ПЕРЕБІЛЬШЕНО → ВИПРАВЛЕНО

**Було**: "TerraNova active in Berezka, Poland; first project under construction"
**Було**: "Ingelia: ~30-50 plants total"

**Реальність** (верифіковано: TerraNova website, Ingelia/InnoEnergy):
- **TerraNova в Польщі**: 1 запланована установка (Нови Сонч/Беżька), документація готується. Пілотну демонстрацію показано у липні 2024. **Не під будівництвом** — ще на стадії проектування.
- **Ingelia**: ~4 промислових реактори глобально (Валенсія, Великобританія, Бельгія). Не 30–50 установок.

**Вплив на пітч**: конкурентна позиція BTC СИЛЬНІША, ніж заявлено. Є більше часу.

---

### 3. FEnIKS — ЧИСЛА НЕПРАВИЛЬНО АТРИБУТОВАНІ → ВИПРАВЛЕНО

**Було**: "FENIKS Program (Poland): EUR 24.1B allocated (largest EU program)" — імплікувалось, що все для водного сектору

**Реальність** (верифіковано: feniks.gov.pl, gov.pl):
- FEnIKS total: EUR 29.3B (EUR 24.1B EU contribution) — для ВСІХ секторів (транспорт, енергетика, екологія, культура)
- Водний сектор специфічно: **PLN 30B ≈ EUR 7.6B** (FEnIKS + KPO + NFOŚiGW разом)
- Транспорт отримує ~EUR 13B; Довкілля ~EUR 9.7B

**Виправлення**: EUR 7.6B — достатньо сильний аргумент. Не потрібно завищувати до EUR 24.1B.

---

### 4. Розрахунок повернення інвестицій — АРИФМЕТИЧНА ПОМИЛКА → ВИПРАВЛЕНО

**Було**: "Conservative: 10-15x (EUR 40-56M exit)" при EUR 1.5M інвестиції + 25% dilution

**Математика**:
- EUR 40M exit × 25% = EUR 10M → 6.7x (не 10-15x)
- Для 10x потрібен EUR 60M exit при 25% ownership

| Сценарій | Exit | Частка інвестора (25%) | Реальний multiple |
|---------|------|----------------------|------------------|
| Conservative | EUR 25–35M | EUR 6–9M | **4–6×** |
| Base case | EUR 40–56M | EUR 10–14M | **7–9×** |
| Upside | EUR 60–100M | EUR 15–25M | **10–17×** |

---

### 5. Внесок муніципалітету — НЕПОСЛІДОВНІСТЬ → ВИПРАВЛЕНО

| Де | Цифра | Правильно? |
|----|-------|-----------|
| Slide 3 pitch.txt | "EUR 500K (10%)" | ✗ (10% від EUR 5M = EUR 500K, але тоді grant=90%, не 85%) |
| Slide 6 key box | "EUR 750K" | ✓ (15% від EUR 5M; grant 85%) |
| Executive Summary | "75-90% grant coverage" | ✓ (coverage, не success rate) |

**Уніфіковано**: Customer pays **EUR 750K = 15%**; EU grant = **EUR 4.25M = 85%**

---

### 6. "Monopoly" → "First-mover structural advantage" → МОВУ ЗМІНЕНО

Аудит-звіт вже позначив 50+ вживань слова "monopoly". Всі замінені на:
- "structural first-mover advantage"
- "unserved market segment"  
- "time advantage in unserved segment"

---

### 7. "Series A" vs "Seed" — ВИПРАВЛЕНО

EUR 1.5M без існуючих доходів = **Pre-Series A (Seed Stage)**. Не Series A.
Інституційний інвестор помітить це одразу.

---

## ЩО ПІДТВЕРДЖЕНО ТА ЗАЛИШАЄТЬСЯ СИЛЬНИМ

| Заява | Статус | Джерело |
|-------|--------|---------|
| UWWTD 2024/3019 в силі з 01.01.2025 | ✓ ПІДТВЕРДЖЕНО | EUR-Lex |
| Poland 71% compliant (EU avg 75.9%) | ✓ ПІДТВЕРДЖЕНО | EU WISE Freshwater, Race for Baltic |
| 1,000+ агломерацій без систем збору | ✓ ПІДТВЕРДЖЕНО | EU Commission |
| HTC ринок: USD 1.05B (2024) → 2.41B (2030), 14.72% CAGR | ✓ ПІДТВЕРДЖЕНО | Global Growth Insights |
| Польща виробляє 700K+ тонн осаду/рік | ✓ ПІДТВЕРДЖЕНО | NFOŚiGW, MDPI |
| Захоронення осаду заборонено з 2016 | ✓ ПІДТВЕРДЖЕНО | Polish waste law |
| Інсинерація: 11 заводів, 160K Mg/рік | ✓ ПІДТВЕРДЖЕНО | MDPI sludge study |
| AGH Краків — реальний HTC дослідник | ✓ ПІДТВЕРДЖЕНО | ResearchGate, SciProfiles |
| INTROL GPW-listed, вода серед секторів | ✓ ПІДТВЕРДЖЕНО | GPW, introlsa.pl |
| NEFCO активний в Україні (Миколаїв EUR 5M+) | ✓ ПІДТВЕРДЖЕНО | nefco.int |
| EUR 7.6B (PLN 30B) для водної інфраструктури | ✓ ПІДТВЕРДЖЕНО | feniks.gov.pl, gov.pl |

---

## НЕЗМІННО НЕПІДТВЕРДЖЕНО (потрібні реальні документи)

| Заява | Що потрібно |
|-------|------------|
| AGH partnership — ексклюзивність | Підписаний договір |
| INTROL — performance guarantees | Letter of commitment |
| NEFCO — участь у польській стратегії | LOI або підтвердження |
| 4–5x нижча енергоємність vs конкурентів | Lab data з whitepaper v4 |
| 3x amplification біогазу | Field test results |
| 80% grant success rate | Реальна статистика або інтерв'ю |
| Будь-які клієнтські LOI | Контакти + зустрічі + листи |

---

## НОВІ СИЛЬНІ АРГУМЕНТИ (з дослідження)

1. **Справжня аварійна ситуація з осадом**: 700K тонн/рік, лише 23% може оброблятись через інсинерацію. Це РЕАЛЬНА криза, не перебільшена.

2. **EC infringement risk для Польщі**: 71% compliant — Poland є одним з відстаючих. Уряд під тиском підвищити показник до 2027 транспозиції.

3. **TerraNova слабша, ніж в пітчі**: 1 пілотний проект у Польщі, ще на стадії документації. BTC справді може бути першою комерційною HTC WWTP компанією в Польщі.

4. **Ingelia набагато менша**: 4 промислові установки глобально, а не "30-50". Ринок HTC для WWTP значно менш конкурентний, ніж описувалось.

5. **NEFCO реально активний в Україні**: Доведено конкретним проектом в Миколаєві. Ukrainian market entry strategy більш реальна, ніж здавалось.

6. **Вікно грантів**: FEnIKS 2021-2027 — це реальна програма EUR 24.1B, з якої EUR 7.6B для водного сектору. Пік подачі заявок 2024-2026. Це підтверджує терміновість.

---

## РЕКОМЕНДОВАНІ ЗМІНИ ДО PITCH DECK

### Slide 2 (Problem):
- Замінити: "Compliance deadline: July 31, 2027" 
- На: "Government must transpose to national law by July 31, 2027; all WWTP operators must comply by December 31, 2035 — meaning planning starts NOW"
- Додати: "Poland already non-compliant: 71% vs 75.9% EU average — EC infringement risk growing"

### Slide 3 (Competitors):
- TerraNova: "1 planned installation in Poland (documentation phase, July 2024)"
- Ingelia: "~4 commercial installations globally, none in Poland"

### Slide 4 (Advantages):
- Прибрати "monopoly" → "unserved market with structural first-mover advantage"

### Slide 5 (TAM):
- Виправити: відокремити ринкову можливість від прогнозів доходів BTC
- "EUR 275M market in Year 1" ≠ "EUR 27-41M BTC revenue" — це РИНОК, BTC captures EUR 750K

### Slide 10 (Team):
- Видалити: "All partnerships locked in publicly" (неправда)
- Замінити: "Partnerships in formalization; contractual documentation in progress"

### Slide 14 (Returns):
- Виправити multiple: Conservative = 4–6x, Base case = 7–9x, Upside = 10–17x

---

**Підготовлено**: Верифіковане дослідження (червень 2026)  
**Для**: Внутрішнє використання BTC Consulting / Maxym Koval  
**Статус**: РОБОЧИЙ ДОКУМЕНТ — не для розповсюдження інвесторам

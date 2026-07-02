# IMAGES NEEDED — BTC Consulting v3 site
**Дата:** 2026-07-01 | Статус: ☐ = потрібно знайти / ☑ = готово

Усі зображення кладуться в `web/v3/img/` за категоріями нижче.
Агент будує з placeholder-ами; після того як зображення додані — замінити placeholder CSS/HTML реальними шляхами.

---

## БЛОКУЮЧІ (без них сайт не виглядає завершеним)

| # | Слот | Шлях | Статус | Де взяти |
|---|------|------|--------|----------|
| 1 | **BTC logo** | `img/logo/btc-logo.svg` | ☐ | Векторний логотип BTC Consulting — надати дизайнеру або попросити в замовника |
| 2 | **Hero WWTP aerial** | `img/stock/wwtp-aerial.jpg` | ☐ | Drone/aerial фото очисної станції. **Варіанти:** Adobe Stock "aerial wastewater treatment plant" / Midjourney: "aerial drone shot wastewater treatment plant morning industrial fog --ar 16:9 --style raw" |

---

## КРИТИЧНІ (потрібні до першого реального показу клієнту)

| # | Слот | Шлях | Сторінка / блок | Де взяти |
|---|------|------|----------------|----------|
| 3 | Lubin WWTP facility | `img/case/lubin-wwtp.jpg` | case-lubin / hero | **Запросити у MPWiK Lubin** — фото їхньої станції (зовнішній вигляд). Альтернатива: Adobe Stock "wastewater treatment plant Poland exterior" |
| 4 | Lubin client portrait | `img/case/lubin-client.jpg` | case-lubin / blockquote | Фото представника MPWiK Lubin (людина з цитатою). Якщо немає — аватар з ініціалами |
| 5 | AGH Kraków logo | `img/partner/agh-krakow.svg` | technologia / partnership | Завантажити з **agh.edu.pl** (прес-матеріали / brand guidelines) |

---

## ВАЖЛИВІ (потрібні до публікації)

| # | Слот | Шлях | Сторінка / блок | Де взяти |
|---|------|------|----------------|----------|
| 6 | HTC Reactor photo | `img/stock/htc-reactor.jpg` | technologia / editorial split | **Власні фото BTC** (реактор/обладнання) — пріоритет. Fallback: Adobe Stock "industrial hydrothermal reactor pressure vessel" |
| 7 | EU Funds visual | `img/stock/eu-funds.jpg` | dotacje / hero | Adobe Stock "European Parliament building flags Brussels" або "EU cohesion fund documents" |
| 8 | Consultants meeting | `img/stock/consultants.jpg` | teo / editorial split | Adobe Stock "engineers reviewing technical documents meeting room industrial" |
| 9 | MPWiK Lubin logo | `img/partner/mpwik-lubin.svg` | case-lubin / client section | **Запросити у клієнта** (MPWiK Lubin) |

---

## ДОДАТКОВІ (можна додати пізніше)

| # | Слот | Шлях | Сторінка | Де взяти |
|---|------|------|---------|----------|
| 10 | BTC Team photo | `img/team/btc-team.jpg` | misja / team block | Командна фотосесія BTC Consulting. До того — текстовий placeholder з іменами |
| 11 | AGH Lab photo | `img/partner/agh-lab.jpg` | technologia / partnership | Опціонально — фото лабораторії AGH; запросити у AGH |

---

## SVG-активи (будує агент — тобі не потрібно шукати)

| Актив | Файл | Що це |
|-------|------|-------|
| HTC Process diagram | `img/svg/htc-process.svg` | Схема процесу: Осад → Реактор → Hydrochar + Вода |
| Hub-Spoke map | `img/svg/hub-spoke-map.svg` | Стилізована карта Польщі з вузлами Hub&Spoke |

---

## Пріоритет дій

```
1. [ ] Надати btc-logo.svg (блокуючий)
2. [ ] Вибрати фото wwtp-aerial (header сайту — перше враження)
3. [ ] Запросити у MPWiK Lubin: фото станції + фото контактної особи + їхній логотип
4. [ ] Завантажити AGH Kraków логотип з agh.edu.pl
5. [ ] Знайти/згенерувати: htc-reactor, eu-funds, consultants (Adobe Stock або AI)
6. [ ] Пізніше: командне фото BTC, фото лабораторії AGH
```

---

*Файл оновлюється агентом після кожної фази збірки. Кожен знайдений файл — замінити ☐ на ☑.*

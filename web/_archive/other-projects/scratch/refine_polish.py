import json

with open("translations/pl.json", "r", encoding="utf-8") as f:
    pl = json.load(f)

# Refined Polish premium business/technical translations
refinements = {
    "home.hero.h1": "Kondensujemy wszystkie <span class=\"h1-problem\">ogromne&nbsp;problemy</span> z osadami w <span class=\"h1-solution\">kompaktowy i bezpieczny hydrowęgiel.</span>",
    "home.problem.card2.p": "W Polsce działa tylko 11 spalarni osadów ściekowych. Kolejki, uzależnienie od jednego odbiorcy, ryzyko przestoju — to nie jest hipotetyczny scenariusz. To codzienność dziesiątek gmin.",
    "home.problem.card1.p": "94% oczyszczalni w Polsce nie posiada komór fermentacyjnych. Susząc osad przy użyciu zakupionej energii — gazu lub prądu — zużywają 1200–1300 Wh na każdy kilogram. Miasta do 100 000 mieszkańców pokrywają te koszty bezpośrednio z budżetu.",
    "home.solution.tbl.r2.l": "Zależność od zewnętrznych operatorów",
    "tech.htc.h2": "Proces trwający w naturze miliony lat skracamy do 2 godzin.",
    "home.solution.tbl.r1.l": "Minimalny roczny strumień osadów",
    "home.hero.micro": "Gmina od 10 tys. mieszkańców lub przedsiębiorstwo rolne? Sprawdź, czy Twój obiekt może stać się sercem regionalnego hubu →",
    "home.grants.item2.p": "Partnerstwo z uczelnią stanowi oficjalny kanał składania wniosków o granty badawcze i infrastrukturalne UE, niedostępne bezpośrednio dla podmiotów komercyjnych.",
    "tech.hero.desc": "Hydrotermalna karbonizacja to sprawdzona technologia. Odtwarzamy naturalny proces zwęglania w zamkniętym reaktorze — bez emisji, bez zapachu i bez uwalniania PFAS. Jeden proces, wiele konfiguracji — dopasowanych do każdego obiektu."
}

# Apply refinements
for k, v in refinements.items():
    if k in pl:
        print(f"Refining [{k}]:\n  Old: {pl[k]}\n  New: {v}\n")
        pl[k] = v

with open("translations/pl.json", "w", encoding="utf-8") as f:
    json.dump(pl, f, ensure_ascii=False, indent=2)

print("Polish translations refined successfully.")

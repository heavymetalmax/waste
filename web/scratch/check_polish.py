import json

with open("translations/pl.json", "r", encoding="utf-8") as f:
    pl = json.load(f)

# Let's inspect some of the key translations
business_terms = [
    "chat.welcome",
    "contact.p",
    "footer.brand.p",
    "home.hero.h1",
    "home.hero.desc",
    "home.problem.h2",
    "home.problem.card1.h3",
    "home.problem.card1.p",
    "home.problem.card2.p",
    "home.problem.card3.p",
    "home.solution.desc",
    "home.solution.tbl.r1.l",
    "home.solution.tbl.r2.l",
    "home.solution.tbl.r3.l",
    "home.solution.tbl.r4.l",
    "home.solution.tbl.r5.l",
    "home.solution.tbl.r6.l",
    "home.grants.h2",
    "home.grants.item1.p",
    "tech.hero.h1",
    "tech.hero.desc",
    "tech.htc.h2",
    "tech.htc.desc",
    "tech.contrast.h2",
    "tech.contrast.callout.h3",
    "tech.contrast.callout.p"
]

print("--- Terminology check in pl.json ---")
for key in business_terms:
    if key in pl:
        print(f"[{key}]:")
        print(pl[key])
        print()

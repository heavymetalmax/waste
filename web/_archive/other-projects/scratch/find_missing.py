import json

with open("translations/ua.json", "r", encoding="utf-8") as f:
    ua = json.load(f)

with open("translations/eu.json", "r", encoding="utf-8") as f:
    eu = json.load(f)

missing = []
for k, v in ua.items():
    if k not in eu or eu[k] == "":
        missing.append((k, v))

print(f"Total missing: {len(missing)}")
for k, v in missing[:20]:
    print(f"{k}: {v}")

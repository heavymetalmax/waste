import json

keys_to_add = {
    "ua": {
        "contact.popover.title": "Швидкий зв'язок",
        "contact.popover.save": "Зберегти в контакти",
        "contact.popover.form": "Зворотний зв'язок",
        "contact.popover.or": "або"
    },
    "eu": {
        "contact.popover.title": "Quick Contact",
        "contact.popover.save": "Save Contact",
        "contact.popover.form": "Contact Form",
        "contact.popover.or": "or"
    },
    "pl": {
        "contact.popover.title": "Szybki kontakt",
        "contact.popover.save": "Zapisz kontakt",
        "contact.popover.form": "Formularz kontaktowy",
        "contact.popover.or": "lub"
    }
}

for lang, trans in keys_to_add.items():
    filepath = f"translations/{lang}.json"
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Update dict
    for k, v in trans.items():
        data[k] = v
        
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated {lang} popover translations.")

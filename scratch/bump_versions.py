import pathlib

ROOT = pathlib.Path(__file__).parent.parent
BIOTC = ROOT / "biotc"

for filepath in BIOTC.glob("*.html"):
    content = filepath.read_text(encoding="utf-8")
    updated = False
    
    if "styles.min.css?v=22" in content:
        content = content.replace("styles.min.css?v=22", "styles.min.css?v=23")
        updated = True
        
    if "app.min.js?v=4" in content:
        content = content.replace("app.min.js?v=4", "app.min.js?v=5")
        updated = True
        
    if updated:
        filepath.write_text(content, encoding="utf-8")
        print(f"Bumped version in {filepath.name}")

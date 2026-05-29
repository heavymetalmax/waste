#!/usr/bin/env python3
"""
BioTC site builder
Usage:  python3 build.py
        python3 build.py --check     # report missing translations only
Output: ua/, pl/, eu/  ← ready for GitHub Pages (deploy from main branch)
"""

import json, re, sys, pathlib, shutil

ROOT  = pathlib.Path(__file__).parent
TDIR  = ROOT / "translations"
TMPL  = ROOT / "biotc"             # source templates
PAGES = ["index.html", "technology.html", "simulator.html", "chat.html"]
LANGS = ["ua", "pl", "eu"]

CHECK_ONLY = "--check" in sys.argv

# ── load translations ────────────────────────────────────────────────────────
def load(lang):
    with open(TDIR / f"{lang}.json", encoding="utf-8") as f:
        return json.load(f)

ua_base = load("ua")

ROUTING_KEYS = {
    "lang.code", "img.team",
    "lang.ua.url", "lang.pl.url", "lang.eu.url",
    "lang.ua.class", "lang.pl.class", "lang.eu.class",
    "lang.ua.tech.url", "lang.pl.tech.url", "lang.eu.tech.url",
    "lang.ua.tech.class", "lang.pl.tech.class", "lang.eu.tech.class",
    "lang.ua.sim.url", "lang.pl.sim.url", "lang.eu.sim.url",
    "lang.ua.sim.class", "lang.pl.sim.class", "lang.eu.sim.class",
}

def merge(lang):
    """Return dict: lang values, falling back to ua only for null/missing content keys."""
    t = load(lang) if lang != "ua" else {}
    out = dict(ua_base)           # start from ua
    for k, v in t.items():
        if k in ROUTING_KEYS:
            out[k] = v            # always use lang-specific value (even "")
        elif v:                   # content: only override if non-empty
            out[k] = v
    return out

# ── substitute {{key}} in text ───────────────────────────────────────────────
KEY_RE = re.compile(r"\{\{([\w.]+)\}\}")

def substitute(text, trans, source_path):
    missing = []
    def replace(m):
        key = m.group(1)
        if key not in trans:
            missing.append(key)
            return f"[[MISSING:{key}]]"
        return trans[key]
    result = KEY_RE.sub(replace, text)
    if missing:
        print(f"  ⚠  {source_path.name}: missing keys: {missing}")
    return result

# ── copy static assets once ──────────────────────────────────────────────────
def ensure_assets():
    """Ensure styles.css, app.js, img/team/ exist at root (already there)."""
    pass   # assets live at /Waste/ root, referenced via ../

# ── main build ───────────────────────────────────────────────────────────────
def build():
    ensure_assets()
    total_missing = 0

    for lang in LANGS:
        trans = merge(lang)
        out_dir = ROOT / lang
        out_dir.mkdir(exist_ok=True)

        for page in PAGES:
            src = TMPL / page
            if not src.exists():
                print(f"  skip {page} (not found in biotc/)")
                continue
            text = src.read_text(encoding="utf-8")
            result = substitute(text, trans, src)
            total_missing += result.count("[[MISSING:")
            if not CHECK_ONLY:
                (out_dir / page).write_text(result, encoding="utf-8")
                print(f"  ✓  {lang}/{page}")

    if total_missing:
        print(f"\n  {total_missing} missing key(s) across all files.")
    else:
        print("\n  All keys resolved. ✓")

if __name__ == "__main__":
    print(f"{'Checking' if CHECK_ONLY else 'Building'} BioTC site…\n")
    build()

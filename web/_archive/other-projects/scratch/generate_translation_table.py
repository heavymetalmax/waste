import json
import os

# Load JSONs
with open("translations/ua.json", "r", encoding="utf-8") as f:
    ua = json.load(f)
with open("translations/eu.json", "r", encoding="utf-8") as f:
    eu = json.load(f)
with open("translations/pl.json", "r", encoding="utf-8") as f:
    pl = json.load(f)

# Artifact file path
out_path = "/Users/max/.gemini/antigravity/brain/9a750c65-81cb-4f71-aa28-5132950cebb0/translation_table.md"

# Group keys logically
groups = {}
for k in ua.keys():
    if k.startswith("_comment"):
        continue
    # Determine group
    if k.startswith("home.hero"):
        g = "Home - Hero Section"
    elif k.startswith("home.problem"):
        g = "Home - Problem Section"
    elif k.startswith("home.solution"):
        g = "Home - Solution Section"
    elif k.startswith("home.calc"):
        g = "Home - Calculations CTA"
    elif k.startswith("home.trust"):
        g = "Home - Trust Section"
    elif k.startswith("home.team"):
        g = "Home - Team Section"
    elif k.startswith("home.grants"):
        g = "Home - Grants Section"
    elif k.startswith("tech.hero"):
        g = "Technology - Hero Section"
    elif k.startswith("tech.htc"):
        g = "Technology - HTC Concept"
    elif k.startswith("tech.configs"):
        g = "Technology - Configurations"
    elif k.startswith("tech.hydrochar"):
        g = "Technology - Hydrochar Specs"
    elif k.startswith("tech.contrast"):
        g = "Technology - Comparison Table"
    elif k.startswith("tech.models"):
        g = "Technology - Models Line"
    elif k.startswith("sim"):
        g = "Simulator Page"
    elif k.startswith("htc"):
        g = "Simulator - Chemical Passport"
    elif k.startswith("chat"):
        g = "AI Consultant Chat"
    elif k.startswith("contact") or k.startswith("form"):
        g = "Contact & Lead Form"
    elif k.startswith("header") or k.startswith("footer"):
        g = "Header, Navigation & Footer"
    else:
        g = "General / UI Elements"
    
    if g not in groups:
        groups[g] = []
    groups[g].append(k)

# Generate Markdown
with open(out_path, "w", encoding="utf-8") as f:
    f.write("# BioTC Website Translation Review Table\n\n")
    f.write("Use this table to review, refine, and plan overrides for all website copy. You can write your custom translations in the **Proposed Change** column.\n\n")
    
    # TOC
    f.write("## Table of Contents\n")
    for gname in sorted(groups.keys()):
        anchor = gname.lower().replace(" ", "-").replace("&", "").replace("-", "").replace("---", "-").replace("(", "").replace(")", "")
        anchor = "".join([c for c in anchor if c.isalnum() or c == "-" or c == "_"])
        f.write(f"- [{gname}](#{anchor})\n")
    f.write("\n---\n\n")
    
    # Write groups
    for gname in sorted(groups.keys()):
        f.write(f"## {gname}\n\n")
        f.write("| Key | Ukrainian (UA) | English (EN) | Polish (PL) | Proposed Change (Write Here) |\n")
        f.write("|---|---|---|---|---|\n")
        
        for k in sorted(groups[gname]):
            val_ua = ua.get(k, "").replace("\n", "<br>").replace("|", "\\|")
            val_en = eu.get(k, "").replace("\n", "<br>").replace("|", "\\|")
            val_pl = pl.get(k, "").replace("\n", "<br>").replace("|", "\\|")
            f.write(f"| `{k}` | {val_ua} | {val_en} | {val_pl} | |\n")
        f.write("\n---\n\n")

print("Translation table generated successfully.")

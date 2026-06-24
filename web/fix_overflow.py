with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add min-width: 0 to all grid items so they don't blow out CSS Grid
grid_fix = """
.grid-2 > div, .grid-3 > div, .grid-4 > div {
  min-width: 0;
  max-width: 100%;
}
"""

css += '\n' + grid_fix

# Also make sure col-card itself doesn't force width
css = css.replace('.col-card {\n  padding: var(--space-md);', '.col-card {\n  padding: var(--space-md);\n  max-width: 100%;\n  box-sizing: border-box;')

with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)


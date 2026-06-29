with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the specific #process .col-card block to include height: auto !important
old_block = """#process .col-card {
  overflow: hidden;
  max-width: 100%;
  box-sizing: border-box;
}"""

new_block = """#process .col-card {
  overflow: hidden;
  max-width: 100%;
  box-sizing: border-box;
  height: auto !important; /* Fix the vertical bleed bug */
}"""

if old_block in css:
    css = css.replace(old_block, new_block)
else:
    # If not found, just append it
    css += "\n" + new_block

with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)


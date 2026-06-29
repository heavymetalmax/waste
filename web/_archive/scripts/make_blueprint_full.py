import re

with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_blueprint_css = """
.hero-blueprint {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0.15;
  z-index: 0;
  pointer-events: none;
  overflow: hidden;
}
"""

# Replace the old .hero-blueprint block
css = re.sub(r'\.hero-blueprint\s*\{[^}]*\}', new_blueprint_css.strip(), css)

with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('ua/index-v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add preserveAspectRatio attribute to the SVG so it covers the whole screen nicely
html = html.replace('<svg viewBox="0 0 800 800" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: 100%;">', 
                    '<svg viewBox="0 0 800 800" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: 100%;" preserveAspectRatio="xMidYMid slice">')

with open('ua/index-v2.html', 'w', encoding='utf-8') as f:
    f.write(html)

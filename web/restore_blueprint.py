with open('add_svg_blueprint.py', 'r', encoding='utf-8') as f:
    script = f.read()

import re
svg_match = re.search(r'<svg viewBox.*?/svg>', script, flags=re.DOTALL)
if svg_match:
    svg_content = svg_match.group(0)
else:
    print("SVG not found in script!")
    exit(1)

with open('Ua/index-v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

blueprint_div = f"""
    <div class="trust-blueprint">
      {svg_content}
    </div>
"""

# Insert into #trust
html = html.replace('<section id="trust">', '<section id="trust" style="position: relative; overflow: hidden;">\n' + blueprint_div)

with open('Ua/index-v2.html', 'w', encoding='utf-8') as f:
    f.write(html)

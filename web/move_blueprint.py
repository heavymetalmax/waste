import re

with open('ua/index-v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the blueprint div
blueprint_match = re.search(r'<div class="problem-blueprint">.*?</svg>\s*</div>', html, flags=re.DOTALL)
if blueprint_match:
    blueprint_str = blueprint_match.group(0)
    
    # Remove from problem
    html = html.replace(blueprint_str, '')
    html = html.replace('<section id="problem" style="position: relative; overflow: hidden;">', '<section id="problem">')
    
    # Rename class
    blueprint_str = blueprint_str.replace('problem-blueprint', 'trust-blueprint')
    
    # Move to trust
    html = html.replace('<section id="trust">', '<section id="trust" style="position: relative; overflow: hidden;">\n    ' + blueprint_str)

with open('ua/index-v2.html', 'w', encoding='utf-8') as f:
    f.write(html)


with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update CSS class name
css = css.replace('.problem-blueprint', '.trust-blueprint')

# Make sure it stands out well against the white background of the trust section
# It currently has opacity: 0.05. We can leave it or bump it slightly. Let's make it 0.08.
css = css.replace('.trust-blueprint {\n  position: absolute;\n  top: 0; left: 0; width: 100%; height: 100%;\n  opacity: 0.05;', '.trust-blueprint {\n  position: absolute;\n  top: 0; left: 0; width: 100%; height: 100%;\n  opacity: 0.08;')

with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)


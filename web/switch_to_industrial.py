import re

with open('ua/index-v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Switch CSS
html = html.replace('href="magazine.css"', 'href="industrial-modern.css"')

# Remove Playfair Display inline styles
html = re.sub(r"font-family:\s*'Playfair Display',\s*serif;", "font-family: 'Inter', sans-serif;", html)

# Replace any var(--accent-gold) with var(--accent-primary) or secondary
html = html.replace('var(--accent-gold)', 'var(--accent-secondary)')

# Replace var(--text-main) background for calculator with var(--bg-card)
html = html.replace('background-color: var(--text-main);', 'background-color: var(--bg-card);')
html = html.replace('color: var(--bg-color);', 'color: var(--text-main);')
html = html.replace('border-color: var(--bg-color);', 'border-color: var(--accent-primary);')

# Update grayscale filter for team
html = html.replace('filter: grayscale(100%);', '') # Let CSS handle it

with open('ua/index-v2.html', 'w', encoding='utf-8') as f:
    f.write(html)

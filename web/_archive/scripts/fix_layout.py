import re

with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix Hero height
hero_fix = """
body > section:nth-of-type(1) {
  /* Hero */
  background-color: var(--color-white);
  color: var(--color-black);
  border-bottom: 4px solid var(--color-black);
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: var(--space-md) 0; /* reduce padding so it fits */
}
"""
css = re.sub(r'body > section:nth-of-type\(1\) \{[^}]*\}', hero_fix.strip(), css)

# Make hero heading smaller on desktop so it fits better
css = css.replace('h1 {\n  font-size: clamp(3rem, 6vw, 5.5rem);', 'h1 {\n  font-size: clamp(2.5rem, 5vw, 4.5rem);')

# Fix Process & Grants section
process_fix = """
/* Process & Grants layout fix */
body > section:nth-of-type(4) {
  background-color: var(--color-black);
  color: var(--color-white);
  border-bottom: 4px solid var(--color-white);
}

/* Left side (Process) */
#process .grid-2 > div:first-child .col-card {
  background: var(--color-black);
  color: var(--color-white);
  border: 4px solid var(--color-gray-dark);
}
#process .grid-2 > div:first-child .col-card .number {
  color: var(--color-white);
  font-size: 3.5rem;
}
#process .grid-2 > div:first-child .col-card > div {
  margin-bottom: 2rem;
  padding-bottom: 2rem;
  border-bottom: 2px solid var(--color-gray-dark);
}
#process .grid-2 > div:first-child .col-card > div:last-child {
  margin-bottom: 0;
  padding-bottom: 0;
  border-bottom: none;
}

/* Right side (Grants) stacked cards */
#process .grid-2 > div:last-child {
  display: flex;
  flex-direction: column;
  gap: var(--space-md);
}
#process .grid-2 > div:last-child .col-card {
  height: auto; /* don't stretch to 100% of a flex column and cause issues */
  background: var(--color-white);
  color: var(--color-black);
  border-color: var(--color-white);
}
"""
css = re.sub(r'/\* Process block override \*/.*?(?=\/\* Trust Section \*/)', process_fix.strip() + '\n\n', css, flags=re.DOTALL)

with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update index-v2.html for the right side of Process to wrap the cards nicely if needed
with open('ua/index-v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# remove stray <div class="col-card"> inline styles if any
html = html.replace('<div class="col-card" >', '<div class="col-card">')

with open('ua/index-v2.html', 'w', encoding='utf-8') as f:
    f.write(html)

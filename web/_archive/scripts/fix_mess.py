import re

with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fix Grids: restore gaps so blocks don't try to merge awkwardly.
css = css.replace('gap: 0; /* Flush blocks */', 'gap: var(--space-md);')
css = css.replace('gap: 0;', 'gap: var(--space-md);')

# 2. Fix Col Cards: remove negative margin hack and ensure they stretch.
css = css.replace('margin: -2px; /* Overlap borders */', '')
# Add flex to col-card
col_card_flex = """
.col-card {
  padding: var(--space-md);
  border: 4px solid var(--color-black);
  background: var(--color-white);
  color: var(--color-black);
  position: relative;
  display: flex;
  flex-direction: column;
  height: 100%;
}
"""
css = re.sub(r'\.col-card\s*\{[^}]*\}', col_card_flex.strip(), css)

# 3. Fix Team images:
team_img_fix = """
.col-card img {
  filter: grayscale(100%) contrast(150%);
  border-bottom: 4px solid var(--color-black);
  margin: -2.5rem -2.5rem 1.5rem -2.5rem;
  width: calc(100% + 5rem);
  max-width: none;
  object-fit: cover;
  flex-shrink: 0;
}
"""
css = re.sub(r'\.col-card img\s*\{[^}]*\}', team_img_fix.strip(), css)

# 4. Process block: let's fix the left side which is a single col-card with 3 items.
# We will just let it be a dark card.
process_fix = """
/* Process block override */
body > section:nth-of-type(4) .col-card {
  background: var(--color-black);
  color: var(--color-white);
  border: 4px solid var(--color-gray-dark);
}
body > section:nth-of-type(4) .col-card .number {
  color: var(--color-white);
  font-size: 3.5rem;
}
body > section:nth-of-type(4) .col-card > div {
  margin-bottom: 2rem;
  padding-bottom: 2rem;
  border-bottom: 2px solid var(--color-gray-dark);
}
body > section:nth-of-type(4) .col-card > div:last-child {
  margin-bottom: 0;
  padding-bottom: 0;
  border-bottom: none;
}
"""
css = re.sub(r'/\* Process block override \*/.*?(?=\/\* Table - Brutalist \*/)', process_fix.strip() + '\n\n', css, flags=re.DOTALL)

# 5. Fix Trust block layout
trust_fix = """
/* Trust Section */
#trust .grid-3 { align-items: stretch; }
#trust .col-card {
  border: 4px solid var(--color-black);
  background: var(--color-gray-light);
  justify-content: flex-start;
}
"""
css = re.sub(r'/\* Trust Section \*/[^}]*\}', trust_fix.strip(), css)

with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)


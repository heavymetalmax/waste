import re

with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Reduce header padding
css = css.replace('padding: 1.5rem 0;', 'padding: 1rem 0;')

# 2. Hero specific sizing to fit on 1 screen
compact_hero_css = """
body > section:nth-of-type(1) {
  background-color: var(--color-white);
  color: var(--color-black);
  border-bottom: 4px solid var(--color-black);
  min-height: calc(100vh - 80px);
  display: flex;
  align-items: center;
  padding: var(--space-sm) 0;
}

body > section:nth-of-type(1) h1 {
  font-size: clamp(2rem, 3.5vw, 3.2rem);
  margin-bottom: 1rem;
}

.hero-desc {
  font-size: 1.1rem;
  font-weight: 500;
  max-width: 800px;
  margin-bottom: 1.5rem;
  line-height: 1.4;
}

.hero-index {
  background-color: var(--color-gray-light);
  border: 4px solid var(--color-black);
  padding: 1rem;
  display: flex;
  flex-direction: column;
}

.index-row {
  display: flex;
  flex-direction: column;
  padding: 0.75rem 0;
  border-bottom: 4px solid var(--color-black);
}

.index-row:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.index-val {
  font-size: 2.5rem;
  font-weight: 900;
  color: var(--color-blue);
  line-height: 1;
  margin-bottom: 0.25rem;
}

.index-val small {
  font-size: 1.2rem;
  font-weight: 800;
  color: var(--color-black);
}

.index-desc strong {
  text-transform: uppercase;
  font-size: 0.85rem;
  font-weight: 800;
  display: block;
}

.index-desc span {
  font-size: 0.85rem;
}

/* Ensure buttons are also slightly more compact in hero */
body > section:nth-of-type(1) .btn {
  padding: 1rem 1.5rem;
}
"""

# Replace the existing hero specific blocks in CSS
css = re.sub(r'body > section:nth-of-type\(1\) \{.*?\}(?=\s*body > section:nth-of-type\(2\))', '', css, flags=re.DOTALL)
css = re.sub(r'/\* Hero Specific \*/.*?(?=\/\* Col Cards)', compact_hero_css.strip() + '\n\n', css, flags=re.DOTALL)

with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)

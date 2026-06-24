with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add safe word breaking and flex-start to col-card
css = css.replace('.col-card {\n  padding: var(--space-md);', '.col-card {\n  padding: var(--space-md);\n  word-break: break-word;\n  justify-content: flex-start;')

# For process left side specifically, make sure the 3rd div doesn't stretch out
process_fix2 = """
#process .grid-2 > div:first-child .col-card > div {
  margin-bottom: 2rem;
  padding-bottom: 2rem;
  border-bottom: 2px solid var(--color-gray-dark);
  flex-shrink: 0;
}
"""
css += process_fix2

with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)


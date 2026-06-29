import re

with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add specific styling for the comparison paragraph
comparison_fix = """
#comparison > .container > p {
  font-size: 1.25rem;
  line-height: 1.6;
  max-width: 900px;
  margin-bottom: var(--space-lg);
  font-weight: 500;
}

/* Make table cells even more spacious and readable */
.table-wrapper table th, .table-wrapper table td {
  padding: 2rem 1.5rem;
}
.table-wrapper table td {
  line-height: 1.5;
}
"""

css += '\n' + comparison_fix.strip()

with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)


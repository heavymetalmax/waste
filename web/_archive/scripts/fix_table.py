import re

with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the old table CSS block entirely
css = re.sub(r'/\* Table - Brutalist \*/.*?(?=\/\* Team Images - Brutalist High Contrast \*/)', '', css, flags=re.DOTALL)

# And remove any stray table overrides we might have added later
css = re.sub(r'/\* Make table cells even more spacious and readable \*/.*?(?=/*|$)', '', css, flags=re.DOTALL)

new_table_css = """
/* Table - Brutalist */
.table-wrapper {
  overflow-x: auto;
  border: 4px solid var(--color-black);
  background-color: var(--color-white);
  color: var(--color-black);
  margin-top: var(--space-md);
  box-shadow: 12px 12px 0 var(--color-black); /* Brutalist drop shadow */
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 1.5rem 1.5rem;
  text-align: left;
  border-bottom: 4px solid var(--color-black);
  border-right: 4px solid var(--color-black);
  line-height: 1.5;
}

th:last-child, td:last-child {
  border-right: none;
}

tr:last-child td {
  border-bottom: none;
}

th {
  font-weight: 900;
  font-size: 1.1rem;
  text-transform: uppercase;
  background-color: var(--color-black);
  color: var(--color-white);
  padding: 1.5rem;
}

td {
  font-size: 1.1rem;
  font-weight: 600;
  background-color: var(--color-white);
  color: var(--color-black);
  vertical-align: top;
}

/* Highlight the BTC column */
th.btc-col, td.btc-col {
  background-color: var(--color-blue);
  color: var(--color-white);
}

/* For better layout within the cells, ensure text isn't cramped */
td:first-child {
  font-weight: 800;
  text-transform: uppercase;
  font-size: 0.9rem;
  background-color: var(--color-gray-light);
  width: 20%;
}
"""

# Insert new table CSS before Team Images
css = css.replace('/* Team Images - Brutalist High Contrast */', new_table_css + '\n\n/* Team Images - Brutalist High Contrast */')

with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)


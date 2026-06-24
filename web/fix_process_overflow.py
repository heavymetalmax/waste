with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add strict overflow boundaries to the process cards
process_overflow_fix = """
/* Prevent any overflow issues specifically in process cards */
#process .col-card {
  overflow: hidden;
  max-width: 100%;
  box-sizing: border-box;
}

#process .col-card p, #process .col-card h3 {
  word-wrap: break-word;
  overflow-wrap: break-word;
  hyphens: auto;
}

/* Ensure body definitively clips horizontal overflow */
html, body {
  overflow-x: hidden;
  width: 100%;
  max-width: 100vw;
}
"""

css += '\n' + process_overflow_fix

with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)


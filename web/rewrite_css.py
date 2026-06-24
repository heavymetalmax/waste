import re

css = """@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

/* ==========================================================================
   BTC Consulting - Heavy Corporate Industrial (High Contrast Blocks)
   ========================================================================== */

:root {
  /* Stark High-Contrast Colors */
  --color-white: #ffffff;
  --color-black: #0a0a0a;
  --color-blue: #0033a0;   /* Deep corporate industrial blue */
  --color-gray-light: #f3f4f6; /* Concrete */
  --color-gray-dark: #374151;  /* Steel */
  
  --bg-color: var(--color-white);
  --text-main: var(--color-black);
  
  --border-color: var(--color-black);

  /* Spacing */
  --space-xs: 0.5rem;
  --space-sm: 1rem;
  --space-md: 2.5rem;
  --space-lg: 5rem;
  --space-xl: 7rem;
}

/* Base */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background-color: var(--bg-color);
  color: var(--text-main);
  font-family: 'Inter', sans-serif;
  line-height: 1.5;
  font-size: 17px;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

a {
  color: inherit;
  text-decoration: none;
}

img {
  max-width: 100%;
  display: block;
  object-fit: cover;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
  font-family: 'Inter', sans-serif;
  line-height: 1.1;
  text-transform: uppercase; /* Industrial punch */
}

h1 {
  font-size: clamp(3rem, 6vw, 5.5rem);
  font-weight: 900;
  letter-spacing: -0.04em;
  margin-bottom: var(--space-md);
  max-width: 900px;
}

h2 {
  font-size: clamp(2.5rem, 5vw, 4rem);
  font-weight: 800;
  letter-spacing: -0.03em;
  margin-bottom: var(--space-lg);
  border-top: 8px solid var(--border-color);
  padding-top: 1rem;
  display: block;
  width: 100%;
}

h3 {
  font-size: 1.5rem;
  font-weight: 800;
  margin-bottom: var(--space-sm);
  letter-spacing: -0.02em;
}

p {
  margin-bottom: var(--space-sm);
  font-weight: 500;
}

/* Layout */
.container {
  width: 100%;
  max-width: 1300px;
  margin: 0 auto;
  padding: 0 var(--space-md);
}

section {
  padding: var(--space-xl) 0;
}

/* Grid System */
.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-lg);
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0; /* Flush blocks */
}

.grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0;
}

@media (max-width: 1024px) {
  .grid-3, .grid-4 { grid-template-columns: 1fr 1fr; }
}

@media (max-width: 768px) {
  .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; }
  h1 { font-size: 2.5rem; }
}

/* Rubrics (Section Labels) */
.rubric {
  display: inline-block;
  background-color: var(--color-black);
  color: var(--color-white);
  padding: 0.5rem 1rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-size: 0.85rem;
  margin-bottom: var(--space-md);
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 1.25rem 2.5rem;
  font-family: 'Inter', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-weight: 800;
  cursor: pointer;
  transition: all 0s; /* Brutalist snap */
  font-size: 1rem;
  border: 4px solid var(--color-black);
  text-align: center;
}

.btn-primary {
  background-color: var(--color-blue);
  color: var(--color-white);
  border-color: var(--color-blue);
}

.btn-primary:hover {
  background-color: var(--color-black);
  border-color: var(--color-black);
}

.btn-outline {
  background-color: transparent;
  color: var(--color-black);
}

.btn-outline:hover {
  background-color: var(--color-black);
  color: var(--color-white);
}

/* Header */
header {
  padding: 1.5rem 0;
  background-color: var(--color-white);
  border-bottom: 4px solid var(--color-black);
}

.logo {
  font-family: 'Inter', sans-serif;
  font-weight: 900;
  font-size: 2rem;
  text-transform: uppercase;
  letter-spacing: -0.05em;
}

.logo span {
  font-weight: 500;
  color: var(--color-blue);
}

/* Specific Sections overrides via HTML structural logic */
/* We will use structural pseudo-classes or ids to paint blocks */

body > section:nth-of-type(1) {
  /* Hero */
  background-color: var(--color-white);
  color: var(--color-black);
  border-bottom: 4px solid var(--color-black);
}

body > section:nth-of-type(2) {
  /* Problem */
  background-color: var(--color-gray-light);
  color: var(--color-black);
  border-bottom: 4px solid var(--color-black);
}

body > section:nth-of-type(3) {
  /* Comparison */
  background-color: var(--color-blue);
  color: var(--color-white);
  border-bottom: 4px solid var(--color-black);
}
body > section:nth-of-type(3) h2 { border-color: var(--color-white); }
body > section:nth-of-type(3) .rubric { background-color: var(--color-white); color: var(--color-blue); }

body > section:nth-of-type(4) {
  /* Process */
  background-color: var(--color-black);
  color: var(--color-white);
  border-bottom: 4px solid var(--color-white);
}
body > section:nth-of-type(4) h2 { border-color: var(--color-white); }
body > section:nth-of-type(4) .rubric { background-color: var(--color-white); color: var(--color-black); }

body > section:nth-of-type(5) {
  /* Calc CTA */
  background-color: var(--color-blue);
  color: var(--color-white);
  border-bottom: 4px solid var(--color-black);
}
body > section:nth-of-type(5) h2 { border-color: var(--color-white); }
body > section:nth-of-type(5) .rubric { background-color: var(--color-white); color: var(--color-blue); }
body > section:nth-of-type(5) .btn-outline { border-color: var(--color-white); color: var(--color-white); }
body > section:nth-of-type(5) .btn-outline:hover { background-color: var(--color-white); color: var(--color-blue); }

body > section:nth-of-type(6) {
  /* Team */
  background-color: var(--color-gray-light);
  color: var(--color-black);
  border-bottom: 4px solid var(--color-black);
}

body > section:nth-of-type(7) {
  /* Trust */
  background-color: var(--color-white);
  color: var(--color-black);
  border-bottom: 4px solid var(--color-black);
}

body > section:nth-of-type(8) {
  /* Contact */
  background-color: var(--color-gray-dark);
  color: var(--color-white);
}
body > section:nth-of-type(8) h2 { border-color: var(--color-white); }

/* Hero Specific */
.hero-desc {
  font-size: 1.5rem;
  font-weight: 500;
  max-width: 800px;
  margin-bottom: var(--space-lg);
  line-height: 1.4;
}

.hero-index {
  background-color: var(--color-gray-light);
  border: 4px solid var(--color-black);
  padding: var(--space-md);
  display: flex;
  flex-direction: column;
}

.index-row {
  display: flex;
  flex-direction: column;
  padding: 1.5rem 0;
  border-bottom: 4px solid var(--color-black);
}

.index-row:last-child {
  border-bottom: none;
}

.index-val {
  font-size: 4rem;
  font-weight: 900;
  color: var(--color-blue);
  line-height: 1;
  margin-bottom: 0.5rem;
}

.index-val small {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--color-black);
}

.index-desc strong {
  text-transform: uppercase;
  font-size: 1rem;
  font-weight: 800;
  display: block;
}

/* Col Cards (Data panels - Blocky) */
.col-card {
  padding: var(--space-md);
  border: 4px solid var(--color-black);
  background: var(--color-white);
  color: var(--color-black);
  margin: -2px; /* Overlap borders */
  position: relative;
}

.col-card h3 {
  font-size: 1.5rem;
}

.col-card .number {
  font-size: 5rem;
  color: var(--color-blue);
  line-height: 1;
  margin-bottom: var(--space-sm);
  display: block;
  font-weight: 900;
}

/* Process block override */
body > section:nth-of-type(4) .col-card {
  background: var(--color-black);
  color: var(--color-white);
  border: 4px solid var(--color-gray-dark);
}
body > section:nth-of-type(4) .col-card .number {
  color: var(--color-white);
}

/* Table - Brutalist */
.table-wrapper {
  overflow-x: auto;
  border: 4px solid var(--color-white);
  background-color: var(--color-blue);
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 1.5rem;
  text-align: left;
  border-bottom: 4px solid var(--color-white);
  border-right: 4px solid var(--color-white);
}

th:last-child, td:last-child {
  border-right: none;
}

tr:last-child td {
  border-bottom: none;
}

th {
  font-weight: 900;
  font-size: 1.25rem;
  text-transform: uppercase;
  background-color: var(--color-black);
  color: var(--color-white);
}

td {
  font-size: 1.1rem;
  font-weight: 600;
}

.btc-col {
  background-color: var(--color-white);
  color: var(--color-blue);
}

/* Team Images - Brutalist High Contrast */
.col-card img {
  filter: grayscale(100%) contrast(150%);
  border-bottom: 4px solid var(--color-black);
  margin-top: calc(-1 * var(--space-md));
  margin-left: calc(-1 * var(--space-md));
  margin-right: calc(-1 * var(--space-md));
  width: calc(100% + var(--space-md) * 2);
  max-width: none;
}

/* Trust Section */
#trust .col-card {
  border: 4px solid var(--color-black);
  background: var(--color-gray-light);
}

/* Footer & Form */
footer {
  background-color: var(--color-black);
  color: var(--color-white);
  padding: var(--space-lg) 0;
  text-align: center;
}

.footer-links {
  display: flex;
  justify-content: center;
  gap: var(--space-md);
  margin-bottom: var(--space-md);
  font-weight: 800;
  text-transform: uppercase;
}

.footer-links a:hover {
  color: var(--color-blue);
}

.contact-form {
  background-color: var(--color-white);
  padding: var(--space-md);
  border: 4px solid var(--color-white); /* override later if needed */
}

.form-group {
  margin-bottom: var(--space-sm);
}

.form-group label {
  display: block;
  font-weight: 800;
  text-transform: uppercase;
  color: var(--color-black);
  margin-bottom: var(--space-xs);
}

.form-group input, .form-group select {
  width: 100%;
  padding: 1.25rem;
  background: var(--color-gray-light);
  border: 4px solid var(--color-gray-light);
  color: var(--color-black);
  font-family: 'Inter', sans-serif;
  font-size: 1.1rem;
  font-weight: 600;
  transition: all 0s;
}

.form-group input:focus, .form-group select:focus {
  outline: none;
  background: var(--color-white);
  border-color: var(--color-blue);
}
"""

with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Also let's clean up index-v2.html from inline styles that clash with the new brutalist CSS
with open('ua/index-v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove inline backgrounds/colors so CSS structural selectors take over completely
html = re.sub(r'style="[^"]*(?:background-color|color|border-color|border-top-color|border-top)[^"]*"', '', html)
html = html.replace('style=""', '')
html = html.replace('style=" "', '')
# Re-add some required layout styles that might have been caught
html = html.replace('<div class="grid-2">', '<div class="grid-2">') # just safe
# We removed filter: grayscale from img in previous steps, let's make sure inline styles are mostly clean
html = re.sub(r'\s+style="[^"]*"', '', html) # Brutal: remove ALL inline styles to let CSS drive

with open('ua/index-v2.html', 'w', encoding='utf-8') as f:
    f.write(html)

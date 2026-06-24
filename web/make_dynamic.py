import re

with open('ua/index-v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Grants HTML to add the huge stat
old_grant = """        <div class="col-card grant-card">
          <h3>Програма FENX.01.03</h3>
          <p>Понад 7.6 млрд євро виділено для Польщі. Програма покриває до 70-85% CapEx для водоканалів. Ми проєктуємо об'єкти так, щоб гарантовано під них підпадати.</p>
        </div>"""

new_grant = """        <div class="col-card grant-card grant-main">
          <h3>Програма FENX.01.03</h3>
          <p class="huge-stat">7.6 млрд €</p>
          <p>виділено для Польщі. Програма покриває до 70-85% CapEx для водоканалів. Ми проєктуємо об'єкти так, щоб гарантовано під них підпадати.</p>
        </div>"""

html = html.replace(old_grant, new_grant)

with open('ua/index-v2.html', 'w', encoding='utf-8') as f:
    f.write(html)


with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

dynamic_css = """
/* DYNAMIC LAYOUT OVERRIDES */

/* 1. Process Staircase Layout */
@media (min-width: 1025px) {
  #process .grid-3 {
    align-items: flex-start;
    padding-bottom: 5rem; /* space for the cascade */
  }
  .process-card:nth-child(1) {
    margin-top: 0;
  }
  .process-card:nth-child(2) {
    margin-top: 6rem;
  }
  .process-card:nth-child(3) {
    margin-top: 12rem;
  }
}

/* 2. Grants Asymmetric Layout */
@media (min-width: 1025px) {
  #grants .grid-3 {
    grid-template-columns: 1.5fr 1fr;
    grid-template-rows: auto auto;
    gap: var(--space-md);
  }
  .grant-card:nth-child(1) {
    grid-column: 1;
    grid-row: 1 / 3;
  }
  .grant-card:nth-child(2) {
    grid-column: 2;
    grid-row: 1;
  }
  .grant-card:nth-child(3) {
    grid-column: 2;
    grid-row: 2;
  }
}

/* Grant Main Card Styling */
.grant-main {
  background-color: var(--color-blue) !important;
  color: var(--color-white) !important;
  border-color: var(--color-blue) !important;
  justify-content: center;
}

.grant-main .huge-stat {
  font-size: clamp(4rem, 8vw, 7rem);
  font-weight: 900;
  line-height: 1;
  letter-spacing: -0.05em;
  margin: 2rem 0;
  color: var(--color-white);
}

.grant-main h3 {
  font-size: 2rem;
  text-transform: uppercase;
}

.grant-main p:not(.huge-stat) {
  font-size: 1.25rem;
  max-width: 80%;
}
"""

css += '\n' + dynamic_css

with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)


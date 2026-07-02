# BTC Consulting — pl_v2

Polish-language static site for biogas/waste-management B2B. All active development lives in `v2/`.

## Dev server

```bash
python3 -m http.server 8000   # serve from /web root
# pages at http://localhost:8000/v2/index.html
```

## Structure

```
v2/                      # active project
  design-system.css      # canonical styles — single source of truth
  DESIGN_SYSTEM.md       # design rules reference
  partials/header.js     # shared header (document.write)
  partials/footer.js     # shared footer (document.write)
  *.html                 # pages (Polish language)
app.min.js               # formsubmit.co handler — included as ../app.min.js?v=5
img/                     # shared images
_archive/                # legacy, do not edit
Ua/                      # Ukrainian-language sister site — INDEPENDENT from v2
```

## Design system rules

- **Brutal-industrial** aesthetic: sharp corners, 4px black borders, hard-offset shadows. No border-radius (except timeline/avatar dots). No soft shadows, no glass/frosted cards.
- **CSS tokens only** — never hardcode hex values or px numbers. Use `var(--color-*)`, `var(--space-*)`, `var(--shadow-hard-*)`.
- **Typography roles:**
  - `var(--font-display)` — H1, H2, large stat numbers
  - `var(--font-primary)` — body text, buttons
  - `var(--font-mono)` — `.rubric`, `.badge-tag`, `<th>`, technical labels
- **Amber (`--color-amber`)** — only for key result numbers (ROI%, savings, grants, efficiency). Not for decorative use, not for CTAs.
- **Section backgrounds** — use `.section-blue / .section-black / .section-gray / .section-gray-dark` classes. Don't add new ID-based CSS rules.
- **Page-local classes** in `<style>` tags are fine for single-page UI (wizard, chat, doc layout). Don't move them to design-system.css unless reused on 2+ pages.
- **Before every change** check `design-system.css` and other pages — don't create a new class if `.col-card / .btn-* / .rubric / .badge-tag` already solves the problem.

## Contact form

All pages share one contact form section (`.contact-section` with `id="contact"`). The **canonical reference is `technology.html`** — keep all pages byte-identical to it. Form submits via formsubmit.co, handled by `../app.min.js?v=5`.

## Partials

Header and footer are injected via `document.write` in `partials/header.js` and `partials/footer.js`. To add a nav link, edit only those files.

## Breakpoints to test

1440px / 1024px / 768px (mobile). Also test Tab-navigation (focus ring visible) and `prefers-reduced-motion`.

## Key pages

| File | Notes |
|---|---|
| `index.html` | Homepage, hero with `.paper-checklist` animation |
| `technology.html` | Technology — canonical form reference |
| `kalkulator-roi.html` | Wizard-based ROI calculator (`.wizard-*`, `.rpt-*`) |
| `mission.html`, `whitepaper.html`, `case-lubin.html` | Doc-style pages (`.doc-*`) |
| `design-guide.html` | Visual component reference — check here before building new UI |
| `template-components.html` | Component snippets |

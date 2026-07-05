# V3_AGENT_BRIEF — BTC Consulting site v3 (execution CLAUDE.md)

> **Purpose of this file:** a single self-contained brief that lets an executor agent build the
> entire v3 site from zero, without asking follow-up questions. Read this top-to-bottom once,
> then work Phase 0 → Phase 6 in order. All paths are absolute from repo root `/Users/max/Projects/Waste/`.
>
> **Language of this doc:** English (for technical precision). **Language of the site:** Polish.
> All site copy is Polish; UI code, comments and keys are English.

---

## COMPETITIVE REFERENCE — Cambi.com (key learnings for v3)

Cambi is the global leader in THP (Thermal Hydrolysis Process) — the closest competitor category.
Their site is strong on trust/proof but misses BTC's advantages. Apply these lessons:

**Cambi live audit findings** (site visited 2026-07-01):
- Design: cream bg `#f0ede8`, rounded organic shapes, soft SaaS feel. Very different from BTC's editorial-industrial direction — do NOT copy their softness.
- Strongest element: 3 stats cards immediately after hero → "3x higher / up to 50% / cut in half" — early, simple, ударні.
- Education block "What is thermal hydrolysis?" — dark navy, video + drop illustrations. BTC needs equivalent.
- Case studies framed as "Real-world impact: See how we drive wastewater innovation globally."
- Closing CTA: "Ready to transform your waste?" — effective rhetorical close.
- NO grants/dotacje content anywhere — this is BTC's unique angle, entirely uncontested.
- NO ROI calculator — BTC's wizard is a competitive differentiator.
- NO urgency / compliance deadline / scarcity — BTC's UWWTD 2026-2028 window is uncontested.
- NO small municipality angle — Cambi starts at 1,500 MT/yr dry solids (large plants only).

**Take from Cambi:**
1. **Stats block = section 2** (immediately after hero, before any explanation). Format: 3 cards, big number + short label. BTC version: `60% mniej kosztów` / `do 85% z dotacji UE` / `6,9 roku zwrotu`
2. **"Co to jest HTC?" education block** — dark section, simple 2-sentence explanation + SVG process diagram. Most wójtów have never heard of HTC.
3. **Named testimonial with one specific number** — *"Jacek Nowak, MPWiK Lubin: osad zredukowany o 75%, zapach całkowicie wyeliminowany"*. One real quote > zero.
4. **Case study = "Realny wpływ"** — frame it as impact, not just a case document.
5. **Closing CTA question** — "Gotowi zamienić problem w zasób?" → form below.
6. **Primary CTA = one action, low friction** — "Porozmawiaj z inżynierem →" or "Zamów bezpłatną ocenę" — not a 5-field form as primary. Phone/email only.
7. **Resources cluster in footer** — whitepaper + UWWTD guide + FAQ + case Lubin as "Zasoby" for non-ready visitors.

**Do NOT copy from Cambi:**
- Rounded corners, soft organic shapes, SaaS warmth — BTC uses STRUKTUR editorial-industrial sharpness
- Generic global messaging — BTC is local, Polish, specific
- Their 6-section mega-nav — BTC stays at 4 nav items max
- "Talk to our team" without urgency — BTC adds "bezpłatna ocena w 2 tygodnie"

**BTC advantages Cambi has NO answer to (lead with these):**
- Grant navigation: only company in Poland guiding small municipalities through FEnIKS/KPO/NFOŚiGW
- <50K PE segment: Cambi doesn't serve this at all
- Hub & Spoke: no competitor offers this model
- Online ROI calculator with live results
- Local Polish team, Polish compliance, Polish language
- Monopoly window 2026–2028 (scarcity no one else mentions)

---

## 0. WHAT WE ARE BUILDING

**BTC Consulting** — Polish B2G/B2B company commercialising **HTC (Hydrothermal Carbonization)**
to process sewage sludge at small/medium wastewater treatment plants (WWTP / oczyszczalnia).

**Products:** `HTC-S` (small, no AD), `HTC-D` (with digester/AD), `TH+HTC` (large, energy self-sufficient).

**Two personas (design every page for both):**

| | Wójt / Burmistrz (decision-maker) | Naczelnik OCS (plant engineer) |
|---|---|---|
| Question #1 | "Can I defend this to the council?" | "Does it actually work?" |
| Fear | Fines, public scandal, spend without result | New tech fails, I'm accountable |
| Language | Money, grants, compliance | Process, parameters, engineering proof |
| CTA | "Bezpłatna ocena — czy kwalifikujesz się na dotację" | "Pobierz whitepaper techniczny" |

**Regulatory driver:** UWWTD 2024/3019 — EU directive; 3 873 Polish WWTPs must modernise by 2035.
First funding window 2026–2028 = BTC's monopoly window.

**Message hierarchy:** `HOOK → REFRAME → EXIT → SCARCITY → CTA`
**Anchor phrase (use across pages):**
> *"Osad to problem dziś. Zasób jutro. Okno dotacji zamknie się wcześniej niż myślisz."*

**SEO cluster:** zagospodarowanie osadów ściekowych, osady ściekowe HTC, utylizacja osadów UWWTD, dotacje na oczyszczalnię.

---

## 1. MANDATORY READING (Phase 0, do this FIRST)

Read via the Read tool before writing any code. Do not invent content — only use verified sources.

> **Path note:** the knowledge base ("wiki") is the numbered folder tree under
> `/Users/max/Projects/Waste/web/website-kit/`, NOT a top-level `wiki/` folder. Verified real paths below.

| Read | Why |
|---|---|
| `/Users/max/Projects/Waste/web/CLAUDE.md` | current dev rules (brutal-industrial, tokens-only, form canon) |
| `/Users/max/Projects/Waste/web/v2/design-system.css` | existing tokens & components to inherit |
| `/Users/max/Projects/Waste/web/website-kit/CONVERSION_PLAN.md` | page-by-page conversion copy & funnel |
| `/Users/max/Projects/Waste/web/website-kit/14-ui-catalog/UI_COMPONENTS_CATALOG.md` | reusable v2 components |
| `/Users/max/Projects/Waste/web/website-kit/01-strategy/messaging-strategy.md` | hero/CTA tone |
| `/Users/max/Projects/Waste/web/website-kit/03-technology/htc-technology.md` | technical parameters (numbers) |
| `/Users/max/Projects/Waste/web/website-kit/04-economics/sludge-economics.md` | economics, gate fees |
| `/Users/max/Projects/Waste/web/website-kit/02-market-hook/market-opportunity.md` | market, UWWTD, grants, deadlines |
| `/Users/max/Projects/Waste/web/website-kit/06-competitive/competitive-analysis.md` | competitors |
| `/Users/max/Projects/Waste/web/website-kit/08-case-study/CORRECTIONS_RESEARCH_REPORT.md` | corrected/verified facts (overrides older numbers) |

**If a path 404s**, search for it: `find /Users/max/Projects/Waste/web/website-kit -name '<name>.md'`.
Do not proceed with a number you cannot trace to one of these files. See §8 (Fact-checking).

---

## 2. TECH STACK (non-negotiable)

- **Static HTML only** — no React/Vue/Next/build step. Pages are plain `.html`.
- **One stylesheet** `v3/design-system.css` — all tokens live here; **no hardcoded hex or px in HTML**.
  Page-specific CSS may live in a `<style>` in that page's `<head>` (only if used on a single page).
- **Block architecture** — every page = a set of independent `<section>` blocks (see §5).
- **Partials via `document.write`** — `v3/partials/header.js` + `v3/partials/footer.js` (same mechanism as v2).
- **Mobile-first** — breakpoints 375 → 768 → 1024 → 1440. Base CSS = 375px, then `@media (min-width:)` up.
- **i18n-ready** — every user-visible string carries `data-i18n="key"`; strings mirrored in `v3/translations/pl.js` (see §7).
- **Forms** — formsubmit.co, handled by `/Users/max/Projects/Waste/web/app.min.js` (include as `../app.min.js?v=5`).
- **Hosting** — static, Netlify/Vercel compatible. No server code.
- **No frameworks, no jQuery, no animation libraries.** Animations = tiny vanilla JS + CSS only.
- **No `!important`** (except the print block) and **no new ID-based CSS rules** — use block classes + section-color classes.

Dev server:
```bash
cd /Users/max/Projects/Waste/web && python3 -m http.server 8000
# → http://localhost:8000/v3/index.html
```

---

## 3. FILE STRUCTURE TO CREATE

```
web/
  v3/                         # NEW active project (build here)
    design-system.css         # v3 tokens + block base styles (mobile-first)
    index.html
    technologia.html
    hub-spoke.html
    teo.html
    dotacje.html
    kalkulator-roi.html
    case-lubin.html
    whitepaper.html
    misja.html
    partials/
      header.js               # new 4-item nav + dropdowns + mobile hamburger
      footer.js               # footer with secondary links
    translations/
      pl.js                   # Polish master strings (window.I18N = {...})
    i18n.js                   # ~10-line engine (applies data-i18n)
    reveal.js                 # IntersectionObserver: scroll reveal + counters + SVG draw
    assets/
      svg/
        htc-process.svg       # flow diagram (inline-ready)
        hub-spoke-map.svg     # hub & spoke topology
      icons/                  # inline SVG icons
    sitemap.xml
    robots.txt
    llms.txt
  img/                        # shared images (unchanged) — stock JPEG + team photos
  app.min.js                  # formsubmit handler (unchanged)
  v2/                         # LEAVE UNTOUCHED (archive/reference)
```

Never edit `v2/`. Copy patterns out of it into `v3/`.

---

## 4. DESIGN DIRECTION — "Editorial Industrial" (STRUKTUR-based)

> **Full reset from v2.** The previous brutal-industrial style (4px borders everywhere, hard-offset shadows,
> pure black/white) is **abandoned**. v3 takes its visual DNA from the STRUKTUR studio reference.
> Do NOT carry over v2 aesthetic patterns unless explicitly listed below as "keep."

### 4.0 Primary Reference: STRUKTUR Studio

Study the STRUKTUR design system and apply its logic to an industrial B2G/B2B context:

| Principle | How it applies to BTC v3 |
|---|---|
| **Cream/sand as page background** | Primary bg = `--color-cream: #f0ede8`. Not white. Sections alternate: cream → black → cream → black. |
| **Typography carries weight — not borders** | H1 is massive, ultra-bold, condensed. No decorative box/frame around it. The type IS the design. |
| **Inline tag chips above headline** | `<span class="tag">UWWTD 2035</span> <span class="tag">KOMUNALNA</span>` — small mono-caps, hairline border, inline row above every H1 |
| **Asymmetric editorial grids** | Mix 40/60, 35/65, 30/70 column splits. Avoid symmetric 50/50 except for card grids. |
| **Photos: sharp crop, no overlay** | Mid-page photos: clean rectangular crop, `border: 1px solid var(--color-black)`, no color overlay. |
| **Hero only: full-bleed photo + overlay** | `--overlay-hero` on full-viewport hero image only. Nowhere else. |
| **Vertical rotated text in margin** | On `/technologia` right margin: `writing-mode: vertical-rl; transform: rotate(180deg)` — technical params like `200°C // 2.0 MPa // 8–12H` |
| **Dark stats section** | Pure black section (`section-black`), white ultra-bold numbers, small muted labels. Confirmed by reference. |
| **Accent color = electric blue** | `--color-accent: #00AAFF` plays STRUKTUR's yellow-green role. Used ONLY on key KPI numbers, `.tag` borders on dark sections, underlines. Never for buttons, decoration, or backgrounds. `--color-amber` does NOT exist in v3 — do not use it. |
| **Thin lines over thick borders** | Accent lines: `1px solid` or `2px solid`. Card outlines: `1px solid var(--color-black)`. **No 4px borders** (v2 pattern — dropped). |
| **No hard-offset box shadows** | The `--shadow-hard-*` tokens from v2 are deprecated. Use `box-shadow: none` or subtle `0 2px 8px rgba(0,0,0,0.08)` on cards. |

### 4.1 Section rhythm (alternating backgrounds)

```
Hero         → section-black (photo + overlay) or cream with giant type
Stats        → section-black (dark, bold numbers)
Problem      → section-cream (warm, editorial)
Solution     → section-white or section-cream
Social proof → section-black or section-cream
Scarcity     → section-black (urgency needs darkness)
CTA / Form   → section-blue (brand, action)
FAQ          → section-cream
```

Never use the same background two sections in a row. The rhythm creates visual breathing.

### 4.2 Typography

```
--font-display : 'Big Shoulders Display', 'Anton', Impact, sans-serif; /* H1/H2, stats */
--font-primary : 'Inter', system-ui, sans-serif;                        /* body, forms */
--font-mono    : 'JetBrains Mono', 'Courier New', monospace;            /* tags, labels, th */
```

Type scale (mobile-first, `clamp`):
```css
h1 { font-size: clamp(3rem, 9vw, 7rem); font-weight: 900; line-height: 0.95; letter-spacing: -0.02em; text-transform: uppercase; }
h2 { font-size: clamp(2rem, 5vw, 3.5rem); font-weight: 800; line-height: 1.05; }
h3 { font-size: clamp(1.25rem, 3vw, 1.75rem); font-weight: 700; }
```

`letter-spacing: -0.02em` on H1/H2 — tight condensed feel like STRUKTUR.
Body text: `font-size: clamp(1rem, 1.5vw, 1.125rem); line-height: 1.7;`

### 4.3 Forbidden (hard rules)

- ❌ `border-radius` on cards/buttons (except `.tag` chips: `2px`)
- ❌ 4px or thicker card borders
- ❌ Hard-offset `box-shadow` (e.g. `12px 12px 0 black`) — this is v2, not v3
- ❌ Color overlays on mid-page photos
- ❌ Generic stock smiling-people photos
- ❌ Video backgrounds, Lottie, external animation libraries
- ❌ Soft/glass morphism cards
- ❌ Gradient buttons
- ❌ More than 3 section background colors on one page

---

## 5. DESIGN TOKENS (authoritative table for v3)

Put these in `:root` in `v3/design-system.css`. **The palette is fixed — do not change values.**
This is a clean start — do NOT copy v2 token values blindly; use this table as source of truth.

### Colors

| Token | Value | Use |
|---|---|---|
| `--color-cream` | `#f0ede8` | **Primary page background** — warm, editorial, not pure white |
| `--color-black` | `#111111` | Text, borders, section-black background |
| `--color-white` | `#ffffff` | Text on dark sections; card backgrounds inside dark sections |
| `--color-blue` | `#0033a0` | Brand, CTA buttons, `.section-blue` background |
| `--color-accent` | `#00AAFF` | **Design accent** — KPI numbers, tag chips border on dark, accent underlines, hover states. Replaces amber for visual accent role. |
| `--color-muted` | `#6b6560` | Secondary text, labels, metadata on cream sections |
| `--color-border` | `#1a1a1a` | Card outlines, thin accent lines (`1px solid`) |

> **Accent color logic:** `--color-accent: #00AAFF` (electric blue) plays the role STRUKTUR's yellow-green plays —
> a high-contrast pop used sparingly. Use for: key KPI numbers, `.tag` border on dark backgrounds,
> horizontal accent lines under H2, hover state on links. `--color-blue: #0033a0` remains
> for CTAs/buttons/section-blue. They are two different blues — one dark/action, one electric/accent.

### Typography tokens

| Token | Value |
|---|---|
| `--font-display` | `'Big Shoulders Display', 'Anton', Impact, sans-serif` |
| `--font-primary` | `'Inter', system-ui, -apple-system, sans-serif` |
| `--font-mono` | `'JetBrains Mono', 'Courier New', monospace` |

### Spacing

| Token | Value | Use |
|---|---|---|
| `--space-xs` | `0.5rem` | Tight gaps, inline padding |
| `--space-sm` | `1rem` | Small gaps |
| `--space-md` | `2rem` | Card padding |
| `--space-lg` | `4rem` | Large gaps |
| `--space-section` | `clamp(5rem, 10vw, 8rem)` | Vertical section padding (top+bottom) |

### Effects

| Token | Value | Use |
|---|---|---|
| `--overlay-hero` | `linear-gradient(rgba(10,10,10,0.7), rgba(0,51,160,0.4))` | Photo hero overlay (hero only) |
| `--border-thin` | `1px solid var(--color-border)` | Card outlines, photo frames |
| `--border-accent` | `2px solid var(--color-border)` | Section dividers, emphasis |
| `--transition` | `0.2s ease` | Hover transitions |
| `--reveal-dist` | `20px` | Scroll-reveal translateY start |

### Section background classes

```css
.section-cream  { background: var(--color-cream); color: var(--color-black); }
.section-white  { background: var(--color-white); color: var(--color-black); }
.section-black  { background: var(--color-black); color: var(--color-white); }
.section-blue   { background: var(--color-blue);  color: var(--color-white); }
```

These four are all you need. No `.section-gray` or `.section-gray-dark` in v3 — cream replaces gray.

### Tag chips (inline, above H1)

```css
.tag {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  border: 1px solid currentColor;
  border-radius: 2px;
  padding: 2px 8px;
  margin-right: 6px;
}
```

Usage above every H1: `<span class="tag">UWWTD 2035</span><span class="tag">KOMUNALNA</span>`

### Font loading (add to every page `<head>` before `design-system.css`)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;900&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
```

### Layout utility classes (add to `design-system.css`)

```css
.container {
  width: 100%;
  max-width: 1200px;
  margin-inline: auto;
  padding-inline: var(--space-md);   /* 2rem sides on mobile */
}
@media (min-width: 768px) {
  .container { padding-inline: var(--space-lg); }  /* 4rem on tablet+ */
}

.grid-4 { display: grid; grid-template-columns: 1fr; gap: var(--space-md); }
@media (min-width: 768px) { .grid-4 { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 1024px) { .grid-4 { grid-template-columns: repeat(4, 1fr); } }

.grid-2 { display: grid; grid-template-columns: 1fr; gap: var(--space-md); }
@media (min-width: 768px) { .grid-2 { grid-template-columns: repeat(2, 1fr); } }
```

### Button variants (all in `design-system.css`)

```css
.btn {
  display: inline-block;
  font-family: var(--font-primary);
  font-weight: 600;
  font-size: 0.9rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  padding: 0.85em 2em;
  border: 2px solid transparent;
  cursor: pointer;
  text-decoration: none;
  transition: background var(--transition), color var(--transition), border-color var(--transition);
}
.btn-primary {
  background: var(--color-blue);
  color: var(--color-white);
  border-color: var(--color-blue);
}
.btn-primary:hover { background: #002080; border-color: #002080; }
/* For use on dark/photo hero backgrounds */
.btn-outline-white {
  background: transparent;
  color: var(--color-white);
  border-color: var(--color-white);
}
.btn-outline-white:hover {
  background: var(--color-white);
  color: var(--color-black);
}
/* For use on light (cream/white) backgrounds */
.btn-outline {
  background: transparent;
  color: var(--color-black);
  border-color: var(--color-black);
}
.btn-outline:hover { background: var(--color-black); color: var(--color-white); }
```

### Hero block CSS (copy to `design-system.css`)

```css
/* Pattern A: background-image div (simpler, use for inline photo control) */
.hero-photo {
  position: relative;
  min-height: 100svh;
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
}
.hero-overlay {
  position: absolute;
  inset: 0;
  background: var(--overlay-hero);
}
.hero-content {
  position: relative;
  z-index: 1;
  color: var(--color-white);
  padding-block: var(--space-section);
}
/* Pattern B: <picture> tag (better for LCP/WebP) */
.block-hero--photo { position: relative; overflow: hidden; min-height: 100svh; }
.hero-bg { position: absolute; inset: 0; }
.hero-bg img { width: 100%; height: 100%; object-fit: cover; }
.block-hero--photo::after {
  content: ''; position: absolute; inset: 0;
  background: var(--overlay-hero); z-index: 1;
}
.hero-overlay-content {
  position: relative; z-index: 2;
  color: var(--color-white);
  display: flex; align-items: center;
  min-height: 100svh;
}
/* Use Pattern B for index.html and technologia.html (critical LCP images) */
/* Use Pattern A for other pages where image may be a placeholder */
```

### Base CSS rules (copy verbatim)

```css
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; overflow-x: hidden; }
body { font-family: var(--font-primary); font-size: clamp(1rem, 1.5vw, 1.125rem);
       line-height: 1.7; background: var(--color-cream); color: var(--color-black); }
img, picture { max-width: 100%; height: auto; display: block; }
:focus-visible { outline: 2px solid var(--color-blue); outline-offset: 3px; }
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation-duration: 0.01ms !important;
  transition-duration: 0.01ms !important; } }
```

### Deprecated from v2 (do NOT use in v3)

```
--shadow-hard-sm / --shadow-hard-lg   → hard offset shadows dropped
--color-gray / --color-gray-dark      → replaced by --color-cream + --color-muted
.section-gray / .section-gray-dark    → use .section-cream instead
4px border on cards                   → use 1px (--border-thin)
```

---

## 6. BLOCK ARCHITECTURE ("Lego" rules)

Every page is an ordered stack of self-contained `<section>` blocks. Each block:

1. Is exactly one `<section class="block-{name} section-{color}" id="{name}">`.
2. Does not depend on any other block (fully isolated CSS; safe to reorder/remove).
3. Styles live in `design-system.css` if reusable, else in a page `<style>` if single-page only.
4. Every visible string has `data-i18n="{page}.{block}.{field}"`.
5. Is wrapped in mandatory comments `<!-- BLOCK: name -->` … `<!-- /BLOCK: name -->`.
6. Unique factual claims carry a source comment (see §8).

### 6.1 Block skeleton

```html
<!-- BLOCK: hero -->
<section class="block-hero section-black" id="hero">
  <!-- Background photo with overlay — hero only -->
  <div class="hero-photo" style="background-image: url('../img/stock/wwtp-aerial.jpg')">
    <div class="hero-overlay"></div>
    <div class="container hero-content">
      <div class="tag-row">
        <span class="tag" data-i18n="home.hero.tag1">UWWTD 2035</span>
        <span class="tag" data-i18n="home.hero.tag2">3 873 oczyszczalni</span>
      </div>
      <h1 data-i18n="home.hero.h1">Osad to problem.<br>Dotacja UE<br>to rozwiązanie.</h1>
      <p class="hero-desc" data-i18n="home.hero.sub">Podaj wolumen osadu — pokażemy CAPEX, oszczędności i okres zwrotu w 60 sekund.</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="kalkulator-roi.html" data-i18n="home.hero.cta1">Oblicz oszczędności →</a>
        <a class="btn btn-outline-white" href="#contact" data-i18n="home.hero.cta2">Zamów bezpłatną ocenę</a>
      </div>
    </div>
  </div>
</section>
<!-- /BLOCK: hero -->

<!-- BLOCK: stats -->
<section class="block-stats section-black" id="stats" data-reveal>
  <div class="container stats-grid">
    <div class="stat"><span class="stat-num" data-count="3873">3 873</span><span class="stat-lbl" data-i18n="home.stats.s1">oczyszczalni do modernizacji</span></div>
    <div class="stat"><span class="stat-num" data-count="85">85%</span><span class="stat-lbl" data-i18n="home.stats.s2">CapEx z dotacji UE</span></div>
    <div class="stat"><span class="stat-num accent" data-count="60">60%</span><span class="stat-lbl" data-i18n="home.stats.s3">oszczędności vs. status quo</span></div>
    <div class="stat"><span class="stat-num">2026</span><span class="stat-lbl" data-i18n="home.stats.s4">okno dotacyjne</span></div>
  </div>
</section>
<!-- /BLOCK: stats -->
```

### 6.2 Photo hero variant (with dark overlay + WebP)
```html
<!-- BLOCK: hero -->
<section class="block-hero block-hero--photo" id="hero">
  <picture class="hero-bg">
    <source srcset="../img/stock/wwtp-01.webp" type="image/webp">
    <img src="../img/stock/wwtp-01.jpg" alt="" width="1920" height="1080" fetchpriority="high">
  </picture>
  <div class="container hero-overlay-content">
    <h1 data-i18n="home.hero.h1">…</h1>
    <!-- CTAs -->
  </div>
</section>
<!-- /BLOCK: hero -->
```
CSS: `.block-hero--photo { position:relative; }` `.hero-bg img { position:absolute; inset:0; width:100%;
height:100%; object-fit:cover; z-index:0; }` `.block-hero--photo::after { content:''; position:absolute;
inset:0; background:var(--overlay-hero); z-index:1; }` `.hero-overlay-content { position:relative; z-index:2;
color:var(--color-white); }`. Above-the-fold hero image = `fetchpriority="high"` and **no** `loading="lazy"`;
every other photo = `loading="lazy"` + explicit `width`/`height`.

### 6.3 KPI / stats block (counter animation)
```html
<!-- BLOCK: stats -->
<section class="block-stats section-black" id="stats" data-reveal>
  <div class="container grid-4">
    <div class="stat-item">
      <div class="stat-number" data-count="3873" data-i18n="home.stats.n1">3 873</div>
      <div class="stat-label" data-i18n="home.stats.l1">oczyszczalni do modernizacji</div>
    </div>
    <!-- 3 more stat-items: PLN 30B dotacji | do 85% CapEx | okno 2026–2028 -->
  </div>
</section>
<!-- /BLOCK: stats -->
```
`data-count` = numeric target; `reveal.js` animates 0→target on first intersection. Numbers use
`--font-display`; add class `accent` to highlight key numbers with `color: var(--color-accent)`.
Do NOT use `--color-amber` — it does not exist in v3.

### 6.4 Scroll reveal + counters + SVG draw (`v3/reveal.js`, pure JS)
- Add `data-reveal` to blocks that should fade/slide in; CSS default `opacity:0; transform:translateY(var(--reveal-dist))`,
  `.is-visible { opacity:1; transform:none; transition:opacity .6s, transform .6s; }`.
- One `IntersectionObserver` toggles `.is-visible`, starts counters (`[data-count]`), and triggers SVG draw
  (`stroke-dashoffset → 0`) once, then unobserves.
- **Guard everything** with `if (window.matchMedia('(prefers-reduced-motion: reduce)').matches)` → set final
  state immediately, run no animation. Content must be fully visible/readable with JS disabled too (progressive
  enhancement: reveal starts from `opacity:1` via a `.js` class on `<html>`, or `<noscript>` fallback style).

### 6.5 FAQ block (accordion, `FAQPage` schema)
Reuse v2 pattern: `.faq-item > button.faq-question (+ .faq-icon) + .faq-answer`. Minimal JS toggle (aria-expanded,
`hidden` attribute). Every FAQ page block must also emit matching `FAQPage` JSON-LD (§9).

### 6.6 Contact block (CANONICAL — byte-identical everywhere)
The contact `<section id="contact" class="block-contact ...">` must be **identical on every page**. Establish the
canonical version on `technologia.html` first, then copy byte-for-byte to all pages (as v2 did with `technology.html`).
Submits via formsubmit.co + `../app.min.js?v=5`. Do not diverge fields between pages.

---

## 7. i18n ARCHITECTURE

`v3/translations/pl.js` (loaded first, before `i18n.js`):
```js
window.I18N = {
  "home.hero.h1": "Osad to problem. Dotacja UE to rozwiązanie.",
  "home.hero.sub": "…",
  // one entry per data-i18n key across all pages
};
```
`v3/i18n.js` (minimal engine):
```js
document.querySelectorAll('[data-i18n]').forEach(el => {
  const k = el.getAttribute('data-i18n');
  if (window.I18N && window.I18N[k] != null) el.textContent = window.I18N[k];
});
```
Rules: keys are `{page}.{block}.{field}`. HTML ships with Polish as inline fallback text (so the page reads
correctly even before JS). Later languages = add `en.js` / `ua.js` with the same keys, load the one matching
`<html lang="">`. Do not put HTML markup inside translation values (text nodes only); for rich blocks split into
multiple keys.

**Existing translation source (reuse, don't reinvent):** `web/website-kit/11-assets/translations/` already contains
`pl.json`, `eu.json`, `ua.json`. Read `pl.json` first and lift any matching copy into `v3/translations/pl.js`
(convert JSON → `window.I18N = {…}`). Later you can wire `en.js`/`ua.js` from `eu.json`/`ua.json`.

---

## 8. FACT-CHECKING RULES (mandatory)

1. Use **only** numbers traceable to the files under `web/website-kit/` listed in §1:
   `03-technology/htc-technology.md`, `04-economics/sludge-economics.md`,
   `02-market-hook/market-opportunity.md`, `06-competitive/competitive-analysis.md`,
   `08-case-study/CORRECTIONS_RESEARCH_REPORT.md`.
   `CORRECTIONS_RESEARCH_REPORT.md` **overrides** any conflicting older number.
2. **Never invent numbers.** If a value is unknown, phrase as "do X%" / "od X" / "~X" rather than a fabricated exact.
3. Every **unique** factual claim gets an inline source comment directly above it:
   ```html
   <!-- fact: wiki/sludge-economics.md — PLN 550/t current avg municipal gate fee -->
   <div class="stat-number" data-count="550" data-i18n="…">PLN 550/t</div>
   ```
4. Dates/deadlines (UWWTD transposition 2027, milestones 2033/2035/2040/2045, funding window 2026–2028)
   must be verified against `02-market-hook/market-opportunity.md` before use.

**Pre-verified anchor facts** (still cite source in code; re-check against files if they disagree):
current municipal sludge cost **PLN 550/t**; BTC gate fee **PLN 200–225/t** (~60% saving); Hub&Spoke spoke (5K PE)
saves **36–41%** within 50 km; payback at 85% grant **6.9 years**; **3 873** Polish WWTPs need modernisation;
**AGH Kraków** technology partner (LOI signed); **MPWiK Lubin** first commercial case (09–10.2025);
HTC process **200°C / 2.0 MPa / 8–12 h / −75% volume**; HTC legal in PL since **14.01.2025**;
typical project **EUR 5M CAPEX → gmina 15% (EUR 750K), EU 85%**.

---

## 9. SEO & AI VISIBILITY

Per page:
- `<title>` = key phrase + `| BTC Consulting`; `<meta name="description">` 150–160 chars with keyword;
  `<link rel="canonical">`; Open Graph (`og:title`, `og:description`, `og:image`); `<html lang="pl">`.
- Semantic HTML5: `<main> <article> <section> <nav> <aside>`; strict `<h1>→<h2>→<h3>` with no skipped levels.
- JSON-LD `Organization` on every page:
  ```json
  {"@context":"https://schema.org","@type":"Organization","name":"BTC Consulting",
   "description":"Technologia HTC do zagospodarowania osadów ściekowych","areaServed":"PL",
   "knowsAbout":["HTC","osady ściekowe","UWWTD","dotacje UE"]}
  ```
- Additional schema: `/technologia` → `TechArticle`; `/kalkulator-roi` → `WebApplication`; `/case-lubin` → `Article`/`CaseStudy`;
  every page with a FAQ block → `FAQPage`.
- Root files: `v3/sitemap.xml`, `v3/robots.txt`, `v3/llms.txt`:
  ```
  # BTC Consulting
  BTC Consulting dostarcza technologię HTC (Hydrothermal Carbonization)
  do zagospodarowania osadów ściekowych dla polskich oczyszczalni ścieków.
  ```

---

## 10. NAVIGATION (partials/header.js)

```
Główna (/)
Rozwiązania ▼
  ├─ Technologia HTC       (/technologia)
  └─ Model Hub & Spoke     (/hub-spoke)
Finansowanie ▼
  ├─ TEO – ocena wstępna   (/teo)
  └─ Dotacje UE            (/dotacje)
Kalkulator ROI            (/kalkulator-roi)
[Bezpłatna ocena →]        (#contact)  — sticky CTA
```
- Desktop: 4 top items, two with dropdowns. `<768px`: hamburger menu (reuse v2's `.mobile-toggle` + `#mobile-nav`
  wiring in `app.min.js`, which already handles `aria-expanded`). Prefer pure-CSS or minimal-JS dropdown; keyboard accessible.
- **Footer** (partials/footer.js) secondary links: `case-lubin`, `whitepaper`, `misja`.

---

## 11. PAGE SPECS (blocks in conversion order)

Copy source = `CONVERSION_PLAN.md`. Numbers source = wiki files (§8). Each block follows §6 rules.

### `/` index.html — 11 blocks
1. **hero** (photo WWTP + overlay) — H1 "Osad to problem. Dotacja UE to rozwiązanie."; 1-line sub; 2 CTA (→ calc, → #contact).
2. **stats** — 4 counters: `3 873 oczyszczalni | PLN 30B dotacji | do 85% CapEx | okno 2026–2028`.
3. **problem** — "Osad to problem, który rośnie" — 3 cols: regulacja UWWTD / koszt utylizacji / brak rozwiązania dla małych gmin.
4. **reframe** — "Osad to zasób" — before/after HTC comparison table with numbers.
5. **solution** — 3 products HTC-S / HTC-D / TH+HTC as selection cards.
6. **economics** — Hub&Spoke mini-preview (PLN 550→200/t, ~60% savings).
7. **proof** — Lubin blockquote + AGH + INTROL logos/mentions.
8. **scarcity** — "Okno dotacji zamknie się wcześniej" — timeline 2026-2028-2035.
9. **cta-exit** — "Bezpłatna ocena wstępna w 2 tygodnie" → /teo or inline.
10. **faq** — 5 Q: koszt / granty / termin realizacji / mała gmina / PFAS.
11. **contact** — canonical.

### `/technologia` technologia.html — establish CANONICAL contact here first
1. hero (reactor photo + overlay) · 2. what-is (2 cols: explanation + **htc-process.svg** flow: Osad surowy → Reaktor HTC (200°C/2MPa) → Hydrochar → Zastosowanie) · 3. tech-stats (200°C / 2.0 MPa / 8–12h / −75% volume, counters) · 4. before-after table (vol −75%, moisture 76%→30%, pathogens eliminated, smell none) · 5. 3-configs cards (HTC-S/HTC-D/TH+HTC with params) · 6. proof ("10 lat badań AGH + MPWiK Lubin") · 7. regulation ("Od 14.01.2025 HTC oficjalnie dozwolona w Polsce") · 8. faq (5 technical Q for engineer) · 9. contact. Add `TechArticle` schema.

### `/hub-spoke` hub-spoke.html — NEW
1. hero · 2. concept (**hub-spoke-map.svg**: 1 hub 25K PE + 4 spoke 5–8K PE, arrows) · 3. economics table (spoke PLN 200/t vs PLN 550/t = PLN 350/t saving) · 4. who-is-spoke (1–20K PE, ≤50 km) · 5. who-is-hub (15–50K PE, has land, wants Gate Fee) · 6. grants (hub 85% grant + spoke reduced gate fee = win-win) · 7. faq · 8. cta ("Sprawdź czy Twoja gmina może być spoke lub hub") · 9. contact.

### `/teo` teo.html
1. hero · 2. what-is-teo (why no TEO = no grant; 4–6 tygodni, EUR 20–40K) · 3. process (4 steps: Analiza danych → Koncepcja → Raport → Aplikacja dotacyjna) · 4. deliverables (PDF report + config recommendation + ścieżka dotacyjna) · 5. proof ("200+ ocen | do 90% grant | 11 lat w branży") · 6. faq (both personas) · 7. cta ("Zamów TEO – wycena w 48h") · 8. contact.

### `/dotacje` dotacje.html — NEW, highest priority
1. hero · 2. why-now (first-come-first-served, okno 2026–2028) · 3. grants-table (FEnIKS 75–85% / KPO / NFOŚiGW / LIFE do 90%) · 4. how-much (EUR 5M CAPEX → gmina EUR 750K 15%, EU EUR 4.25M 85%) · 5. timeline (UWWTD: 2027 transposition / 2033 / 2035 / 2040 / 2045) · 6. btc-role ("BTC = navigator dotacyjny. Bez TEO nie ma dotacji.") · 7. faq (5 Q) · 8. cta · 9. contact.

### `/kalkulator-roi` kalkulator-roi.html — adapt v2 wizard
Keep the full wizard (`#wizard-step1..4` + results, classes `.wizard-* .rpt-*`). v3 improvements:
full-screen step per screen on mobile; **sticky progress bar** on mobile; results screen **share button**
(encode results into URL params, decode on load). Add `WebApplication` schema. Verify formulas against
`12-calculator/BTC_Calculator_Model_PL.xlsx` if present.

### `/case-lubin` case-lubin.html (doc layout)
1. hero (lubin-wwtp photo + overlay; tag: "CASE STUDY — MPWIK LUBIN") · 2. metadata table (Klient: MPWiK Lubin / Lokalizacja: Lubin, Dolny Śląsk / Realizacja: IX–X 2025 / Konfiguracja: HTC-S) · 3. challenge (osad problem before HTC) · 4. solution (what BTC delivered) · 5. results stats (−75% volume / wilgoć 76%→30% / patogeny: 0 / zapach: brak) · 6. blockquote (MPWiK Lubin client quote) · 7. bridge-to-small ("Model Hub & Spoke — rozwiązanie dla małych gmin") · 8. faq (3–4 Q) · 9. contact. Schema: `Article` + `CaseStudy`.

### `/whitepaper` whitepaper.html (doc layout)
1. hero (doc header; tag: "WHITEPAPER TECHNICZNY") · 2. abstract (3-sentence summary of HTC) · 3. contents-preview (4 chapters listed, each with 1-line description) · 4. download-cta ("Pobierz whitepaper PDF — 24 strony") — button links to `../website-kit/03-technology/whitepaper_btc_consulting_v4.pdf` (verified path) · 5. also-read (links to /technologia and /case-lubin). No `<form>`, no schema (simple content page).

### `/misja` misja.html (doc layout)
1. hero (section-cream, no photo; tag: "MISJA"; H1: "Kontrolujemy osad. Zanim UWWTD zmusi.") · 2. about (2-col: BTC story paragraph + 4 team portrait cards from `../img/team/`) · 3. credentials (AGH Kraków partnership block: logo + "10 lat wspólnych badań"; MPWiK Lubin: logo + "pierwsza komercyjna instalacja HTC w Polsce") · 4. values (3 tiles: Polskie rozwiązanie / Weryfikowalna technologia / Konkretne liczby) · 5. contact. Schema: `Organization`.

### Contact form — formsubmit.co configuration

**Email for form action:** use `maxym.koval@gmail.com` (owner's email).
Form action: `https://formsubmit.co/maxym.koval@gmail.com`
Include hidden fields: `<input type="hidden" name="_subject" value="BTC Consulting — zapytanie ze strony">` and `<input type="hidden" name="_captcha" value="false">`.

---

## 12. GRAPHICS & ASSETS

- **htc-process.svg** — inline flow diagram, animated draw-in (`stroke-dasharray/offset` → 0 on reveal).
- **hub-spoke-map.svg** — schematic geographic topology, hub node + spoke nodes + arrows.
- **Counters** — `[data-count]` animate up on scroll.
- **Scroll fade-in** — every `data-reveal` block.
- **Photos (real locations — verified):**
  - 7 Adobe Stock JPEG live at `web/website-kit/11-assets/stock-photos/AdobeStock_*.jpeg` (industrial WWTP/water).
    **Copy the ones you use into `web/img/stock/`** (create the dir) with clean names (e.g. `wwtp-01.jpg`), then
    reference `../img/stock/…`. Use in hero sections with `--overlay-hero`; `<picture>` WebP + JPEG fallback;
    `loading="lazy"` (except above-fold hero); always `width`/`height`.
  - Team photos: 4 JPG already at `web/img/team/` (`koval-m`, `krop-a`, `krop-e`, `wilk-m`; also mirrored in
    `11-assets/team-photos/`). Reference `../img/team/…`. Cards with hard shadow + 4px border, in a "Zespół" block
    or footer-adjacent (e.g. `/misja`).
- Existing background asset `web/img/Procedural-Gradient-Background.gif` — do NOT use (video/gif bg is forbidden).
- Forbidden: generic happy-people stock, clipart icons, video backgrounds.

If WebP versions don't exist yet, generate them (`cwebp` if available) or ship JPEG-only `<img>` and note it as TODO —
do not block the build on WebP.

---

## 13. MOBILE CHECKLIST (priority #1 — design every block at 375px FIRST)

- [ ] Base CSS has no media queries; enhancements added at `@media (min-width:768px)` then `1024px` then `1440px`.
- [ ] H1 uses `clamp()`, never fixed px (`clamp(2.5rem,6vw,5rem)`).
- [ ] Body `font-size ≥ 16px`; `line-height ≥ 1.6`.
- [ ] Tap targets `min-height:48px; min-width:48px`; min 8px gap between interactive elements.
- [ ] Tables: `.table-wrapper { overflow-x:auto }` OR a collapsed stacked variant on mobile.
- [ ] Nav = hamburger `<768px`, keyboard accessible, `aria-expanded` toggled.
- [ ] Wizard: each step full-screen on mobile, no horizontal scroll, progress bar sticky.
- [ ] Images `max-width:100%; height:auto`.
- [ ] No horizontal overflow anywhere (`html,body { overflow-x:hidden }` + audit at 375px).
- [ ] Test in DevTools iPhone SE (375) and iPhone 14 Pro (390); check nav, form, wizard, tables, stats-grid.

---

## 14. EXECUTION ORDER

**Phase 0 — Prep:** read §1 files; audit `v2/design-system.css` → token list; list new v3 classes; write `v3/design-system.css` (tokens + mobile-first reset + block base styles + section-color classes).

**Phase 1 — Skeleton:** `partials/header.js` (new nav + dropdowns + hamburger); `partials/footer.js`; `i18n.js`; `reveal.js`; finalise `design-system.css`.

**Phase 2 — Home:** `index.html` (all 11 blocks); test 375px + 1440px.

**Phase 3 — Conversion pages:** `technologia.html` (define canonical contact here) → `teo.html` → `dotacje.html` → `hub-spoke.html` → `kalkulator-roi.html`. Build `htc-process.svg` and `hub-spoke-map.svg` here.

**Phase 4 — Supporting:** `case-lubin.html`, `whitepaper.html`, `misja.html`.

**Phase 5 — SEO/tech:** JSON-LD on every page; `sitemap.xml`; `robots.txt`; `llms.txt`; fill `translations/pl.js` with all keys.

**Phase 6 — QA:** mobile test each page (375/768/1024); Tab-nav focus ring visible; `prefers-reduced-motion` disables animation; re-verify every number vs wiki (§8); validate HTML (no unclosed/mis-nested tags); PageSpeed target 90+.

---

## 15. DEFINITION OF DONE

- [ ] 9 pages build & render; dev server serves `/v3/*` with no console errors.
- [ ] Contact section byte-identical across all pages (canon = technologia.html).
- [ ] Every visible string has `data-i18n`; `translations/pl.js` has every key; `i18n.js` applies cleanly.
- [ ] No hardcoded hex/px in HTML; no `!important` (except print); no new ID-based CSS rules.
- [ ] Every block wrapped in `<!-- BLOCK: name -->` comments and CSS-isolated.
- [ ] Every unique fact has a `<!-- fact: source — value -->` comment; no number lacks a traceable source.
- [ ] JSON-LD (Organization + page-specific + FAQPage) present; meta/canonical/OG on every page.
- [ ] Mobile checklist (§13) passes at 375px; reduced-motion respected; focus rings visible.
- [ ] `sitemap.xml`, `robots.txt`, `llms.txt` present. `v2/` untouched.
- [ ] All image placeholders clearly marked with `data-slot` attribute; no broken `<img>` paths.
- [ ] `web/v3/IMAGES_NEEDED.md` generated listing all placeholder slots with source recommendations.

---

## 16. IMAGE SLOTS AND PLACEHOLDER PROTOCOL

### Rule: always use placeholders, never broken paths

For every image slot, use a labeled placeholder. Never leave a broken `<img src="">` or empty `background-image`. Two patterns:

**For `<section>` hero backgrounds** — use inline CSS variable:
```html
<section class="block-hero section-black" id="hero">
  <div class="hero-photo" style="background-image: var(--img-hero, none);">
    <!-- agent leaves var(--img-hero, none); real path set after image is sourced -->
```

**For editorial split images** — use a `<div class="img-placeholder">`:
```html
<div class="img-placeholder" data-slot="htc-reactor">
  <!-- replace with: <img src="img/stock/htc-reactor.jpg" alt="..."> -->
</div>
```

**Add this utility in `design-system.css`:**
```css
.img-placeholder {
  position: relative;
  min-height: 300px;
  background: repeating-linear-gradient(
    45deg, #1a1a1a, #1a1a1a 10px, #222 10px, #222 20px
  );
}
.img-placeholder::after {
  content: "[ " attr(data-slot) " ]";
  position: absolute; inset: 0;
  display: flex; align-items: center; justify-content: center;
  color: #555; font-family: monospace; font-size: 0.75rem;
  letter-spacing: 0.1em;
}
```

---

### Required image inventory

| Slot ID | Page / Block | Type | Min size | Notes |
|---------|-------------|------|----------|-------|
| `wwtp-aerial` | index / `block-hero` | Full-bleed photo BG | 1920×1080 | Aerial/drone WWTP; dark CSS overlay applied — slightly out-of-focus OK |
| `htc-reactor` | technologia / editorial split | Photo 40/60 layout | 800×600 | Physical HTC reactor or equipment; industrial feel |
| `eu-funds` | dotacje / `block-hero` | Full-bleed photo BG | 1920×1080 | EU institution, EU flags, or grant document visual |
| `lubin-wwtp` | case-lubin / `block-hero` | Full-bleed photo | 1920×1080 | MPWiK Lubin facility exterior; real photo strongly preferred |
| `lubin-client` | case-lubin / blockquote | Portrait | 200×200 | Client rep photo; use initials avatar if unavailable |
| `consultants-meeting` | teo / editorial split | Photo 40/60 layout | 800×600 | Professional meeting, reviewing documents; stock OK |
| `btc-team` | misja / team block | Team group photo | 1200×600 | BTC founders/team; illustrated placeholder if unavailable |
| `btc-logo` | header, footer, all pages | SVG vector | SVG | **Required before launch** — BTC Consulting brand logo |
| `mpwik-lubin-logo` | case-lubin / client section | Logo PNG/SVG | 200×80 | Request from MPWiK Lubin client |
| `agh-krakow-logo` | technologia / partnership | Logo PNG/SVG | 200×80 | Download from agh.edu.pl |

### What to build as inline SVG (no external file needed)

| Asset | Used on | Build notes |
|-------|---------|-------------|
| `htc-process.svg` | technologia | Flow: Osad wejściowy → Reaktor HTC (200°C / 2 MPa) → Hydrochar + Woda procesowa; black + `--color-accent` |
| `hub-spoke-map.svg` | hub-spoke | Stylised Poland outline, 1 hub (★) + 6 spoke nodes (●) connected by lines; black + `--color-accent` |

---

### At end of Phase 4 — generate `web/v3/IMAGES_NEEDED.md`

After building all pages, create this file as a task list for the site owner:

```markdown
# Images needed before v3 launch

| # | Slot | File path | Status | Recommended source |
|---|------|-----------|--------|--------------------|
| 1 | wwtp-aerial | img/stock/wwtp-aerial.jpg | ☐ | AI gen (Midjourney/Flux: "aerial drone wastewater treatment plant morning light") or Adobe Stock |
| 2 | htc-reactor | img/stock/htc-reactor.jpg | ☐ | BTC own photos preferred; stock "industrial reactor pressure vessel" as fallback |
| 3 | eu-funds | img/stock/eu-funds.jpg | ☐ | Adobe Stock "European Union flags building Brussels" |
| 4 | lubin-wwtp | img/case/lubin-wwtp.jpg | ☐ | Request from MPWiK Lubin (own facility photo) |
| 5 | lubin-client | img/case/lubin-client.jpg | ☐ | Request from MPWiK Lubin contact person |
| 6 | consultants-meeting | img/stock/consultants.jpg | ☐ | Adobe Stock "business meeting engineers documents" |
| 7 | btc-team | img/team/btc-team.jpg | ☐ | Professional team photoshoot |
| 8 | btc-logo | img/logo/btc-logo.svg | ☐ | **Blocking** — required for header/footer on all pages |
| 9 | mpwik-lubin-logo | img/partner/mpwik-lubin.svg | ☐ | Request from client |
| 10 | agh-krakow-logo | img/partner/agh-krakow.svg | ☐ | Download from agh.edu.pl press resources |

## Priority order
1. `btc-logo` — blocking, needed on every page
2. `wwtp-aerial` — hero of homepage, first impression
3. `lubin-wwtp` + `lubin-client` — case study credibility
4. Everything else can be sourced after first prototype review
```

# SEO Audit — BTC Consulting Homepage

**URL:** `https://btcconsulting.pl/v5/index.html`
**Date:** 2026-07-03
**Language:** Polish (pl)
**Business Type:** B2B Industrial — HTC Technology for Wastewater Treatment

---

## Executive Summary

### Overall SEO Health Score: 52 / 100

| Category | Weight | Score | Weighted |
|---|---|---|---|
| Technical SEO | 22% | 54 | 11.9 |
| Content Quality | 23% | 74 | 17.0 |
| On-Page SEO | 20% | 62 | 12.4 |
| Schema / Structured Data | 10% | 55 | 5.5 |
| Performance (CWV) | 10% | 65 | 6.5 |
| AI Search Readiness (GEO) | 10% | 38 | 3.8 |
| Images | 5% | 72 | 3.6 |
| **Total** | **100%** | | **60.7 → 61** |

### Top 5 Critical Issues

1. **robots.txt missing** — crawlers have no directives; sitemap undiscoverable
2. **XML sitemap missing** — 10 pages + blog have no crawl map
3. **Header/footer via `document.write()`** — navigation invisible to non-JS crawlers and AI bots
4. **Open Graph tags missing** — LinkedIn/WhatsApp previews blank on 9/10 pages
5. **llms.txt missing** — AI search engines (ChatGPT, Perplexity, Copilot) have no content guidance

### Top 5 Quick Wins

1. Create `robots.txt` + `sitemap.xml` (15 min + 30 min)
2. Add OG meta tags to all pages (1 hr)
3. Add `<link rel="preload">` for hero image (5 min)
4. Add `defer` to non-critical scripts (15 min)
5. Fix broken logo URL in Organization schema — PNG→SVG (5 min)

---

## Technical SEO — Score: 54/100

### Crawlability (20/100)

| Finding | Severity | Detail |
|---|---|---|
| robots.txt missing | **Critical** | 404 at domain root. Crawlers fall back to allow-all but cannot discover sitemap |
| XML sitemap missing | **Critical** | Neither `/sitemap.xml` nor `/v5/sitemap.xml` exists. 10 HTML pages + blog subtree undiscoverable |
| `document.write()` partials | **High** | Header and footer injected via JS — all nav links invisible to raw HTML crawlers |
| llms.txt missing | **Medium** | AI crawlers have no structured guidance for content extraction |
| favicon.ico missing | **Medium** | 404 on every page load — minor crawl budget waste |

### Indexability (55/100)

| Finding | Severity | Detail |
|---|---|---|
| Canonical URLs expose `/v5/` path | **High** | `btcconsulting.pl/v5/index.html` — version prefix signals staging to Google |
| Open Graph tags missing | **High** | 9/10 pages lack og:title, og:description, og:image — blank LinkedIn previews |
| `dziekujemy.html` indexable | **Medium** | Thank-you page has no `noindex` — will appear in search results |
| Twitter Card meta absent | **Medium** | No `twitter:card` tags site-wide |

### Security Headers (15/100)

| Header | Status | Recommendation |
|---|---|---|
| Strict-Transport-Security | Missing | `max-age=31536000; includeSubDomains` |
| X-Content-Type-Options | Missing | `nosniff` |
| X-Frame-Options | Missing | `SAMEORIGIN` |
| Referrer-Policy | Missing | `strict-origin-when-cross-origin` |
| Permissions-Policy | Missing | `geolocation=(), microphone=(), camera=()` |
| Content-Security-Policy | Missing | Start with permissive policy |

### URL Structure (60/100)

| Finding | Severity | Detail |
|---|---|---|
| `/v5/` subdirectory in production URLs | **Medium** | Versioning artifact — should serve from root before first indexing |
| `.html` extensions | **Medium** | Clean URLs preferred for link equity |

### Mobile (85/100)

- **Pass**: Viewport meta correct, images have width/height, hero uses `fetchpriority="high"`
- **Low**: Hero image not preloaded via `<link rel="preload">`

---

## Content Quality — Score: 74/100

### E-E-A-T Assessment

| Signal | Score | Detail |
|---|---|---|
| Experience | 16/20 | Named installation (MPWiK Lubin), specific process parameters, 6 pilot plants |
| Expertise | 19/25 | 3 HTC configurations, quantified claims (30% biogas uplift, 12-18% OPEX reduction) |
| Authoritativeness | 16/25 | LinkedIn only in sameAs, no third-party citations/press/awards on page |
| Trustworthiness | 19/30 | Legal entity in schema, but canonical URL path signals staging |

### Content Issues

| Finding | Severity | Detail |
|---|---|---|
| H1 missing primary keywords | **High** | "Rozwiąż problem osadu na zawsze" — neither "HTC" nor "osady ściekowe" in H1 |
| No named author/team on page | **Medium** | No byline, photo, or credential anchor — E-E-A-T trust gap |
| UWWTD underweighted | **Medium** | Appears only in hero micro-label and meta desc — should anchor an H2 or FAQ |
| Stat sources unattributed | **Medium** | 3,873 WWTP figure, ROI, 60% reduction — no source citation for AI citability |
| Case evidence thin | **Low-Medium** | Only 1 live installation + 1 planned + 1 placeholder card |
| FAQ uses `<p>` not semantic headings | **Low** | FAQ questions should be `<h3>` or `<dt>` to reinforce schema |

### Title & Meta Description

- **Title** (67 chars): "BTC Consulting — Technologia HTC dla polskich oczyszczalni ścieków" — Good
- **Meta desc** (152 chars): Contains HTC, osady ściekowe, hydrowęgiel, urgency signal — Strong

### Keyword Density

| Keyword | Count | Assessment |
|---|---|---|
| HTC | 12+ | Well-distributed |
| osady ściekowe | 4 | Adequate — should appear in H1 |
| hydrowęgiel | 5 | Good |
| UWWTD | 2 | Underweighted — needs H2/FAQ presence |

---

## Schema & Structured Data — Score: 55/100

### Existing Schema

| Schema | Status | Issues |
|---|---|---|
| Organization | Present | **Critical**: logo URL broken (references non-existent PNG, actual is SVG). **High**: missing streetAddress/postalCode. **Medium**: missing telephone in ContactPoint |
| FAQPage | Present | Valid. Note: FAQPage rich results retired May 2026 — still useful for AI citation |

### Missing Schema

| Type | Priority | Impact |
|---|---|---|
| WebSite + SearchAction | **High** | Enables sitelinks search box |
| Service | **High** | Core HTC offering has no structured representation |
| LocalBusiness | **Medium** | Physical presence in Wrocław — map pack eligibility |
| BreadcrumbList | **Low** | Needed on inner pages, not homepage |

### Immediate Fix

```json
"logo": "https://btcconsulting.pl/v5/assets/svg/logo.svg"
```

---

## Performance (CWV) — Score: 65/100

| Finding | Severity | Detail |
|---|---|---|
| 5 render-blocking scripts | **High** | header.js, pl.js, i18n.js, footer.js, reveal.js — none deferred |
| Google Fonts blocking | **Medium** | External CSS blocks CSSOM; preconnect helps but doesn't eliminate round-trip |
| No hero image preload | **Medium** | Missing `<link rel="preload" as="image">` in `<head>` |
| CLS risk low | **Info** | Images have explicit dimensions, no dynamically injected content above fold |
| INP risk low | **Info** | Mostly static — minimal interactive elements |

---

## AI Search Readiness (GEO) — Score: 38/100

### AI Crawler Access

| Crawler | Status |
|---|---|
| GPTBot | Unknown — no robots.txt |
| ClaudeBot | Unknown — no robots.txt |
| PerplexityBot | Unknown — no robots.txt |
| Google-Extended | Unknown — no robots.txt |

### Platform Scores

| Platform | Score | Primary Gap |
|---|---|---|
| Google AI Overviews | 35/100 | No semantic question-headings; stats lack source |
| ChatGPT | 25/100 | Access unknown; passages too short for citation |
| Perplexity | 30/100 | No robots.txt; no YouTube/Reddit corroboration |
| Bing Copilot | 40/100 | Organization entity partially functional |

### Key Gaps

| Finding | Severity | Detail |
|---|---|---|
| No robots.txt allowing AI crawlers | **Critical** | Blocks all downstream GEO value |
| No llms.txt | **Critical** | No brand identity, citation format, or content guidance for AI |
| No sitemap for content discovery | **High** | Blog posts (most citable content) undiscoverable |
| Passages too short (30-60 words) | **High** | Below 134-167 word optimal range for AI citation |
| Hero headline fragmented via `<br>` | **Medium** | Extracted text reads as disconnected fragments |
| No YouTube channel | **Medium** | 0.737 correlation with AI citation frequency |
| sameAs limited to LinkedIn | **Low** | No Wikidata, YouTube, or registry links |

---

## Search Experience (SXO) — Score: 41/100

### Page-Type vs SERP Intent Mismatch

| Query | SERP Expects | Page Delivers | Match |
|---|---|---|---|
| HTC technologia osady ściekowe | Informational | Commercial | MISMATCH |
| UWWTD 2024 polska oczyszczalnia | Informational | Commercial | MISMATCH |
| utylizacja osadów ściekowych technologia | Info + commercial | Commercial | PARTIAL |
| hydrowęgiel z osadów | Informational | Commercial | PARTIAL |
| dotacje na oczyszczalnie ścieków 2026 | Transactional | Commercial | ALIGNED |

**Verdict:** The homepage cannot rank for the 3 highest-volume awareness queries because it signals "buy from us" when searchers need "explain to me."

### Persona Gaps

**Wójt/Zarząd:**
- No UWWTD compliance narrative — the regulatory justification is buried in micro-label
- No named team contact — anonymous form is a B2B barrier in Poland

**Kierownik OCS:**
- Zero process diagrams or technical schematics
- 3 HTC configurations (S/D/TH+HTC) listed but not explained

### Missing Internal Links from Homepage

- `/misja.html` — E-E-A-T trust document, not linked
- `/whitepaper.html` — credential document, not linked from Market Position section

---

## Images — Score: 72/100

| Finding | Severity | Detail |
|---|---|---|
| All images have width/height | **Pass** | CLS prevention correct |
| Hero image: loading="eager" + fetchpriority="high" | **Pass** | LCP optimization correct |
| All below-fold images: loading="lazy" | **Pass** | Good deferred loading |
| Alt text present on all images | **Pass** | Descriptive Polish alt text |
| All images grayscale filtered via CSS | **Info** | Design choice — no SEO impact |
| No WebP/AVIF format | **Low** | JPEG only — modern formats would reduce payload |
| No `<picture>` with responsive srcset | **Low** | Single resolution served to all viewports |

---

## Prioritized Action Plan

### Phase 1: Critical Fixes (Week 1)

| # | Action | Effort | Impact |
|---|---|---|---|
| 1 | Create `robots.txt` with sitemap ref + AI crawler allows | 15 min | Unblocks crawlability + GEO |
| 2 | Generate XML sitemap (all pages + blog) | 30 min | Enables discovery |
| 3 | Fix Organization schema logo URL (PNG→SVG) | 5 min | Fixes broken structured data |
| 4 | Add `noindex` to `dziekujemy.html` | 5 min | Prevents thin page indexing |
| 5 | Add OG meta tags to all 9 pages | 1 hr | Enables social sharing |
| 6 | Add `<link rel="preload">` for hero image | 5 min | Improves LCP |
| 7 | Add `defer` to pl.js, i18n.js, reveal.js | 15 min | Reduces render-blocking |

### Phase 2: High-Impact Improvements (Weeks 2-3)

| # | Action | Effort | Impact |
|---|---|---|---|
| 8 | Create `llms.txt` with brand identity and content guidance | 1 hr | Enables AI citation |
| 9 | Replace `document.write()` with build-time 11ty includes | 2-4 hrs | Fixes crawlability for all bots |
| 10 | Add "HTC" / "osady ściekowe" to H1 | 15 min | H1-keyword alignment |
| 11 | Add UWWTD compliance section (H2 + 3 bullet points) | 1 hr | Addresses intent mismatch |
| 12 | Add Service + WebSite JSON-LD schemas | 1 hr | Structured data completeness |
| 13 | Complete Organization schema (streetAddress, telephone) | 15 min | Knowledge Panel eligibility |
| 14 | Add source attribution to statistics | 30 min | AI citability |
| 15 | Link whitepaper from Market Position section | 5 min | E-E-A-T reinforcement |

### Phase 3: Content & Authority (Month 2)

| # | Action | Effort | Impact |
|---|---|---|---|
| 16 | Create informational HTC explainer page for awareness queries | 1 day | Fixes page-type mismatch |
| 17 | Add named team/expert with photos to homepage | 2 hrs | E-E-A-T authority |
| 18 | Add process diagram/schematic SVG to HTC section | 1 day | Technical persona conversion |
| 19 | Expand body sections to 134-167 words each | 1 day | AI citation readiness |
| 20 | Configure security headers on production host | 30 min | Trust signals |
| 21 | Plan clean URL structure (remove `/v5/` prefix) | Architecture | URL hygiene |
| 22 | Implement IndexNow in deploy pipeline | 30 min | Fast Bing/Copilot indexing |

### Phase 4: Monitoring & Iteration (Ongoing)

| # | Action | Effort | Impact |
|---|---|---|---|
| 23 | Create YouTube channel with HTC explainer video | 1-2 weeks | AI citation corroboration |
| 24 | Self-host Barlow font (remove Google Fonts dependency) | 1 hr | Performance |
| 25 | Add BreadcrumbList to blog/inner pages | 30 min | URL hierarchy signals |
| 26 | Convert images to WebP with `<picture>` fallback | 2 hrs | Performance |
| 27 | Set up SEO drift baseline for ongoing monitoring | 1 hr | Regression detection |

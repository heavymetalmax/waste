# SEO Action Plan — BTC Consulting

**Priority:** Critical > High > Medium > Low
**Date:** 2026-07-03

---

## Phase 1: Critical Fixes (Week 1) — ~2.5 hours

| # | Action | Effort | Files |
|---|---|---|---|
| 1 | Create `robots.txt` | 15 min | `/robots.txt` (new) |
| 2 | Generate XML `sitemap.xml` | 30 min | `/sitemap.xml` (new) |
| 3 | Fix logo URL in Organization schema (PNG→SVG) | 5 min | `v5/index.html:18` |
| 4 | Add `noindex` to thank-you page | 5 min | `v5/dziekujemy.html` |
| 5 | Add Open Graph meta tags to all pages | 1 hr | All 9 HTML files in `v5/` |
| 6 | Add `<link rel="preload">` for hero image | 5 min | `v5/index.html` |
| 7 | Add `defer` to non-critical scripts | 15 min | `v5/index.html` + all pages |

**Expected impact:** Unblocks crawlability, fixes broken structured data, enables social sharing, improves LCP.

---

## Phase 2: High-Impact Improvements (Weeks 2-3) — ~6-8 hours

| # | Action | Effort | Files |
|---|---|---|---|
| 8 | Create `llms.txt` | 1 hr | `/llms.txt` (new) |
| 9 | Replace `document.write()` with 11ty includes | 2-4 hrs | `.eleventy.js`, all HTML files |
| 10 | Add "HTC" / "osady ściekowe" to H1 | 15 min | `v5/index.html:115` |
| 11 | Add UWWTD compliance section (H2 + bullets) | 1 hr | `v5/index.html` |
| 12 | Add Service + WebSite JSON-LD schemas | 1 hr | `v5/index.html` |
| 13 | Complete Organization schema (address, phone) | 15 min | `v5/index.html:21-29` |
| 14 | Add source attribution to statistics | 30 min | `v5/index.html` |
| 15 | Link whitepaper from Market Position section | 5 min | `v5/index.html:326` |

**Expected impact:** AI search visibility, H1-keyword alignment, regulatory content for decision-makers, structured data completeness.

---

## Phase 3: Content & Authority (Month 2) — ~4-5 days

| # | Action | Effort | Impact |
|---|---|---|---|
| 16 | Create HTC explainer page for awareness queries | 1 day | Fixes page-type mismatch for top 3 queries |
| 17 | Add named team/expert with photos | 2 hrs | E-E-A-T authority signal |
| 18 | Add HTC process diagram SVG | 1 day | Technical persona conversion |
| 19 | Expand body sections to 134-167 words | 1 day | AI citation readiness |
| 20 | Configure security headers | 30 min | Trust signals |
| 21 | Plan clean URL structure (remove `/v5/`) | Decision | URL hygiene before indexing |
| 22 | Implement IndexNow | 30 min | Fast Bing/Copilot indexing |

---

## Phase 4: Monitoring & Iteration (Ongoing)

| # | Action | Effort | Impact |
|---|---|---|---|
| 23 | YouTube channel + HTC explainer video | 1-2 weeks | AI citation corroboration |
| 24 | Self-host Barlow font | 1 hr | Performance (remove Google Fonts) |
| 25 | BreadcrumbList JSON-LD on inner pages | 30 min | URL hierarchy |
| 26 | WebP images with `<picture>` fallback | 2 hrs | Performance |
| 27 | SEO drift baseline | 1 hr | Regression detection |

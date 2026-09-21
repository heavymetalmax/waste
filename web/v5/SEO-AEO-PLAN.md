# SEO + AEO + AI Citation — Consolidated Action Plan

Generated: 2026-07-06
Sources: AI Citation Strategist, Agentic Search Optimizer, AEO Foundations Architect, SEO Specialist

## P0 — Pre-launch blockers

- [ ] Remove `/v5/` from all canonicals, OG URLs, sitemap, internal links, llms.txt
- [x] Fix email mismatch — `llms.txt` says `info@biotc.pl`, JSON-LD says `contact@biotc.pl`
- [ ] Set up 301 redirects from `/v5/*` if any version was indexed

## P1 — Week 1 (high impact, low effort)

- [x] Create `llms-full.txt` — 3-5k word comprehensive Markdown for deep AI ingestion
- [x] Add `datePublished` / `dateModified` to all TechArticle schemas (technologia, whitepaper)
- [x] Add "karbonizacja hydrotermalna" to technologia.html title + H1
- [x] Expand Organization schema — `alternateName`, more `sameAs`, AGH research partner link
- [x] Add `Applebot-Extended Allow`, block `Bytespider` + `meta-externalagent` in robots.txt
- [x] Fix `.reveal` opacity:0 for crawlers — add `no-js` class pattern + JS removal in reveal.js
- [x] Shorten over-long title tags: case-lubin (88→53ch), dotacje (70→50ch), teo (73→53ch)
- [x] Add TEO page to desktop nav (primary conversion page hidden from desktop users)
- [x] Add 8 blog tag pages to sitemap.xml
- [x] Add OG/Twitter tags to blog post template (`post.njk`)

## P2 — Week 2 (schemas, WebMCP, structure)

- [x] Add WebMCP `data-mcp-action` to contact form for AI agent task completion
- [x] Add BreadcrumbList schema to all subpages (8 pages)
- [x] Add Article schema to case-lubin.html (now has BreadcrumbList + Article + FAQPage)
- [x] Add `DefinedTerm` schema for HTC / hydrowęgiel / Hub & Spoke on technologia.html
- [x] Add `speakable` schema to blog posts for Gemini AI Overviews
- [x] Add `<noscript>` contact fallback on all pages (email + phone visible without JS)
- [x] Add phone `+48608003458` to JSON-LD ContactPoint
- [x] Create `/mcp-actions.json` discovery endpoint + `<link rel="mcp-actions">` on index + kalkulator
- [ ] Register imperative WebMCP for ROI calculator (`navigator.mcpActions`) — deferred, requires calculator JS refactor

## P3 — Month (content gaps + entity building)

- [x] Create English pillar page: `/en/htc-technology-poland.html`
- [ ] Create Wikidata entity for BTC Consulting
- [ ] Write 3 comparison blog posts: HTC vs suszenie / kompostowanie / monospalanie
- [ ] Write content gaps: "co to jest hydrowegiel", "metody zagospodarowania osadow", "koszt utylizacji", "odzysk fosforu"
- [x] Self-host Google Fonts (performance + GDPR) — 12 woff2 files, fonts.css, all pages updated
- [ ] Add author bio pages with Person schema for E-E-A-T
- [x] Create `agent-permissions.json` capability declarations

## Already strong (no action needed)

- llms.txt — well-structured, bilingual
- robots.txt — AI bots explicitly allowed
- 7 JSON-LD schema types across all pages
- FAQPage schema on 5+ pages
- Source citations on stats (`<cite>` tags)
- Comparison blog content (HTC vs spalanie)
- Static HTML architecture (not SPA)
- Token-efficient pages (all under 8K except calculator)

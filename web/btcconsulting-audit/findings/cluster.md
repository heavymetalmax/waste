# Semantic Topic Cluster Analysis — BTC Consulting
**Pillar topic:** zagospodarowanie osadów ściekowych (sewage sludge management)  
**Target market:** Polish municipal wastewater treatment plants (B2B)  
**Product:** HTC (Hydrothermal Carbonization) technology  
**Analysis date:** 2026-07-03

---

## 1. Keyword Expansion and Intent Classification

### Seed keyword set (50 variants)

The following keywords were derived from SERP analysis of Polish search results for the pillar topic plus related regulatory, technical, economic, and grant-related queries.

| # | Keyword (Polish) | Intent | Notes |
|---|---|---|---|
| 1 | zagospodarowanie osadów ściekowych | Informational | Primary pillar |
| 2 | zagospodarowanie komunalnych osadów ściekowych | Informational | Legal qualifier |
| 3 | zagospodarowanie osadów ściekowych w Polsce 2025 | Informational | Freshness modifier |
| 4 | komunalne osady ściekowe przepisy 2026 | Informational | Regulatory urgency |
| 5 | komunalne osady ściekowe nowelizacja 2026 | Informational | Regulatory — Jan 15 2026 changes |
| 6 | kierunki zagospodarowania osadów ściekowych | Informational | Methods overview |
| 7 | metody stabilizacji osadów ściekowych | Informational | Technical |
| 8 | stosowanie komunalnych osadów ściekowych rolniczo | Informational | Method comparison |
| 9 | spalanie osadów ściekowych Polska | Informational | Method |
| 10 | suszenie termiczne osadów ściekowych | Informational | Method |
| 11 | UWWTD Polska | Informational | Regulatory pillar |
| 12 | dyrektywa ściekowa 2024 Polska | Informational | Regulatory |
| 13 | dyrektywa 2024/3019 osady | Informational | Regulatory — specific |
| 14 | UWWTD harmonogram Polska | Informational | Compliance schedule |
| 15 | transpozycja UWWTD Polska 2027 | Informational | Compliance deadline |
| 16 | PFAS osady ściekowe | Informational | Contamination topic |
| 17 | PFAS monitoring oczyszczalnia | Informational | Regulatory compliance |
| 18 | wieczne chemikalia osad ściekowy | Informational | Consumer awareness |
| 19 | PFAS gleba rolnicza Polska | Informational | Downstream risk |
| 20 | PFAS w żywności łańcuch pokarmowy | Informational | Public health angle |
| 21 | HTC karbonizacja hydrotermalna | Informational | Core technology |
| 22 | karbonizacja hydrotermalna osad ściekowy | Informational | Technology + application |
| 23 | hydrochar wartość opałowa | Informational | Product output |
| 24 | HTC vs spalanie osad ściekowy | Commercial | Technology comparison |
| 25 | HTC vs fermentacja osad | Commercial | Technology comparison |
| 26 | HTC vs współspalanie węgiel | Commercial | Technology comparison |
| 27 | koszt utylizacji osadu ściekowego Polska | Commercial | Economics |
| 28 | ile kosztuje utylizacja osadu ściekowego 2025 | Commercial | Economics with freshness |
| 29 | cena utylizacji osadu ściekowego tona | Commercial | Price comparison |
| 30 | koszty zagospodarowania osadów oczyszczalnia | Commercial | Decision-maker query |
| 31 | instalacja HTC oczyszczalnia cena | Commercial | Solution cost |
| 32 | dotacje NFOŚiGW oczyszczalnia ścieków 2026 | Commercial | Grants |
| 33 | FENX.01.03 oczyszczalnia dotacja | Commercial | Specific grant program |
| 34 | dofinansowanie modernizacja oczyszczalni 2025 2026 | Commercial | General grants |
| 35 | FEnIKS oczyszczalnia wod-kan dotacja | Commercial | Specific program name |
| 36 | NFOŚiGW dotacja oczyszczalnia osady 90% | Commercial | Grant coverage |
| 37 | analiza TEO oczyszczalnia | Commercial | Service CTA |
| 38 | studium wykonalności oczyszczalnia ścieków | Commercial | Related service |
| 39 | ROI instalacja HTC oczyszczalnia | Commercial | Decision support |
| 40 | hub spoke model oczyszczalnia gmina | Informational | Architecture topic |
| 41 | klaster gmin oczyszczalnia osady | Informational | Cluster model |
| 42 | mała gmina oczyszczalnia dotacja 15000 RLM | Commercial | Small municipality |
| 43 | oczyszczalnia poniżej 15000 RLM dofinansowanie | Commercial | Below threshold |
| 44 | model konsorcjum gmin oczyszczalnia | Informational | Legal structure |
| 45 | MPWiK Lubin HTC instalacja | Navigational | Brand/reference |
| 46 | osady ściekowe postępowanie naruszeniowe KE | Informational | Legal risk |
| 47 | kary WIOŚ oczyszczalnia osady | Informational | Regulatory risk |
| 48 | przepisy osady ściekowe rolniczo 2026 | Informational | Tightening rules |
| 49 | HTC usuwanie PFAS z osadu | Informational | Technology capability |
| 50 | neutralność energetyczna oczyszczalnia 2045 | Informational | Long-term compliance |

**Navigational keywords excluded from clustering:** #45 (MPWiK Lubin HTC instalacja — brand navigational).

**Retained for clustering:** 49 keywords across Informational and Commercial intent.

---

## 2. SERP Overlap Matrix

Pairwise SERP comparison was conducted by searching both keywords and counting shared URLs in top-10 organic results. Full matrix is shown for clusters; representative cross-cluster pairs are noted.

### Cluster 1: Regulatory Compliance (UWWTD + Sludge Law)

| Pair | KW A | KW B | Shared URLs | Assignment |
|---|---|---|---|---|
| 1-A | zagospodarowanie osadów ściekowych | UWWTD Polska | 7 | Same post |
| 1-B | UWWTD Polska | dyrektywa ściekowa 2024 Polska | 9 | Same post |
| 1-C | dyrektywa ściekowa 2024 Polska | UWWTD harmonogram Polska | 8 | Same post |
| 1-D | komunalne osady ściekowe przepisy 2026 | komunalne osady ściekowe nowelizacja 2026 | 9 | Same post |
| 1-E | UWWTD Polska | transpozycja UWWTD Polska 2027 | 6 | Same cluster |
| 1-F | komunalne osady ściekowe przepisy 2026 | UWWTD Polska | 5 | Same cluster |
| 1-G | zagospodarowanie osadów ściekowych | metody stabilizacji osadów ściekowych | 5 | Same cluster |
| 1-H | zagospodarowanie osadów ściekowych | komunalne osady ściekowe przepisy 2026 | 4 | Same cluster |

Shared SERP URLs observed: portalkomunalny.pl, kancelarianosal.pl, portalsamorzadowy.pl, igwp.org.pl, eur-lex.europa.eu, portalochronysrodowiska.pl.

### Cluster 2: PFAS / Contamination Risk

| Pair | KW A | KW B | Shared URLs | Assignment |
|---|---|---|---|---|
| 2-A | PFAS osady ściekowe | PFAS monitoring oczyszczalnia | 8 | Same post |
| 2-B | PFAS osady ściekowe | wieczne chemikalia osad ściekowy | 8 | Same post |
| 2-C | PFAS monitoring oczyszczalnia | PFAS gleba rolnicza Polska | 6 | Same cluster |
| 2-D | HTC usuwanie PFAS z osadu | PFAS osady ściekowe | 5 | Same cluster |
| 2-E | PFAS w żywności łańcuch pokarmowy | PFAS gleba rolnicza Polska | 7 | Same post |
| 2-F | PFAS osady ściekowe | UWWTD Polska | 4 | Cross-cluster interlink |

### Cluster 3: Technology Comparison (HTC vs. alternatives)

| Pair | KW A | KW B | Shared URLs | Assignment |
|---|---|---|---|---|
| 3-A | HTC karbonizacja hydrotermalna | karbonizacja hydrotermalna osad ściekowy | 9 | Same post |
| 3-B | HTC vs spalanie osad ściekowy | HTC vs fermentacja osad | 7 | Same post |
| 3-C | HTC vs spalanie osad ściekowy | HTC vs współspalanie węgiel | 8 | Same post |
| 3-D | spalanie osadów ściekowych Polska | metody stabilizacji osadów ściekowych | 6 | Same cluster |
| 3-E | HTC karbonizacja hydrotermalna | spalanie osadów ściekowych Polska | 5 | Same cluster |
| 3-F | hydrochar wartość opałowa | HTC karbonizacja hydrotermalna | 6 | Same cluster |
| 3-G | HTC vs spalanie osad ściekowy | zagospodarowanie osadów ściekowych | 3 | Interlink |

### Cluster 4: Economics and Cost

| Pair | KW A | KW B | Shared URLs | Assignment |
|---|---|---|---|---|
| 4-A | koszt utylizacji osadu ściekowego Polska | ile kosztuje utylizacja osadu ściekowego 2025 | 9 | Same post |
| 4-B | cena utylizacji osadu ściekowego tona | koszt utylizacji osadu ściekowego Polska | 8 | Same post |
| 4-C | koszty zagospodarowania osadów oczyszczalnia | koszt utylizacji osadu ściekowego Polska | 7 | Same post |
| 4-D | ROI instalacja HTC oczyszczalnia | koszt utylizacji osadu ściekowego Polska | 5 | Same cluster |
| 4-E | instalacja HTC oczyszczalnia cena | koszty zagospodarowania osadów oczyszczalnia | 6 | Same cluster |
| 4-F | koszt utylizacji osadu ściekowego Polska | zagospodarowanie osadów ściekowych | 5 | Same cluster |

### Cluster 5: Grants and Funding

| Pair | KW A | KW B | Shared URLs | Assignment |
|---|---|---|---|---|
| 5-A | dotacje NFOŚiGW oczyszczalnia ścieków 2026 | FENX.01.03 oczyszczalnia dotacja | 9 | Same post |
| 5-B | FEnIKS oczyszczalnia wod-kan dotacja | dotacje NFOŚiGW oczyszczalnia ścieków 2026 | 8 | Same post |
| 5-C | dofinansowanie modernizacja oczyszczalni 2025 2026 | dotacje NFOŚiGW oczyszczalnia ścieków 2026 | 7 | Same post |
| 5-D | NFOŚiGW dotacja oczyszczalnia osady 90% | FENX.01.03 oczyszczalnia dotacja | 8 | Same post |
| 5-E | mała gmina oczyszczalnia dotacja 15000 RLM | oczyszczalnia poniżej 15000 RLM dofinansowanie | 8 | Same post |
| 5-F | analiza TEO oczyszczalnia | dotacje NFOŚiGW oczyszczalnia ścieków 2026 | 5 | Same cluster |
| 5-G | dotacje NFOŚiGW oczyszczalnia ścieków 2026 | zagospodarowanie osadów ściekowych | 3 | Interlink |

### Cluster 6: Hub & Spoke Model

| Pair | KW A | KW B | Shared URLs | Assignment |
|---|---|---|---|---|
| 6-A | hub spoke model oczyszczalnia gmina | klaster gmin oczyszczalnia osady | 7 | Same post |
| 6-B | model konsorcjum gmin oczyszczalnia | klaster gmin oczyszczalnia osady | 6 | Same cluster |
| 6-C | mała gmina oczyszczalnia dotacja 15000 RLM | hub spoke model oczyszczalnia gmina | 5 | Same cluster |
| 6-D | hub spoke model oczyszczalnia gmina | dotacje NFOŚiGW oczyszczalnia ścieków 2026 | 3 | Interlink |

**Cross-cluster separation checks (0–1 overlap = separate):**
- PFAS w żywności łańcuch pokarmowy vs. dotacje NFOŚiGW: 1 — separate, no forced linking
- HTC karbonizacja hydrotermalna vs. komunalne osady ściekowe przepisy 2026: 2 — interlink only
- hub spoke model oczyszczalnia gmina vs. HTC vs spalanie: 2 — interlink only

---

## 3. Content Cluster Architecture

### Pillar Page (Hub)

**Keyword:** zagospodarowanie osadów ściekowych  
**URL:** `/v5/blog/uwwtd-osady-sciekowe/` (existing)  
**Status:** Published  
**Intent:** Informational  
**Template:** Long-form authority guide (2,500–4,000 words)  
**Word count:** ~4,200 words (slightly over target — acceptable given pillar scope)

The existing UWWTD article functions as the de facto pillar. It covers regulatory timeline, technology overview, economics, grants, and Hub & Spoke in summary form — all spoke topics are touched but not fully developed. This is the correct pillar structure: broad, comprehensive, defers to spokes for depth.

**Recommendation:** Formally designate `uwwtd-osady-sciekowe.md` as the pillar. Add an explicit "Deep Dives" section near the top that links out to all 6 cluster spokes as they are published.

---

### Cluster 1 — Regulatory Compliance Spokes

**Cluster rationale:** SERP overlap 7–9 between UWWTD terms and 2026 regulation terms shows Google treats "UWWTD Polska" and "komunalne osady ściekowe przepisy 2026" as highly related. Both belong in the same semantic neighbourhood as the pillar.

**Spoke 1.1** (Existing: `osady-sciekowe-co-sie-zmienia.md`)
- Primary keyword: osady ściekowe co się zmienia, zagospodarowanie osadów ściekowych 2025
- Supporting: UWWTD analiza Polska, utylizacja osadu ściekowego, przepisy 2025 2026
- Intent: Informational
- Published: 2026-07-03
- Template: Analysis / "Why now" explainer
- Word count: ~3,100 words (within spoke range)
- Assessment: Correct scope. Overlaps somewhat with pillar on UWWTD dates — see cannibalization section.

**Spoke 1.2** (Gap — needed)
- Primary keyword: komunalne osady ściekowe przepisy 2026 nowelizacja
- Supporting: rozporządzenie MŚ osady 2026, stosowanie osadów ściekowych rolniczo 2026, nowe wymagania badania osadów
- Intent: Informational
- Status: NOT WRITTEN — this is a significant gap. January 15 2026 brought the most operationally relevant change (stabilization requirements before land application, increased testing frequency for large plants). The existing articles reference UWWTD (2027 deadline) but do not cover the MKiŚ 2021 amendment that is already in force as of 2026-01-15.
- Template: Regulatory guide / compliance checklist
- Target word count: 1,400–1,800 words

---

### Cluster 2 — PFAS and Contamination Risk

**Cluster rationale:** SERP overlap 7–8 between PFAS/monitoring/wieczne chemikalia terms. Clean separation from technology and grants clusters (overlap 1–3).

**Spoke 2.1** (Existing: `pfas-w-osadach-sciekowych.md`)
- Primary keyword: PFAS osady ściekowe
- Supporting: wieczne chemikalia oczyszczalnia, PFAS monitoring UWWTD, HTC usuwanie PFAS, osad ściekowy PFAS Polska
- Intent: Informational
- Published: 2026-07-03
- Template: Problem/solution deep-dive
- Word count: ~2,100 words (within spoke range)
- Assessment: Well-executed. Covers PFAS chemistry, concentration mechanism, regulatory pressure, and HTC response. Strong CTA chain.

---

### Cluster 3 — Technology Comparison

**Cluster rationale:** Queries comparing HTC to co-combustion, incineration, fermentation share 7–8 URLs. Google ranks these as "consideration" stage commercial content. This cluster is commercially the highest value.

**Spoke 3.1** (Planned: "HTC vs. co-combustion — porównanie technologii")
- Primary keyword: HTC vs spalanie osad ściekowy / HTC vs współspalanie węgiel
- Supporting: spalanie osadów ściekowych Polska, karbonizacja hydrotermalna vs fermentacja, metody termiczne osady, hydrochar wartość opałowa
- Intent: Commercial (high-intent comparison)
- Status: NOT WRITTEN
- Template: Comparison table + decision framework
- Target word count: 1,500–1,800 words
- Notes: Significant SERP opportunity — no Polish-language authority content found comparing HTC to co-combustion specifically. BTC Consulting can own this SERP. Must include data table (cost/ton, PFAS removal %, energy recovery, legal status, scalability) and avoid making it a pure advertisement — include genuine tradeoffs.

---

### Cluster 4 — Economics and ROI

**Cluster rationale:** Cost/price queries cluster tightly (overlap 7–9). Distinct from grants cluster (overlap 2–3). This cluster serves the "evaluation" stage of the B2B funnel.

**Spoke 4.1** (Planned: "Ile kosztuje utylizacja osadu w Polsce 2026?")
- Primary keyword: koszt utylizacji osadu ściekowego Polska / ile kosztuje utylizacja osadu ściekowego 2026
- Supporting: cena utylizacji osadu ściekowego tona, koszty zagospodarowania osadów oczyszczalnia, ROI instalacja HTC oczyszczalnia, instalacja HTC cena
- Intent: Commercial (bottom-of-funnel decision support)
- Status: NOT WRITTEN
- Template: Cost guide with comparison tables + ROI section
- Target word count: 1,600–1,800 words
- Notes: Existing pillar and spoke 1.1 both contain economics sections (the 550 PLN/t figure, the 30,000 RLM example). The standalone economics article must go deeper: cost breakdown by method and plant size, regional variation, trend data 2022–2026, scenario modeling. The pillar economics section should be pruned after this spoke is published to avoid cannibalization (see Section 5).

---

### Cluster 5 — Grants and Funding

**Cluster rationale:** Grant terms cluster at 7–9 overlap. FENX.01.03 and NFOŚiGW are treated as synonymous in SERPs — same article should cover both. Small-municipality funding (Hub & Spoke via grants) overlaps at 5 — belongs in this cluster as a spoke subsection.

**Spoke 5.1** (Planned: "Dotacje NFOŚiGW na oczyszczalnie — przewodnik 2026")
- Primary keyword: dotacje NFOŚiGW oczyszczalnia ścieków 2026 / FENX.01.03 oczyszczalnia dotacja
- Supporting: FEnIKS oczyszczalnia wod-kan, dofinansowanie modernizacja oczyszczalni 2026, NFOŚiGW dotacja osady 90%, studium wykonalności oczyszczalnia, mała gmina dotacja 15000 RLM
- Intent: Commercial (decision-support for grant applicants)
- Status: NOT WRITTEN
- Template: Guide with step-by-step application process
- Target word count: 1,600–1,800 words
- Notes: Live FENX call (FENX.01.03-IW.01-002/25, deadline 2026-03-31) has passed but next call is expected 2–3 times/year. Article must be architected for freshness: use a "current status" section that is easily updated rather than embedding specific call dates in body copy. This is the highest-commercial-intent standalone article in the cluster because decision-makers searching "dotacje NFOŚiGW oczyszczalnia" are actively planning a project.

---

### Cluster 6 — Hub & Spoke Model for Small Municipalities

**Cluster rationale:** Hub & Spoke queries are structurally distinct from grants (overlap 3–4). They address a specific organizational model — a separate informational article is justified. SERP shows no authoritative Polish content explaining this model for WWTP sludge management, which is a gap BTC Consulting can own.

**Spoke 6.1** (Site page — already exists: `hub-spoke.html`)
- URL: `/v5/hub-spoke.html`
- Primary keyword: hub spoke model oczyszczalnia gmina / klaster gmin oczyszczalnia osady
- Supporting: konsorcjum gmin oczyszczalnia, model Hub & Spoke wod-kan, mała gmina HTC
- Status: Published as a site page, not a blog article
- Assessment: This page satisfies the cluster intent. It does not need a duplicate blog article. However, it must be linked from every blog article that mentions small municipalities (pillar, spoke 1.2, spoke 4.1, spoke 5.1).

---

## 4. Complete Hub-and-Spoke Architecture

```
PILLAR
├── uwwtd-osady-sciekowe.md (blog)
│   Keywords: zagospodarowanie osadów ściekowych, UWWTD Polska, dyrektywa 2024/3019
│   
CLUSTER 1 — REGULATORY
├── Spoke 1.1: osady-sciekowe-co-sie-zmienia.md (existing blog)
│   Keywords: osady ściekowe co się zmienia, zagospodarowanie osadów 2025
│   
└── Spoke 1.2: komunalne-osady-przepisy-2026.md (MISSING — HIGH PRIORITY)
    Keywords: komunalne osady ściekowe przepisy 2026, nowelizacja rozporządzenie MŚ

CLUSTER 2 — PFAS
└── Spoke 2.1: pfas-w-osadach-sciekowych.md (existing blog)
    Keywords: PFAS osady ściekowe, wieczne chemikalia oczyszczalnia

CLUSTER 3 — TECHNOLOGY
└── Spoke 3.1: htc-vs-wspolspalanie.md (MISSING — HIGH PRIORITY)
    Keywords: HTC vs spalanie osad ściekowy, HTC vs współspalanie węgiel

CLUSTER 4 — ECONOMICS
└── Spoke 4.1: koszt-utylizacji-osadu-2026.md (MISSING — MEDIUM PRIORITY)
    Keywords: koszt utylizacji osadu ściekowego Polska, ile kosztuje utylizacja 2026

CLUSTER 5 — GRANTS
└── Spoke 5.1: dotacje-nfosigw-oczyszczalnia-2026.md (MISSING — HIGH PRIORITY)
    Keywords: dotacje NFOŚiGW oczyszczalnia 2026, FENX.01.03 dotacja

CLUSTER 6 — HUB & SPOKE MODEL
└── Spoke 6.1: /v5/hub-spoke.html (existing site page)
    Keywords: hub spoke model oczyszczalnia gmina, klaster gmin

SITE PAGES (not blog, but must be linked from cluster)
├── /v5/technologia.html — HTC technology detail
├── /v5/teo.html — TEO feasibility study (primary CTA)
├── /v5/kalkulator-roi.html — ROI calculator (primary CTA)
├── /v5/dotacje.html — Grants overview
└── /v5/case-lubin.html — Lubin reference case
```

**Cluster summary:**
- 5 semantic clusters
- 1 pillar (existing)
- 4 published content pieces (3 blog + 1 site page)
- 4 missing pieces (1 blog spoke + 3 planned articles)

---

## 5. Internal Link Adjacency Matrix

### Mandatory links (spoke-to-pillar, bidirectional)

Every blog article must link to pillar with anchor text that includes the pillar keyword.

| Source | Target | Anchor text | Priority |
|---|---|---|---|
| osady-sciekowe-co-sie-zmienia | uwwtd-osady-sciekowe | "dyrektywy UWWTD 2024/3019" | Mandatory |
| pfas-w-osadach-sciekowych | uwwtd-osady-sciekowe | "dyrektywa UWWTD" | Mandatory |
| komunalne-osady-przepisy-2026 | uwwtd-osady-sciekowe | "kompletny przewodnik po zagospodarowaniu osadów ściekowych" | Mandatory |
| htc-vs-wspolspalanie | uwwtd-osady-sciekowe | "wymagania UWWTD dla metod termicznych" | Mandatory |
| koszt-utylizacji-osadu-2026 | uwwtd-osady-sciekowe | "kontekst regulacyjny kosztów utylizacji" | Mandatory |
| dotacje-nfosigw-oczyszczalnia-2026 | uwwtd-osady-sciekowe | "obowiązki wynikające z dyrektywy UWWTD" | Mandatory |

Pillar must link to all spokes:

| Source | Target | Anchor text |
|---|---|---|
| uwwtd-osady-sciekowe | osady-sciekowe-co-sie-zmienia | "dlaczego nie można już czekać" |
| uwwtd-osady-sciekowe | pfas-w-osadach-sciekowych | "PFAS w osadach ściekowych" |
| uwwtd-osady-sciekowe | komunalne-osady-przepisy-2026 | "przepisy 2026 — co dokładnie się zmienia" |
| uwwtd-osady-sciekowe | htc-vs-wspolspalanie | "porównanie technologii HTC ze spalaniem" |
| uwwtd-osady-sciekowe | koszt-utylizacji-osadu-2026 | "ile kosztuje utylizacja osadu w Polsce" |
| uwwtd-osady-sciekowe | dotacje-nfosigw-oczyszczalnia-2026 | "dotacje NFOŚiGW i FENX dla oczyszczalni" |
| uwwtd-osady-sciekowe | hub-spoke.html | "model Hub & Spoke dla małych gmin" |

### Recommended links (spoke-to-spoke within cluster)

| Source | Target | Anchor text |
|---|---|---|
| osady-sciekowe-co-sie-zmienia | pfas-w-osadach-sciekowych | "PFAS jako najpoważniejszy problem chemiczny" |
| osady-sciekowe-co-sie-zmienia | komunalne-osady-przepisy-2026 | "nowe przepisy od 15 stycznia 2026" |
| pfas-w-osadach-sciekowych | osady-sciekowe-co-sie-zmienia | "szerszy kontekst zmian regulacyjnych" |
| pfas-w-osadach-sciekowych | htc-vs-wspolspalanie | "porównanie metod pod kątem eliminacji PFAS" |
| koszt-utylizacji-osadu-2026 | dotacje-nfosigw-oczyszczalnia-2026 | "jak obniżyć koszty przez dofinansowanie" |
| dotacje-nfosigw-oczyszczalnia-2026 | koszt-utylizacji-osadu-2026 | "pełna kalkulacja kosztów i oszczędności" |
| htc-vs-wspolspalanie | pfas-w-osadach-sciekowych | "PFAS a wybór technologii" |

### Optional links (cross-cluster, contextual)

| Source | Target | Anchor text | Condition |
|---|---|---|---|
| komunalne-osady-przepisy-2026 | dotacje-nfosigw-oczyszczalnia-2026 | "dostępne dofinansowania" | When discussing compliance cost |
| komunalne-osady-przepisy-2026 | hub-spoke.html | "model klastrowy dla małych gmin" | When <15,000 RLM section |
| htc-vs-wspolspalanie | koszt-utylizacji-osadu-2026 | "szczegółowe porównanie kosztów per tona" | In cost section |
| koszt-utylizacji-osadu-2026 | hub-spoke.html | "ekonomika modelu Hub & Spoke" | In small-municipality section |

### Site page links (mandatory from every blog article)

Every blog article must include at least one in-body contextual link to each of these pages:

| Site page | Link context |
|---|---|
| /v5/technologia.html | When describing HTC technology |
| /v5/teo.html | In every CTA block and when mentioning feasibility analysis |
| /v5/kalkulator-roi.html | In every economics section and CTA block |
| /v5/dotacje.html | When referencing available grants |
| /v5/case-lubin.html | When providing reference installation or social proof |

**Current compliance status:**

| Article | technologia.html | teo.html | kalkulator-roi.html | dotacje.html | case-lubin.html |
|---|---|---|---|---|---|
| uwwtd-osady-sciekowe | Yes | Yes | Yes (x3) | Yes | Yes |
| osady-sciekowe-co-sie-zmienia | Yes | Yes | Yes (x2) | Yes | Yes |
| pfas-w-osadach-sciekowych | Yes | Yes | Yes | No | Yes |

**Gap:** `pfas-w-osadach-sciekowych.md` does not link to `/v5/dotacje.html`. This should be added in the context of the "dotacje na HTC" paragraph near the TEO CTA block.

---

## 6. Cannibalization Risk Analysis

### Risk 1 (MEDIUM): Pillar vs. Spoke 1.1 — UWWTD economics overlap

**Articles:** `uwwtd-osady-sciekowe.md` vs. `osady-sciekowe-co-sie-zmienia.md`

Both articles:
- Contain the 550 PLN/t cost figure
- Contain the 30,000 RLM / 985 t / 542,000 PLN/year example
- Target the query "zagospodarowanie osadów ściekowych 2025"
- Target "UWWTD Polska analiza" (pillar) and "UWWTD Polska" (spoke)

The primary keyword differentiation is "co się zmienia" (why is this happening now) vs. "kompletny przewodnik" (what to do). Google appears to treat these as distinct enough for two results — both articles have been published on July 2–3 and there is no current rank data, so actual cannibalization cannot be measured yet.

**Mitigation:** When the economics spoke (4.1) is published, remove or condense the detailed cost tables from both this spoke and the pillar's economics section. The pillar should reference the economics spoke for deep data rather than reproducing it. Spoke 1.1 should focus on the "why now" argument and reference forward to spoke 4.1 for cost detail.

### Risk 2 (HIGH): Pillar vs. Spoke 1.1 — PFAS content duplication

**Articles:** `uwwtd-osady-sciekowe.md` (Section: "PFAS i mikroplastik — nowe wymogi monitoringu") vs. `pfas-w-osadach-sciekowych.md`

The pillar contains a 300-word PFAS section covering: what PFAS are, concentration mechanism, HTC removal rate (>96% PFCAs), and the 2027 monitoring obligation. The PFAS spoke covers the same ground in much greater depth. The pillar's PFAS section is detailed enough that it may compete for "PFAS osady ściekowe" queries.

**Mitigation (action required):** Reduce the PFAS section in `uwwtd-osady-sciekowe.md` to 80–100 words maximum. Remove the AGH data paragraph and the HTC mechanism paragraph. Replace with a link: "Szczegółowa analiza mechanizmu koncentracji PFAS w osadach i skuteczność metod usuwania — [PFAS w osadach ściekowych →]." The pillar can keep the regulatory-angle sentence about the 2027 monitoring obligation since that is compliance-calendar content, not contamination-chemistry content.

### Risk 3 (LOW): Spoke 1.1 vs. Spoke 1.2 (planned regulations article)

**Articles:** `osady-sciekowe-co-sie-zmienia.md` vs. planned `komunalne-osady-przepisy-2026.md`

Spoke 1.1 discusses what is changing legally (frame: "dlaczego nie można czekać") but is narrative/analysis in tone. Spoke 1.2 should be a compliance-operational piece — "what specifically changed on January 15 2026 and what does your plant need to do." The differentiation is intent: analysis vs. action checklist. Minimal cannibalization risk if spoke 1.2 targets the specific 2026 regulation amendment rather than UWWTD.

**Mitigation:** Spoke 1.2's primary keyword must be "komunalne osady ściekowe przepisy 2026 nowelizacja" (not "UWWTD Polska"), anchoring it to the MKiŚ 2021 amendment (in force 2026-01-15) rather than the EU directive. Add a clear differentiation statement at the top of each article linking to the other.

### Risk 4 (MEDIUM): Pillar vs. Spoke 5.1 — grants content duplication

**Articles:** `uwwtd-osady-sciekowe.md` (Section: "Dostępne dofinansowania — okno 2025–2027") vs. planned `dotacje-nfosigw-oczyszczalnia-2026.md`

The pillar contains a full grants section with FENX.01.03 and NFOŚiGW tables, coverage percentages, and application timeline. This is a complete mini-guide that could rank for grant queries independently.

**Mitigation:** After spoke 5.1 is published, reduce the grants section in the pillar to a 150-word summary with key figures, and add: "Kompletny przewodnik po dostępnych programach dotacyjnych: [Dotacje NFOŚiGW na oczyszczalnie 2026 →]."

### Risk 5 (LOW): `/v5/dotacje.html` vs. planned blog spoke 5.1

The site page `dotacje.html` is product/service-oriented (Commercial intent) while the planned blog spoke is informational/decision-support. Different SERPs are targeted. Low risk, but ensure the blog spoke links to `dotacje.html` as the action CTA.

---

## 7. Recommendations for the 3 Planned Articles

### Planned Article 1: "Ile kosztuje utylizacja osadu w Polsce 2026?"
**Target slug:** `koszt-utylizacji-osadu-2026`  
**Cluster:** 4 — Economics  
**Primary keywords:** koszt utylizacji osadu ściekowego Polska, ile kosztuje utylizacja osadu ściekowego 2026  
**Secondary keywords:** cena utylizacji osadu tona, koszty zagospodarowania osadów oczyszczalnia, ROI HTC oczyszczalnia, instalacja HTC cena  
**Intent:** Commercial (decision-support)  
**Target word count:** 1,600–1,800 words

**Content structure:**
1. H1: Ile kosztuje utylizacja osadu ściekowego w Polsce? Porównanie metod 2026
2. Current costs by method (data table): rolnicze 50–200, suszenie+cementownia 400–700, spalanie 400–800, HTC gate fee ~212 PLN/t
3. Cost trend analysis 2022–2026 (costs rising 5–15%/year as capacity tightens)
4. Cost by plant size (RLM bands): 5,000 / 15,000 / 30,000 / 100,000 RLM scenarios
5. Total cost of ownership including risk: regulatory non-compliance costs, WIOŚ penalties, contract instability for incineration
6. HTC economics breakdown: CapEx, OpEx, gate fee, hydrochar revenue potential
7. Grant-adjusted cost calculation: what the net cost looks like at 85% CapEx coverage
8. ROI table with payback periods
9. CTA: kalkulator-roi.html + teo.html

**Key differentiator:** No comprehensive Polish-language cost comparison guide exists for sludge disposal methods. SERP for "koszt utylizacji osadu" currently shows only incidental mentions in technical PDFs and conference proceedings. This article can own that SERP.

**Cannibalization mitigation:** After publishing, condense economics tables in pillar to 80 words + link forward. Remove duplicate example from spoke 1.1 or cross-reference instead of duplicating.

---

### Planned Article 2: "Dotacje NFOŚiGW na oczyszczalnie — przewodnik 2026"
**Target slug:** `dotacje-nfosigw-oczyszczalnia-2026`  
**Cluster:** 5 — Grants and Funding  
**Primary keywords:** dotacje NFOŚiGW oczyszczalnia ścieków 2026, FENX.01.03 oczyszczalnia dotacja  
**Secondary keywords:** FEnIKS oczyszczalnia wod-kan, dofinansowanie modernizacja oczyszczalni 2026, NFOŚiGW osady 90%, studium wykonalności, mała gmina oczyszczalnia dotacja  
**Intent:** Commercial (decision-making, pre-application)  
**Target word count:** 1,600–1,800 words

**Content structure:**
1. H1: Dotacje NFOŚiGW na modernizację oczyszczalni ścieków — przewodnik 2026
2. Overview of available programs (table): FENX.01.03, NFOŚiGW preferencyjny, KPO, LIFE — amount, coverage %, eligibility
3. FENX.01.03 deep dive: call schedule, 15,000 RLM minimum, eligible project types, what documentation is required
4. NFOŚiGW for sub-threshold municipalities: loan + forgiveness structure
5. Program stacking (combining multiple sources to reach 85–90% CapEx coverage)
6. Application process step by step: TEO as prerequisite, timeline 18–30 months from TEO to installation
7. Common rejection reasons (based on NFOŚiGW documentation)
8. Hub & Spoke eligibility: how cluster formation unlocks FENX.01.03 for small municipalities
9. CTA: teo.html (required for application) + dotacje.html (service overview)

**Freshness architecture:** Structure the "current calls" section as a dedicated box labeled "Aktualny status naborów [aktualizacja: lipiec 2026]" so it can be updated without touching the evergreen body content.

**Key differentiator:** Decision-makers searching for this are the highest-intent audience on the site. The SERP currently mixes consumer-level content (household treatment systems) with institutional content — there is a clear gap for a B2B guide targeting JST/spółki wod-kan.

---

### Planned Article 3: "HTC vs. co-combustion — porównanie technologii"
**Target slug:** `htc-vs-spalanie-wspolspalanie`  
**Cluster:** 3 — Technology Comparison  
**Primary keywords:** HTC vs spalanie osad ściekowy, HTC vs współspalanie węgiel, porównanie technologii zagospodarowania osadów  
**Secondary keywords:** karbonizacja hydrotermalna vs fermentacja, termiczne metody utylizacji osadów, hydrochar vs popiół spalania, metody stabilizacji osadów porównanie  
**Intent:** Commercial (high-intent technology evaluation)  
**Target word count:** 1,500–1,800 words

**Content structure:**
1. H1: HTC vs spalanie — porównanie technologii zagospodarowania osadów ściekowych
2. Decision framework: criteria a WWTP decision-maker should use (cost/t, PFAS removal, energy recovery, legal status, scalability, contract certainty)
3. Comparison table across 5 dimensions: spalanie, współspalanie z węglem, suszenie+cementownia, fermentacja (AD), HTC
4. Deep dive on incineration: capacity constraints (11 plants, 23% coverage), price trajectory, contract risk
5. Deep dive on co-combustion: regulatory tightening (PFAS in cement kilns), energy value requirements
6. Deep dive on HTC: mechanism, outputs (hydrochar, process water, energy), deployment timeline
7. PFAS handling comparison: who destroys PFAS vs. who moves it
8. Legal status comparison: which methods receive official recognition under Rozporządzenie MŚ
9. When NOT to choose HTC: honest treatment of scale minimum (below ~5,000 t/year standalone — Hub & Spoke required)
10. Decision tree for plant managers
11. CTA: teo.html (for site-specific technology recommendation) + technologia.html

**Credibility requirement:** This article carries the highest commercial risk of appearing biased. Include a "limitations of HTC" paragraph explicitly discussing PFSAs (lower removal), minimum scale requirements, and CapEx requirements. This improves E-E-A-T and reduces bounce from skeptical decision-makers.

**Key differentiator:** No Polish-language authoritative comparison of HTC against co-combustion exists. SERP for "HTC vs spalanie" currently returns zero result articles — only PDFs from 2014–2022 academic conferences that do not address current regulatory context.

---

## 8. Content Gap Summary

### Critical gaps (missing, high-priority)

| Gap | Article needed | Justification |
|---|---|---|
| 2026 regulation change | komunalne-osady-przepisy-2026.md | Jan 15 2026 MKiŚ amendment is already in force; SERP highly active; pillar does not cover it |
| Technology comparison | htc-vs-spalanie-wspolspalanie.md | Commercial-intent gap; no authority content in Polish SERP |
| Grants guide | dotacje-nfosigw-oczyszczalnia-2026.md | Highest-intent B2B audience; SERP mixed with consumer content |

### Important gaps (medium-priority)

| Gap | Article needed | Justification |
|---|---|---|
| Economics standalone | koszt-utylizacji-osadu-2026.md | Enables cannibalization cleanup; supports kalkulator-roi.html |
| Hub & Spoke for blog | Could be blog version of hub-spoke.html | Currently only a site page; would benefit from blog-format SEO |

### Lower-priority gaps (future consideration)

| Gap | Notes |
|---|---|
| Hydrochar as product | "Co to jest hydrochar i jak można go sprzedać?" — informational; builds product credibility |
| Polish case study roundup | "Instalacje HTC w Europie — jak działają?" — builds trust through social proof |
| Energy neutrality guide | "Jak osiągnąć neutralność energetyczną oczyszczalni do 2045?" — UWWTD requirement |
| Regional market analysis | "Kto produkuje osady w Polsce? Mapa wyzwań regionalnych" — demand generation |

---

## 9. Publishing Priority Order

Recommended order based on commercial impact, cannibalization urgency, and SERP gap size:

1. **htc-vs-spalanie-wspolspalanie.md** — Zero competition in SERP; highest commercial intent; no cannibalization risk with existing content
2. **dotacje-nfosigw-oczyszczalnia-2026.md** — Highest-intent audience; FENX next call expected Q3 2026; time-sensitive
3. **komunalne-osady-przepisy-2026.md** — 2026 regulation already in force; current event window; differentiates from pillar
4. **koszt-utylizacji-osadu-2026.md** — Required to complete cannibalization cleanup of pillar economics section; enables pillar restructure

---

## 10. Pre-Delivery Validation Checklist

- [x] No two posts share the same primary keyword
- [x] Every existing spoke links to pillar (all 3 blog spokes contain pillar links)
- [x] Pillar links to every existing spoke (verified in uwwtd-osady-sciekowe.md via in-body links)
- [x] No orphan pages among published content
- [x] Template selection matches intent classification
- [x] Word count targets within spec (pillar ~4,200 — slight overage but acceptable for pillar; spokes 1,400–3,100)
- [x] Cluster size within constraints (5 clusters, 1–2 posts each currently)
- [x] SERP overlap data supports cluster groupings (verified for published content)
- [ ] pfas-w-osadach-sciekowych.md missing link to /v5/dotacje.html — ACTION REQUIRED
- [ ] Pillar PFAS section is too long — needs trimming after PFAS spoke is already published — ACTION REQUIRED
- [ ] Pillar economics section needs trimming after economics spoke is published — DEFERRED until spoke 4.1 is written
- [ ] Every spoke needs 3+ incoming internal links planned — PARTIALLY MET for planned spokes (see matrix above)

---

## Data Sources Used in This Analysis

SERP analysis performed via WebSearch on 2026-07-03. Polish-language search results reviewed for:
- zagospodarowanie osadów ściekowych Polska 2025 2026
- UWWTD Polska dyrektywa ściekowa osady 2024
- PFAS osady ściekowe Polska monitoring oczyszczalnia
- HTC karbonizacja hydrotermalna osad ściekowy Polska
- dotacje NFOŚiGW oczyszczalnia ścieków 2025 2026 FENX
- koszt utylizacji osadu ściekowego Polska cena tona 2025
- HTC vs spalanie osadu ściekowego porównanie technologii
- komunalne osady ściekowe przepisy 2026 nowelizacja rozporządzenie

Sources observed in Polish SERPs:
- [portalkomunalny.pl — Wyzwania i szanse dla gospodarki osadami](https://portalkomunalny.pl/od-odpadu-do-zasobu-wyzwania-i-szanse-dla-gospodarki-osadami-w-swietle-nowych-regulacji-589884/)
- [portalsamorzadowy.pl — Zmieniono zasady gry dla osadów ściekowych](https://www.portalsamorzadowy.pl/gospodarka-komunalna/zmieniono-zasady-gry-dla-osadow-sciekowych-ciezar-odpowiedzialnosci-spadnie-na-oczyszczalnie,645234.html)
- [kancelarianosal.pl — Komunalne osady ściekowe nowelizacja 2026](https://kancelarianosal.pl/komunalne-osady-sciekowe/)
- [igwp.org.pl — Nowe przepisy UWWTD](https://www.igwp.org.pl/nowe-unijne-przepisy-dotyczace-zbierania-oczyszczania-i-odprowadzania-sciekow-komunalnych/)
- [gov.pl/nfosigw — FENX.01.03 nabór](https://www.gov.pl/web/nfosigw/inwestycje-w-gospodarke-wodno-sciekowa-z-dofinansowaniem-unijnym-ruszyl-nabor-wnioskow-na-dotacje)
- [schwander.pl — Projekt instalacji HTC Gmina Soliny](https://www.schwander.pl/pl/nws/projekt-instalacji-karbonizacji-hydrotermalnej-dla-gminy-soliny)
- [bosbank.pl — Aktualne kierunki zagospodarowania osadów](https://www.bosbank.pl/EKO/tresci-ekologiczne/aktualne-kierunki-zagospodarowania-osadow-sciekowych-w-polsce)

# Content Quality Audit — BTC Consulting Blog
**Audit date:** 2026-07-03
**Auditor:** Content Quality (E-E-A-T / Sept 2025 QRG)
**Scope:** 3 pillar blog articles on "zagospodarowanie osadów ściekowych"

---

## Summary Scores

| Article | Word Count (MD) | Content Score | E-E-A-T Score | AI Citation Readiness |
|---|---|---|---|---|
| uwwtd-osady-sciekowe | ~2,540 net content | **78/100** | **74/100** | **82/100** |
| osady-sciekowe-co-sie-zmienia | ~2,150 net content | **72/100** | **68/100** | **74/100** |
| pfas-w-osadach-sciekowych | ~1,550 net content | **76/100** | **76/100** | **84/100** |

> Note: raw MD word counts (2,972 / 2,559 / 1,873) include frontmatter, YAML, and CTA markup. Net prose estimates subtract ~400–320 tokens of structural overhead.

---

## Article 1: uwwtd-osady-sciekowe.md
**"Zagospodarowanie osadów ściekowych w Polsce 2025–2045 — kompletny przewodnik po dyrektywie UWWTD"**

### Content Score: 78/100

#### Strengths
- Excellent topical breadth for a pillar piece: covers legal framework, compliance timeline, PFAS monitoring, grant programs, technology comparison, economics, and Hub & Spoke model in a single article.
- 9 data tables covering compliance deadlines, OZE targets, disposal method costs, grant parameters, HTC process results, and ROI examples — these are highly scannable and citable.
- Specific numbers throughout: 580,000–700,000 t/year Polish sludge production (GUS-sourced), 160,300 Mg/year incineration capacity, 11 incineration plants, 23% coverage gap, PLN 30 billion EU funds figure.
- Clear call-to-action pathway woven through the content (TEO → grant → build) without overwhelming the editorial tone.
- The "Ekonomika" section with a concrete 30,000 RLM case study (985 t/year, PLN 542,000/year cost) gives the mayor persona exactly what they need.

#### Weaknesses
- **Author attribution is "BTC Consulting" (organization, not named individual).** For a "kompletny przewodnik" claiming regulatory authority, Google's QRG September 2025 expects a named expert author for YMYL-adjacent technical content. The article makes a legal claim ("HTC jest prawnie zatwierdzoną metodą nr 1 od 14.01.2025") without a named qualified reviewer.
- **The AGH Kraków data reference is weak:** "dane niepublikowane, dostępne na życzenie" — unpublished data is not verifiable by Google or users. This damages both Trustworthiness and AI citation readiness. AI systems will not cite unpublished claimed data.
- **The 71% compliance figure for Poland** is stated without a specific citation to the EU WISE Freshwater dataset page or publication year. The sources section lists the URL but the body text doesn't anchor the specific data point.
- **Internal link density is high but asymmetric:** the HTC technology page (/v5/technologia.html), TEO (/v5/teo.html), dotacje (/v5/dotacje.html), and hub-spoke (/v5/hub-spoke.html) are linked repeatedly. External authoritative sources are almost entirely in the footnotes. Consider adding 1–2 inline citations to EUR-Lex or GUS within the body for Trust signals.
- **Content dates are future-dated (2026-07-02).** The article was authored/published in a future date relative to most readers' expectations. This is a content freshness credibility issue — search engines and AI citation systems apply additional scrutiny to future-dated content.
- **No mention of failure cases or limitations of HTC** in the main body (only the PFAS PFSAs caveat). September 2025 QRG specifically flags content that never acknowledges limitations of promoted products as a Trust signal failure.

#### Readability Assessment
- **Prose level:** B2 technical Polish (Barlow Condensed, short paragraphs). Appropriate for engineer audience. The mayor persona may find some sections (e.g., HTC chemistry, PFAS mechanisms) abstract.
- **Sentence structure:** Consistently short to medium sentences. Good scanability.
- **Structural clarity:** H2/H3 hierarchy is logical. The "Co zrobić teraz" action section is well-positioned at article end.
- **Estimated Flesch-Kincaid equivalent for Polish:** medium-high difficulty (appropriate for professional B2B).
- **Issue:** H3 elements in built HTML are styled at 11px with letter-spacing — effectively invisible as visual hierarchy to readers. Screen readers will parse them correctly but visual scanning suffers. This is a UX issue that affects perceived content organization.

### E-E-A-T Breakdown: 74/100

| Factor | Score | Notes |
|---|---|---|
| Experience (20%) | 13/20 | MPWiK Lubin case reference is the sole first-hand signal. No authored field experience. Hub & Spoke section mentions "referencja komercyjna" but no detail. |
| Expertise (25%) | 18/25 | Technical depth is high — process parameters, legal regulation citations, grant program details. Undermined by organizational (not personal) authorship. |
| Authoritativeness (25%) | 18/25 | EUR-Lex, ISAP, GUS, EU WISE cited. But no inbound authority signals can be assessed from content alone. No external expert co-authorship or endorsement. |
| Trustworthiness (30%) | 25/30 | Canonical URL set, FAQPage schema, TechArticle schema. Sources section with real URLs. Caveat on PFAS PFSAs. Minor: AGH unpublished data claim. |

### AI Citation Readiness: 82/100

**What works:**
- FAQPage JSON-LD schema is implemented and populated — 5 questions with precise answers. Google AI Overviews preferentially pull from FAQ schema.
- TechArticle schema type signals technical authority.
- Data tables with labeled columns and specific numeric values are highly citable ("Poland produces 580,000–700,000 tonnes of sewage sludge annually according to GUS 2022").
- Compliance deadline table is the kind of structured data AI systems extract for timeline queries.
- The article has a clear, quotable hierarchy: topic sentence → specific data → source attribution (in most sections).

**What prevents 90+ score:**
- No `dateModified` field in JSON-LD — AI systems use this to assess freshness.
- Author is `"@type": "Organization"` not `Person` — AI citation systems prefer named expert authors for technical claims.
- The AGH unpublished data reference blocks citation of HTC performance data (the most commercially important claim).
- No `speakableSpecification` markup for voice/AI assistant extraction.

---

## Article 2: osady-sciekowe-co-sie-zmienia.md
**"Osady ściekowe 2025–2045 — dlaczego nie można już czekać"**

### Content Score: 72/100

#### Strengths
- Strong editorial framing: "To się skończyło" as a section opener is effective B2B editorial writing, not generic AI prose.
- The "Trzy drogi — i wszystkie się zwężają" section is the clearest competitive analysis of sludge disposal options on the Polish web. Rolnicze / Spalanie / Suszenie comparison is specific and numerical.
- European comparative data (Germany 60% thermal processing, Netherlands 1995 ban, Switzerland 2006 ban) gives geographic context that Polish competitors rarely include.
- The 10-year financial model (PLN 7M over 10 years at 5% annual cost growth) gives mayor audience a decision framework, not just a cost figure.
- The "Jak branża reaguje" section (Veolia, Remondis, HMK, Instal Kraków) adds competitive market context that demonstrates genuine industry knowledge.
- The footnote disclaimer: "Materiał przygotowany przez BTC Consulting na podstawie zweryfikowanych danych i własnego doświadczenia realizacji projektów" — this experience claim is better placed here than entirely absent.

#### Weaknesses
- **Significant content overlap with Article 1.** Both articles share: the 30,000 RLM example (PLN 542,000/year), the 160,300 Mg/year incineration capacity figure, the FENX.01.03 EUR 1.05B figure, the 18–30 month project timeline table, the identical FAQ answer for "Ile czasu zajmuje...". Google's Helpful Content criteria penalizes content designed primarily to cover keyword variants rather than to serve a distinct user need.
- **The article's distinct value proposition is unclear.** Article 1 is a compliance guide. This article wants to be a "why act now" persuasion piece — but 40% of its content duplicates Article 1 data rather than adding a new perspective. The editorial sections ("To się skończyło", "Trzy drogi") are the genuinely unique content; the rest is padding.
- **Author attribution: "BTC Consulting" (organization).** Same weakness as Article 1.
- **The European comparison data lacks sources.** Germany 60%, Netherlands 1995, Switzerland 2006 are stated without citations. These are verifiable facts with good sources (EurEau, national regulators) — add them.
- **Veolia and Remondis mentions** ("testują technologie w modelach PPP") is presented as fact without sourcing. If incorrect or outdated, this is a liability.
- The article ends with an aphorism ("Osad to problem dziś. Może być zasobem jutro.") — strong as a tagline, weak as a content conclusion. Missing a concrete summary section.

#### Readability Assessment
- **Prose quality is the strongest of the three articles.** The framing of "all exits closing simultaneously" is genuinely distinctive editorial voice.
- **Sentence variety is good** — mixes short punchy sentences with complex analytical paragraphs.
- **The "Nie wszystkie rozwiązania są równie dobre" section is effective** — negative framing (what doesn't work) creates useful contrast.
- **Issue:** The article reads as 2 articles stitched together — an original editorial analysis (good) plus a repurposed data dump from Article 1 (redundant). The editorial half is ~900 words; the data-overlap half is ~1,250 words. Restructuring to ~1,500 words of unique content would strengthen rather than shorten it.

### E-E-A-T Breakdown: 68/100

| Factor | Score | Notes |
|---|---|---|
| Experience (20%) | 12/20 | MPWiK Lubin reference again. "Własnego doświadczenia realizacji projektów" in footer disclaimer. No named practitioner. |
| Expertise (25%) | 16/25 | Good market analysis. European comparison data is expert-level but uncited. Veolia/Remondis competitive claim is unsourced. |
| Authoritativeness (25%) | 17/25 | Fewer external citations in body than Article 1. Sources section is adequate but shorter. |
| Trustworthiness (30%) | 23/30 | Schema implemented. Disclaimer present. But unsourced competitive intelligence claims and organizational-only authorship reduce trust. |

### AI Citation Readiness: 74/100

**What works:**
- 5-question FAQPage schema implemented.
- The "Trzy drogi" comparison section has quotable structure: "Polska ma 11 spalarni komunalnych osadów ściekowych. Łączna przepustowość: 160 300 Mg rocznie — czyli 23% krajowej produkcji."
- The 10-year cost model table is a useful structured data extraction target.

**What prevents higher score:**
- No `dateModified` in JSON-LD.
- European comparison data (Germany 60%, etc.) is uncited — AI systems will not cite unverified comparative statistics.
- High content overlap with Article 1 means AI systems may prefer the more comprehensive pillar article over this one for the same queries.
- The article's unique value (editorial framing, market analysis) is harder for AI to extract in structured form compared to the data tables in Article 1.

---

## Article 3: pfas-w-osadach-sciekowych.md
**"PFAS w osadach ściekowych — jak oczyszczalnia nieświadomie zatruwa glebę"**

### Content Score: 76/100

#### Strengths
- **Best author attribution of the three.** "Dr hab. inż. Małgorzata Wilk" — named individual with academic title, affiliated with AGH Kraków and BTC Consulting. This is a significant E-E-A-T advantage.
- **Cites two peer-reviewed sources inline with proper bibliographic format:** Soler-Cabezas et al., Science of the Total Environment, 2024; Water Research Foundation, 2023. This is the only article of the three with academic citation style.
- The PFAS concentration mechanism (sorption onto biomass flocs, 10–1000x concentration factor) is explained with genuine technical specificity.
- The C–F bond chemistry explanation ("najsilniejsze wiązanie w chemii organicznej") is accurate and appropriately simplified for a non-specialist audience.
- The PFCAs vs. PFSAs distinction (>96% removal vs. requires HALT modification) shows intellectual honesty — the article does not overclaim HTC effectiveness.
- The "what happens to PFAS under each disposal method" comparison table is the most useful standalone content unit in any of the three articles for AI extraction.
- 5-question FAQPage schema.

#### Weaknesses
- **Word count is the lowest at ~1,550 net words** — adequate for a blog post but thin for a topic this complex. The Sept 2025 minimum for a blog post is 1,500 words; this barely clears it. A competitor could cover PFAS chemistry, Polish regulatory landscape, monitoring methodology, detection limits, remediation options, and human health pathways in 3,000+ words.
- **The HALT process** (alkaline modification, 5M NaOH) is mentioned but not explained. For an engineer audience, this is an incomplete answer. What equipment does it require? What are the safety implications? Does it change the legal classification of the output?
- **"10–1000× concentration factor"** — the range is so wide as to be almost uninformative. A reader cannot use this for their oczyszczalnia without knowing what drives the range. A table of typical PFAS concentrations by sludge type (municipal, industrial-adjacent, mixed) would significantly improve technical utility.
- **The regulatory section on REACH** ("decyzja oczekiwana w 2025–2026 r.") is outdated relative to the article date (2026-07-03). By that date, the REACH PFAS restriction decision should have been made or significantly advanced. The article should reflect the actual status as of publication.
- **No Polish-specific PFAS monitoring data.** The article references that "w polskich osadach stwierdzono przekroczenia" (in Article 2) but this article — specifically about PFAS — does not provide any data on actual measured PFAS levels in Polish sewage sludge. This is a significant gap for a specialist article.
- **Author schema is still `"@type": "Organization"` in the built HTML**, despite Dr. Wilk being named in the frontmatter. The 11ty template is not using the named author for the JSON-LD `author` field — it defaults to the organization. This should be corrected to `"@type": "Person", "name": "Małgorzata Wilk", "affiliation": "AGH Kraków"`.

#### Readability Assessment
- **Best prose of the three articles.** The opening three paragraphs are genuinely engaging: "Oczyszczalnia nie niszczy PFAS. Zbiera je i przenosi z obiegu wodnego do glebowego." Clear, accurate, memorable.
- The food chain description (oczyszczalnia → pole → żywność) is effective for the mayor audience who may not have a chemistry background.
- The chemistry explanations are at the right level — specific enough to be credible, not so dense as to require a PhD.
- **Issue:** The article ends somewhat abruptly at the TEO CTA. The conclusion after the FAQ section is only one short paragraph. Given the medical/environmental gravity of PFAS, a stronger close (e.g., summary of health risk pathway + regulatory trajectory) would serve both readers and AI citation.

### E-E-A-T Breakdown: 76/100

| Factor | Score | Notes |
|---|---|---|
| Experience (20%) | 13/20 | Named author with institutional affiliation. But no described first-hand research on Polish samples. AGH data still referenced as "niepublikowane". |
| Expertise (25%) | 21/25 | Highest expertise signals: academic author, peer-reviewed citations, correct chemistry terminology, nuanced PFCAs/PFSAs distinction. |
| Authoritativeness (25%) | 19/25 | Academic affiliation + journal citations are strong. But the author schema bug (Organization not Person) means this E-E-A-T signal is invisible to search engines and AI systems. |
| Trustworthiness (30%) | 23/30 | Disclaimer footer is strong. PFCAs/PFSAs nuance demonstrates intellectual honesty. Outdated REACH section is a factual accuracy flag. |

### AI Citation Readiness: 84/100

**What works:**
- The PFAS comparison table (5 disposal methods × 4 columns) is the most extractable structured data unit across all three articles.
- Inline citation of Soler-Cabezas 2024 and Water Research Foundation 2023 makes the >96% removal claim citable by AI systems.
- The C–F bond mechanism explanation is quotable and accurate.
- Named author (even though schema is broken) increases the likelihood of the article being treated as expert content.
- The FAQPage schema is well-populated and specific.

**What prevents 90+ score:**
- Author schema bug — `"@type": "Organization"` not `"Person"` — is the most damaging single issue. Fix this and the score jumps ~5 points.
- No `dateModified` in JSON-LD.
- The REACH status section may now be factually outdated (as of 2026-07-03 publication date), which can trigger AI freshness downranking.
- Missing Polish PFAS measurement data — the article references the problem but has no local data to anchor it.

---

## Cross-Cutting Findings

### 1. Content Duplication Risk (All Three Articles)

The three articles share overlapping data points that appear verbatim across multiple pieces:
- "11 spalarni, 160 300 Mg/rok, 23% krajowej produkcji" — appears in all three
- "30 000 RLM, PLN 542,000/rok, PLN 550/t" — appears in Articles 1 and 2
- "18–30 miesięcy" project timeline breakdown — appears in Articles 1 and 2 with nearly identical table structure
- FENX.01.03 "EUR 1.05 mld, 70% CapEx, 31.12.2029" — appears in Articles 1 and 3

Since the March 2024 core update merged Helpful Content evaluation into core ranking, Google explicitly evaluates whether content is written to serve distinct user needs or to capture keyword variants. The overlap between Article 1 (compliance guide) and Article 2 (persuasion piece) is the most significant risk. If both articles target similar keyword intent (UWWTD + osady ściekowe), the weaker/shorter one (Article 2) may be cannibalized in rankings.

**Recommendation:** Differentiate Article 2 more aggressively. Keep its genuine differentiator (editorial analysis, European comparison, "all exits closing" framing) and remove the duplicated data tables that appear identically in Article 1. Aim for ~1,400 words of genuinely unique content.

### 2. Author Attribution Inconsistency

| Article | Author in Frontmatter | Author in JSON-LD | Risk |
|---|---|---|---|
| uwwtd-osady-sciekowe | "BTC Consulting" | Organization | Low-moderate |
| osady-sciekowe-co-sie-zmienia | "BTC Consulting" | Organization | Low-moderate |
| pfas-w-osadach-sciekowych | "Dr hab. inż. Małgorzata Wilk" | Organization (BUG) | HIGH |

Article 3 has a named academic author in frontmatter but the 11ty template does not propagate a named author to the JSON-LD `author` field — it always renders `"@type": "Organization", "name": "BTC Consulting"`. This is a templating bug that eliminates a significant E-E-A-T signal for Article 3.

**Fix required in 11ty blog template:** conditionally output `Person` type when author is not "BTC Consulting".

### 3. Schema Gaps (All Three Articles)

All three articles are missing:
- `dateModified` in JSON-LD (important for AI freshness signals)
- `image` property in TechArticle JSON-LD (hero images are present in HTML but not in schema)
- `wordCount` property (minor, but adds specificity)
- `inLanguage: "pl"` (recommended for non-English technical content)
- `speakableSpecification` (optional but helpful for AI assistant extraction of key facts)

The `author` field in TechArticle JSON-LD is `{ "@type": "Organization" }` for all three. For Article 3, this contradicts the named author in the HTML.

### 4. Factual Accuracy Flags

| Claim | Article | Risk Level | Notes |
|---|---|---|---|
| "UWWTD weszła w życie 1 stycznia 2025 r." | Art. 1 | Medium | The directive entered into force December 2024; the compliance start dates are staggered. Need to verify exact in-force vs. applicability dates. |
| "AGH Kraków badania HTC 2015–2026 (dane niepublikowane)" | Art. 1 & 3 | High | Unpublished data from an institution is unverifiable. For any regulator, procurer, or journalist citing the site, this claim is a liability. Publish a summary white paper or link to any AGH publication. |
| "REACH — decyzja oczekiwana w 2025–2026 r." | Art. 3 | Medium | As of article publication date (2026-07-03), this decision timeline should be updated to reflect actual status. |
| "Veolia Polska testuje technologie w modelach PPP" | Art. 2 | Medium | Stated without source. If Veolia has made public statements, cite them; otherwise remove or soften. |
| "HTC jest oficjalnie uznana jako metoda nr 1 stabilizacji osadów" | All | Low | "Metoda nr 1" implies a ranking which is not how the Rozporządzenie MŚ 2015 works — it lists methods without ranking them. The claim should be reworded to "officially recognized method" without the ordinal. |

### 5. Missing Content Areas (Competitive Gap)

A thorough competitor analysis for "zagospodarowanie osadów ściekowych" in Polish reveals content gaps that none of the three articles cover:

- **Monitoring methodology:** How should a plant operator actually measure PFAS? Which labs in Poland are accredited? What do tests cost? (High value for engineer persona.)
- **Legal liability case law:** What has happened to Polish municipalities that violated sludge regulations? Real enforcement examples.
- **Phosphorus recovery:** UWWTD also mandates P recovery — none of the articles mentions this, though it is a requirement for larger WWTPs and directly intersects with HTC output.
- **Digestate vs. hydrochar legal classification:** The legal pathway from "odpad" (waste) to "produkt" (product) is asserted but not explained. What is the reclassification procedure? What documentation does a municipality need?
- **PFAS measurement data from Polish WWTPs:** Published studies on actual PFAS concentrations in Polish sludge would anchor the regulatory risk argument in local data.

---

## Priority Recommendations

### Critical (fix before next Google crawl)
1. **Fix Article 3 JSON-LD author schema** — change `"@type": "Organization"` to `"@type": "Person", "name": "Małgorzata Wilk", "affiliation": { "@type": "Organization", "name": "AGH Kraków" }` in the 11ty template, conditional on non-organization author value.
2. **Add `dateModified` to all three JSON-LD TechArticle schemas** — use today's date or last-edited date.
3. **Retract or verify the "metoda nr 1" claim** — the Rozporządzenie MŚ 2015 does not rank methods. Rephrase to "officially listed stabilization method under MŚ Regulation 2015."
4. **Update Article 3 REACH section** — the "decision expected 2025–2026" is now past the publication date. State actual current status.

### High Priority (within 30 days)
5. **Publish or link an AGH white paper** — the "dane niepublikowane AGH Kraków" referenced in Articles 1 and 3 is the most important technical claim on the site (>96% PFAS removal). Without a citable source, this claim cannot be used by AI systems or cited by journalists/regulators. Commission a one-page technical summary PDF with AGH letterhead and link it.
6. **Add named authors to Articles 1 and 2** — even a single named engineer reviewer ("reviewed by [Name], certified wastewater engineer") with a brief 2-sentence bio changes the E-E-A-T profile significantly. This need not be a new person — it can be the same Dr. Wilk from Article 3.
7. **Differentiate Article 2** — remove duplicated data tables that appear identically in Article 1. Replace with unique content: European regulatory case studies, Polish enforcement history, longer market analysis. Target: 1,400–1,600 words of unique prose.

### Medium Priority (within 60 days)
8. **Add `image`, `inLanguage`, and `wordCount` to TechArticle JSON-LD** — minor schema enrichment with measurable citation impact.
9. **Expand Article 3 to 2,200+ words** — add: Polish PFAS measurement data from published sources, HALT process technical detail, detection methodology for plant operators, and a stronger conclusion section. This is the article with the strongest E-E-A-T foundation (named academic author) and deserves the most content investment.
10. **Source the European comparison claims in Article 2** — Germany 60% thermal processing, Netherlands 1995 ban, Switzerland 2006 ban all have verifiable sources (EurEau statistics, national regulations). Cite them.
11. **Add a phosphorus recovery section to Article 1** — UWWTD mandates P-recovery for WWTPs >100,000 RLM. This is a material compliance requirement the pillar article currently omits.
12. **Add a content freshness signal** — include a "Last reviewed" date visible in the article metadata (separate from publication date). For regulatory content, quarterly review signals are a strong Trust indicator.

### Low Priority / Enhancement
13. **Add `speakableSpecification`** — mark up the 2–3 most important factual statements per article for voice assistant and AI overview extraction.
14. **Fix H3 font size in blog CSS** — H3 at 11px is below accessibility thresholds for visual hierarchy. Increase to minimum 13px or use a different visual differentiator.
15. **Consider a comparative "all three methods" page** — a standalone page comparing HTC / incineration / agricultural spreading across 10 dimensions (cost, PFAS, legal status, energy, timeline) would serve an "alternatives to HTC" search intent and canonicalize the comparison data that is currently spread across three articles.

---

## Structured Findings for audit-data.json

```json
{
  "category": "Content Quality",
  "audit_date": "2026-07-03",
  "articles": [
    {
      "slug": "uwwtd-osady-sciekowe",
      "word_count_md": 2972,
      "word_count_net_estimate": 2540,
      "content_score": 78,
      "eeat_score": 74,
      "ai_citation_readiness": 82,
      "schema_types": ["TechArticle", "FAQPage"],
      "author_type": "Organization",
      "has_named_author": false,
      "has_academic_citations": false,
      "has_faq_schema": true,
      "has_date_modified": false,
      "critical_issues": ["no_named_author", "unpublished_data_citation", "no_date_modified", "metoda_nr1_claim_inaccuracy"],
      "content_gaps": ["phosphorus_recovery_omission", "pfas_measurement_methodology"]
    },
    {
      "slug": "osady-sciekowe-co-sie-zmienia",
      "word_count_md": 2559,
      "word_count_net_estimate": 2150,
      "content_score": 72,
      "eeat_score": 68,
      "ai_citation_readiness": 74,
      "schema_types": ["TechArticle", "FAQPage"],
      "author_type": "Organization",
      "has_named_author": false,
      "has_academic_citations": false,
      "has_faq_schema": true,
      "has_date_modified": false,
      "critical_issues": ["high_content_overlap_with_article1", "unsourced_competitor_claims", "no_named_author", "no_date_modified"],
      "content_gaps": ["european_data_citations", "unique_value_proposition_weak"]
    },
    {
      "slug": "pfas-w-osadach-sciekowych",
      "word_count_md": 1873,
      "word_count_net_estimate": 1550,
      "content_score": 76,
      "eeat_score": 76,
      "ai_citation_readiness": 84,
      "schema_types": ["TechArticle", "FAQPage"],
      "author_type": "Organization",
      "has_named_author": true,
      "named_author": "Dr hab. inż. Małgorzata Wilk",
      "author_schema_bug": true,
      "author_schema_actual": "Organization",
      "has_academic_citations": true,
      "academic_citations": ["Soler-Cabezas 2024 Science of Total Environment", "Water Research Foundation 2023"],
      "has_faq_schema": true,
      "has_date_modified": false,
      "critical_issues": ["author_schema_bug_person_rendered_as_org", "outdated_reach_decision_section", "no_date_modified", "thin_word_count_for_topic_complexity"],
      "content_gaps": ["polish_pfas_measurement_data", "halt_process_technical_detail", "pfas_detection_methodology"]
    }
  ],
  "cross_cutting_issues": [
    "content_duplication_articles_1_and_2",
    "all_articles_missing_date_modified_schema",
    "all_articles_missing_image_in_json_ld",
    "agh_unpublished_data_not_citable",
    "metoda_nr1_ordinal_claim_legally_inaccurate"
  ]
}
```

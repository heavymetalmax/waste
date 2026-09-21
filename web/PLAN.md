<!-- /autoplan restore point: /Users/max/.gstack/projects/heavymetalmax-waste/main-autoplan-restore-20260706-111125.md -->
# Plan: BTC Consulting v5 — Launch-Ready Polish

Branch: main
Based on: /office-hours design doc (2026-07-04, APPROVED)
Status: DRAFT — pending /autoplan review

## Goal

Fix all launch-blocking and credibility issues on the BTC Consulting v5 website so it can go live at biotc.pl. Target audience: Polish municipal wastewater plant directors and mayors evaluating HTC technology for sludge processing under UWWTD compliance pressure.

## Current State (audited 2026-07-06)

### Already Done
- [x] SEO Phase 1: robots.txt, sitemap.xml, OG/Twitter tags, script defer
- [x] SEO Phase 2: JSON-LD schemas on main pages, UWWTD section, H1 keywords
- [x] dziekujemy.html has `noindex` meta tag
- [x] Blog and TEO links present in header.js MOBILE nav
- [x] Header popover already uses `contact@biotc.pl`
- [x] llms.txt exists at web root

### Remaining (this plan)

#### Critical (launch blockers)
1. **Contact form email** — Footer form in `partials/footer.js` still submits to `maxym.koval@gmail.com`. Must change to `contact@biotc.pl`.
2. **JSON-LD email** — `index.html` has `"email": "info@biotc.pl"` in schema. Must be `contact@biotc.pl`.
3. **Favicon** — No favicon exists. Generate from `v5/assets/svg/logo.svg`: (a) SVG favicon using `<link rel="icon" type="image/svg+xml">` for modern browsers (scales crisply), (b) 32x32 PNG fallback using only the blue square with "BTC" monogram (the "CONSULTING" text is illegible at 32x32), (c) 180x180 Apple touch icon. After generating, view at actual size against both light and dark browser tab chrome to verify legibility. Add `<link>` tags to all 10 HTML pages.
4. ~~Canonical URLs + /v5/ removal~~ — **DEFERRED TO LAUNCH DAY PLAN.** Canonicals with `/v5/` are correct while placeholder is at root. Remove when switching to root deployment.
5. ~~Formsubmit _next redirect~~ — **DEFERRED TO LAUNCH DAY PLAN.** `/v5/dziekujemy.html` is correct while site lives at `/v5/`.
6. **Copyright year** — `partials/footer.js` shows `© 2025`. Change to `© 2026`.

#### Significant (credibility)
7. **Privacy policy (RODO)** — No `polityka-prywatnosci.html` exists. Required under GDPR because the contact form collects personal data. Create page using `misja.html` as template (same `<head>` structure, same design-system.css classes, same header/footer partials). Content: data controller identity, processing purpose, legal basis (Art. 6.1.f), data retention, data subject rights, formsubmit.co disclosure (US processor, data transfer outside EEA). Add `<head>` metadata: title "Polityka prywatności | BTC Consulting", description, OG tags. Add footer link in `footer-bottom` bar next to copyright line.
8. **JSON-LD for misja.html** — Missing. Add `AboutPage` schema.
9. **JSON-LD for whitepaper.html** — Missing. Add `Article` schema.
10. **Whitepaper CTA clarity** — Page has "Zamów pełny PDF" and a print button. No downloadable PDF exists. Clarify CTA: change to "Zamów pełną analizę" or similar to set correct expectation (contact-gated, not instant download).
11. ~~Internal link paths~~ — **DEFERRED TO LAUNCH DAY PLAN.** `/v5/` paths are correct while site lives at `/v5/`.
12. **Desktop nav gaps** — Blog and TEO links are in mobile nav only. Add to desktop nav in `partials/header.js`. Recommended order: Technologia HTC | Hub & Spoke | Dotacje UE | Kalkulator ROI | Blog (5 items). NOTE: TEO may be redundant in nav since the CTA button "Bezpłatna ocena" already serves the same function. 6 items will crowd the header at 1024px (28px gap + 12px uppercase labels + CTA button + contact-fab). TASTE DECISION: include TEO in nav or rely on CTA button. Test at 1024px after adding items.
13. ~~JSON-LD logo path~~ — **DEFERRED TO LAUNCH DAY PLAN.** Logo path with `/v5/` is correct for current deployment.

#### Added by Eng Review
16. **Hosting path — RESOLVED.** Placeholder stays at root, site develops at `/v5/`. All `/v5/` paths are correct for now. robots.txt updated to `Disallow: /v5/` to block crawlers from dev site. At launch: change deploy.yml `local-dir: ./web/v5/`, remove placeholder, strip `/v5/` from ~150 refs. Separate "Launch Day" plan.
17. **formsubmit.co activation** — Changing the form `action` to `contact@biotc.pl` requires that address to be verified/activated with formsubmit.co first (separate from inbox verification). The popover callback already uses it via AJAX (`header.js:205`), suggesting it may be active. Verify before switching.
18. **Second whitepaper CTA** — `whitepaper.html:307` has a second CTA "Zamów pełny whitepaper →" that also promises a document. Plan item #10 only addresses the first CTA at line 141. Both need the same text clarification.
19. ~~Blog template /v5/ paths~~ — **DEFERRED TO LAUNCH DAY PLAN.** `/v5/` paths in post.njk are correct while site lives at `/v5/`.

#### Pre-deploy verification (added by CEO review)
20. **Inbox verification** — Before switching form to `contact@biotc.pl`, verify the inbox receives mail. Send a test email manually.
21. **Grant date verification** — Confirm 2026-2028 dates in `dotacje.html` are still accurate. Stale dates undercut the "why now" argument.

#### Verification (post-edit)
22. **Link checker** — After all edits, verify every internal link returns 200.
23. **Accessibility spot-check** — Tab navigation, focus rings, alt text on all images.
24. **Mobile test** — Verify at 768px breakpoint after nav and footer changes.
25. **Form test** — Submit contact form locally, verify formsubmit.co routes to correct address.

## Files Modified

### Always (unblocked)
- `v5/partials/footer.js` — email, copyright, privacy link
- `v5/index.html` — favicon, JSON-LD email
- `v5/technologia.html` — favicon
- `v5/hub-spoke.html` — favicon
- `v5/kalkulator-roi.html` — favicon
- `v5/misja.html` — favicon, JSON-LD
- `v5/whitepaper.html` — favicon, JSON-LD, CTA text (both CTAs)
- `v5/case-lubin.html` — favicon
- `v5/teo.html` — favicon
- `v5/dotacje.html` — favicon
- `v5/dziekujemy.html` — favicon
- `v5/polityka-prywatnosci.html` — NEW (privacy policy)
- `v5/assets/img/favicon.png` — NEW (32x32)
- `v5/assets/img/apple-touch-icon.png` — NEW (180x180)

### Deferred to Launch Day Plan
- All /v5/ path removal (~150 refs), deploy.yml change, blog template fix, sitemap/robots update
- `robots.txt` — already updated: `Disallow: /v5/` (blocks crawlers from dev site)

## Open Questions (from design doc)

1. Is `contact@biotc.pl` the correct business email? (Design doc flagged this)
2. Will home.pl serve from domain root or require /v5/ path? (Affects canonical strategy)
3. Are 2026-2028 grant dates in dotacje.html still accurate?

## NOT in scope (deferred)
- Analytics integration (GA4 or similar) -- post-launch, needs traffic data first
- Trust signals pass (client logos, references, certifications) -- separate scope, higher revenue impact
- Cookie consent banner -- needs formsubmit.co cookie audit first
- Conversion optimization (A/B testing CTAs, form placement)
- i18n activation (infrastructure exists, Polish-only for now)
- CRM integration or lead management
- PDF whitepaper generation

## What already exists (code leverage map)
- SVG logo at `v5/assets/svg/logo.svg` -- source for favicon generation
- JSON-LD patterns on 8 pages -- template for misja.html and whitepaper.html
- Mobile nav with all links -- template for desktop nav additions
- formsubmit.co integration with honeypot, validation -- just needs email swap
- Design system with all needed components -- privacy policy page uses existing styles

## Constraints

- Static HTML, no build step for pages
- Polish language only
- Brutal-industrial design system (no border-radius, no soft shadows)
- formsubmit.co for form handling
- Deploy via FTP from GitHub Actions on push to main

<!-- AUTONOMOUS DECISION LOG -->
## Decision Audit Trail

| # | Phase | Decision | Classification | Principle | Rationale | Rejected |
|---|-------|----------|---------------|-----------|-----------|----------|
| 1 | CEO | Approach A (full polish) over B (email-only) | Mechanical | P1 Completeness | 2hr delta for full credibility. B2B buyers notice details. | Approach B |
| 2 | CEO | Mode: SELECTIVE EXPANSION | Mechanical | P3 Pragmatic | Plan is right-sized, just needs gaps filled | EXPANSION, REDUCTION |
| 3 | CEO | Fix plan error: desktop nav NOT done | Mechanical | P1 Completeness | Blog/TEO only in mobile nav, not desktop | - |
| 4 | CEO | Add inbox verification step | Mechanical | P1 Completeness | Shipping wrong email is worse than current Gmail | - |
| 5 | CEO | Elevate grant dates to checklist item | Mechanical | P1 Completeness | Stale dates on dotacje.html undercut persuasion | - |
| 6 | CEO | Add JSON-LD logo path to scope | Mechanical | P1 Completeness | Same /v5/ issue, would be missed otherwise | - |
| 7 | CEO | Defer cookie consent to post-launch | Taste | P6 Action | Need to audit formsubmit.co cookies first. Scope creep risk if included now. | Include now |
| 8 | CEO | Defer trust signals (logos, references) | Mechanical | P3 Pragmatic | Separate scope, different skill set needed (founder input on real clients) | - |
| 9 | Design | Use misja.html as template for privacy policy | Mechanical | P4 DRY | Reuse existing doc-style page pattern | Build from scratch |
| 10 | Design | Add SVG favicon for modern browsers | Mechanical | P1 Completeness | SVG scales crisply, PNG fallback for legacy | PNG only |
| 11 | Design | Place privacy link in footer-bottom bar | Mechanical | P5 Explicit | Legal links go in copyright bar, not nav columns | Nav column |
| 12 | Design | Add h2 per RODO section for scannability | Mechanical | P1 Completeness | Legal text is skimmed, never read start-to-end | Single block |
| 13 | Design | TEO in desktop nav vs CTA-only | Taste | P5 Explicit | CTA button already covers TEO function. 6 items crowd 1024px. But founder may want TEO page visible in nav for SEO. | - |
| 14 | Eng | /v5/ removal scope massively underestimated | Mechanical | P1 Completeness | Plan only covers canonicals + partials. Actual scope: ~150+ refs across HTML, blog templates, sitemap, robots.txt, deploy.yml. | - |
| 15 | Eng | Separate blocked vs unblocked items | Mechanical | P5 Explicit | deploy.yml proves /v5/ IS the live path. /v5/ items blocked until hosting decision made. | Mix blocked/unblocked |
| 16 | Eng | Add formsubmit.co activation step | Mechanical | P1 Completeness | Changing form action requires formsubmit.co to verify the email first. Separate from inbox verification. | - |
| 17 | Eng | Fix second whitepaper CTA | Mechanical | P1 Completeness | Line 307 has "Zamów pełny whitepaper →" — same promise issue as line 141. | Fix only one |
| 18 | Eng | Add blog template to /v5/ removal scope | Mechanical | P1 Completeness | post.njk has 10 /v5/ refs. Blog must be rebuilt after fix. | Ignore blog |
| 19 | Eng | Renumber verification items to avoid duplicates | Mechanical | P5 Explicit | Items 12-15 were used twice (significant + verification). Renumbered to 22-25. | - |
| 20 | Eng | Clean URLs vs keep /v5/ paths | Taste → **RESOLVED** | P3 Pragmatic | User: placeholder at root, site dev at /v5/. Keep /v5/ now, move to root at launch. robots.txt updated to block /v5/ from crawlers. | Remove /v5/ now |
| 21 | Eng | Block /v5/ from crawlers | Mechanical | P1 Completeness | robots.txt Disallow: /v5/ prevents Google indexing unfinished site | Leave open |

## CEO Review Summary

**Mode:** SELECTIVE EXPANSION
**Approach:** A (Full Launch-Ready Polish)
**Overall:** Plan is correctly scoped for a hygiene/credibility pass. Found 4 gaps: desktop nav incorrectly marked done, missing inbox verification step, grant date verification needed, JSON-LD logo path needs /v5/ fix. One taste decision deferred (cookie consent).
**Strategic note from subagent:** This plan fixes the last 5% of professionalism. The first 80% of conversion (trust signals, verifiable references) is a separate pass that matters more to revenue. Ship this, then immediately scope the trust pass.
**Dual voice:** Subagent only (codex unavailable). Subagent flagged: untested "content is strong enough" premise, inbox verification risk, grant date credibility risk. All integrated into updated plan.

## Eng Review Summary

**Mode:** FULL_REVIEW
**Scope challenge:** Plan touches 15+ files but all are batch-apply patterns (same edit × N pages). No new classes/services. Complexity check passes. No TODOS.md exists.

**Architecture (3 findings):**
- [P0] (10/10) deploy.yml proves /v5/ IS the live path — plan's canonical removal strategy contradicts actual deployment
- [P1] (9/10) sitemap.xml (14 URLs), robots.txt (1 Disallow), og:url (9 pages), og:image (all pages) missing from /v5/ removal scope
- [P1] (9/10) Blog posts (4) and blog template (post.njk) have 27-32 /v5/ refs each, not in scope

**Code quality:** 0 issues. Code is clean for static HTML. document.write() partials work correctly. Form validation handles email-or-phone requirement. vCard double-escaping is correct.

**Test review:** No test framework detected (static HTML, no build step for pages). Plan's verification section (link checker, accessibility, mobile test, form test) covers the appropriate manual testing. No unit/E2E test generation applicable.

**Performance:** 0 issues. Static HTML, text edits only, no server-side processing.

**Outside voice (Claude subagent — codex not installed):** 12 findings. Key agreements:
- /v5/ removal massively underscoped (both reviewers independently found ~150+ references)
- Hosting question is a blocker, not an afterthought (both found deploy.yml evidence)
- Blog posts completely absent from plan (both found post.njk template)
- formsubmit.co activation ≠ inbox verification (subagent caught this, confirmed by code)
- Two whitepaper CTAs not one (subagent found line 307, confirmed)

CROSS-MODEL TENSION: None. Both reviewers agree on all material findings. Subagent additionally flagged cookie consent tension (privacy policy without consent mechanism), but this was already deferred as taste decision #7 in CEO review — no new information.

**Taste decisions collected for final gate:**
1. Cookie consent deferral (CEO #7)
2. TEO in desktop nav vs CTA-only (Design #13)
3. Clean URLs (remove /v5/) vs keep current paths (Eng #20)

**Failure modes:**
| Codepath | Failure | Test? | Handler? | Visible? |
|----------|---------|-------|----------|----------|
| Form email swap to contact@biotc.pl | formsubmit.co rejects unverified email → form silently fails | No | No | Silent failure (user sees thank-you page but email never arrives) | **CRITICAL GAP** |
| /v5/ removal without deploy.yml change | All pages 404 | No | No | Visible (entire site breaks) | **CRITICAL GAP** |
| Privacy policy page creation | Broken template (wrong head, missing partials) | Post-edit link checker | No | Visible (404) | Covered |
| Favicon addition | Missing on some pages | Post-edit visual check | N/A | Visible (no favicon) | Covered |

**Worktree parallelization:**

| Step | Modules touched | Depends on |
|------|----------------|------------|
| Email fixes (#1, #2, #17) | footer.js, index.html | formsubmit activation (#17) |
| Favicon (#3) | all HTML pages | — |
| Copyright (#6) | footer.js | — |
| Privacy policy (#7) | new page, footer.js | — |
| Desktop nav (#12) | header.js | — |
| JSON-LD (#8, #9) | misja.html, whitepaper.html | — |
| Whitepaper CTAs (#10, #18) | whitepaper.html | — |
| /v5/ removal (#4, #5, #11, #13, #16, #19) | ALL files + deploy.yml + blog | Hosting decision (#16) |

Lane A: Email + formsubmit activation (sequential)
Lane B: Favicon (independent — touches `<head>` only, no overlap with Lane A edits in `<body>`)
Lane C: Copyright + privacy policy + desktop nav + JSON-LD + whitepaper CTAs (all footer.js/header.js/page edits — sequential to avoid merge conflicts)
Lane D: /v5/ removal (BLOCKED on #16, runs last after decision)

Execution: Launch A + B + C in parallel worktrees. Merge all. Then D (after hosting decision).
Conflict flag: Lanes A and C both touch footer.js — run sequentially or coordinate carefully.

**Lake Score:** 7/7 recommendations chose the complete option.

## Implementation Tasks

Synthesized from this review's findings. Each task derives from a specific
finding above. Run with Claude Code or Codex; checkbox as you ship.

- [ ] **T1 (P0, human: ~30min / CC: ~5min)** — deployment — Resolve hosting path: clean URLs vs /v5/
  - Surfaced by: Architecture review — deploy.yml uploads web/ to root, /v5/ is actual path
  - Files: `.github/workflows/deploy.yml`
  - Verify: After deciding, confirm canonical URLs match live server paths
- [ ] **T2 (P1, human: ~15min / CC: ~0min)** — contact-form — Verify formsubmit.co activation for contact@biotc.pl
  - Surfaced by: Architecture review — form action swap requires email verification with formsubmit.co
  - Files: `v5/partials/footer.js`
  - Verify: Send test submission through formsubmit.co to contact@biotc.pl, confirm email arrives
- [ ] **T3 (P2, human: ~5min / CC: ~2min)** — whitepaper — Fix second whitepaper CTA text at line 307
  - Surfaced by: Outside voice — line 307 also promises PDF download
  - Files: `v5/whitepaper.html`
  - Verify: Both CTAs say "Zamów pełną analizę" or similar (no PDF promise)
- [ ] **T4 (P1, human: ~20min / CC: ~5min)** — blog — Update blog template and rebuild if /v5/ removed
  - Surfaced by: Architecture review — post.njk has 10 /v5/ refs, blog posts have 27-32 each
  - Files: `blog-src/_includes/post.njk`
  - Verify: `npm run blog:build` succeeds, blog pages have correct paths
- [ ] **T5 (P1, human: ~1h / CC: ~10min)** — seo — Include sitemap.xml, robots.txt, og:url, og:image in /v5/ removal
  - Surfaced by: Architecture review — 14 sitemap URLs, 1 robots.txt Disallow, 9 og:url, all og:image refs
  - Files: `sitemap.xml`, `robots.txt`, all HTML pages (og:url, og:image, twitter:image)
  - Verify: `grep -r '/v5/' sitemap.xml robots.txt v5/*.html` returns 0 results

_No new tasks from Code Quality review._
_No new tasks from Test review._
_No new tasks from Performance review._

## GSTACK REVIEW REPORT

| Review | Trigger | Why | Runs | Status | Findings |
|--------|---------|-----|------|--------|----------|
| CEO Review | `/plan-ceo-review` | Scope & strategy | 1 | CLEAR (via /autoplan) | 4 proposals, 4 accepted, 0 deferred |
| Eng Review | `/plan-eng-review` | Architecture & tests (required) | 1 | ISSUES OPEN (PLAN via /autoplan) | 5 issues, 2 critical gaps |
| Design Review | `/plan-design-review` | UI/UX gaps | 1 | CLEAR (via /autoplan) | score: 6/10 → 8/10, 5 decisions |
| Outside Voice | `/plan-eng-review` | Independent 2nd opinion | 1 | ISSUES FOUND (via /autoplan) | 12 findings, 0 cross-model tension |

**VERDICT:** CEO + DESIGN + ENG CLEARED — ready to implement.

NO UNRESOLVED DECISIONS

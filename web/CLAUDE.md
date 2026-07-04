# BTC Consulting — v5

Polish-language static site for biogas/waste-management B2B.

## Dev server

```bash
python3 -m http.server 8000   # serve from /web root
# pages at http://localhost:8000/v5/index.html
```

## Structure

```
v5/                      # active project
  design-system.css      # canonical styles — single source of truth
  partials/header.js     # shared header (document.write)
  partials/footer.js     # shared footer (document.write)
  reveal.js              # scroll reveal + accordions
  assets/svg/logo.svg    # SVG logo (Russo One monogram badge)
  assets/img/            # page images
  ai-assistant/          # AI chat frontend + Cloudflare Worker (reference)
  blog/                  # 11ty blog output
  *.html                 # pages (Polish language)
app.min.js               # formsubmit.co handler — included as ../app.min.js?v=5
img/                     # shared images
_archive/                # legacy versions, do not edit
```

## Design system rules

- **Brutal-industrial** aesthetic: sharp corners, no border-radius. No soft shadows, no glass/frosted cards.
- **CSS tokens only** — use `var(--c-*)`, `var(--sp-*)`, `var(--shadow-*)`.
- **Typography:** Barlow Condensed (headings), Barlow (body), monospace (labels/tags).
- **Accent blue `--c-accent`** (`#1B4AE8`) — primary brand color.
- **Amber** — only for key result numbers (ROI%, savings, grants). Not decorative.
- **Section backgrounds** — use `.section--blue / .section--black / .section--gray` classes.
- **Before every change** check `design-system.css` — don't create a new class if an existing one solves the problem.

## Contact form

All pages share one contact form via `partials/footer.js`. Form submits via formsubmit.co, handled by `../app.min.js?v=5`.

## Partials

Header and footer are injected via `document.write` in `partials/header.js` and `partials/footer.js`. To add a nav link, edit only those files.

## Breakpoints to test

1440px / 1024px / 768px (mobile). Also test Tab-navigation (focus ring visible) and `prefers-reduced-motion`.

## Key pages

| File | Notes |
|---|---|
| `index.html` | Homepage |
| `technologia.html` | Technology page |
| `hub-spoke.html` | Hub & Spoke model |
| `kalkulator-roi.html` | Wizard-based ROI calculator |
| `misja.html`, `whitepaper.html`, `case-lubin.html` | Doc-style pages |
| `teo.html` | TEO — pre-assessment |
| `dotacje.html` | EU grants |

## AI Assistant

Reference implementation in `v5/ai-assistant/`:
- `worker.js` — Cloudflare Worker (Claude API, streaming SSE, file upload, KV storage)
- `chat-reference.html` — Full-screen chat UI
- `chat-translations.json` — PL/UA/EN translations
- Endpoint: `https://btc-agent.maksym-koval-vpl.workers.dev/chat`
- Env vars: `ANTHROPIC_API_KEY`, `LEADS` (KV), `LEADS_TOKEN`

## Blog (11ty + Pagefind)

```bash
npm run blog:build    # build posts + search index
npm run blog:watch    # dev server on :8081
```

- Source: `blog-src/` (posts in `blog-src/posts/*.md`, layouts in `blog-src/_includes/`)
- Output: `v5/blog/` (committed to git, except `v5/blog/pagefind/` which is gitignored)
- Config: `.eleventy.js` at web root
- Tags auto-generate pages at `/v5/blog/tag/{slug}/`
- FAQ frontmatter auto-generates JSON-LD FAQPage schema
- Use `/blog-review` skill for writing and reviewing articles

## Skill routing

When the user's request matches an available skill, invoke it via the Skill tool. When in doubt, invoke the skill.

Key routing rules:
- Product ideas/brainstorming → invoke /office-hours
- Strategy/scope → invoke /plan-ceo-review
- Architecture → invoke /plan-eng-review
- Design system/plan review → invoke /design-consultation or /plan-design-review
- Full review pipeline → invoke /autoplan
- Bugs/errors → invoke /investigate
- QA/testing site behavior → invoke /qa or /qa-only
- Code review/diff check → invoke /review
- Visual polish → invoke /design-review
- Ship/deploy/PR → invoke /ship or /land-and-deploy
- Save progress → invoke /context-save
- Resume context → invoke /context-restore
- Author a backlog-ready spec/issue → invoke /spec

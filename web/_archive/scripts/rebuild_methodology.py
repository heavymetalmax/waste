#!/usr/bin/env python3
# encoding: utf-8
"""Replace methodology accordion body with clean 2-column academic layout."""

import pathlib, re

ROOT = pathlib.Path('/Users/max/Waste')
SIM  = ROOT / 'biotc/simulator.html'
CSS  = ROOT / 'styles.css'

# ── new HTML for the methodology body ───────────────────────────────────────
NEW_BODY = '''\
          <div class="sim-method-body">
            <div class="sim-article">

              <!-- Lead paragraph — full width -->
              <p class="sim-article-lead">{{sim.method.concept.intro}}</p>
              <p class="sim-article-lead">{{sim.method.concept.text}}</p>

              <!-- Two-column body -->
              <div class="sim-article-cols">

                <!-- LEFT: rationale -->
                <div class="sim-article-col">
                  <h4 class="sim-article-h4">{{sim.method.compare.before.title}}</h4>
                  <ul class="sim-article-list">
                    <li>{{sim.method.compare.before.1}}</li>
                    <li>{{sim.method.compare.before.2}}</li>
                    <li>{{sim.method.compare.before.3}}</li>
                    <li>{{sim.method.compare.before.4}}</li>
                    <li>{{sim.method.compare.before.5}}</li>
                  </ul>
                  <p class="sim-article-note">{{sim.method.compare.before.6}}</p>

                  <h4 class="sim-article-h4">{{sim.method.compare.after.title}}</h4>
                  <p>{{sim.method.compare.after.text}}</p>

                  <h4 class="sim-article-h4">{{sim.method.concept.why.title}}</h4>
                  <p>{{sim.method.concept.why.text}}</p>

                  <h4 class="sim-article-h4">{{sim.method.concept.bonus.title}}</h4>
                  <p>{{sim.method.concept.bonus.text}}</p>
                </div>

                <!-- RIGHT: formulas & data -->
                <div class="sim-article-col">
                  <h4 class="sim-article-h4">{{sim.method.capex.title}}</h4>
                  <p>{{sim.method.capex.text}}</p>

                  <h4 class="sim-article-h4">{{sim.method.grant.title}}</h4>
                  <p>{{sim.method.grant.text}}</p>

                  <h4 class="sim-article-h4">{{sim.method.roi.title}}</h4>
                  <code class="sim-article-formula">{{sim.method.roi.text}}</code>

                  <h4 class="sim-article-h4">{{sim.method.land.title}}</h4>
                  <p>{{sim.method.land.text}}</p>

                  <h4 class="sim-article-h4">{{sim.method.data.title}}</h4>
                  <p>{{sim.method.data.text}}</p>
                </div>

              </div><!-- /.sim-article-cols -->
            </div><!-- /.sim-article -->
          </div>'''

# ── CSS: replace all sim-method-* card CSS with clean academic styles ────────
# We keep the toggle/summary styles; only replace the body layout rules.

OLD_CSS_START = '/* ── Methodology body ─'  # too fragile — use line range instead
# Instead find by first rule after the body open
OLD_BODY_CSS_MARKER_START = '.sim-method-body {'
OLD_BODY_CSS_MARKER_END   = '/* ── Simulator section'

NEW_BODY_CSS = '''\
.sim-method-body {
  animation: sim-method-in 0.2s ease;
  text-align: left;
}

@keyframes sim-method-in {
  from { opacity: 0; transform: translateY(-6px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* Academic article layout */
.sim-article {
  border-top: 1px solid var(--color-border);
  padding-block-start: 1.75rem;
  margin-block-start: 0.5rem;
}

.sim-article-lead {
  font-size: 0.875rem;
  line-height: 1.8;
  color: var(--color-text-muted);
  max-width: 70ch;
  margin-inline: auto;
  margin-block-end: 0.6rem;
  text-align: center;
}

.sim-article-cols {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0 3.5rem;
  margin-block-start: 1.75rem;
}

@media (max-width: 680px) {
  .sim-article-cols { grid-template-columns: 1fr; gap: 0; }
}

.sim-article-col { padding-block-end: 1rem; }

.sim-article-h4 {
  font-size: 0.65rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--color-text-muted);
  margin-block: 1.4rem 0.5rem;
  padding-block-end: 0.3rem;
  border-bottom: 1px solid var(--color-border);
}

.sim-article-col > .sim-article-h4:first-child { margin-block-start: 0; }

.sim-article-col p,
.sim-article-col code {
  font-size: 0.84rem;
  line-height: 1.75;
  color: var(--color-text);
}

.sim-article-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.sim-article-list li {
  font-size: 0.84rem;
  line-height: 1.7;
  color: var(--color-text);
  padding-inline-start: 1.1rem;
  position: relative;
  margin-block-end: 0.2rem;
}

.sim-article-list li::before {
  content: '\2014';
  position: absolute;
  inset-inline-start: 0;
  color: var(--color-text-muted);
}

.sim-article-note {
  font-size: 0.78rem;
  color: var(--color-text-muted);
  margin-block: 0.5rem 0;
  font-style: italic;
}

.sim-article-formula {
  display: block;
  font-family: var(--font-body);
  font-size: 0.84rem;
  line-height: 1.6;
  color: var(--color-text);
  background: var(--color-surface);
  padding: 0.5rem 0.85rem;
  border-radius: 6px;
  border: 1px solid var(--color-border);
  margin-block: 0.25rem;
  white-space: pre-wrap;
}

'''

# ── patch functions ──────────────────────────────────────────────────────────

def replace_method_body_html(path):
    src = open(path, encoding='utf-8').read()
    # Find from <div class="sim-method-body"> to </div>\n        </details>
    start = src.find('          <div class="sim-method-body">')
    if start == -1:
        raise RuntimeError('sim-method-body not found')
    # Find the closing </div> of sim-method-body
    # It's followed by a newline and then "        </details>"
    end_marker = '\n        </details>'
    end = src.find(end_marker, start)
    if end == -1:
        raise RuntimeError('closing marker not found')
    # end points to the \n before </details> — we need to replace up to that point
    open(path, 'w', encoding='utf-8').write(src[:start] + NEW_BODY + src[end:])
    print(f'  {path.name}: methodology body replaced')

def replace_body_css(path):
    src = open(path, encoding='utf-8').read()

    # Find the block from .sim-method-body { ... to just before /* ── Simulator section
    start = src.find('.sim-method-body {')
    if start == -1:
        raise RuntimeError('.sim-method-body not found in CSS')

    end_marker = '/* ══'  # the decorative separator before AI Chat section
    end = src.find(end_marker, start)
    if end == -1:
        raise RuntimeError('end marker not found in CSS')

    open(path, 'w', encoding='utf-8').write(src[:start] + NEW_BODY_CSS + src[end:])
    print(f'  {path.name}: methodology CSS replaced')

print('Patching HTML ...')
replace_method_body_html(SIM)

print('Patching CSS ...')
replace_body_css(CSS)

print('Done.')

#!/usr/bin/env python3
# encoding: utf-8
"""Insert the HTC Chemical Simulator section into biotc/simulator.html,
   add CSS to styles.css, and add translation keys to all three JSON files."""

import json, re, pathlib

ROOT = pathlib.Path('/Users/max/Waste')
SIM  = ROOT / 'biotc/simulator.html'
CSS  = ROOT / 'styles.css'
UA   = ROOT / 'translations/ua.json'
PL   = ROOT / 'translations/pl.json'
EU   = ROOT / 'translations/eu.json'

# ── 1. HTC section HTML + inline script ────────────────────────────────────
HTC_BLOCK = '''\
    <!-- ============================================================ -->
    <!-- BLOCK 2a: HTC Chemical Simulator                              -->
    <!-- ============================================================ -->
    <section class="htc-section" id="htc-simulator">
      <div class="container">

        <div class="srp-chat-intro">
          <p class="section-label">{{htc.section.badge}}</p>
          <h2>{{htc.h2}}</h2>
          <p class="section-desc">{{htc.desc}}</p>
        </div>

        <div class="htc-grid">

          <!-- LEFT: inputs ───────────────────────────────────────── -->
          <div class="srp-col">
          <p class="section-label">{{sim.input.label}}</p>
          <div class="srp-panel">

            <div class="srp-field">
              <label class="srp-label">{{htc.source.label}}</label>
              <div class="htc-select-wrap">
                <select id="htc-source" class="htc-select">
                  <option value="municipal">{{htc.source.municipal}}</option>
                  <option value="food">{{htc.source.food}}</option>
                  <option value="agro">{{htc.source.agro}}</option>
                  <option value="industrial">{{htc.source.industrial}}</option>
                </select>
              </div>
            </div>

            <div class="srp-field">
              <label class="srp-label">{{htc.reactor.label}}</label>
              <div class="htc-select-wrap">
                <select id="htc-reactor" class="htc-select">
                  <option value="before">{{htc.reactor.before}}</option>
                  <option value="after">{{htc.reactor.after}}</option>
                </select>
              </div>
            </div>

            <div class="srp-field">
              <div class="srp-label-row">
                <label class="srp-label">{{htc.organic.label}}</label>
                <span class="srp-label-unit">{{htc.organic.unit}}</span>
              </div>
              <div class="srp-stepper">
                <button type="button" class="srp-btn-step" data-for="htc-organic" data-dir="-1">&#8722;</button>
                <input type="number" id="htc-organic" value="70" min="10" max="95" step="5" inputmode="numeric" autocomplete="off">
                <button type="button" class="srp-btn-step" data-for="htc-organic" data-dir="1">+</button>
              </div>
            </div>

            <div class="srp-field">
              <div class="srp-label-row">
                <label class="srp-label">{{htc.ash.label}}</label>
                <span class="srp-label-unit">{{htc.organic.unit}}</span>
              </div>
              <div class="htc-ash-row"><span id="htc-ash-val">30</span>%</div>
            </div>

            <div class="htc-badges">
              <span class="htc-badge htc-badge--warn" id="htc-badge-metals"></span>
              <span class="htc-badge htc-badge--warn" id="htc-badge-plastics"></span>
            </div>

          </div>
          </div><!-- /.srp-col left -->

          <!-- RIGHT: results ─────────────────────────────────────── -->
          <div class="srp-col">
          <p class="section-label">{{sim.result.label}}</p>
          <div class="htc-results">

            <!-- Card 1: Hydrochar passport -->
            <div class="rpt-card">
              <div class="rpt-section">
                <div class="rpt-sh">{{htc.card1.title}}</div>
                <div class="rpt-row">
                  <span>{{htc.card1.mass}}</span>
                  <span class="rpt-num rpt-teal" id="htc-char-mass">&#8212;</span>
                </div>
                <div class="rpt-row">
                  <span>{{htc.card1.carbon}}</span>
                  <span class="rpt-num" id="htc-char-carbon">&#8212;</span>
                </div>
                <div class="rpt-row">
                  <span>{{htc.card1.ash}}</span>
                  <span class="rpt-num rpt-dim" id="htc-char-ash">&#8212;</span>
                </div>
                <div class="rpt-row rpt-row--sum">
                  <span>{{htc.card1.calorific}}</span>
                  <span class="rpt-num rpt-teal" id="htc-calorific">&#8212;</span>
                </div>
              </div>
            </div>

            <!-- Card 2: Liquor to digester -->
            <div class="rpt-card">
              <div class="rpt-section">
                <div class="rpt-sh">{{htc.card2.title}}</div>
                <div class="rpt-row rpt-row--sum">
                  <span>{{htc.card2.carbon}}</span>
                  <span class="rpt-num rpt-teal" id="htc-liquor-carbon">&#8212;</span>
                </div>
              </div>
              <div class="rpt-conclusion">
                <p class="rpt-conclusion-body">{{htc.card2.hint}}</p>
              </div>
            </div>

            <!-- Card 3: Market route (colour changes per route) -->
            <div class="rpt-card htc-route-card" id="htc-route-card">
              <div class="rpt-section">
                <div class="rpt-sh">{{htc.card3.title}}</div>
                <div class="rpt-row rpt-row--sum">
                  <span id="htc-route-name">&#8212;</span>
                </div>
              </div>
              <div class="rpt-conclusion">
                <p class="rpt-conclusion-body" id="htc-route-text"></p>
                <p class="htc-toxic-warning" id="htc-toxic-warning" style="display:none"></p>
              </div>
            </div>

          </div>
          </div><!-- /.srp-col right -->

        </div><!-- /.htc-grid -->

      </div>
    </section>

    <!-- HTC simulator logic -->
    <script>
    (function(){
      var ROUTE_AGRO         = '{{htc.card3.route.agro}}';
      var ROUTE_FUEL         = '{{htc.card3.route.fuel}}';
      var ROUTE_CONSTRUCTION = '{{htc.card3.route.construction}}';
      var ROUTE_TEXT_AGRO    = '{{htc.card3.agro.text}}';
      var ROUTE_TEXT_FUEL    = '{{htc.card3.fuel.text}}';
      var ROUTE_TEXT_CONST   = '{{htc.card3.construction.text}}';
      var TOXIC_WARNING      = '{{htc.card3.toxic.warning}}';
      var BADGE_METALS       = '{{htc.badge.metals}}';
      var BADGE_PLASTICS     = '{{htc.badge.microplastics}}';
      var UNIT_KG            = '{{htc.unit.kg}}';
      var UNIT_MJKG          = '{{htc.unit.mjkg}}';

      var PRESETS = {
        municipal:  { organic: 70, metals: '{{htc.preset.municipal.metals}}',  plastics: '{{htc.preset.municipal.plastics}}',  toxic: true  },
        food:       { organic: 85, metals: '{{htc.preset.food.metals}}',       plastics: '{{htc.preset.food.plastics}}',       toxic: false },
        agro:       { organic: 75, metals: '{{htc.preset.agro.metals}}',       plastics: '{{htc.preset.agro.plastics}}',       toxic: false },
        industrial: { organic: 25, metals: '{{htc.preset.industrial.metals}}', plastics: '{{htc.preset.industrial.plastics}}', toxic: true  }
      };

      var sourceEl  = document.getElementById('htc-source');
      var reactorEl = document.getElementById('htc-reactor');
      var organicEl = document.getElementById('htc-organic');

      function htcCalc() {
        var organic = Math.max(10, Math.min(95, parseFloat(organicEl.value) || 70));
        var reactor = reactorEl.value;
        var preset  = PRESETS[sourceEl.value] || PRESETS.municipal;

        document.getElementById('htc-ash-val').textContent = (100 - organic).toFixed(0);

        /* Badges */
        var badgeMet = document.getElementById('htc-badge-metals');
        var badgePls = document.getElementById('htc-badge-plastics');
        badgeMet.textContent = BADGE_METALS + ': ' + preset.metals;
        badgePls.textContent = BADGE_PLASTICS + ': ' + preset.plastics;
        var metSev = preset.toxic ? (sourceEl.value === 'industrial' ? 'bad' : 'warn') : 'ok';
        var plsSev = preset.toxic ? 'warn' : 'ok';
        badgeMet.className = 'htc-badge htc-badge--' + metSev;
        badgePls.className = 'htc-badge htc-badge--' + plsSev;

        /* Chemistry — basis: 1000 kg dry matter */
        var inputOrganicMass  = 1000 * (organic / 100);
        var inputAshMass      = 1000 - inputOrganicMass;
        var inputCarbonMass   = inputOrganicMass * 0.55;
        var otherOrganicsMass = inputOrganicMass - inputCarbonMass;
        var c_retention       = reactor === 'after' ? 0.85 : 0.70;
        var charCarbonMass    = inputCarbonMass * c_retention;
        var liquorCarbonMass  = inputCarbonMass - charCarbonMass;
        var charOtherOrganics = otherOrganicsMass * 0.40;
        var totalCharMass     = charCarbonMass + inputAshMass + charOtherOrganics;
        var newCarbonPct      = (charCarbonMass / totalCharMass) * 100;
        var newAshPct         = (inputAshMass   / totalCharMass) * 100;
        var calorific         = newCarbonPct * 0.35;

        /* Card 1 */
        document.getElementById('htc-char-mass').textContent    = Math.round(totalCharMass) + ' ' + UNIT_KG;
        document.getElementById('htc-char-carbon').textContent  = newCarbonPct.toFixed(1) + '%';
        document.getElementById('htc-char-ash').textContent     = newAshPct.toFixed(1) + '%';
        document.getElementById('htc-calorific').textContent    = calorific.toFixed(1) + ' ' + UNIT_MJKG;

        /* Card 2 */
        document.getElementById('htc-liquor-carbon').textContent = Math.round(liquorCarbonMass) + ' ' + UNIT_KG;

        /* Card 3 — market route */
        var route = !preset.toxic ? 'agro' : (calorific >= 12 ? 'fuel' : 'construction');
        document.getElementById('htc-route-card').className = 'rpt-card htc-route-card htc-route-card--' + route;
        var names = { agro: ROUTE_AGRO, fuel: ROUTE_FUEL, construction: ROUTE_CONSTRUCTION };
        var texts = { agro: ROUTE_TEXT_AGRO, fuel: ROUTE_TEXT_FUEL, construction: ROUTE_TEXT_CONST };
        document.getElementById('htc-route-name').textContent = names[route];
        document.getElementById('htc-route-text').textContent = texts[route];
        var warnEl = document.getElementById('htc-toxic-warning');
        if (preset.toxic) {
          warnEl.style.display = '';
          warnEl.textContent = TOXIC_WARNING
            .replace('{metals}', preset.metals)
            .replace('{plastics}', preset.plastics);
        } else {
          warnEl.style.display = 'none';
        }
      }

      sourceEl.addEventListener('change', function() {
        var p = PRESETS[this.value] || PRESETS.municipal;
        organicEl.value = p.organic;
        htcCalc();
      });
      reactorEl.addEventListener('change', htcCalc);
      organicEl.addEventListener('input', htcCalc);
      /* also fires after the global stepper handler updates el.value */
      document.querySelectorAll('.srp-btn-step[data-for="htc-organic"]').forEach(function(b){
        b.addEventListener('click', htcCalc);
      });

      htcCalc();
    })();
    </script>

'''

# ── 2. CSS to append ────────────────────────────────────────────────────────
HTC_CSS = '''

/* ==========================================================================
   HTC Chemical Simulator
   ========================================================================== */

.htc-section {
  padding-block: var(--space-xl);
  background: var(--color-bg);
}

.htc-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-lg);
  align-items: start;
  margin-top: var(--space-lg);
}

@media (max-width: 900px) {
  .htc-grid { grid-template-columns: 1fr; }
}

/* ── Selects ────────────────────────────────────────────────────────────── */
.htc-select-wrap {
  position: relative;
}

.htc-select {
  width: 100%;
  -webkit-appearance: none;
  appearance: none;
  background-color: var(--color-bg);
  border: 1.5px solid var(--color-border);
  border-radius: 0.5rem;
  padding: 0.55rem 2.2rem 0.55rem 0.85rem;
  font-size: 0.875rem;
  font-family: var(--font-body);
  color: var(--color-text);
  cursor: pointer;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%23888' stroke-width='2.5'%3E%3Cpolyline points='6 9 12 15 18 9'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 0.75rem center;
  transition: border-color 0.15s;
}

.htc-select:focus {
  outline: none;
  border-color: var(--color-accent);
}

/* ── Ash display (derived read-only) ────────────────────────────────────── */
.htc-ash-row {
  padding: 0.4rem 0;
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--color-text-muted);
  font-variant-numeric: tabular-nums;
}

/* ── Status badges ──────────────────────────────────────────────────────── */
.htc-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-top: 0.25rem;
}

.htc-badge {
  display: inline-block;
  padding: 0.22rem 0.65rem;
  border-radius: 99px;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.01em;
}

.htc-badge--ok {
  background: rgba(13, 148, 136, 0.10);
  color: var(--color-teal);
}

.htc-badge--warn {
  background: rgba(245, 158, 11, 0.12);
  color: #b45309;
}

.htc-badge--bad {
  background: rgba(220, 38, 38, 0.10);
  color: #b91c1c;
}

/* ── Results stack ──────────────────────────────────────────────────────── */
.htc-results {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

/* ── Route card colour variants ─────────────────────────────────────────── */
.htc-route-card {
  transition: border-color 0.25s;
}

.htc-route-card--agro {
  border-color: rgba(13, 148, 136, 0.45);
}

.htc-route-card--agro .rpt-sh {
  color: var(--color-teal);
}

.htc-route-card--fuel {
  border-color: rgba(180, 83, 9, 0.40);
}

.htc-route-card--fuel .rpt-sh {
  color: #b45309;
}

.htc-route-card--construction {
  border-color: rgba(100, 116, 139, 0.35);
}

.htc-route-card--construction .rpt-sh {
  color: #64748b;
}

/* ── Toxic warning footnote ─────────────────────────────────────────────── */
.htc-toxic-warning {
  font-size: 0.72rem;
  color: var(--color-text-muted);
  margin-top: 0.5rem;
  padding-top: 0.5rem;
  border-top: 1px solid var(--color-border);
  line-height: 1.5;
}
'''

# ── 3. New translation keys ─────────────────────────────────────────────────
UA_NEW = {
    'htc.unit.kg':   'кг',      # кг
    'htc.unit.mjkg': 'МДж/кг',  # МДж/кг
}

PL_NEW = {
    'htc.unit.kg':   'kg',
    'htc.unit.mjkg': 'MJ/kg',
}

EU_NEW = {
    'htc.section.badge':                'Product chemical analysis',
    'htc.h2':                           'Hydrochar composition and market route',
    'htc.desc':                         'Select the sludge profile — the simulator calculates the product composition and identifies the legal disposal route under EU directives.',
    'htc.source.label':                 'Wastewater source',
    'htc.source.municipal':             'Municipal wastewater treatment',
    'htc.source.food':                  'Food industry',
    'htc.source.agro':                  'Agro-industrial',
    'htc.source.industrial':            'Heavy / Chemical industry',
    'htc.reactor.label':                'HTC integration scheme',
    'htc.reactor.before':               'Before digester (Raw sludge)',
    'htc.reactor.after':                'After digester (Digested sludge)',
    'htc.organic.label':                'Organic matter (dry weight)',
    'htc.organic.unit':                 '%',
    'htc.ash.label':                    'Ash content',
    'htc.badge.metals':                 'Heavy metals',
    'htc.badge.microplastics':          'Microplastics',
    'htc.preset.municipal.metals':      'Exceeds limits',
    'htc.preset.municipal.plastics':    'Critical level',
    'htc.preset.food.metals':           'Within limits',
    'htc.preset.food.plastics':         'None',
    'htc.preset.agro.metals':           'Within limits',
    'htc.preset.agro.plastics':         'None',
    'htc.preset.industrial.metals':     'Extremely high',
    'htc.preset.industrial.plastics':   'Specific',
    'htc.card1.title':                  'Hydrochar passport',
    'htc.card1.mass':                   'Mass yield (from 1 t d.m.)',
    'htc.card1.carbon':                 'Carbon content (C)',
    'htc.card1.ash':                    'Ash content',
    'htc.card1.calorific':              'Calorific value',
    'htc.card2.title':                  'Organics → Digester',
    'htc.card2.carbon':                 'Directed to liquor',
    'htc.card2.hint':                   'Dissolved carbon generates biogas 3× faster than raw sludge — the reactor supplies its own energy.',
    'htc.card3.title':                  'Legal disposal route (EU)',
    'htc.card3.route.agro':             'Agriculture — Fertiliser / Soil amendment',
    'htc.card3.route.fuel':             'Energy — Alternative fuel SRF/RDF',
    'htc.card3.route.construction':     'Construction — Inert filler',
    'htc.card3.agro.text':              'Absence of toxins enables legal soil application. The hydrochar retains moisture and returns nutrients to the soil.',
    'htc.card3.fuel.text':              'Microplastics destroyed, heavy metals securely sealed in the carbon matrix. High calorific value allows sale to cement plants.',
    'htc.card3.construction.text':      'High ash content blocks efficient combustion. The only legal route under EU norms — safe encapsulation of toxins in concrete or asphalt.',
    'htc.card3.toxic.warning':          '⚠ HTC immobilises {metals} in the carbon matrix and reduces {plastics} to <0.01 mm.',
    'htc.unit.kg':                      'kg',
    'htc.unit.mjkg':                    'MJ/kg',
}

# ── helpers ─────────────────────────────────────────────────────────────────

def patch_json(path, new_keys):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    for k, v in new_keys.items():
        data[k] = v
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)
    print(f'  patched {path.name}: +{len(new_keys)} keys')

MARKER = '    <!-- ============================================================ -->\n    <!-- BLOCK 2b: AI Agent Chat'

def patch_html(path, block):
    with open(path, encoding='utf-8') as f:
        src = f.read()
    if 'htc-simulator' in src:
        print(f'  {path.name}: HTC section already present, skipping')
        return
    idx = src.find(MARKER)
    if idx == -1:
        raise RuntimeError(f'Marker not found in {path}')
    # Insert block right before the marker (keep the blank lines before marker)
    out = src[:idx] + block + '\n' + src[idx:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(out)
    print(f'  patched {path.name}: HTC section inserted')

def patch_css(path, css):
    with open(path, encoding='utf-8') as f:
        src = f.read()
    if 'htc-section' in src:
        print(f'  {path.name}: HTC CSS already present, skipping')
        return
    with open(path, 'w', encoding='utf-8') as f:
        f.write(src + css)
    print(f'  patched {path.name}: HTC CSS appended')

# ── run ──────────────────────────────────────────────────────────────────────
print('Patching simulator.html ...')
patch_html(SIM, HTC_BLOCK)

print('Patching styles.css ...')
patch_css(CSS, HTC_CSS)

print('Patching translations ...')
patch_json(UA, UA_NEW)
patch_json(PL, PL_NEW)
patch_json(EU, EU_NEW)

print('Done.')

#!/usr/bin/env python3
# encoding: utf-8
"""Replace HTC Chemical Simulator section with bubble-tab UI + single rpt-card."""

import json, pathlib

ROOT = pathlib.Path('/Users/max/Waste')
SIM  = ROOT / 'biotc/simulator.html'
CSS  = ROOT / 'styles.css'
UA   = ROOT / 'translations/ua.json'
PL   = ROOT / 'translations/pl.json'
EU   = ROOT / 'translations/eu.json'

# ── new translation keys ────────────────────────────────────────────────────
UA_NEW = {
    'htc.source.municipal.tab':      'Міські',
    'htc.source.food.tab':           'Харчова',
    'htc.source.agro.tab':           'Агро',
    'htc.source.industrial.tab':     'Хімічна',
    'htc.reactor.before.tab':        'Сирий осад',
    'htc.reactor.after.tab':         'Зброджений',
    'htc.route.agro.short':          'Агро',
    'htc.route.fuel.short':          'SRF/RDF',
    'htc.route.construction.short':  'Будівництво',
}

PL_NEW = {
    'htc.source.municipal.tab':      'Miejskie',
    'htc.source.food.tab':           'Spożywcza',
    'htc.source.agro.tab':           'Agro',
    'htc.source.industrial.tab':     'Chemiczna',
    'htc.reactor.before.tab':        'Surowy osad',
    'htc.reactor.after.tab':         'Zfermentowany',
    'htc.route.agro.short':          'Agro',
    'htc.route.fuel.short':          'SRF/RDF',
    'htc.route.construction.short':  'Budownictwo',
}

EU_NEW = {
    'htc.source.municipal.tab':      'Municipal',
    'htc.source.food.tab':           'Food',
    'htc.source.agro.tab':           'Agro',
    'htc.source.industrial.tab':     'Chemical',
    'htc.reactor.before.tab':        'Raw sludge',
    'htc.reactor.after.tab':         'Digested',
    'htc.route.agro.short':          'Agro',
    'htc.route.fuel.short':          'SRF/RDF',
    'htc.route.construction.short':  'Construction',
}

def patch_json(path, new_keys):
    data = json.load(open(path, encoding='utf-8'))
    for k, v in new_keys.items():
        data[k] = v
    json.dump(data, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2, sort_keys=True)
    print(f'  {path.name}: +{len(new_keys)} keys')

# ── new HTC block (HTML + inline script) ───────────────────────────────────
NEW_BLOCK = '''\
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

            <!-- Source type — bubble tabs -->
            <div class="srp-field">
              <label class="srp-label">{{htc.source.label}}</label>
              <div class="srp-sc-tabs" role="tablist">
                <button type="button" class="srp-sc-tab active" data-source="municipal"  role="tab">{{htc.source.municipal.tab}}</button>
                <button type="button" class="srp-sc-tab"        data-source="food"       role="tab">{{htc.source.food.tab}}</button>
                <button type="button" class="srp-sc-tab"        data-source="agro"       role="tab">{{htc.source.agro.tab}}</button>
                <button type="button" class="srp-sc-tab"        data-source="industrial" role="tab">{{htc.source.industrial.tab}}</button>
              </div>
            </div>

            <!-- Reactor position — bubble toggle -->
            <div class="srp-field">
              <label class="srp-label">{{htc.reactor.label}}</label>
              <div class="srp-sc-tabs" role="tablist">
                <button type="button" class="srp-sc-tab active" data-reactor="before" role="tab">{{htc.reactor.before.tab}}</button>
                <button type="button" class="srp-sc-tab"        data-reactor="after"  role="tab">{{htc.reactor.after.tab}}</button>
              </div>
            </div>

            <!-- Organic % stepper -->
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

            <!-- Ash (derived, read-only) -->
            <div class="srp-field">
              <div class="srp-label-row">
                <label class="srp-label">{{htc.ash.label}}</label>
                <span class="srp-label-unit">{{htc.organic.unit}}</span>
              </div>
              <div class="htc-ash-row"><span id="htc-ash-val">30</span>%</div>
            </div>

            <!-- Contaminant badges -->
            <div class="htc-badges">
              <span class="htc-badge htc-badge--warn" id="htc-badge-metals"></span>
              <span class="htc-badge htc-badge--warn" id="htc-badge-plastics"></span>
            </div>

          </div>
          </div><!-- /.srp-col left -->

          <!-- RIGHT: single rpt-card (same pattern as economics results) -->
          <div class="srp-col">
          <p class="section-label">{{sim.result.label}}</p>
          <div class="htc-results">

            <div class="rpt-card" id="htc-route-card">

              <!-- Route headline — mirrors ROI kpi row -->
              <div class="rpt-kpi">
                <span class="rpt-kpi-lbl">{{htc.card3.title}}</span>
                <span class="rpt-kpi-val" id="htc-kpi-route">&#8212;</span>
              </div>
              <p class="rpt-kpi-note" id="htc-route-long"></p>

              <!-- Hydrochar passport -->
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

              <!-- Liquor to digester -->
              <div class="rpt-section">
                <div class="rpt-sh">{{htc.card2.title}}</div>
                <div class="rpt-row rpt-row--sum">
                  <span>{{htc.card2.carbon}}</span>
                  <span class="rpt-num rpt-teal" id="htc-liquor-carbon">&#8212;</span>
                </div>
                <div class="rpt-row rpt-row--sub">{{htc.card2.hint}}</div>
              </div>

              <!-- Conclusion: route description + toxic warning -->
              <div class="rpt-conclusion">
                <div class="rpt-sh">{{sim.conclusion.label}}</div>
                <p class="rpt-conclusion-body" id="htc-route-text"></p>
                <p class="htc-toxic-warning" id="htc-toxic-warning" style="display:none"></p>
              </div>

            </div><!-- /.rpt-card -->

          </div>
          </div><!-- /.srp-col right -->

        </div><!-- /.htc-grid -->

      </div>
    </section>

    <!-- HTC simulator logic -->
    <script>
    (function(){
      var ROUTE_AGRO_SHORT  = '{{htc.route.agro.short}}';
      var ROUTE_FUEL_SHORT  = '{{htc.route.fuel.short}}';
      var ROUTE_CONST_SHORT = '{{htc.route.construction.short}}';
      var ROUTE_AGRO_LONG   = '{{htc.card3.route.agro}}';
      var ROUTE_FUEL_LONG   = '{{htc.card3.route.fuel}}';
      var ROUTE_CONST_LONG  = '{{htc.card3.route.construction}}';
      var ROUTE_TEXT_AGRO   = '{{htc.card3.agro.text}}';
      var ROUTE_TEXT_FUEL   = '{{htc.card3.fuel.text}}';
      var ROUTE_TEXT_CONST  = '{{htc.card3.construction.text}}';
      var TOXIC_WARNING     = '{{htc.card3.toxic.warning}}';
      var BADGE_METALS      = '{{htc.badge.metals}}';
      var BADGE_PLASTICS    = '{{htc.badge.microplastics}}';
      var UNIT_KG           = '{{htc.unit.kg}}';
      var UNIT_MJKG         = '{{htc.unit.mjkg}}';

      var PRESETS = {
        municipal:  { organic: 70, metals: '{{htc.preset.municipal.metals}}',  plastics: '{{htc.preset.municipal.plastics}}',  toxic: true  },
        food:       { organic: 85, metals: '{{htc.preset.food.metals}}',       plastics: '{{htc.preset.food.plastics}}',       toxic: false },
        agro:       { organic: 75, metals: '{{htc.preset.agro.metals}}',       plastics: '{{htc.preset.agro.plastics}}',       toxic: false },
        industrial: { organic: 25, metals: '{{htc.preset.industrial.metals}}', plastics: '{{htc.preset.industrial.plastics}}', toxic: true  }
      };

      var currentSource  = 'municipal';
      var currentReactor = 'before';
      var organicEl = document.getElementById('htc-organic');

      function htcCalc() {
        var organic = Math.max(10, Math.min(95, parseFloat(organicEl.value) || 70));
        var preset  = PRESETS[currentSource] || PRESETS.municipal;

        document.getElementById('htc-ash-val').textContent = (100 - organic).toFixed(0);

        /* Contaminant badges */
        var badgeMet = document.getElementById('htc-badge-metals');
        var badgePls = document.getElementById('htc-badge-plastics');
        badgeMet.textContent = BADGE_METALS + ': ' + preset.metals;
        badgePls.textContent = BADGE_PLASTICS + ': ' + preset.plastics;
        badgeMet.className = 'htc-badge htc-badge--' + (preset.toxic ? (currentSource === 'industrial' ? 'bad' : 'warn') : 'ok');
        badgePls.className = 'htc-badge htc-badge--' + (preset.toxic ? 'warn' : 'ok');

        /* Chemistry — basis: 1000 kg dry matter */
        var inputOrganicMass  = 1000 * (organic / 100);
        var inputAshMass      = 1000 - inputOrganicMass;
        var inputCarbonMass   = inputOrganicMass * 0.55;
        var otherOrganicsMass = inputOrganicMass - inputCarbonMass;
        var c_retention       = currentReactor === 'after' ? 0.85 : 0.70;
        var charCarbonMass    = inputCarbonMass * c_retention;
        var liquorCarbonMass  = inputCarbonMass - charCarbonMass;
        var charOtherOrganics = otherOrganicsMass * 0.40;
        var totalCharMass     = charCarbonMass + inputAshMass + charOtherOrganics;
        var newCarbonPct      = (charCarbonMass / totalCharMass) * 100;
        var newAshPct         = (inputAshMass   / totalCharMass) * 100;
        var calorific         = newCarbonPct * 0.35;

        /* Passport rows */
        document.getElementById('htc-char-mass').textContent     = Math.round(totalCharMass) + ' ' + UNIT_KG;
        document.getElementById('htc-char-carbon').textContent   = newCarbonPct.toFixed(1) + '%';
        document.getElementById('htc-char-ash').textContent      = newAshPct.toFixed(1) + '%';
        document.getElementById('htc-calorific').textContent     = calorific.toFixed(1) + ' ' + UNIT_MJKG;
        document.getElementById('htc-liquor-carbon').textContent = Math.round(liquorCarbonMass) + ' ' + UNIT_KG;

        /* Route headline */
        var route  = !preset.toxic ? 'agro' : (calorific >= 12 ? 'fuel' : 'construction');
        var kpiEl  = document.getElementById('htc-kpi-route');
        kpiEl.textContent = { agro: ROUTE_AGRO_SHORT, fuel: ROUTE_FUEL_SHORT, construction: ROUTE_CONST_SHORT }[route];
        kpiEl.className   = 'rpt-kpi-val htc-route--' + route;
        document.getElementById('htc-route-long').textContent  = { agro: ROUTE_AGRO_LONG, fuel: ROUTE_FUEL_LONG,  construction: ROUTE_CONST_LONG  }[route];
        document.getElementById('htc-route-text').textContent  = { agro: ROUTE_TEXT_AGRO, fuel: ROUTE_TEXT_FUEL,  construction: ROUTE_TEXT_CONST  }[route];

        /* Toxic warning */
        var warnEl = document.getElementById('htc-toxic-warning');
        if (preset.toxic) {
          warnEl.style.display = '';
          warnEl.textContent = TOXIC_WARNING.replace('{metals}', preset.metals).replace('{plastics}', preset.plastics);
        } else {
          warnEl.style.display = 'none';
        }
      }

      /* Source tabs */
      document.querySelectorAll('.srp-sc-tab[data-source]').forEach(function(btn) {
        btn.addEventListener('click', function() {
          document.querySelectorAll('.srp-sc-tab[data-source]').forEach(function(b){ b.classList.remove('active'); });
          btn.classList.add('active');
          currentSource = btn.dataset.source;
          organicEl.value = (PRESETS[currentSource] || PRESETS.municipal).organic;
          htcCalc();
        });
      });

      /* Reactor tabs */
      document.querySelectorAll('.srp-sc-tab[data-reactor]').forEach(function(btn) {
        btn.addEventListener('click', function() {
          document.querySelectorAll('.srp-sc-tab[data-reactor]').forEach(function(b){ b.classList.remove('active'); });
          btn.classList.add('active');
          currentReactor = btn.dataset.reactor;
          htcCalc();
        });
      });

      /* Organic stepper — click fires after global handler updates el.value */
      document.querySelectorAll('.srp-btn-step[data-for="htc-organic"]').forEach(function(b){
        b.addEventListener('click', htcCalc);
      });
      organicEl.addEventListener('input', htcCalc);

      htcCalc();
    })();
    </script>

'''

# ── CSS additions ───────────────────────────────────────────────────────────
ROUTE_CSS = '''
/* HTC route kpi colour variants */
.rpt-kpi-val.htc-route--agro         { color: var(--color-teal); }
.rpt-kpi-val.htc-route--fuel         { color: #b45309; }
.rpt-kpi-val.htc-route--construction { color: #64748b; }
'''

# ── replace section ─────────────────────────────────────────────────────────
MARKER_START = '    <!-- ============================================================ -->\n    <!-- BLOCK 2a: HTC Chemical Simulator'
MARKER_END   = '\n    <!-- ============================================================ -->\n    <!-- BLOCK 2b: AI Agent Chat'

def replace_htc_section(path, new_block):
    src = open(path, encoding='utf-8').read()
    start = src.find(MARKER_START)
    end   = src.find(MARKER_END)
    if start == -1 or end == -1:
        raise RuntimeError(f'Markers not found in {path}')
    out = src[:start] + new_block + src[end:]
    open(path, 'w', encoding='utf-8').write(out)
    print(f'  {path.name}: HTC section replaced')

def append_css(path, css):
    src = open(path, encoding='utf-8').read()
    if 'htc-route--agro' in src:
        print(f'  {path.name}: route CSS already present')
        return
    open(path, 'w', encoding='utf-8').write(src + css)
    print(f'  {path.name}: route CSS appended')

# ── run ──────────────────────────────────────────────────────────────────────
print('Patching translations ...')
patch_json(UA, UA_NEW)
patch_json(PL, PL_NEW)
patch_json(EU, EU_NEW)

print('Replacing HTC section in simulator.html ...')
replace_htc_section(SIM, NEW_BLOCK)

print('Adding route CSS ...')
append_css(CSS, ROUTE_CSS)

print('Done.')

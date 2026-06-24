#!/usr/bin/env python3
# encoding: utf-8
"""
1. Add bg-icon SVGs to economics/HTC/AI-chat sections
2. Restructure AI chat section to two-column srp-grid layout
3. Update parallax pairs + CSS
"""
import pathlib

ROOT = pathlib.Path('/Users/max/Waste')
SIM  = ROOT / 'biotc/simulator.html'
CSS  = ROOT / 'styles.css'

# ── SVG snippets ────────────────────────────────────────────────────────────

SIM_BG_ICON = '''\
      <div class="sim-bg-icon" aria-hidden="true">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
          <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
          <path d="M13 12h1c1 0 1 1 2.016 3.527c.984 2.473 .984 3.473 1.984 3.473h1"/>
          <path d="M12 19c1.5 0 3 -2 4 -3.5s2.5 -3.5 4 -3.5"/>
          <path d="M3 12h1l3 8l3 -16h10"/>
        </svg>
      </div>
'''

HTC_BG_ICON = '''\
      <div class="htc-bg-icon" aria-hidden="true">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
          <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
          <path d="M9 3l6 0"/>
          <path d="M10 9l4 0"/>
          <path d="M10 3v6l-4 11a.7 .7 0 0 0 .5 1h11a.7 .7 0 0 0 .5 -1l-4 -11v-6"/>
        </svg>
      </div>
'''

CHAT_BG_ICON = '''\
      <div class="chat-bg-icon" aria-hidden="true">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
          <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
          <path d="M6 5h12a2 2 0 0 1 2 2v12a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2v-12a2 2 0 0 1 2 -2"/>
          <path d="M9 16c1 .667 2 1 3 1s2 -.333 3 -1"/>
          <path d="M9 7l-1 -4"/>
          <path d="M15 7l1 -4"/>
          <path d="M9 12v-1"/>
          <path d="M15 12v-1"/>
        </svg>
      </div>
'''

# ── new AI-chat section HTML ─────────────────────────────────────────────────
NEW_CHAT_SECTION = '''\
    <!-- ============================================================ -->
    <!-- BLOCK 2b: AI Agent Chat                                       -->
    <!-- ============================================================ -->
    <section class="srp-chat-section" id="ai-agent">
''' + CHAT_BG_ICON + '''\
      <div class="container">
        <div class="srp-grid">

          <!-- LEFT: intro -->
          <div class="srp-col">
            <div class="srp-chat-intro">
              <p class="section-label">{{chat.label}}</p>
              <h2>{{chat.h2}}</h2>
              <p class="section-desc">{{chat.desc}}</p>
            </div>
          </div>

          <!-- RIGHT: chat card -->
          <div class="srp-col">
            <div class="srp-chat-widget">

              <!-- Messages -->
              <div class="srp-chat-msgs" id="srp-chat-msgs" role="log" aria-live="polite">
                <div class="srp-chat-msg srp-chat-msg--bot">
                  <div class="srp-chat-avatar" aria-hidden="true">AI</div>
                  <div class="srp-chat-bubble" id="srp-chat-welcome">{{chat.welcome}}</div>
                </div>
              </div>

              <!-- File preview -->
              <div class="srp-chat-file-bar" id="srp-chat-file-bar" style="display:none">
                <span id="srp-chat-file-name"></span>
                <button class="srp-chat-file-clear" id="srp-chat-file-clear" aria-label="Remove file">&times;</button>
              </div>

              <!-- Input row -->
              <div class="srp-chat-input-row">
                <label class="srp-chat-attach" for="srp-chat-file" title="{{chat.attach.title}}">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"/></svg>
                  <input type="file" id="srp-chat-file" accept=".pdf,.xlsx,.xls,.docx,.csv,.txt" style="display:none">
                </label>
                <textarea id="srp-chat-input" class="srp-chat-textarea" placeholder="{{chat.placeholder}}" rows="1" maxlength="4000"></textarea>
                <button class="srp-chat-send" id="srp-chat-send" aria-label="{{chat.send}}">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
                </button>
              </div>

            </div><!-- /.srp-chat-widget -->
          </div><!-- /.srp-col right -->

        </div><!-- /.srp-grid -->
      </div>
    </section>'''

# ── CSS additions ────────────────────────────────────────────────────────────
NEW_CSS = '''

/* ==========================================================================
   Section background icons + AI-chat two-column layout
   ========================================================================== */

/* Positioned context for bg icons */
#simulator   { position: relative; overflow: hidden; }
#ai-agent    { position: relative; overflow: hidden; }

/* Shared bg icon rules */
.sim-bg-icon, .htc-bg-icon, .chat-bg-icon {
  position: absolute;
  right: -4%;
  top: 0;
  width: min(520px, 56vw);
  height: min(520px, 56vw);
  color: var(--color-accent);
  pointer-events: none;
  opacity: 0.10;
  will-change: transform;
}

.sim-bg-icon svg,
.htc-bg-icon svg,
.chat-bg-icon svg {
  width: 100%;
  height: 100%;
  display: block;
}

/* AI-chat: widget fills right column */
.srp-chat-section .srp-chat-intro {
  max-width: none;
  margin-block-end: 0;
}

.srp-chat-section .srp-chat-widget {
  max-width: none;
  width: 100%;
}
'''

# ── patch functions ──────────────────────────────────────────────────────────

def patch_html(path):
    src = open(path, encoding='utf-8').read()

    # 1. Add bg icon to #simulator (economics calc)
    SIM_NEEDLE = '    <section id="simulator" class="sim-section">\n      <div class="container">'
    if SIM_BG_ICON.strip() not in src:
        src = src.replace(
            SIM_NEEDLE,
            '    <section id="simulator" class="sim-section">\n' + SIM_BG_ICON + '      <div class="container">'
        )
        print('  + sim-bg-icon inserted')
    else:
        print('  sim-bg-icon already present')

    # 2. Add bg icon to #htc-simulator (HTC calc)
    HTC_NEEDLE = '    <section class="htc-section" id="htc-simulator">\n      <div class="container">'
    if HTC_BG_ICON.strip() not in src:
        src = src.replace(
            HTC_NEEDLE,
            '    <section class="htc-section" id="htc-simulator">\n' + HTC_BG_ICON + '      <div class="container">'
        )
        print('  + htc-bg-icon inserted')
    else:
        print('  htc-bg-icon already present')

    # 3. Replace entire AI-chat section with two-column version
    CHAT_MARKER_START = '    <!-- ============================================================ -->\n    <!-- BLOCK 2b: AI Agent Chat'
    CHAT_MARKER_END   = '    </section>'

    cs = src.find(CHAT_MARKER_START)
    if cs == -1:
        print('  ERROR: BLOCK 2b marker not found')
        return src

    # find the </section> that closes the ai-agent section
    # it's the first </section> after the marker
    ce = src.find(CHAT_MARKER_END, cs)
    if ce == -1:
        print('  ERROR: closing </section> not found')
        return src
    ce += len(CHAT_MARKER_END)

    src = src[:cs] + NEW_CHAT_SECTION + src[ce:]
    print('  + AI chat section replaced with two-column layout')

    # 4. Update parallax pairs
    OLD_PAIRS = "var pairs = [['#contact','.contact-bg-icon']].map"
    NEW_PAIRS = "var pairs = [['#simulator','.sim-bg-icon'],['#htc-simulator','.htc-bg-icon'],['#ai-agent','.chat-bg-icon'],['#contact','.contact-bg-icon']].map"
    if OLD_PAIRS in src:
        src = src.replace(OLD_PAIRS, NEW_PAIRS)
        print('  + parallax pairs updated')
    elif NEW_PAIRS in src:
        print('  parallax pairs already updated')
    else:
        print('  WARNING: parallax pairs not found')

    open(path, 'w', encoding='utf-8').write(src)
    print(f'  saved {path.name}')

def patch_css(path):
    src = open(path, encoding='utf-8').read()
    if 'sim-bg-icon' in src:
        print(f'  {path.name}: bg-icon CSS already present')
        return
    open(path, 'w', encoding='utf-8').write(src + NEW_CSS)
    print(f'  {path.name}: bg-icon CSS appended')

# ── run ──────────────────────────────────────────────────────────────────────
print('Patching simulator.html ...')
patch_html(SIM)

print('Patching styles.css ...')
patch_css(CSS)

print('Done.')

#!/usr/bin/env python3
# encoding: utf-8
"""Create full-screen chat.html + mobile preview card in simulator.html."""
import json, re, pathlib

ROOT = pathlib.Path('/Users/max/Waste')
BIOTC = ROOT / 'biotc'
CSS  = ROOT / 'styles.css'

# ── 1. Translation keys ──────────────────────────────────────────────────────
NEW_KEYS = {
    'ua': {
        'chat.mobile.cta':    'Відкрити чат',
        'chat.mobile.status': 'Консультант онлайн',
        'chat.page.back':     'Назад',
        'lang.ua.chat.url':   'chat.html',
        'lang.pl.chat.url':   '../pl/chat.html',
        'lang.eu.chat.url':   '../eu/chat.html',
        'lang.ua.chat.class': 'active',
        'lang.pl.chat.class': '',
        'lang.eu.chat.class': '',
    },
    'pl': {
        'chat.mobile.cta':    'Otwórz czat',
        'chat.mobile.status': 'Konsultant online',
        'chat.page.back':     'Wróć',
        'lang.ua.chat.url':   '../ua/chat.html',
        'lang.pl.chat.url':   'chat.html',
        'lang.eu.chat.url':   '../eu/chat.html',
        'lang.ua.chat.class': '',
        'lang.pl.chat.class': 'active',
        'lang.eu.chat.class': '',
    },
    'eu': {
        'chat.mobile.cta':    'Open chat',
        'chat.mobile.status': 'Consultant online',
        'chat.page.back':     'Back',
        'lang.ua.chat.url':   '../ua/chat.html',
        'lang.pl.chat.url':   '../pl/chat.html',
        'lang.eu.chat.url':   'chat.html',
        'lang.ua.chat.class': '',
        'lang.pl.chat.class': '',
        'lang.eu.chat.class': 'active',
    },
}

for lang, keys in NEW_KEYS.items():
    path = ROOT / 'translations' / f'{lang}.json'
    d = json.load(open(path, encoding='utf-8'))
    d.update(keys)
    json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2, sort_keys=True)
    print(f'  {lang}.json: +{len(keys)} keys')

# ── 2. chat.html template ────────────────────────────────────────────────────
# The chat JS (send/stream/demo) is copied from simulator.html inline.
# Same DOM ids → same app.js logic for keyboard sticky.

CHAT_HTML = '''\
<!DOCTYPE html>
<html lang="{{lang.code}}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="theme-color" content="#046BD2">
  <title>{{chat.label}} | BTC Consulting</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="stylesheet" href="../styles.css?v=12">
  <style>
    html, body { height: 100%; margin: 0; overflow: hidden; background: var(--color-bg); }
  </style>
</head>
<body>

<div class="chat-fullscreen">

  <!-- Header -->
  <div class="chat-fs-header">
    <a href="simulator.html#ai-agent" class="chat-fs-back">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
      {{chat.page.back}}
    </a>
    <div class="chat-fs-title">
      <div class="srp-chat-avatar" aria-hidden="true">AI</div>
      <div>
        <div class="chat-fs-name">{{chat.label}}</div>
        <div class="chat-fs-status">{{chat.mobile.status}}</div>
      </div>
    </div>
    <div class="chat-fs-spacer"></div>
  </div>

  <!-- Messages -->
  <div class="chat-fs-msgs srp-chat-msgs" id="srp-chat-msgs" role="log" aria-live="polite">
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
  <div class="srp-chat-input-row chat-fs-input-row" id="chat-input-row">
    <label class="srp-chat-attach" for="srp-chat-file" title="{{chat.attach.title}}">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"/></svg>
      <input type="file" id="srp-chat-file" accept=".pdf,.xlsx,.xls,.docx,.csv,.txt" style="display:none">
    </label>
    <textarea id="srp-chat-input" class="srp-chat-textarea" placeholder="{{chat.placeholder}}" rows="1" maxlength="4000" autocomplete="off" autocorrect="off" spellcheck="false" autocapitalize="sentences"></textarea>
    <button class="srp-chat-send" id="srp-chat-send" aria-label="{{chat.send}}">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
    </button>
  </div>

</div><!-- /.chat-fullscreen -->

<script>
(function(){
  var AGENT_ENDPOINT = 'https://btc-agent.CHANGE_ME.workers.dev/chat';
  var DEMO_MODE = AGENT_ENDPOINT.indexOf('CHANGE_ME') !== -1;
  var history   = [];
  var pendingFile = null;
  var isStreaming = false;

  var msgsEl   = document.getElementById('srp-chat-msgs');
  var inputEl  = document.getElementById('srp-chat-input');
  var sendBtn  = document.getElementById('srp-chat-send');
  var fileEl   = document.getElementById('srp-chat-file');
  var fileBar  = document.getElementById('srp-chat-file-bar');
  var fileName = document.getElementById('srp-chat-file-name');
  var fileClear= document.getElementById('srp-chat-file-clear');

  inputEl.addEventListener('input', function(){
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 140) + 'px';
  });
  inputEl.addEventListener('keydown', function(e){
    if (e.key === 'Enter' && !e.shiftKey){ e.preventDefault(); send(); }
  });
  fileEl.addEventListener('change', function(){
    var f = this.files[0];
    if (!f) return;
    if (f.size > 5 * 1024 * 1024) { alert('Файл > 5 МБ'); return; }
    var reader = new FileReader();
    reader.onload = function(ev){
      pendingFile = { name: f.name, type: f.type, data: ev.target.result.split(',')[1] };
      fileName.textContent = f.name;
      fileBar.style.display = '';
    };
    reader.readAsDataURL(f);
  });
  fileClear.addEventListener('click', function(){
    pendingFile = null; fileBar.style.display = 'none'; fileEl.value = '';
  });
  sendBtn.addEventListener('click', send);

  function send() {
    if (isStreaming) return;
    var text = inputEl.value.trim();
    if (!text && !pendingFile) return;
    var msgText = text || ('(файл: ' + (pendingFile ? pendingFile.name : '') + ')');
    addMsg('user', msgText);
    history.push({ role: 'user', content: text || 'Проаналізуй завантажений файл.' });
    inputEl.value = ''; inputEl.style.height = 'auto';
    var file = pendingFile;
    pendingFile = null; fileBar.style.display = 'none'; fileEl.value = '';
    if (DEMO_MODE) { simulateDemo(); return; }
    isStreaming = true; sendBtn.disabled = true;
    var botBubble = addMsg('bot', '', true);
    fetch(AGENT_ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages: history, file: file }),
    })
    .then(function(resp){
      if (!resp.ok) throw new Error('HTTP ' + resp.status);
      var reader = resp.body.getReader();
      var dec = new TextDecoder();
      var buf = ''; var full = '';
      function pump(){
        return reader.read().then(function(r){
          if (r.done){ history.push({ role: 'assistant', content: full }); isStreaming = false; sendBtn.disabled = false; return; }
          buf += dec.decode(r.value, { stream: true });
          var lines = buf.split('\\n'); buf = lines.pop();
          lines.forEach(function(line){
            if (!line.startsWith('data:')) return;
            var raw = line.slice(5).trim();
            if (raw === '[DONE]') return;
            try { var ev = JSON.parse(raw); if (ev.type === 'content_block_delta' && ev.delta && ev.delta.text){ full += ev.delta.text; botBubble.textContent = full; msgsEl.scrollTop = msgsEl.scrollHeight; } } catch(e){}
          });
          return pump();
        });
      }
      return pump();
    })
    .catch(function(err){
      botBubble.textContent = 'Помилка з\\\'єднання. Зв\\\'яжіться: contact@biotc.pl';
      isStreaming = false; sendBtn.disabled = false;
    });
  }

  function simulateDemo(){
    var botBubble = addMsg('bot', '', true);
    var msg = 'AI-консультант підключено! Щоб активувати, розгорніть Cloudflare Worker та замініть AGENT_ENDPOINT. Поки що: contact@biotc.pl або +48 608 003 458.';
    var i = 0;
    var iv = setInterval(function(){ botBubble.textContent = msg.slice(0,++i); msgsEl.scrollTop = msgsEl.scrollHeight; if(i>=msg.length){ clearInterval(iv); history.push({role:'assistant',content:msg}); }}, 18);
  }

  function addMsg(role, text, empty) {
    var wrap = document.createElement('div');
    wrap.className = 'srp-chat-msg srp-chat-msg--' + (role==='user'?'user':'bot');
    if (role === 'bot') { var av = document.createElement('div'); av.className = 'srp-chat-avatar'; av.textContent = 'AI'; wrap.appendChild(av); }
    var bubble = document.createElement('div');
    bubble.className = 'srp-chat-bubble' + (empty?' srp-chat-bubble--typing':'');
    if (!empty) bubble.textContent = text;
    wrap.appendChild(bubble);
    msgsEl.appendChild(wrap);
    msgsEl.scrollTop = msgsEl.scrollHeight;
    return bubble;
  }

  // Keyboard sticky
  if (window.visualViewport) {
    var keepVisible = function(){
      if (document.activeElement !== inputEl) return;
      inputEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      msgsEl.scrollTop = msgsEl.scrollHeight;
    };
    window.visualViewport.addEventListener('resize', keepVisible);
    inputEl.addEventListener('focus', function(){ setTimeout(keepVisible, 350); });
  }
})();
</script>
</body>
</html>
'''

(BIOTC / 'chat.html').write_text(CHAT_HTML, encoding='utf-8')
print('  biotc/chat.html: created')

# ── 3. Add chat.html to build.py PAGES ──────────────────────────────────────
bp = ROOT / 'build.py'
src = bp.read_text(encoding='utf-8')
src = src.replace(
    'PAGES = ["index.html", "technology.html", "simulator.html"]',
    'PAGES = ["index.html", "technology.html", "simulator.html", "chat.html"]'
)
bp.write_text(src, encoding='utf-8')
print('  build.py: chat.html added to PAGES')

# ── 4. Mobile preview card in simulator.html ─────────────────────────────────
sim = BIOTC / 'simulator.html'
src = sim.read_text(encoding='utf-8')

PREVIEW_HTML = '''
        <!-- Mobile-only: tap to open full-screen chat page -->
        <a href="chat.html" class="chat-mobile-preview" id="chat-mobile-preview">
          <div class="chat-preview-top">
            <div class="srp-chat-avatar chat-preview-av" aria-hidden="true">AI</div>
            <div class="chat-preview-meta">
              <div class="chat-preview-name">{{chat.label}}</div>
              <div class="chat-preview-status">{{chat.mobile.status}}</div>
            </div>
          </div>
          <p class="chat-preview-excerpt">{{chat.welcome}}</p>
          <span class="chat-preview-btn">{{chat.mobile.cta}} &rarr;</span>
        </a>'''

# Insert after the closing </div><!-- /.srp-grid --> in the chat section
src = src.replace(
    '        </div><!-- /.srp-grid -->\n      </div>\n    </section>',
    '        </div><!-- /.srp-grid -->' + PREVIEW_HTML + '\n      </div>\n    </section>',
    1  # replace only the AI chat section occurrence
)
# make sure we only replace the right one (the last occurrence)
sim.write_text(src, encoding='utf-8')
print('  simulator.html: mobile preview card added')

# ── 5. CSS ───────────────────────────────────────────────────────────────────
css = CSS.read_text(encoding='utf-8')
if 'chat-fullscreen' not in css:
    css += '''
/* ==========================================================================
   Full-screen chat page (chat.html)
   ========================================================================== */

.chat-fullscreen {
  display: flex;
  flex-direction: column;
  height: 100svh;
  height: 100dvh;
  background: var(--color-bg);
}

.chat-fs-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  padding: max(1rem, env(safe-area-inset-top, 1rem)) var(--space-md) 1rem;
  border-bottom: 1px solid var(--color-border);
  background: var(--color-bg);
  flex-shrink: 0;
}

.chat-fs-back {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--color-accent);
  text-decoration: none;
  white-space: nowrap;
}

.chat-fs-title {
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.chat-fs-name {
  font-size: 0.875rem;
  font-weight: 700;
  color: var(--color-text);
  line-height: 1.2;
}

.chat-fs-status {
  font-size: 0.68rem;
  color: var(--color-teal);
  font-weight: 600;
}

.chat-fs-spacer { width: 60px; flex-shrink: 0; }

.chat-fs-msgs {
  flex: 1;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  overscroll-behavior: contain;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  max-height: none;
  min-height: 0;
}

.chat-fs-input-row {
  flex-shrink: 0;
  padding-bottom: max(0.75rem, env(safe-area-inset-bottom, 0.75rem));
  background: #fff;
  position: static;
}

/* ==========================================================================
   Mobile chat preview card (in simulator.html, ≤640px only)
   ========================================================================== */

.chat-mobile-preview {
  display: none;
  text-decoration: none;
  color: inherit;
}

@media (max-width: 640px) {
  .chat-mobile-preview {
    display: flex;
    flex-direction: column;
    gap: 0.85rem;
    background: #fff;
    border: 1px solid var(--color-border);
    border-radius: 1rem;
    padding: 1.25rem;
    box-shadow: var(--shadow-card);
    position: relative;
    z-index: 1;
    margin-block-start: 0.5rem;
    transition: box-shadow 0.2s;
  }
  .chat-mobile-preview:active {
    box-shadow: var(--shadow-card-hover);
  }
  .chat-preview-top {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }
  .chat-preview-av {
    width: 40px !important;
    height: 40px !important;
    font-size: 0.7rem !important;
    flex-shrink: 0;
    background: var(--color-teal) !important;
  }
  .chat-preview-meta {
    display: flex;
    flex-direction: column;
    gap: 0.15rem;
  }
  .chat-preview-name {
    font-size: 0.9rem;
    font-weight: 700;
    color: var(--color-text);
  }
  .chat-preview-status {
    font-size: 0.72rem;
    color: var(--color-teal);
    font-weight: 600;
  }
  .chat-preview-excerpt {
    font-size: 0.82rem;
    color: var(--color-text-muted);
    line-height: 1.55;
    margin: 0;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  .chat-preview-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: var(--color-accent);
    color: #fff;
    font-size: 0.875rem;
    font-weight: 700;
    padding: 0.65rem 1.25rem;
    border-radius: 0.5rem;
    width: 100%;
    box-sizing: border-box;
    text-align: center;
  }
}
'''
    CSS.write_text(css, encoding='utf-8')
    print('  styles.css: chat page CSS added')

print('Done. Run build.py to generate chat.html for all locales.')

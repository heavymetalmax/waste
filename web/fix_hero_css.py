import re

with open('industrial.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the old Hero Stage Static Layout block we added
css = re.sub(r'/\* --- Hero Stage Static Layout --- \*/.*?@media.*?\}', '', css, flags=re.DOTALL)
# also just in case it didn't match:
css = re.sub(r'/\* --- Hero Stage Static Layout --- \*/.*', '', css, flags=re.DOTALL)

new_css = '''
/* --- Hero Stage Financial Index Layout --- */
.hero-stage {
  position: relative !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 0 !important;
  height: auto !important;
  width: 100% !important;
  margin-top: 0 !important;
  border-top: 3px solid #111 !important;
  border-bottom: 1px solid #111 !important;
  padding-block: 0 !important;
  background: transparent !important;
}

.stage-stat {
  position: relative !important;
  visibility: visible !important;
  opacity: 1 !important;
  transform: none !important;
  top: auto !important;
  left: auto !important;
  right: auto !important;
  bottom: auto !important;
  width: 100% !important;
  margin: 0 !important;
  padding: 1.5rem 0 !important;
  display: flex !important;
  flex-direction: row !important;
  justify-content: space-between !important;
  align-items: center !important;
  background: transparent !important;
  border: none !important;
  border-bottom: 1px solid #dcd7cb !important;
  border-radius: 0 !important;
  box-shadow: none !important;
  pointer-events: auto !important;
}

.stage-stat:last-child {
  border-bottom: none !important;
}

.stage-num-wrap {
  flex: 0 0 auto !important;
  margin-right: 1.5rem !important;
  text-align: left !important;
  color: var(--accent-color) !important;
}

.stage-num {
  font-family: 'Playfair Display', serif !important;
  line-height: 1 !important;
  font-weight: 700 !important;
  display: flex !important;
  align-items: baseline !important;
  gap: 0.5rem !important;
}

.sn-pre {
  font-size: 1.25rem !important;
  font-family: 'Inter', sans-serif !important;
  font-weight: 500 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.1em !important;
  color: #111 !important;
}

.sn-val {
  font-size: 3.5rem !important;
  background: none !important;
  -webkit-text-fill-color: var(--accent-color) !important;
  color: var(--accent-color) !important;
  letter-spacing: -0.02em !important;
}

.sn-unit {
  font-size: 1.5rem !important;
  font-family: 'Inter', sans-serif !important;
  color: #111 !important;
  margin-left: 0.2rem !important;
}

.stage-text-wrap {
  flex: 1 1 auto !important;
  text-align: right !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 0.25rem !important;
}

.stage-label {
  display: block !important;
  font-family: 'Inter', sans-serif !important;
  font-size: 0.95rem !important;
  font-weight: 600 !important;
  color: #111 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.05em !important;
}

.stage-sub {
  display: block !important;
  font-family: 'Playfair Display', serif !important;
  font-size: 1.05rem !important;
  font-style: italic !important;
  color: #555 !important;
}

/* Animations reset */
.stage-stat .stage-num, .stage-stat .stage-text-wrap {
  animation: none !important;
  filter: none !important;
}

@media (min-width: 1024px) {
  .hero-stage {
    margin-left: auto;
  }
}
'''

with open('industrial.css', 'w', encoding='utf-8') as f:
    f.write(css + new_css)

import re

with open('ua/index-v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Extract and remove blueprint from Hero
blueprint_svg = re.search(r'(<svg class="hero-blueprint".*?</svg>)', html, flags=re.DOTALL)
if blueprint_svg:
    blueprint_svg_str = blueprint_svg.group(1)
    html = html.replace(blueprint_svg_str, '')
    
    # Move blueprint to the Problem section
    html = html.replace('<section id="problem">', '<section id="problem" style="position: relative; overflow: hidden;">\n    ' + blueprint_svg_str)

# 2. Replace the hero-index box with an animated checklist
old_hero_index = re.search(r'<div class="hero-index">.*?</div>\s*</div>\s*</div>\s*</section>', html, flags=re.DOTALL)

if old_hero_index:
    new_checklist = """<div class="hero-checklist">
          <div class="check-item" style="--anim-delay: 0.2s;">
            <div class="check-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="square"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </div>
            <div class="check-content">
              <span class="check-val">До 85% грант на CapEx</span>
              <span class="check-desc">Оптимізація ТЕО під вимоги FENX.01.03</span>
            </div>
          </div>
          
          <div class="check-item" style="--anim-delay: 0.6s;">
            <div class="check-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="square"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </div>
            <div class="check-content">
              <span class="check-val">Рішення для міст 15-50k</span>
              <span class="check-desc">На відміну від вендорів, ми працюємо з малими громадами</span>
            </div>
          </div>
          
          <div class="check-item" style="--anim-delay: 1.0s;">
            <div class="check-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="square"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </div>
            <div class="check-content">
              <span class="check-val">Технологія TH-AD-HTC</span>
              <span class="check-desc">Спеціально розроблена для польських осадів стічних вод</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>"""
    html = html.replace(old_hero_index.group(0), new_checklist)

with open('ua/index-v2.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add styles for the animated checklist
checklist_css = """
/* Hero Animated Checklist */
.hero-checklist {
  display: flex;
  flex-direction: column;
  gap: var(--space-md);
  margin-top: 2rem;
}

.check-item {
  display: flex;
  align-items: flex-start;
  gap: 1.5rem;
  opacity: 0;
  transform: translateX(30px);
  animation: slideInCheck 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  animation-delay: var(--anim-delay);
}

@keyframes slideInCheck {
  0% { opacity: 0; transform: translateX(30px); }
  100% { opacity: 1; transform: translateX(0); }
}

.check-icon {
  width: 48px;
  height: 48px;
  background-color: var(--color-black);
  color: var(--color-white);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  border: 4px solid var(--color-black);
}

.check-icon svg {
  width: 24px;
  height: 24px;
  stroke-dasharray: 40;
  stroke-dashoffset: 40;
  animation: drawCheck 0.5s ease-out forwards;
  animation-delay: calc(var(--anim-delay) + 0.4s);
}

@keyframes drawCheck {
  0% { stroke-dashoffset: 40; }
  100% { stroke-dashoffset: 0; }
}

.check-content {
  display: flex;
  flex-direction: column;
}

.check-val {
  font-size: 1.5rem;
  font-weight: 900;
  color: var(--color-blue);
  line-height: 1.1;
  margin-bottom: 0.5rem;
  text-transform: uppercase;
}

.check-desc {
  font-size: 1rem;
  font-weight: 600;
  color: var(--color-black);
}

@media (max-width: 768px) {
  .hero-checklist {
    margin-top: 3rem;
  }
}
"""

css += "\n" + checklist_css

with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)


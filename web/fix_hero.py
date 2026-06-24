import re

with open('ua/index-v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Extract and remove the ENTIRE hero-blueprint div
blueprint_match = re.search(r'<div class="hero-blueprint">.*?</svg>\s*</div>', html, flags=re.DOTALL)
if blueprint_match:
    blueprint_str = blueprint_match.group(0)
    html = html.replace(blueprint_str, '')
    
    # Move blueprint to the Problem section, rename class so it fits
    blueprint_str = blueprint_str.replace('hero-blueprint', 'problem-blueprint')
    html = html.replace('<section id="problem">', '<section id="problem" style="position: relative; overflow: hidden;">\n    ' + blueprint_str)

# 2. Re-write the checklist to be a "paper" element
old_checklist = re.search(r'<div class="hero-checklist">.*?</section>', html, flags=re.DOTALL)

if old_checklist:
    new_paper_html = """<div class="paper-checklist-wrapper">
          <div class="paper-checklist">
            <div class="paper-header">
              <span class="paper-title">CHECKLIST // PROJECT INITIATION</span>
            </div>
            
            <div class="check-item">
              <div class="check-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="square"><polyline points="20 6 9 17 4 12"></polyline></svg>
              </div>
              <div class="check-content">
                <span class="check-val">До 85% грант на CapEx</span>
                <span class="check-desc">Оптимізація ТЕО під вимоги FENX.01.03</span>
              </div>
            </div>
            
            <div class="check-item">
              <div class="check-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="square"><polyline points="20 6 9 17 4 12"></polyline></svg>
              </div>
              <div class="check-content">
                <span class="check-val">Рішення для міст 15-50k</span>
                <span class="check-desc">На відміну від вендорів, ми працюємо з малими громадами</span>
              </div>
            </div>
            
            <div class="check-item">
              <div class="check-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="square"><polyline points="20 6 9 17 4 12"></polyline></svg>
              </div>
              <div class="check-content">
                <span class="check-val">Технологія TH-AD-HTC</span>
                <span class="check-desc">Спеціально розроблена для польських осадів стічних вод</span>
              </div>
            </div>
            
          </div>
        </div>
      </div>
    </div>
  </section>"""
    html = html.replace(old_checklist.group(0), new_paper_html)

with open('ua/index-v2.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the hero-checklist CSS with the new paper-checklist CSS
new_css = """
/* PAPER CHECKLIST */
.paper-checklist-wrapper {
  perspective: 1000px;
}

.paper-checklist {
  background: var(--color-white);
  border: 4px solid var(--color-black);
  box-shadow: 16px 16px 0 var(--color-black);
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-top: 2rem;
  
  /* Initial state for slide-up */
  transform: translateY(150px) rotateX(10deg);
  opacity: 0;
  animation: paperSlideUp 1s cubic-bezier(0.16, 1, 0.3, 1) 0.2s forwards;
}

@keyframes paperSlideUp {
  0% { transform: translateY(150px) rotateX(10deg); opacity: 0; }
  100% { transform: translateY(0) rotateX(0); opacity: 1; }
}

.paper-header {
  border-bottom: 4px solid var(--color-black);
  padding-bottom: 1rem;
  margin-bottom: 0.5rem;
}

.paper-title {
  font-family: monospace;
  font-weight: 900;
  font-size: 1.2rem;
  letter-spacing: 0.05em;
  color: var(--color-black);
}

.paper-checklist .check-item {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  /* Reset previous slide-in */
  opacity: 1;
  transform: none;
  animation: none;
}

.paper-checklist .check-icon {
  width: 40px;
  height: 40px;
  background-color: transparent;
  color: var(--color-blue);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  border: 4px solid var(--color-black);
}

.paper-checklist .check-icon svg {
  width: 24px;
  height: 24px;
  stroke-dasharray: 40;
  stroke-dashoffset: 40;
  /* Drawing animation */
  animation: drawCheck 0.5s cubic-bezier(0.65, 0, 0.35, 1) forwards;
}

/* Staggered checkmarks */
.paper-checklist .check-item:nth-child(2) .check-icon svg { animation-delay: 1.2s; }
.paper-checklist .check-item:nth-child(3) .check-icon svg { animation-delay: 1.8s; }
.paper-checklist .check-item:nth-child(4) .check-icon svg { animation-delay: 2.4s; }

.paper-checklist .check-val {
  font-size: 1.3rem;
  font-weight: 900;
  color: var(--color-black);
  line-height: 1.1;
  margin-bottom: 0.25rem;
  text-transform: uppercase;
}

.paper-checklist .check-desc {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--color-gray-dark);
}

/* Re-bind blueprint for problem section */
.problem-blueprint {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  opacity: 0.05;
  z-index: 0;
  pointer-events: none;
}
"""

css = re.sub(r'/\* Hero Animated Checklist \*/.*?(?=\/\* PROCESS SECTION ANIMATION)', new_css + '\n', css, flags=re.DOTALL)

with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)


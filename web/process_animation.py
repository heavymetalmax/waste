with open('ua/index-v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert the animation divs right after <section id="process">
insert_html = """
    <!-- Background Animation -->
    <div class="process-bg-anim"></div>
    <div class="scanner-line"></div>
"""

html = html.replace('<section id="process">', '<section id="process">' + insert_html)

with open('ua/index-v2.html', 'w', encoding='utf-8') as f:
    f.write(html)


with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

animation_css = """
/* PROCESS SECTION ANIMATION */
#process {
  position: relative;
  overflow: hidden;
}

#process .container {
  position: relative;
  z-index: 2; /* Keep content above animation */
}

/* Subtle moving engineering grid */
.process-bg-anim {
  position: absolute;
  top: -50px; left: -50px; 
  width: calc(100% + 100px); 
  height: calc(100% + 100px);
  background-image: 
    linear-gradient(rgba(255, 255, 255, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.05) 1px, transparent 1px);
  background-size: 60px 60px;
  background-position: 0 0;
  animation: processGridMove 15s linear infinite;
  z-index: 0;
  pointer-events: none;
}

@keyframes processGridMove {
  0% { transform: translateY(0); }
  100% { transform: translateY(-60px); } /* seamless loop on cell size */
}

/* Sweeping optical scanner line */
.scanner-line {
  position: absolute;
  top: -20%;
  left: 0;
  width: 100%;
  height: 250px;
  background: linear-gradient(
    to bottom, 
    transparent 0%, 
    rgba(0, 51, 160, 0.05) 40%, 
    rgba(0, 51, 160, 0.3) 50%, 
    rgba(0, 51, 160, 0.05) 60%, 
    transparent 100%
  );
  border-top: 1px solid rgba(0, 51, 160, 0.5);
  border-bottom: 1px solid rgba(0, 51, 160, 0.5);
  animation: processScanSweep 6s ease-in-out infinite alternate;
  z-index: 1;
  pointer-events: none;
  opacity: 0.8;
}

@keyframes processScanSweep {
  0% { top: -20%; }
  100% { top: 120%; }
}
"""

css += '\n' + animation_css

with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)


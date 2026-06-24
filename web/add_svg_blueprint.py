import re

# 1. Modify CSS
with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

blueprint_css = """
/* Hero Blueprint Animation */
.hero-blueprint {
  position: absolute;
  top: 50%;
  left: 0;
  transform: translateY(-50%);
  width: 55%;
  height: 100%;
  opacity: 0.15;
  z-index: 0;
  pointer-events: none;
  overflow: hidden;
}

.bp-line {
  fill: none;
  stroke: var(--color-black);
  stroke-width: 2;
  stroke-dasharray: 4000;
  stroke-dashoffset: 4000;
  animation: drawBlueprint 15s ease-in-out infinite alternate;
}

.bp-line-thin {
  fill: none;
  stroke: var(--color-black);
  stroke-width: 0.5;
  stroke-dasharray: 2000;
  stroke-dashoffset: 2000;
  animation: drawBlueprint 20s ease-in-out infinite alternate;
}

@keyframes drawBlueprint {
  0% { stroke-dashoffset: 4000; }
  100% { stroke-dashoffset: 0; }
}

body > section:nth-of-type(1) {
  position: relative;
  overflow: hidden; /* To keep blueprint inside */
}

/* Ensure container text stays above blueprint */
body > section:nth-of-type(1) .container {
  position: relative;
  z-index: 2;
}
"""

css += '\n' + blueprint_css

with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Modify HTML
with open('ua/index-v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

blueprint_html = """  <!-- HERO SECTION -->
  <section>
    <!-- Background SVG Blueprint -->
    <div class="hero-blueprint">
      <svg viewBox="0 0 800 800" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: 100%;">
        <!-- Frame -->
        <path class="bp-line-thin" d="M 50 50 L 750 50 L 750 750 L 50 750 Z" />
        <path class="bp-line-thin" d="M 50 150 L 750 150 M 50 650 L 750 650" />
        <path class="bp-line-thin" d="M 150 50 L 150 750 M 650 50 L 650 750" />
        
        <!-- Reactor Main Body -->
        <path class="bp-line" d="M 300 200 C 300 120 500 120 500 200 L 500 600 C 500 680 300 680 300 600 Z" />
        <path class="bp-line" d="M 280 200 L 520 200 M 280 600 L 520 600" />
        
        <!-- Center Shaft -->
        <path class="bp-line" d="M 400 80 L 400 700" />
        
        <!-- Impellers / Agitators -->
        <path class="bp-line" d="M 320 280 L 480 280 M 320 400 L 480 400 M 320 520 L 480 520" />
        
        <!-- Top Motor / Valve Area -->
        <rect class="bp-line" x="360" y="50" width="80" height="50" />
        <circle class="bp-line-thin" cx="400" cy="75" r="15" />
        
        <!-- Pipes In/Out -->
        <!-- Inlet -->
        <path class="bp-line" d="M 150 250 L 300 250" />
        <circle class="bp-line" cx="225" cy="250" r="15" />
        <!-- Outlet -->
        <path class="bp-line" d="M 500 550 L 650 550" />
        <circle class="bp-line" cx="575" cy="550" r="15" />
        
        <!-- Tech Data Lines -->
        <path class="bp-line-thin" d="M 500 300 L 600 250 L 700 250" />
        <circle class="bp-line" cx="500" cy="300" r="5" />
        <path class="bp-line-thin" d="M 300 500 L 200 450 L 100 450" />
        <circle class="bp-line" cx="300" cy="500" r="5" />
        
        <!-- Extra Pressure Vessels -->
        <rect class="bp-line" x="180" y="350" width="40" height="100" />
        <path class="bp-line-thin" d="M 200 350 L 200 250" />
      </svg>
    </div>
    <div class="container">"""

html = html.replace('  <!-- HERO SECTION -->\n  <section>\n    <div class="container">', blueprint_html)

with open('ua/index-v2.html', 'w', encoding='utf-8') as f:
    f.write(html)


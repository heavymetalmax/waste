import pathlib
import subprocess

ROOT = pathlib.Path(__file__).parent.parent

# Read app.js
app_js_path = ROOT / "app.js"
app_content = app_js_path.read_text(encoding="utf-8")

# Find the target block
target = """    // Button click
    if (trigger) trigger.addEventListener('click', (e) => { e.preventDefault(); open(); });
    if (closeBtn) closeBtn.addEventListener('click', (e) => { e.preventDefault(); close(); });

    // Swipe up from footer (touch only)
    let touchStartY = 0;
    let startedAtBottom = false;
    document.addEventListener('touchstart', (e) => {
      touchStartY = e.touches[0].clientY;
      startedAtBottom = atBottom();
    }, { passive: true });
    document.addEventListener('touchend', (e) => {
      if (!startedAtBottom || strip.classList.contains('open')) return;
      if (touchStartY - e.changedTouches[0].clientY > 40) open();
    }, { passive: true });

    // Close on scroll away from bottom
    let lastY = window.scrollY;
    window.addEventListener('scroll', () => {
      const y = window.scrollY;
      if (strip.classList.contains('open') && y < lastY && !atBottom()) close();
      lastY = y;
    }, { passive: true });"""

replacement = """    // Button click (toggle style)
    if (trigger) trigger.addEventListener('click', (e) => {
      e.preventDefault();
      if (strip.classList.contains('open')) {
        close();
      } else {
        open();
      }
    });
    if (closeBtn) closeBtn.addEventListener('click', (e) => { e.preventDefault(); close(); });

    // Swipe up from footer (touch only)
    let touchStartY = 0;
    let startedAtBottom = false;
    document.addEventListener('touchstart', (e) => {
      touchStartY = e.touches[0].clientY;
      startedAtBottom = atBottom();
    }, { passive: true });
    document.addEventListener('touchend', (e) => {
      if (!startedAtBottom || strip.classList.contains('open')) return;
      if (touchStartY - e.changedTouches[0].clientY > 40) open();
    }, { passive: true });"""

if target in app_content:
    app_content = app_content.replace(target, replacement)
    app_js_path.write_text(app_content, encoding="utf-8")
    print("app.js updated successfully.")
else:
    print("Target block not found in app.js!")

# Run esbuild to minify styles.css
subprocess.run(["npx", "-y", "esbuild", "styles.css", "--minify", "--outfile=styles.min.css"], cwd=str(ROOT))
print("styles.min.css updated.")

# Run esbuild to minify app.js
subprocess.run(["npx", "-y", "esbuild", "app.js", "--minify", "--outfile=app.min.js"], cwd=str(ROOT))
print("app.min.js updated.")

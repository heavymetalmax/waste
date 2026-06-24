with open('ua/index-v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_items = """
            <div class="check-item">
              <div class="check-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="square"><polyline points="20 6 9 17 4 12"></polyline></svg>
              </div>
              <div class="check-content">
                <span class="check-val">Скорочення об'єму в 5 разів</span>
                <span class="check-desc">Радикальне зменшення витрат на логістику та утилізацію</span>
              </div>
            </div>
            
            <div class="check-item">
              <div class="check-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="square"><polyline points="20 6 9 17 4 12"></polyline></svg>
              </div>
              <div class="check-content">
                <span class="check-val">Нейтралізація мікропластику</span>
                <span class="check-desc">Частки &lt; 0.01 мм (повна відповідність новій директиві ЄС)</span>
              </div>
            </div>
            
          </div>"""

# Find the end of the paper-checklist and insert the new items
html = html.replace('          </div>\n        </div>\n      </div>\n    </div>\n  </section>', new_items + '\n        </div>\n      </div>\n    </div>\n  </section>')

with open('ua/index-v2.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_delays = """
.paper-checklist .check-item:nth-child(5) .check-icon svg { animation-delay: 6.5s; }
.paper-checklist .check-item:nth-child(6) .check-icon svg { animation-delay: 7.5s; }
"""

# Just append to the end of CSS
with open('ua/industrial-modern.css', 'a', encoding='utf-8') as f:
    f.write(new_delays)


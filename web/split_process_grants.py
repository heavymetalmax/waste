import re

# 1. HTML Update
with open('ua/index-v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_process_html = """  <!-- PROCESS & GRANTS -->
  <section id="process" >
    <div class="container">
      <div class="grid-2">
        <!-- Process -->
        <div>
          <span class="rubric">Процес</span>
          <h2>Від контакту до проєкту</h2>
          
          <div class="col-card">
            <div>
              <span class="number">01</span>
              <h3>Опишіть об'єкт</h3>
              <p>Розкажіть нам про вашу станцію: тип, розмір у РЛМ, поточний спосіб утилізації мулу. Займає 5 хвилин, без зобов'язань.</p>
            </div>
            <div>
              <span class="number">02</span>
              <h3>Безкоштовна інженерна оцінка</h3>
              <p>Наші інженери аналізують ваші дані і дають конкретні цифри: очікувана економія та доступне грантове фінансування.</p>
            </div>
            <div>
              <span class="number">03</span>
              <h3>ТЕО та грантовий пакет під FENX</h3>
              <p>Розробляємо повне ТЕО, спеціально адаптоване під вимоги NFOŚiGW та FENX.01.03, для гарантованого отримання гранту на CapEx.</p>
            </div>
          </div>
        </div>

        <!-- Grants -->
        <div>
          <span class="rubric">Фінансування</span>
          <h2>Вікно можливостей до 2027</h2>
          
          <div class="col-card">
            <h3 >Програма FENX.01.03</h3>
            <p>Понад 7.6 млрд євро виділено для Польщі. Програма покриває до 70-85% CapEx для водоканалів. Ми проєктуємо об'єкти так, щоб гарантовано під них підпадати.</p>
          </div>
          
          <div class="col-card">
            <h3>Фонди NFOŚiGW</h3>
            <p>Національний фонд пропонує поєднання пільгових позик та дотацій (уморення до 30-50%). Наше ТЕО розробляється з урахуванням специфічних вимог експертів NFOŚiGW.</p>
          </div>

          <div class="col-card">
            <h3>Документація під ключ</h3>
            <p>Вам не потрібно шукати грантових консультантів окремо. Розробка пакету документації для фондів інтегрована в нашу роботу над технічним проєктом.</p>
          </div>
        </div>
      </div>
    </div>
  </section>"""

new_process_html = """  <!-- PROCESS -->
  <section id="process">
    <div class="container">
      <span class="rubric">Процес</span>
      <h2>Від контакту до проєкту</h2>
      
      <div class="grid-3">
        <div class="col-card process-card">
          <span class="number">01</span>
          <h3>Опишіть об'єкт</h3>
          <p>Розкажіть нам про вашу станцію: тип, розмір у РЛМ, поточний спосіб утилізації мулу. Займає 5 хвилин, без зобов'язань.</p>
        </div>
        <div class="col-card process-card">
          <span class="number">02</span>
          <h3>Безкоштовна інженерна оцінка</h3>
          <p>Наші інженери аналізують ваші дані і дають конкретні цифри: очікувана економія та доступне грантове фінансування.</p>
        </div>
        <div class="col-card process-card">
          <span class="number">03</span>
          <h3>ТЕО та грантовий пакет під FENX</h3>
          <p>Розробляємо повне ТЕО, спеціально адаптоване під вимоги NFOŚiGW та FENX.01.03, для гарантованого отримання гранту на CapEx.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- GRANTS -->
  <section id="grants">
    <div class="container">
      <span class="rubric">Фінансування</span>
      <h2>Вікно можливостей до 2027</h2>
      
      <div class="grid-3">
        <div class="col-card grant-card">
          <h3>Програма FENX.01.03</h3>
          <p>Понад 7.6 млрд євро виділено для Польщі. Програма покриває до 70-85% CapEx для водоканалів. Ми проєктуємо об'єкти так, щоб гарантовано під них підпадати.</p>
        </div>
        
        <div class="col-card grant-card">
          <h3>Фонди NFOŚiGW</h3>
          <p>Національний фонд пропонує поєднання пільгових позик та дотацій (уморення до 30-50%). Наше ТЕО розробляється з урахуванням специфічних вимог експертів NFOŚiGW.</p>
        </div>

        <div class="col-card grant-card">
          <h3>Документація під ключ</h3>
          <p>Вам не потрібно шукати грантових консультантів окремо. Розробка пакету документації для фондів інтегрована в нашу роботу над технічним проєктом.</p>
        </div>
      </div>
    </div>
  </section>"""

html = html.replace(old_process_html, new_process_html)
with open('ua/index-v2.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. CSS Update
with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace nth-of-type with IDs to prevent structural breaks
css = css.replace('body > section:nth-of-type(2)', '#problem')
css = css.replace('body > section:nth-of-type(3)', '#comparison')
css = css.replace('body > section:nth-of-type(4)', '#process')
css = css.replace('body > section:nth-of-type(5)', '#calculator')
css = css.replace('body > section:nth-of-type(6)', '#team')
css = css.replace('body > section:nth-of-type(7)', '#trust')
css = css.replace('body > section:nth-of-type(8)', '#contact')

# Add Grants specific styling, and clean up the old Process nested hacks
new_process_css = """
/* PROCESS SECTION */
#process {
  background-color: var(--color-black);
  color: var(--color-white);
  border-bottom: 4px solid var(--color-white);
}
#process h2 { border-color: var(--color-white); }
#process .rubric { background-color: var(--color-white); color: var(--color-black); }

.process-card {
  background: var(--color-black);
  color: var(--color-white);
  border: 4px solid var(--color-gray-dark);
}
.process-card .number {
  color: var(--color-white);
  font-size: 3.5rem;
}

/* GRANTS SECTION */
#grants {
  background-color: var(--color-white);
  color: var(--color-black);
  border-bottom: 4px solid var(--color-black);
}
.grant-card {
  background: var(--color-white);
  color: var(--color-black);
  border-color: var(--color-black);
}
"""

# Remove old #process block hacks
css = re.sub(r'#process\s+\.grid-2.*?(?=\/\* Trust Section)', new_process_css + '\n\n', css, flags=re.DOTALL)
# Also remove the process_overflow_fix we added since we don't need it anymore
css = re.sub(r'/\* Prevent any overflow issues specifically in process cards \*/.*?max-width: 100vw;\n\}', '', css, flags=re.DOTALL)

with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)


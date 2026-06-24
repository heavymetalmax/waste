with open('ua/index-v2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We will inject the Calculator CTA before the Trust section
calc_html = """
  <!-- CALCULATOR CTA -->
  <section id="calculator" style="background-color: var(--text-main); color: var(--bg-color); border-bottom: none;">
    <div class="container">
      <div class="grid-2" style="align-items: center;">
        <div>
          <span class="rubric" style="color: var(--bg-color); border-color: var(--bg-color);">Розрахунки</span>
          <h2 style="color: var(--bg-color); border-color: var(--bg-color); margin-bottom: var(--space-sm);">AI-Калькулятор для вашого водоканалу</h2>
          <p style="color: #dcd7cb; font-size: 1.1rem; margin-bottom: var(--space-md);">Завантажте ваш лабораторний звіт (PDF, Excel, скан). Наш AI зчитає параметри та за 60 секунд видасть вихід гідровугілля, скорочення об'єму та клас хабу.</p>
          <a href="simulator.html" class="btn btn-outline" style="color: var(--bg-color); border-color: var(--bg-color);">Перейти до розрахунків →</a>
        </div>
        <div style="background-color: rgba(255, 255, 255, 0.05); padding: var(--space-md); border-top: 4px solid var(--accent-gold);">
          <ul style="list-style: none; color: #dcd7cb; font-size: 1.05rem;">
            <li style="margin-bottom: 0.8rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">✓ Вихід гідровугілля (т/добу)</li>
            <li style="margin-bottom: 0.8rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">✓ Точне скорочення об'єму відходів</li>
            <li style="margin-bottom: 0.8rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">✓ Орієнтовна окупність проєкту</li>
            <li>✓ Відповідність критеріям грантів ЄС</li>
          </ul>
        </div>
      </div>
    </div>
  </section>
"""

# We will inject the Team section after the Trust section
team_html = """
  <!-- TEAM -->
  <section id="team" style="background-color: var(--bg-alt);">
    <div class="container">
      <span class="rubric">Команда</span>
      <h2 style="text-align: center; display: block; width: 100%;">Люди, які несуть персональну відповідальність за проєкт</h2>
      
      <div class="grid-4" style="margin-top: var(--space-lg);">
        <div class="col-card" style="padding: 0; background: transparent; border-top: 4px solid var(--border-color);">
          <img src="../img/team/krop-e.jpg" alt="Dr inż. Eugeniusz Krop" style="width: 100%; height: auto; display: block; filter: grayscale(100%); margin-bottom: var(--space-xs);">
          <div style="padding-top: var(--space-xs);">
            <h3 style="font-size: 1.2rem; margin-bottom: 0;">Dr inż. Eugeniusz Krop</h3>
            <p style="font-family: 'Playfair Display', serif; font-style: italic; color: var(--accent-gold); margin-bottom: 0.5rem;">Технічний директор</p>
            <p style="font-size: 0.9rem;">28 масштабних промислових впроваджень. Серед клієнтів: ORLEN.</p>
          </div>
        </div>

        <div class="col-card" style="padding: 0; background: transparent; border-top: 4px solid var(--border-color);">
          <img src="../img/team/wilk-m.jpg" alt="Dr hab. inż. Małgorzata Wilk" style="width: 100%; height: auto; display: block; filter: grayscale(100%); margin-bottom: var(--space-xs);">
          <div style="padding-top: var(--space-xs);">
            <h3 style="font-size: 1.2rem; margin-bottom: 0;">Dr hab. inż. M. Wilk</h3>
            <p style="font-family: 'Playfair Display', serif; font-style: italic; color: var(--accent-gold); margin-bottom: 0.5rem;">R&D верифікація</p>
            <p style="font-size: 0.9rem;">Завідувачка кафедри AGH Kraków. TOP 2% вчених світу (Stanford).</p>
          </div>
        </div>

        <div class="col-card" style="padding: 0; background: transparent; border-top: 4px solid var(--border-color);">
          <img src="../img/team/krop-a.jpg" alt="Andrzej Krop" style="width: 100%; height: auto; display: block; filter: grayscale(100%); margin-bottom: var(--space-xs);">
          <div style="padding-top: var(--space-xs);">
            <h3 style="font-size: 1.2rem; margin-bottom: 0;">Andrzej Krop</h3>
            <p style="font-family: 'Playfair Display', serif; font-style: italic; color: var(--accent-gold); margin-bottom: 0.5rem;">Управління проєктами</p>
            <p style="font-size: 0.9rem;">Екс-CEO європейського підрозділу японської корпорації. Гарант строків.</p>
          </div>
        </div>

        <div class="col-card" style="padding: 0; background: transparent; border-top: 4px solid var(--border-color);">
          <img src="../img/team/koval-m.jpg" alt="Max Koval" style="width: 100%; height: auto; display: block; filter: grayscale(100%); margin-bottom: var(--space-xs);">
          <div style="padding-top: var(--space-xs);">
            <h3 style="font-size: 1.2rem; margin-bottom: 0;">Max Koval</h3>
            <p style="font-family: 'Playfair Display', serif; font-style: italic; color: var(--accent-gold); margin-bottom: 0.5rem;">B2B Стратегія</p>
            <p style="font-size: 0.9rem;">Позиціонування BioTC на ринках ЄС та робота з грантовими структурами.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

content = content.replace('  <!-- CONTACT -->', calc_html + '\n' + team_html + '\n  <!-- CONTACT -->')

with open('ua/index-v2.html', 'w', encoding='utf-8') as f:
    f.write(content)

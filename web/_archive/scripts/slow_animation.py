with open('ua/industrial-modern.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Slow down the paper sliding
css = css.replace(
    'transform: translateY(150px) rotateX(10deg);',
    'transform: translateY(300px) rotateX(15deg);'
)

css = css.replace(
    'animation: paperSlideUp 1s cubic-bezier(0.16, 1, 0.3, 1) 0.2s forwards;',
    'animation: paperSlideUp 3s cubic-bezier(0.22, 1, 0.36, 1) 0.5s forwards;'
)

# Slow down the checkmarks stagger to wait for the paper
css = css.replace(
    '.paper-checklist .check-item:nth-child(2) .check-icon svg { animation-delay: 1.2s; }',
    '.paper-checklist .check-item:nth-child(2) .check-icon svg { animation-delay: 3.5s; }'
)
css = css.replace(
    '.paper-checklist .check-item:nth-child(3) .check-icon svg { animation-delay: 1.8s; }',
    '.paper-checklist .check-item:nth-child(3) .check-icon svg { animation-delay: 4.5s; }'
)
css = css.replace(
    '.paper-checklist .check-item:nth-child(4) .check-icon svg { animation-delay: 2.4s; }',
    '.paper-checklist .check-item:nth-child(4) .check-icon svg { animation-delay: 5.5s; }'
)

# Make the drawing of the checkmark slightly slower too
css = css.replace(
    'animation: drawCheck 0.5s cubic-bezier(0.65, 0, 0.35, 1) forwards;',
    'animation: drawCheck 0.8s cubic-bezier(0.65, 0, 0.35, 1) forwards;'
)


with open('ua/industrial-modern.css', 'w', encoding='utf-8') as f:
    f.write(css)


import re

with open("sections/purelane-ingredients.liquid", "r") as f:
    content = f.read()

# Fix .wrap padding
content = re.sub(
    r'\.wrap \{ max-width: var\(--maxw\); margin: 0 auto; padding: 0 14px; \}',
    r'.wrap { max-width: var(--maxw); margin: 0 auto; padding: 0 18px; }',
    content
)

# Fix .d2 font-size
content = re.sub(
    r'\.panel-head \.d2 \{ margin-bottom: 12px; font-family: \'Outfit\', sans-serif; font-size: clamp\(34px, 4vw, 46px\);',
    r'.panel-head .d2 { margin-bottom: 12px; font-family: \'Outfit\', sans-serif; font-size: clamp(30px, 4.6vw, 54px);',
    content
)

# Fix .d3 font-size
content = re.sub(
    r'\.pillar \.d3 \{ margin-bottom: 11px; font-family: \'Outfit\', sans-serif; font-size: clamp\(20px, 2.2vw, 24px\);',
    r'.pillar .d3 { margin-bottom: 11px; font-family: \'Outfit\', sans-serif; font-size: clamp(21px, 2.5vw, 30px);',
    content
)

# Fix .pillar p (.body-s) font size and line height
content = re.sub(
    r'\.pillar p \{ margin-bottom: 20px; flex: 1; font-size: 13\.5px; color: var\(--paper-2\); line-height: 1\.5; \}',
    r'.pillar p { margin-bottom: 20px; flex: 1; font-size: 14.5px; color: var(--paper-2); line-height: 1.66; }',
    content
)

# Fix --sec-y media query
# Currently in style: --sec-y: 34px;
if '@media(max-width:760px) { #Purelane' not in content:
    content = content.replace(
        '  #Purelane-{{ section.id }} .sec { position: relative; padding: var(--sec-y) 0; }',
        '  @media(max-width:760px) { #Purelane-{{ section.id }} { --sec-y: 22px; } }\n  #Purelane-{{ section.id }} .sec { position: relative; padding: var(--sec-y) 0; }'
    )

with open("sections/purelane-ingredients.liquid", "w") as f:
    f.write(content)

print("Updated typography and spacing in purelane-ingredients.liquid")

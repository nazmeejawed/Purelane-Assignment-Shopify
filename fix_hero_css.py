import re

with open("sections/purelane-hero.liquid", "r") as f:
    content = f.read()

# We need to replace the hallucinated block:
old_css_regex = r'#PurelaneHero-\{\{ section\.id \}\} \.hp\.a \{ height: 100%; \}.*?margin-right: 0; \}'

new_css = """  #PurelaneHero-{{ section.id }} .hs1 .a { height: 100%; z-index: 3; }
  #PurelaneHero-{{ section.id }} .hs2 .a { height: 80%; margin-right: -8%; z-index: 1; }
  #PurelaneHero-{{ section.id }} .hs2 .b { height: 97%; z-index: 3; }
  #PurelaneHero-{{ section.id }} .hs3 .a { height: 75%; margin-right: -8%; z-index: 1; order: 1; }
  #PurelaneHero-{{ section.id }} .hs3 .c { height: 97%; z-index: 3; order: 2; }
  #PurelaneHero-{{ section.id }} .hs3 .b { height: 79%; margin-left: -8%; z-index: 2; order: 3; }"""

content = re.sub(old_css_regex, new_css, content, flags=re.DOTALL)

with open("sections/purelane-hero.liquid", "w") as f:
    f.write(content)

print("Fixed the prototype CSS for bottle sizes and orders.")

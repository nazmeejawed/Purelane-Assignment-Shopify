import re

with open("sections/purelane-hero.liquid", "r") as f:
    content = f.read()

# Replace the old height css for slide 3 with the new one
old_css = """  #PurelaneHero-{{ section.id }} .hslide[data-n="3"] .hp { height: 88%; }
  #PurelaneHero-{{ section.id }} .hslide[data-n="3"] .hp.b { height: 80%; margin-right: -1%; }
  #PurelaneHero-{{ section.id }} .hslide[data-n="3"] .hp.c { height: 76%; margin-right: -1.5%; }"""

new_css = """  #PurelaneHero-{{ section.id }} .hslide[data-n="3"] .hp { height: 76%; margin-right: -1.5%; }
  #PurelaneHero-{{ section.id }} .hslide[data-n="3"] .hp.b { height: 90%; margin-right: -1%; z-index: 3; }
  #PurelaneHero-{{ section.id }} .hslide[data-n="3"] .hp.c { height: 80%; margin-right: 0; }"""

if old_css in content:
    content = content.replace(old_css, new_css)
else:
    print("Old CSS not found precisely. Falling back to regex.")
    content = re.sub(
        r'#PurelaneHero-\{\{ section\.id \}\} \.hslide\[data-n="3"\] \.hp \{ height: 88%; \}\s*#PurelaneHero-\{\{ section\.id \}\} \.hslide\[data-n="3"\] \.hp\.b \{ height: 80%; margin-right: -1%; \}\s*#PurelaneHero-\{\{ section\.id \}\} \.hslide\[data-n="3"\] \.hp\.c \{ height: 76%; margin-right: -1\.5%; \}',
        new_css,
        content
    )

with open("sections/purelane-hero.liquid", "w") as f:
    f.write(content)

print("Updated height CSS for slide 3 to make the middle bottle biggest.")

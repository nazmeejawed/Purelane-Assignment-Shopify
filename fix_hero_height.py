import re

with open("sections/purelane-hero.liquid", "r") as f:
    content = f.read()

# Add the missing height CSS for the bottles
height_css = """
  #PurelaneHero-{{ section.id }} .hp.a { height: 100%; }
  #PurelaneHero-{{ section.id }} .hslide[data-n="2"] .hp { height: 94%; }
  #PurelaneHero-{{ section.id }} .hslide[data-n="2"] .hp.b { height: 82%; margin-right: -2%; }
  #PurelaneHero-{{ section.id }} .hslide[data-n="3"] .hp { height: 88%; }
  #PurelaneHero-{{ section.id }} .hslide[data-n="3"] .hp.b { height: 80%; margin-right: -1%; }
  #PurelaneHero-{{ section.id }} .hslide[data-n="3"] .hp.c { height: 76%; margin-right: -1.5%; }
"""

# Insert it after the existing .hp CSS
content = content.replace("  #PurelaneHero-{{ section.id }} .hslide.on .hp.d3 { transition-delay: .54s; }", 
                          "  #PurelaneHero-{{ section.id }} .hslide.on .hp.d3 { transition-delay: .54s; }\n" + height_css)

with open("sections/purelane-hero.liquid", "w") as f:
    f.write(content)

print("Updated height CSS")

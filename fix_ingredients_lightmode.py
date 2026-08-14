import re

with open("sections/purelane-ingredients.liquid", "r") as f:
    content = f.read()

# We need to add text-transform: uppercase to .d2 and .d3
content = content.replace("color: var(--surface); line-height: .96; }", "color: var(--surface); line-height: .96; text-transform: uppercase; }")
content = content.replace("color: var(--surface); line-height: 1.1; }", "color: var(--surface); line-height: 1.1; text-transform: uppercase; }")

# Update pillar .pi to light mode styles
old_pi = "background: linear-gradient(150deg, rgba(240,160,60,.22), rgba(75,58,143,.34)); border: 1px solid rgba(236,230,247,.2); color: var(--accent);"
new_pi = "background: linear-gradient(150deg, rgba(201,118,29,.18), rgba(75,58,143,.12)); border: 1px solid rgba(75,58,143,.16); color: #4f7d10;"
content = content.replace(old_pi, new_pi)

# Add SVG recoloring block
svg_recoloring = """
  /* Botanical Line Art SVG recoloring */
  #Purelane-{{ section.id }} .ing-i .art svg { stroke: #0d5b52; }
  #Purelane-{{ section.id }} .ing-i .art svg [stroke="#f0a03c"] { stroke: #b8701c; }
  #Purelane-{{ section.id }} .ing-i .art svg [fill="#ece6f7"] { fill: #0d5b52; }
  #Purelane-{{ section.id }} .ing-i .art svg [stroke="#f0a03c"][stroke-width="2.4"] { stroke: #b8701c; }
"""

content = content.replace("/* Pillars */", svg_recoloring + "\n  /* Pillars */")

# Add correct text-transform uppercase on d3 for pillars
# (Already handled by replacing line-height: 1.1)

# Also fix .rule i:first-child in light mode:
content = content.replace("rgba(236,230,247,.44)", "rgba(75,58,143,.34)")

with open("sections/purelane-ingredients.liquid", "w") as f:
    f.write(content)

print("Updated purelane-ingredients.liquid with light mode fixes.")

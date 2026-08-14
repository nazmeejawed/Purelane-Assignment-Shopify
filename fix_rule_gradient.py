import re

with open("sections/purelane-ingredients.liquid", "r") as f:
    content = f.read()

# Fix the gradient for .rule i (base) vs .rule i:first-child
old_rule = "#Purelane-{{ section.id }} .panel-head .rule i { flex: 1; height: 1.5px; background: linear-gradient(90deg, transparent, rgba(75,58,143,.34)); }"
new_rule = "#Purelane-{{ section.id }} .panel-head .rule i { flex: 1; height: 1.5px; background: linear-gradient(90deg, rgba(75,58,143,.34), transparent); }"
content = content.replace(old_rule, new_rule)

with open("sections/purelane-ingredients.liquid", "w") as f:
    f.write(content)

print("Fixed the rule gradient!")

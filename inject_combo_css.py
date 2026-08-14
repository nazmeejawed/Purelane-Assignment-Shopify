import re

with open("purelane-homepage.html", "r") as f:
    html = f.read()

# Extract the combo CSS block from purelane-homepage.html
match = re.search(r'/\* ---------- BEST SELLING COMBOS ---------- \*/.*?(?=/\* ----------)', html, re.DOTALL)
combo_css = match.group(0) if match else ""

# Read the current sections/purelane-combos.liquid
with open("sections/purelane-combos.liquid", "r") as f:
    content = f.read()

# Prepend the CSS wrapped in a style tag
final_content = f"<style>\n{combo_css}</style>\n\n{content}"

with open("sections/purelane-combos.liquid", "w") as f:
    f.write(final_content)

print("Injected combo CSS successfully.")

import re

with open("purelane-homepage.html", "r") as f:
    html = f.read()

# I will write a regex to extract all combo related CSS rules across the entire file
combo_rules = []

# Base rules
match1 = re.search(r'/\* ---------- BEST SELLING COMBOS ---------- \*/.*?(?=/\* ----------)', html, re.DOTALL)
if match1:
    combo_rules.append(match1.group(0))

# Mobile media queries
match2 = re.search(r'@media\(max-width:767px\)\{.*?\}', html, re.DOTALL)
if match2:
    mobile_css = match2.group(0)
    # Extract only lines containing combo, comborail, swipecue from mobile
    lines = mobile_css.split('\n')
    combo_lines = [l for l in lines if 'combo' in l or 'swipecue' in l]
    if combo_lines:
        combo_rules.append("@media(max-width:767px){\n  " + "\n  ".join(combo_lines) + "\n}")

# Light theme
match3 = re.search(r'/\* ---------- comborail, tiers, badges ---------- \*/.*?(?=/\* ----------)', html, re.DOTALL)
if match3:
    combo_rules.append(match3.group(0))

# Read the current sections/purelane-combos.liquid
with open("sections/purelane-combos.liquid", "r") as f:
    content = f.read()

# Replace existing <style> block
content = re.sub(r'<style>.*?</style>\n*', '', content, flags=re.DOTALL)

# Prepend the CSS wrapped in a style tag
final_content = f"<style>\n" + "\n".join(combo_rules) + "\n</style>\n\n" + content

with open("sections/purelane-combos.liquid", "w") as f:
    f.write(final_content)

print("Injected COMPLETE combo CSS successfully.")

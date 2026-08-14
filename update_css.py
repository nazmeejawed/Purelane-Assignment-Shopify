import re

with open("purelane-homepage.html", "r") as f:
    html = f.read()

style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
css = style_match.group(1)

# Get root variables
root_vars_1 = re.search(r':root\{(.*?)\}', css, re.DOTALL).group(1)
root_vars_2 = re.search(r'(:root\{\n--p-combo2:url.*?)\}', css, re.DOTALL).group(1)
root_vars_2 = root_vars_2.replace(':root{', '')

# Get VERSION 2 variables
light_vars = re.search(r'(--accent-2:#c9761d;\n\s*--surface:#17102b;.*?--g-inset:inset 0 1px 0 rgba\(255,255,255,\.92\);)', css, re.DOTALL).group(1)

# Get specific class blocks we need
def get_block(regex):
    matches = re.finditer(regex, css, re.MULTILINE | re.DOTALL)
    blocks = []
    for m in matches:
        blocks.append(m.group(0))
    return "\n".join(blocks)

# We want these exactly from the prototype
classes_regex = [
    r'^\.d2\{.*?\}',
    r'^\.lede\{.*?\}',
    r'^\.kicker\{.*?\}',
    r'^\.rule\{.*?\}',
    r'^\.rule i\{.*?\}',
    r'^\.rule svg\{.*?\}',
    r'^\.btn\{.*?\}',
    r'^\.btn svg\{.*?\}',
    r'^\.btn-primary\{.*?\}',
    r'^\.btn-primary:hover\{.*?\}',
    r'^\.btn-ghost\{.*?\}',
    r'^\.btn-ghost:hover\{.*?\}',
    r'^\.glass\{.*?\}',
    r'^\.glass::after\{.*?\}',
    r'^\.comborail\{.*?\}',
    r'^\.comborail::-webkit-scrollbar\{.*?\}',
    r'^\.combo\{.*?\}',
    r'^\.combo:hover\{.*?\}',
    r'^\.combo\.hero-combo\{.*?\}',
    r'^\.combo \.tray\{.*?\}',
    r'^\.combo \.save\{.*?\}',
    r'^\.combo \.flag\{.*?\}',
    r'^\.combo \.body\{.*?\}',
    r'^\.combo \.body h3\{.*?\}',
    r'^\.combo \.cnt\{.*?\}',
    r'^\.combo \.inc\{.*?\}',
    r'^\.combo \.prow\{.*?\}',
    r'^\.combo \.prow strong\{.*?\}',
    r'^\.combo \.prow s\{.*?\}',
    r'^\.combo \.prow em\{.*?\}',
    r'^\.combo \.fine\{.*?\}',
    r'^\.combo \.btn\{.*?\}',
    r'^\.stack\{.*?\}',
    r'^\.stack \.it\{.*?\}',
    r'^\.stack \.plus\{.*?\}',
    r'^\.stack \.it span:not\(\.pimg\)\{.*?\}',
    r'^\.stack \.it \.tile\{.*?\}',
    r'^\.swipecue\{.*?\}',
    r'^\.swipecue svg\{.*?\}',
    r'^\.railnote\{.*?\}',
    r'^\.pimg\{.*?\}',
    r'^\.p-.*?(?:\r?\n|$)', # gets all p- classes
]

extracted_css = ""
for regex in classes_regex:
    block = get_block(regex)
    if block:
        extracted_css += block + "\n"

# And the overrides
overrides_regex = [
    r'^\.glass::after\{.*?\}',
    r'^\.combo\.hero-combo\{.*?\}',
    r'^\.combo \.tray\{.*?\}',
    r'^\.combo \.save\{.*?\}',
    r'^\.combo \.flag\{.*?\}',
    r'^\.tier \.tag,\.combo \.prow em\{.*?\}'
]

override_css = "\n/* VERSION 2 OVERRIDES */\n"
for regex in overrides_regex:
    # Need to match the ones near the end of the file (after line 650)
    matches = list(re.finditer(regex, css, re.MULTILINE | re.DOTALL))
    if len(matches) > 1:
        override_css += matches[-1].group(0) + "\n" # take the last one
    elif len(matches) == 1:
        # maybe it's just one
        pass


ns = "#purelane-combos-{{ section.id }}"

# construct final CSS
final_css = f"""<style>
{ns} {{
{root_vars_1}
{root_vars_2}
  /* OVERRIDES */
  {light_vars}
  
  padding: clamp(40px, 6vw, 80px) 0;
}}

{ns} a {{ text-decoration: none; }}
{ns} p, {ns} h2, {ns} h3 {{ margin: 0; }}
{ns} .wrap {{ max-width: 1200px; margin: 0 auto; padding: 0 18px; }}

/* BASE CLASSES */
"""

# Namespace the extracted CSS
for line in extracted_css.splitlines():
    if line.strip() == "": continue
    if line.startswith("."):
        # simple replacement for start of line
        line = ns + " " + line
    elif line.startswith("@media"):
        # media query needs block. We can just skip media queries for now or handle them.
        pass
    final_css += line + "\n"

for line in override_css.splitlines():
    if line.strip() == "": continue
    if line.startswith("."):
        line = ns + " " + line
    final_css += line + "\n"

# Media queries for combos
final_css += f"""
@media(max-width: 1200px) {{
  {ns} .combo {{ flex: 0 0 268px; }}
}}
@media(max-width: 900px) {{
  {ns} .comborail {{ margin: 0 -14px; padding: 4px 14px 12px; }}
  {ns} .glass::after {{ background: linear-gradient(180deg, rgba(255,255,255,.55), transparent 32%, transparent 74%, rgba(201,118,29,.06)); }}
}}
"""

final_css += "</style>\n"

with open("new_style.liquid", "w") as f:
    f.write(final_css)

print("CSS generation done")

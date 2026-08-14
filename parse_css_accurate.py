import re

with open("style_dump.css", "r") as f:
    css = f.read()

def get_rule(pattern):
    m = re.search(pattern, css, re.DOTALL | re.MULTILINE)
    return m.group(0) if m else ""

def get_all_rules(pattern, content=css):
    return [m.group(0) for m in re.finditer(pattern, content, re.DOTALL | re.MULTILINE)]

root_vars = get_rule(r':root\{.*?\}')
svg_vars = get_all_rules(r':root\{\s*--p-[^}]*\}')
all_root = root_vars + "\n" + "\n".join(svg_vars)

# We want exactly these classes
typo = get_all_rules(r'^(\.d1,\.d2,\.d3,\.d4|\.d1|\.d2|\.d3|\.d4|\.lede|\.body-s|\.kicker|\.wrap)\{.*?\}')
glass = get_all_rules(r'^(\.glass|\.glass::after|\.glass-2)\{.*?\}')
btn = get_all_rules(r'^(\.btn|\.btn svg|\.btn-primary|\.btn-primary:hover|\.btn-ghost|\.btn-ghost:hover|\.btn-sm)\{.*?\}')
combo = get_all_rules(r'^(\.comborail|\.comborail::-webkit-scrollbar|\.combo|\.combo:hover|\.combo\.hero-combo|\.combo \.tray|\.combo \.save|\.combo \.flag|\.stack|\.stack \.it|\.stack \.it \.pimg|\.stack \.it \.tile|\.stack \.it \.tile svg|\.stack \.it span|\.stack \.plus|\.combo \.body|\.combo \.body h3|\.combo \.cnt|\.combo \.inc|\.combo \.prow|\.combo \.prow strong|\.combo \.prow s|\.combo \.prow em|\.combo \.fine|\.combo \.btn|\.railnote|\.swipecue|\.swipecue svg|\.rule|\.rule i|\.rule svg|\.panel-head \.rule i:first-child|\.panel-head \.rule i:last-child)\{.*?\}')
pimg = get_all_rules(r'^(\.pimg|\.p-kitchen|\.p-dish|\.p-tap|\.p-laundry|\.p-wm|\.p-toilet|\.p-eraser|\.p-metal|\.p-mbtl|\.p-kbtl|\.p-tbtl|\.p-handwash|\.p-floor|\.p-combo2)\{.*?\}')

# SPLIT by the comment
overrides_section = re.split(r'/\* ---------- scenes: sunlit shallow water ---------- \*/', css)[1]

light_vars_match = re.search(r'(--accent-2:#c9761d;\s*--surface:#17102b;.*?--g-inset:inset 0 1px 0 rgba\(255,255,255,\.92\);)', overrides_section, re.DOTALL)
light_vars = light_vars_match.group(1) if light_vars_match else "/* ERROR extracting light vars */"

o_glass = get_all_rules(r'^(\.glass|\.glass::after|\.glass-2)\{.*?\}', overrides_section)
o_btn = get_all_rules(r'^(\.btn|\.btn svg|\.btn-primary|\.btn-primary:hover|\.btn-ghost|\.btn-ghost:hover|\.btn-sm)\{.*?\}', overrides_section)
o_combo = get_all_rules(r'^(\.comborail|\.comborail::-webkit-scrollbar|\.combo|\.combo:hover|\.combo\.hero-combo|\.combo \.tray|\.combo \.save|\.combo \.flag|\.stack|\.stack \.it|\.stack \.it \.pimg|\.stack \.it \.tile|\.stack \.it \.tile svg|\.stack \.it span|\.stack \.plus|\.combo \.body|\.combo \.body h3|\.combo \.cnt|\.combo \.inc|\.combo \.prow|\.combo \.prow strong|\.combo \.prow s|\.combo \.prow em|\.combo \.fine|\.combo \.btn|\.railnote|\.swipecue|\.swipecue svg|\.rule|\.rule i|\.rule svg|\.panel-head \.rule i:first-child|\.panel-head \.rule i:last-child)\{.*?\}', overrides_section)
o_combo_extra = get_all_rules(r'^(\.tier \.tag,\.combo \.prow em|\.tier\.best,\.combo\.hero-combo|\.stack \.it \.tile)\{.*?\}', overrides_section)

ns = "#purelane-combos-{{ section.id }}"
final_css = f"<style>\n{ns} {{\n"
all_root = all_root.replace(":root{", "").replace("}", "")
final_css += all_root + "\n"
final_css += "\n  /* LIGHT MODE VARS */\n  " + light_vars + "\n"
final_css += "  padding: clamp(40px, 6vw, 80px) 0;\n"
final_css += "}\n\n"
final_css += f"{ns} a {{ text-decoration: none; }}\n"
final_css += f"{ns} p, {ns} h2, {ns} h3 {{ margin: 0; }}\n\n"

def namespace(rules_list):
    res = ""
    for r in rules_list:
        parts = r.split("{", 1)
        if len(parts) == 2:
            selectors = parts[0].split(",")
            ns_selectors = [ns + " " + s.strip() for s in selectors]
            res += ",".join(ns_selectors) + "{" + parts[1] + "\n"
    return res

final_css += "/* TYPOGRAPHY */\n" + namespace(typo)
final_css += "/* GLASS */\n" + namespace(glass)
final_css += "/* BUTTONS */\n" + namespace(btn)
final_css += "/* COMBOS */\n" + namespace(combo)
final_css += "/* PIMG */\n" + namespace(pimg)

final_css += "\n/* OVERRIDES */\n"
final_css += namespace(o_glass)
final_css += namespace(o_btn)
final_css += namespace(o_combo)
final_css += namespace(o_combo_extra)

# Add media queries for combos correctly from prototype
# I will just write them statically to ensure they are 100% correct according to prototype's media queries
final_css += f"""
@media(max-width:1200px){{
  {ns} .combo{{flex:0 0 268px}}
}}
@media(max-width:900px){{
  {ns} .comborail{{margin:0 -14px;padding:4px 14px 12px}}
  {ns} .stack .it .pimg{{height:56px}}
  {ns} .stack .it .tile{{height:56px;width:38px}}
}}
"""

final_css += "</style>\n"

with open("combos_exact.liquid", "w") as f:
    f.write(final_css)

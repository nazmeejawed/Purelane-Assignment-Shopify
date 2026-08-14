import re

with open('purelane-homepage.html', 'r') as f:
    lines = f.readlines()

# Extract lines 832 to 879 (0-indexed, so 832-879 corresponds to lines 833-880)
svg_lines = lines[832:880]
svg_text = "".join(svg_lines)

# Perform replacements
replacements = {
    'class="wl wl-a"': 'class="pl-wl pl-wl-a"',
    'class="wl wl-b"': 'class="pl-wl pl-wl-b"',
    'class="wl wl-c"': 'class="pl-wl pl-wl-c"',
    'class="wl wl-s"': 'class="pl-wl pl-wl-s"',
    'class="sv"': 'class="pl-sv"',
    'id="cg"': 'id="pl-cg"',
    'url(#cg)': 'url(#pl-cg)',
    'id="wf"': 'id="pl-wf"',
    'url(#wf)': 'url(#pl-wf)',
    'id="wf2"': 'id="pl-wf2"',
    'url(#wf2)': 'url(#pl-wf2)',
    'id="sg"': 'id="pl-sg"',
    'url(#sg)': 'url(#pl-sg)',
    'id="sf"': 'id="pl-sf"',
    'url(#sf)': 'url(#pl-sf)',
    'id="sfw"': 'id="pl-sfw"',
    'url(#sfw)': 'url(#pl-sfw)'
}

for old, new in replacements.items():
    svg_text = svg_text.replace(old, new)

# Add 4 spaces of indentation to every line (except empty ones)
indented_svg_text = "\n".join("      " + line if line.strip() else line for line in svg_text.split("\n"))

with open('sections/purelane-hero.liquid', 'r') as f:
    hero_lines = f.readlines()

# Replace lines 417 to 489 in purelane-hero.liquid (0-indexed, which corresponds to 418-490)
# Wait, let's find the exact indices
start_idx = -1
end_idx = -1
for i, line in enumerate(hero_lines):
    if '<div class="pl-wl pl-wl-a">' in line:
        start_idx = i
        break

for i in range(start_idx, len(hero_lines)):
    if '<div class="pl-bub">' in line:
        end_idx = i
        break
    if '<div class="pl-bub">' in hero_lines[i]:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    new_hero_lines = hero_lines[:start_idx] + [indented_svg_text] + hero_lines[end_idx:]
    with open('sections/purelane-hero.liquid', 'w') as f:
        f.writelines(new_hero_lines)
    print(f"Successfully replaced lines {start_idx+1} to {end_idx} with the SVGs.")
else:
    print(f"Could not find start/end indices. start: {start_idx}, end: {end_idx}")

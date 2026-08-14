import re

with open("purelane-homepage.html", "r") as f:
    html = f.read()

# 1. Extract the first style block (V1 CSS)
match1 = re.search(r'<style>.*?</style>', html, re.DOTALL)
css1 = match1.group(0) if match1 else ""

# 2. Extract the second style block (V2 Light Theme CSS)
match2 = re.search(r'<style>(?:\s*/\* ============================================================\s*VERSION 2).*?</style>', html, re.DOTALL)
css2 = match2.group(0) if match2 else ""

# 3. Extract the scenes div (including water)
match_scenes = re.search(r'<div class="scenes" id="scenes" data-d="1">.*?</div>\n\n', html, re.DOTALL)
if not match_scenes:
    match_scenes = re.search(r'<div class="scenes" id="scenes" data-d="1">.*?</div>\s*</main>', html, re.DOTALL)
    scenes_html = match_scenes.group(0).replace("</main>", "") if match_scenes else ""
else:
    scenes_html = match_scenes.group(0)

# We need to make sure we don't accidentally grab too much if </div> matches something else.
# Let's find the exact end of scenes.
# In purelane-homepage.html, it's:
# <div class="scenes" id="scenes" data-d="1">
# ...
#   <div class="water" id="water">
#      ...
#   </div>
# </div>
start_idx = html.find('<div class="scenes" id="scenes" data-d="1">')
end_idx = html.find('<div class="wrap">', start_idx) # The wrap starts the Hero section
scenes_html = html[start_idx:end_idx].strip()

# 4. Extract the parallax JS
match_js = re.search(r'<script>\s*\(function\(\) \{\s*var reduce = window\.matchMedia.*?</script>', html, re.DOTALL)
js_html = match_js.group(0) if match_js else ""

# Combine them exactly as they are in the prototype, plus the Shopify override to ensure body is transparent
final_content = f"""<!-- Purelane Cinematic Background (1:1 Port from Prototype) -->
{css1}
{css2}

<style>
/* Shopify specific overrides to ensure the background is visible */
html, body, .gradient, #MainContent, .shopify-section {{ background: transparent !important; }}
</style>

{scenes_html}

{js_html}
"""

with open("snippets/purelane-background.liquid", "w") as f:
    f.write(final_content)

print("Extraction complete. Replaced purelane-background.liquid with 1:1 prototype port.")

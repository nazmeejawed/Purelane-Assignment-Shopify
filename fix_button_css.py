import re

with open("sections/purelane-ingredients.liquid", "r") as f:
    content = f.read()

# Replace the .btn-ghost styles with the light mode overrides
old_btn = "background: rgba(236,230,247,.10); border: 1px solid rgba(236,230,247,.30); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); color: var(--surface);"
new_btn = "background: rgba(255,255,255,.66); border: 1px solid rgba(75,58,143,.22); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); color: #01423b;"
content = content.replace(old_btn, new_btn)

old_btn_hover = "background: rgba(36,26,61,.08) !important;"
new_btn_hover = "background: rgba(255,255,255,.9) !important;"
content = content.replace(old_btn_hover, new_btn_hover)

with open("sections/purelane-ingredients.liquid", "w") as f:
    f.write(content)

print("Fixed the button CSS!")

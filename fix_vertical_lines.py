import re

with open("sections/purelane-ingredients.liquid", "r") as f:
    content = f.read()

# Replace the invisible white line with the light mode dark line
old_line = "background: linear-gradient(180deg, transparent, rgba(236,230,247,.24), transparent);"
new_line = "background: linear-gradient(180deg, transparent, rgba(75,58,143,.20), transparent);"
content = content.replace(old_line, new_line)

with open("sections/purelane-ingredients.liquid", "w") as f:
    f.write(content)

print("Fixed the vertical ingredient separator lines!")

import re

with open("layout/theme.liquid", "r") as f:
    content = f.read()

# Insert {% if request.page_type == 'index' %}{% render 'purelane-background' %}{% endif %} after <body ...>
body_pattern = r'(<body[^>]*>)'
replacement = r'\1\n    {% if request.page_type == \'index\' %}\n      {% render \'purelane-background\' %}\n    {% endif %}'

new_content = re.sub(body_pattern, replacement, content, count=1)

with open("layout/theme.liquid", "w") as f:
    f.write(new_content)

print("Injected purelane-background into theme.liquid!")

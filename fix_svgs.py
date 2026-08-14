import re

with open("purelane-homepage.html", "r") as f:
    html = f.read()

# find the SVG variables block which looks like:
# --p-combo2:url(...);
# --p-dish:url(...);
# ...
# --p-wm:url(...);

matches = re.findall(r'--p-[a-z0-9]+:url\("data:image/svg\+xml;base64,[^"]+"\);', html)
variables = "\n".join(matches)

css_to_add = f"\n:root {{\n{variables}\n}}\n"

with open("assets/purelane-base.css", "a") as f:
    f.write(css_to_add)

print("Added SVG variables to purelane-base.css")

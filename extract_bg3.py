import re

with open("purelane-homepage.html", "r") as f:
    content = f.read()

lines = content.split('\n')

html_block = '\n'.join(lines[825:885])

# CSS block specifically for scenes and water
css_lines = []
# Base CSS for scenes
css_lines.append('\n'.join(lines[63:123]))
# Light mode CSS for scenes
css_lines.append('@media (prefers-color-scheme: light) {')
# Add only the light mode overrides for the water elements
css_lines.append('\n'.join(lines[672:684]))
css_lines.append('}')

css_block = "<style>\n" + "\n".join(css_lines) + "\n</style>\n"

with open("snippets/purelane-background.liquid", "w") as out:
    out.write(css_block + html_block)

print("Updated snippets/purelane-background.liquid with exact correct CSS!")

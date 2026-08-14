import re

with open("snippets/purelane-background.liquid", "r") as f:
    content = f.read()

transparent_css = """
/* Make Shopify's default backgrounds transparent on the homepage so the cinematic background shows through */
body.gradient, .gradient { background: transparent !important; }
#MainContent { background: transparent !important; }
.section-header { background: transparent !important; }
"""

if "Make Shopify's default" not in content:
    content = content.replace("</style>", transparent_css + "</style>")

with open("snippets/purelane-background.liquid", "w") as f:
    f.write(content)

print("Transparency CSS re-added!")

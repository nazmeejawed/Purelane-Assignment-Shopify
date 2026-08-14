import re

with open("snippets/purelane-background.liquid", "r") as f:
    content = f.read()

transparent_css_v2 = """
/* Make Shopify's default backgrounds transparent on the homepage so the cinematic background shows through */
body.gradient, .gradient { background: transparent !important; }
#MainContent, .content-for-layout, .section-header { background: transparent !important; }
.color-scheme-1, .color-scheme-2, .color-scheme-3, .color-scheme-4, .color-scheme-5 { background: transparent !important; }
body { background: transparent !important; }
"""

# Replace the old transparency CSS with the new one
content = re.sub(
    r'/\* Make Shopify\'s default backgrounds transparent.*?\*/.*?#MainContent \{ background: transparent !important; \}.*?\.section-header \{ background: transparent !important; \}',
    transparent_css_v2,
    content,
    flags=re.DOTALL
)

with open("snippets/purelane-background.liquid", "w") as f:
    f.write(content)

print("Updated transparency CSS!")

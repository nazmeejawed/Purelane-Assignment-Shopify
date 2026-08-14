import re

with open("snippets/purelane-background.liquid", "r") as f:
    content = f.read()

# Add a CSS rule to make Shopify's default backgrounds transparent so our scenes can show through
transparent_css = """
/* Make Shopify's default backgrounds transparent on the homepage so the cinematic background shows through */
body.gradient, .gradient { background: transparent !important; }
#MainContent { background: transparent !important; }
.section-header { background: transparent !important; }
"""

# Insert before </style>
content = content.replace("</style>", transparent_css + "</style>")

with open("snippets/purelane-background.liquid", "w") as f:
    f.write(content)

print("Added transparency overrides to snippet.")

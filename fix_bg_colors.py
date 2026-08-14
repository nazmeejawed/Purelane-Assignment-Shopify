import re

with open("snippets/purelane-background.liquid", "r") as f:
    content = f.read()

# Replace the base s1-s4 and wl-a/b/c/s with the light mode ones directly
# Replace .scenes{...} to .scenes{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden;background:#eee7fb}
content = re.sub(
    r'\.scenes\{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden;background:var\(--brand\)\}',
    r'.scenes{position:fixed;inset:0;z-index:-1;pointer-events:none;overflow:hidden;background:#eee7fb}',
    content
)

# Replace .s1 to .s4
content = re.sub(
    r'\.s1\{background:linear-gradient\(178deg,#1ea38d 0%,#0b8578 22%,#017069 48%,#4b3a8f 74%,#01524e 100%\)\}',
    r'.s1{background:linear-gradient(178deg,#fbfffb 0%,#eafaec 24%,#d6f1dc 54%,#bfe8ca 100%)}',
    content
)
content = re.sub(
    r'\.s2\{background:linear-gradient\(178deg,#12907f 0%,#04756e 26%,#4b3a8f 58%,#01514d 100%\)\}',
    r'.s2{background:linear-gradient(178deg,#f6fdf7 0%,#e3f7e7 26%,#cbedd4 58%,#b2e2c2 100%)}',
    content
)
content = re.sub(
    r'\.s3\{background:linear-gradient\(178deg,#067c71 0%,#00625d 30%,#014e4a 64%,#023c39 100%\)\}',
    r'.s3{background:linear-gradient(178deg,#f0fbf2 0%,#d9f2df 28%,#bde6c8 60%,#a2d9b6 100%)}',
    content
)
content = re.sub(
    r'\.s4\{background:linear-gradient\(178deg,#036359 0%,#014b46 32%,#013431 66%,#012422 100%\)\}',
    r'.s4{background:linear-gradient(178deg,#e9f8ec 0%,#cdedd6 30%,#addcbe 62%,#8ecdaa 100%)}',
    content
)

# Replace wl-a, wl-b, wl-c, wl-s
content = re.sub(
    r'\.wl-a\{mix-blend-mode:screen;opacity:\.8;animation:drift-a 34s linear infinite\}',
    r'.wl-a{mix-blend-mode:soft-light;opacity:1;animation:drift-a 34s linear infinite}\n.wl-a .sv{filter:contrast(1.25)}',
    content
)
content = re.sub(
    r'\.wl-b\{mix-blend-mode:screen;opacity:\.54;animation:drift-b 23s linear infinite\}',
    r'.wl-b{mix-blend-mode:overlay;opacity:.66;animation:drift-b 23s linear infinite}',
    content
)
content = re.sub(
    r'\.wl-c\{mix-blend-mode:screen;opacity:\.5;animation:shaft-sway 19s ease-in-out infinite\}',
    r'.wl-c{mix-blend-mode:overlay;opacity:.6;animation:shaft-sway 19s ease-in-out infinite}',
    content
)
content = re.sub(
    r'\.wl-s\{mix-blend-mode:screen;opacity:\.7;animation:surface 11s ease-in-out infinite;transform-origin:50% 0\}',
    r'.wl-s{mix-blend-mode:overlay;opacity:.72;animation:surface 11s ease-in-out infinite;transform-origin:50% 0}',
    content
)

# Replace @media (prefers-color-scheme: light) block completely, moving contents to root level
# We can just remove the @media wrapper and closing brace
content = content.replace('@media (prefers-color-scheme: light) {', '')
# The closing brace is right before "/* Make Shopify's default"
content = content.replace('}\n\n/* Make Shopify\'s default', '\n/* Make Shopify\'s default')

# Let's also ensure .glass on light isn't duplicated or we don't care about it here since .glass isn't in this file's HTML anyway.

with open("snippets/purelane-background.liquid", "w") as f:
    f.write(content)

print("Updated purelane-background.liquid with light mode backgrounds!")

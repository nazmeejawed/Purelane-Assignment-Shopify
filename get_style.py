import re
with open("purelane-homepage.html", "r") as f:
    html = f.read()
style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
if style_match:
    with open("style_dump.css", "w") as f:
        f.write(style_match.group(1))

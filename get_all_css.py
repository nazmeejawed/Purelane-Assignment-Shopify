import re

with open("purelane-homepage.html", "r") as f:
    html = f.read()

styles = re.findall(r'<style>(.*?)</style>', html, re.DOTALL)
with open("style_dump.css", "w") as f:
    f.write("\n\n/* SECOND STYLE BLOCK */\n\n".join(styles))

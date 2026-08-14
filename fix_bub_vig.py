import re

with open("snippets/purelane-background.liquid", "r") as f:
    content = f.read()

# Replace .bub span
content = re.sub(
    r'\.bub span\{position:absolute;bottom:-6%;left:var\(--x\);width:var\(--s\);height:var\(--s\);border-radius:50%;\s*border:1px solid rgba\(230,255,242,\.5\);background:radial-gradient\(circle at 34% 30%,rgba\(255,255,255,\.42\),rgba\(255,255,255,0\) 62%\);\s*animation:rise var\(--dur\) linear infinite;animation-delay:var\(--dly\);opacity:0\}',
    r'.bub span{position:absolute;bottom:-6%;left:var(--x);width:var(--s);height:var(--s);border-radius:50%;\n  border:1px solid rgba(75,58,143,.26);background:radial-gradient(circle at 34% 30%,rgba(255,255,255,.9),rgba(255,255,255,0) 64%);\n  animation:rise var(--dur) linear infinite;animation-delay:var(--dly);opacity:0}',
    content
)

# Replace .vig
content = re.sub(
    r'\.vig\{position:absolute;inset:0;pointer-events:none;\s*background:radial-gradient\(126% 86% at 50% 28%,transparent 38%,rgba\(1,50,46,\.20\) 78%,rgba\(1,34,32,\.44\) 100%\),\s*linear-gradient\(180deg,rgba\(1,38,36,\.30\) 0%,transparent 18%,transparent 66%,rgba\(1,32,30,\.40\) 100%\)\}',
    r'.vig{position:absolute;inset:0;pointer-events:none;\n  background:\n  radial-gradient(126% 88% at 50% 26%,transparent 42%,rgba(75,58,143,.07) 80%,rgba(0,80,74,.16) 100%),\n  linear-gradient(180deg,rgba(255,255,255,.40) 0%,transparent 20%,transparent 70%,rgba(0,84,78,.10) 100%)}',
    content
)

with open("snippets/purelane-background.liquid", "w") as f:
    f.write(content)

print("Updated bub and vig for light mode!")

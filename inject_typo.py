import re

with open("sections/purelane-combos.liquid", "r") as f:
    content = f.read()

if ".kicker{" not in content:
    typo_css = """
/* ---------- TYPOGRAPHY & PANEL ---------- */
.kicker{display:inline-block;font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--paper-3);margin-bottom:8px}
.d2{font-family:'Outfit',sans-serif;font-size:clamp(28px,6vw,44px);font-weight:800;letter-spacing:-.01em;line-height:1;text-transform:uppercase;color:var(--surface)}
.lede{font-size:15px;color:var(--paper-2);line-height:1.55;max-width:54ch}
.panel-head{text-align:center;margin-bottom:26px}
.panel-head .d2{margin-bottom:12px}
.panel-head .rule{margin:0 auto;justify-content:center;max-width:240px}
.rule{display:flex;align-items:center;gap:12px;color:var(--accent)}
.rule i{flex:1;height:1px;background:linear-gradient(90deg,rgba(236,230,247,.44),transparent)}
.panel-head .rule i:first-child{background:linear-gradient(90deg,transparent,rgba(75,58,143,.34))}
.panel-head .rule i:last-child{background:linear-gradient(270deg,transparent,rgba(75,58,143,.34))}
.rule svg{width:16px;height:16px;flex:0 0 auto}
"""
    content = content.replace("<style>\n", f"<style>\n{typo_css}\n")
    
    with open("sections/purelane-combos.liquid", "w") as f:
        f.write(content)
        
print("Typography CSS appended to combos.")

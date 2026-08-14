import re

with open("sections/purelane-combos.liquid", "r") as f:
    content = f.read()

if ".btn{" not in content:
    btn_css = """
.btn{display:inline-flex;align-items:center;gap:10px;height:46px;padding:0 22px;border-radius:999px;
  font-family:'Outfit',sans-serif;font-weight:700;font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;
  transition:.3s var(--ease);text-decoration:none;cursor:pointer}
.btn svg{width:15px;height:15px;flex:0 0 auto}
.btn-primary{background:linear-gradient(135deg,#00706a,#004b46);color:#f4fdf6;
  box-shadow:0 12px 26px rgba(0,80,74,.22),inset 0 1px 0 rgba(255,255,255,.24)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 18px 36px rgba(0,80,74,.32),inset 0 1px 0 rgba(255,255,255,.28)}
.btn-ghost{background:rgba(255,255,255,.66);border:1px solid rgba(75,58,143,.22);color:#01423b;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.btn-ghost:hover{background:rgba(255,255,255,.9);transform:translateY(-2px)}
"""
    content = content.replace("<style>\n", f"<style>\n{btn_css}\n")
    
    with open("sections/purelane-combos.liquid", "w") as f:
        f.write(content)
        
print("Button CSS appended to combos.")

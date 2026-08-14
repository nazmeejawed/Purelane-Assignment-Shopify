import re

with open("sections/purelane-combos.liquid", "r") as f:
    content = f.read()

if ".glass{" not in content:
    glass_css = """
.glass{
  background:var(--g-bg);
  backdrop-filter:blur(24px) saturate(150%);
  -webkit-backdrop-filter:blur(24px) saturate(150%);
  border:1px solid var(--g-line);
  border-radius:var(--r);
  box-shadow:var(--g-shadow),var(--g-inset);
  position:relative;
  overflow:hidden;
}
.glass::after{content:"";position:absolute;inset:0;pointer-events:none;border-radius:inherit;
  box-shadow:inset 0 0 0 1px rgba(255,255,255,.07)}
@media(max-width:767px){
  .glass{backdrop-filter:blur(16px) saturate(140%);-webkit-backdrop-filter:blur(16px) saturate(140%)}
}
/* ---------- comborail, tiers, badges ---------- */
.tier .tag,.combo .prow em{background:rgba(201,118,29,.14);border:1px solid rgba(201,118,29,.34);color:#4f7d10}
.tier.best,.combo.hero-combo{border-color:rgba(201,118,29,.46);
  box-shadow:0 12px 34px rgba(0,74,66,.12),0 0 0 1px rgba(201,118,29,.25),var(--g-inset)}
.combo .tray{background:linear-gradient(162deg,rgba(255,255,255,.56),rgba(236,230,247,.34));
  border-bottom:1px solid rgba(255,255,255,.62)}
.combo .save{background:rgba(255,255,255,.84);border:1px solid rgba(201,118,29,.34);color:#4f7d10}
.combo .flag{background:linear-gradient(135deg,#00706a,#004b46);color:#f4fdf6}
"""
    content = content.replace("<style>\n", f"<style>\n{glass_css}\n")
    
    with open("sections/purelane-combos.liquid", "w") as f:
        f.write(content)
        
print("Glass CSS appended to combos.")

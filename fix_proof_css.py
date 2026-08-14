import re

with open("sections/purelane-proof.liquid", "r") as f:
    content = f.read()

css_to_add = """
    /* Core Layout & Typography */
    #Purelane-{{ section.id }} .glass {
      background: var(--g-bg);
      backdrop-filter: blur(24px) saturate(150%);
      -webkit-backdrop-filter: blur(24px) saturate(150%);
      border: 1px solid var(--g-line);
      border-radius: var(--r);
      box-shadow: var(--g-shadow), var(--g-inset);
      position: relative;
      overflow: hidden;
    }
    #Purelane-{{ section.id }} .glass::after {
      content: ""; position: absolute; inset: 0; pointer-events: none; border-radius: inherit;
      background: linear-gradient(115deg, rgba(255,255,255,.16), transparent 30%, transparent 72%, rgba(240,160,60,.07));
    }
    #Purelane-{{ section.id }} .glass-2 {
      background: linear-gradient(158deg, rgba(236,230,247,.10), rgba(0,48,46,.22));
      backdrop-filter: blur(18px) saturate(135%);
      -webkit-backdrop-filter: blur(18px) saturate(135%);
      border: 1px solid rgba(236,230,247,.16);
      border-radius: var(--r);
      box-shadow: 0 18px 48px rgba(18,12,34,.36), inset 0 1px 0 rgba(255,255,255,.16);
      position: relative; overflow: hidden;
    }
    #Purelane-{{ section.id }} .btn {
      display: inline-flex; align-items: center; gap: 10px; height: 46px; padding: 0 22px; border-radius: 999px;
      font-size: 12.5px; font-weight: 700; letter-spacing: .13em; text-transform: uppercase; transition: .35s var(--ease); white-space: nowrap;
      text-decoration: none;
    }
    #Purelane-{{ section.id }} .btn svg { width: 15px; height: 15px; flex: 0 0 auto; }
    #Purelane-{{ section.id }} .btn-primary {
      background: linear-gradient(135deg, var(--accent-2), #5d8d1c); color: #08211a;
      box-shadow: 0 12px 30px rgba(201,118,29,.34), inset 0 1px 0 rgba(255,255,255,.34);
    }
    #Purelane-{{ section.id }} .btn-primary:hover {
      transform: translateY(-2px); box-shadow: 0 18px 40px rgba(201,118,29,.44), inset 0 1px 0 rgba(255,255,255,.4);
    }
    #Purelane-{{ section.id }} .d2 {
      font-family: 'Outfit', system-ui, sans-serif; font-size: clamp(30px, 4.6vw, 54px); line-height: .94;
      text-transform: uppercase; letter-spacing: -.018em; font-weight: 800; color: var(--surface);
    }
    #Purelane-{{ section.id }} .body-s {
      font-size: 14.5px; color: var(--paper-2); line-height: 1.66;
    }
    #Purelane-{{ section.id }} .kicker {
      font-size: 11px; font-weight: 700; letter-spacing: .22em; text-transform: uppercase; color: var(--paper-3);
    }
    #Purelane-{{ section.id }} .sec-pad {
      padding: clamp(26px, 3.4vw, 40px);
    }
    @media(max-width: 760px) {
      #Purelane-{{ section.id }} .glass { backdrop-filter: blur(16px) saturate(140%); -webkit-backdrop-filter: blur(16px) saturate(140%); }
      #Purelane-{{ section.id }} .glass-2 { backdrop-filter: blur(12px) saturate(130%); -webkit-backdrop-filter: blur(12px) saturate(130%); }
      #Purelane-{{ section.id }} .sec-pad { padding: 22px 18px; }
    }
"""

if ".glass-2 {" not in content:
    content = content.replace("/* Scoped CSS for Proof Section */", "/* Scoped CSS for Proof Section */" + css_to_add)
    with open("sections/purelane-proof.liquid", "w") as f:
        f.write(content)
    print("Added base CSS to purelane-proof.liquid")
else:
    print("Already added.")

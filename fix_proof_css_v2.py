import re

with open("sections/purelane-proof.liquid", "r") as f:
    content = f.read()

new_style = """
  <style>
    /* Scoped CSS for Proof Section */
    #Purelane-{{ section.id }} .proof { display: grid; gap: 22px; grid-template-columns: 1fr; align-items: center; }
    @media(min-width: 900px) { #Purelane-{{ section.id }} .proof { grid-template-columns: .86fr 1.14fr; gap: 34px; } }
    #Purelane-{{ section.id }} .proof-l .d2 { margin-bottom: 14px; }
    #Purelane-{{ section.id }} .proof-l .btn { margin-top: 22px; }
    #Purelane-{{ section.id }} .stats { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; padding: 22px 18px; }
    @media(min-width: 640px) { #Purelane-{{ section.id }} .stats { grid-template-columns: repeat(4, 1fr); } }
    #Purelane-{{ section.id }} .stat { text-align: center; }
    #Purelane-{{ section.id }} .stat .ring {
      width: 74px; height: 74px; margin: 0 auto 11px; border-radius: 50%; display: grid; place-items: center;
      border: 1.5px solid rgba(75,58,143,.24); background: radial-gradient(circle at 34% 26%, rgba(255,255,255,.86), rgba(236,230,247,.52));
      font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 19px; color: var(--pl-surface); letter-spacing: -.02em;
    }
    #Purelane-{{ section.id }} .stat h5 { font-size: 10.5px; font-weight: 700; letter-spacing: .13em; text-transform: uppercase; color: var(--pl-accent); margin-bottom: 5px; }
    #Purelane-{{ section.id }} .stat p { font-size: 11.4px; color: var(--pl-paper-2); line-height: 1.44; }

    /* Rotator CSS */
    #Purelane-{{ section.id }} .rot { position: relative; padding: 18px 12px 16px; border-radius: 22px; display: flex; flex-direction: column; align-items: center; justify-content: center; }
    #Purelane-{{ section.id }} .rot .frame { position: relative; width: 100%; height: 206px; }
    #Purelane-{{ section.id }} .rot .frame .pimg { position: absolute; left: 50%; top: 50%; height: 196px; opacity: 0; filter: drop-shadow(0 11px 17px rgba(0,74,66,.14)); transform: translate(-50%, -50%) scale(0.96); transition: .6s var(--pl-ease); }
    #Purelane-{{ section.id }} .rot .frame .pimg.on { opacity: 1; transform: translate(-50%, -50%) scale(1); }
    #Purelane-{{ section.id }} .rot .cap { margin-top: 12px; text-align: center; min-height: 32px; }
    #Purelane-{{ section.id }} .rot .cap b { display: block; font-family: 'Outfit', sans-serif; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: .1em; color: var(--pl-surface); }
    #Purelane-{{ section.id }} .rot .cap span { display: block; font-size: 11px; color: var(--pl-paper-3); margin-top: 3px; }
    #Purelane-{{ section.id }} .rot .dots { display: flex; gap: 6px; justify-content: center; margin-top: 12px; }
    #Purelane-{{ section.id }} .rot .dots i { width: 5px; height: 5px; border-radius: 50%; background: rgba(75,58,143,.22); transition: .4s var(--pl-ease); }
    #Purelane-{{ section.id }} .rot .dots i.on { background: #b8701c; width: 17px; border-radius: 999px; }

    @media(max-width: 760px) {
      #Purelane-{{ section.id }} .stat .ring { width: 64px; height: 64px; font-size: 16.5px; }
      #Purelane-{{ section.id }} .rot .frame { height: 172px; }
      #Purelane-{{ section.id }} .rot .frame .pimg { height: 164px; }
    }

    /* Core Layout & Typography (Light Theme) */
    #Purelane-{{ section.id }} .glass {
      background: var(--pl-g-bg);
      backdrop-filter: blur(24px) saturate(150%);
      -webkit-backdrop-filter: blur(24px) saturate(150%);
      border: 1px solid var(--pl-g-line);
      border-radius: var(--pl-r);
      box-shadow: var(--pl-g-shadow), var(--pl-g-inset);
      position: relative;
      overflow: hidden;
    }
    #Purelane-{{ section.id }} .glass::after {
      content: ""; position: absolute; inset: 0; pointer-events: none; border-radius: inherit;
      background: linear-gradient(115deg, rgba(255,255,255,.55), transparent 32%, transparent 74%, rgba(201,118,29,.06));
    }
    #Purelane-{{ section.id }} .glass-2 {
      background: linear-gradient(158deg, rgba(255,255,255,.66), rgba(236,230,247,.44));
      backdrop-filter: blur(18px) saturate(135%);
      -webkit-backdrop-filter: blur(18px) saturate(135%);
      border: 1px solid rgba(75,58,143,.13);
      border-radius: var(--pl-r);
      box-shadow: 0 16px 38px rgba(58,44,112,.10), inset 0 1px 0 rgba(255,255,255,.86);
      position: relative; overflow: hidden;
    }
    #Purelane-{{ section.id }} .btn {
      display: inline-flex; align-items: center; gap: 10px; height: 46px; padding: 0 22px; border-radius: 999px;
      font-size: 12.5px; font-weight: 700; letter-spacing: .13em; text-transform: uppercase; transition: .35s var(--pl-ease); white-space: nowrap;
      text-decoration: none;
    }
    #Purelane-{{ section.id }} .btn svg { width: 15px; height: 15px; flex: 0 0 auto; }
    #Purelane-{{ section.id }} .btn-primary {
      background: linear-gradient(135deg, #00706a, #004b46); color: #f4fdf6;
      box-shadow: 0 12px 26px rgba(0,80,74,.26), inset 0 1px 0 rgba(255,255,255,.22);
    }
    #Purelane-{{ section.id }} .btn-primary:hover {
      transform: translateY(-2px); box-shadow: 0 18px 36px rgba(0,80,74,.32), inset 0 1px 0 rgba(255,255,255,.28);
    }
    #Purelane-{{ section.id }} .d2 {
      font-family: 'Outfit', system-ui, sans-serif; font-size: clamp(30px, 4.6vw, 54px); line-height: .94;
      text-transform: uppercase; letter-spacing: -.018em; font-weight: 800; color: var(--pl-surface);
    }
    #Purelane-{{ section.id }} .body-s {
      font-size: 14.5px; color: var(--pl-paper-2); line-height: 1.66; margin: 0;
    }
    #Purelane-{{ section.id }} .kicker {
      font-size: 11px; font-weight: 700; letter-spacing: .22em; text-transform: uppercase; color: var(--pl-paper-3);
    }
    #Purelane-{{ section.id }} .sec-pad {
      padding: clamp(26px, 3.4vw, 40px);
    }
    @media(max-width: 760px) {
      #Purelane-{{ section.id }} .glass { backdrop-filter: blur(16px) saturate(140%); -webkit-backdrop-filter: blur(16px) saturate(140%); }
      #Purelane-{{ section.id }} .glass-2 { backdrop-filter: blur(12px) saturate(130%); -webkit-backdrop-filter: blur(12px) saturate(130%); }
      #Purelane-{{ section.id }} .sec-pad { padding: 22px 18px; }
    }
  </style>"""

new_content = re.sub(r'<style>.*?</style>', new_style, content, flags=re.DOTALL)

with open("sections/purelane-proof.liquid", "w") as f:
    f.write(new_content)

print("Updated style block with --pl- variables and Light Theme styles")

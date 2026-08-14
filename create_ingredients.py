import re
import os

with open("purelane-homepage.html", "r") as f:
    content = f.read()

# Extract the ingredients section HTML
ing_match = re.search(r'<!-- ================= INGREDIENTS ================= -->(.*?)<!-- ================= PILLARS ================= -->', content, re.DOTALL)
ing_html = ing_match.group(1).strip() if ing_match else ""

# Extract the pillars section HTML
pillars_match = re.search(r'<!-- ================= PILLARS ================= -->(.*?)<!-- ================= PROOF ================= -->', content, re.DOTALL)
pillars_html = pillars_match.group(1).strip() if pillars_match else ""

# Create the liquid section combining both
liquid_content = f"""
{{%- comment -%}}
  Purelane Ingredients & Pillars Section
{{%- endcomment -%}}

<style>
  /* Scoped CSS for Purelane Ingredients & Pillars */
  #Purelane-{{{{ section.id }}}} {{
    --ink: #f4f0fb;
    --deep: #e2daf3;
    --brand: #4b3a8f;
    --brand-lt: #6b55b8;
    --paper: #241a3d;
    --paper-2: rgba(36,26,61,.78);
    --paper-3: rgba(36,26,61,.56);
    --accent: #b8701c;
    --accent-2: #c9761d;
    --surface: #17102b;
    --g-bg: linear-gradient(158deg, rgba(255,255,255,.80), rgba(236,230,247,.56) 58%, rgba(222,212,240,.50));
    --g-line: rgba(75,58,143,.16);
    --g-shadow: 0 22px 54px rgba(58,44,112,.13);
    --g-inset: inset 0 1px 0 rgba(255,255,255,.92);
    --r: 26px;
    --maxw: 1180px;
    --sec-y: 34px;
    --ease: cubic-bezier(.2,.7,.2,1);
  }}

  #Purelane-{{{{ section.id }}}} .sec {{ position: relative; padding: var(--sec-y) 0; }}
  #Purelane-{{{{ section.id }}}} .wrap {{ max-width: var(--maxw); margin: 0 auto; padding: 0 14px; }}
  #Purelane-{{{{ section.id }}}} .glass {{ background: var(--g-bg); border: 1px solid var(--g-line); border-radius: var(--r); box-shadow: var(--g-shadow), var(--g-inset); backdrop-filter: blur(22px); -webkit-backdrop-filter: blur(22px); }}
  #Purelane-{{{{ section.id }}}} .sec-pad {{ padding: clamp(26px, 3.4vw, 40px); }}
  
  #Purelane-{{{{ section.id }}}} .panel-head {{ text-align: center; margin-bottom: 26px; }}
  #Purelane-{{{{ section.id }}}} .panel-head .d2 {{ margin-bottom: 12px; font-family: 'Outfit', sans-serif; font-size: clamp(34px, 4vw, 46px); font-weight: 800; letter-spacing: -.03em; color: var(--surface); line-height: .96; }}
  #Purelane-{{{{ section.id }}}} .panel-head .rule {{ margin: 0 auto; justify-content: center; max-width: 240px; display: flex; align-items: center; gap: 14px; opacity: .4; color: var(--surface); }}
  #Purelane-{{{{ section.id }}}} .panel-head .rule i {{ flex: 1; height: 1.5px; background: linear-gradient(90deg, transparent, rgba(236,230,247,.44)); }}
  #Purelane-{{{{ section.id }}}} .panel-head .rule i:first-child {{ background: linear-gradient(90deg, transparent, rgba(236,230,247,.44)); }}
  #Purelane-{{{{ section.id }}}} .panel-head .rule svg {{ width: 22px; height: 22px; }}

  /* Ingredients */
  #Purelane-{{{{ section.id }}}} .ing {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 0; }}
  @media(min-width:760px) {{ #Purelane-{{{{ section.id }}}} .ing {{ grid-template-columns: repeat(5, 1fr); }} }}
  #Purelane-{{{{ section.id }}}} .ing-i {{ text-align: center; padding: 16px 12px; position: relative; }}
  @media(min-width:760px) {{ #Purelane-{{{{ section.id }}}} .ing-i + .ing-i::before {{ content: ""; position: absolute; left: 0; top: 14%; bottom: 14%; width: 1px; background: linear-gradient(180deg, transparent, rgba(236,230,247,.24), transparent); }} }}
  #Purelane-{{{{ section.id }}}} .ing-i .art {{ height: 88px; display: grid; place-items: center; margin-bottom: 12px; }}
  #Purelane-{{{{ section.id }}}} .ing-i .art svg {{ height: 84px; width: auto; }}
  #Purelane-{{{{ section.id }}}} .ing-i h4 {{ font-family: 'Outfit', sans-serif; font-size: 12.5px; font-weight: 700; letter-spacing: .11em; text-transform: uppercase; color: var(--surface); margin-bottom: 6px; }}
  #Purelane-{{{{ section.id }}}} .ing-i p {{ font-size: 12.2px; color: var(--paper-2); line-height: 1.5; }}

  /* Pillars */
  #Purelane-{{{{ section.id }}}} .pillars {{ display: grid; gap: 16px; grid-template-columns: 1fr; margin-top: 16px; }}
  @media(min-width:820px) {{ #Purelane-{{{{ section.id }}}} .pillars {{ grid-template-columns: repeat(3, 1fr); }} }}
  #Purelane-{{{{ section.id }}}} .pillar {{ padding: 26px 24px 24px; display: flex; flex-direction: column; }}
  #Purelane-{{{{ section.id }}}} .pillar .pi {{ width: 50px; height: 50px; border-radius: 15px; display: grid; place-items: center; margin-bottom: 16px; background: linear-gradient(150deg, rgba(240,160,60,.22), rgba(75,58,143,.34)); border: 1px solid rgba(236,230,247,.2); color: var(--accent); }}
  #Purelane-{{{{ section.id }}}} .pillar .pi svg {{ width: 24px; height: 24px; }}
  #Purelane-{{{{ section.id }}}} .pillar .d3 {{ margin-bottom: 11px; font-family: 'Outfit', sans-serif; font-size: clamp(20px, 2.2vw, 24px); font-weight: 700; letter-spacing: -.01em; color: var(--surface); line-height: 1.1; }}
  #Purelane-{{{{ section.id }}}} .pillar p {{ margin-bottom: 20px; flex: 1; font-size: 13.5px; color: var(--paper-2); line-height: 1.5; }}
  #Purelane-{{{{ section.id }}}} .pillar .btn {{ align-self: flex-start; }}
  
  /* Buttons */
  #Purelane-{{{{ section.id }}}} .btn {{ display: inline-flex; align-items: center; justify-content: center; gap: 10px; height: 46px; padding: 0 22px; border-radius: 999px; font-size: 12.5px; font-weight: 700; letter-spacing: .13em; text-transform: uppercase; transition: transform .35s var(--ease), box-shadow .35s var(--ease), background .35s var(--ease) !important; white-space: nowrap; text-decoration: none !important; }}
  #Purelane-{{{{ section.id }}}} .btn-sm {{ height: 38px; padding: 0 18px; font-size: 11px; letter-spacing: .14em; }}
  #Purelane-{{{{ section.id }}}} .btn-ghost {{ background: rgba(236,230,247,.10); border: 1px solid rgba(236,230,247,.30); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); color: var(--surface); }}
  #Purelane-{{{{ section.id }}}} .btn-ghost:hover {{ background: rgba(36,26,61,.08) !important; transform: translateY(-2px); }}

  /* Reveal Animations */
  #Purelane-{{{{ section.id }}}} .rv {{ opacity: 0; transform: translateY(30px); filter: blur(7px); transition: opacity .95s var(--ease), transform .95s var(--ease), filter .95s var(--ease); }}
  #Purelane-{{{{ section.id }}}} .rv.in {{ opacity: 1; transform: none; filter: none; }}
  #Purelane-{{{{ section.id }}}} .rv-d2 {{ transition-delay: .18s; }}
  #Purelane-{{{{ section.id }}}} .rv-d3 {{ transition-delay: .27s; }}
</style>

<div id="Purelane-{{{{ section.id }}}}">
  {ing_html}
  {pillars_html}
</div>

<script>
  (function() {{
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var revs = document.querySelectorAll('#Purelane-{{{{ section.id }}}} .rv');
    if ('IntersectionObserver' in window && !reduce && !document.body.classList.contains('shopify-design-mode')) {{
      var ro = new IntersectionObserver(
        function (es) {{
          es.forEach(function (e) {{
            if (e.isIntersecting) {{
              e.target.classList.add('in');
              ro.unobserve(e.target);
            }}
          }});
        }},
        {{ rootMargin: '0px 0px -12% 0px', threshold: 0.12 }}
      );
      revs.forEach(function (el) {{
        ro.observe(el);
      }});
    }} else {{
      revs.forEach(function (el) {{
        el.classList.add('in');
      }});
    }}
  }})();
</script>

{{% schema %}}
{{
  "name": "Purelane Ingredients",
  "settings": [],
  "presets": [
    {{
      "name": "Purelane Ingredients"
    }}
  ]
}}
{{% endschema %}}
"""

with open("sections/purelane-ingredients.liquid", "w") as f:
    f.write(liquid_content)

print("Created purelane-ingredients.liquid")

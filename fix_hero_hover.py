import re

with open("sections/purelane-hero.liquid", "r") as f:
    content = f.read()

# 1. Add CSS hover states for buttons
hover_css = """
  #PurelaneHero-{{ section.id }} .btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 16px 32px rgba(0,80,74,.32), inset 0 1px 0 rgba(255,255,255,.3) !important;
    filter: brightness(1.05);
  }
  #PurelaneHero-{{ section.id }} .btn-ghost:hover {
    background: rgba(36,26,61,.08) !important;
    transform: translateY(-2px);
  }
"""
content = content.replace("  #PurelaneHero-{{ section.id }} .btn svg {", hover_css + "  #PurelaneHero-{{ section.id }} .btn svg {")

# 2. Add bottle parallax logic in Javascript
# Find the end of the script, before "/* Fix SVG filters"
parallax_js = """
    /* Mouse Hover Parallax for Hero Products (Bottles) */
    if (window.matchMedia('(min-width: 1024px)').matches && stage && !reduce) {
      window.addEventListener('mousemove', function(e) {
        const mx = (e.clientX / window.innerWidth - 0.5) * 2;
        const my = (e.clientY / window.innerHeight - 0.5) * 2;
        
        // Move the entire stage slightly
        stage.style.transform = `translate3d(${ (mx * -16).toFixed(2) }px, ${ (my * -10).toFixed(2) }px, 0)`;
      }, { passive: true });
      
      // Reset when mouse leaves
      window.addEventListener('mouseleave', function() {
        stage.style.transform = `translate3d(0, 0, 0)`;
      });
    }

"""
content = content.replace("    /* Fix SVG filters and gradients in Shopify Theme Editor (<base> tag issues) */", parallax_js + "    /* Fix SVG filters and gradients in Shopify Theme Editor (<base> tag issues) */")

with open("sections/purelane-hero.liquid", "w") as f:
    f.write(content)

print("Updated JS and CSS")

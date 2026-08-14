import re

html_file = 'purelane-homepage.html'
with open(html_file, 'r') as f:
    content = f.read()

# CSS variables from V2
# They start with :root{ \n  --ink:#f4f0fb; ... }
v2_vars = re.search(r'(:root\s*\{[^}]+\})', content[content.find('VERSION 2 - BRAND COLOURS'):]).group(1)

# All CSS
# Actually, the user wants the exact prototype styles. To avoid conflicts with Dawn's global CSS, we can namespace them slightly, but the user said "SHOPIFY HERO = LOCAL PROTOTYPE HERO". So we'll put the exact CSS, but wrap it in a <style> block.
css1 = content[content.find('.kicker{'):content.find('/* ---------- SCROLL & HIGHLIGHT ---------- */')]
css2 = content[content.find('/* ============================================================') : content.find('/* ---------- PDP in brand colours ---------- */')]

# The scenes/SVG block
scenes_html = content[content.find('<div class="scenes"'):content.find('<!-- ================= TICKER ================= -->')]

# The hero HTML block
hero_html = content[content.find('<!-- ================= HERO ================= -->'):content.find('<!-- ================= CUSTOMER REVIEWS (auto marquee) ================= -->')]

# The script block
script_block = """<script>
document.addEventListener("DOMContentLoaded", () => {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var revs = document.querySelectorAll('.hero .rv');
  if ('IntersectionObserver' in window && !reduce) {
    var ro = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); ro.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.12 });
    revs.forEach(function (el) { ro.observe(el); });
  } else {
    revs.forEach(function (el) { el.classList.add('in'); });
  }

  /* Parallax and dots */
  var stage = document.getElementById('hstage');
  var dots = document.getElementById('hdots');
  var slides = stage ? [].slice.call(stage.querySelectorAll('.hslide')) : [];
  var dotBtns = dots ? [].slice.call(dots.querySelectorAll('button')) : [];
  var t;
  
  function setSlide(n) {
    slides.forEach(function(s, i) { s.classList.toggle('on', i === n); });
    dotBtns.forEach(function(b, i) { b.classList.toggle('on', i === n); });
  }
  
  dotBtns.forEach(function(b, i) {
    b.addEventListener('click', function() {
      clearInterval(t);
      setSlide(i);
    });
  });
  
  if (slides.length > 1) {
    var idx = 0;
    t = setInterval(function() {
      idx = (idx + 1) % slides.length;
      setSlide(idx);
    }, 4500);
  }
});
</script>"""

# The schema block
schema_block = """{% schema %}
{
  "name": "Hero (Purelane)",
  "tag": "section",
  "class": "purelane-hero-section",
  "settings": [
    {
      "type": "text",
      "id": "heading",
      "label": "Heading",
      "default": "Clean\\nThat\\nLasts"
    },
    {
      "type": "text",
      "id": "highlighted_word",
      "label": "Highlighted Word",
      "default": "Lasts"
    },
    {
      "type": "textarea",
      "id": "paragraph",
      "label": "Paragraph",
      "default": "Homecare that works on the toughest grime, made from plants. Kind to your home, your family and the world outside it."
    },
    {
      "type": "text",
      "id": "primary_cta_label",
      "label": "Primary CTA Label",
      "default": "Shop now"
    },
    {
      "type": "url",
      "id": "primary_cta_link",
      "label": "Primary CTA Link"
    },
    {
      "type": "text",
      "id": "secondary_cta_label",
      "label": "Secondary CTA Label",
      "default": "How it works"
    },
    {
      "type": "url",
      "id": "secondary_cta_link",
      "label": "Secondary CTA Link"
    }
  ],
  "blocks": [
    {
      "type": "trust_badge",
      "name": "Trust Badge",
      "limit": 3,
      "settings": [
        {
          "type": "select",
          "id": "icon",
          "label": "Icon",
          "options": [
            { "value": "plant", "label": "Plant" },
            { "value": "shield", "label": "Shield" },
            { "value": "check", "label": "Check" }
          ],
          "default": "plant"
        },
        {
          "type": "text",
          "id": "text",
          "label": "Badge Text",
          "default": "Plant\\npowered"
        }
      ]
    },
    {
      "type": "stage_slide",
      "name": "Stage Slide",
      "limit": 3,
      "settings": [
        {
          "type": "text",
          "id": "title",
          "label": "Title",
          "default": "Single bottle"
        },
        {
          "type": "text",
          "id": "price",
          "label": "Price",
          "default": "₹200"
        },
        {
          "type": "text",
          "id": "compare_price",
          "label": "Compare Price",
          "default": "₹299"
        },
        {
          "type": "text",
          "id": "discount_badge",
          "label": "Discount Badge",
          "default": "33% off"
        },
        {
          "type": "html",
          "id": "product_html",
          "label": "Products HTML",
          "info": "Overrides the default layout. E.g. <span class=\\"hp p-kbtl a d1\\"></span>"
        }
      ]
    }
  ],
  "presets": [
    {
      "name": "Hero (Purelane)",
      "blocks": [
        {
          "type": "trust_badge",
          "settings": { "icon": "plant", "text": "Plant\\npowered" }
        },
        {
          "type": "trust_badge",
          "settings": { "icon": "shield", "text": "Safe for\\nkids & pets" }
        },
        {
          "type": "trust_badge",
          "settings": { "icon": "check", "text": "Zero harsh\\nchemicals" }
        },
        {
          "type": "stage_slide",
          "settings": { "title": "Single bottle", "price": "₹200", "compare_price": "₹299", "discount_badge": "33% off" }
        },
        {
          "type": "stage_slide",
          "settings": { "title": "Any 2 products", "price": "₹349", "compare_price": "₹598", "discount_badge": "Save ₹249" }
        },
        {
          "type": "stage_slide",
          "settings": { "title": "Any 3 products", "price": "₹499", "compare_price": "₹897", "discount_badge": "Save ₹398" }
        }
      ]
    }
  ]
}
{% endschema %}"""

# To make the schema work, I must inject Liquid variables into the hero HTML.
hero_html = hero_html.replace(
    '<h1 class="d1 rv in">Clean<br>That<br><span class="lime">Lasts</span></h1>',
    """{%- assign heading_parts = section.settings.heading | split: section.settings.highlighted_word -%}
      <h1 class="d1 rv in">{{ heading_parts[0] | newline_to_br }}{% if section.settings.highlighted_word != blank %}<span class="lime">{{ section.settings.highlighted_word }}</span>{% endif %}{{ heading_parts[1] | newline_to_br }}</h1>"""
)

hero_html = hero_html.replace(
    '<p class="lede rv rv-d2">Homecare that works on the toughest grime, made from plants. Kind to your home, your family and the world outside it.</p>',
    '<p class="lede rv rv-d2">{{ section.settings.paragraph | escape }}</p>'
)

hero_html = hero_html.replace(
    '<a class="btn btn-primary" href="#shop">Shop now\n            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h13m-5-6 6 6-6 6"/></svg>\n          </a>',
    """{%- if section.settings.primary_cta_label != blank -%}
        <a class="btn btn-primary" href="{{ section.settings.primary_cta_link | default: '#' }}">{{ section.settings.primary_cta_label | escape }}
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h13m-5-6 6 6-6 6"/></svg>
        </a>
        {%- endif -%}"""
)

hero_html = hero_html.replace(
    '<a class="btn btn-ghost" href="#how">How it works</a>',
    """{%- if section.settings.secondary_cta_label != blank -%}
        <a class="btn btn-ghost" href="{{ section.settings.secondary_cta_link | default: '#' }}">{{ section.settings.secondary_cta_label | escape }}</a>
        {%- endif -%}"""
)

# Fix scenes CSS to be absolute instead of fixed, confined to the section
css1 = css1.replace('.scenes{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden;background:var(--brand)}', '.scenes{position:absolute;inset:0;z-index:0;pointer-events:none;overflow:hidden;background:var(--brand)}')
css1 = css1.replace('.hero{padding:142px 0 var(--sec-y);', '.hero{position:relative;padding:142px 0 var(--sec-y);overflow:hidden;')
# If .hero does not have position: relative, the .scenes div will overflow. I will add position:relative to .purelane-hero-section (the parent of .scenes).

with open('sections/purelane-hero.liquid', 'w') as out:
    out.write("<style>\n")
    out.write(v2_vars + "\n")
    out.write(".purelane-hero-section { position: relative; overflow: hidden; }\n")
    out.write(css1 + "\n")
    out.write(css2 + "\n")
    out.write("</style>\n")
    out.write(scenes_html + "\n")
    out.write(hero_html + "\n")
    out.write(script_block + "\n")
    out.write(schema_block + "\n")


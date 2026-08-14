import re
import json

html_template = """
<section id="Purelane-{{ section.id }}">
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
      border: 1.5px solid rgba(236,230,247,.3); background: radial-gradient(circle at 34% 26%, rgba(236,230,247,.18), rgba(75,58,143,.22));
      font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 19px; color: var(--surface); letter-spacing: -.02em;
    }
    #Purelane-{{ section.id }} .stat h5 { font-size: 10.5px; font-weight: 700; letter-spacing: .13em; text-transform: uppercase; color: var(--accent); margin-bottom: 5px; }
    #Purelane-{{ section.id }} .stat p { font-size: 11.4px; color: var(--paper-2); line-height: 1.44; }

    /* Rotator CSS */
    #Purelane-{{ section.id }} .rot { position: relative; padding: 18px 12px 16px; border-radius: 22px; display: flex; flex-direction: column; align-items: center; justify-content: center; }
    #Purelane-{{ section.id }} .rot .frame { position: relative; width: 100%; height: 206px; }
    #Purelane-{{ section.id }} .rot .frame .pimg { position: absolute; left: 50%; top: 50%; height: 196px; opacity: 0; filter: drop-shadow(0 11px 17px rgba(0,74,66,.14)); transform: translate(-50%, -50%) scale(0.96); transition: .6s var(--ease); }
    #Purelane-{{ section.id }} .rot .frame .pimg.on { opacity: 1; transform: translate(-50%, -50%) scale(1); }
    #Purelane-{{ section.id }} .rot .cap { margin-top: 12px; text-align: center; min-height: 32px; }
    #Purelane-{{ section.id }} .rot .cap b { display: block; font-family: 'Outfit', sans-serif; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: .1em; color: var(--surface); }
    #Purelane-{{ section.id }} .rot .cap span { display: block; font-size: 11px; color: var(--paper-3); margin-top: 3px; }
    #Purelane-{{ section.id }} .rot .dots { display: flex; gap: 6px; justify-content: center; margin-top: 12px; }
    #Purelane-{{ section.id }} .rot .dots i { width: 5px; height: 5px; border-radius: 50%; background: rgba(75,58,143,.22); transition: .4s var(--ease); }
    #Purelane-{{ section.id }} .rot .dots i.on { background: #b8701c; width: 17px; border-radius: 999px; }

    @media(max-width: 760px) {
      #Purelane-{{ section.id }} .stat .ring { width: 64px; height: 64px; font-size: 16.5px; }
      #Purelane-{{ section.id }} .rot .frame { height: 172px; }
      #Purelane-{{ section.id }} .rot .frame .pimg { height: 164px; }
    }
  </style>

  <section class="sec" id="{{ section.settings.section_id }}" data-scene="3">
    <div class="wrap">
      <div class="glass sec-pad rv">
        <div class="proof">
          <div class="proof-l">
            <span class="kicker">{{ section.settings.kicker }}</span>
            <h2 class="d2" style="margin-top:12px">{{ section.settings.heading | newline_to_br }}</h2>
            <p class="body-s" style="max-width:40ch">{{ section.settings.text }}</p>
            {% if section.settings.button_label != blank %}
            <a class="btn btn-primary" href="{{ section.settings.button_link }}">{{ section.settings.button_label }}
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h13m-5-6 6 6-6 6"/></svg>
            </a>
            {% endif %}
          </div>

          <div class="glass-2 rot" id="rot-{{ section.id }}" aria-hidden="true">
            <div class="frame">
              {% assign first = true %}
              {% for block in section.blocks %}
                {% if block.type == 'product' %}
                  <span class="pimg p-{{ block.settings.icon }} {% if first %}on{% endif %}" role="img" aria-label="{{ block.settings.title }}" data-name="{{ block.settings.title }}" data-note="{{ block.settings.note }}"></span>
                  {% assign first = false %}
                {% endif %}
              {% endfor %}
            </div>
            <div class="cap">
              {% for block in section.blocks %}
                {% if block.type == 'product' %}
                  <b>{{ block.settings.title }}</b><span>{{ block.settings.note }}</span>
                  {% break %}
                {% endif %}
              {% endfor %}
            </div>
            <div class="dots">
              {% assign first = true %}
              {% for block in section.blocks %}
                {% if block.type == 'product' %}
                  <i class="{% if first %}on{% endif %}"></i>
                  {% assign first = false %}
                {% endif %}
              {% endfor %}
            </div>
          </div>

          <div class="glass-2 stats proof-stats" style="grid-column:1/-1">
            {% for block in section.blocks %}
              {% if block.type == 'stat' %}
              <div class="stat">
                <div class="ring">{{ block.settings.ring_value }}</div>
                <h5>{{ block.settings.heading }}</h5>
                <p>{{ block.settings.text }}</p>
              </div>
              {% endif %}
            {% endfor %}
          </div>
        </div>
      </div>
    </div>
  </section>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      var rot = document.getElementById('rot-{{ section.id }}');
      if (rot) {
        var rimgs = [].slice.call(rot.querySelectorAll('.frame .pimg'));
        var rdots = [].slice.call(rot.querySelectorAll('.dots i'));
        var rcapB = rot.querySelector('.cap b');
        var rcapS = rot.querySelector('.cap span');
        var ri = 0, rtimer = null;
        function rstep() {
          if(!rimgs.length) return;
          rimgs[ri].classList.remove('on');
          if (rdots[ri]) rdots[ri].classList.remove('on');
          ri = (ri + 1) % rimgs.length;
          rimgs[ri].classList.add('on');
          if (rdots[ri]) rdots[ri].classList.add('on');
          rcapB.innerHTML = rimgs[ri].getAttribute('data-name');
          rcapS.textContent = rimgs[ri].getAttribute('data-note');
        }
        var mql = window.matchMedia('(prefers-reduced-motion: reduce)');
        if (!mql.matches && window.IntersectionObserver) {
          var rio = new IntersectionObserver(function (es) {
            es.forEach(function (e) {
              if (e.isIntersecting && !rtimer) rtimer = setInterval(rstep, 2900);
              else if (!e.isIntersecting && rtimer) { clearInterval(rtimer); rtimer = null; }
            });
          }, { threshold: 0.25 });
          rio.observe(rot);
        }
      }
    });
  </script>
</section>

{% schema %}
{
  "name": "Purelane Proof",
  "settings": [
    {
      "type": "text",
      "id": "section_id",
      "label": "Section ID",
      "default": "proof"
    },
    {
      "type": "text",
      "id": "kicker",
      "label": "Kicker",
      "default": "Why it works"
    },
    {
      "type": "textarea",
      "id": "heading",
      "label": "Heading",
      "default": "Tough on grime.\\nGentle on everything else."
    },
    {
      "type": "textarea",
      "id": "text",
      "label": "Text",
      "default": "Every formula is built on plant-derived cleansers and essential oils. It behaves exactly like the cleaner you are used to, minus the things you never signed up for."
    },
    {
      "type": "text",
      "id": "button_label",
      "label": "Button Label",
      "default": "See the ingredient list"
    },
    {
      "type": "url",
      "id": "button_link",
      "label": "Button Link"
    }
  ],
  "blocks": [
    {
      "type": "product",
      "name": "Product Rotator",
      "settings": [
        {
          "type": "select",
          "id": "icon",
          "label": "Product Icon",
          "options": [
            { "value": "kitchen", "label": "Kitchen Cleaner" },
            { "value": "tap", "label": "Tap Cleaner" },
            { "value": "laundry", "label": "Laundry Detergent" },
            { "value": "toilet", "label": "Toilet Cleaner" },
            { "value": "floor", "label": "Floor Cleaner" },
            { "value": "dish", "label": "Dishwash Gel" },
            { "value": "handwash", "label": "Handwash" },
            { "value": "metal", "label": "Metal Cleaner" },
            { "value": "wm", "label": "Washing Machine Cleaner" },
            { "value": "eraser", "label": "Magic Eraser" }
          ],
          "default": "kitchen"
        },
        {
          "type": "text",
          "id": "title",
          "label": "Title",
          "default": "Kitchen cleaner"
        },
        {
          "type": "text",
          "id": "note",
          "label": "Note",
          "default": "Foam lifts grease, no scrubbing"
        }
      ]
    },
    {
      "type": "stat",
      "name": "Stat",
      "settings": [
        {
          "type": "text",
          "id": "ring_value",
          "label": "Ring Value",
          "default": "99.9%"
        },
        {
          "type": "text",
          "id": "heading",
          "label": "Heading",
          "default": "Germ kill"
        },
        {
          "type": "text",
          "id": "text",
          "label": "Text",
          "default": "Tested against germs and bacteria"
        }
      ]
    }
  ],
  "presets": [
    {
      "name": "Purelane Proof",
      "blocks": [
        { "type": "product", "settings": { "icon": "kitchen", "title": "Kitchen cleaner", "note": "Foam lifts grease, no scrubbing" } },
        { "type": "product", "settings": { "icon": "tap", "title": "Tap & limescale", "note": "Melts hard water stains" } },
        { "type": "product", "settings": { "icon": "laundry", "title": "Laundry detergent", "note": "Tough on odour, soft on fabric" } },
        { "type": "product", "settings": { "icon": "toilet", "title": "Toilet cleaner", "note": "Kills 99.9% of germs" } },
        { "type": "product", "settings": { "icon": "floor", "title": "Floor cleaner", "note": "Neem powered, pet safe" } },
        { "type": "product", "settings": { "icon": "dish", "title": "Dishwash gel", "note": "Cuts grease, kind to hands" } },
        { "type": "stat", "settings": { "ring_value": "99.9%", "heading": "Germ kill", "text": "Tested against germs and bacteria" } },
        { "type": "stat", "settings": { "ring_value": "0%", "heading": "Sulphates", "text": "No SLS, chlorine or parabens" } },
        { "type": "stat", "settings": { "ring_value": "100%", "heading": "Plant based", "text": "Cleansers derived from plants" } },
        { "type": "stat", "settings": { "ring_value": "4.8", "heading": "Rated", "text": "Across 8,000+ verified reviews" } }
      ]
    }
  ]
}
{% endschema %}
"""

with open("sections/purelane-proof.liquid", "w") as f:
    f.write(html_template)
print("Created purelane-proof.liquid")

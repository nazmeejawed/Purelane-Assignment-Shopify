import json
import re

html_template = """<section class="sec" id="combos" data-scene="3">
  <div class="wrap">
    <div class="panel-head rv">
      <span class="kicker">{{ section.settings.kicker }}</span>
      <h2 class="d2" style="margin-top:12px">{{ section.settings.title }}</h2>
      <div class="rule"><i></i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21c0-6.5 3.5-11 8-12.5C20 15 16.5 20 12 21Z"/><path d="M12 21C12 14.5 8.5 10 4 8.5 4 15 7.5 20 12 21Z"/></svg><i></i></div>
      <p class="lede" style="margin:14px auto 0">{{ section.settings.description }}</p>
    </div>
    
    <div class="comborail rv">
      {%- for block in section.blocks -%}
      <article class="glass combo {% if block.settings.is_primary %}hero-combo{% endif %}" {{ block.shopify_attributes }}>
        <div class="tray">
          {%- if block.settings.saving_badge != blank -%}
          <span class="save">{{ block.settings.saving_badge }}</span>
          {%- endif -%}
          {%- if block.settings.flag_badge != blank -%}
          <span class="flag">{{ block.settings.flag_badge }}</span>
          {%- endif -%}
          
          <div class="stack">
            {%- for i in (1..5) -%}
              {%- assign p_class_key = 'p' | append: i | append: '_class' -%}
              {%- assign p_label_key = 'p' | append: i | append: '_label' -%}
              {%- assign p_class = block.settings[p_class_key] -%}
              {%- assign p_label = block.settings[p_label_key] -%}
              
              {%- if p_class != blank and p_class != 'none' -%}
                {%- if i > 1 -%}
                <span class="plus" aria-hidden="true">+</span>
                {%- endif -%}
                
                <span class="it">
                  {%- if p_class == 'p-tile' -%}
                  <span class="tile"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21c0-6.5 3.5-11 8-12.5C20 15 16.5 20 12 21Z"/><path d="M12 21C12 14.5 8.5 10 4 8.5 4 15 7.5 20 12 21Z"/></svg></span>
                  {%- else -%}
                  <span class="pimg {{ p_class }}" role="img" aria-label="{{ p_label | escape }}"></span>
                  {%- endif -%}
                  <span>{{ p_label }}</span>
                </span>
              {%- endif -%}
            {%- endfor -%}
          </div>
        </div>
        <div class="body">
          <h3>{{ block.settings.title }}</h3>
          <div class="cnt">{{ block.settings.product_count }}</div>
          <p class="inc">{{ block.settings.description }}</p>
          <div class="prow">
            <strong>{{ block.settings.price }}</strong>
            {%- if block.settings.compare_price != blank -%}<s>{{ block.settings.compare_price }}</s>{%- endif -%}
            {%- if block.settings.saving_text != blank -%}<em>{{ block.settings.saving_text }}</em>{%- endif -%}
          </div>
          <div class="fine">Inclusive of all taxes &middot; COD available</div>
          <a class="btn {% if block.settings.is_primary %}btn-primary{% else %}btn-ghost{% endif %}" href="{{ block.settings.button_link | default: '#bundles' }}">
            {{ block.settings.button_label }} 
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h13m-5-6 6 6-6 6"/></svg>
          </a>
        </div>
      </article>
      {%- endfor -%}
    </div>
    
    <div class="swipecue" aria-hidden="true">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h13m-5-6 6 6-6 6"/></svg>
      {{ section.settings.swipe_text }}
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Best Selling Combos",
  "settings": [
    {
      "type": "text",
      "id": "kicker",
      "label": "Eyebrow Text",
      "default": "Pre-built to save you money"
    },
    {
      "type": "text",
      "id": "title",
      "label": "Heading",
      "default": "Best selling combos"
    },
    {
      "type": "textarea",
      "id": "description",
      "label": "Description",
      "default": "Swipe through the boxes people order most. Each one is already priced below buying the same products on their own."
    },
    {
      "type": "text",
      "id": "swipe_text",
      "label": "Bottom Swipe Text",
      "default": "Swipe for more combos"
    }
  ],
  "blocks": [
    {
      "type": "combo",
      "name": "Combo Bundle",
      "settings": [
        {
          "type": "checkbox",
          "id": "is_primary",
          "label": "Highlight as Primary (Best Value)",
          "default": false
        },
        {
          "type": "text",
          "id": "saving_badge",
          "label": "Left Badge (e.g. You save ₹398)"
        },
        {
          "type": "text",
          "id": "flag_badge",
          "label": "Right Highlight Badge (e.g. Most popular)"
        },
        {
          "type": "header",
          "content": "Product Details"
        },
        {
          "type": "text",
          "id": "title",
          "label": "Combo Title",
          "default": "Kitchen essentials"
        },
        {
          "type": "text",
          "id": "product_count",
          "label": "Product Count Text",
          "default": "3 products"
        },
        {
          "type": "textarea",
          "id": "description",
          "label": "Description",
          "default": "Includes: Foaming Kitchen Cleaner, Dishwash Gel & Tap Cleaner."
        },
        {
          "type": "text",
          "id": "price",
          "label": "Current Price",
          "default": "₹499"
        },
        {
          "type": "text",
          "id": "compare_price",
          "label": "Compare-at Price",
          "default": "₹897"
        },
        {
          "type": "text",
          "id": "saving_text",
          "label": "Saving Text",
          "default": "Save ₹398"
        },
        {
          "type": "text",
          "id": "button_label",
          "label": "Button Label",
          "default": "Shop bundle"
        },
        {
          "type": "url",
          "id": "button_link",
          "label": "Button Link"
        }
      ]
    }
  ],
  "presets": [
    {
      "name": "Best Selling Combos"
    }
  ]
}
{% endschema %}
"""

# Now add the 5 product options dynamically to the schema
schema = json.loads(html_template.split('{% schema %}')[1].split('{% endschema %}')[0])

options = [
    {"value": "none", "label": "None (Hidden)"},
    {"value": "p-kitchen", "label": "Kitchen Cleaner"},
    {"value": "p-dish", "label": "Dishwash Gel"},
    {"value": "p-tap", "label": "Tap Cleaner"},
    {"value": "p-laundry", "label": "Laundry Detergent"},
    {"value": "p-tile", "label": "Leaf Tile (Fabric Cond.)"},
    {"value": "p-wm", "label": "Washing Machine Cleaner"},
    {"value": "p-floor", "label": "Floor Cleaner"},
    {"value": "p-handwash", "label": "Handwash"},
    {"value": "p-toilet", "label": "Toilet Cleaner"},
    {"value": "p-eraser", "label": "Magic Eraser"}
]

for i in range(1, 6):
    schema['blocks'][0]['settings'].extend([
        {
            "type": "header",
            "content": f"Product {i} Illustration"
        },
        {
            "type": "select",
            "id": f"p{i}_class",
            "label": "Icon",
            "options": options,
            "default": "none"
        },
        {
            "type": "text",
            "id": f"p{i}_label",
            "label": "Label",
            "default": ""
        }
    ])

# Rebuild the file
final_template = html_template.split('{% schema %}')[0] + '{% schema %}\n' + json.dumps(schema, indent=2) + '\n{% endschema %}\n'

with open("sections/purelane-combos.liquid", "w") as f:
    f.write(final_template)

print("Created purelane-combos.liquid successfully.")

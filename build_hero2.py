import re

html_file = 'purelane-homepage.html'
with open(html_file, 'r') as f:
    content = f.read()

with open('sections/purelane-hero.liquid', 'r') as f:
    hero_code = f.read()

badges_replacement = """<div class="badges glass-2" aria-label="Product promises">
      {%- for block in section.blocks -%}
        {%- if block.type == 'trust_badge' -%}
          <div class="badge" {{ block.shopify_attributes }}>
            <span class="bi">
              {%- if block.settings.icon == 'plant' -%}
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21c0-6.5 3.5-11 8-12.5C20 15 16.5 20 12 21Z"/><path d="M12 21C12 14.5 8.5 10 4 8.5 4 15 7.5 20 12 21Z"/></svg>
              {%- elsif block.settings.icon == 'shield' -%}
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 4.5 6v6.2c0 4.3 3.1 7.6 7.5 8.8 4.4-1.2 7.5-4.5 7.5-8.8V6L12 3Z"/><path d="m9 12 2.2 2.2L15.4 10"/></svg>
              {%- elsif block.settings.icon == 'check' -%}
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.4"/><path d="M6.4 17.6 17.6 6.4"/></svg>
              {%- endif -%}
            </span>
            <span>{{ block.settings.text | newline_to_br }}</span>
          </div>
        {%- endif -%}
      {%- endfor -%}
    </div>"""

# Replace the static badges
hero_code = re.sub(
    r'<div class="badges glass-2" aria-label="Product promises">.*?</div>\n    </div>',
    badges_replacement,
    hero_code,
    flags=re.DOTALL
)

# Badgestrip replacement
badgestrip_replacement = """<div class="badgestrip rv rv-d4">
        {%- for block in section.blocks -%}
          {%- if block.type == 'trust_badge' -%}
            <div class="glass-2">
              {%- if block.settings.icon == 'plant' -%}
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21c0-6.5 3.5-11 8-12.5C20 15 16.5 20 12 21Z"/><path d="M12 21C12 14.5 8.5 10 4 8.5 4 15 7.5 20 12 21Z"/></svg>
              {%- elsif block.settings.icon == 'shield' -%}
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 4.5 6v6.2c0 4.3 3.1 7.6 7.5 8.8 4.4-1.2 7.5-4.5 7.5-8.8V6L12 3Z"/><path d="m9 12 2.2 2.2L15.4 10"/></svg>
              {%- elsif block.settings.icon == 'check' -%}
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.4"/><path d="M6.4 17.6 17.6 6.4"/></svg>
              {%- endif -%}
              {{ block.settings.text | replace: '\n', ' ' }}
            </div>
          {%- endif -%}
        {%- endfor -%}
      </div>"""

hero_code = re.sub(
    r'<div class="badgestrip rv rv-d4">.*?</div>\n      </div>',
    badgestrip_replacement,
    hero_code,
    flags=re.DOTALL
)

# Replace the hero-prod slides
hstage_replacement = """<div class="hstage" id="hstage">
        {%- assign slide_blocks = section.blocks | where: 'type', 'stage_slide' -%}
        {%- if slide_blocks.size > 0 -%}
          {%- for block in slide_blocks -%}
            {%- assign slide_index = forloop.index -%}
            <div class="hslide hs{{ slide_index }} {% if slide_index == 1 %}on{% endif %}" data-n="{{ slide_index }}" {{ block.shopify_attributes }}>
              {%- if block.settings.product_html != blank -%}
                {{ block.settings.product_html }}
              {%- else -%}
                {%- if slide_index == 1 -%}
                  <span class="hp p-kbtl a d1" role="img" aria-label="Purelane foaming kitchen cleaner spray bottle"></span>
                {%- elsif slide_index == 2 -%}
                  <span class="hp p-tbtl a d1" role="img" aria-label="Purelane tap cleaner and limescale remover spray bottle"></span>
                  <span class="hp p-kbtl b d2" role="img" aria-label="Purelane foaming kitchen cleaner spray bottle"></span>
                {%- else -%}
                  <span class="hp p-tbtl a d1" role="img" aria-label="Purelane tap cleaner and limescale remover spray bottle"></span>
                  <span class="hp p-mbtl b d2" role="img" aria-label="Purelane copper, bronze and brass cleaner pump bottle"></span>
                  <span class="hp p-kbtl c d3" role="img" aria-label="Purelane foaming kitchen cleaner spray bottle"></span>
                {%- endif -%}
              {%- endif -%}
              <div class="glass-2 ptag">
                <span class="lbl">{{ block.settings.title }}</span>
                <span class="val"><strong>{{ block.settings.price }}</strong><s>{{ block.settings.compare_price }}</s></span>
                <span class="cut">{{ block.settings.discount_badge }}</span>
              </div>
            </div>
          {%- endfor -%}
        {%- endif -%}
      </div>"""

hero_code = re.sub(
    r'<div class="hstage" id="hstage">.*?</div></div><div class="hdots"',
    hstage_replacement + '</div><div class="hdots"',
    hero_code,
    flags=re.DOTALL
)

# Replace the hdots
hdots_replacement = """<div class="hdots" id="hdots">
        {%- assign slide_blocks = section.blocks | where: 'type', 'stage_slide' -%}
        {%- if slide_blocks.size > 0 -%}
          {%- for block in slide_blocks -%}
            <button type="button" class="{% if forloop.index == 1 %}on{% endif %}" aria-label="Show {{ forloop.index }} products"></button>
          {%- endfor -%}
        {%- endif -%}
      </div>"""

hero_code = re.sub(
    r'<div class="hdots" id="hdots">.*?</div></div>',
    hdots_replacement + '</div>',
    hero_code,
    flags=re.DOTALL
)


with open('sections/purelane-hero.liquid', 'w') as out:
    out.write(hero_code)


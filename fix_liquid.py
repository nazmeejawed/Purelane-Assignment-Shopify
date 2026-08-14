import re

with open("sections/purelane-combos.liquid", "r") as f:
    content = f.read()

# Replace the dynamic loop with explicit 5 blocks
old_loop = """          <div class="stack">
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
          </div>"""

new_loop = """          <div class="stack">
            {%- assign has_prev = false -%}
            
            {%- if block.settings.p1_class != blank and block.settings.p1_class != 'none' -%}
              <span class="it">
                {%- if block.settings.p1_class == 'p-tile' -%}
                <span class="tile"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21c0-6.5 3.5-11 8-12.5C20 15 16.5 20 12 21Z"/><path d="M12 21C12 14.5 8.5 10 4 8.5 4 15 7.5 20 12 21Z"/></svg></span>
                {%- else -%}
                <span class="pimg {{ block.settings.p1_class }}" role="img" aria-label="{{ block.settings.p1_label | escape }}"></span>
                {%- endif -%}
                <span>{{ block.settings.p1_label }}</span>
              </span>
              {%- assign has_prev = true -%}
            {%- endif -%}
            
            {%- if block.settings.p2_class != blank and block.settings.p2_class != 'none' -%}
              {%- if has_prev -%}<span class="plus" aria-hidden="true">+</span>{%- endif -%}
              <span class="it">
                {%- if block.settings.p2_class == 'p-tile' -%}
                <span class="tile"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21c0-6.5 3.5-11 8-12.5C20 15 16.5 20 12 21Z"/><path d="M12 21C12 14.5 8.5 10 4 8.5 4 15 7.5 20 12 21Z"/></svg></span>
                {%- else -%}
                <span class="pimg {{ block.settings.p2_class }}" role="img" aria-label="{{ block.settings.p2_label | escape }}"></span>
                {%- endif -%}
                <span>{{ block.settings.p2_label }}</span>
              </span>
              {%- assign has_prev = true -%}
            {%- endif -%}
            
            {%- if block.settings.p3_class != blank and block.settings.p3_class != 'none' -%}
              {%- if has_prev -%}<span class="plus" aria-hidden="true">+</span>{%- endif -%}
              <span class="it">
                {%- if block.settings.p3_class == 'p-tile' -%}
                <span class="tile"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21c0-6.5 3.5-11 8-12.5C20 15 16.5 20 12 21Z"/><path d="M12 21C12 14.5 8.5 10 4 8.5 4 15 7.5 20 12 21Z"/></svg></span>
                {%- else -%}
                <span class="pimg {{ block.settings.p3_class }}" role="img" aria-label="{{ block.settings.p3_label | escape }}"></span>
                {%- endif -%}
                <span>{{ block.settings.p3_label }}</span>
              </span>
              {%- assign has_prev = true -%}
            {%- endif -%}
            
            {%- if block.settings.p4_class != blank and block.settings.p4_class != 'none' -%}
              {%- if has_prev -%}<span class="plus" aria-hidden="true">+</span>{%- endif -%}
              <span class="it">
                {%- if block.settings.p4_class == 'p-tile' -%}
                <span class="tile"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21c0-6.5 3.5-11 8-12.5C20 15 16.5 20 12 21Z"/><path d="M12 21C12 14.5 8.5 10 4 8.5 4 15 7.5 20 12 21Z"/></svg></span>
                {%- else -%}
                <span class="pimg {{ block.settings.p4_class }}" role="img" aria-label="{{ block.settings.p4_label | escape }}"></span>
                {%- endif -%}
                <span>{{ block.settings.p4_label }}</span>
              </span>
              {%- assign has_prev = true -%}
            {%- endif -%}
            
            {%- if block.settings.p5_class != blank and block.settings.p5_class != 'none' -%}
              {%- if has_prev -%}<span class="plus" aria-hidden="true">+</span>{%- endif -%}
              <span class="it">
                {%- if block.settings.p5_class == 'p-tile' -%}
                <span class="tile"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21c0-6.5 3.5-11 8-12.5C20 15 16.5 20 12 21Z"/><path d="M12 21C12 14.5 8.5 10 4 8.5 4 15 7.5 20 12 21Z"/></svg></span>
                {%- else -%}
                <span class="pimg {{ block.settings.p5_class }}" role="img" aria-label="{{ block.settings.p5_label | escape }}"></span>
                {%- endif -%}
                <span>{{ block.settings.p5_label }}</span>
              </span>
            {%- endif -%}
          </div>"""

if old_loop in content:
    content = content.replace(old_loop, new_loop)
    with open("sections/purelane-combos.liquid", "w") as f:
        f.write(content)
    print("Fixed Liquid syntax for stack items.")
else:
    print("Old loop not found, checking if already replaced...")

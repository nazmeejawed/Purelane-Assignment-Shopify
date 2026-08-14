import re

with open("sections/purelane-hero.liquid", "r") as f:
    content = f.read()

# Make background of PurelaneHero transparent
content = content.replace("background: var(--ink);", "background: transparent;")

# Fix z-index of .scenes
content = content.replace("position: fixed; inset: 0; z-index: 0; pointer-events: none;", "position: fixed; inset: 0; z-index: -1; pointer-events: none;")

# Un-scope .scenes CSS
content = re.sub(r'#PurelaneHero-\{\{\s*section\.id\s*\}\}\s+\.(scenes|scene|s1|water|wl|wl-a|wl-b|wl-c|wl-s|bub)', r'.\1', content)

# Add global transparency CSS right after <style>
global_css = """
<style>
  body, .gradient, #MainContent, .shopify-section { background: transparent !important; }
"""
content = content.replace("<style>", global_css)

# Add JS script before <style>
js_script = """
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const scenes = document.querySelector('.scenes');
    if (scenes && scenes.parentElement !== document.body) {
      document.body.prepend(scenes);
    }
  });
</script>
"""
content = content.replace("<style>", js_script + "<style>")

with open("sections/purelane-hero.liquid", "w") as f:
    f.write(content)

print("Done")

import re

with open("snippets/purelane-background.liquid", "r") as f:
    content = f.read()

js_script = """
<script>
  (function() {
    var scenes = [].slice.call(document.querySelectorAll('.scene'));
    var stage = document.getElementById('scenes');
    var current = 0;
    
    function setScene(n) {
      if (n === current) return;
      current = n;
      scenes.forEach(function (s, i) { s.classList.toggle('on', i + 1 === n); });
      if (stage) stage.setAttribute('data-d', String(n));
    }
    
    function pickScene() {
      var zones = [].slice.call(document.querySelectorAll('[data-scene]'));
      var focus = window.scrollY + window.innerHeight * 0.5;
      var n = 1;
      
      for (var i = 0; i < zones.length; i++) {
        var z = zones[i], top = 0, el = z;
        while (el) { top += el.offsetTop; el = el.offsetParent; }
        if (top <= focus) n = parseInt(z.getAttribute('data-scene'), 10) || n;
      }
      setScene(n);
    }
    
    window.addEventListener('scroll', pickScene, {passive: true});
    window.addEventListener('resize', pickScene, {passive: true});
    
    // Initial check
    setTimeout(pickScene, 100);
  })();
</script>
"""

# Append script before closing div or at the very end
if "setScene(" not in content:
    content = content + js_script

with open("snippets/purelane-background.liquid", "w") as f:
    f.write(content)

print("Added background scroll JS!")

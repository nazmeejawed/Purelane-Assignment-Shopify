import re

with open("snippets/purelane-background.liquid", "r") as f:
    content = f.read()

# We need to replace the pickScene listener and add the frame logic
# Currently we have:
#     window.addEventListener('scroll', pickScene, {passive: true});
#     window.addEventListener('resize', pickScene, {passive: true});
#     
#     // Initial check
#     setTimeout(pickScene, 100);
#   })();
# </script>

# Let's extract the exact JS from the prototype and replace the current JS block completely for safety.

new_js = """<script>
  (function() {
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var scenes = [].slice.call(document.querySelectorAll('.scene'));
    var zones = [].slice.call(document.querySelectorAll('[data-scene]'));
    var stage = document.getElementById('scenes');
    var current = 0;
    
    function setScene(n) {
      if (n === current) return;
      current = n;
      scenes.forEach(function (s, i) { s.classList.toggle('on', i + 1 === n); });
      if (stage) stage.setAttribute('data-d', String(n));
    }
    
    function pickScene() {
      var focus = window.scrollY + window.innerHeight * 0.5, n = 1;
      for (var i = 0; i < zones.length; i++) {
        var z = zones[i], top = 0, el = z;
        while (el) { top += el.offsetTop; el = el.offsetParent; }
        if (top <= focus) n = parseInt(z.getAttribute('data-scene'), 10) || n;
      }
      setScene(n);
    }

    var hdr = document.getElementById('shopify-section-header');
    var prod = document.getElementById('heroProd');
    var raf = null, mx = 0, my = 0;

    function frame() {
      raf = null;
      var y = window.scrollY || window.pageYOffset;
      if (hdr) hdr.classList.toggle('up', y > 90);
      if (!reduce) {
        var wl = document.querySelectorAll('#water .wl');
        for (var i = 0; i < wl.length; i++) {
          var d = [0.05, 0.09, 0.03, 0.02][i] || 0.05;
          wl[i].style.setProperty('--px', (mx * d * 130).toFixed(1) + 'px');
          wl[i].style.setProperty('--py', (-y * d + my * d * 90).toFixed(1) + 'px');
        }
        if (prod) {
          var f = Math.min(y / 700, 1);
          prod.style.transform = 'translate3d(' + (mx * -16).toFixed(2) + 'px,' + (-f * 54 + my * -10).toFixed(2) + 'px,0) scale(' + (1 - f * 0.06).toFixed(3) + ')';
          prod.style.opacity = (1 - f * 0.55).toFixed(3);
        }
      }
      pickScene();
    }
    
    function onScroll() { if (!raf) raf = requestAnimationFrame(frame); }
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);

    if (!reduce && window.matchMedia('(min-width: 1024px)').matches) {
      window.addEventListener('mousemove', function (e) {
        mx = (e.clientX / window.innerWidth - 0.5) * 2;
        my = (e.clientY / window.innerHeight - 0.5) * 2;
        onScroll();
      }, { passive: true });
    }
    
    setTimeout(onScroll, 100);
  })();
</script>"""

# Replace the existing script block
content = re.sub(r'<script>\s*\(function\(\) \{.*?</script>', new_js, content, flags=re.DOTALL)

with open("snippets/purelane-background.liquid", "w") as f:
    f.write(content)

print("Updated JS successfully.")

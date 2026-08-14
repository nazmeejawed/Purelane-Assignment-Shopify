import re

with open("snippets/purelane-background.liquid", "r") as f:
    html = f.read()

# Make wl-a IDs unique
wl_a_start = html.find('<div class="wl wl-a">')
wl_b_start = html.find('<div class="wl wl-b">')
wl_a_chunk = html[wl_a_start:wl_b_start]

wl_a_chunk = wl_a_chunk.replace('id="cg"', 'id="cg-a"')
wl_a_chunk = wl_a_chunk.replace('url(#cg)', 'url(#cg-a)')
wl_a_chunk = wl_a_chunk.replace('id="wf"', 'id="wf-a"')
wl_a_chunk = wl_a_chunk.replace('url(#wf)', 'url(#wf-a)')
wl_a_chunk = wl_a_chunk.replace('id="wf2"', 'id="wf2-a"')
wl_a_chunk = wl_a_chunk.replace('url(#wf2)', 'url(#wf2-a)')

# Make wl-b IDs unique
wl_c_start = html.find('<div class="wl wl-c">')
wl_b_chunk = html[wl_b_start:wl_c_start]

wl_b_chunk = wl_b_chunk.replace('id="cg"', 'id="cg-b"')
wl_b_chunk = wl_b_chunk.replace('url(#cg)', 'url(#cg-b)')
wl_b_chunk = wl_b_chunk.replace('id="wf"', 'id="wf-b"')
wl_b_chunk = wl_b_chunk.replace('url(#wf)', 'url(#wf-b)')
wl_b_chunk = wl_b_chunk.replace('id="wf2"', 'id="wf2-b"')
wl_b_chunk = wl_b_chunk.replace('url(#wf2)', 'url(#wf2-b)')

# Reconstruct
html = html[:wl_a_start] + wl_a_chunk + wl_b_chunk + html[wl_c_start:]

with open("snippets/purelane-background.liquid", "w") as f:
    f.write(html)

print("Fixed SVG duplicate IDs.")

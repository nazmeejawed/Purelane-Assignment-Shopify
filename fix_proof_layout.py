import re

with open("sections/purelane-proof.liquid", "r") as f:
    content = f.read()

# Fix the .proof layout to match the correct layout from the prototype
content = re.sub(
    r'@media\(min-width: 900px\) \{ #Purelane-\{\{ section\.id \}\} \.proof \{ grid-template-columns: .86fr 1\.14fr; gap: 34px; \} \}',
    r'@media(min-width: 900px) { #Purelane-{{ section.id }} .proof { grid-template-columns: 1.05fr .62fr; gap: 30px; align-items: center; } }',
    content
)

# Also fix the base .proof just in case, removing align-items: center from base if it's there
content = re.sub(
    r'#Purelane-\{\{ section\.id \}\} \.proof \{ display: grid; gap: 22px; grid-template-columns: 1fr; align-items: center; \}',
    r'#Purelane-{{ section.id }} .proof { display: grid; gap: 22px; grid-template-columns: 1fr; }',
    content
)

# Add .proof-stats
if '.proof-stats' not in content:
    content = content.replace(
        '#Purelane-{{ section.id }} .proof-l .btn { margin-top: 22px; }',
        '#Purelane-{{ section.id }} .proof-l .btn { margin-top: 22px; }\n    #Purelane-{{ section.id }} .proof-stats { margin-top: 20px; }'
    )

with open("sections/purelane-proof.liquid", "w") as f:
    f.write(content)

print("Updated proof layout CSS")

import json

with open("templates/index.json", "r") as f:
    data = json.load(f)

if "purelane_combos_new" in data["sections"]:
    data["sections"]["purelane_combos_new"] = {
        "type": "purelane-combos",
        "settings": {}
    }

with open("templates/index.json", "w") as f:
    json.dump(data, f, indent=2)

print("Updated index.json to match minimal schema")

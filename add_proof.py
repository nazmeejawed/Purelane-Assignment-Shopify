import json

with open("templates/index.json", "r") as f:
    data = json.load(f)

# Create the section object
data["sections"]["purelane_proof_new"] = {
    "type": "purelane-proof",
    "settings": {}
}

# Insert into the order array
order = data["order"]
if "purelane_ingredients_QEtB80" in order:
    idx = order.index("purelane_ingredients_QEtB80")
    order.insert(idx + 1, "purelane_proof_new")
else:
    order.append("purelane_proof_new")

with open("templates/index.json", "w") as f:
    json.dump(data, f, indent=2)

print("Added purelane-proof to index.json")

import json

with open("templates/index.json", "r") as f:
    data = json.load(f)

# Add the missing blocks to purelane_proof_new
data["sections"]["purelane_proof_new"] = {
    "type": "purelane-proof",
    "blocks": {
        "prod_1": {
            "type": "product",
            "settings": {
                "icon": "dish",
                "title": "Dishwash gel",
                "note": "Cuts grease, kind to hands"
            }
        },
        "prod_2": {
            "type": "product",
            "settings": {
                "icon": "kitchen",
                "title": "Kitchen cleaner",
                "note": "Foam lifts grease, no scrubbing"
            }
        },
        "stat_1": {
            "type": "stat",
            "settings": {
                "ring_value": "99.9%",
                "heading": "Germ kill",
                "text": "Tested against germs and bacteria"
            }
        },
        "stat_2": {
            "type": "stat",
            "settings": {
                "ring_value": "0%",
                "heading": "Sulphates",
                "text": "No SLS, chlorine or parabens"
            }
        },
        "stat_3": {
            "type": "stat",
            "settings": {
                "ring_value": "100%",
                "heading": "Plant based",
                "text": "Cleansers derived from plants"
            }
        },
        "stat_4": {
            "type": "stat",
            "settings": {
                "ring_value": "4.8",
                "heading": "Rated",
                "text": "Across 8,000+ verified reviews"
            }
        }
    },
    "block_order": [
        "prod_1",
        "prod_2",
        "stat_1",
        "stat_2",
        "stat_3",
        "stat_4"
    ],
    "settings": {}
}

with open("templates/index.json", "w") as f:
    json.dump(data, f, indent=2)

print("Updated purelane_proof_new with blocks")

import json

file_path = "templates/index.json"

with open(file_path, "r") as f:
    data = json.load(f)

# Find the purelane-proof section
proof_key = None
for key, section in data.get("sections", {}).items():
    if section.get("type") == "purelane-proof":
        proof_key = key
        break

if proof_key:
    blocks = data["sections"][proof_key].get("blocks", {})
    
    # We will redefine the blocks entirely to match the 6 products and 4 stats
    new_blocks = {
        "prod_1": {
          "type": "product",
          "settings": {
            "icon": "kitchen",
            "title": "Kitchen cleaner",
            "note": "Foam lifts grease, no scrubbing"
          }
        },
        "prod_2": {
          "type": "product",
          "settings": {
            "icon": "tap",
            "title": "Tap & limescale",
            "note": "Melts hard water stains"
          }
        },
        "prod_3": {
          "type": "product",
          "settings": {
            "icon": "laundry",
            "title": "Laundry detergent",
            "note": "Tough on odour, soft on fabric"
          }
        },
        "prod_4": {
          "type": "product",
          "settings": {
            "icon": "toilet",
            "title": "Toilet cleaner",
            "note": "Kills 99.9% of germs"
          }
        },
        "prod_5": {
          "type": "product",
          "settings": {
            "icon": "floor",
            "title": "Floor cleaner",
            "note": "Neem powered, pet safe"
          }
        },
        "prod_6": {
          "type": "product",
          "settings": {
            "icon": "dish",
            "title": "Dishwash gel",
            "note": "Cuts grease, kind to hands"
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
    }
    
    data["sections"][proof_key]["blocks"] = new_blocks
    
    # Ensure block order is correct
    data["sections"][proof_key]["block_order"] = [
        "prod_1", "prod_2", "prod_3", "prod_4", "prod_5", "prod_6",
        "stat_1", "stat_2", "stat_3", "stat_4"
    ]
    
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)
    
    print("Updated templates/index.json successfully.")
else:
    print("purelane-proof section not found in templates/index.json")


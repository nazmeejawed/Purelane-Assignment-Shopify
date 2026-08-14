import json

with open("templates/index.json", "r") as f:
    data = json.load(f)

# Add the purelane_combos section
data["sections"]["purelane_combos_new"] = {
  "type": "purelane-combos",
  "blocks": {
    "combo_1": {
      "type": "combo",
      "settings": {
        "is_primary": False,
        "saving_badge": "You save ₹398",
        "flag_badge": "Most popular",
        "title": "Kitchen essentials",
        "product_count": "3 products",
        "description": "Includes: Foaming Kitchen Cleaner, Dishwash Gel & Tap Cleaner. Everything for a sparkling kitchen, no need to pick separately.",
        "price": "₹499",
        "compare_price": "₹897",
        "saving_text": "Save ₹398",
        "button_label": "Shop bundle",
        "p1_class": "p-kitchen",
        "p1_label": "Cuts grease instantly",
        "p2_class": "p-dish",
        "p2_label": "Squeaky clean dishes",
        "p3_class": "p-tap",
        "p3_label": "Melts hard water stains"
      }
    },
    "combo_2": {
      "type": "combo",
      "settings": {
        "is_primary": False,
        "saving_badge": "You save ₹448",
        "flag_badge": "",
        "title": "Laundry care bundle",
        "product_count": "3 products",
        "description": "Includes: Laundry Detergent, Fabric Conditioner & Machine Cleaner Powder. Softer, fresher wash, all in one box.",
        "price": "₹499",
        "compare_price": "₹947",
        "saving_text": "Save ₹448",
        "button_label": "Shop bundle",
        "p1_class": "p-laundry",
        "p1_label": "Removes tough stains & odour",
        "p2_class": "p-tile",
        "p2_label": "Softens & freshens every wash",
        "p3_class": "p-wm",
        "p3_label": "Deep-cleans your machine"
      }
    },
    "combo_3": {
      "type": "combo",
      "settings": {
        "is_primary": True,
        "saving_badge": "Biggest saving",
        "flag_badge": "Best value",
        "title": "Complete home bundle",
        "product_count": "5 products",
        "description": "Includes: Kitchen Cleaner, Laundry Detergent, Floor Cleaner, Toilet Cleaner & Handwash. Our biggest saving box.",
        "price": "₹799",
        "compare_price": "₹1,495",
        "saving_text": "Save ₹696",
        "button_label": "Shop bundle",
        "p1_class": "p-kitchen",
        "p1_label": "Cuts grease instantly",
        "p2_class": "p-floor",
        "p2_label": "Kills 99.9% germs",
        "p3_class": "p-handwash",
        "p3_label": "Gentle hydration for hands"
      }
    },
    "combo_4": {
      "type": "combo",
      "settings": {
        "is_primary": False,
        "saving_badge": "You save ₹398",
        "flag_badge": "",
        "title": "Bathroom deep clean",
        "product_count": "3 products",
        "description": "Includes: Toilet Cleaner, Tap Cleaner & Magic Eraser. A complete bathroom refresh in one box.",
        "price": "₹499",
        "compare_price": "₹897",
        "saving_text": "Save ₹398",
        "button_label": "Shop bundle",
        "p1_class": "p-toilet",
        "p1_label": "Kills 99.9% germs",
        "p2_class": "p-tap",
        "p2_label": "Melts hard water stains",
        "p3_class": "p-eraser",
        "p3_label": "Scrubs away soap scum"
      }
    },
    "combo_5": {
      "type": "combo",
      "settings": {
        "is_primary": False,
        "saving_badge": "You save ₹249",
        "flag_badge": "",
        "title": "Hard water solution kit",
        "product_count": "2 products",
        "description": "Includes: Tap Cleaner & Toilet Cleaner. A quick, focused fix for hard water stains across the home.",
        "price": "₹349",
        "compare_price": "₹598",
        "saving_text": "Save ₹249",
        "button_label": "Shop bundle",
        "p1_class": "p-tap",
        "p1_label": "Melts hard water stains",
        "p2_class": "p-toilet",
        "p2_label": "Fights limescale in the bowl"
      }
    }
  },
  "block_order": ["combo_1", "combo_2", "combo_3", "combo_4", "combo_5"],
  "settings": {}
}

if "purelane_combos_new" not in data["order"]:
    # add combos right after proof section if it exists, or at the end
    if "purelane_proof_new" in data["order"]:
        idx = data["order"].index("purelane_proof_new")
        data["order"].insert(idx + 1, "purelane_combos_new")
    else:
        data["order"].append("purelane_combos_new")

with open("templates/index.json", "w") as f:
    json.dump(data, f, indent=2)

print("Added purelane_combos to index.json")

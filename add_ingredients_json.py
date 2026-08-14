import json
import uuid
import string
import random
import re

def generate_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

with open('templates/index.json', 'r') as f:
    content = f.read()

# Strip comments (multiline)
content_no_comments = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

data = json.loads(content_no_comments)

# Add the purelane_ingredients section
ing_id = f"purelane_ingredients_{generate_id()}"

data['sections'][ing_id] = {
    "type": "purelane-ingredients",
    "settings": {}
}

# Insert it after purelane_reviews
if "purelane_reviews_7piJX4" in data['order']:
    idx = data['order'].index("purelane_reviews_7piJX4")
    data['order'].insert(idx + 1, ing_id)
else:
    data['order'].append(ing_id)

with open('templates/index.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Updated templates/index.json")

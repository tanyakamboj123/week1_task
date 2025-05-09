import json
import os

# Step 1: Load JSON from file
with open('products.json', 'r') as infile:
    products = json.load(infile)

# Step 2: Filter products with price >= 129.37
filtered = [p for p in products if p["price"] >= 129.37]

# Step 3: Sort by category (A-Z), then price (high to low), then name (A-Z)
sorted_products = sorted(filtered, key=lambda x: (x["category"], -x["price"], x["name"]))

# Step 4: Save the result to a new JSON file (optional)
with open('sorted_filtered_products.json', 'w') as outfile:
    json.dump(sorted_products, outfile, indent=4)

# Also print to console
print(json.dumps(sorted_products, indent=4))

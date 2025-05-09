import json

# Load both JSON files
with open('config_old.json', 'r') as f:
    old_config = json.load(f)

with open('config_new.json', 'r') as f:
    new_config = json.load(f)

# Convert lists to dictionaries using 'key' as the identifier
old_dict = {entry['key']: entry['value'] for entry in old_config}
new_dict = {entry['key']: entry['value'] for entry in new_config}

# Count differences
diff_count = sum(
    1 for key in old_dict if key in new_dict and old_dict[key] != new_dict[key]
)

print(f"Number of settings with a different value: {diff_count}")
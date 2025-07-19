import json

with open("tusimple_train.json", "r") as f:
    data = json.load(f)

for item in data:
    item["raw_file"] = f"clips/{item['raw_file']}"

with open("tusimple_train.json", "w") as f:
    json.dump(data, f)

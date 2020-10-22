import json

with open("states.json") as f:
    data = json.load(f)

for state in data["states"]:
    print(state["name"], state["abbreviation"])
    del state["abbreviation"]

with open("new_states.json", "w") as f:
    json.dump(data, f, indent=2)
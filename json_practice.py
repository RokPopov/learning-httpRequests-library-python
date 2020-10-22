import json

people_string = """
{
"people": [
    {
        "name": "John Smith",
        "phone": "555-555-555",
        "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
        "has_license": false
    },
    {
        "name": "Jane Doe",
        "phone": "444-444-444",
        "emails": null,
        "has_license": true
    }
    ]
    }
"""

data = json.loads(people_string)

# print(type(data["people"]))
# print(data)

for person in data["people"]:
    print(person["name"])

for person in data["people"]:
    del person["phone"]

new_string = json.dumps(data, indent=2, sort_keys=True)

print(new_string)
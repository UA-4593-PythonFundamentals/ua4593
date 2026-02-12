import json
# import xml 
# import csv


# with open('lessons\\lesson14\\example.json', 'r') as file:
#     data = json.load(file)
#     print(type(data))
#     from pprint import pprint
#     pprint(data, indent=4, width=45, compact=False)


# json_string = """{
#   "user": "Alice Brown",
#   "hobbies": ["reading", "hiking", "gaming"],
#   "address": {
#     "street": "123 Main St",
#     "city": "New York",
#     "zip": "10001"
#   }
# }"""
# data = json.loads(json_string)
# pprint(data, indent=4, width=45, compact=False)




person = {
    'name': 'Anna Schmidt',
    'age': 28,
    'city': 'Berlin',
    'email': 'anna@example.de',
    "hobbies": ["reading", "hiking", "gaming"],
}

with open('lessons\\lesson14\\person.json', 'w') as file:
    json.dump(person, file, indent=4)

json_string = json.dumps(person)
print(json_string)
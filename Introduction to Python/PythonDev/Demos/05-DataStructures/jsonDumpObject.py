# Import the standard JSON module.
import json

# A Python dictionary.
person = {"name": "Andy", "age": 21, "height": 1.67, "isWelsh": True }

# Dump Python dictionary into a JSON string. 
personJson = json.dumps(person, indent=4)  

# Use the JSON string (e.g. in a real example, send it to a REST service).
print(personJson)

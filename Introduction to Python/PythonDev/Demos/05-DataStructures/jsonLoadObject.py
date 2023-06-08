# Import the standard JSON module.
import json

# A simple string of JSON data.
personJson = '{"name": "Andy", "age": 21, "height": 1.67, "isWelsh": true }'

# Load JSON string into a Python dictionary. 
person = json.loads(personJson)  

# Use the Python dictionary.
print("%s is %d years old" % (person["name"], person["age"]))
print("Height is %.2f, Welshness is %s" % (person["height"], person["isWelsh"]))

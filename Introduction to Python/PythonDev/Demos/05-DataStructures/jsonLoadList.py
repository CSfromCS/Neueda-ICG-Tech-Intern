# Import the standard JSON module.
import json

# A simple string of JSON data, representing an array.
coordsJson = '[ { "x": 100, "y": 150 }, { "x": 200, "y": 250 } ]'

# Load JSON string into a Python list. 
coords = json.loads(coordsJson)

# Use the Python list.
print("Point 0 is %d, %d" % (coords[0]["x"], coords[0]["y"]))
print("Point 1 is %d, %d" % (coords[1]["x"], coords[1]["y"]))

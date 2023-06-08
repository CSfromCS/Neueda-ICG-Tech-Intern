import json

with open("sampledata.json") as fh:

    for line in fh:
        obj = json.loads(line)
        print("%s,%d,%f" % (obj["name"], obj["age"], obj["salary"]))
        
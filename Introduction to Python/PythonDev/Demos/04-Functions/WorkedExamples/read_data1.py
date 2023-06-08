import re

pattern = re.compile('Attribute ID \(0xC2\)')

with open('data.txt') as fh:
    for line in fh:
        result = pattern.search(line)
        if result:
            print(line)
		
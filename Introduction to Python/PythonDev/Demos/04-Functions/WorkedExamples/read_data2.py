import re

reObj = re.compile('Attribute ID \(0xC2\)')

def process_line(line):
    result = reObj.search(line)
    if result:
        print(line)
		
with open('data.txt') as fh:
    for line in fh:
        process_line(line)


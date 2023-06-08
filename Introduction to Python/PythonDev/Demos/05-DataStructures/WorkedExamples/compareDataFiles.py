import re

file1Attributes = set()
file2Attributes = set()

reObj = re.compile('Attribute ID \(0x..\)\s+(.+)')

def process_line(line, theSet):
    match = reObj.search(line)
    if match:
        theSet.add(match.group(1))
		
def process_file(filename):
    attributes = set()
    with open(filename) as fh:
        for line in fh:
            process_line(line, attributes)
    return attributes

# main code
file1Attributes = process_file('dataFile1.txt')
file2Attributes = process_file('dataFile2.txt')

print('Atrributes that are common in both files:')
print(file1Attributes.intersection(file2Attributes))


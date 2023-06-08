import re

reObj = re.compile('Attribute ID \(0xC2\)')
lineNumber = 1

def process_line(line, fhOut):
    result = reObj.search(line)
    if result:
        global lineNumber
        str = '[{0:03d}]: {1}'.format(lineNumber, line)
        fhOut.write(str)
        lineNumber += 1

def process_files(filename1, filename2) :
    with open(filename1, 'r') as fh1, open(filename2, 'w') as fh2:
        for line in fh1:
            process_line(line, fh2)

if __name__ == '__main__':
    process_files('data.txt', 'result.txt')
    print('Written %d lines to result.txt' % (lineNumber-1))




		

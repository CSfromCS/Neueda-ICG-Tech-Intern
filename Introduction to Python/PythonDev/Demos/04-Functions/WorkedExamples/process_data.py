import re

# Global variables.
attr_pattern = re.compile('Attribute ID \(0xC2\)')
data_pattern = re.compile('Vendor Specific \(hex\): ([0-9A-Fa-f]{2} [0-9A-Fa-f]{2}) ([0-9A-Fa-f]{2} [0-9A-Fa-f]{2}) ([0-9A-Fa-f]{2} [0-9A-Fa-f]{2})')
count = 0


# Find the next line that contains the text matching the regexp in attr_pattern.
def find_attribute_line(fh):
    for line in fh:
        result = attr_pattern.search(line)
        if result:
            return line


# Find the next line that contains the text matching the regexp in data_pattern.			
def process_attribute_data(fh, line):
    
    global count
    count += 1
	
    print("[%d] %s" % (count, line))
    
    for line in fh:
        result = data_pattern.search(line)
        if result:
            groups = result.groups()
            print("Value 0: [%s] %s" % (groups[0], parse_hex_bytes(groups[0])))
            print("Value 1: [%s] %s" % (groups[1], parse_hex_bytes(groups[1])))
            print("Value 2: [%s] %s" % (groups[2], parse_hex_bytes(groups[2])))
            print("----------------------------------------------------------------------------------------------------")
            break
			
			
# Convert a string of hex in the format "XX XX" into a decimal (i.e. denary) number.	
def parse_hex_bytes(str):
    nums = str.split()
    hex = nums[0] + nums[1]
    dec = int(hex, 16)

	# If the top bit is set, treat the number as negative. E.g. convert FFFF to -1.
    if dec & 0x8000: 	
        dec = -((~dec & 0xffff) + 1)
	
    return dec
	
	
# Main code			
with open('data.txt') as fh:
    while True:
        line = find_attribute_line(fh)
        if line:
            process_attribute_data(fh, line)			
        else:
            break		
    			
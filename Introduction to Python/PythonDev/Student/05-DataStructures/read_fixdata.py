# Import all the handler functions for FIX fields.
from handlers import *


# Global variables.
__tokenseparator = "\x01"    # "\x01" is ASCII hex code 01, i.e. the "Start of Header" character in FIX.
__kvseparator = "="


# Function to split a line of FIX data into tokens, using __tokenseperator as the separator.        
def tokenize_line(line):

    # TODO 2a: 
    # Split the line of text into tokens, using __tokenseperator as the separator.

    # TODO 2b: 
    # Create an empty dictionary, ready to hold all the FIX keys/values.
    
    # TODO 2c: 
    # Loop through all the tokens (from 2a above). 
    #    Split each token at the = character, into a key/value pair.
    #    Insert the key/value pair into the dictionary.
    
    # TODO 2d: Return the dictionary.

    
    
# Function to process a dictionary of FIX key/value pairs.
def process_data(datadict):

    # TODO 3:
	# Loop through all the key/value pairs in datadict. For each key/value pair, do the following:
	#     Call the appropriate handler function, depending on the key (pass the value as a parameter). 
	#     E.g. if the key is "8", call proc8(value)
	#     E.g. if the key is "9", call proc9(value)
	#     E.g. if the key is "35", call proc35(value)
	#     Etc... (if the key is anything else, call proc_other(value) instead)

	
# Main code.            
with open('fixdata.txt') as fh:
    for line in fh:
        datadict = tokenize_line(line)
        print(datadict)
        process_data(datadict)

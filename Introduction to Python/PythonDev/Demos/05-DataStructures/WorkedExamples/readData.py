# Keep a dictionary of goals scored for each player.
# The key is the name of a player.
# The value is a set of goals scored by that player.
goals_dict = dict()

# Process data for a player name and the list of goals for that player.
def process_data(name, goals_string):

    # Split the goals-scored string into a list of separate values, and add them all to a set.
    goals_list = goals_string.split(',')	
    goals_set  = set(goals_list)	

    # Insert player into dictionary if not already present.
    if goals_dict.get(name):
        goals_dict[name].update(goals_set)	# For existing player, merge the new set with the existing set.
    else:	
        goals_dict[name] = goals_set        # Insert as a new player with a new set.
	
	
# Main code - process the file and populate goals_dict with all the info.		
with open('data.txt') as fh:

    # Loop through all the lines of text in the file.
    for name in fh:
	
        # Read the name of a player (strip off the trailing \r\n).
        name = name.rstrip('\r\n')
		
		# Read the goals-scored list (strip off trailing \r\n).
        goals_string = fh.readline().rstrip('\r\n')
		
		# Process the data we just read in.
        process_data(name, goals_string)

		
# Display the goal-scoring pattern for each player.
for k,v in goals_dict.items():
    print("%s\t%s" % (k, v))

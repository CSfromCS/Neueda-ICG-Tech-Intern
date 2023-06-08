import greetings

print("Name of current module is %s" % __name__)
print("Name of greetings module is %s" % greetings.__name__)

'''
I added the following statements.
Note that reload() is in the imp module.
'''	
print("I'm now going to reload the greetings module...")
from imp import reload 
reload(greetings)
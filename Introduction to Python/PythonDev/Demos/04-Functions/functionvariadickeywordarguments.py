# This function has variadic keyword arguments.
def myfunc(**kwargs):
  for key, value in kwargs.items(): 
    print("key %s, value %s" % (key, value)) 

# This function has variadic positional arguments and variadic keyword arguments.
def myfunc2(*args, **kwargs):
  print("Variadic positional args:")
  for arg in args:
    print("  %s" % arg)

  print("Variadic keyword args:")
  for key, value in kwargs.items(): 
    print ("  key %s, value %s" % (key, value)) 

# Usage of myfunc():
myfunc(favTeam="Swans", favNum=3, favColour="red")

# Usage of myfunc2():
myfunc2("Ole", "Dole", "Doffen", favTeam="Swans", favNum=3)


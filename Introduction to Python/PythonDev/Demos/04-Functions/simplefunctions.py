def say_goodmorning():
  print("Start of say_goodmorning")
  print(" Good morning!")
  print("End of say_goodmorning\n")

def say_goodafternoon():
  print("Start of say_goodafternoon")
  print("  Good afternoon!")
  print("End of say_goodafternoon\n")

def say_goodevening():
  pass


# Usage (i.e. client code)
say_goodmorning()
say_goodafternoon()
say_goodevening()

f = say_goodmorning   
f()                   # Calls say_goodmorning() really

print("THE END")

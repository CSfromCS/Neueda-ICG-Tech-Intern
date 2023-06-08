def display_favourite_things(name, *things):
  print("Favourite things for %s" % name)
  for thing in things:
    print("  %s" % thing)

# Usage (i.e. client code)
display_favourite_things("Andy", "Jayne", "Emily", "Thomas", 3, "Swans")

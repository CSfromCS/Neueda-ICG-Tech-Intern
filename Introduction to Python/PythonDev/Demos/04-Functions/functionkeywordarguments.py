def book_flight(fromairport, toairport, numadults=1, numchildren=0):
  print("\nFlight booked from %s to %s" % (fromairport, toairport))
  print("Number of adults: %d" % numadults)
  print("Number of children: %d" % numchildren)

# Usage (i.e. client code)
book_flight(fromairport="BRS", toairport="VER", numadults=2, numchildren=2)
book_flight("LHR", "CDG", numchildren=2)
book_flight(numchildren=3, fromairport="LGW", toairport="NCE")

# This call would be invalid:
# book_flight(numchildren=3, "LGW", "NCE")

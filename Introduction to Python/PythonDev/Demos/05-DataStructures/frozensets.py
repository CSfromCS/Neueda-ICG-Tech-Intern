set1 = frozenset({"dog", "ant", "bat", "cat", "dog"})
set2 = frozenset()
set3 = frozenset(("dog", "ant", "bat", "cat", "dog"))
set4 = frozenset("abracadabra")
set5 = frozenset({c.upper() for c in "abracadabra"})

print("set1 has %d items: %s" % (len(set1), set1))
print("set2 has %d items: %s" % (len(set2), set2))
print("set3 has %d items: %s" % (len(set3), set3))
print("set4 has %d items: %s" % (len(set4), set4))
print("set5 has %d items: %s" % (len(set5), set5))
      

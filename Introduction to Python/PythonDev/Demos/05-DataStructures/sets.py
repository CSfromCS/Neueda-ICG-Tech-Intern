set1 = {"dog", "ant", "bat", "cat", "dog"}
set2 = set()
set3 = set(("dog", "ant", "bat", "cat", "dog"))
set4 = set("abracadabra")
set5 = {c.upper() for c in "abracadabra"}

print("set1 has %d items: %s" % (len(set1), set1))
print("set2 has %d items: %s" % (len(set2), set2))
print("set3 has %d items: %s" % (len(set3), set3))
print("set4 has %d items: %s" % (len(set4), set4))
print("set5 has %d items: %s" % (len(set5), set5))
      

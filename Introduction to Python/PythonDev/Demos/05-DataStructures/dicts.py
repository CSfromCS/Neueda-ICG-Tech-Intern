dict1 = {"us": "+1", "nl": "+31", "no": "+47"}
dict2 = dict()
dict3 = dict({"us": "+1", "nl": "+31", "no": "+47"})
dict4 = dict(us="+1", nl="+31", no="+47")
dict5 = dict(zip(["us", "nl", "no"], ["+1", "+31", "+47"]))

print("dict1 has %d items: %s" % (len(dict1), dict1))
print("dict2 has %d items: %s" % (len(dict2), dict2))
print("dict3 has %d items: %s" % (len(dict3), dict3))
print("dict4 has %d items: %s" % (len(dict4), dict4))
print("dict5 has %d items: %s" % (len(dict5), dict5))
      

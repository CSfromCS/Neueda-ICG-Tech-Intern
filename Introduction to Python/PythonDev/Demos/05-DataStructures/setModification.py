s1 = {"GB", "US", "SG"}
s2 = {"GB", "US", "AU"}
s3 = {"GB", "US", "F", "CA"}
s4 = {"GB", "US", "I", "D"}
s5 = {"GB", "US", "P", "N"}

s1.add("HK")
s1.remove("US")
s1.discard("D")
print("%s" % s1)       # {'SG', 'HK', 'GB'}

print("%s" % s1.pop()) # SG
print("%s" % s1)       # {'HK', 'GB'}

s1.update(s2,s3)
s1 |= s4 | s5
print("%s" % s1)       # {'D', 'AU', 'US', 'I', 'F', 'P', 'N', 'GB', 'CA', 'HK'}

s1.intersection_update(s2,s3)
s1 &= s4 & s5
print("%s" % s1)       # {'GB', 'US'}

s1.difference_update({"AA", "BB"},{"CC", "GB"})
s1 -= {"DD", "EE"} | {"FF", "GG"}
print("%s" % s1)       # {'US'}

s1.symmetric_difference_update(s2)
s1 ^= s2
print("%s" % s1)       # {'US'}

s1copy = s1.copy()
s1.clear()
print("%s" % s1copy)   # {'US'}
print("%s" % s1)       # set()

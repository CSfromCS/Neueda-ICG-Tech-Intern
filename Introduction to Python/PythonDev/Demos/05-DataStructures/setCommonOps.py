s1 = {"GB", "US", "SG"}
s2 = {"GB", "US", "AU"}
s3 = {"F", "BE", "CA"}

print("%s" % ("GB" in s1))         # True
print("%s" % ("GB" not in s1))     # False

print("%s" % (s1.isdisjoint(s2)))  # False
print("%s" % (s1.isdisjoint(s3)))  # True

print("%s" % (s1.issubset(s2)))    # False
print("%s" % (s1 <= s2))           # False
print("%s" % (s1 < s2))            # False

print("%s" % (s1.issuperset(s2)))  # False
print("%s" % (s1 >= s2))           # False
print("%s" % (s1 > s2))            # False

print("%s" % (s1.union(s2, s3)))   # {'GB', 'US', 'BE', 'F', 'CA', 'AU', 'SG'}
print("%s" % (s1 | s2 | s3))       # {'GB', 'US', 'BE', 'F', 'CA', 'AU', 'SG'}

print("%s" % (s1.difference(s2, s3))) # {'SG'}
print("%s" % (s1 - s2 - s3))          # {'SG'}

print("%s" % (s1.symmetric_difference(s2))) # {'AU', 'SG'}
print("%s" % (s1 ^ s2))                     # {'AU', 'SG'}

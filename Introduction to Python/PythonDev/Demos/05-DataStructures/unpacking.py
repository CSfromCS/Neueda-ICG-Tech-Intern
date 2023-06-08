euro = ["GB", "ES", "NL", "F"]

# Manually getting items.
a, b, c, d = euro[0], euro[1], euro[2], euro[3]
print("%s %s %s %s" % (a, b, c, d))    # GB ES NL F

# Unpacking.
e, f, g, h = euro
print("%s %s %s %s" % (e, f, g, h))    # GB ES NL F

# Catch-all unpacking.
i, j, *k = euro
print("%s %s %s" % (i, j, k))          # GB ES NL F



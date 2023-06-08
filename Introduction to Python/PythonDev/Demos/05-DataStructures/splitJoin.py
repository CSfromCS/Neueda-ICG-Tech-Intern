str = "and we were singing, hymns and arias, land of my fathers, ar hyd yr nos"

words = str.split(", ")

lines = "...\n".join(words)

print("%s" % lines)
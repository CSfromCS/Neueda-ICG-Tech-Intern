euro = ["GB", "ES", "NL", "F", "D", "I", "P"]

print("%s" % (euro[1]))                 # ES
print("%s" % (euro[1:5]))               # ['ES', 'NL', 'F', 'D']
print("%s" % (euro[1:5:2]))             # ['ES', 'F']
print("%s" % (euro[3:]))                # ['F', 'D', 'I', 'P']
print("%s" % (euro[:-3]))               # ['GB', 'ES', 'NL', 'F']

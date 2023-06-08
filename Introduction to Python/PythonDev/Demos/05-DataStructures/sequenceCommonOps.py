euro = ["GB", "ES", "NL", "F", "D", "I", "P"]
asia = ["SG", "JP"]

try:
	print("%s" % "F" in euro)               # True
	print("%s" % "F" not in euro)           # False
	print("%s" % (euro + asia))             # ['GB', 'ES', 'NL', 'F', 'D', 'I', 'P', 'SG', 'JP']
	print("%s" % (asia * 2))                # ['SG', 'JP', 'SG', 'JP']
	print("%s" % (2 * asia))                # ['SG', 'JP', 'SG', 'JP']
	print("%d" % len(euro))                 # 7
	print("%s" % min(euro))                 # D
	print("%s" % max(euro))                 # P
	print("%d" % euro.index("NL"))          # 2
#	print("%d" % euro.index("ZZ"))          # This will cause a ValueError.
	print("%d" % euro.index("NL", 1))       # 2
	print("%d" % euro.index("NL", 1, 4))    # 2
	print("%d" % euro.count("ES"))          # 1

except ValueError as e:
	print("Error occurred: %s" % e)
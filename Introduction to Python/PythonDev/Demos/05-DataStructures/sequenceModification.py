euro = ["GB", "ES", "NL", "F"]

euro[0] = "CY"
euro[1:3] = ["US", "AU", "AT"]
euro.append("SW")
euro.extend(["YU", "ZR"])
euro.insert(1, "NI")
print("%s" % euro)      # ['CY', 'NI', 'US', 'AU', 'AT', 'F', 'SW', 'YU', 'ZR']

euro.pop()
euro.pop(1)
del euro[2:4]
print("%s" % euro)      # ['CY', 'US', 'F', 'SW', 'YU']

euro.remove("US")
euro.reverse()
print("%s" % euro)      # ['YU', 'SW', 'F', 'CY']

eurocopy = euro.copy()
euro.clear()
print("%s" % eurocopy)  # ['YU', 'SW', 'F', 'CY']
print("%s" % euro)      # []

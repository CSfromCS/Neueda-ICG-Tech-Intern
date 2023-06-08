def personNameLength(p) :
    return len(p)
    
names = ["Andy", "Jayne", "Em", "Tom"]

sortedNamesAlphabetically = sorted(names)
print(sortedNamesAlphabetically)

sortedNamesByLength = sorted(names, key=personNameLength)
print(sortedNamesByLength)

sortedNamesByLengthDescending = sorted(names, key=personNameLength, reverse=True)
print(sortedNamesByLengthDescending)

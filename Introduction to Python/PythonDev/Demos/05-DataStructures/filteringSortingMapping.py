def startsWithB(element):
    if len(element) and element[0] == 'B':
        return True
    else:
        return False
		
def topAndTail(element):
    return "***" + element + "***"

names = ["Zak", "Tim", "Ben", "Joe", "Kim", "Bud", "Ted", "Baz"]
bnames = list(filter(startsWithB, names))
print(bnames)

sortedBnames = sorted(bnames)
print(sortedBnames)

mappedSortedBnames = list(map(topAndTail, sortedBnames))
print(mappedSortedBnames)

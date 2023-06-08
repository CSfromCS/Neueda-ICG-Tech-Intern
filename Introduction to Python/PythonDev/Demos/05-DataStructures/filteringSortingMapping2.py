def myfilter(f, items) : 
    resultItems = []
    for item in items:
       if f(item):
          resultItems.append(item)
    return resultItems          

def myfilter2(f, items) : 
    return [item for item in items if f(item)]

myfilter2AsLambda = lambda f, items : \
    [item for item in items if f(item)]
    
    
def topAndTail(element):
    return "***" + element + "***"

names = ["Zak", "Tim", "Ben", "Joe", "Kim", "Bud", "Ted", "Baz"]
bnames = list(myfilter2AsLambda(lambda e: len(e) and e[0] == 'B', names))
print(bnames)

sortedBnames = sorted(bnames)
print(sortedBnames)

mappedSortedBnames = list(map(topAndTail, sortedBnames))
print(mappedSortedBnames)

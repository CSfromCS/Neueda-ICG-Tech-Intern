def display_range(msg, r):
    print("\n" + msg)
    for i in r:
        print(i)
        
range1 = range(5)
range2 = range(5,10)
range3 = range(5,10,2)

display_range("range1", range1)
display_range("range2", range2)
display_range("range3", range3)

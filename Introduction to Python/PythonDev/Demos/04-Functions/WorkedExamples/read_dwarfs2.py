with open('dwarfs.txt') as fh:
    i = 1
    for line in fh:
        print("[%d] %s" % (i, line))
        i += 1
		
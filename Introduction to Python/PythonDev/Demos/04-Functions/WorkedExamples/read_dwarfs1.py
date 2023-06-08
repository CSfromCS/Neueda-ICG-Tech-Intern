fh = open('dwarfs.txt', 'r')

i = 1
for line in fh:
    print("[%d] %s" % (i, line))
    i += 1
	
fh.close()

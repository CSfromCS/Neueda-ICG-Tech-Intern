ftemps = range(0, 50, 5)
ctemps = { int((f-32)*5/9) for f in ftemps }

print("ctemps:  %s" % ctemps)

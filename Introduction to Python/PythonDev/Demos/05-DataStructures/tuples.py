tuple1 = ()
tuple2 = "Norway",     # or:  tuple2 = ("Norway",)
tuple3 = 3, 19, 2      # or:  tuple3 = (3, 19, 2)
tuple4 = tuple()
tuple5 = tuple(tuple3)

print("tuple1 has %d items: %s" % (len(tuple1), tuple1))
print("tuple2 has %d items: %s" % (len(tuple2), tuple2))
print("tuple3 has %d items: %s" % (len(tuple3), tuple3))
print("tuple4 has %d items: %s" % (len(tuple4), tuple4))
print("tuple5 has %d items: %s" % (len(tuple5), tuple5))
      

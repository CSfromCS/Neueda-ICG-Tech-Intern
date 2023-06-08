i1 = 12345
i2 = 1234567890123456789
i3 = int("123", 8)
print("%d %d %d" % (i1, i2, i3))

f1 = 1.23
f2 = 4.56e-34
f3 = 7.89e+34
f4 = float("123.45")
print("%g %g %g %g" % (f1, f2, f3, f4))

c1 = 1 + 2j
c2 = 3 - 4j
c3 = 5j
c4 = complex("6+7j")
print("%g + %gi" % (c1.real, c1.imag))
print("%g + %gi" % (c2.real, c2.imag))
print("%g + %gi" % (c3.real, c3.imag))
print("%g + %gi" % (c4.real, c4.imag))

 

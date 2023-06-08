import math

print(dir(math))

print("pi is %f" % math.pi)
print("360 degrees in radians is %g" % math.radians(360))
print("2 * pi radians in degrees is %g" % math.degrees(2 * math.pi))

print("sin(90 degrees) is %.4f" % math.sin(math.pi / 2))
print("cos(90 degrees) is %.4f" % math.cos(math.pi / 2))
print("acos(0) is %g degrees" % math.degrees(math.acos(0)))

print("hypoteneuse of right-angled triangle (sides 3, 4) is %g" % math.hypot(3, 4))
print("5 factorial is %g" % math.factorial(5))


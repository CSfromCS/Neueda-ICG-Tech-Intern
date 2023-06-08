print("Numbers from 1-5 inclusive")
i = 1
while i <= 5:
  print(i)
  i = i + 1
  
print("First 5 odd numbers")
i = 1
num = 1
while i <= 5:
  print(num)
  i = i + 1
  num = num + 2


print("5 strings from the keyboard, in uppercase")
i = 1
while i <= 5:
  str = input("Please enter string %d: " % i)
  print(str.upper())
  i = i + 1

magicnumber = int(input("What is the magic number? "))

print("This loop terminates if it hits the magic number")
for i in range(1, 21):
  if i == magicnumber:
    break
  print(i)
print("End")

print("\nThis loop skips the magic number")
for i in range(1, 21):
  if i == magicnumber:
    continue
  print(i)
print("End")


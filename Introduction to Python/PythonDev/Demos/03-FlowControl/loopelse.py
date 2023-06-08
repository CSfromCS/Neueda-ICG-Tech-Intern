magicnumber = int(input("What is the magic number? "))

print("This loop does some processing if it doesn't detect the magic number")
for i in range(1, 21):
  if i == magicnumber:
    break
  print(i)
else:
  print("The magic number %d was not detected" % magicnumber)

print("End")

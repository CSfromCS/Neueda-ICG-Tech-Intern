while True:
  exammark = int(input("Enter a valid exam mark: "))
  if exammark >= 0 and exammark <= 100:
    break
	
print("Your exam mark is %d" % exammark)

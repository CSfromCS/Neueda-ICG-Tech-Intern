number = int(input("Enter a football jersey number [1 to 11]: "))

if number == 1:
  print("Goalie")

elif number in range(2, 6):
  print("Defender")

elif number in range(6, 10):
  print("Midfielder")

else:
  print("Striker")
  

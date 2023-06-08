age = int(input("Please enter your age: "))
gender = input("Please enter your gender [M/F]: ").lower()

if age < 18:

  if gender == "m":
    print("Boy")
  else:
    print("Girl")
  
else: 

  if age >= 100: 
    print("Centurion")
   
  if gender == "m": 
    print("Man")
  else: 
    print("Woman")
  
print("The End")

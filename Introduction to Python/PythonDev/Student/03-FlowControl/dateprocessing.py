# Ask the user for a day, month, and year.
day   = int(input("Enter a day (1-31): "))
month = int(input("Enter a month (1-12): "))
year  = int(input("Enter a year (0 to 2099): "))

# Add the rest of your code here.

valid = True
# validate year
if(year < 0 or year > 2099):
    valid = False
    

# is leap?
leap_year = False
if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
    print(f"{year} is a leap year!")
    leap_year = True
else:
    print(f"{year} is NOT a leap year.")
    leap_year = False
    
    
# validate month
if(month < 1 or month > 12):
    valid = False

    
# validate day
nonleap = [31,28,31,30,31,30,31,31,30,31,30,31]
leap = [31,29,31,30,31,30,31,31,30,31,30,31]

if(leap_year):
    if((day < 0) or (day > leap[month-1])):
        valid = False
else:
    if((day < 0) or (day > nonleap[month-1])):
        valid = False


    
if(valid):
    print(f"{day}/{month}/{year} is a valid date!")
else:
    print(f"{day}/{month}/{year} is NOT a valid date.")
    
    
months = ["January","February","March","April","May", "June", "July", "August", "September", "October", "November","December"]
    
print("\n-----------\n")
print(f"All days in {months[month-1]} {year}")

if(leap_year):
    for i in range(1,leap[month-1]+1):
        if(i%10 == 1):
            sfx = "st"
        elif(i%10 == 2):
            sfx = "nd"
        elif(i%10 == 3):
            sfx = "rd"
        else:
            sfx = "th"
        print(f"{i}{sfx} {months[month-1]} {year}")
else:
    for i in range(1,nonleap[month-1]+1):
        if(i%10 == 1):
            sfx = "st"
        elif(i%10 == 2):
            sfx = "nd"
        elif(i%10 == 3):
            sfx = "rd"
        else:
            sfx = "th"
        print(f"{i}{sfx} {months[month-1]} {year}")
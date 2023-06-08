# Ask the user for a day, month, and year.
day   = int(input("Enter a day (1-31): "))
month = int(input("Enter a month (1-12): "))
year  = int(input("Enter a year (0 to 2099): "))

# Determine if it's a leapyear.
def isLeapYear(year):
    isLeapYear = ((year % 4 == 0) and not (year %
                  100 == 0)) or (year % 400 == 0)
    return isLeapYear

# Determine if it's a valid date.


def getDaysInMonth(month, year):
    if month == 2:
        daysInMonth = 29 if isLeapYear else 28
    elif month in (4, 6, 9, 11):
        daysInMonth = 30
    else:
        daysInMonth = 31
    return daysInMonth


def isValidDate(day, month, year):
    daysInMonth = getDaysInMonth(month, year)
    isvalid = day >= 1 and day <= daysInMonth and \
        month >= 1 and month <= 12 and \
        year >= 0 and year <= 2099
    return isvalid

# print("%02d/%02d/%04d valid? %s" % (day, month, year, isvalid))

# Determine the name of the month.


def getMonthName(month):
    if month == 1:
        monthName = "January"
    elif month == 2:
        monthName = "February"
    elif month == 3:
        monthName = "March"
    elif month == 4:
        monthName = "April"
    elif month == 5:
        monthName = "May"
    elif month == 6:
        monthName = "June"
    elif month == 7:
        monthName = "July"
    elif month == 8:
        monthName = "August"
    elif month == 9:
        monthName = "September"
    elif month == 10:
        monthName = "October"
    elif month == 11:
        monthName = "November"
    elif month == 12:
        monthName = "December"
    else:
        monthName = "Not Known"     # Should never happen

    return monthName


def getDaySuffix(day):
    if day in (1, 21, 31):
        suffix = "st"
    elif day in (2, 22):
        suffix = "nd"
    elif day in (3, 23):
        suffix = "rd"
    else:
        suffix = "th"
    return suffix

# Display all the dates in the month.


def displayAllDatesInMonth(month, year, verbose=False):
    daysInMonth = getDaysInMonth(month, year)

    monthName = getMonthName(month)

    for day in range(1, daysInMonth+1):
        suffix = getDaySuffix(day)
        if (verbose):
            print("%d%s %s %d" % (day, suffix, monthName, year))
        else:
            print(f"{day:02.0f}/{month:02.0f}/{year}")


# print("Dates in %s, %d" % (monthName, year))
displayAllDatesInMonth(month, year)

# for day in range(1, daysInMonth+1):
#     if day in (1, 21, 31):
#         suffix = "st"
#     elif day in (2, 22):
#         suffix = "nd"
#     elif day in (3, 23):
#         suffix = "rd"
#     else:
#         suffix = "th"

#     print("%d%s %s %d" % (day , suffix, monthName, year))

def displaySpecialDatesInMonth(month, year, *args, verbose=False):
    daysInMonth = getDaysInMonth(month, year)

    monthName = getMonthName(month)

    for day in args:
        suffix = getDaySuffix(day)
        if (verbose):
            print("%d%s %s %d" % (day, suffix, monthName, year))
        else:
            print(f"{day:02.0f}/{month:02.0f}/{year}")


displaySpecialDatesInMonth(12, year, 3, 25, 26, 31, verbose=True)

displaySpecialDatesInMonth(12, year, 3, 25, 26, 31)

month = int(input("Enter a month number [1-12]: "))

is_summer = month >=6 and month <= 8
is_winter = month == 12 or month == 1 or month == 2
is_transition_season = not(is_winter or is_summer)

print("%s %s %s" % (is_summer, is_winter, is_transition_season))

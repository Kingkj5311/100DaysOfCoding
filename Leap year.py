# Which year do you want to check?
year = int(input())
x=0
y=0
z=0
# Is /by 400 (can be a leap year)
if year % 400 == 0:
    # Is /by 400 z = 1 to let the rest of the code know
    z=1
    if year % 100 != 0 and z == 1:
        # y = 1 to let the rest of the code know it is /by 400 (is a leap year) and isn't /by 100 (is a leap year)
        y=1
        # Need to check if it is also /by 4 (is a leap year) because it is /by 400 (is a leap year) and isn't /by 100 (is a leap year)
        if year % 4 == 0 and y == 1:
            print("Leap year")
        else:
            print("Not leap year")
else:
    # Isn't /by 400 x = 1 to let the rest of the code know
    x=1
    # All years divisble by 100 are not leap years except the ones /by 400
    # If it is divisible 100 it is not unless it is /by 400 = leap year
    # First, all years not /by 100 are leap years (then) + years not /by 400 = not a leap year, unless /by 4 = leap year
    if year % 100 != 0 and x == 1:
        y=1
        # Check if the year is /by 4 and told [y=1] the year is not /by 100 (is a leap year) and year is not /by 400 (can be a leap year)
        # Except if it is divisble by 4 therefore it is a leap year
        # Need to check if /by 4 because it is not /by 100 (is a leap year) and not /by 400 (can be a leap year)
        if year % 4 == 0 and y == 1: 
            print("Leap year")
        else:
            print("Not leap year")
    else:
        # Automatically not a leap year because it is /by 100 (not a leap year) and not /by 400 (not a leap year)
        # No need to check if /by 4 (already failed, is /by 100 (not a leap year) and isn't /by 400 (not a leap year)
        print("Not leap year")
        
# =========================================================================================================
# Clean uncommented code
"""
year = int(input())
x=0
y=0
z=0
if year % 400 == 0:
    z=1
    if year % 100 != 0 and z == 1:
        y=1
        if year % 4 == 0 and y == 1:
            print("Leap year")
        else:
            print("Not leap year")
else:
    x=1
    if year % 100 != 0 and x == 1:
        y=1
        if year % 4 == 0 and y == 1: 
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Not leap year")
"""
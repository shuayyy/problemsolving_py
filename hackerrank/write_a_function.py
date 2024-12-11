def is_leap(year):
    if year % 400 == 0:
        leap = True
    # Not a leap year if divisible by 100 but not by 400
    elif year % 100 == 0:
        leap = False
    # Leap year if divisible by 4 but not by 100
    elif year % 4 == 0:
        leap = True
    # Not a leap year otherwise
    else:
        leap = False

    return leap


year = int(input())
print(is_leap(year))
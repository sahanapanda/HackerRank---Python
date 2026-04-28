# Day 2 - Leap Year
# Problem: Check whether a given year is a leap year

def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

year = int(input())
print(is_leap(year))

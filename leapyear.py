#program using if-else to check whether a year is a leap year

"""
Rule for Leap Year
A year is a leap year if:
It is divisible by 4, and Not divisible by 100,
OR divisible by 400.
"""
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
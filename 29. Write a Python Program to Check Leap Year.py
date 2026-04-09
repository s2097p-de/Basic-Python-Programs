# Write a Python Program to Check Leap Year.

"""
Given a year, determine whether it is a leap year. For example, 2000 is a leap year, while 2003 is not.

A year is a leap year if it satisfies the following conditions:

It is divisible by 4, and
Not divisible by 100, unless
It is also divisible by 400

"""

# 1st method:
y = int(input("Enter Year You want to Check.. "))
leap = lambda x: (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0)

if leap(y):
    print("Leap year")
else:
    print("Not a leap year")


# 2nd method 
import calendar 
y = int(input("Enter Year You want to Check.. "))

if calendar.isleap(y):
    print("Leap year")  
else:
    print("Not a leap year")



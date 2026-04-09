#Write a Python program to display calendar.
import calendar as cal

year = int(input("Enter the year : "))
month = int(input("Enter the month : "))


calender = cal.month(year,month)
print(calender)
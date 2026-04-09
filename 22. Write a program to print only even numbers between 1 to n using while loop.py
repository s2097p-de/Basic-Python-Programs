# 22. Write a program to print only even numbers between 1 to n using while loop.py
"""
Short Description:

If user enters 10 for the value of n than only even numbers between 1 to 10 should be printed.
"""
n = int(input("Enter the Number : "))
i= int(input("Enter i : "))

while i<=n:
    if i % 2 ==0:
        print(f"Number is even {i}")
        
    i+=1
    
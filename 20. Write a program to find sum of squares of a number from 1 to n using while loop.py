# 20. Write a program to find sum of squares of a number from 1 to n using while loop.

n = int(input("Enter the number :  "))
i =  1
sum = 0

while i<= n:
    sum += i**2
    i += 1
    print(f"sum is {sum}")
# 21. Write a program to find sum of cubes of a number from 1 to n using while loop.

n = int(input("Enter the Number: "))
i=1
sum=0

while i<=n:
    sum += i **3
    i+=1
    print(f"SUM is {sum}")
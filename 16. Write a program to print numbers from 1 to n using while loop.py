# 16. Write a program to print numbers from 1 to n using while loop.

i = int(input("Enter the initization number: "))
n = int(input("Enter Number upto which you want to print: "))
if n > 0:
    while i <= n:
        print(i, end=" ")
        i+=1
# the final value of i is 6 but it will not print because the condition becomes false when i = 6.
else:
    print('You entered negative number that\'s why program does\'nt print numbers')
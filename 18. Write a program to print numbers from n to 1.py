# 18. Write a program to print numbers from n to 1.

n = int(input('Enter initialization number: '))
i = int(input('Enter a number down till which you want to print: '))
while n >= i:
    print(n, end=" ")
    n -= 1


    
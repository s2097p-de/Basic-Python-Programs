# 23. Write a program to find sum of even numbers from 1 to n using while loop.

n = int(input("Enter the number : "))
i = 1
sum=0

while i <= n:
    if i % 2==0:
        sum += i
        print(f"sum is {sum}")
    i+=1
print('The Sum of Even numbers between 1 and',n,'is =', sum)    
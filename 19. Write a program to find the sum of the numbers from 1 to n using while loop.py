# 19. Write a program to find the sum of the numbers from 1 to n using while loop.

n = int(input('Enter Number upto which you want to sum: '))
i = 1
sum = 0 # Here we set sum = 0 because zero is the number that does'nt effect the sum of two numbers like
# if we add 1 + 0 then answer is 1 so it means 0 does'nt effect the sum.
while i <= n:
    sum += i
    i += 1
print('The sum =', sum)
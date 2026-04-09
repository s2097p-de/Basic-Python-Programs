# 24. Write a program to find sum of first n even numbers.

"""
Description:

sum of n even numbers means if n = 4 then it can add 2 + 4 + 6 + 8 and if n = 5 then 10 also added.
n = 4 means first 4 even numbers.
if n = 4 then the sum = 20.
Here n will be decided by the user.

n = 3 then 2 + 4 + 6 = 12
"""
n = int(input('How many even numbers you want to add: '))
i = 1 
sum = 0
count = 0 
while count < n: 
    if i % 2 == 0:
        sum += i
        count += 1
    i += 1
print('The sum of first', count, 'even numbers =', sum)
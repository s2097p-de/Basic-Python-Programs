"""
Start with a list of 10 numbers. Iterate through them and sort them into two separate lists: one for even numbers 
and one for odd numbers.

Given Input: numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]

Expected Output:

Even numbers: [12, 34, 10, 8, 2]
Odd numbers: [7, 21, 5, 3, 19]
"""
numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
odd=[]
even=[]

for num in numbers:
    if num %2 ==0:
        even.append(num)
    else:
        odd.append(num)

print(f"Even list is {even}")
print(f"ODD list is {odd}")
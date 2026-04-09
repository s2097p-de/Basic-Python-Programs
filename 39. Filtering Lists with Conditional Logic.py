# Iterate through a given list of numbers and print only those numbers which are divisible by 5.

"""
This exercise teaches the use of the modulo operator (%) and loop filtering. 
In data processing, you often need to sift through large datasets to extract subsets that meet mathematical criteria.

Given Input: num_list = [10, 20, 33, 46, 55]

Expected Output:

Divisible by 5:
10, 20, 55
"""

num_list = [10, 20, 33, 46, 55]

print("Given list is", num_list)
print("Divisible by 5:")
for num in num_list:
    if num %5 == 0:
        print(num)
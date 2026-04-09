### Write a program to swap values of two numbers

# Take User Input
a = float (input("Enter the value 1 : "))
b = float (input("Enter the value 2 : "))

print(f" the value of a before swapping {a}")
print(f" the value of b before swapping {b}")

"""
## Method :1
temp = 0

## swap value 
temp = a
a = b
b = temp

print(f"the value a after swapping {a}")
print(f"the value b after swapping {b}")
"""
## Method : 2 
a,b = b,a

print(f"the value a after swapping {a}")
print(f"the value b after swapping {b}")
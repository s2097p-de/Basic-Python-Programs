### 7. Calculation program.py

"""Write a program to calculate:
a. Area of rectangle.    b. Perimeter of rectangle.    c. Area of square.
d. Perimeter of square.  e. Area of circle.            f. Circumference of Circle. 
"""

import math 

## a. Area of rectangle.

height = float(input("Enter the Triangle Height in mm :   "))
base = float(input("Enter The Triangle Base in mm :   ") )

area = 0.5 * height * base 
print(f"Area of the Triangle is {area} mm**2 ")

print("--------------------------------------------------------------------------")

##  b. Perimeter of rectangle. 

length = float (input ("Enter the length of Rectangale in mm :  "))
width = float (input ("Enter the Width of a Rectangle  in mm :  "))

perimeter = 2 * (length + width)

print(f"Perimeter of rectangle is {perimeter} mm")

print("--------------------------------------------------------------------------")

# c. Area of square.

arm = float (input("Arm of a square in mm :  "))

area = arm ** 2  #area = arm * arm
print(f"Area of Square is {area} mm**2")

print("--------------------------------------------------------------------------")

## d. Perimeter of square.

arm = float (input("Arm of a square in mm :  "))

perimetersq = 4 * arm 
print(f"Perimeter of Square is {perimetersq} mm")

print("--------------------------------------------------------------------------")
# e. Area of circle.

r = float (input("Enter the radius of the circle mm :  "))

area = math.pi *(r*r)
print(f"Area of circle is {area} mm**2")

print("--------------------------------------------------------------------------")

##f. Circumference of Circle.C=2πr

r = float (input("Enter the radius of the Circle in mm :  "))

c = 2*math.pi*r

print(f"The Circumference of Circle is {c} mm")


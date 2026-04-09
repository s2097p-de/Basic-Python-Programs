# Write a Python program to solve quadratic equation.
#The standard form of a quadratic equation is:
#𝑎𝑥2 + 𝑏𝑥 + 𝑐 = 0
#where
# a, b and c are real numbers and
# 𝑎 ≠ 0
# The solutions of this quadratic equation is given by:
# (−𝑏 ± (𝑏2 − 4𝑎𝑐)1/2)/(2𝑎)

import math

# insert coefficient..
a = float(input("Enter First Number : "))
b = float(input("Enter Second Number : "))
c = float(input("Enter Third Number : "))

#calculate discriminant
dis = (b**2)-4*a*c

# Check if the discriminant is positive, negative, or zero
if dis > 0:
# Two real and distinct roots
    root1 = (-b + math.sqrt(dis)) / (2*a)
    root2 = (-b - math.sqrt(dis)) / (2*a)
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")

elif dis == 0:
# One real root (repeated)
    root = -b / (2*a)
    print(f"Root: {root}")
else:
# Complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(dis)) / (2*a)
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")
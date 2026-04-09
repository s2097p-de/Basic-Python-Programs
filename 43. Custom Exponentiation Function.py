"""
Write a function called exponent(base, exp) that returns an integer value of the base raised to the power of the exponent.

Exercise Purpose: Learn about “Accumulator Patterns.” Although Python has a built-in power operator (**), making your own version
shows how repeated multiplication works and how functions return results to the main program.

Given Input: base = 2, exp = 5

Expected Output: 2 raises to the power of 5: 32
"""

def exponent(base , exp):
    num = exp
    result = 1
    # Repeat multiplication 'exp' times
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is:", result)


exponent(2,5)
"""
Question: Write a program to accept electricity unit consumption and calculate total price at the rate of
 5 rs unit. Give a discount of 10% on all over bill.
"""

"""
Description:

5 rupee per unit.
if user enters 100 units then it means 100*5 = 500(total price), it is the price that you have to
pay means 1000 Rs of elctricity is used.
"""

# take user input 
unit = float (input("Enter electricity bill consumption (in unit):  "))

rate = 5  # 5 rupee per unit.

total_price = unit * rate

print(f"Total Bill Price {total_price} Rs ")

# Give a discount of 10% on all over bill.
discount_price = total_price * 0.90

print(f"After discount of 10% on all over bill is {discount_price}")
"""
 Calculate income tax for a given income based on these rules:

First rs.10,000: 0% tax
Next rs.10,000: 10% tax
Remaining income: 20% tax
Exercise Purpose: This exercise introduces “Tax Brackets” logic, a classic example of complex conditional branching. It shows how to calculate values cumulatively instead of applying a single percentage to the entire amount.

Given Input: income = 45000

Expected Output: Total income tax to pay is 9000
"""
# Take user input
income = int(input("Enter your income : "))

# checking condition
if income <= 10000:
    print("not tax payble")
elif income>10000 and income<= 20000:
    tax_pay = income *(10/100)
    print(f"tax pay rs {tax_pay}")
elif income > 20000:
    tax_pay = income *(20/100) 
    print(f"you pay tax rs {tax_pay}")


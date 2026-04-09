"""
Write a program to accept total sales amount and find the profit amount @ 5%.

Description:

lets say total sales is 60 k so we have to find profit which is 5% of the total sales.
if a person sales 60 k a day then it means 5 percent of profit is 60,000 * 5/100 = 30,00.
so 30,00 is the profit he gains if he sales 60,000 a day.
"""

totalSalesperDay = int(input('Enter total sales per day: '))

proFIT = int(input('Enter a profit percentage which you want from total sales per day: '))

profitAmount = totalSalesperDay * (proFIT / 100)

print('Total profit if the total sales per day is', totalSalesperDay, 'is equal to', profitAmount)

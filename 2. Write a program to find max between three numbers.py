## 2. Write a program to find max between three numbers.

# Taking User Input 

num1 = int(input("Enter Number 1 =  "))
num2 = int(input("Enter Number 2 =  "))
num3 = int(input("Enter Number 3 =  "))

# Checking condition
if num1 > num2 and num1 > num3 :
    print(f"{num1} is the max num ")

elif num2 > num3 and num2 > num1 :
    print(f"{num2} is the max num ")

else:
    print(f"{num3} is the max num ")
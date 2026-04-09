## 5. Write a program to find min between two numbers.py

### Taking User input.
num1 = int(input("Enter the number 1 : "))
num2 = int(input("enter the number 2 : "))

### Checking condition.using lambda function
if num1 < num2 :
    print(f"{num1} is the min number.")
else:
    print(f"{num2} is the min number.")
## 4. Write a program to find min between 3 numbers.

### taking user input.
no1 = float(input("Enter the first number : "))
no2 = float(input("Enter the second number : "))
no3 = float(input("Enter the third number : "))

### checking condition.
if no1 < no2 and no1 < no3 :
    print(f"{no1} is the lowest number.")
elif no2 < no1 and no2 < no3 :
    print(f"{no2} is the lowest number.")
else:
    print(f"{no3} is the lowest number.")
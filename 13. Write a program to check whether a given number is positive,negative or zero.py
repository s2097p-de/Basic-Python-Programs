# 13. Write a program to check whether a given number is positive,negative or zero.

num = float(input("Enter number : "))

# condition
if num > 0 :
    print(f"You enter {num} and it is a positive number.")
elif num == 0 :
    print(f"You enter {num} and it is a zero number.")
else :
    print(f"You enter {num} and it is a negative number.")
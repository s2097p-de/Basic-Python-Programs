# 1. Write a program to check whether an age is able to voting or not.

# taking user input 
age = int (input("Please Enter Your Age : "))


# checking the condition

if age >= 18 :
    print(f"Your Age Is {age}.\n You Are Eligible For Voting.")

else:
    print(f"Your Age Is {age}.\n You Are Not Eligible For Voting.")
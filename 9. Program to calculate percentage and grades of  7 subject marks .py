"""
Write a program to accept marks of 7 subjects and find total marks and percentage assumimg full marks as
100 in each subject.
"""

sub_1 = float (input ("Enter Sub_1 number is "))
sub_2 = float (input ("Enter Sub_2 number is "))
sub_3 = float (input ("Enter Sub_3 number is "))
sub_4 = float (input ("Enter Sub_4 number is "))
sub_5 = float (input ("Enter Sub_5 number is "))
sub_6 = float (input ("Enter Sub_6 number is "))
sub_7 = float (input ("Enter Sub_7 number is "))

gained_marks = sub_1 + sub_2 + sub_3 + sub_4 + sub_5 + sub_6 + sub_7
# full marks as 100 in each subject.
total_marks = 100 * 7

## percentage calculation
per_cal = (gained_marks / total_marks ) * 100

print(f"Total marks gained {gained_marks} and percentage of marks {per_cal} and total marks {total_marks}")

"""
You can also calculate grades with the help of percentage like if percentage >= 80 then display A-grade.
if percentage >= 60 then display B-grade. if percentage >= 40 then display C-grade and if
percentage < 40 then display D-grade or you can put this condition into else block as well.
"""
if per_cal >= 80 :
    print("A-grade")
elif per_cal < 80 and per_cal >= 60 :
    print(" B-grade")
elif per_cal < 60 and per_cal >= 40 :
    print ("C-grade")
elif per_cal < 40 :
    print("D-grade")
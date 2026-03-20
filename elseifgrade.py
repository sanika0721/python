"""
Write a python Program to Print Grades Based on Marks
 Marks >= 90 → Grade A
 Marks >= 80 and < 90 → Grade B
 Marks >= 70 and < 80 → Grade C
 Marks >= 60 and < 70 → Grade D
 Marks < 60 → Grade F
"""
marks = float(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")
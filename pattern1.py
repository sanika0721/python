"""
Write a Python program to print a right triangle star pattern
using a for loop .
*
* *
* * *
* * * *
* * * * *
"""

# Define the number of rows for the triangle
rows = 5
# Outer loop for the number of rows
for i in range(1, rows + 1):
    # Inner loop for the number of stars in each row
    for j in range(i):
        print("*", end=" ")
    # Move to the next line after each row is printed
    print()



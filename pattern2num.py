"""
Write a Python program to print a number triangle pattern using a for loop
1
1 2
1 2 3
1 2 3 4
"""
rows = 4

# Outer loop handles the vertical rows
for i in range(1, rows + 1):
    # Inner loop handles the numbers in each row
    for j in range(1, i + 1):
        print(j, end=" ")

    # Line break after each row
    print()
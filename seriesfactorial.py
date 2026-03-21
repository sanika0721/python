#Write a Python program to evaluate the following series
# 1!+2!+3!+4!.................+n!
#Sum of Factorial Series
n = int(input("Enter the value of n: "))
total_sum = 0
factorial = 1
for i in range(1, n + 1):
    # Update the current factorial (e.g., 3! = 2! * 3)
    factorial *= i
    # Add the current factorial to the running total
    total_sum += factorial
print(f"The sum of the series up to", n,"!", "is: ",total_sum)

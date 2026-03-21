#Write a Python program to evaluate the following series
# 1+2+3+4+………+n

n = int(input("Enter the value of n: "))
sum_series = 0

# The range starts at 1 and goes up to (but not including) n+1
for i in range(1, n + 1):
    sum_series += i

print("The sum of the series from 1 to", n, "is: ",sum_series)
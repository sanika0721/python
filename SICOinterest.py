"""
Develop a Python program to calculate both Simple Interest and Compound
Interest for a given Principal amount (P), Rate of Interest (R), and Time (T) and
display the Simple Interest (SI), Compound Interest (CI), and Total Amount (A).
"""
P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (in years): "))

# Simple Interest
SI = (P * R * T) / 100
# Compound Interest Amount
A = P * (1 + R/100) ** T
# Compound Interest
CI = A - P

print("Simple Interest =", SI)
print("Compound Interest =", CI)
print("Total Amount =", A)
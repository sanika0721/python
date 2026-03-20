"""
program should accept the number of electricity units and
calculate the total bill according to the slab rate.
Slab Rates
1 – 50 units → ₹2 per unit
51 – 100 units → ₹4 per unit
101 – 150 units → ₹6 per unit
Above 150 units → ₹8 per unit
"""

units = int(input("Enter the number of units consumed: "))
if units <= 50:
    amount = units * 2
elif units <= 100:
    amount = (50 * 2) + (units - 50) * 4
elif units <= 150:
    amount = (50 * 2) + (50 * 4) + (units - 100) * 6
else:
    amount = (50 * 2) + (50 * 4) + (50 * 6) + (units - 150) * 8

print("Total electricity bill = ₹", amount)
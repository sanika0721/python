balance = 5000

while True:
    amount = int(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance -= amount
        print("Withdrawal successful!")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance!")

    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() != 'yes':
        break
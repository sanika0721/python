#ATM withdrawl system

balance=70000

while balance>0:
    print("Welcom to the ATM")
    print("1.withdrawl")
    print("2.check balance")
    print("3.exit")
    choice=int(input("enter your choice:"))
    if choice==1:

        amount=int(input("enter the amount to  withdraw:"))
        if amount>balance:
             print ("insufficient balance")
        else:
            balance=balance-amount
            print("withdrawl successful")
            print("remaining balance in your account is :",balance)
        choose = input("do you want to continue??(yes/no):")
        if choose.lower() !='yes':
            break
    elif choice==2:
        print("your current balance is :",balance)
        choose = input("do you want to continue??(yes/no):")
        if choose.lower() !='yes':
            break
    elif choice==3:
        print("Thank you for using our ATM>_< *<>*,,HAVE A NICE DAY!!!>>> VISIT AGAIN<>_<>")
        break
    else:
        print("INVALID CHOICE!!!")


#condition to check whether a student can get a pass or not
x=int(input("Enter your Age"))
if x>=6 and x<=20 :
    print(" you are Eligible to get a Bus pass")
else:
    print(" you are not eligible to get a buss pass")

    #like wise using if else if conditions 

    age=int(input("Enter your age"))
    if age<5:
        print("Free ticket")
    elif age>5 and age<=10 :
        print("half ticket under the child consession will be awarded")
    elif age>=60:
        print(" you will get a senior citizen bus ticket with consession")
    else :
        print(" you nhave to pay full amount for the ticket")




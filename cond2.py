#library membership program
print("_____LIBRARYB MEMBERSHIP CREDENTIALS______")
amount=0
name=input("enter your name: ")
age=int(input("enter your age: "))
if age>3 and age<=18:
    print("CONGRATS!!!!!")
    print("You have got a student memebrship in our Library")
    amount=amount+age*10
    print("your membership amount is: ",amount)

elif age>18 and age<=60:
    print("CONGRATS!!!!!")
    print("You have got a adult memebrship in our Library")
    amount=amount=age*20 
    print("your membership amount is ",amount)
    
else:
    print("CONGRATS!!!!!")
    print("YOU HAVE GOT A SENIOR CITIZEN MEMBERSHIP IN OUR LIBRARY")
    amount=amount+age*15
    print("your membership amount is ", amount)
    
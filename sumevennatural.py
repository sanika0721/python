n=int(input("Enter the number"))
sumeven=0
sumodd=0
for i in range (1,n+1):
    if i%2==0:
        sumeven = sumeven+i
    else:
        sumodd = sumodd+i
print("Sum of first ", n, "even natural numbers = ", sumeven)
print("Sum of first ", n, "odd natural numbers = ", sumodd)
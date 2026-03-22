#Write a Python program to check whether a number is palindrome or not
num = int(input("Enter a number: "))
temp = num
reverse_num = 0
while temp > 0:
    # Get the last digit
    digit = temp % 10
    # Add it to the reversed number (shifting digits left)
    reverse_num = (reverse_num * 10) + digit
    # Remove the last digit from the original
    temp = temp // 10

if num == reverse_num:
    print(num, "is a Palindrome")
else:
    print(num, "is not a Palindrome")
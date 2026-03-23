#tuples
#creating tuple having only one element
t1=("shampoo",)
tu=("cucu","banana","carrot","cocunut")
print(tu[1])#accessing tuple elements
print(tu[-2])
print(tu[1:3])#slicing  of tuple elments

genders = ("male","female","other")
gender1=("m","f","o")
ctu=genders + gender1 # tuple concatenation
print(ctu)
print(type(genders[1:3]))
genders.count("male")




# Python Tuple Problem Solving - All in One File

# Sample tuple
t = (12, 45, 7, 23, 89, 34, 10, 21, 34, 45, 66, 77)

print("Original Tuple:", t)

# 1. Maximum and Minimum
print("\n1. Maximum and Minimum")
print("Maximum:", max(t))
print("Minimum:", min(t))

# 2. Count Even and Odd Numbers
print("\n2. Count Even and Odd Numbers")
even = 0
odd = 0
for i in t:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even count:", even)
print("Odd count:", odd)

# 3. Reverse a Tuple
print("\n3. Reverse Tuple")
print("Reversed Tuple:", t[::-1])

# 4. Sum of Elements
print("\n4. Sum of Elements")
print("Sum:", sum(t))

# 5. Remove Duplicates
print("\n5. Remove Duplicates")
unique = tuple(set(t))
print("Tuple without duplicates:", unique)

# 6. Frequency of Element (example: 45)
print("\n6. Frequency of Element")
element = 45
print(f"Frequency of {element}:", t.count(element))

# 7. Modify Tuple (Add element)
print("\n7. Modify Tuple")
lst = list(t)
lst.append(100)
modified_tuple = tuple(lst)
print("Updated Tuple:", modified_tuple)

# 8. Merge Two Tuples
print("\n8. Merge Two Tuples")
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print("Merged Tuple:", t1 + t2)

# 9. Find Index of an Element
print("\n9. Find Index")
print("Index of 23:", t.index(23))

# 10. Nested Tuple Access
print("\n10. Nested Tuple Access")
nested = ((1, 2), (3, 4), (5, 6))
print("Element:", nested[1][0])

# Bonus: Second Largest Element
print("\n Bonus: Second Largest Element")
unique_list = list(set(t))
unique_list.sort()
print("Second Largest:", unique_list[-2])
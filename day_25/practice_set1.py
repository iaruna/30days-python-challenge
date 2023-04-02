# Exercise 1: Reverse a list in Python
# Given:
# list1 = [100, 200, 300, 400, 500]
# Expected output:
# [500, 400, 300, 200, 100]
# Solution 1: list function reverse()
print("Solution-1")
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

# Solution 2: Using negative slicing

list1 = [100, 200, 300, 400, 500]
list1 = list1[::-1]
print(list1)

print()
# ----------------------------------------------------------------------------------------------
print("Solution-2")

# Exercise 2: Concatenate two lists index-wise
# Given:
# list1 = ["M", "na", "i", "Aa"]
# list2 = ["y", "me", "s", "shi"]
# Expected output:
# ['My', 'name', 'is', 'Aashi']
# Solution: Using the zip() function.

list1 = ["M", "na", "i", "Aa"]
list2 = ["y", "me", "s", "shi"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

print()
# ----------------------------------------------------------------------------------------------------
print("Solution-3")

# Exercise 3: Turn every item of a list into its square
# Given:
# numbers = [1, 2, 3, 4, 5, 6, 7]
# Expected output:
# [1, 4, 9, 16, 25, 36, 49]
# Solution 1: Using loop and list method
numbers = [1, 2, 3, 4, 5, 6, 7]
result = []
for i in numbers:
    result.append(i*i)
print(result)

# Solution 2: Use list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7]
result = [x * x for x in numbers]
print(result)

print()
# --------------------------------------------------------------------------------------------------------
print("Solution-4")

# Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected output:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# Solution:

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result = [x + y for x in list1 for y in list2]
print(result)

print()
# --------------------------------------------------------------------------------------------------------------------------
print("Solution-5")

# Exercise 5: Iterate both lists simultaneously
# Given
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# Expected output:
# 10 400
# 20 300
# 30 200
# 40 100

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, list2[::-1]):
    print(x, y)

print()
# ---------------------------------------------------------------------------------------------------------
print("Solution-6")

# Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# Expected output:
# ["Mike", "Emma", "Kelly", "Brad"]
# Solution: Using a filter() function to remove None type from the list

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
result = list(filter(None, list1))
print(result)

print()
# --------------------------------------------------------------------------------------------------------------------
print("Solution-7")

# Exercise 7: Add new item to list after a specified item
# Given:
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected output:
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
# Solution: Using the append() method

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# understand indexing
# list1[0] = 10
# list1[1] = 20
# list1[2] = [300, 400, [5000, 6000], 500]
# list1[2][2] = [5000, 6000]
# list1[2][2][1] = 6000
# solution

list1[2][2].append(7000)
print(list1)

print()
# ------------------------------------------------------------------------------
print("Solution-8")

# Exercise 8: Extend nested list by adding the sublist
# Given List:
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# # sub list to add
# sub_list = ["h", "i", "j"]
# Expected Output:
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

# understand indexing
# list1[2] = ['c', ['d', 'e', ['f', 'g'], 'k'], 'l']
# list1[2][1] = ['d', 'e', ['f', 'g'], 'k']
# list1[2][1][2] = ['f', 'g']

# solution
list1[2][1][2].extend(sub_list)
print(list1)

print()
# ---------------------------------------------------------------------------------------
print("Solution-9")

# Exercise 9: Replace list’s item with new value if found
# Given:
# list1 = [5, 10, 15, 20, 25, 50, 20]
# Expected output:
# [5, 10, 15, 200, 25, 50, 20]

list1 = [5, 10, 15, 20, 25, 50, 20]

# get the first occurrence index
index = list1.index(20)

# update item present at location
list1[index] = 200
print(list1)

print()
# -----------------------------------------------------------------------------
print("Solution-10")

# Exercise 10: Remove all occurrences of a specific item from a list.
# Given:
# list1 = [5, 20, 15, 20, 25, 50, 20]
# Expected output:
# [5, 15, 25, 50]

# Solution 1: Use the list comprehension

list1 = [5, 20, 15, 20, 25, 50, 20]
# list comprehension
# remove specific items and return a new list


def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]


res = remove_value(list1, 20)
print(res)
# Solution 2: while loop (slow solution)

list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)
print(list1)

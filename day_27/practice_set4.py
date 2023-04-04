# Python Data Structure Exercise for Beginners

# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
# Given:
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# Expected Output:
# Element at odd-index positions from list one
# [6, 12, 18]
# Element at even-index positions from list two
# [4, 12, 20, 28]
# Printing Final third list
# [6, 12, 18, 4, 12, 20, 28]
print("Solution 1:")
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
result = list()

odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = list2[0::2]
print("Element at even-index positions from list two")
print(even_elements)

print("Printing Final third list")
result.extend(odd_elements)
result.extend(even_elements)
print(result)

print()
# --------------------------------------------------------------------------------------------------------
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
# Given:
# list1 = [34, 54, 67, 89, 11, 43, 94]
# Expected Output:
# List After removing element at index 4  [34, 54, 67, 89, 43, 94]
# List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
# List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
print("Solution 2:")
sample_list = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", sample_list)
element = sample_list.pop(4)
print("List After removing element at index 4 ", sample_list)

sample_list.insert(2, element)
print("List after Adding element at index 2 ", sample_list)

sample_list.append(element)
print("List after Adding element at last ", sample_list)

print()
# --------------------------------------------------------------------------------------------------------
# Exercise 3: Slice list into 3 equal chunks and reverse each chunk
# Given:
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# Expected Outcome:
# Chunk  1 [11, 45, 8]
# After reversing it  [8, 45, 11]
# Chunk  2 [23, 14, 12]
# After reversing it  [12, 14, 23]
# Chunk  3 [78, 45, 89]
# After reversing it  [89, 45, 78]
print("Solution 3:")
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list ", sample_list)

length = len(sample_list)
chunk_size = int(length / 3)
start = 0
end = chunk_size

# run loop 3 times
for i in range(3):
    # get indexes
    indexes = slice(start, end)
    
    # get chunk
    list_chunk = sample_list[indexes]
    print("Chunk ", i, list_chunk)
    
    # reverse chunk
    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end += chunk_size

print()
# --------------------------------------------------------------------------------------------------------
# Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.
# Given:
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# Expected Output:
# Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
print("Solution 4:")
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sample_list)

count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Printing count of each item  ", count_dict)

print()
# --------------------------------------------------------------------------------------------------------
# Exercise 5: Create a Python set such that it shows the element from both lists in a pair
# Given:
# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]
# Expected Output:
# Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}
print("Solution 5:")
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
result = zip(first_list, second_list)
result_set = set(result)
print(result_set)

print()
# --------------------------------------------------------------------------------------------------------
# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
# Given:
# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}
# Expected Output:
# Intersection is  {57, 83, 29}
# First Set after removing common element  {65, 42, 78, 23}
print("Solution 6:")
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

intersection = first_set.intersection(second_set)
print("Intersection is ", intersection)
for item in intersection:
    first_set.remove(item)

print("First Set after removing common element ", first_set)

print()
# --------------------------------------------------------------------------------------------------------
# Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set
# Given:
# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}
# Expected Output:
# First set is subset of second set - True
# Second set is subset of First set -  False
# First set is Super set of second set -  False
# Second set is Super set of First set -  True
# First Set  set()
# Second Set  {67, 73, 43, 48, 83, 57, 29}
print("Solution 7:")
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

print("First set is subset of second set -", first_set.issubset(second_set))
print("Second set is subset of First set - ", second_set.issubset(first_set))

print("First set is Super set of second set - ", first_set.issuperset(second_set))
print("Second set is Super set of First set - ", second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print("First Set ", first_set)
print("Second Set ", second_set)

print()
# --------------------------------------------------------------------------------------------------------
# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
# Given:
# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
# Expected Outcome:
# After removing unwanted elements from list [47, 69, 76, 97]
print("Solution 8:")
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

print("List:", roll_number)
print("Dictionary:", sample_dict)

# create new list
roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
print("after removing unwanted elements from list:", roll_number)

print()
# --------------------------------------------------------------------------------------------------------
# Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates
# Given:
# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
# Expected Outcome:
# [47, 52, 44, 53, 54]
print("Solution 9:")
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

print("Dictionary's values - ", speed.values())

speed_list = list()

# iterate dict values
for val in speed.values():
    # check if value not present in a list
    if val not in speed_list:
        speed_list.append(val)
print("unique list", speed_list)

print()
# --------------------------------------------------------------------------------------------------------
# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
# Given:
# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# Expected Outcome:
# unique items [87, 45, 41, 65, 99]
# tuple (87, 45, 41, 65, 99)
# min: 41
# max: 99
print("Solution 10:")
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
print("Original list", sample_list)

sample_list = list(set(sample_list))
print("unique list", sample_list)

t = tuple(sample_list)
print("tuple ", t)

print("Minimum: ", min(t))
print("Maximum: ", max(t))
''' Exercise 1: Reverse the tuple
Given:
tuple1 = (10, 20, 30, 40, 50)
Expected output:
(50, 40, 30, 20, 10)'''

print("Solution 1:")
tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
print(tuple1)

print()
# ----------------------------------------------------------------------------------------------------------
""" Exercise 2: Access value 20 from the tuple
The given tuple is a nested tuple. write a Python program to print the value 20.
Given:
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
Expected output:
20 """

print("Solution 2:")
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

print()
# ----------------------------------------------------------------------------------------------------------
''' Exercise 3: Create a tuple with single item 50 '''

print("Solution 3:")
tuple1 = (50, )
print(tuple1)

print()
# ----------------------------------------------------------------------------------------------------------
''' Exercise 4: Write a program to unpack the following tuple into four variables and display each variable.
Given:
tuple1 = (10, 20, 30, 40)
Expected output:
tuple1 = (10, 20, 30, 40)
# Your code
print(a) # should print 10
print(b) # should print 20
print(c) # should print 30
print(d) # should print 40 '''

print("Solution 4:")
tuple1 = (10, 20, 30, 40)
a, b, c, d = tuple1
print(tuple1)
print(a)
print(b)
print(c)
print(d)

print()
# ----------------------------------------------------------------------------------------------------------
''' Exercise 5: Swap two tuples in Python
Given:
tuple1 = (11, 22)
tuple2 = (99, 88)
Expected output:
tuple1: (99, 88)
tuple2: (11, 22) '''

print("Solution 5:")
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(f"tuple1: {tuple1}")
print(f"tuple2: {tuple2}")

print()
# ----------------------------------------------------------------------------------------------------------
''' Exercise 6: Copy specific elements from one tuple to a new tuple
Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
Given:
tuple1 = (11, 22, 33, 44, 55, 66)
Expected output:
tuple2: (44, 55) '''

print("Solution 6:")
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:5]
# tuple2 = tuple1[3:-1]
print(tuple2)

print()
# ----------------------------------------------------------------------------------------------------------
''' Exercise 7: Modify the tuple Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222
Given:
tuple1 = (11, [22, 33], 44, 55)
Expected output:
tuple1: (11, [222, 33], 44, 55) '''

print("Solution 7:")
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)

print()
# ----------------------------------------------------------------------------------------------------------
''' Exercise 8: Sort a tuple of tuples by 2nd item
Given:
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
Expected output:
(('c', 11), ('a', 23), ('d', 29), ('b', 37)) '''

print("Solution 8:")
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)

print()
# ----------------------------------------------------------------------------------------------------------
''' Exercise 9: Counts the number of occurrences of item 50 from a tuple
Given:
tuple1 = (50, 10, 60, 70, 50)
Expected output:
2 '''

print("Solution 9:")
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

print()
# ----------------------------------------------------------------------------------------------------------
''' Exercise 10: Check if all items in the tuple are same
tuple1 = (45, 45, 45, 45)
Expected output:
True '''

print("Solution 10:")


def check(tuple):
    return all(i == tuple[0] for i in tuple)


tuple1 = (45, 45, 45, 45)
print(check(tuple1))

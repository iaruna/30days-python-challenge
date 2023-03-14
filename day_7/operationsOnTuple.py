# Accessing Values in Tuples
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print(f"tup1[0]: ", tup1[0])
print(f"tup1[1:5]: ", tup1[1:5])

# Delete Tuple Elements
tup = ('physics',  1997, 'chemistry', 2000)
print(tup)
del(tup)
# print("After deleting tup : ")
# print(tup)

A = len((1, 2, 3)) # Length
print(A)

a = (1, 2, 3) + (4, 5, 6)	# Concatenation
print(a)

b = ('Hi!',) * 4 # Repetition
print(b)

3 in (1, 2, 3) # Membership
print("Yes, 3 is available!")

for x in (1, 2, 3):
     print (x) # Iteration

L = ('spam', 'Spam', 'SPAM!') # Indexing, Slicing, and Matrixes
print(L[2])
print(L[-2])
print(L[1:])
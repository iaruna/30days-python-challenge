tuple = ( (3, 7, 1, 18, 9), "Raju", 5, 20, 3, 7, 6, 8, "Nikhil", "Deepanshu",8, 20)
# tuple[0] = 90 # TypeError: 'tuple' object does not support item assignment
print(type(tuple), tuple)
print(len(tuple))
print(tuple[0])
print(tuple[-1])
print(tuple[2])
# print(tuple[34]) # IndexError: tuple index out of range

if  342 in tuple:
  print("Yes 342 is present in this tuple")
tup2 = tuple[1:4]
print(tup2)

tuple1 =  (5, 20, 3, 7, 6, 8)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)

tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"))
print(tuple3)
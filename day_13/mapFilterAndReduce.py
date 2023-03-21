from functools import reduce


def cube(x):
    return x * x * x


print(cube(2))

# # map function - map is a highter order function
l = [1, 3, 5, 7, 9, 8, 6]
newl = []
for item in l:
    newl.append(cube(item))
newl = map(cube, l)  # location
newl = list(map(cube, l))  # converted in list
print(newl)

# filter- filter is a highter order function


def filter_function(a):
    return a > 4


newnewl = list(filter(filter_function, l))
print(newnewl)


numbers = [1, 3, 6, 8, 5]


def mysum(x, y):
    return x + y


sum = reduce(mysum, numbers)
print(sum)

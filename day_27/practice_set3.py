# Exercise 1: Write a program to create a function that takes two arguments, name and age, and print their value.
print("Solution 1:")
def func(name, age):
    print(name, age)
# call function
func("Aruna", 25)

print()
# ---------------------------------------------------------------------------------------------------------------------
# Exercise 2: Create a function with variable length of arguments
print("Solution 2:")
def func1(*args):
    for i in args:
        print(i)
print("Printing values")
func1(20, 40, 60)
print("Printing values")
func1(80, 100)

print()
# ---------------------------------------------------------------------------------------------------------------------
# Exercise 3: Return multiple values from a function
# Given:
# def calculation(a, b):
#     # Your Code
# res = calculation(40, 10)
# print(res)
# Expected Output
# 50, 30
print("Solution 3:(1)")
def calculation(a, b):
    sum = a + b
    sub = a - b
    return sum, sub
result = calculation(40, 10)
print(result)
print("Solution 3:(2)")
def calculation(a,b):
    return a + b , a - b
sum, sub = calculation(40, 10)
print(sum, sub)

print()
# ---------------------------------------------------------------------------------------------------------------------
# Exercise 4: Create a function with a default argument
print("Solution 4:")
def employee(name, salary=22000):
    # print(f"Name: {name} Salary: {salary}")
    print("Name:", name, "Salary:", salary)
employee("Aashi")
employee("Arohi", 25000)

print()
# ---------------------------------------------------------------------------------------------------------------------
# Exercise 5: Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it
print("Solution 5:")
def func_outer(a, b):
    pass

    def addition(a, b):
        return a + b
    
    #call inner function from outer function
    return addition(a,b) + 5

result =func_outer(7, 10)
print(result)

print()
# ---------------------------------------------------------------------------------------------------------------------
# Exercise 6: Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
# A recursive function is a function that calls itself again and again.
# Expected Output:
# 55
print("Solution 6:")
def add(num):
    if num:
        return num + add(num-1)
    else:
        return 0
result = add(10)
print(result)

print()
# ---------------------------------------------------------------------------------------------------------------------
# Exercise 7: Assign a different name to function and call it through the new name
print("Solution 7:")
def student(name, age):
    print(name, age)

student("Amvi", 7)
show_student = student
show_student("Anu", 9)

print()
# ---------------------------------------------------------------------------------------------------------------------
# Exercise 8: Generate a Python list of all the even numbers between 4 to 30
# Expected Output:
# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
print("Solution 8:")

print(list(range(4, 30, 2)))

print()
# ---------------------------------------------------------------------------------------------------------------------
# Exercise 9: Find the largest item from a given list
# x = [4, 6, 8, 24, 12, 2]
# Expected Output:
# 24
print("Solution 9:")
x = [4, 6, 8, 24, 12, 2]
print(max(x))

# Python Functions Exercise
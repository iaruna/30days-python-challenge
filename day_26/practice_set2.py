# Exercise 1: Print First 10 natural numbers using while loop
print("Solution 1:")
i = 1
while i <= 10:
    print(i)
    i += 1

print()
# ---------------------------------------------------------------------------------------------------------------------

# Exercise 2: Print the following pattern Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
print("Solution 2:")
row = 5
for i in range(1, row+1, 1):
    for j in range(1, i+1):
        print(j, end=" ")
    print("")

print()
# --------------------------------------------------------------------------------------------------------------------

# Exercise 3: Calculate the sum of all numbers from 1 to a given number
print("Solution 3:")
s = 0
number = int(input("Enter your number: "))
for i in range(1, number+1, 1):
    s += i
print(f"Sum of {number} is {s}")

n = int(input("Enter your number: "))
x = sum(range(1, n + 1))
print('Sum is:', x)

print()
# --------------------------------------------------------------------------------------------------------------------
# Exercise 4: Write a program to print multiplication table of a given number
# For example, num = 2 so the output should be 2 4 6 8 10 12 14 16 18 20

print("Solution 4:")
n = 2
for i in range(1, 11, 1):
    table = 2 * i
    print(table)

print()
# --------------------------------------------------------------------------------------------------------------------
# Exercise 5: Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop
# Given:
# numbers = [12, 75, 150, 180, 145, 525, 50]
# Expected output:
# 75
# 150
# 145

print("Solution 5:")
numbers = [12, 75, 150, 180, 145, 525, 50]
for n in numbers:
    if n > 500:
        break
    elif n > 150:
        continue
    elif n % 5 == 0:
        print(n)

print()
# --------------------------------------------------------------------------------------------------------------------
# Exercise 6: Count the total number of digits in a number
# For example, the number is 75869, so the output should be 5.
print("Solution 6:")
number = 75869
count = 0
while number != 0:
    number = number // 10
    count += 1
print(f"Total number of digits {count}")

print()
# --------------------------------------------------------------------------------------------------------------------
# Exercise 7: Print the following pattern
# Write a program to use for loop to print the following reverse number pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

print("Solution7:")
n = 5
k = 5
for i in range(0, n+1):
    for j in range(k-i, 0, -1):
        print(j, end=" ")
    print()

print()
# -------------------------------------------------------------------------------------------------------------------

# Exercise 8: Print list in reverse order using a loop
# Given:
# list1 = [10, 20, 30, 40, 50]
# Expected output:
# 50
# 40
# 30
# 20
# 10
print("Solution 8:(1)")
list = [10, 20, 30, 40, 50]
newlist = reversed(list)
for i in newlist:
    print(i)
print("Solution 8:(2)")
list1 = [10, 20, 30, 40, 50]
size = len(list1) - 1
for i in range(size, -1, -1):
    print(list1[i])

print()
# -------------------------------------------------------------------------------------------------------------------
# Exercise 9: Display numbers from -10 to -1 using for loop
print("Solution 9:")
for number in range(-10, 0, 1):
    print(number)

print()
# -------------------------------------------------------------------------------------------------------------------
# Exercise 10: Use else block to display a message “Done” after successful execution of for loop
print("Solution 10:")
for i in range(5):
    print(i)
else:
    print("Done")

print()
# -------------------------------------------------------------------------------------------------------------------
# Exercise 11: Write a program to display all prime numbers within a range
# Given range: start = 25, end = 50
# Expected output: Prime numbers between 25 and 50 are: 29 31 37 41 43 47
print("Solution 11:")
start = 25
end = 50
print(f"Prime numbers between {start} and {end} are: ")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

print()
# -------------------------------------------------------------------------------------------------------------------
# Exercise 12: Display Fibonacci series up to 10 terms
# Expected output:
# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34
print("Solution 12:")
number1, number2 = 0, 1
print("Fibonacci sequence:")
for i in range(10):
    print(number1, end="  ")
    result = number1 + number2
    number1 = number2
    number2 = result

print()
# -------------------------------------------------------------------------------------------------------------------
# Exercise 13: Find the factorial of a given number
# For example: calculate the factorial of 5
print("Solution 13:")
n = 5
factorial = 1
if n < 0:
    print("Factorial does not exist for negative numbers")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, n+1):
        factorial = factorial * i
    print(f"Factorial of {i} is {factorial}")

print()
# -------------------------------------------------------------------------------------------------------------------
# Exercise 14: Reverse a given integer number
# Given: 76542
# Expected output: 24567
print("Solution 14:")
number = 76542
rev_number = 0
print(f"Given number is {number}")
while number > 0:
    reminder = number % 10
    rev_number = (rev_number * 10) + reminder
    number = number // 10
print(f"Reverse nunber {rev_number}")

print()
# -------------------------------------------------------------------------------------------------------------------
# Exercise 15: Use a loop to display elements from a given list present at odd index positions
# Given:
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Expected output:
# 20 40 60 80 100
print("Solution 15:")
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list[1::2]:
    print(i, end=" ")

print()
# -------------------------------------------------------------------------------------------------------------------
# Exercise 16: Calculate the cube of all numbers from 1 to a given number
print("Solution 16:")
input_number = 6
for i in range(1, input_number + 1):
    print(f"Number is {i} and cube is {(i * i * i)}")

print()
# -------------------------------------------------------------------------------------------------------------------
# Exercise 17: Find the sum of the series upto n terms
print("Solution 17:")
n = 5
start = 2
sum_seq = 0
for i in range(0, n):
    # print(start, end="+")
    sum_seq += start
    start = start * 10 + 2
print("Sum of [2 + 22 + 222 + 2222 + 22222] series is:", sum_seq)

print()
# -------------------------------------------------------------------------------------------------------------------
# Exercise 18: Print the following pattern
# Write a program to print the following start pattern using the for loop
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
print("Solution 18:")
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

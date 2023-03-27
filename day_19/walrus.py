# New operator 3.8 onward &  allows you to assign a value to a variable within an expression.
a = True
print(a)
print(a := False)

numbers = [1, 2, 4, 6, 8]

while (n := len(numbers)) > 0:
    print(numbers.pop())

# assignment expression assigns values to variables as part of a larger expression.
foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)

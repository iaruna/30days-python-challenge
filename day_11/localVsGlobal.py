x = 4
print(x)

def hello():
    x = 5
    y = 1
    print(f"The local x is {x}")
    print("Hello World!")

print(f"The global x is {x}")
hello()
x = 5
print(f"The global x is {x}")

y = 10
def my_func():
    global y
    x = 5
    y = 5
my_func()
print(y)
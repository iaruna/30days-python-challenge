def factorial(num):
    if num == 1 or num ==0:
        return 1
    else:
        return(num * factorial(num - 1))

num = 7
print(factorial(num))
print(factorial(5))

# fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
        # return((n-1) + (n-2))   # wrong
print(f"fibonacci(0) is {fibonacci(0)}")
print(f"fibonacci(1) is {fibonacci(1)}")
print(f"fibonacci(2) is {fibonacci(2)}")
print(f"fibonacci(3) is {fibonacci(3)}")
print(f"fibonacci(4) is {fibonacci(4)}")
print(f"fibonacci(5) is {fibonacci(5)}")
print(f"fibonacci(6) is {fibonacci(6)}")
print(f"fibonacci(7) is {fibonacci(7)}")
print(f"fibonacci(8) is {fibonacci(8)}")
print(f"fibonacci(9) is {fibonacci(9)}")
print(f"fibonacci(10) is {fibonacci(10)}")
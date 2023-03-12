def Gmean(a, b):
    mean = (a * b) / (a + b)
    print(mean)

def IsGreater(a, b):
    if (a > b):
        print("First number is greater")
    else:
        print("second number is greater or equal")

a = 9
b = 8
Gmean(a, b)
IsGreater(12, 15)

c = 7
d = 8
Gmean(c, d)
IsGreater(c, d)
print(min(c, d))


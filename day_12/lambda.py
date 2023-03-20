def double(x):
    return x*2


print(double(5))


def double(x): return x*2
def cube(x): return x*x*x


def avg(x, y, z): return (x+y+z)/3


print(double(6))
print(cube(5))
print(avg(3, 5, 7))


def appl(fx, value):
    return 6 + fx(value)


print(appl(cube, 2))
print(appl(lambda x: x*x*x, 2))
print(appl(lambda x: x*x, 2))

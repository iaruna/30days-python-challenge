print("Decorator")


def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx


@greet
def hello():
    print("Hello Amvi")


@greet
def sum(a, b):
    print(a+b)


hello()
# greet(sum)(3,8)
sum(5, 7)

"""function cache is a technique for improving the performance of a program by storing the results of a function so that 
you can reuse the results instead of recomputing them every time the function is called"""
from functools import lru_cache
import time


@lru_cache(maxsize=None)
def func(x):
    time.sleep(4)
    return x*9


print(func(9))
print("Done for 9")
print(func(81))
print("Done for 81")
print(func(79))
print("Done for 79")
print(func(69))
print("Done for 69")
print(func(59))
print("Done for 59")
print(func(49))
print("Done for 49")
print(func(39))
print("Done for 39")
print(func(49))
print("Done for 49")
print(func(59))
print("Done for 59")
print(func(69))
print("Done for 69")
print(func(79))
print("Done for 79")
print(func(89))
print("Done for 89")

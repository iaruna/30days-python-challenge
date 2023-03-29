'''Generators are a powerful tool for working with large or complex data sets, as they allow you
to generate the values on-the-fly, rather than having to create and store the entire sequence in memory.'''

def my_generator():
    for i in range(5000):
        # Complex computations
        # . The yield statement returns a value from the generator and suspends the execution of the function until the next value is requested.
        yield i

gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in  gen:
    print(j)
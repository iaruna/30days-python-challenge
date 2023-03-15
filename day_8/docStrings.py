def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)

# Accessing Docstrings
def my_function():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.''' 
    return None 
print("Using __doc__:")
print(my_function.__doc__)

print("Using help:")
help(my_function)

# One-line Docstrings
def power(a, b):
    """Returns arg1 raised to power arg2."""
    return a**b
print(power.__doc__)

# Multi-line Docstrings
def my_function(arg1):
    """
    Summary line.
  
    Extended description of function.
  
    Parameters:
    arg1 (int): Description of arg1
  
    Returns:
    int: Description of return value
  
    """
  
    return arg1
  
print(my_function.__doc__)
a = int(input("Enter any value between 5 and 9: "))
if a == quit:
    pass
if(a < 5 or a > 9):
    raise ValueError("Value should be between 5 and 9")

# define Python user-defined exceptions
class Error(Exception):  # Base class for other exceptions
    pass
class zerodivision(Error): # Raised when the input value is zero
    pass
try:
    i_num = int(input("Enter a number: "))
    if i_num == 0:
        raise zerodivision
except zerodivision:  
    print("Input value is zero, try again!")
    print()

# NetworkError has base RuntimeError and not Exception
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg
try:
    raise Networkerror("Error")
except Networkerror as e:
    print(e.args)
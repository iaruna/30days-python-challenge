'''Four types of arguments:
Default Arguments, Keyword Arguments, Required Arguments, Variable length Arguments'''

def name(fname = "Aruna", lname = "Kumari"): # Default
    print("Hello," ,fname ,lname)
name()
# name(Aki)  #NameError: name 'Sabhya' is not defined
name(lname = "K")


def name(fname, mname, lname):  # Keyword Arguments
    print("Hello," ,fname ,mname ,lname)
name("Ms." , "Arohi", "Aryan")
#name(lname ='Kumari', fname ='Aruna') # TypeError: name() missing 1 required positional argument: 'mname' 
name(mname = ".", lname ='Kumari', fname ='Aruna')


def name(fname, mname, lname): #Required Arguments
    print("Hello,", fname, mname, lname)
# name("Peter", "Quill") # TypeError: name() missing 1 required positional argument: "lname"
name("Mr." , "Peter", "Quill")

'''While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.'''
def name(*name):  # Variable length Arguments 1)Arbitrary
    print("Hi!!,", name[0], name[1], name[2])
name("Sakshi", "Mona", "Aruna")

# processing in the form of dictionary.
def name (**name):  # 2)Keyword Arbitrary Arguments
    print("Hello,", name["fname"], name["lname"])
name(fname = "Aruna", lname = "Kumari")

def name(fname, mname, lname): # return statement
    return "Hello," + fname +" " + mname + " " + lname
print(name("Ms.", "Aruna", "Kumari"))

def average(*numbers):
  sum = 0
  for i in numbers:
    sum = sum + i
#   print("Average is: ", sum / len(numbers))
  return sum / len(numbers)
avg = average(5, 6, 7, 1)
print(avg)


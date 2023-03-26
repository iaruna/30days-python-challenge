# if we use more than one inheritance then it's called as hybrid Inheritance.
# Hybrid inheritance is a combination of multiple and single inheritance in Object-oriented programming.

# Python program to demonstrate Hierarchical inheritance
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class1


class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

# Derivied class2


class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")


# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

# Hierarchical inheritance is a type of inheritance in OOP where multiple  sunclasses inherit from a single base class.
# A single base class acts as a parent class for multiple subclasses.


class BaseClass:
    pass


class D1(BaseClass):
    pass


class D2(BaseClass):
    pass


class D3(D1):
    pass

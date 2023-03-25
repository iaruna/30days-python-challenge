# Python Program to depict multiple inheritance
# when method is overridden in both classes

class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")


class Class3(Class1):
    def m(self):
        print("In Class3")


class Class4(Class2, Class3):
    pass


obj = Class4()
obj.m()

# Python Program to depict multiple inheritance
# when every class defines the same method


class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")


class Class3(Class1):
    def m(self):
        print("In Class3")


class Class4(Class2, Class3):
    def m(self):
        print("In Class4")


obj = Class4()
obj.m()

Class2.m(obj)
Class3.m(obj)
Class1.m(obj)


class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")


class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")

# class DancerEmployee(Employee, Dancer):


class DancerEmployee(Dancer, Employee):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name


o = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show()

# MRO
print(DancerEmployee.mro())

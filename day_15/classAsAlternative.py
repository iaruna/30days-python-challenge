class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])


e1 = Employee("Sohan", 12000)
print(e1.name)
print(int(e1.salary))

string = "Rohan-15000"
# e = Employee(string.split("-"), 12000)
# e = Employee(string.split("-")[0], string.split("-")[1])
e2 = Employee.fromStr(string)
print(e2.name)
print(int(e2.salary))


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromString(cls, string):
        name, age = string.split(",")
        return cls(name, int(age))


Person = person.fromString("John, 30")
print(Person.name, Person.age)

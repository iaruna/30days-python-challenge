class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print("The default langauge is Python")


e1 = Employee("Sayali K", 101)
e1.showDetails()
e2 = Programmer("Amvi Singh", 102)
e2.showDetails()
e2.showLanguage()

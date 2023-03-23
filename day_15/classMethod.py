class Employee:
    company = "Bajaj"

    def show(self):
        print(
            f"The name of Employee is {self.name} and Company is {self.company}.")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany


e1 = Employee()
e1.name = "Saloni"
e1.show()
e1.changeCompany("Cognizant")
e1.show()
print(Employee.company)

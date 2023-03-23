class employee:
    companyName = "Apple"
    noOfemployees = 0

    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        employee.noOfemployees += 1

    def showDetails(self):
        print(
            f"The name of the employee is {self.name} and the raise amount in {self.noOfemployees} sized {self.companyName} is {self.raise_amount}.")


# employee.showDetails(emp1)
emp1 = employee("Sohan")
emp1.raise_amount = 0.03
emp1.companyName = "Apple India"
emp1.showDetails()
employee.companyName = "TCS"
print(employee.companyName)

emp2 = employee("Rohan")
emp2.companyName = "Tata Communications"
emp2.showDetails()

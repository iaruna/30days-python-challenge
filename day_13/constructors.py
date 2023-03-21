class person:
    name = "Aasu"
    occ = "Developer"
    salary = 6000

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = person()
a.name = "Divya"
a.occ = "HR"
a.info()

# With init

# perpose is to initialise value and it returns null


class person:
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = person("Aasu", "Developer")
b = person("Divya", "HR")
a.info()
b.info()

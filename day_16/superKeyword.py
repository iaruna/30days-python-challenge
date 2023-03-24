class ParentClass:
    def parent_method(self):
        print("This is the parent method.")


class ChildClass(ParentClass):
    def parent_method(self):
        print("Rakhi")
        super().parent_method()

    def child_method(self):
        print("This is the child method.")
        super().parent_method()


child_object = ChildClass()
child_object.child_method()
child_object.parent_method()


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class programmer(Employee):
    def __init__(self, name, id, lang):
        # self.name = name
        # self.id = id
        super().__init__(name, id)
        self.lang = lang


e = Employee("Raunak", 102)
p = programmer("Raktim", 103, "Python")
print(e.name)
print(p.name)
print(p.id)
print(p.lang)

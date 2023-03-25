# single inheritance
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")


class Child(Parent):  # Derived class
    def func2(self):
        print("This function is in child class.")


object = Child()  # Driver's code
object.func1()
object.func2()


class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal.")


class cat(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name, species="cat")
        self.breed = breed

    def make_sound(self):
        print("Purr")


d = cat("Cat", "Persian cat")
d.make_sound()
a = animal("Cat", "Cat")
a.make_sound()

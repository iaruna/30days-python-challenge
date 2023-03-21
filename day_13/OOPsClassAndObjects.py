class Parrot:

    # class attribute
    name = ""
    age = 0


# create parrot1 object
parrot1 = Parrot()
parrot1.name = "Budgerigar"

# create parrot1 object
parrot2 = Parrot()
parrot2.name = "Blu"
parrot2.age = 10

# create another object parrot2
parrot3 = Parrot()
parrot3.name = "Woo"
parrot3.age = 15

# access attributes
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")
print(f"{parrot3.name} is {parrot3.age} years old")


class person:
    name = "Aruna"
    age = 24

    def info(self):  # self means wo object jiske liye method call ho raha hai ex- a ka name, age
        print(f"{self.name} is {self.age} years old!")


a = person()
a.info()

a = person()
a.name = "Arohi"
a.age = 17
print(a.name, a.age)

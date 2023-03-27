class employee:
    def __init__(self):
        self.name = "sakshi"


a = employee()
a.emp1 = 5
print(a.name)
# print(a.__name)  # can't be accessed directly
# print(a._employee__name)  # can be accessed indirectly
print(a.__dir__())


class emp:
    def __init__(self):
        self._name = "Sayali"

    def _funName(self):      # protected method
        return "Digit Marketing"


class Subject(emp):  # inherited class
    pass


obj = emp()
print(dir(obj))
# calling by object of Student class
print(obj._name)
print(obj._funName())

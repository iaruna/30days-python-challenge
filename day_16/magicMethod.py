class employee:
    # name = "Saloni"
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i = i+1
        return i


# e = employee()
e = employee("Sahil")
print(e.name)
print(len(e))

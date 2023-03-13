l =  [3, 5, 6, "Apple", True]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])

colors = ["Red", "Green", "Blue", "Yellow",  "Black"]
print(colors[2]) # Accessing list items

print(l[-3]) # Negative index
print(l[len(l)-3]) # Positive index

if 7 in l:
    print("Yes")
else:
    print("No")

if "Green" in colors:
    print("Green is present")
else:
    print("Green is absent")

print(l[1:-1])
print(l[1:4])
print(l[1:5:2])

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)
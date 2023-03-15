# dict is ordered 3.7 onward
dict ={
    103 : "Aruna",
    123 : "Aaru",
    113 : "Rashi"
}
print(dict[103])

info = {"Name" : "Arohi", "Age": 17, "eligible" : False}
print(info)
print(info["Name"])
print(info.get("Name2"))
print(info.keys())
print(info.values())

for key in info.keys():
    print(key)
    print(info[key])

print(info.items())

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")
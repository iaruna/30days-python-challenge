# Exercise 1: Convert two lists into a dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

print("Solution 1: Using the zip() function and a dict() constructor")
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict1 = dict(zip(keys, values))
print(res_dict1)

print()
# ---------------------------------------------------------------------------------------------------------------------------------------
# Exercise 2: Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

print("Solution 2:")
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict1, **dict2}
print(dict3)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

print()
# ---------------------------------------------------------------------------------------------------------------------------------------
# Exercise 3: Print the value of key ‘history’ from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# Expected output:
# 80

print("Solution 3:")
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])

print()
# ---------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4: Initialize dictionary with default values  In Python, we can initialize the keys with the same values.
# Given:
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# Expected output:
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
print("Solution 4:Using fromkeys() method it returns a dictionary with the specified keys and the specified value.")

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

result = dict.fromkeys(employees, defaults)
print(result)

# Individual data
print(result["Kelly"])

print()
# ---------------------------------------------------------------------------------------------------------------------------------------
# Exercise 5: Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
# Given dictionary:
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# # Keys to extract
# keys = ["name", "salary"]
# Expected output:
# {'name': 'Kelly', 'salary': 8000}

print("Solution 5:(1) Using Dictionary Comprehension")
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
newDict = {k: sampleDict[k] for k in keys}
print(newDict)

print("(2) Using the update() method and loop")
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
# keys to extract
keys = ["name", "salary"]
# new dict
res = dict()
for k in keys:
    # add current key with its value from sample_dict
    res.update({k: sample_dict[k]})
print(res)

print()
# ---------------------------------------------------------------------------------------------------------------------------------------
# Exercise 6: Delete a list of keys from a dictionary
# Given:
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# # Keys to remove
# keys = ["name", "salary"]
# Expected output:
# {'city': 'New york', 'age': 25}

print("Solution 6: (1) Using the pop() method and loop")
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]
for k in keys:
    sample_dict.pop(k)
print(sample_dict)
print("Solution 6: (2) Using Dictionary Comprehension")
sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
print(sample_dict)

print()
# ---------------------------------------------------------------------------------------------------------------------------------------
# Exercise 7: Write a Python program to check if value 200 exists in the following dictionary.
# Given:
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# Expected output:
# 200 present in a dict

print("Solution 7:")
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print('200 present in a dict')

print()
# ---------------------------------------------------------------------------------------------------------------------------------------
# Exercise 8: Write a program to rename a key city to a location in the following dictionary.
# Given:
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# Expected output:
# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

print("Solution 8:")
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

print()
# ---------------------------------------------------------------------------------------------------------------------------------------
# Exercise 9: Get the key of a minimum value from the following dictionary
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# Expected output:
# Math

print("Solution 9:")
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(min(sample_dict, key=sample_dict.get))

print()
# ---------------------------------------------------------------------------------------------------------------------------------------
# Exercise 10: Write a Python program to change Brad’s salary to 8500 in the following dictionary.
# Given:
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# Expected output:
# {
#    'emp1': {'name': 'Jhon', 'salary': 7500},
#    'emp2': {'name': 'Emma', 'salary': 8000},
#    'emp3': {'name': 'Brad', 'salary': 8500}
# }

print("Solution 10:")
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}
sample_dict['emp3']['salary'] = 8500
print(sample_dict)

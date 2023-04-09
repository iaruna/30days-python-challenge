''' Exercise 1: Convert the following dictionary into JSON format
data = {"key1" : "value1", "key2" : "value2"}
Expected Output:
data = {"key1" : "value1", "key2" : "value2"} '''

from json import JSONEncoder
import json
print("Solution 1:")
data = {"key1": "value1", "key2": "value2"}
jsonData = json.dumps(data)
print(jsonData)

print()
# ---------------------------------------------------------------------------------
''' Exercise 2: Access the value of key2 from the following JSON
import json
sampleJson = """{"key1": "value1", "key2": "value2"}"""
# write code to print the value of key2
Expected Output:
value2 '''

print("Solution 2:")
sampleJson = """{"key1": "value1", "key2": "value2"}"""
data = json.loads(sampleJson)
print(data['key2'])

print()
# ---------------------------------------------------------------------------------
''' Exercise 3: PrettyPrint following JSON data
PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").
sampleJson = {"key1": "value1", "key2": "value2"}
Expected Output:
{
  "key1" = "value2",
  "key2" = "value2",
  "key3" = "value3"
} '''

print("Solution 3:")
sampleJson = {"key1": "value2", "key2": "value2", "key3": "value3"}
prettyPrintedJson = json.dumps(sampleJson, indent=2, separators=(",", " = "))
print(prettyPrintedJson)

print()
# ---------------------------------------------------------------------------------
''' Exercise 4: Sort JSON keys in and write them into a file
Sort following JSON data alphabetical order of keys
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
Expected Output:
{
    "age": 29,
    "id": 1,
    "name": "value2"
} '''

print("Solution 4:")
sampleJson = {"id": 1, "name": "value2", "age": 29}

print("Started writing JSON data into a file")
with open("sampleJson.json", "w") as write_file:
    json.dump(sampleJson, write_file, indent=4, sort_keys=True)
print("Done writing JSON data into a file")

print()
# ---------------------------------------------------------------------------------
''' Exercise 5: Access the nested key ‘salary’ from the following JSON
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
write code to print the value of salary
Expected Output:
7000 '''

print("Solution 5:")
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
data = json.loads(sampleJson)
print(data['company']['employee']['payble']['salary'])

print()
# ---------------------------------------------------------------------------------
''' Exercise 6: Convert the following Vehicle Object into JSON
import json
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price
vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
# Convert it into JSON format
Expected Output:
{
    "name": "Toyota Rav4",
    "engine": "2.5L",
    "price": 32000
} '''

print("Solution 6:")


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
print("Encode Vehicle Object into JSON")
vehicleJson = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
print(vehicleJson)

print()
# ---------------------------------------------------------------------------------
''' Exercise 7: Convert the following JSON into Vehicle Object
{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }
For example, we should be able to access Vehicle Object using the dot operator like this.
vehicleObj.name, vehicleObj.engine, vehicleObj.price '''

print("Solution 7:")


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


def vehicleDecoder(obj):
    return Vehicle(obj['name'], obj['engine'], obj['price'])


vehicleObj = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }',
                        object_hook=vehicleDecoder)

print("Type of decoded object from JSON Data")
print(type(vehicleObj))
print("Vehicle Details")
print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)

print()
# ---------------------------------------------------------------------------------
''' Exercise 8: Check whether following json is valid or invalid. If Invalid correct it
{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000
            "bonus":800
         }
      }
   }
} '''

print("Solution 8:")


def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True


InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } }"""
isValid = validateJSON(InvalidJsonData)

print("Given JSON string is Valid", isValid)

print()
# ---------------------------------------------------------------------------------
''' Exercise 9: Parse the following JSON to get all the values of a key ‘name’ within an array
[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]
Expected Output:
["name1", "name2"] '''

print("Solution 9:")

sampleJson = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""


sampleJson = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""


sampleJson = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

data = []
try:
    data = json.loads(sampleJson)
except Exception as e:
    print(e)

dataList = [item.get('name') for item in data]
print(dataList)

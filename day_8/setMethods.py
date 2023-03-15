s1 = {2, 4, 6, 5}
s2 = {2, 3, 9, 7}
print(s1,s2)
print(s1.union(s2))
s1. update(s2)
print(s1,s2)

city1 = {"Delhi", "Goa", "Pune"}
city2 = {"Bihar", "UP", "Delhi"}
print(city1.intersection(city2))
city1. intersection_update(city2)
print(city1, city2)

# symmetric difference
city1 = {"Delhi", "Goa", "Pune"}
city2 = {"Bihar", "UP", "Delhi"}
print(city1.symmetric_difference(city2))
city = city1. difference(city2)
print(city)

# disjoint
city1 = {"Delhi", "Goa", "Pune"}
city2 = {"Bihar", "UP", "Delhi"}
print(city1.isdisjoint(city2))

# superset means available in both sets
city1 = {"Delhi", "Goa", "Pune"}
city2 = {"Bihar", "UP"}
city3 = {"Delhi", "Goa"}
print(city1.issuperset(city2))
print(city1.issuperset(city3))

# subset if all the items of original set are present in particular set
city1 = {"Delhi", "Goa", "Pune"}
city2 = {"Delhi", "Goa"}
print(city2.issubset(city1))

cities = {"Delhi", "Goa", "Pune"}
cities.add("Kolkata")
print(cities)

cities = {"Delhi", "Goa", "Pune"}
cities.remove("Goa")
print(cities)

cities = {"Delhi", "Goa", "Pune"}
cities.discard("Kolkata")
print(cities)

cities = {"Delhi", "Goa", "Pune"}
item = cities.pop()
print(cities)
print(item)


# cities = {"Delhi", "Goa", "Pune"}
# del.cities
# print(cities)

cities = {"Delhi", "Goa", "Pune"}
cities.clear()
print(cities)

# check if city exist
cities = {"Delhi", "Goa", "Pune"}
if "Delhi" in cities:
    print("Yes, Delhi is present")
else:
    print("Delhi is not present")
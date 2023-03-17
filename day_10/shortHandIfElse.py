# a = 2
# b = 330
# print("A") if a > b else print("B")

# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")

# c = 9 if a < b else 0
# print(c)

# i = 10
# print(True) if i < 15 else print(False)

x = 87
result = {x > 190: "First condition satisfied!", 
        x == 87: "Second condition satisfied!"}.get(
True, "Third condition satisfied")
print(result)

# x = 87
# {x < 190: print("First condition satisfied!"),
# x == 87: print("Second condition satisfied!")}.get(
# True, print("Third condition satisfied!"))
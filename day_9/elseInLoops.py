for i in []:
# for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("Sorry no i")

i = 0
while i < 7:
    print(i)
    i = i+1
    if i == 8:
    # if i == 4:
        break
else:
    print("Sorry no i")


for x in range(5):
    print("Iteration no {} in for loop" .format(x+1))
    # print(f"Iteration no {x+1} in for loop")
else:
    print("else block in loop")
print("Out of loop")
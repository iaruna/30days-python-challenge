for i in range(1,12):
    if(i == 11):
        break
    print("5 X" ,i, "=",  5 *i )
print( "Out of loop")


# for j in range(12):
#     if(j == 10):
#         print("Skip the iteration")
#         continue
#     print("5 X" ,j+1, "=" ,5 * (j+1))


i = 0
while True:
  print(i)
  i = i + 1
  if(i%10 == 0):
    break


# for i in range(1,101,1):
#     print(i ,end=" ")
#     if(i==10):
#         break
#     else:
#         print("Miss")
# print("Thank you")

for i in [2, 3, 4, 5, 7, 6, 8, 0]:
    if (i % 2 != 0):
        continue
    print(i)
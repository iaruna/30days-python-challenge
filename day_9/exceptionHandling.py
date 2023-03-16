a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*(i)}")
except:
    print("Invalid Input!")

print("End of program")

try:
    num = int(input("Enter an integer: "))
    a = [6, 4]
    print(a[num])
except ValueError:
    print("Number entered is not in an integer.")

except IndexError:
    print("Index Error")
x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
# if x is o
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
        # case with if-condition
    case _ if x<=9:
        print("x is less than 9")
    case _ if x>=9:
        print("x is greater than 9")
    case _:
        print(x)

#Syntax:
# match variable_name:
#             case ‘pattern1’ : //statement1
#             case ‘pattern2’ : //statement2
#             …
#             case ‘pattern n’ : //statement n

x = 4
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)
        
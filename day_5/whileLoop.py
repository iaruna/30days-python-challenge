
# don't run this because it through error
# number = 0
# while number < 10:
#     print(f"Number is {number}!") # It runs infinitely.

i = 5
while(i > 0):
    print(i)
    i= i - 1
else:
    print("I am inside else")
'''the count variable is set to 5 which decrements after each iteration. Depending upon the while loop condition'''


#  create a do while loop in Python, need to modify the while loop a bit in order to get similar behavior to a do while loop in other languages.
# secret_word = "python"
# counter = 0
# while True:
#     word = input("Enter the secret word: ").lower()
#     counter = counter + 1
#     if word == secret_word:
#         break
#     if word != secret_word and counter > 7: 
#         break
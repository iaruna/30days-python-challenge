# rt--> open file in text mode
# rb --> open file in binary mode

# writing a file
f = open("file1.txt", "w")
f.write("Have a Good Day!")
f.close()

# Add in file
f = open("file.txt", "a")
f.write("Have a Good Day!\n")
f.close()

# or

with open("file.txt","a") as f:
    f.write("Hey, I am inside with\n")

# reading a file
f = open("file.txt", "r")
# print(f)
text = f.read()
print(text)
f.close()
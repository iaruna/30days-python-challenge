# with open("file.txt", "w") as f:
#     dates = ['20/3/21', '21/3/21', '22/3/21']
#     for date in dates:
#         f.write(date + '\n')

f = open('file.txt', 'r')
print(f.read())
text = f.read()
print(text)
f.close()


f = open("file1.txt", "w")
f.write("Hello Shiva, How's your day!")
f.close()


with open("file1.txt", "r") as f:
    print(type(f))
    f.seek(6)  # move to 6th  byte in file
    data = f.read(9)  # read next 9 bytes
    print(data)

with open("file1.txt", "w") as f:
    f.write("Good Morning!")
    f.truncate(13)  # start to given nos. of bytes
with open("file1.txt", "r") as f:
    print(f.read())

# with open("file1.txt", "r") as f:
#     data = f.read(9)  # read the first 10 bytes
#     current_position = f.tell()  # save the current position
#     print(current_position)
#     f.seek(current_position)  # seek to the current position
#     print(f.seek(current_position))
#     print(data)

    f.tell()  # read all file
    print(f.read())

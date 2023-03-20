import os

folders = os.listdir('python')

for folder in folders:
    print(folder)
    print(os.listdir(f"python/{folder}"))


# Get the current working directory (CWD)
def current_path():
    print(os.getcwd())
    print()


print('Current working directory before')
current_path()  # printing CWD before

os.chdir('../')  # changing the CWD
print('Current working directory after')
current_path()

files = os.listdir(".")  # current directory
print(files)

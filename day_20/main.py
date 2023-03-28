import shutil  # it's a built-in module which help to perform high level file operations, including copying
import os

# Functions in the shutil module

# copy function is use to copies file located at source to a new location specified by destination.
shutil.copy("main.py", "shell_utility.py")

os.rename("shell_utility.py", "main1.py")

# similar to .copy, but it preserves more metadata about the original file, like timestamp.
shutil.copy2("main.py", "main2.py")

# copies the folder with file located at source to a new location specified by destination.
shutil.copytree("newfolder", "folder")

# moves the file located at source to destination.
shutil.move("newfolder/file.txt", "file.file")

# deletes the directory located at path, along with all of its contents.
shutil.rmtree("folder")

os.remove("file.file")

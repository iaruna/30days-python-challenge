import os

if (not os.path.exists("python")):
    os.mkdir("python")


for i in range(0, 30):
    os.mkdir(f'python/day{i+1}')

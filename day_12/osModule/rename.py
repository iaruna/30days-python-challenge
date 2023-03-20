import os

for i in range(0, 30):
    # source and destination
    os.rename(f"python/day{i+1}", f"python/day_{i+1}")

#Good Morning,Good Afternoon and Good Evening
import time
# timestamp = time.strftime("%H : %M : %S")
# print(timestamp)
# timestamp = time.strftime("%H")
# print(timestamp)
# timestamp = time.strftime("%M")
# print(timestamp)
# timestamp = time.strftime("%S")
# print(timestamp)

import datetime
currentTime = datetime.datetime.now()
currentTime.hour
name = input("Enter Your Name: ")
if currentTime.hour < 12:
    print(f"{name},", "Good Morning.")
elif 12 <= currentTime.hour < 18:
    print(f"{name},", "Good Afternoon.")
else:
    print(f"{name},", "Good Evening.")
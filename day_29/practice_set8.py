# Exercise 1: Print current date and time in Python

print("Solution 1:")
import datetime
print(datetime.datetime.now())
# print(datetime.datetime.now().time)

print()
# ----------------------------------------------------------------------------------------------------------------
''' Exercise 2: Convert string into a datetime object
For example, You received the following date in string format. Please convert it into Python’s DateTime object.
Given:
date_string = "Apr 6 2023  6:40PM"
Expected output:
2023-04-06 18:40:00 '''

print("Solution 2:")
from datetime import datetime
date_string = "Apr 6 2023  6:40PM"
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)

print()
# ----------------------------------------------------------------------------------------------------------------
''' Exercise 3: Subtract a week (7 days)  from a given date in Python
Given:
given_date = datetime(2023, 4, 6)
Expected output:
2023-03-30 '''

print("Solution 3:")
from datetime import datetime, timedelta
given_date = datetime(2023, 4, 6)
print("Given date")
print(given_date)
days_to_subtract = 7
res_date = given_date - timedelta(days=days_to_subtract)
print("New Date")
print(res_date)

print()
# ----------------------------------------------------------------------------------------------------------------
''' Exercise 4: Print a date in a the following format
Given:
given_date = datetime(2023, 4, 6)
Expected output:
Thursday 06 April 2023 '''

print("Solution 4:")
from datetime import datetime
given_date = datetime(2023, 4, 6)
print("Given date is")
print(given_date.strftime('%A %d %B %Y'))

print()
# ----------------------------------------------------------------------------------------------------------------
''' Exercise 5: Find the day of the week of a given date
Given:
given_date = datetime(2023, 4, 7)
Expected output:
Friday '''

print("Solution 5:")
from datetime import datetime
given_date = datetime(2023, 4, 7)
# to get weekday as integer
print(given_date.today().weekday())
# To get the english name of the weekday
print(given_date.strftime('%A'))

print("Solution 2 using calendar module")
import calendar
from datetime import datetime
given_date = datetime(2023, 4, 7)
weekday = calendar.day_name[given_date.weekday()]
print(weekday)

print()
# ----------------------------------------------------------------------------------------------------------------
''' Exercise 6: Add a week (7 days) and 12 hours to a given date
Given:
# 2023-03-22 10:00:00
given_date = datetime(2023, 3, 22, 10, 0, 0)
Expected output:
2023-03-29 22:00:00 '''

print("Solution 6:")
from datetime import datetime, timedelta
given_date = datetime(2023, 3, 22, 10, 00, 00)
print("Given date")
print(given_date)
days_to_add = 7
res_date = given_date + timedelta(days=days_to_add, hours=12)
print("New Date")
print(res_date)

print()
# ----------------------------------------------------------------------------------------------------------------
''' Exercise 7: Print current time in milliseconds '''

print("Solution 7:")
import time
milliseconds = int(round(time.time() * 1000))
print(milliseconds)

print()
# ----------------------------------------------------------------------------------------------------------------
''' Exercise 8: Convert the following datetime into a string
Given:
given_date = datetime(2023, 2, 25)
Expected output:
"2023-02-25 00:00:00" '''

print("Solution 8:")
from datetime import datetime
given_date = datetime(2023, 2, 25)
string_date = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(string_date)

print()
# ----------------------------------------------------------------------------------------------------------------
''' Exercise 9: Calculate the date 4 months from the current date
Given:
# 2023-02-25
given_date = datetime(2020, 2, 25).date()
Expected output:
2023-06-25 '''

print("Solution 9:")
from datetime import datetime
from dateutil.relativedelta import relativedelta
# 2023-02-25
given_date = datetime(2023, 2, 25).date()
months_to_add = 4
new_date = given_date + relativedelta(months=+ months_to_add)
print(new_date)

print()
# ----------------------------------------------------------------------------------------------------------------
''' Exercise 10: Calculate number of days between two given dates
Given:
# 2023-02-25
date_1 = datetime(2023, 2, 25)
# 2023-09-17
date_2 = datetime(2023, 9, 17)
Expected output:
205 days '''

print("Solution 10:")
from datetime import datetime
# 2023-02-25
date_1 = datetime(2023, 2, 25).date()
# 2023-09-17
date_2 = datetime(2023, 9, 17).date()
delta = None
if date_1 > date_2:
    print("date_1 is greater")
    delta = date_1 - date_2
else:
    print("date_2 is greater")
    delta = date_2 - date_1
print("Difference is", delta.days, "days")

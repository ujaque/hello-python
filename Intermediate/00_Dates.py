
from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta

now = datetime.now()

print(now.day)
print(now.hour)
print(now.minute)
print(now.year)
print(now.month)
print(now.second)

timestamp = now.timestamp()

print(timestamp)

year_2023 = datetime(2023, 1, 1)


def printDate(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

printDate(year_2023)

## Time

current_time = time(21, 6, 0)

print("time")
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

## Date

current_date_original = date.today()
print("date")
print(current_date_original.year)
print(current_date_original.month)
print(current_date_original.day)


current_date_modified = date(current_date_original.year +1, current_date_original.month, current_date_original.day)

print(current_date_modified.year)
print(current_date_modified.month)
print(current_date_modified.day)

## timedelta

print(type(current_date_original))
print(type(current_date_modified))

diff = current_date_modified - current_date_original

print(diff)


start_timedelta = timedelta(200,100,100, weeks=10)
end_timedelta = timedelta(300,100,100, weeks=13)

print(end_timedelta-start_timedelta)
print(end_timedelta+start_timedelta)




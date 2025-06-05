import sys
import datetime

day_dict = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
            }
month, day = list(map(int, sys.stdin.readline().split()))
temp = datetime.date(2009, day, month)

print(day_dict[temp.weekday()])
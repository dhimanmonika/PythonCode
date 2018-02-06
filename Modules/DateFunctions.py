"""Date class"""

import datetime

print("\n Date Arithmetics\n")

today = datetime.date.today()
print ('Today    :', today)

one_day = datetime.timedelta(days=1)
print('One day  :', one_day)

yesterday = today - one_day
print('Yesterday:', yesterday)

tomorrow = today + one_day
print ('Tomorrow :', tomorrow)

print ('tomorrow - yesterday:', tomorrow - yesterday)
print ('yesterday - tomorrow:', yesterday - tomorrow)



print("formatting ")
format = "%a %b %d %H:%M:%S %Y"

today = datetime.datetime.today()
print ('ISO     :', today)

s = today.strftime(format)
print('strftime:', s)

d = datetime.datetime.strptime(s, format)
print ('strptime:', d.strftime(format))
"datetime module "

import datetime

print("Time class\n")
t=datetime.time(1,2,4)
print("time : ",t)
print("hour :",t.hour)
print("minutes :",t.minute)
print("seconds :",t.second)
print("microseconds :",t.microsecond)


print("\npassing values for microseconds to time : 1, 0, 0.1, 0.6")
for m in [ 1, 0, 0.1, 0.6 ]:
    try:
        print('%02.1f :' % m, datetime.time(0, 0, 0, microsecond=m))
    except TypeError:
        print ('ERROR:float value not acceptable for microseconds')



print("\nDate class\n")
d=datetime.date.today()
print("today's date :",d)
print("month :",d.month)
print("day :",d.day)
print("year :",d.year)


print("\nreplacing year of date :")
d1 = datetime.date(2008, 3, 12)
print ('before replacement date:', d1)


d2 = d1.replace(year=2009)
print ('after replacement date :', d2)

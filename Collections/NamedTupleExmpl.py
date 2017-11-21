"""Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index."""

from collections import namedtuple
import csv


Point =namedtuple('Point',['x','y']) # intializing namedtuple
p=Point(10,20)   # assigning values
print(p.x)       # accesing using name


myrecord =namedtuple('myrecord','name,language,age,gender')

for emp in map(myrecord._make, csv.reader(open("input.csv", "r"))):
    print(emp.name, emp.language)



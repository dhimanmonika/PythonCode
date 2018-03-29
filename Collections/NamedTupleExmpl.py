"""Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index."""

from collections import namedtuple
import csv


Point =namedtuple('Point',['x','y']) # intializing namedtuple
p=Point(10,20)   # assigning values
print(p.x)       # accesing using name


myrecord =namedtuple('myrecord','name,language,age,gender')

for emp in map(myrecord._make, csv.reader(open("input.csv", "r"))):
    print(emp.name, emp.language)

"""
1. _make() :- This function is used to return a namedtuple() from the iterable passed as argument.
2. _asdict() :- This function returns the OrdereDict() as constructed from the mapped values of namedtuple().
3. using “**” (double star) operator :- This function is used to convert a dictionary into the namedtuple().
"""
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# initializing iterable
li = ['Manjeet', '19', '411997']

# initializing dict
di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

# using _make() to return namedtuple()
print("The namedtuple instance using iterable is  : ")
print(Student._make(li))

# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is  : ")
print(S._asdict())

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is  : ")
print(Student(**di))
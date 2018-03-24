"""
Exception handling :
"""
# import module sys to get the type of exception
import sys

randomList = ['a', 2, 0]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        print("The reciprocal of", entry, "is", r)
        print()
        continue
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()




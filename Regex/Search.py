"""" Lets use a regular expression to match a date string
 in the form of Month name followed by day number"""
import re

def useSearch(data):
    match=re.search(r'([a-zA-Z]+)\s\d+',data)
    if(match):
        print(match.group())
    else:
        print("not found")

if __name__=="__main__":
    data = "Today is December 1"
    useSearch(data)
    data1="this doesnt contain date"
    useSearch(data1)


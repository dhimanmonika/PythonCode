"""A regular expression in a programming language is a special text string used for describing a search pattern.
It is extremely useful for extracting information from text such as code, files, log, spreadsheets or even documents. """

import re

example="this is regular expression example"

text="expression"

emails='abc.gs@gmail.com ,' \
       'def@yaahoo.in,' \
       'fdgdhru'

result1= re.findall(r"^\w+",example)
print(result1)  # finding first alphanumeric in the string

result2 =re.split(r"\s",example)
print(result2)  #splitting on the basis of space

result3=re.split(r's',example)
print(result3)  #split on the basis of s

result4=re.match("(t\w+)",example)
print(result4)  #match the given pattern.

result5= re.search(text,example)
print(result5) # search pattern in given string

result6=re.findall(r'[\w\.-]+@[\w\.-]+',emails)
print(result6) # pattern matching

result7 = re.findall(r"^\w", emails, flags = re.MULTILINE)
print(result7) #

""" re.search() -> returns object if matched else none
    re.match() : This function attempts to match pattern to whole string. The re.match function returns a match object
     on success, None on failure. 
"""
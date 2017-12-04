"""You are given a string .
Your task is to find the indices of the start and end of string in ."""
import re

S,k=input(),input()

results= list(map(lambda x:(x.start(1),x.end(1)-1),re.finditer(r"(?=(%s))"%k,S)))

if results:
    for x in results:
        print(x)
else:
    print("(-1, -1")
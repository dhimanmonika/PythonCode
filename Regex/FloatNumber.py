"""You are given a string .
Your task is to verify that is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

Number can start with +, - or . symbol.
You are given a string .
Your task is to verify that is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

Number can start with +, - or . symbol.
For example:
✔+4.50
✔-1.0
✔.5
✔-.7
✔+.4
✖ -+4.5

Number must contain at least decimal value.
For example:
✖ 12.
✔12.0

Number must have exactly one . symbol.
Number must not give any exceptions when converted using .
Number must contain at least decimal value.
For example:
✖ 12.
✔12.0

Number must have exactly one . symbol.
Number must not give any exceptions when converted using ."""





import re

T=int(input())
for i in range (T):
    N=str(input())
    match=re.search(r'[-+]?[0-9]*\.+?[0-9]+',N)
    if(match):
        s=match.start()
        e=match.end()
        if (s==0 and e==len(N)):
            print("True")
        else :
            print("False")
    else :
        print("False")
"""
A valid mobile number is a ten digit number starting with a or .
For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.
"""


import re
N= int(input())
for i in range(N):
    if( re.match(r'[789]\d{9}$', input())):
        print("YES")
    else:
        print("NO")

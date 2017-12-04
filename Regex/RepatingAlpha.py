"""You are given a string .
Your task is to find the first occurrence of an alphanumeric character in (read from left to right) that has consecutive repetitions."""

import re
S=input()
m=re.search(r'([a-zA-Z0-9])\1{1,}',S)
if (m):
    print(m.group(1))
else:
    print("-1")
"""You are given lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.
Sample Input

11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}

Sample Output
#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff
"""

import re
N=int(input())
for i in range(N):
    a=re.findall(r'(?<!^)[\s:](#[\da-fA-F]{3,6})',input())
    if (a):
        for j in a:
            print(j)
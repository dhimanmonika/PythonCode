"""
The function reduce(func, seq) continually applies the function func() to the sequence seq. It returns a single value.
"""
from functools import reduce

l=[1,2,6,3,4,9,7,23,66]
print("original list ",l)

# find the maximum number from the list

max=reduce(lambda x,y:x if (x>y) else y,l)

print("the max value from the list ",max)

#find sum of elements of the list

sum=reduce(lambda x,y:x+y,l)
print("the sum of all the elements of list ",sum)
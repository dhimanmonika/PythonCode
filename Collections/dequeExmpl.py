""" Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction."""

from collections import deque

d=deque('abc')

d.append('d') # append to right
print(d)

d.appendleft('z')#append to left side
print(d)

d.pop() #return rightmost element
print(d)

d.popleft() # return the leftmost element
print(d)

d.reverse() # reverse the dict
print(d)

d.extend('ghi') # add multiple elements at a time
print(d)

d.rotate(1) #rotate right
print(d)

d.rotate(-1) #rotate left
print(d)

d.clear()  # emplty the deque
print(d)





from math import pi

def circle_area(r):
    if type(r) not in[int, float]:
        raise TypeError("radius should be integer or float")
    if r<0:
        raise ValueError('cannot find area with negative radius')
    return pi*r*r


res=circle_area("abd")
print(res)
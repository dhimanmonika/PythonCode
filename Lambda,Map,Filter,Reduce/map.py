"""The map() function in Python takes in a function and a list.

The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item"""


def square(n):
    return n*n


sq=map(lambda x:square(x),[1,2,3,4,5])
print(list(sq))


"""or 
sq=map(lambda x:x*x,[1,2,3,4,5])
print(list(sq))
"""
""" decorator to make division check"""


# for two parameters
def divisionCheck(fun):
    def inner(a,b):
        print(" divide : ",a,"and ",b)
        if b==0:
            return "cannot divide by zero "
        return fun(a,b)
    return inner

@divisionCheck
def divide(a,b):
    return a/b



#using args and kwargs
"""def divisionCheck(fun):
    def inner(*args,**kwargs):
        a,b=(args)
        if b==0:
            return "cannot divide by zero "
        return fun(a,b)
    return inner
@divisionCheck
def divide(a,b):
    return a/b"""


print(divide(4,0))

"""Multiple decorators can be chained in Python.

This is to say, a function can be decorated multiple times with different (or same) decorators. We simply place the decorators above the desired function."""

def star(fun):
    def inner(*args,**kwargs):
        print("*"*30)
        print("i am decorating with stars")
        fun(*args,**kwargs)
        print("*"*30)
    return inner

def percent(fun):
    def inner(*args,**kwargs):
        print("%"*30)
        print("i am decorating with percentage")
        fun(*args,**kwargs)
        print("%"*30)
    return inner


@star
@percent
def ordinary(msg):
   print(msg)


if __name__=="__main__":
    msg="hi i am ordinary function"
    ordinary(msg)



"""output:
******************************
i am decorating with stars
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
i am decorating with percentage
hi i am ordinary function
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************
"""
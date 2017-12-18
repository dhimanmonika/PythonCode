"""--------------------DECORATORS--------------------------

A decorator takes in a function, adds some functionality and returns it.

Such function that take other functions as arguments are also called higher order functions."""

def pretty(fun):
    def inner():
        print("hi i am pretty decorator")
        fun()
    return inner

@pretty
def ordinary():
    print("hi i am ordinary function.But decorator makes me pretty")


ordinary()
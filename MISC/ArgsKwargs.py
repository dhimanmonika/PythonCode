"""The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function.
It is used to pass a non-keyworded, variable-length argument list."""


def testify(arg1, *argv):
    print("first argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)



testify('Hello', 'Welcome', 'to', 'GeeksforGeeks')


"""The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. 
We use the name kwargs with the double star. 
The reason is because the double star allows us to pass through keyword arguments (and any number of them)."""

def hello(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print ("%s == %s" %(key, value))

hello(name="GeeksforGeeks")
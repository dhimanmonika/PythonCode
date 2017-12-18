#calculate the time taken by the function


def CalTime(fun):
    import time
    def inner(*args,**kwargs):
        print("calculating time taken by function {}".format(fun.__name__))
        t1=time.time()
        fun(*args,**kwargs)
        t2=time.time()
        print("time taken by the function {} is {} seconds ".format(fun.__name__,t2-t1))
    return inner



@CalTime
def square(n):
    print([x*x for x in range(n)])


square(10)


"""generator to generate fibonacci sequence"""
def fib(n):
    a,b=0,1

    while a<n:
        yield a
        a,b=b,a+b


for item in fib(50):
    print(item)

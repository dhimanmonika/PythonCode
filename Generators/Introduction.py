"""
It is fairly simple to create a generator in Python. It is as easy as defining a normal function with yield statement instead of a return statement.

If a function contains at least one yield statement it becomes generator.

The difference is that, while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successive calls.
"""

def gen(n):
    print("first yield statement")
    yield n+1

    print("second yield statement")
    yield n + 2

    print("third yield statement")
    yield n + 3


"""a=gen(5)

print(next(a))
print(next(a))
print(next(a))"""

for item in gen(5):
    print(item)
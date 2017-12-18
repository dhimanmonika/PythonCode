"""
A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
Decorators in Python make an extensive use of closures as well.
"""

""" inner fun multiplier  can access the value of n. times3 is a closure function"""
def outer_multiplier(n):
    def inner_multiplier(x):
        return n*x
    return inner_multiplier



times3=outer_multiplier(3)

print(times3(9))




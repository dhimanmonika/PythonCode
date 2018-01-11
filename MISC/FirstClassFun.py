"""
    A function is an instance of the Object type.
    You can store the function in a variable.
    You can pass the function as a parameter to another function.
    You can return the function from a function.
    You can store them in data structures such as hash tables, lists, …
"""

# passing function as an argument

def loud(text):
    return text.upper()

def slow(text):
    return text.lower()


def greet(fun):
    greeting=fun("Hi !!! good morning")
    print(greeting)

greet(loud)
greet(slow)
"""The __init__ method is run as soon as an object of a class is instantiated (i.e. created).
The method is useful to do any initialization (i.e. passing initial values to your object) you want to do with your object.
Notice the double underscores both at the beginning and at the end of the name."""

class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('PythonCoder')
p.say_hi()
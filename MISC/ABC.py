"""Abstract classes are classes that contain one or more abstract methods. An abstract method is a method that is declared,
 but contains no implementation.
 Abstract classes may not be instantiated, and require subclasses to provide implementations for the abstract methods. """


from abc import ABC ,abstractmethod

class Basic(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def do_something(self):
        print("This is written in basic class")


class Child(Basic):
    def  do_something(self):
        super(Child,self).do_something()
        print("This is written in Child class",self.value)


class Child1(Basic):
    def  do_something(self):
        print("This is written in Child 1  class",self.value)


c=Child("bye")
c.do_something()
c1=Child1("tata")
c1.do_something()


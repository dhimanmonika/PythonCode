from abc import ABC,abstractmethod


class AbstarctClass(ABC):
    def __init__(self,value):
        self.value=value

    @abstractmethod
    def dosomething(self):
        pass

class Addition(AbstarctClass):
    def dosomething(self):
        return self.value+42

class Multiplication(AbstarctClass):
    def dosomething(self):
        return self.value*42


x = Addition(10)
y = Multiplication(10)
print(x.dosomething())
print(y.dosomething())


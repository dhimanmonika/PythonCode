"""Class functions that begins with double underscore __ are called special functions in Python. """
#operator overloading



class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return Point(x,y)



P=Point(2,3)
P1=Point(3,2)
P2=P+P1

print(P2)
"""Class variables are shared - they can be accessed by all instances of that class.
There is only one copy of the class variable and when any one object makes a change to a class variable,
 that change will be seen by all the other instances.

Object variables are owned by each individual object/instance of the class.
In this case, each object has its own copy of the field i.e. they are not shared and are not related in any way to the
field by the same name in a different instance."""

class Robot:
    population=0 # class variable

    def __init__(self,name):
        self.name=name
        print("intializing {}".format(self.name))
        Robot.population+=1

    def die(self):
        print("{} is being destroyed".format(self.name))
        Robot.population-=1

    def sayhi(self):
        print("my master calls me {}".format(self.name))

    @classmethod
    def howmany(cls):
        print("we have {} robots left".format(cls.population))


robo1=Robot("robo1")
robo1.sayhi()
Robot.howmany()


robo2=Robot("robo2")
robo2.sayhi()
Robot.howmany()

print("Robots work is done , lets finish them ")
robo1.die();
robo2.die();
Robot.howmany()
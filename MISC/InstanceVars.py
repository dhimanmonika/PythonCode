"""
Class vs. Instance

"""



class Person:
    def __init__(self,initialAGE):
        if initialAGE<0:
            self.age=0
            print("Age is invalid setting it to 0")
        else :
            self.age =initialAGE

    def HowOldAm(self):
        if self.age<13:
            print("you are young bcoz your age is",self.age)
        elif self.age in range(13,19):
            print("you are teenager bcoz your age is",self.age)
        else :
            print("you are old bcoz your age is",self.age)






age=2
p=Person(age)
p.HowOldAm()

age=-2
p=Person(age)
p.HowOldAm()

        

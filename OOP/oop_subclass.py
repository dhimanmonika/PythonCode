"""One of the major benefits of object oriented programming is reuse of code and one of the ways this is achieved is through the inheritance mechanism. Inheritance can be best imagined as implementing a type and subtype relationship between classes."""

class SchoolMember:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("initialising the school memeber {} ".format(self.name))

    def tell(self):
        print("name : '{}'  age: '{}'".format(self.name,self.age))

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Alison', 40, 30000)
s = Student('Jane', 25, 75)

# prints a blank line
print()

members = [t, s]
for member in members:
    # Works for both Teachers and Students
    member.tell()
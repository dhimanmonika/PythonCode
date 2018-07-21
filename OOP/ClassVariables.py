class Employee:

    num_of_employee=0
    raise_amt=1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_employee+= 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)



emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)


emp_1.raise_amt=1.05

print("number of employee" ,Employee.num_of_employee)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
print(Employee.raise_amt)
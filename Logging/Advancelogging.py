import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
File_handler=logging.FileHandler('employee.Log')
File_handler.setFormatter(formatter)
logger.addHandler(File_handler)




class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        print('{} {}'.format(self.fname, self.lname))

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname,self.lname)

    @property
    def fullname(self):
         return '{} {}'.format(self.fname,self.lname)

emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')


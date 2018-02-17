import unittest
import Employee

class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass\n')

    @classmethod
    def tearDownClass(cls):
        print('TeardownClass\n')

    def setUp(self):
        print("SetUp\n")
        self.emp_1 = Employee('monika', 'dhiman', 50000)
        self.emp_2 = Employee('nitish', 'goswami', 60000)

    def tearDown(self):
        print("TearDown\n")


    def test_email(self):
        print("test email\n")
        self.assertEqual(self.emp_1.email,'monika.dhiman@gmail.com')
        self.assertEqual(self.emp_2.email,'nitish.goswami@gmail.com')

        self.emp_1='john'
        self.emp_2='smith'

        self.assertEqual(self.emp_1.email, 'john.dhiman@gmail.com')
        self.assertEqual(self.emp_2.email, 'smith.goswami@gmail.com')

    def test_fullname(self):
        print("test fullname\n")
        self.assertEqual(self.emp_1.fullname, 'monika dhiman')
        self.assertEqual(self.emp_2.fullname, 'nitish goswami')

        self.emp_1 = 'john'
        self.emp_2 = 'smith'

        self.assertEqual(self.emp_1.fullname, 'john dhiman')
        self.assertEqual(self.emp_2.fullname, 'smith goswami')


if __name__ == '__main__':
    unittest.main()
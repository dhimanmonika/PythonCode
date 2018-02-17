import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result=calc.add(10,5)
        self.assertEqual(result,15)

    def test_multiply(self):
        result = calc.multiply(10, 5)
        self.assertEqual(result,50)

    def test_subtract(self):
        result = calc.subtract(10, 5)
        self.assertEqual(result,5)

    def test_divide(self):
        result=calc.divide(10,5)
        self.assertEqual(result,2)

        #self.assertRaises(ValueError,calc.divide,10,2)
        with self.assertRaises(ValueError):
            calc.divide(10,0)


if __name__=='__main__':
    unittest.main()






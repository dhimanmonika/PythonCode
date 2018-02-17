

import unittest
from Circle import circle_area
from math import pi

class TestAreaCircle(unittest.TestCase):

    def test_Area(self):
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0),0)

    def test_values(self):
        self.assertRaises(ValueError,circle_area,-1)

    def test_types(self):
        self.assertRaises(TypeError,circle_area,True)
        self.assertRaises(TypeError, circle_area,1+2j)




if __name__=='__main__':
    unittest.main()
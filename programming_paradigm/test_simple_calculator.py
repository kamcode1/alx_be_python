import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()


    def test_addition(self):
        self.assertEqual(self.calc.add(2,3), 5)
        self.assertEqual(self.calc.add(-1,1), 0)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)
    
    def test_multiply(self):     
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_divisionzero(self):
        self.assertIsNone(self.calc.divide(6, 0))

if __name__=='__main__':
    unittest.main()
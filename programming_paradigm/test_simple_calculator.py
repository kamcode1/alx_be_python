import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()


    def test_add(self):
        result = self.calc.add(2,3)
        self.assertEqual(result, 5)

    def test_sub(self):
        result = self.calc.subtract(2, 3)
        self.assertEqual(result, -1)
    
    def test_multiply(self):     
        result = self.calc.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = self.calc.divide(6, 3)
        self.assertEqual(result, 2)

    def test_divisionzero(self):
        result = self.calc.divide(6, 0)
        self.assertIsNone(result)

if __name__=='__main__':
    unittest.main()
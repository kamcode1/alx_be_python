import unittest
from simple_calculator import SimpleCalculator

class test(unittest.TestCase):
    def test_add(self):
        self.a = 2
        self.b = 3 
        result = self.a + self.b
        self.assertEqual(result, 5)

    def test_sub(self):
        self.a = 2
        self.b = 3 
        result = self.a - self.b
        self.assertEqual(result, -1)
    
    def test_multiply(self):
        self.a = 2
        self.b = 3 
        result = 2 * 3
        self.assertEqual(result, 6)

    def test_divide(self):
        self.a = 6
        self.b = 3 
        result = self.a / self.b
        self.assertEqual(result, 2)
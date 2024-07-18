import unittest
import square

class Testsquare(unittest.TestCase):

    def test_sq(self):
        result = square.sq(5)
        self.assertEqual(result, 25)


if __name__ == '__main__':
    unittest.main()
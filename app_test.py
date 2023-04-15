import unittest
from my_app import addition, subtraction, multiplication, division

class TestMyApp(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)

    def test_subtraction(self):
        self.assertNotEqual(subtraction(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 4) == 11)

    def test_division(self):
        self.assertEqual(division(10, 2), 6)

    def test_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, division, 10, 0)

if __name__ == '__main__':
    unittest.main()


import unittest
from my_app import *

class TestMyApp(unittest.TestCase):
    
    # Successful Test Case 1: addition() function 
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
    
    # Successful Test Case 2: subtraction() function
    def test_subtraction(self):
        self.assertNotEqual(subtraction(5, 2), 2)
        
    # Failed Test Case 3: multiplication() function
    def test_multiplication(self):
        self.assertTrue(multiplication(3, 4) == 11)
        
    # Failed Test Case 4: division() function
    def test_division(self):
        self.assertEqual(division(10, 2), 6)
        
    # Successful Test Case 5: division() function 
    def test_division_by_zero(self):
        with self.assertRaises(Exception): division(10, 0)

if __name__ == '__main__':
    unittest.main()


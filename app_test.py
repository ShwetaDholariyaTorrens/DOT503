import unittest
from test import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_palindromes(self):
        # positive test cases (palindromes)
        self.assertTrue(is_palindrome("racecar"))     # correct
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))    # correct
        self.assertTrue(is_palindrome("Was It A Rat I Saw"))           # correct

    def test_non_palindromes(self):
        # negative test cases (not palindromes)
        self.assertFalse(is_palindrome("hello"))      # correct
        self.assertFalse(is_palindrome("Python Programming"))           # correct    


if __name__ == '__main__':
    unittest.main()

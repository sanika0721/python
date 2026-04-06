"""
Unit tests for utility functions.
"""

import unittest
from utils import greet, add, is_palindrome


class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_greet_empty(self):
        self.assertEqual(greet(""), "Hello, !")


class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, 1), 0)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.1, 2.2), 3.3, places=5)


class TestIsPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("never odd or even"))


if __name__ == "__main__":
    unittest.main()
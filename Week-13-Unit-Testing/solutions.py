# Week 13 Solutions
import unittest

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def is_palindrome(s):
    return s==s[::-1]

class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
    def test_subtract(self):
        self.assertEqual(subtract(5,3),2)
    def test_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))

if __name__=="__main__":
    unittest.main()

import unittest
from prime import is_prime

class TestPrime(unittest.TestCase):

    def test_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(14))
        self.assertFalse(is_prime(15))
        
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            is_prime(-1)
            
    def test_zero_and_one(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        
    def test_large_input(self):
        self.assertTrue(is_prime(7907)) # a prime number
        self.assertFalse(is_prime(7908)) # not a prime number

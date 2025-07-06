import unittest
from hello import greet, factorial

class TestHello(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Mark"), "Hello, Mark!")
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("") , "Hello, !")

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

if __name__ == "__main__":
    unittest.main()

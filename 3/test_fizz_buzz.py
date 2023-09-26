import unittest
from fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_15(self):
        self.assertEqual(fizz_buzz(45), 'FizzBuzz')
        
    def test_3(self):
        self.assertEqual(fizz_buzz(12), 'Fizz')
        
    def test_5(self):
        self.assertEqual(fizz_buzz(25), 'Buzz')
        
    def test_str(self):
        self.assertEqual(fizz_buzz(11), '11')
        
        
if __name__ == '__main__':
    unittest.main()
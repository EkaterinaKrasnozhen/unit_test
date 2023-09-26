import unittest
from first_last6 import first_last6


class TestFirstLast6(unittest.TestCase):
    def test_first6(self):
        self.assertTrue(first_last6([6,2,4]))
        
    def test_last6(self):
        self.assertTrue(first_last6([0,2,6]))
        
    def test_no6(self):
        self.assertFalse(first_last6([0,2,1]))
        
    def test_botht6(self):
        self.assertTrue(first_last6([6,2,6]))
        
        
if __name__ == '__main__':
    unittest.main()
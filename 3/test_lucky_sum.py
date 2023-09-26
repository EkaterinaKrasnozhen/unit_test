import unittest
from lucky_sum import lucky_sum


class TestLuckySum(unittest.TestCase):
    def test_lucky_sum(self):
        self.assertEqual(lucky_sum(3,3,3), 9)
        
    def test_lucky_sum13(self):
        self.assertEqual(lucky_sum(3,3,13), 6)
        self.assertEqual(lucky_sum(3,13,3), 6)
        self.assertEqual(lucky_sum(13,3,3), 6)
        
    def test_lucky_sum_two13(self):
        self.assertEqual(lucky_sum(3,13,13), 3)
        self.assertEqual(lucky_sum(13,3,13), 3)
        self.assertEqual(lucky_sum(13,13,3), 3)
        
    def test_lucky_sum_no13(self):
        self.assertEqual(lucky_sum(3,2,2), 7)
        
    def test_lucky_all13(self):
        self.assertRaisesRegex(ValueError, 'Все числа равны 13', lucky_sum, num1=13, num2=13, num3=13)
          
        
if __name__ == '__main__':
    unittest.main()
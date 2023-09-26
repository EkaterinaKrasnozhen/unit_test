import unittest
from calc_discount import calculate_discount


class TestFizzBuzz(unittest.TestCase):
    def test_calc_discount_raise_sum_minus(self):
        self.assertRaisesRegex(RuntimeError, "Скидка должна быть больше 0", calculate_discount, sum=-1, discount=1) 
        
    def test_calc_discount_raise_discount_minus(self):
        self.assertRaisesRegex(RuntimeError, "Скидка должна быть больше 0", calculate_discount, sum=1, discount=-1)
        
    def test_calc_discount_asserError_discount_more100(self):
        self.assertRaisesRegex(AssertionError, "скидка должна быть в пределах от 0 до 100", calculate_discount, sum=100, discount=1011) 
    
    def test_calc_discount(self):
        self.assertEqual(calculate_discount(100, 10), 90)    
        
        
if __name__ == '__main__':
    unittest.main()
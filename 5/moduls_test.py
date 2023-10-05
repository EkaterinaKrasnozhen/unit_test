# Задание №1
# Создайте два модуля. Первый модуль генерирует список случайных чисел. Второй модуль находит
# максимальное число в этом списке.
# Вам нужно сначала написать юнит-тесты для каждого модуля, затем написать интеграционный
# тест, который проверяет, что оба модуля работают вместе правильно

import unittest
from random_list import get_randomList
from max_num import get_max_num


class TestRnd(unittest.TestCase): # проверяем две функции и проверяем их, интеграционный тест
    def test_rnd(self):
        lst = get_randomList(10)
        self.assertEqual(get_max_num(lst), sorted(lst)[-1])
        
        
if __name__ == '__main__':
    unittest.main()
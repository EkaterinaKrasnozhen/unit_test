# Задание №2
# У вас есть два класса - UserService и UserRepository. UserService использует UserRepository для
# получения информации о пользователе. Ваша задача - написать интеграционный тест, который
# проверяет, что UserService и UserRepository работают вместе должным образом.

import unittest
from unittest.mock import Mock
from user_repo import UserRepository
from user_service import UserService


class TestPayment(unittest.TestCase):
    def setUp(self) -> None:
        self.user_service = UserService(UserRepository())
        
    def test_user(self):
        self.assertEqual(self.user_service.get_user_name(3), 'User 3')
        
        
if __name__ == '__main__':
    unittest.main()
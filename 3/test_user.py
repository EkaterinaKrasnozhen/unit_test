# Задание №6
# Разработайте класс User с методом аутентификации по логину и паролю. Метод должен возвращать true, если
# введенные логин и пароль корректны, иначе false. Протестируйте все методы

import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User('login', 'password')
        
    def test_success_authentificate(self):
        self.user.authentificate(self.user.login, self.user.password)
        self.assertTrue(self.user.is_authentificate)

    def test_wrong_pass_authentificate(self):
        self.user.authentificate(self.user.login, '')
        self.assertFalse(self.user.is_authentificate)
        
    def test_wrong_login_authentificate(self):
        self.user.authentificate('', self.user.password)
        self.assertFalse(self.user.is_authentificate)
        
    def test_wrong_pass_login_authentificate(self):
        self.user.authentificate('', '')
        self.assertFalse(self.user.is_authentificate)
        
        
if __name__ == '__main__':
    unittest.main()
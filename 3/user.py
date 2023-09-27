class User:
    def __init__(self, login: str, password: str) -> None:
        self._login = login
        self._password = password
        self._is_authentificate = False
    
    def authentificate(self, login: str, password: str) -> bool:
        self._is_authentificate = self._login == login and self._password == password
        return self._is_authentificate
    
    @property
    def login(self):
        return self._login
    
    @property
    def password(self):
        return self._password
    
    @property
    def is_authentificate(self):
        return self._is_authentificate
    

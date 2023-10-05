from user_repo import UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self._user_repo = user_repo
        
    def get_user_name(self, user_id: int) -> str  :
        return self._user_repo.get_user_by_id(user_id)  
    
    

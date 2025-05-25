from typing import List, Optional
from uuid import UUID
from src.models.user import User
from src.services.users_storage import UserStorage

class UserService(UserStorage):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserService, cls).__new__(cls)
            cls._instance.users = []
        return cls._instance

    def create_user(self, user: User) -> User:
        self.users.append(user)
        return user

    def get_users(self) -> List[User]:
        return self.users

    def get_user(self, user_id: UUID) -> Optional[User]:
        return next((user for user in self.users if user.id == user_id), None)

    def update_user(self, user_id: UUID, updated_user: User) -> Optional[User]:
        for index, user in enumerate(self.users):
            if user.id == user_id:
                self.users[index] = updated_user
                return updated_user
        return None

    def delete_user(self, user_id: UUID) -> bool:
        for index, user in enumerate(self.users):
            if user.id == user_id:
                del self.users[index]
                return True
        return False

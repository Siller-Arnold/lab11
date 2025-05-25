from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional
from src.models.user import User

class UserStorage(ABC):
    """Abstract class for user storage (in-memory or database)."""
    @abstractmethod
    def create_user(self, user: User) -> User:
        pass
    @abstractmethod
    def get_user(self, user_id: UUID) -> Optional[User]:
        pass
    @abstractmethod
    def get_users(self) -> List[User]:
        pass
    @abstractmethod
    def update_user(self, user_id: UUID, updated_user: User) -> Optional[User]:
        pass
    @abstractmethod
    def delete_user(self, user_id: UUID) -> bool:
        pass
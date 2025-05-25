from functools import lru_cache
from fastapi import Depends
from sqlalchemy.orm import Session
from config import get_settings
from src.db.database import get_db
from src.services.users_storage import UserStorage
from src.services.users_service import UserService
from src.db.users_repository import UsersRepository

@lru_cache
def get_user_storage(db: Session = Depends(get_db)) -> UserStorage:
    """Returns the appropriate user storage mechanism based on TestMode setting."""
    if get_settings().TEST_MODE:
        return UserService()  # Use in-memory service
    return UsersRepository(db)  # Use database repository

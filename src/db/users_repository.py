from typing import List, Optional
from uuid import UUID
from sqlalchemy.future import select
from src.db.entities import User
from src.models.user import User as UserModel
from sqlalchemy.orm import Session
import uuid

from src.services.users_storage import UserStorage

class UsersRepository(UserStorage):
    """Repository for user data access."""

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, userModel: UserModel) -> UserModel:
        """Create a new user."""
        user = User(
            id=str(uuid.uuid4()),
            name=userModel.name,
            email=userModel.email,
            age=userModel.age
        )
        self.db.add(user) 
        self.db.commit()
        self.db.refresh(user)   
        return UserModel(
            id=str(user.id),
            name=user.name,
            email=user.email,
            age=user.age
        )

    def get_user(self, user_id: UUID) -> Optional[UserModel]:
        """Retrieve a user by ID."""
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            return UserModel(
                id=str(user.id),
                name=user.name,
                email=user.email,
                age=user.age
            )
        return None

    def get_users(self) -> List[UserModel]:
        """Retrieve all users."""
        users = self.db.query(User).all()
        return [
            UserModel(id=str(u.id), name=u.name, email=u.email, age=u.age)
            for u in users
            ]

    def update_user(self, user_id: UUID, updated_user: UserModel) -> Optional[UserModel]:
        """Update user details."""
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            user.name = updated_user.name
            user.email = updated_user.email
            user.age = updated_user.age
            self.db.commit()
            self.db.refresh(user)
            return UserModel(
                id=str(user.id),
                name=user.name,
                email=user.email,
                age=user.age
            )
        return None

    def delete_user(self, user_id: UUID) -> bool:
        """Delete a user by ID."""
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False
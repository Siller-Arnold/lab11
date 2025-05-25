# Define Base class for ORM models
import uuid
from sqlalchemy import UUID, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "py_khnu"}
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,unique=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
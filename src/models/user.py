#from dataclasses import Field
from uuid import uuid4
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    id: str = str(uuid4())
    name: str = Field(..., min_length=2, max_length=100, description="Name cannot be empty.")
    email: EmailStr = Field(..., description="E-Mail must have a guilty format.")
    age: int = Field(..., ge=0, le=120, description="Age must be between 0 and 120.")

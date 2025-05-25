from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from src.models.user import User
from src.services.user_service import user_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=User, operation_id="create_new_user", summary="Add a new user",
             description="This endpoint allows you to create a new user and store them in the system.")
def create_user(user: User):
    return user_service.create_user(user)

@router.get("/", response_model=list[User], operation_id="get_all_users", summary="Show all users",
            description="Retrieves a list of all registered users in the system.")
def get_users():
    return user_service.get_users()

@router.get("/{user_id}", response_model=User, operation_id="get_defined_user", summary="Show user data",
            description="Retrieves a specific user using their unique ID. If the user is not found, a 404 error is returned.")
def get_user(user_id: UUID):
    user = user_service.get_user(str(user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User, operation_id="change_user_data", summary="Update user data",
            description="Allows you to update an existing user's details using their unique ID.")
def update_user(user_id: UUID, updated_user: User):
    user = user_service.update_user(str(user_id), updated_user)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}", operation_id="delete_user", summary="Delete a user", 
               description="Deletes a user from the system using their unique ID. If the user does not exist, a 404 error is returned.")
def delete_user(user_id: UUID):
    if not user_service.delete_user(str(user_id)):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

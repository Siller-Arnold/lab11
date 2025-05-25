import logging
import sys
from fastapi import FastAPI, Request, HTTPException, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from config import get_settings
from src.db.database import get_db
from src.dependencies import get_user_storage
from src.services.users_storage import UserStorage
from src.models.user import User

# Logger initialisieren
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 🌟 API definition with OpenAPI metadata
app = FastAPI(
    title="User Management API",
    description="With this API you can create, get, change and delete user data.",
    contact={
        "name": "Olena Siller",
        "email": "olenasiller@student.karazin.ua",
    },
    openapi_tags=[{"name": "Users", "description": "Operations with users"}] 
)

# 🔵 API-Info-Endpoint
@app.get("/info", tags=["Info"], description="Show information about the system.")
def get_info():
    return {
        "name": "API for User Management",
        "description": "API for management of user data.",
        "contact": {
            "name": "API Support - Olena Siller",
            "email": "olenasiller@student.karazin.ua"
        }
    }

# 🔹 Benutzer erstellen
@app.post("/users/", response_model=User, operation_id="create_new_user", summary="Add a new user",
          description="This endpoint allows you to create a new user and store them in the system.")
def create_user(
    user: User,
    user_storage: UserStorage = Depends(get_user_storage)  # Richtige Dependency
):
    user.id = str(user.id)
    return user_storage.create_user(user)

# 🔹 Alle Benutzer abrufen
@app.get("/users/", response_model=List[User], operation_id="get_all_users", summary="Show all users",
         description="Retrieves a list of all registered users in the system.")
def get_users(user_storage: UserStorage = Depends(get_user_storage)):
    return user_storage.get_users()

# 🔹 Einzelnen Benutzer abrufen
@app.get("/users/{user_id}", response_model=User, operation_id="get_defined_user", summary="Show user data",
         description="Retrieves a specific user using their unique ID. If the user is not found, a 404 error is returned.")
def get_user(user_id: UUID, user_storage: UserStorage = Depends(get_user_storage)):
    user = user_storage.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.id = str(user.id)
    return user

# 🔹 Benutzer aktualisieren
@app.put("/users/{user_id}", response_model=User, operation_id="change_user_data", summary="Update user data",
         description="Allows you to update an existing user's details using their unique ID.")
def update_user(
    user_id: UUID,
    updated_user: User,
    user_storage: UserStorage = Depends(get_user_storage)
):
    user = user_storage.update_user(user_id, updated_user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# 🔹 Benutzer löschen
@app.delete("/users/{user_id}", operation_id="delete_user", response_model=dict, summary="Delete a user",
            description="Deletes a user from the system using their unique ID. If the user does not exist, a 404 error is returned.")
def delete_user(user_id: UUID, user_storage: UserStorage = Depends(get_user_storage)):
    success = user_storage.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

# 🔵 FastAPI-Server starten (nur, wenn direkt gestartet)
if __name__ == "__main__":
    logger.info("Starting the server...")
    import uvicorn
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
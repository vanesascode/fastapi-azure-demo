from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from .items import fake_items

router = APIRouter(
    prefix="/users",    # All endpoints will start with /users
    tags=["users"],     # For organizing documentation
    responses={404: {"description": "Not found"}},
)

class User(BaseModel):
    id: int
    name: str
    email: str
    active: bool = True
    edad: int | None = None  # Optional age field

class UserCreate(BaseModel):
    name: str
    email: str
    edad: int | None = None  # Optional age field

fake_users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "active": True, "edad": 30},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "active": True},
    {"id": 3, "name": "Alice Johnson", "email": "alice@example.com", "active": True, "edad": 28}
]

@router.get("/", response_model=List[User])
async def get_users():
    return fake_users

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    for user in fake_users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Calculate the highest ID automatically (avoids magic numbers)
_user_id_counter = max(user["id"] for user in fake_users) if fake_users else 0

@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    global _user_id_counter
    _user_id_counter += 1
    new_user = {
        "id": _user_id_counter,
        "name": user.name,
        "email": user.email,
        "active": True,
        "edad": user.edad  # Include age if provided
    }
    fake_users.append(new_user)
    return new_user

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserCreate):
    for i, existing_user in enumerate(fake_users):
        if existing_user["id"] == user_id:
            fake_users[i].update({
                "name": user.name,
                "email": user.email,
                "edad": user.edad  # Update age if provided
            })
            return fake_users[i]
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    for i, user in enumerate(fake_users):
        if user["id"] == user_id:
            deleted_user = fake_users.pop(i)
            return {"message": f"User {deleted_user['name']} deleted"}
    raise HTTPException(status_code=404, detail="User not found")

@router.get("/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: int, q: str | None = None, short: bool = False
):
    """
    Get a specific item from a user
    
    - **user_id**: ID of the user who owns the item
    - **item_id**: ID of the item to get
    - **q**: Optional query parameter
    - **short**: If True, returns a summarized version without description
    """
    # Search for the item in fake_items
    found_item = None
    for item in fake_items:
        if item["item_id"] == item_id:
            found_item = item
            break
    
    # If item is not found
    if not found_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    found_user = None
    for user in fake_users:
        if user["id"] == user_id:
            found_user = user
            break
    
    if not found_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Create response with real data
    result = {
        "item_id": found_item["item_id"],
        "name": found_item["name"],
        "price": found_item["price"],
        "owner_id": found_user["id"],
        "owner_name": found_user["name"]
    }
    
    # Add query parameter if it exists
    if q:
        result.update({"q": q})
    
    # Add description if not short version
    if not short:
        result.update({
            "description": f"This is an amazing {found_item['name']} that has a price of {found_item['price']}"
        })
    
    return result
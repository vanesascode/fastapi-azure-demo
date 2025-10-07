from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import Annotated, List, FrozenSet
from .items import fake_items
from uuid import UUID, uuid4

router = APIRouter(
    prefix="/users",    # All endpoints will start with /users
    tags=["users"],     # For organizing documentation
    responses={404: {"description": "Not found"}},
)

class User(BaseModel):
    id: UUID
    name: str
    email: str
    active: bool = True
    roles: FrozenSet[str] = frozenset() # Set of roles (no duplicates, unordered) This means that even if you put: "roles": ["artist", "dancer", "dancer"], the user will only have the roles "artist" and "dancer"
    edad: int | None = None  # Optional age field

class UserCreate(BaseModel):
    name: str
    email: str
    edad: int | None = None  # Optional age field
    roles: FrozenSet[str] = frozenset()

fake_users = [
    {
        "id": "a1b2c3d4-e5f6-7890-1234-567890abcdef", 
        "name": "John Doe", 
        "email": "john@example.com", 
        "active": True, 
        "roles": ["admin", "writer"], # We add roles (as a list, Pydantic will convert it to FrozenSet)
        "edad": 30
    },
    {
        "id": "b5e8f4c1-d2a9-40b3-8c7e-9f0a1b2c3d4e", 
        "name": "Jane Smith", 
        "email": "jane@example.com", 
        "active": True,
        "roles": ["editor"], # Un solo rol
        "edad": None
    },
    {
        "id": "c7a8b9d0-e1f2-3456-7890-fedcba987654", 
        "name": "Alice Johnson", 
        "email": "alice@example.com", 
        "active": True, 
        "roles": [], # Sin roles (lista vacía)
        "edad": 28
    }
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

@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    new_user = {
        "id": str(uuid4()), 
        "name": user.name,
        "email": user.email,
        "active": True,
        "roles": list(user.roles),
        "edad": user.edad  # Include age if provided
    }
    fake_users.append(new_user)
    return new_user

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserCreate):# The UserCreate model appears in the documentation to fill out
    for i, existing_user in enumerate(fake_users):
        if existing_user["id"] == user_id:
            fake_users[i].update({
                "name": user.name,
                "email": user.email,
                "roles": list(user.roles), 
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

#The title and description will appear in the redoc documentation
@router.get("/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: int, q: Annotated[ str | None, Query(min_length=3, max_length=50, pattern="^[aeiouAEIOU]{3,50}$", title="Query of only vocals", description="A query parameter that only accepts vowels."), ] = None, short: bool = False
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
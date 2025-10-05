from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from .items import fake_items

router = APIRouter(
    prefix="/users",    # Todos los endpoints empezarán con /users
    tags=["users"],     # Para organizar en la documentación
    responses={404: {"description": "Not found"}},
)

class User(BaseModel):
    id: int
    name: str
    email: str
    active: bool = True

class UserCreate(BaseModel):
    name: str
    email: str

fake_users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "active": True},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "active": True},
    {"id": 3, "name": "Alice Johnson", "email": "alice@example.com", "active": True}
]

@router.get("/", response_model=List[User])
async def get_users():
    return fake_users

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    for user in fake_users:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}

@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    new_user = {
        "id": len(fake_users) + 1,
        "name": user.name,
        "email": user.email,
        "active": True
    }
    fake_users.append(new_user)
    return new_user

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserCreate):
    for i, existing_user in enumerate(fake_users):
        if existing_user["id"] == user_id:
            fake_users[i].update({
                "name": user.name,
                "email": user.email
            })
            return fake_users[i]
    return {"error": "User not found"}

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    for i, user in enumerate(fake_users):
        if user["id"] == user_id:
            deleted_user = fake_users.pop(i)
            return {"message": f"User {deleted_user['name']} deleted"}
    return {"error": "User not found"}

@router.get("/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: int, q: str | None = None, short: bool = False
):
    """
    Obtener un item específico de un usuario
    
    - **user_id**: ID del usuario propietario del item
    - **item_id**: ID del item a obtener
    - **q**: Parámetro de consulta opcional
    - **short**: Si es True, devuelve una versión resumida sin descripción
    """
    # Buscar el item en fake_items
    found_item = None
    for item in fake_items:
        if item["item_id"] == item_id:
            found_item = item
            break
    
    # Si no se encuentra el item
    if not found_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    found_user = None
    for user in fake_users:
        if user["id"] == user_id:
            found_user = user
            break
    
    if not found_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Crear respuesta con datos reales
    result = {
        "item_id": found_item["item_id"],
        "name": found_item["name"],
        "price": found_item["price"],
        "owner_id": found_user["id"],
        "owner_name": found_user["name"]
    }
    
    # Añadir parámetro de consulta si existe
    if q:
        result.update({"q": q})
    
    # Añadir descripción si no es versión corta
    if not short:
        result.update({
            "description": f"This is an amazing {found_item['name']} that has a price of {found_item['price']}"
        })
    
    return result
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

router = APIRouter(
    prefix="/items", # Añade automáticamente /items al inicio de todas las rutas de este router: DRY (Don't Repeat Yourself)
    tags=["items"], #Organiza la documentación en http://127.0.0.1:8000/docs
    responses={404: {"description": "Not found"}}, # Respuesta posible que indicamos en el Swagger para rutas no encontradas
)

class FormatType(str, Enum):
    simple = "simple"
    detailed = "detailed"

class ItemBase(BaseModel):
    item_id: int
    name: str
    price: float

class ItemCreate(BaseModel):
    name: str
    price: float

fake_items = [
    {"item_id": 1, "name": "Laptop", "price": 999.99},
    {"item_id": 2, "name": "Mouse", "price": 29.99},
    {"item_id": 3, "name": "Keyboard", "price": 79.99},
    {"item_id": 4, "name": "Monitor", "price": 299.99},
    {"item_id": 5, "name": "Webcam", "price": 89.99},
    {"item_id": 6, "name": "Speakers", "price": 59.99},
    {"item_id": 7, "name": "Headphones", "price": 149.99},
    {"item_id": 8, "name": "Microphone", "price": 199.99},
    {"item_id": 9, "name": "Tablet", "price": 399.99},
    {"item_id": 10, "name": "Phone", "price": 699.99},
]

# http://127.0.0.1:8000/items/?skip=0&limit=10
@router.get("/", response_model=List[ItemBase])
async def get_items(skip: int = 0, limit: int = 10):
    """
    Obtener items con paginación
    
    - **skip**: Número de elementos a saltar (por defecto 0)
    - **limit**: Número máximo de elementos a devolver (por defecto 10)
    
    Ejemplos:
    - /items/ → Primeros 10 items
    - /items/?limit=3 → Primeros 3 items  
    - /items/?skip=3&limit=2 → Items 4 y 5
    """
    return fake_items[skip : skip + limit]

@router.get("/search", response_model=List[ItemBase])
async def search_items(
    q: str,  # Obligatorio para búsqueda
    min_price: Optional[float] = None,
    max_price: Optional[float] = None
):
    """
    Buscar items por criterios
    
    - **q**: Término de búsqueda (busca en el nombre)
    - **min_price**: Precio mínimo (opcional)
    - **max_price**: Precio máximo (opcional)
    """
    results = []
    
    for item in fake_items:
        if q.lower() not in item["name"].lower():
            continue
            
        if min_price and item["price"] < min_price:
            continue
            
        if max_price and item["price"] > max_price:
            continue
            
        results.append(item)
    
    return results

@router.get("/{item_id}", response_model=dict)
async def get_item(item_id: int, include_details: bool = False, format: Optional[FormatType] = None):  
    """
    Obtener un item específico por ID
    
    - **item_id**: ID único del item (obligatorio)
    - **include_details**: Incluir detalles adicionales (opcional, por defecto False)
    - **format**: Formato de respuesta (opcional: solo "simple" o "detailed")
    
    Ejemplos:
    - /items/1 → Item básico
    - /items/1?include_details=true → Item con más info
    - /items/1?format=detailed → Item con formato específico
    - /items/1?include_details=true&format=simple → Ambos parámetros
    """
    # Buscar el item
    for item in fake_items:
        if item["item_id"] == item_id:
            # Item básico
            result = {
                "item_id": item["item_id"],
                "name": item["name"],
                "price": item["price"]
            }
            
            # Añadir detalles si se solicita
            if include_details:
                result["category"] = "electronics"
                result["in_stock"] = True
                result["rating"] = 4.5
            
            # Aplicar formato si se especifica
            if format == FormatType.simple:
                result["display"] = f"{item['name']} - ${item['price']}"
            elif format == FormatType.detailed:
                result["description"] = f"High-quality {item['name']} for ${item['price']}"
            
            return result
    
    # Si no se encuentra el item
    from fastapi import HTTPException
    raise HTTPException(status_code=404, detail="Item not found")

@router.post("/", response_model=ItemBase)
async def create_item(item: ItemCreate): # El modelo ItemCreate aparece en la documentación para rellenar
    """Crear un nuevo item"""
    new_item = {
        "item_id": len(fake_items) + 1,
        "name": item.name,
        "price": item.price
    }
    fake_items.append(new_item)
    return new_item
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

router = APIRouter(
    prefix="/items", # Automatically adds /items at the beginning of all routes in this router: DRY (Don't Repeat Yourself)
    tags=["items"], # Organizes documentation at http://127.0.0.1:8000/docs
    responses={404: {"description": "Not found"}}, # Possible response we indicate in Swagger for routes not found
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
    Get items with pagination
    
    - **skip**: Number of elements to skip (default 0)
    - **limit**: Maximum number of elements to return (default 10)
    
    Examples:
    - /items/ → First 10 items
    - /items/?limit=3 → First 3 items  
    - /items/?skip=3&limit=2 → Items 4 and 5
    """
    return fake_items[skip : skip + limit]

@router.get("/search", response_model=List[ItemBase])
async def search_items(
    q: str,  # Required for search
    min_price: Optional[float] = None,
    max_price: Optional[float] = None
):
    """
    Search items by criteria
    
    - **q**: Search term (searches in the name)
    - **min_price**: Minimum price (optional)
    - **max_price**: Maximum price (optional)
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
async def get_item(item_id: int, include_details: bool = False, format_type: Optional[FormatType] = None):  
    """
    Get a specific item by ID
    
    - **item_id**: Unique item ID (required)
    - **include_details**: Include additional details (optional, default False)
    - **format_type**: Response format (optional: only "simple" or "detailed")
    
    Examples:
    - /items/1 → Basic item
    - /items/1?include_details=true → Item with more info
    - /items/1?format=detailed → Item with specific format
    - /items/1?include_details=true&format=simple → Both parameters
    """
    # Search for the item
    for item in fake_items:
        if item["item_id"] == item_id:
            # Basic item
            result = {
                "item_id": item["item_id"],
                "name": item["name"],
                "price": item["price"]
            }
            
            # Add details if requested
            if include_details:
                result["category"] = "electronics"
                result["in_stock"] = True
                result["rating"] = 4.5
            
            # Apply format if specified
            if format_type == FormatType.simple:
                result["display"] = f"{item['name']} - ${item['price']}"
            elif format_type == FormatType.detailed:
                result["description"] = f"High-quality {item['name']} for ${item['price']}"
            
            return result
    
    # If item is not found
    raise HTTPException(status_code=404, detail="Item not found")

_item_id_counter = max(item["item_id"] for item in fake_items) if fake_items else 0

@router.post("/", response_model=ItemBase)
async def create_item(item: ItemCreate): # The ItemCreate model appears in the documentation to fill out
    """Create a new item"""
    global _item_id_counter
    _item_id_counter += 1
    new_item = {
        "item_id": _item_id_counter,
        "name": item.name,
        "price": item.price
    }
    fake_items.append(new_item)
    return new_item
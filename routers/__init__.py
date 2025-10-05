"""
Routers package for FastAPI application.
Contains all API endpoint routers organized by resource.
"""

# Import routers to make them easily accessible
from .users import router as users_router
from .items import router as items_router
from .models import router as models_router

# Define what gets imported with "from routers import *"
__all__ = ["users_router", "items_router", "models_router"]
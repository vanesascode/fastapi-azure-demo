from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from routers import users, items, models

app = FastAPI(
    title="FastAPI Scaffolding Project",
    description="A well-organized FastAPI application with routers",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(items.router)
app.include_router(models.router)

class HelloResponse(BaseModel):
    Hello: str

@app.get("/", response_model=HelloResponse)
def read_root():
    return {"Hello": "World"}

@app.get("/datetime")
def get_datetime():
    from datetime import datetime
    return {
        "timestamp": datetime.now(),
    }

@app.get("/images/{image_path:path}")
async def serve_image(image_path: str):
    """
    Serve images from different folders
    
    Useful examples:
    - /images/products/laptop.jpg
    - /images/users/avatars/juan.png
    - /images/blog/2024/article-1/cover.jpg
    """
    # In real life, here you would verify that the file exists
    # and return FileResponse(f"/static/images/{image_path}")
    
    return {
        "image_path": image_path,
        "full_url": f"https://myserver.com/static/images/{image_path}",
        "type": "image",
        "folder": image_path.split('/')[0] if '/' in image_path else "root"
    }

# This endpoint must go at the end to avoid conflicts with other endpoints
@app.get("/{name}", response_model=HelloResponse)
def read_root_name(name: str):
    return {"Hello": name}

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

@app.get("/{name}", response_model=HelloResponse)
def read_root_name(name: str):
    return {"Hello": name}

@app.get("/images/{image_path:path}")
async def serve_image(image_path: str):
    """
    Servir imágenes desde diferentes carpetas
    
    Ejemplos útiles:
    - /images/productos/laptop.jpg
    - /images/usuarios/avatares/juan.png
    - /images/blog/2024/articulo-1/portada.jpg
    """
    # En la vida real, aquí verificarías que el archivo existe
    # y devolverías FileResponse(f"/static/images/{image_path}")
    
    return {
        "image_path": image_path,
        "full_url": f"https://miservidor.com/static/images/{image_path}",
        "tipo": "imagen",
        "carpeta": image_path.split('/')[0] if '/' in image_path else "raiz"
    }


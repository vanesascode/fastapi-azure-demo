from fastapi import APIRouter
from enum import Enum

router = APIRouter(
    prefix="/models",    # Todos los endpoints empezarán con /users
    tags=["models"],     # Para organizar en la documentación
    responses={404: {"description": "Not found"}},
)

class ModelName(str, Enum): # En el swagger saldrán las opciones a elegir en un desplegable
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@router.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet: # opción 1
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet": # opción 2
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
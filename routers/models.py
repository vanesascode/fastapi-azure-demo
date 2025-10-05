from fastapi import APIRouter
from enum import Enum

router = APIRouter(
    prefix="/models",    # All endpoints will start with /models
    tags=["models"],     # For organizing documentation
    responses={404: {"description": "Not found"}},
)

class ModelName(str, Enum): # Options will appear in a dropdown in Swagger
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@router.get("/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet: # option 1
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet": # option 2
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
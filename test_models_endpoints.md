# Models Endpoints Tests

Test commands for endpoints defined in `routers/models.py`.

## Prerequisites

Make sure the FastAPI server is running:

```bash
.\scaffolding\Scripts\activate
fastapi dev main.py
```

Server should be running on: http://127.0.0.1:8000

## Available Models

- alexnet
- resnet
- lenet

## Models Endpoints

### 1. Get Model - alexnet

```powershell
curl http://127.0.0.1:8000/models/alexnet
```

**Expected Response:**

```json
{
  "model_name": "alexnet",
  "message": "Deep Learning FTW!"
}
```

### 2. Get Model - lenet

```powershell
curl http://127.0.0.1:8000/models/lenet
```

**Expected Response:**

```json
{
  "model_name": "lenet",
  "message": "LeCNN all the images"
}
```

### 3. Get Model - resnet

```powershell
curl http://127.0.0.1:8000/models/resnet
```

**Expected Response:**

```json
{
  "model_name": "resnet",
  "message": "Have some residuals"
}
```

### 4. Test Error Cases

**Invalid model name:**

```powershell
curl http://127.0.0.1:8000/models/invalid_model
```

**Expected Response:**

```json
{
  "detail": [
    {
      "type": "enum",
      "loc": ["path", "model_name"],
      "msg": "Input should be 'alexnet', 'resnet' or 'lenet'",
      "input": "invalid_model",
      "ctx": {
        "expected": "'alexnet', 'resnet' or 'lenet'"
      }
    }
  ]
}
```

## Notes

- Model names are **case-sensitive**
- Only the three predefined model names are accepted
- This demonstrates **Enum validation** in FastAPI
- In Swagger UI, you'll see a dropdown with the three valid options

# Main Endpoints Tests

Test commands for endpoints defined in `main.py`.

## Prerequisites

Make sure the FastAPI server is running:

```bash
.\scaffolding\Scripts\activate
fastapi dev main.py
```

Server should be running on: http://127.0.0.1:8000

## Main Endpoints

### 1. Root Endpoint

**PowerShell:**

```powershell
curl http://127.0.0.1:8000/
```

**Expected Response:**

```json
{ "Hello": "World" }
```

### 2. DateTime Endpoint

**PowerShell:**

```powershell
curl http://127.0.0.1:8000/datetime
```

**Expected Response:**

```json
{
  "timestamp": "2025-10-05T11:30:00.123456"
}
```

### 3. Dynamic Name Endpoint

**PowerShell:**

```powershell
curl http://127.0.0.1:8000/carlos
```

**Expected Response:**

```json
{ "Hello": "carlos" }
```

### 4. Image Path Converter (Path Parameter)

**PowerShell:**

```powershell
curl "http://127.0.0.1:8000/images/products/laptop.jpg"
```

**Expected Response:**

```json
{
  "image_path": "products/laptop.jpg",
  "full_url": "https://myserver.com/static/images/products/laptop.jpg",
  "type": "image",
  "folder": "products"
}
```

**Test with nested path:**

```powershell
curl "http://127.0.0.1:8000/images/users/avatars/john.png"
```

**Expected Response:**

```json
{
  "image_path": "users/avatars/john.png",
  "full_url": "https://myserver.com/static/images/users/avatars/john.png",
  "type": "image",
  "folder": "users"
}
```

## Documentation Access

### Swagger UI

```powershell
curl http://127.0.0.1:8000/docs
```

### ReDoc

```powershell
curl http://127.0.0.1:8000/redoc
```

### OpenAPI Schema

```powershell
curl http://127.0.0.1:8000/openapi.json
```

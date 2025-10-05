# Items Endpoints Tests

Test commands for endpoints defined in `routers/items.py`.

## Prerequisites

Make sure the FastAPI server is running:

```bash
.\scaffolding\Scripts\activate
fastapi dev main.py
```

Server should be running on: http://127.0.0.1:8000

## Available Items (IDs 1-10)

- ID 1: Laptop ($999.99)
- ID 2: Mouse ($29.99)
- ID 3: Keyboard ($79.99)
- ID 4: Monitor ($299.99)
- ID 5: Webcam ($89.99)
- ID 6: Speakers ($59.99)
- ID 7: Headphones ($149.99)
- ID 8: Microphone ($199.99)
- ID 9: Tablet ($399.99)
- ID 10: Phone ($699.99)

## Items Endpoints

### 1. Get All Items (with pagination)

**Get first 10 items:**

```powershell
curl http://127.0.0.1:8000/items/
```

**Get first 3 items:**

```powershell
curl "http://127.0.0.1:8000/items/?limit=3"
```

**Skip 3, get 2 items:**

```powershell
curl "http://127.0.0.1:8000/items/?skip=3&limit=2"
```

### 2. Get Single Item (basic)

```powershell
curl http://127.0.0.1:8000/items/1
```

**Expected Response:**

```json
{
  "item_id": 1,
  "name": "Laptop",
  "price": 999.99
}
```

### 3. Get Item with Details

```powershell
curl "http://127.0.0.1:8000/items/1?include_details=true"
```

**Expected Response:**

```json
{
  "item_id": 1,
  "name": "Laptop",
  "price": 999.99,
  "category": "electronics",
  "in_stock": true,
  "rating": 4.5
}
```

### 4. Get Item with Format

**Simple format:**

```powershell
curl "http://127.0.0.1:8000/items/5?format_type=simple"
```

**Expected Response:**

```json
{
  "item_id": 5,
  "name": "Webcam",
  "price": 89.99,
  "display": "Webcam - $89.99"
}
```

**Detailed format:**

```powershell
curl "http://127.0.0.1:8000/items/5?format_type=detailed"
```

**Expected Response:**

```json
{
  "item_id": 5,
  "name": "Webcam",
  "price": 89.99,
  "description": "High-quality Webcam for $89.99"
}
```

### 5. Search Items

**Search by name:**

```powershell
curl "http://127.0.0.1:8000/items/search?q=laptop"
```

**Search with price range:**

```powershell
curl "http://127.0.0.1:8000/items/search?q=phone&min_price=100&max_price=800"
```

### 6. Create New Item

**Simple JSON method (recommended):**

```powershell
$body = '{"name": "Gaming Mouse", "price": 79.99}'
Invoke-RestMethod -Uri "http://127.0.0.1:8000/items/" -Method POST -Body $body -ContentType "application/json"
```

**Alternative method with UTF-8:**

```powershell
$item = @{
    name = "Gaming Mouse"
    price = 79.99
}
$body = $item | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:8000/items/" -Method POST -Body ([System.Text.Encoding]::UTF8.GetBytes($body)) -ContentType "application/json; charset=utf-8"
```

**Expected Response:**

```json
{
  "item_id": 11,
  "name": "Gaming Mouse",
  "price": 79.99
}
```

### 7. Test Error Cases

**Non-existent item:**

```powershell
curl http://127.0.0.1:8000/items/999
```

**Expected Response:**

```json
{ "detail": "Item not found" }
```

**Invalid item ID:**

```powershell
curl http://127.0.0.1:8000/items/abc
```

**Expected Response:**

```json
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": ["path", "item_id"],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "abc"
    }
  ]
}
```

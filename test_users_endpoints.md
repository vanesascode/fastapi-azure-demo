# Users Endpoints Tests

Test commands for endpoints defined in `routers/users.py`.

## Prerequisites

Make sure the FastAPI server is running:

```bash
.\scaffolding\Scripts\activate
fastapi dev main.py
```

Server should be running on: http://127.0.0.1:8000

## Available Users

- ID 1: John Doe (john@example.com, edad: 30)
- ID 2: Jane Smith (jane@example.com, edad: 25)
- ID 3: Alice Johnson (alice@example.com, edad: 28)

## Users Endpoints

### 1. Get All Users

```powershell
curl http://127.0.0.1:8000/users/
```

**Expected Response:**

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "active": true,
    "edad": 30
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane@example.com",
    "active": true,
    "edad": 25
  },
  {
    "id": 3,
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "active": true,
    "edad": 28
  }
]
```

### 2. Get Single User

```powershell
curl http://127.0.0.1:8000/users/1
```

**Expected Response:**

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "active": true,
  "edad": 30
}
```

### 3. Create New User (with age)

**Method 1 - Simple JSON string (recommended):**

```powershell
$body = '{"name": "Carlos Garcia", "email": "carlos@example.com", "edad": 35}'
Invoke-RestMethod -Uri "http://127.0.0.1:8000/users/" -Method POST -Body $body -ContentType "application/json"
```

**Method 2 - Using ConvertTo-Json with UTF-8:**

```powershell
$user = @{
    name = "Carlos Garcia"
    email = "carlos@example.com"
    edad = 35
}
$body = $user | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:8000/users/" -Method POST -Body ([System.Text.Encoding]::UTF8.GetBytes($body)) -ContentType "application/json; charset=utf-8"
```

**Expected Response:**

```json
{
  "id": 4,
  "name": "Carlos Garcia",
  "email": "carlos@example.com",
  "active": true,
  "edad": 35
}
```

### 4. Create New User (without age)

**Simple JSON method:**

```powershell
$body = '{"name": "Maria Lopez", "email": "maria@example.com"}'
Invoke-RestMethod -Uri "http://127.0.0.1:8000/users/" -Method POST -Body $body -ContentType "application/json"
```

**Expected Response:**

```json
{
  "id": 5,
  "name": "Maria Lopez",
  "email": "maria@example.com",
  "active": true,
  "edad": null
}
```

### 5. Update User

**Simple JSON method:**

```powershell
$body = '{"name": "John Updated", "email": "john.updated@example.com", "edad": 31}'
Invoke-RestMethod -Uri "http://127.0.0.1:8000/users/1" -Method PUT -Body $body -ContentType "application/json"
```

### 6. Delete User

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/users/2" -Method DELETE
```

**Expected Response:**

```json
{
  "message": "User Jane Smith deleted"
}
```

### 7. Get User's Item (Cross-router endpoint)

**Basic user item:**

```powershell
curl http://127.0.0.1:8000/users/1/items/1
```

**Expected Response:**

```json
{
  "item_id": 1,
  "name": "Laptop",
  "price": 999.99,
  "owner_id": 1,
  "owner_name": "John Doe",
  "description": "This is an amazing Laptop that has a price of 999.99"
}
```

**User item with query parameter:**

```powershell
curl "http://127.0.0.1:8000/users/1/items/1?q=gaming"
```

**User item (short version):**

```powershell
curl "http://127.0.0.1:8000/users/1/items/1?short=true"
```

### 8. Test Error Cases

**Non-existent user:**

```powershell
curl http://127.0.0.1:8000/users/999
```

**Expected Response:**

```json
{ "detail": "User not found" }
```

**Non-existent item for user:**

```powershell
curl http://127.0.0.1:8000/users/1/items/999
```

**Expected Response:**

```json
{ "detail": "Item not found" }
```

**Non-existent user for item:**

```powershell
curl http://127.0.0.1:8000/users/999/items/1
```

**Expected Response:**

```json
{ "detail": "User not found" }
```

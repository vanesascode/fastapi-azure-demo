# FastAPI Curl Tests

This file contains curl commands to test all endpoints of the FastAPI application.

## Prerequisites

1. Make sure the FastAPI server is running:

   ```bash
   .\scaffolding\Scripts\activate
   uvicorn main:app --reload
   ```

2. Server should be running on: http://127.0.0.1:8000

## Test Commands

### 1. Test Root Endpoint

```bash
curl -X GET "http://127.0.0.1:8000/" -H "accept: application/json"
```

**Expected Response:**

```json
{ "Hello": "World" }
```

### 2. Test Items Endpoint (without query parameter)

```bash
curl -X GET "http://127.0.0.1:8000/items/42" -H "accept: application/json"
```

**Expected Response:**

```json
{ "item_id": 42, "q": null }
```

### 3. Test Items Endpoint (with query parameter)

```bash
curl -X GET "http://127.0.0.1:8000/items/42?q=test" -H "accept: application/json"
```

**Expected Response:**

```json
{ "item_id": 42, "q": "test" }
```

### 4. Test Items Endpoint (with different item_id)

```bash
curl -X GET "http://127.0.0.1:8000/items/123?q=example" -H "accept: application/json"
```

**Expected Response:**

```json
{ "item_id": 123, "q": "example" }
```

### 5. Test Invalid Item ID (should return validation error)

```bash
curl -X GET "http://127.0.0.1:8000/items/abc" -H "accept: application/json"
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

## Documentation URLs

### Interactive Documentation (Swagger UI)

```bash
curl -X GET "http://127.0.0.1:8000/docs"
```

### Alternative Documentation (ReDoc)

```bash
curl -X GET "http://127.0.0.1:8000/redoc"
```

### OpenAPI Schema

```bash
curl -X GET "http://127.0.0.1:8000/openapi.json" -H "accept: application/json"
```

## PowerShell Alternative (if curl is not available)

**Important**: In PowerShell, `curl` is an alias for `Invoke-WebRequest` which has different syntax.

### Option 1: Use PowerShell's Invoke-RestMethod (Recommended)

```powershell
# Test root endpoint
Invoke-RestMethod -Uri "http://127.0.0.1:8000/" -Method Get

# Test items endpoint
Invoke-RestMethod -Uri "http://127.0.0.1:8000/items/42" -Method Get

# Test with query parameter
Invoke-RestMethod -Uri "http://127.0.0.1:8000/items/42?q=test" -Method Get

# Test different item ID
Invoke-RestMethod -Uri "http://127.0.0.1:8000/items/123?q=example" -Method Get

# Test invalid item ID (validation error)
Invoke-RestMethod -Uri "http://127.0.0.1:8000/items/abc" -Method Get
```

### Option 2: Use PowerShell's Invoke-WebRequest

```powershell
# Test root endpoint
Invoke-WebRequest -Uri "http://127.0.0.1:8000/" -Method Get -Headers @{"accept"="application/json"}

# Test items endpoint
Invoke-WebRequest -Uri "http://127.0.0.1:8000/items/42" -Method Get -Headers @{"accept"="application/json"}

# Test with query parameter
Invoke-WebRequest -Uri "http://127.0.0.1:8000/items/42?q=test" -Method Get -Headers @{"accept"="application/json"}
```

### Option 3: Use real curl (if installed separately)

If you have curl.exe installed separately:

```powershell
# Use full path to curl.exe
curl.exe -X GET "http://127.0.0.1:8000/" -H "accept: application/json"

# Or remove the PowerShell alias temporarily
Remove-Item alias:curl
curl -X GET "http://127.0.0.1:8000/" -H "accept: application/json"
```

## Batch Testing Script

Create a batch file to run all tests:

```batch
@echo off
echo Testing FastAPI Endpoints...
echo.

echo 1. Testing root endpoint:
curl -X GET "http://127.0.0.1:8000/" -H "accept: application/json"
echo.

echo 2. Testing items endpoint without query:
curl -X GET "http://127.0.0.1:8000/items/42" -H "accept: application/json"
echo.

echo 3. Testing items endpoint with query:
curl -X GET "http://127.0.0.1:8000/items/42?q=test" -H "accept: application/json"
echo.

echo 4. Testing invalid item ID:
curl -X GET "http://127.0.0.1:8000/items/abc" -H "accept: application/json"
echo.

echo All tests completed!
```

Save this as `test_endpoints.bat` and run it to test all endpoints at once.

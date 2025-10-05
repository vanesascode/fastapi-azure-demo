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

## External API Endpoints

### 1. External Post (DummyJSON)

Test fetching a post from external API - demonstrates async/await usage.

**PowerShell:**

```powershell
curl http://127.0.0.1:8000/external/post/1
```

**Expected Response:**

```json
{
  "source": "DummyJSON API",
  "post_id": 1,
  "title": "His mother had always taught him",
  "body": "His mother had always taught him not to ever think of himself as better than others...",
  "user_id": 9,
  "tags": ["history", "american", "crime"],
  "reactions": { "likes": 192, "dislikes": 25 },
  "api_response_time": "0.234s",
  "status": "success"
}
```

**Test different posts:**

```powershell
curl http://127.0.0.1:8000/external/post/5
curl http://127.0.0.1:8000/external/post/10
```

**Test error case (non-existent post):**

```powershell
curl http://127.0.0.1:8000/external/post/999999
```

**Expected Error Response:**

```json
{
  "detail": "Post not found in external API"
}
```

## String ↔ Bytes Conversion Endpoints

### 1. Filename Encoding Conversion

Test string to bytes conversion with filename processing - demonstrates encoding/decoding.

**PowerShell:**

```powershell
curl http://127.0.0.1:8000/convert/filename/archivo1.jpg
```

**Expected Response:**

```json
{
  "original_filename": "archivo1.jpg",
  "encoding_process": {
    "step_1_string": "archivo1.jpg",
    "step_2_bytes_repr": "b'archivo1.jpg'",
    "step_3_base64": "YXJjaGl2bzEuanBn",
    "step_4_back_to_bytes": "b'archivo1.jpg'",
    "step_5_back_to_string": "archivo1.jpg"
  },
  "byte_analysis": {
    "total_bytes": 12,
    "byte_values": [97, 114, 99, 104, 105, 118, 111, 49, 46, 106, 112, 103],
    "first_byte": 97,
    "last_byte": 103
  },
  "verification": {
    "strings_match": true,
    "encoding_used": "UTF-8",
    "transport_encoding": "Base64"
  },
  "practical_uses": [
    "File upload processing",
    "Network data transmission",
    "Database blob storage",
    "Cryptographic operations"
  ]
}
```

**Test with special characters:**

```powershell
curl "http://127.0.0.1:8000/convert/filename/niño_español.txt"
```

**Test with spaces (URL encoded):**

```powershell
curl "http://127.0.0.1:8000/convert/filename/my%20file.pdf"
```

### 2. Image Processing Simulation

Test image bytes handling - demonstrates real-world file processing.

**PowerShell:**

```powershell
curl http://127.0.0.1:8000/convert/image-simulation
```

**Expected Response:**

```json
{
  "status": "success",
  "image_info": {
    "filename": "profile_photo.jpg",
    "content_type": "image/jpeg",
    "size_bytes": 10
  },
  "conversions": {
    "filename_to_bytes": {
      "original": "profile_photo.jpg",
      "bytes_length": 17,
      "first_byte": 112
    },
    "image_to_base64": {
      "bytes_sample": "b'\\xff\\xd8\\xff\\xe0JFIF'",
      "base64_result": "/9j/4EpGSUY=",
      "base64_length": 12
    }
  },
  "byte_analysis": {
    "total_bytes": 10,
    "header_bytes": [255, 216, 255, 224, 74, 70, 73, 70],
    "is_jpeg": true,
    "is_png": false
  },
  "demonstration": {
    "purpose": "Show string ↔ bytes conversion for images",
    "use_cases": [
      "File upload processing",
      "Image transmission via JSON",
      "File type detection",
      "Database storage"
    ]
  }
}
```

### 3. Simple Bytes Conversion Test

Ultra-minimal endpoint for testing basic string ↔ bytes conversion.

**PowerShell:**

```powershell
curl http://127.0.0.1:8000/convert/image-simple
```

**Expected Response:**

```json
{
  "original": "hello",
  "as_bytes": "b'hello'",
  "back_to_string": "hello",
  "success": true
}
```

### 4. Ultra-Simple Test Endpoint

Minimal test endpoint for debugging connectivity issues.

**PowerShell:**

```powershell
curl http://127.0.0.1:8000/convert/test
```

**Expected Response:**

```json
{
  "message": "This should always work in Postman"
}
```

## Educational Notes

### String ↔ Bytes Conversion Concepts

- **UTF-8 Encoding:** How strings become bytes for storage/transmission
- **Base64 Encoding:** Safe way to transport binary data in text format
- **File Processing:** Real-world scenarios where string/bytes conversion matters
- **Error Handling:** Proper exception handling for encoding errors

### Practical Applications

- **File Uploads:** Converting filenames and file content
- **API Data Transport:** Using Base64 for binary data in JSON
- **Database Storage:** Storing binary data as bytes
- **Network Communication:** Proper encoding for data transmission

## Notes

- **External API endpoints demonstrate real async/await usage** - they actually need `await` because they make network calls
- **Error handling** is implemented for both network errors and HTTP status errors
- **Response times** are included to show the performance impact of external calls
- **Connection management** uses `async with` for proper resource cleanup
- These endpoints will fail if there's no internet connection (expected behavior)

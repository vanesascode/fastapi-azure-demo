# FastAPI Test Suite - Complete Endpoint Testing

This directory contains organized test files for all FastAPI endpoints, separated by module.

## Test Files Structure

```
📁 Test Files
├── 📄 test_main_endpoints.md      # Main app endpoints (/, /datetime, /images)
├── 📄 test_items_endpoints.md     # Items CRUD operations (/items/*)
├── 📄 test_users_endpoints.md     # Users CRUD + cross-router (/users/*)
├── 📄 test_models_endpoints.md    # AI Models enum validation (/models/*)
└── 📄 README_tests.md            # This overview file
```

## Quick Start

1. **Start the server:**

   ```bash
   .\scaffolding\Scripts\activate
   fastapi dev main.py
   ```

2. **Choose your test file:**
   - **General app features** → `test_main_endpoints.md`
   - **Product/Item management** → `test_items_endpoints.md`
   - **User management** → `test_users_endpoints.md`
   - **AI Model validation** → `test_models_endpoints.md`

## Test Coverage

### 🏠 Main Endpoints (`test_main_endpoints.md`)

- Root endpoint (`/`)
- DateTime utility (`/datetime`)
- Dynamic name greeting (`/{name}`)
- Path parameter converter (`/images/{path:path}`)
- Documentation access (`/docs`, `/redoc`, `/openapi.json`)

### 📦 Items Endpoints (`test_items_endpoints.md`)

- **GET** `/items/` - List with pagination
- **GET** `/items/{id}` - Single item with options
- **GET** `/items/search` - Search with filters
- **POST** `/items/` - Create new item
- Error handling (404, validation)

### 👥 Users Endpoints (`test_users_endpoints.md`)

- **GET** `/users/` - List all users
- **GET** `/users/{id}` - Single user
- **POST** `/users/` - Create user (with/without age)
- **PUT** `/users/{id}` - Update user
- **DELETE** `/users/{id}` - Delete user
- **GET** `/users/{id}/items/{id}` - Cross-router functionality
- Error handling (404, validation)

### 🤖 Models Endpoints (`test_models_endpoints.md`)

- **GET** `/models/{model_name}` - Enum-validated model selection
- Error handling (invalid enum values)

## PowerShell Commands

All test files use **PowerShell-compatible** curl syntax:

- ✅ `curl http://127.0.0.1:8000/endpoint`
- ✅ `curl "http://127.0.0.1:8000/endpoint?param=value"`
- ✅ `Invoke-RestMethod` for POST/PUT/DELETE operations

## Data Overview

### Pre-loaded Items (IDs 1-10)

1. Laptop ($999.99)
2. Mouse ($29.99)
3. Keyboard ($79.99)
4. Monitor ($299.99)
5. Webcam ($89.99)
6. Speakers ($59.99)
7. Headphones ($149.99)
8. Microphone ($199.99)
9. Tablet ($399.99)
10. Phone ($699.99)

### Pre-loaded Users (IDs 1-3)

1. John Doe (30 years old)
2. Jane Smith (25 years old)
3. Alice Johnson (28 years old)

### Available Models

- `alexnet`
- `resnet`
- `lenet`

## Learning Features Demonstrated

- **CRUD Operations** (Create, Read, Update, Delete)
- **Path Parameters** (IDs, enum validation)
- **Query Parameters** (pagination, filtering, options)
- **Request Bodies** (JSON for POST/PUT)
- **Response Models** (Pydantic validation)
- **Error Handling** (404, validation errors)
- **Cross-Router Communication** (users accessing items)
- **Optional Fields** (age field in users)
- **Path Converters** (file path handling)
- **Enum Validation** (predefined model names)

## Next Steps

1. Run tests from each file to understand different FastAPI features
2. Modify test data to see validation in action
3. Try invalid inputs to see error handling
4. Explore the auto-generated docs at `/docs`

Happy testing! 🚀

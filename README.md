# FastAPI Scaffolding Project

FastAPI basic REST API with instructions to start a project and test it, but also with lots of examples to learn FastApi and Python for beginners

## Environment Information

**Python Version:** 3.13.7

## Virtual Environment Setup

### Steps performed to create and activate the virtual environment:

1. **Check Python version:**

   ```powershell
   python --version
   ```

   Output: `Python 3.13.7`

2. **Create virtual environment:**

   ```powershell
   python -m venv scaffolding
   ```

3. **Activate virtual environment:**

   ```powershell
   .\scaffolding\Scripts\activate
   ```

4. **To deactivate the virtual environment (when needed):**
   ```powershell
   deactivate
   ```

## FastAPI Installation

### Why `pip install "fastapi[standard]"`?

We installed FastAPI with the `[standard]` option which automatically includes:

- **FastAPI**: The main framework
- **Uvicorn**: High-performance ASGI server
- **Starlette**: Base framework on which FastAPI is built
- **Pydantic**: For data validation and serialization
- **Jinja2**: Template engine
- **python-multipart**: For handling forms and files
- **email-validator**: For email validation

### What is Starlette?

**Starlette** is the lightweight and asynchronous web framework that serves as FastAPI's foundation:

- ASGI (Asynchronous Server Gateway Interface) framework
- Minimalist but powerful
- High performance
- Provides routing, middleware, WebSockets, background tasks, etc.

### Why don't we need to install Uvicorn separately?

In previous documentation versions it showed:

```bash
pip install fastapi
pip install uvicorn[standard]  # No longer needed
```

Now with a single command we get everything:

```bash
pip install "fastapi[standard]"  # Includes Uvicorn and more
```

### Installation command executed:

```powershell
pip install "fastapi[standard]"
```

## Running the Application

### Command to start the server:

**Important**: Make sure your virtual environment is activated first:

```powershell
.\scaffolding\Scripts\activate
fastapi dev main.py
```

### Important URLs:

- **Main application**: http://127.0.0.1:8000
- **Interactive documentation (Swagger)**: http://127.0.0.1:8000/docs
- **Alternative documentation (ReDoc)**: http://127.0.0.1:8000/redoc
- **OpenAPI JSON schema**: http://127.0.0.1:8000/openapi.json

### What you'll see at each URL:

**http://127.0.0.1:8000**

- Your FastAPI application running
- Shows responses from your endpoints
- By default, the root endpoint `/` returns `{"Hello": "World"}`

**http://127.0.0.1:8000/docs**

- Automatic interactive documentation (Swagger UI)
- You can test all endpoints directly from the browser
- Shows parameters, data types, expected responses
- Includes usage examples

## Dependency Management

### View installed packages:

```powershell
pip list
```

### Generate dependencies file:

```powershell
pip freeze > requirements.txt
```

### Install from requirements.txt:

```powershell
pip install -r requirements.txt
```

**Why use requirements.txt?**

- Freezes exact versions of all packages
- Allows recreating the same environment elsewhere
- Essential for deployment and collaboration
- Prevents compatibility issues between versions

## Project Structure

```
ScaffoldingFastApi0/
├── scaffolding/          # Virtual environment
│   ├── Scripts/          # Activation scripts and executables
│   ├── Lib/             # Installed libraries
│   └── pyvenv.cfg       # Virtual environment configuration
├── routers/             # Modular organization (NEW!)
│   ├── __init__.py      # Makes it a Python package
│   ├── users.py         # User-related endpoints
│   ├── items.py         # Item-related endpoints
│   └── models.py        # Additional endpoints
├── main.py              # FastAPI application entry point
├── requirements.txt     # Python dependencies
├── test_endpoints.md    # Curl commands for testing endpoints
├── test_endpoints.bat   # Batch script for automated testing
└── README.md            # This file
```

### 🎯 Learning Points - Modular Architecture

#### Why use routers instead of putting everything in main.py?

**❌ Monolithic approach (bad for large projects):**

```python
# All in main.py - gets messy quickly
@app.get("/users/")
@app.post("/users/")
@app.get("/items/")
@app.post("/items/")
# ... 50+ endpoints in one file
```

**✅ Modular approach (scalable):**

```python
# main.py - clean and organized
from routers import users, items
app.include_router(users.router)
app.include_router(items.router)
```

#### Key Benefits:

- **DRY Principle**: Router prefixes avoid repeating `/users` in every route
- **Team Collaboration**: Different developers can work on different routers
- **Testing**: Easier to test isolated functionality
- **Maintenance**: Changes to user logic only affect `users.py`

#### Cross-Router Data Sharing:

Notice how `users.py` imports data from `items.py`:

```python
from .items import fake_items  # Sharing data between modules
```

This demonstrates Python's relative imports and module system in action!

## FastAPI Learning Highlights

### 🔄 Pydantic Models for Data Validation

**Automatic validation** - FastAPI uses Pydantic to validate incoming data:

```python
class UserCreate(BaseModel):
    name: str           # Required string
    email: str         # Required string

# FastAPI automatically:
# ✅ Validates data types
# ✅ Returns 422 error if validation fails
# ✅ Generates API documentation
```

### 🎪 `enumerate()` Function - Python Essential

Found in `users.py` for updating/deleting items:

```python
for i, existing_user in enumerate(fake_users):
    # i = index (0, 1, 2...)
    # existing_user = actual user data
    if existing_user["id"] == user_id:
        fake_users[i] = updated_data  # Modify original list
```

**Why not just a regular loop?** Because you need the **index** to modify the original list.

### 🗂️ `.pop(i)` Method - List Manipulation

Removes AND returns an element:

```python
deleted_user = fake_users.pop(i)  # Two actions in one!
# 1. Removes user from list
# 2. Stores removed user in variable
```

### 🔗 Cross-Module Data Access

**Real-world pattern** - sharing data between modules:

```python
# users.py imports items data
from .items import fake_items

# Now users can access item information
# Demonstrates Python's import system
```

### 🎯 Type Hints for API Parameters

**Different data types** serve different purposes:

```python
async def read_user_item(
    user_id: int,              # Path param: numeric ID
    item_id: str,              # Path param: flexible ID (codes, UUIDs)
    q: str | None = None,      # Query param: optional filter
    short: bool = False        # Query param: boolean flag
):
```

**Why `item_id: str`?** Real items often have alphanumeric IDs like `"PROD-ABC123"` or `"uuid-a1b2c3d4"`.

### Next Steps

- [x] Install FastAPI with standard dependencies
- [x] Create application structure
- [x] Configure dependency files (requirements.txt)
- [x] Test all endpoints and documentation URLs

## Testing

### Manual Testing with Browser

Access the URLs mentioned in the "Running the Application" section.

### Automated Testing with Curl

Run the batch script for quick endpoint testing:

```powershell
.\test_endpoints.bat
```

Or use individual curl commands from `test_endpoints.md` file.

### PowerShell Alternative

If curl is not available, use PowerShell:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/" -Method Get
Invoke-RestMethod -Uri "http://127.0.0.1:8000/items/42?q=test" -Method Get
```

## Troubleshooting

### Common Issues:

1. **`uvicorn` command not found**:

   - Make sure virtual environment is activated: `.\scaffolding\Scripts\activate`
   - Check if FastAPI was installed correctly: `pip list | findstr fastapi`

2. **Module not found errors**:

   - Ensure you're in the correct directory with `main.py`
   - Verify virtual environment is activated

3. **Port already in use**:
   - Use a different port: `uvicorn main:app --port 8001 --reload`
   - Or kill the process using port 8000

## FastAPI Special Features

### Path Converter - Handling File Paths in URLs

One interesting feature implemented in this project is the **Path Converter**, which allows handling file paths as URL parameters.

#### The Problem

Normal path parameters only capture a single segment:

```python
@app.get("/files/{filename}")  # ❌ Only captures "document.pdf"
async def get_file(filename: str):
    return {"file": filename}
```

**URL**: `/files/folder/subfolder/document.pdf`  
**Result**: `filename = "folder"` ❌ (loses the rest)

#### The Solution: `:path` Converter

Using Starlette's path converter:

```python
@app.get("/images/{image_path:path}")  # ✅ Captures entire path
async def serve_image(image_path: str):
    return {"image_path": image_path}
```

**URL**: `/images/productos/laptops/gaming.jpg`  
**Result**: `image_path = "productos/laptops/gaming.jpg"` ✅

#### Real-World Use Cases

```
File Server Structure:
/static/
  ├── documentos/
  │   ├── manual.pdf
  │   └── guias/
  │       └── instalacion.pdf
  ├── imagenes/
  │   ├── logo.png
  │   └── fotos/
  │       └── equipo.jpg
  └── videos/
      └── tutoriales/
          └── api-usage.mp4
```

**Working URLs:**

- `/images/documentos/manual.pdf` → Serves the PDF
- `/images/imagenes/fotos/equipo.jpg` → Serves the image
- `/images/videos/tutoriales/api-usage.mp4` → Serves the video

#### Important Notes

1. **Order matters**: Specific routes must come before path converters

   ```python
   @app.get("/images/config")        # ✅ Specific first
   @app.get("/images/{path:path}")   # ✅ Generic last
   ```

2. **Leading slash**: For paths starting with `/`, use double slash in URL

   ```
   URL: /images//home/user/file.txt
   Result: path = "/home/user/file.txt"
   ```

3. **Common applications**:
   - File servers (like Google Drive)
   - Documentation systems (like GitBook)
   - Repository browsers (like GitHub)
   - Media streaming services

# FastAPI Scaffolding Project

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
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── test_endpoints.md    # Curl commands for testing endpoints
├── test_endpoints.bat   # Batch script for automated testing
└── README.md            # This file
```

## Next Steps

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

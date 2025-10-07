from typing import Annotated, List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Query
import httpx
import base64
from routers import users, items, models

app = FastAPI(
    title="FastAPI Scaffolding Project",
    description="A well-organized FastAPI application with routers",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(items.router)
app.include_router(models.router)

class HelloResponse(BaseModel):
    Hello: str

@app.get("/", response_model=HelloResponse)
def read_root():
    return {"Hello": "World"}

@app.get("/datetime")
def get_datetime():
    from datetime import datetime
    return {
        "timestamp": datetime.now(),
    }

@app.get("/images/{image_path:path}")
async def serve_image(image_path: str):
    """
    Serve images from different folders
    
    Useful examples:
    - /images/products/laptop.jpg
    - /images/users/avatars/juan.png
    - /images/blog/2024/article-1/cover.jpg
    """
    # In real life, here you would verify that the file exists
    # and return FileResponse(f"/static/images/{image_path}")
    
    return {
        "image_path": image_path,
        "full_url": f"https://myserver.com/static/images/{image_path}",
        "type": "image",
        "folder": image_path.split('/')[0] if '/' in image_path else "root"
    }

@app.get("/external/post/{post_id}")
async def get_external_post(post_id: int):
    """
    Get a post from an external API (DummyJSON) - Example of async/await
    
    This endpoint demonstrates:
    - How to make external API calls with httpx and await
    - Error handling for external services
    - Real use case for async/await in FastAPI
    
    Example: /external/post/1
    """
    try:
        async with httpx.AsyncClient() as client:
            # This is where we NEED await - external API call
            response = await client.get(f"https://dummyjson.com/posts/{post_id}")
            
            if response.status_code == 404:
                raise HTTPException(status_code=404, detail="Post not found in external API")
            
            response.raise_for_status()  # Raises exception for bad status codes
            post_data = response.json()
            
            # Add some extra info to show we processed it
            return {
                "source": "DummyJSON API",
                "post_id": post_id,
                "title": post_data.get("title"),
                "body": post_data.get("body"),
                "user_id": post_data.get("userId"),
                "tags": post_data.get("tags", []),
                "reactions": post_data.get("reactions", {}),
                "api_response_time": f"{response.elapsed.total_seconds():.3f}s",
                "status": "success"
            }
        # Thanks to the 'with', the connection is closed automatically here
            
    except httpx.RequestError as e:
        raise HTTPException(status_code=503, detail=f"External API unavailable: {str(e)}")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"External API error: {e.response.text}")

@app.get("/convert/filename/{filename}")
async def convert_filename_encoding(filename: str):
    """
    Demonstrate string ↔ bytes conversion - Example of encoding/decoding
    
    This endpoint demonstrates:
    - Converting string to bytes (encode)
    - Converting bytes back to string (decode)
    - Base64 encoding for safe transport
    - Real use case for filename processing
    
    Example: /convert/filename/archivo1.jpg
    """
    try:
        # 1. Start with string filename (what user provides)
        original_string = filename
        
        # 2. String → Bytes (encode to UTF-8)
        filename_bytes = original_string.encode('utf-8')
        
        # 3. It converts to Base64 for safe transport/storage
        base64_encoded = base64.b64encode(filename_bytes).decode('ascii')
        
        # 4. Now let's reverse the process...
        # Base64 → Bytes
        decoded_from_base64 = base64.b64decode(base64_encoded.encode('ascii'))
        
        # 5. Bytes → String (decode from UTF-8)
        reconstructed_string = decoded_from_base64.decode('utf-8')
        
        # 6. Demonstrate some properties of bytes
        byte_values = list(filename_bytes)  # Show individual byte values
        
        return {
            "original_filename": original_string,
            "encoding_process": {
                "step_1_string": original_string,
                "step_2_bytes_repr": str(filename_bytes),  # String representation of bytes
                "step_3_base64": base64_encoded,
                "step_4_back_to_bytes": str(decoded_from_base64),
                "step_5_back_to_string": reconstructed_string
            },
            "byte_analysis": {
                "total_bytes": len(filename_bytes),
                "byte_values": byte_values,
                "first_byte": filename_bytes[0] if filename_bytes else None,
                "last_byte": filename_bytes[-1] if filename_bytes else None
            },
            "verification": {
                "strings_match": original_string == reconstructed_string,
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
        
    except UnicodeError as e:
        raise HTTPException(status_code=400, detail=f"Encoding error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Conversion error: {str(e)}")

@app.get("/convert/image-simulation")
async def simulate_image_processing():
    """
    Simulate image processing with bytes - Real-world example
    
    This endpoint demonstrates:
    - How images are handled as bytes in real applications
    - String metadata vs bytes content
    - Base64 encoding for image transmission
    - Real use case scenarios
    
    Example: GET /convert/image-simulation
    """
    try:
        # Simulate an uploaded image (in reality this would come from UploadFile)
        image_metadata = {
            "filename": "profile_photo.jpg",
            "content_type": "image/jpeg",
            "size_kb": 245
        }
        
        # Simulate smaller image content as bytes
        simulated_image_bytes = b'\xff\xd8\xff\xe0JFIF'
        
        # Step 1: String metadata (filename) → Bytes
        filename_bytes = image_metadata["filename"].encode('utf-8')
        
        # Step 2: Image bytes → Base64 (for JSON transmission)
        image_base64 = base64.b64encode(simulated_image_bytes).decode('ascii')
        
        # Simplified response for better Postman compatibility
        return {
            "status": "success",
            "image_info": {
                "filename": image_metadata["filename"],
                "content_type": image_metadata["content_type"],
                "size_bytes": len(simulated_image_bytes)
            },
            "conversions": {
                "filename_to_bytes": {
                    "original": image_metadata["filename"],
                    "bytes_length": len(filename_bytes),
                    "first_byte": filename_bytes[0] if filename_bytes else None
                },
                "image_to_base64": {
                    "bytes_sample": str(simulated_image_bytes),
                    "base64_result": image_base64,
                    "base64_length": len(image_base64)
                }
            },
            "byte_analysis": {
                "total_bytes": len(simulated_image_bytes),
                "header_bytes": list(simulated_image_bytes[:5]),
                "is_jpeg": simulated_image_bytes.startswith(b'\xff\xd8'),
                "is_png": simulated_image_bytes.startswith(b'\x89PNG')
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
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")

# See the difference between having a list of queries vs many query parameters defined (between multiple_queries and various_queries):
@app.get("/multiple-queries/")
async def multiple_queries(q: Annotated[list[str] | None, Query()] = None):
    """
    Example of multiple query parameters with the same name
    
    - **q**: List of query strings (e.g. ?q=foo&q=bar)
    
    Example: /multiple-queries/?q=apple&q=banana&q=cherry
    """
    return {"queries": q}

@app.get("/various-queries/")
async def various_queries(
    q: Annotated[str | None, Query(min_length=3, max_length=50)] = None,
    page: int = 1,
    size: int = 10,
    sort: Annotated[str, Query(pattern="^(asc|desc)$")] = "asc"
):
    """
    Example of various query parameters with validation
    
    - **q**: Optional search query (min 3 chars, max 50)
    - **page**: Page number (default 1)
    - **size**: Page size (default 10)
    - **sort**: Sort order ("asc" or "desc", default "asc")
    
    Example: /various-queries/?q=fastapi&page=2&size=5&sort=desc
    """
    return {
        "query": q,
        "page": page,
        "size": size,
        "sort": sort
    }

# This endpoint must go at the end to avoid conflicts with other endpoints
@app.get("/{name}", response_model=HelloResponse)
def read_root_name(name: str):
    return {"Hello": name}


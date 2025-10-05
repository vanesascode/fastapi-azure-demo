import os
from dotenv import load_dotenv

# Load environment variables from .env file - Run: python env_example.py
load_dotenv()

name = os.getenv("MY_NAME", "World")
debug = os.getenv("DEBUG", "False")
api_version = os.getenv("API_VERSION", "unknown")
secret_message = os.getenv("SECRET_MESSAGE", "No secret found")

print(f"Hello {name} from Python")
print(f"Debug mode: {debug}")
print(f"API Version: {api_version}")
print(f"Secret: {secret_message}")
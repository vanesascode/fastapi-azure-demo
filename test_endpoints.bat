@echo off
@echo off
REM ================================================================
REM FastAPI Complete Endpoints Batch Testing Script
REM ================================================================
REM 
REM WHAT IS THIS FILE?
REM This is a Windows batch script (.bat) that automatically tests
REM ALL FastAPI endpoints from all routers in sequence. It combines
REM all tests from test_main_endpoints.md, test_items_endpoints.md,
REM test_users_endpoints.md, and test_models_endpoints.md into one
REM automated test suite.
REM
REM HOW TO USE:
REM 1. Make sure your FastAPI server is running:
REM    - Open PowerShell in the project directory
REM    - Run: .\scaffolding\Scripts\activate
REM    - Run: fastapi dev main.py
REM    - Server should be running on http://127.0.0.1:8000
REM
REM 2. Run this batch file:
REM    - Double-click this file in Windows Explorer, OR
REM    - In PowerShell/CMD, run: .\test_endpoints.bat
REM
REM WHAT IT TESTS:
REM - Main endpoints (/, /datetime, /{name}, /images/*)
REM - Items CRUD operations (/items/*)
REM - Users CRUD operations (/users/*)
REM - Models enum validation (/models/*)
REM - Cross-router functionality (/users/{id}/items/{id})
REM - Error handling and validation
REM
REM IMPORTANT NOTES:
REM - This uses simplified curl syntax that works in PowerShell
REM - Some requests will show errors (404, validation) - this is normal!
REM - The script tests both success and error cases
REM - For POST/PUT operations, see the individual test_*.md files
REM ================================================================
echo ================================================================
echo FastAPI Complete Test Suite
echo ================================================================
echo.

echo ================================
echo TESTING MAIN ENDPOINTS
echo ================================
echo.

echo 1. Root endpoint:
curl http://127.0.0.1:8000/
echo.

echo 2. DateTime endpoint:
curl http://127.0.0.1:8000/datetime
echo.

echo 3. Dynamic name endpoint:
curl http://127.0.0.1:8000/carlos
echo.

echo 4. Image path converter:
curl "http://127.0.0.1:8000/images/products/laptop.jpg"
echo.

echo 5. Image nested path:
curl "http://127.0.0.1:8000/images/users/avatars/john.png"
echo.

echo ================================
echo TESTING ITEMS ENDPOINTS
echo ================================
echo.

echo 6. Get all items (default pagination):
curl http://127.0.0.1:8000/items/
echo.

echo 7. Get limited items:
curl "http://127.0.0.1:8000/items/?limit=3"
echo.

echo 8. Get items with skip and limit:
curl "http://127.0.0.1:8000/items/?skip=3&limit=2"
echo.

echo 9. Get single item (basic):
curl http://127.0.0.1:8000/items/1
echo.

echo 10. Get item with details:
curl "http://127.0.0.1:8000/items/1?include_details=true"
echo.

echo 11. Get item with simple format:
curl "http://127.0.0.1:8000/items/5?format_type=simple"
echo.

echo 12. Get item with detailed format:
curl "http://127.0.0.1:8000/items/5?format_type=detailed"
echo.

echo 13. Search items by name:
curl "http://127.0.0.1:8000/items/search?q=laptop"
echo.

echo 14. Search items with price range:
curl "http://127.0.0.1:8000/items/search?q=phone&min_price=100&max_price=800"
echo.

echo 15. Test non-existent item (should show 404 error):
curl http://127.0.0.1:8000/items/999
echo.

echo 16. Test invalid item ID (should show validation error):
curl http://127.0.0.1:8000/items/abc
echo.

echo ================================
echo TESTING USERS ENDPOINTS
echo ================================
echo.

echo 17. Get all users:
curl http://127.0.0.1:8000/users/
echo.

echo 18. Get single user:
curl http://127.0.0.1:8000/users/1
echo.

echo 19. Get user's item (cross-router):
curl http://127.0.0.1:8000/users/1/items/1
echo.

echo 20. Get user's item with query parameter:
curl "http://127.0.0.1:8000/users/1/items/1?q=gaming"
echo.

echo 21. Get user's item (short version):
curl "http://127.0.0.1:8000/users/1/items/1?short=true"
echo.

echo 22. Test non-existent user (should show 404 error):
curl http://127.0.0.1:8000/users/999
echo.

echo 23. Test non-existent item for user (should show 404 error):
curl http://127.0.0.1:8000/users/1/items/999
echo.

echo 24. Test non-existent user for item (should show 404 error):
curl http://127.0.0.1:8000/users/999/items/1
echo.

echo ================================
echo TESTING MODELS ENDPOINTS
echo ================================
echo.

echo 25. Get alexnet model:
curl http://127.0.0.1:8000/models/alexnet
echo.

echo 26. Get lenet model:
curl http://127.0.0.1:8000/models/lenet
echo.

echo 27. Get resnet model:
curl http://127.0.0.1:8000/models/resnet
echo.

echo 28. Test invalid model (should show validation error):
curl http://127.0.0.1:8000/models/invalid_model
echo.

echo ================================
echo TESTING STRING/BYTES CONVERSION ENDPOINTS
echo ================================
echo.

echo 29. External API - Get post 1 (async/await demo):
curl http://127.0.0.1:8000/external/post/1
echo.

echo 30. External API - Test error case:
curl http://127.0.0.1:8000/external/post/999999
echo.

echo 31. Filename encoding conversion:
curl http://127.0.0.1:8000/convert/filename/archivo1.jpg
echo.

echo 32. Filename with special characters:
curl "http://127.0.0.1:8000/convert/filename/file%20with%20spaces.txt"
echo.

echo 33. Image processing simulation:
curl http://127.0.0.1:8000/convert/image-simulation
echo.

echo 34. Simple bytes conversion:
curl http://127.0.0.1:8000/convert/image-simple
echo.

echo 35. Ultra-simple test endpoint:
curl http://127.0.0.1:8000/convert/test
echo.

echo ================================
echo TESTING DOCUMENTATION ENDPOINTS
echo ================================
echo.

echo 36. OpenAPI JSON schema:
curl http://127.0.0.1:8000/openapi.json
echo.

echo ================================================================
echo ALL TESTS COMPLETED!
echo ================================================================
echo.
echo Summary:
echo - Tested 36 different endpoints
echo - Covered all routers: main, items, users, models
echo - Tested string/bytes conversion endpoints
echo - Tested external API integration (async/await)
echo - Tested both success and error cases
echo - Some errors (404, validation) are expected and normal
echo.
echo For POST/PUT/DELETE operations, see individual test files:
echo - test_main_endpoints.md
echo - test_items_endpoints.md  
echo - test_users_endpoints.md
echo - test_models_endpoints.md
echo ================================================================

pause
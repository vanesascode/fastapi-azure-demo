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

echo 4. Testing different item ID with query:
curl -X GET "http://127.0.0.1:8000/items/123?q=example" -H "accept: application/json"
echo.

echo 5. Testing invalid item ID (should show validation error):
curl -X GET "http://127.0.0.1:8000/items/abc" -H "accept: application/json"
echo.

echo All tests completed!
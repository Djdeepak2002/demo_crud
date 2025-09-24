# API Testing Commands for Django CRUD Demo
# Run these commands in PowerShell

# ===============================
# 1. TEST PRODUCTS API
# ===============================

# Get all products
curl -X GET "http://127.0.0.1:8000/api/catalog/products/"

# Create a new product
curl -X POST "http://127.0.0.1:8000/api/catalog/products/" `
  -H "Content-Type: application/json" `
  -d '{
    "name": "iPhone 15",
    "description": "Latest iPhone model",
    "price": 999.99,
    "currency": "USD"
  }'

# Create another product
curl -X POST "http://127.0.0.1:8000/api/catalog/products/" `
  -H "Content-Type: application/json" `
  -d '{
    "name": "Samsung Galaxy S24",
    "description": "Android flagship phone",
    "price": 899.99,
    "currency": "USD"
  }'

# Get a specific product (replace 1 with actual product ID)
curl -X GET "http://127.0.0.1:8000/api/catalog/products/1/"

# Update a product (replace 1 with actual product ID)
curl -X PUT "http://127.0.0.1:8000/api/catalog/products/1/" `
  -H "Content-Type: application/json" `
  -d '{
    "name": "iPhone 15 Pro",
    "description": "Premium iPhone model",
    "price": 1099.99,
    "currency": "USD"
  }'

# Delete a product (replace 1 with actual product ID)
curl -X DELETE "http://127.0.0.1:8000/api/catalog/products/1/"

# ===============================
# 2. TEST EXCHANGE RATES API
# ===============================

# Get all exchange rates
curl -X GET "http://127.0.0.1:8000/api/catalog/rates/"

# Create a new exchange rate
curl -X POST "http://127.0.0.1:8000/api/catalog/rates/" `
  -H "Content-Type: application/json" `
  -d '{
    "base": "USD",
    "target": "INR",
    "rate": 83.25
  }'

# Create another exchange rate
curl -X POST "http://127.0.0.1:8000/api/catalog/rates/" `
  -H "Content-Type: application/json" `
  -d '{
    "base": "USD",
    "target": "EUR",
    "rate": 0.92
  }'

# ===============================
# 3. TEST SALES REPORT
# ===============================

# Get sales report
curl -X GET "http://127.0.0.1:8000/api/catalog/reports/sales/"

# ===============================
# 4. FETCH LIVE EXCHANGE RATES
# ===============================

# This command fetches live exchange rates from an external API
# Run this in the terminal where your Django server is NOT running:
# C:/Users/User/Desktop/demo_crud/venv/Scripts/python.exe manage.py fetch_rates --base USD --target INR
# C:/Users/User/Desktop/demo_crud/venv/Scripts/python.exe manage.py fetch_rates --base USD --target EUR
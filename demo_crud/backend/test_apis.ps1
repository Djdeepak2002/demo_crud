# PowerShell API Testing Script
# More PowerShell-friendly commands using Invoke-RestMethod

Write-Host "=== Django CRUD API Testing ===" -ForegroundColor Green

# Base URL
$baseUrl = "http://127.0.0.1:8000/api/catalog"

Write-Host "`n1. Testing Products API..." -ForegroundColor Yellow

# Get all products
Write-Host "Getting all products..."
try {
    $products = Invoke-RestMethod -Uri "$baseUrl/products/" -Method GET
    Write-Host "Found $($products.count) products" -ForegroundColor Green
    $products | Format-Table -AutoSize
} catch {
    Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
}

# Create a new product
Write-Host "`nCreating a new product..."
$newProduct = @{
    name = "Test Product"
    description = "A test product created via PowerShell"
    price = 29.99
    currency = "USD"
} | ConvertTo-Json

try {
    $created = Invoke-RestMethod -Uri "$baseUrl/products/" -Method POST -Body $newProduct -ContentType "application/json"
    Write-Host "Product created successfully!" -ForegroundColor Green
    $created | Format-List
} catch {
    Write-Host "Error creating product: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host "`n2. Testing Exchange Rates API..." -ForegroundColor Yellow

# Get all exchange rates
Write-Host "Getting all exchange rates..."
try {
    $rates = Invoke-RestMethod -Uri "$baseUrl/rates/" -Method GET
    Write-Host "Found $($rates.count) exchange rates" -ForegroundColor Green
    $rates | Format-Table -AutoSize
} catch {
    Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
}

# Create a new exchange rate
Write-Host "`nCreating a new exchange rate..."
$newRate = @{
    base = "USD"
    target = "GBP"
    rate = 0.79
} | ConvertTo-Json

try {
    $createdRate = Invoke-RestMethod -Uri "$baseUrl/rates/" -Method POST -Body $newRate -ContentType "application/json"
    Write-Host "Exchange rate created successfully!" -ForegroundColor Green
    $createdRate | Format-List
} catch {
    Write-Host "Error creating exchange rate: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host "`n3. Testing Sales Report..." -ForegroundColor Yellow

# Get sales report
try {
    $report = Invoke-RestMethod -Uri "$baseUrl/reports/sales/" -Method GET
    Write-Host "Sales report generated successfully!" -ForegroundColor Green
    Write-Host "Report content type: $($report.GetType().Name)"
} catch {
    Write-Host "Error getting sales report: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host "`n=== Testing Complete ===" -ForegroundColor Green
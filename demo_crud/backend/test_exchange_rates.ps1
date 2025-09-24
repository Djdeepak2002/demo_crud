# Test ExchangeRate-API.com Integration
# Make sure to set your API key in .env file first!

Write-Host "=== Testing ExchangeRate-API.com Integration ===" -ForegroundColor Green

# Base URL
$baseUrl = "http://127.0.0.1:8000/api/catalog"

Write-Host "`n1. Fetching live exchange rate via API endpoint..." -ForegroundColor Yellow

# Test the new live rate fetching endpoint
$rateRequest = @{
    base = "USD"
    target = "INR"
} | ConvertTo-Json

try {
    $liveRate = Invoke-RestMethod -Uri "$baseUrl/rates/fetch_live_rate/" -Method POST -Body $rateRequest -ContentType "application/json"
    Write-Host "Live rate fetched successfully!" -ForegroundColor Green
    $liveRate | Format-List
} catch {
    Write-Host "Error fetching live rate: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Make sure your API key is set in .env file!" -ForegroundColor Yellow
}

Write-Host "`n2. Fetching another currency pair..." -ForegroundColor Yellow

$eurRequest = @{
    base = "USD"
    target = "EUR"
} | ConvertTo-Json

try {
    $eurRate = Invoke-RestMethod -Uri "$baseUrl/rates/fetch_live_rate/" -Method POST -Body $eurRequest -ContentType "application/json"
    Write-Host "EUR rate fetched successfully!" -ForegroundColor Green
    $eurRate | Format-List
} catch {
    Write-Host "Error fetching EUR rate: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host "`n3. Getting all stored exchange rates..." -ForegroundColor Yellow

try {
    $allRates = Invoke-RestMethod -Uri "$baseUrl/rates/" -Method GET
    Write-Host "Found $($allRates.count) stored exchange rates:" -ForegroundColor Green
    $allRates | Format-Table -Property base, target, rate, fetched_at -AutoSize
} catch {
    Write-Host "Error getting rates: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host "`n=== Testing Complete ===" -ForegroundColor Green
# Simple Exchange Rate API Test
Write-Host "=== Simple Exchange Rate API Test ===" -ForegroundColor Green

$baseUrl = "http://127.0.0.1:8000/api/catalog"

Write-Host "`n1. Testing the fetch_live_rate endpoint..." -ForegroundColor Yellow

# Test data for USD to INR
$testData = @{
    base = "USD"
    target = "INR"
} | ConvertTo-Json

Write-Host "Sending request to fetch USD->INR rate..."
Write-Host "URL: $baseUrl/rates/fetch_live_rate/"
Write-Host "Data: $testData"

try {
    $response = Invoke-RestMethod -Uri "$baseUrl/rates/fetch_live_rate/" -Method POST -Body $testData -ContentType "application/json"
    
    Write-Host "`n✅ SUCCESS!" -ForegroundColor Green
    Write-Host "Response:" -ForegroundColor Cyan
    $response | ConvertTo-Json -Depth 3 | Write-Host
    
} catch {
    Write-Host "`n❌ ERROR!" -ForegroundColor Red
    Write-Host "Error Message: $($_.Exception.Message)" -ForegroundColor Red
    
    if ($_.Exception.Response) {
        $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
        $responseBody = $reader.ReadToEnd()
        Write-Host "Response Body: $responseBody" -ForegroundColor Yellow
    }
}

Write-Host "`n2. Checking all stored rates..." -ForegroundColor Yellow

try {
    $allRates = Invoke-RestMethod -Uri "$baseUrl/rates/" -Method GET
    Write-Host "✅ Found rates:" -ForegroundColor Green
    $allRates | Format-Table -Property base, target, rate, fetched_at -AutoSize
} catch {
    Write-Host "❌ Error getting rates: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host "`n=== Test Complete ===" -ForegroundColor Green
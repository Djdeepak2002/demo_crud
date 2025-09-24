from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import redirect

def home_view(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Django CRUD API Dashboard</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                background: white;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                padding: 30px;
            }
            .header {
                text-align: center;
                margin-bottom: 40px;
            }
            .header h1 {
                color: #333;
                font-size: 2.5rem;
                margin-bottom: 10px;
            }
            .header p {
                color: #666;
                font-size: 1.1rem;
            }
            .status {
                background: #d4edda;
                border: 1px solid #c3e6cb;
                color: #155724;
                padding: 15px;
                border-radius: 8px;
                margin-bottom: 30px;
                text-align: center;
                font-weight: bold;
            }
            .api-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }
            .api-card {
                background: #f8f9fa;
                border: 1px solid #e9ecef;
                border-radius: 10px;
                padding: 20px;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .api-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            }
            .api-card h3 {
                color: #495057;
                margin-bottom: 15px;
                font-size: 1.3rem;
            }
            .api-card p {
                color: #6c757d;
                margin-bottom: 15px;
                line-height: 1.5;
            }
            .btn {
                display: inline-block;
                padding: 10px 20px;
                background: #007bff;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                transition: background 0.3s ease;
                margin: 5px;
                font-size: 0.9rem;
            }
            .btn:hover { background: #0056b3; }
            .btn.admin { background: #28a745; }
            .btn.admin:hover { background: #1e7e34; }
            .btn.reports { background: #ffc107; color: #212529; }
            .btn.reports:hover { background: #e0a800; }
            .feature-list {
                list-style: none;
                margin: 15px 0;
            }
            .feature-list li {
                color: #28a745;
                margin: 5px 0;
                padding-left: 20px;
                position: relative;
            }
            .feature-list li:before {
                content: "✓";
                position: absolute;
                left: 0;
                font-weight: bold;
            }
            .quick-stats {
                background: #e9ecef;
                border-radius: 10px;
                padding: 20px;
                margin-top: 30px;
            }
            .stats-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
            }
            .stat-item {
                background: white;
                padding: 15px;
                border-radius: 8px;
                text-align: center;
            }
            .stat-value {
                font-size: 2rem;
                font-weight: bold;
                color: #007bff;
            }
            .stat-label {
                color: #6c757d;
                font-size: 0.9rem;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🚀 Django CRUD API Dashboard</h1>
                <p>Complete API Testing Interface - Server Running Successfully</p>
            </div>
            
            <div class="status">
                🟢 Server Status: ONLINE - Django 5.2.6 with PostgreSQL Database
            </div>
            
            <div class="api-grid">
                <div class="api-card">
                    <h3>🏠 API Root</h3>
                    <p>Main API endpoint with Django REST Framework browsable interface. Start here to explore all available endpoints.</p>
                    <ul class="feature-list">
                        <li>Interactive API documentation</li>
                        <li>Endpoint discovery</li>
                        <li>Authentication info</li>
                    </ul>
                    <a href="/api/catalog/" class="btn">Open API Root</a>
                </div>
                
                <div class="api-card">
                    <h3>📦 Products API</h3>
                    <p>Complete CRUD operations for product management. Create, read, update, delete products with sales tracking.</p>
                    <ul class="feature-list">
                        <li>Full CRUD operations</li>
                        <li>Sales increment feature</li>
                        <li>2 products in database</li>
                        <li>Stock management</li>
                    </ul>
                    <a href="/api/catalog/products/" class="btn">View Products</a>
                    <a href="/api/catalog/products/?format=json" class="btn">JSON View</a>
                </div>
                
                <div class="api-card">
                    <h3>💱 Exchange Rates API</h3>
                    <p>Live exchange rate data from ExchangeRate-API.com. View current rates and fetch live updates.</p>
                    <ul class="feature-list">
                        <li>Live rate fetching</li>
                        <li>7 currency pairs stored</li>
                        <li>Real-time updates</li>
                        <li>API integration</li>
                    </ul>
                    <a href="/api/catalog/rates/" class="btn">View Rates</a>
                    <a href="/api/catalog/rates/?format=json" class="btn">JSON View</a>
                </div>
                
                <div class="api-card">
                    <h3>🔧 Admin Panel</h3>
                    <p>Django admin interface for complete data management. Full administrative access to all models.</p>
                    <ul class="feature-list">
                        <li>User management</li>
                        <li>Data administration</li>
                        <li>Product management</li>
                        <li>Exchange rate monitoring</li>
                    </ul>
                    <a href="/admin/" class="btn admin">Admin Panel</a>
                    <small style="display: block; margin-top: 10px; color: #6c757d;">
                        👤 Username: admin | 🔑 Password: admin123
                    </small>
                </div>
                
                <div class="api-card">
                    <h3>📊 Reports</h3>
                    <p>Sales reporting and analytics dashboard. View comprehensive sales data and statistics.</p>
                    <ul class="feature-list">
                        <li>Sales reports</li>
                        <li>Product analytics</li>
                        <li>Custom templates</li>
                        <li>Export capabilities</li>
                    </ul>
                    <a href="/api/catalog/reports/sales/" class="btn reports">Sales Report</a>
                </div>
            </div>
            
            <div class="quick-stats">
                <h3>📈 Current Database Stats</h3>
                <div class="stats-grid">
                    <div class="stat-item">
                        <div class="stat-value">2</div>
                        <div class="stat-label">Products</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">7</div>
                        <div class="stat-label">Exchange Rates</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">Live</div>
                        <div class="stat-label">API Updates</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value">Active</div>
                        <div class="stat-label">Server Status</div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """)

urlpatterns = [
    path('', home_view, name='home'),  # Add homepage
    path('admin/', admin.site.urls),
    path('api/catalog/', include('catalog.urls')),  # connect your app
]

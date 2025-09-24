# 🚀 Django CRUD API with Exchange Rates

A comprehensive Django REST API project featuring full CRUD operations for products and live exchange rate integration with PostgreSQL database.

## 🌟 **Project Overview**

This project demonstrates a complete Django REST API with the following capabilities:
- **Full CRUD Operations** for Product management
- **Live Exchange Rate Integration** using ExchangeRate-API.com
- **PostgreSQL Database** for data persistence
- **Django Admin Panel** for easy data management
- **REST API Endpoints** with Django REST Framework
- **Sales Tracking** and analytics capabilities

## 🏗️ **Project Architecture**

```
demo_crud/
├── backend/                    # Django application
│   ├── catalog/               # Main app
│   │   ├── models.py         # Database models (Product, ExchangeRate)
│   │   ├── views.py          # API viewsets and business logic
│   │   ├── serializers.py    # DRF serializers
│   │   ├── urls.py           # URL routing
│   │   ├── admin.py          # Admin panel configuration
│   │   └── management/       # Custom management commands
│   │       └── commands/
│   │           └── fetch_rates.py  # Exchange rate fetching
│   ├── demo_crud/            # Project settings
│   │   ├── settings.py       # Django configuration
│   │   ├── urls.py           # Main URL routing
│   │   └── wsgi.py           # WSGI configuration
│   ├── manage.py             # Django management script
│   ├── requirements.txt      # Python dependencies
│   ├── Dockerfile           # Docker configuration
│   └── docker-compose.yml   # Multi-container setup
├── venv/                     # Virtual environment
└── .env                     # Environment variables
```

## 🛠️ **Technology Stack**

- **Backend:** Django 5.2.6 + Django REST Framework 3.16.1
- **Database:** PostgreSQL with psycopg2-binary
- **API Integration:** ExchangeRate-API.com for live currency rates
- **Environment:** Python 3.10.9
- **Containerization:** Docker & Docker Compose (optional)

## 📊 **Database Models**

### **Product Model**
```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    sales_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
```

### **ExchangeRate Model**
```python
class ExchangeRate(models.Model):
    base = models.CharField(max_length=3)      # e.g., "USD"
    target = models.CharField(max_length=3)    # e.g., "EUR"
    rate = models.DecimalField(max_digits=12, decimal_places=6)
    fetched_at = models.DateTimeField(auto_now_add=True)
```

## 🚀 **Quick Start**

### **Prerequisites**
- Python 3.10+
- PostgreSQL
- ExchangeRate-API.com account (free)

### **1. Clone and Setup**
```bash
git clone <repository-url>
cd demo_crud
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r backend/requirements.txt
```

### **2. Environment Configuration**
Create `.env` file in the backend directory:
```env
EXCHANGE_RATE_API_KEY=your_api_key_here
```

### **3. Database Setup**
```bash
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### **4. Run Development Server**
```bash
python manage.py runserver
```
Server will start at: `http://127.0.0.1:8000/`

## 🔗 **API Endpoints**

### **🏠 Main URLs**
- **API Root:** `http://127.0.0.1:8000/api/catalog/`
- **Admin Panel:** `http://127.0.0.1:8000/admin/`
- **Project Dashboard:** `http://127.0.0.1:8000/`

### **📦 Product API Endpoints**

| Method | URL | Description | Request Body |
|--------|-----|-------------|--------------|
| `GET` | `/api/catalog/products/` | List all products | - |
| `POST` | `/api/catalog/products/` | Create new product | `{"name": "string", "description": "string", "price": "decimal", "stock": integer}` |
| `GET` | `/api/catalog/products/{id}/` | Get specific product | - |
| `PUT` | `/api/catalog/products/{id}/` | Update product (full) | `{"name": "string", "description": "string", "price": "decimal", "stock": integer}` |
| `PATCH` | `/api/catalog/products/{id}/` | Update product (partial) | `{"price": "decimal"}` (any field) |
| `DELETE` | `/api/catalog/products/{id}/` | Delete product | - |
| `POST` | `/api/catalog/products/{id}/increment_sales/` | Increment sales count | `{"qty": integer}` |

### **💱 Exchange Rate API Endpoints**

| Method | URL | Description | Request Body |
|--------|-----|-------------|--------------|
| `GET` | `/api/catalog/rates/` | List all exchange rates | - |
| `POST` | `/api/catalog/rates/` | Create exchange rate | `{"base": "USD", "target": "EUR", "rate": "decimal"}` |
| `GET` | `/api/catalog/rates/{id}/` | Get specific rate | - |
| `PUT` | `/api/catalog/rates/{id}/` | Update rate (full) | `{"base": "USD", "target": "EUR", "rate": "decimal"}` |
| `PATCH` | `/api/catalog/rates/{id}/` | Update rate (partial) | `{"rate": "decimal"}` |
| `DELETE` | `/api/catalog/rates/{id}/` | Delete rate | - |
| `POST` | `/api/catalog/rates/fetch_live_rate/` | Fetch live rate from API | `{"base": "USD", "target": "EUR"}` |

### **📊 Additional Endpoints**
- **Sales Reports:** `/api/catalog/reports/sales/` - Visual sales analytics

## 🧪 **API Usage Examples**

### **Create a Product**
```bash
curl -X POST http://127.0.0.1:8000/api/catalog/products/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "iPhone 15",
    "description": "Latest iPhone model",
    "price": "999.99",
    "stock": 50
  }'
```

### **Fetch Live Exchange Rate**
```bash
curl -X POST http://127.0.0.1:8000/api/catalog/rates/fetch_live_rate/ \
  -H "Content-Type: application/json" \
  -d '{
    "base": "USD",
    "target": "EUR"
  }'
```

### **Update Product Stock**
```bash
curl -X PATCH http://127.0.0.1:8000/api/catalog/products/1/ \
  -H "Content-Type: application/json" \
  -d '{"stock": 25}'
```

## 🌐 **Browser Testing**

### **Django REST Framework Browsable API**
Navigate to any API endpoint in your browser to access the interactive API interface:

1. **Products List:** `http://127.0.0.1:8000/api/catalog/products/`
2. **Exchange Rates:** `http://127.0.0.1:8000/api/catalog/rates/`
3. **Individual Product:** `http://127.0.0.1:8000/api/catalog/products/1/`

### **Admin Panel Access**
1. **URL:** `http://127.0.0.1:8000/admin/`
2. **Login:** Use superuser credentials created during setup
3. **Features:** Full CRUD operations with admin interface

## 🔧 **Management Commands**

### **Fetch Exchange Rates**
```bash
python manage.py fetch_rates USD EUR  # Fetch USD to EUR rate
python manage.py fetch_rates USD INR  # Fetch USD to INR rate
```

## 🐳 **Docker Deployment**

### **Using Docker Compose**
```bash
cd backend
docker-compose up --build
```

### **Manual Docker Build**
```bash
cd backend
docker build -t django-crud-api .
docker run -p 8000:8000 django-crud-api
```

## 📁 **Project Structure Details**

### **Key Files**
- **`models.py`** - Database schema definitions
- **`views.py`** - API business logic and viewsets
- **`serializers.py`** - Data serialization for API responses
- **`urls.py`** - URL routing configuration
- **`admin.py`** - Admin panel customization
- **`settings.py`** - Django project configuration

### **Key Features**
- ✅ **Full CRUD Operations** for both Products and Exchange Rates
- ✅ **Live API Integration** with ExchangeRate-API.com
- ✅ **Django Admin Interface** for easy data management
- ✅ **RESTful API Design** following best practices
- ✅ **Database Relationships** and constraints
- ✅ **Error Handling** and validation
- ✅ **Dockerized** for easy deployment

## 🔐 **Environment Variables**

Required environment variables in `.env` file:
```env
# Exchange Rate API
EXCHANGE_RATE_API_KEY=your_exchangerate_api_key_here

# Database (if using custom settings)
DB_NAME=djangodb
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 **Troubleshooting**

### **Common Issues**

1. **Exchange Rate API not working:**
   - Ensure `EXCHANGE_RATE_API_KEY` is set correctly
   - Use correct URL: `/api/catalog/rates/fetch_live_rate/`

2. **Database connection issues:**
   - Verify PostgreSQL is running
   - Check database credentials in settings

3. **Admin panel empty:**
   - Run migrations: `python manage.py migrate`
   - Create superuser: `python manage.py createsuperuser`

## 📄 **License**

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎯 **Next Steps**

- [ ] Add authentication and authorization
- [ ] Implement pagination for large datasets
- [ ] Add unit tests and integration tests
- [ ] Create API documentation with Swagger/OpenAPI
- [ ] Add caching for exchange rates
- [ ] Implement rate limiting for API endpoints

---

**Built with ❤️ using Django & Django REST Framework**

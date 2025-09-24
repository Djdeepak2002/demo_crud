# 🚀 Django CRUD API with Exchange Rates

A comprehensive Django REST API project featuring full CRUD operations for products and live exchange rate integration with PostgreSQL database.

![Django](https://img.shields.io/badge/Django-5.2.6-green)
![DRF](https://img.shields.io/badge/DRF-3.16.1-blue)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)

## 🌟 **Features**

- ✅ **Full CRUD Operations** for Product management
- ✅ **Live Exchange Rate Integration** using ExchangeRate-API.com
- ✅ **PostgreSQL Database** with proper relationships
- ✅ **Django Admin Panel** for easy data management
- ✅ **REST API Endpoints** with Django REST Framework
- ✅ **Sales Tracking** and increment functionality
- ✅ **Docker Support** for containerized deployment
- ✅ **Interactive API Documentation** via DRF Browsable API

## 🚀 **Quick Start**

### **1. Setup Virtual Environment**
```bash
cd demo_crud
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac
```

### **2. Install Dependencies**
```bash
cd demo_crud/backend
pip install -r requirements.txt
```

### **3. Configure Environment**
Create `.env` file in `demo_crud/backend/`:
```env
EXCHANGE_RATE_API_KEY=your_api_key_from_exchangerate_api_com
```

### **4. Database Setup**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### **5. Run Server**
```bash
python manage.py runserver
```

🎉 **Server running at:** `http://127.0.0.1:8000/`

## 🔗 **API Endpoints**

### **Main URLs**
- **🏠 Dashboard:** `http://127.0.0.1:8000/`
- **📡 API Root:** `http://127.0.0.1:8000/api/catalog/`
- **⚙️ Admin Panel:** `http://127.0.0.1:8000/admin/`

### **Products API**
- **GET/POST** `/api/catalog/products/` - List/Create products
- **GET/PUT/PATCH/DELETE** `/api/catalog/products/{id}/` - Individual product operations
- **POST** `/api/catalog/products/{id}/increment_sales/` - Increment sales count

### **Exchange Rates API**
- **GET/POST** `/api/catalog/rates/` - List/Create exchange rates
- **GET/PUT/PATCH/DELETE** `/api/catalog/rates/{id}/` - Individual rate operations
- **POST** `/api/catalog/rates/fetch_live_rate/` - Fetch live rates from API

## 🏗️ **Project Architecture**

```
demo_crud/
├── demo_crud/backend/          # Django application
│   ├── catalog/               # Main app
│   │   ├── models.py         # Database models
│   │   ├── views.py          # API viewsets
│   │   ├── serializers.py    # DRF serializers
│   │   ├── urls.py           # URL routing
│   │   └── admin.py          # Admin configuration
│   ├── demo_crud/            # Django project settings
│   ├── manage.py             # Django management
│   ├── requirements.txt      # Dependencies
│   └── docker-compose.yml    # Docker setup
├── venv/                     # Virtual environment
└── README.md                 # This file
```

## 🛠️ **Technology Stack**

- **Backend:** Django 5.2.6 + Django REST Framework 3.16.1
- **Database:** PostgreSQL with psycopg2-binary
- **API Integration:** ExchangeRate-API.com
- **Environment:** Python 3.10.9
- **Containerization:** Docker & Docker Compose

## 📊 **Database Models**

### **Product**
- Name, Description, Price, Stock
- Sales count tracking
- Timestamp fields

### **ExchangeRate**
- Base/Target currency codes
- Exchange rate value
- Fetch timestamp

## 🧪 **Testing the API**

### **Using Browser (DRF Browsable API)**
1. Navigate to `http://127.0.0.1:8000/api/catalog/products/`
2. Use forms to CREATE, UPDATE, DELETE products
3. Test exchange rates at `http://127.0.0.1:8000/api/catalog/rates/`

### **Using cURL**
```bash
# Create a product
curl -X POST http://127.0.0.1:8000/api/catalog/products/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Product", "price": "29.99", "stock": 100}'

# Fetch live exchange rate
curl -X POST http://127.0.0.1:8000/api/catalog/rates/fetch_live_rate/ \
  -H "Content-Type: application/json" \
  -d '{"base": "USD", "target": "EUR"}'
```

## 🐳 **Docker Deployment**

```bash
cd demo_crud/backend
docker-compose up --build
```

## 📝 **Documentation**

For detailed documentation, see: `demo_crud/README.md`

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 **License**

MIT License - see the LICENSE file for details.

---

**🚀 Ready to explore the API? Start with:** `http://127.0.0.1:8000/`
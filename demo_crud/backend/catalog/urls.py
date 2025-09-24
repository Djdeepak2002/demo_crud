from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, ExchangeRateViewSet, sales_report

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"rates", ExchangeRateViewSet, basename="rates")

urlpatterns = [
    path("", include(router.urls)),
    path("reports/sales/", sales_report, name="sales_report"),
]

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from .models import Product, ExchangeRate
from .serializers import ProductSerializer, ExchangeRateSerializer
import requests
from django.conf import settings
from django.http import HttpResponse


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("-created_at")
    serializer_class = ProductSerializer

    @action(detail=True, methods=["post"])
    def increment_sales(self, request, pk=None):
        product = self.get_object()
        qty = int(request.data.get("qty", 1))
        product.sales_count += qty
        product.stock = max(product.stock - qty, 0)
        product.save()
        return Response(ProductSerializer(product).data)

class ExchangeRateViewSet(viewsets.ModelViewSet):
    queryset = ExchangeRate.objects.all().order_by("-fetched_at")
    serializer_class = ExchangeRateSerializer
    
    @action(detail=False, methods=['post'])
    def fetch_live_rate(self, request):
        """Fetch live exchange rate from ExchangeRate-API.com"""
        import os
        
        api_key = os.environ.get('EXCHANGE_RATE_API_KEY')
        if not api_key or api_key == 'YOUR_API_KEY_HERE':
            return Response(
                {"error": "API key not configured"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        base = request.data.get('base', 'USD').upper()
        target = request.data.get('target', 'INR').upper()
        
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base}"
        
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                if data.get("result") == "success":
                    conversion_rates = data.get("conversion_rates", {})
                    rate = conversion_rates.get(target)
                    
                    if rate:
                        # Store in database
                        exchange_rate = ExchangeRate.objects.create(
                            base=base,
                            target=target,
                            rate=rate
                        )
                        
                        return Response({
                            "success": True,
                            "message": f"Fetched and stored rate {base}->{target} = {rate}",
                            "data": ExchangeRateSerializer(exchange_rate).data
                        })
                    else:
                        return Response(
                            {"error": f"Currency {target} not available"}, 
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response(
                        {"error": data.get("error-type", "API Error")}, 
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {"error": f"HTTP Error: {resp.status_code}"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        except requests.exceptions.RequestException as e:
            return Response(
                {"error": f"Request failed: {str(e)}"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# Simple page for visualization
def sales_report(request):
    products = Product.objects.all().order_by("created_at")
    labels = [p.name for p in products]
    values = [p.sales_count for p in products]
    return render(request, "catalog/reports.html", {"labels": labels, "values": values})

def index(request):
    return HttpResponse("Catalog API is working!")

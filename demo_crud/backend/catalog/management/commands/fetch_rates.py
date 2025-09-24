from django.core.management.base import BaseCommand
from catalog.models import ExchangeRate
import requests
import os
from django.conf import settings

class Command(BaseCommand):
    help = "Fetch latest exchange rate for a pair and store it using ExchangeRate-API.com"

    def add_arguments(self, parser):
        parser.add_argument("--base", type=str, default="USD", help="Base currency code (e.g., USD)")
        parser.add_argument("--target", type=str, default="INR", help="Target currency code (e.g., INR)")
        parser.add_argument("--all", action="store_true", help="Fetch all available rates for base currency")

    def handle(self, *args, **options):
        api_key = os.environ.get('EXCHANGE_RATE_API_KEY')
        if not api_key or api_key == 'YOUR_API_KEY_HERE':
            self.stdout.write(
                self.style.ERROR("Please set your EXCHANGE_RATE_API_KEY in the .env file")
            )
            return

        base = options["base"].upper()
        target = options["target"].upper()
        
        # API URL for ExchangeRate-API.com
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base}"
        
        self.stdout.write(f"Fetching exchange rates for {base}...")
        
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                
                if data.get("result") == "success":
                    conversion_rates = data.get("conversion_rates", {})
                    
                    if options["all"]:
                        # Store all available rates
                        count = 0
                        for currency, rate in conversion_rates.items():
                            if currency != base:  # Don't store base->base rate
                                ExchangeRate.objects.create(
                                    base=base, 
                                    target=currency, 
                                    rate=rate
                                )
                                count += 1
                        
                        self.stdout.write(
                            self.style.SUCCESS(f"Stored {count} exchange rates for {base}")
                        )
                    else:
                        # Store specific target rate
                        rate = conversion_rates.get(target)
                        if rate:
                            er = ExchangeRate.objects.create(
                                base=base, 
                                target=target, 
                                rate=rate
                            )
                            self.stdout.write(
                                self.style.SUCCESS(f"Stored rate {base}->{target} = {rate}")
                            )
                        else:
                            self.stdout.write(
                                self.style.ERROR(f"Currency {target} not found in response")
                            )
                            available = list(conversion_rates.keys())[:10]  # Show first 10 available
                            self.stdout.write(f"Available currencies: {', '.join(available)}...")
                else:
                    error_type = data.get("error-type", "Unknown error")
                    self.stdout.write(
                        self.style.ERROR(f"API Error: {error_type}")
                    )
            else:
                self.stdout.write(
                    self.style.ERROR(f"HTTP Error: {resp.status_code}")
                )
        
        except requests.exceptions.RequestException as e:
            self.stdout.write(
                self.style.ERROR(f"Request failed: {str(e)}")
            )

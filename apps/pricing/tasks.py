from celery import shared_task
from django.utils.timezone import now
from apps.stocks.models import Stock
from .models import StockPrice

@shared_task
def fetch_prices():
    for stock in Stock.objects.filter(is_active=True):
        StockPrice.objects.create(
            stock=stock,
            price=100.00,
            source="mock_api",
            timestamp=now()
        )

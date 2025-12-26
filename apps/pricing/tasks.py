from celery import shared_task
from .models import StockPrice
from apps.alerts.tasks import evaluate_alerts_for_symbol


@shared_task
def fetch_prices():
    symbol = "AAPL"
    price = 192.50

    StockPrice.objects.create(
        symbol=symbol,
        price=price
    )

    evaluate_alerts_for_symbol.delay(symbol, str(price))

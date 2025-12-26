from celery import shared_task
from decimal import Decimal

from .models import Alert
from .services import evaluate_alert


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=10)
def evaluate_alerts_for_symbol(self, symbol: str, price: str):
    alerts = Alert.objects.filter(
        symbol=symbol,
        is_active=True,
    )

    for alert in alerts:
        evaluate_alert(alert, Decimal(price))

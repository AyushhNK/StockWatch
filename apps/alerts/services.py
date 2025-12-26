from decimal import Decimal
from django.utils import timezone

from .models import Alert
from apps.pricing.models import StockPrice
from apps.notifications.services import send_notification


def evaluate_alert(alert: Alert, current_price: Decimal):
    triggered = False
    message = ""

    if alert.condition == Alert.Condition.PRICE_ABOVE:
        if current_price > alert.threshold:
            triggered = True
            message = f"{alert.symbol} price crossed above {alert.threshold}"

    elif alert.condition == Alert.Condition.PRICE_BELOW:
        if current_price < alert.threshold:
            triggered = True
            message = f"{alert.symbol} price dropped below {alert.threshold}"

    elif alert.condition == Alert.Condition.PERCENT_CHANGE:
        past_price = StockPrice.objects.filter(
            symbol=alert.symbol,
            created_at__gte=timezone.now()
            - timezone.timedelta(minutes=alert.time_window_minutes)
        ).order_by("created_at").first()

        if past_price:
            change = (
                (current_price - past_price.price) / past_price.price
            ) * 100

            if abs(change) >= alert.threshold:
                triggered = True
                message = (
                    f"{alert.symbol} changed {change:.2f}% "
                    f"in last {alert.time_window_minutes} minutes"
                )

    if triggered:
        alert.last_triggered_at = timezone.now()
        alert.save(update_fields=["last_triggered_at"])

        send_notification(alert.user, message)

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Alert(models.Model):
    class Condition(models.TextChoices):
        PRICE_ABOVE = "price_above"
        PRICE_BELOW = "price_below"
        PERCENT_CHANGE = "percent_change"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)

    condition = models.CharField(
        max_length=30,
        choices=Condition.choices
    )

    threshold = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    time_window_minutes = models.IntegerField(
        null=True,
        blank=True,
        help_text="Used only for percent change alerts"
    )

    is_active = models.BooleanField(default=True)
    last_triggered_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.symbol} - {self.condition}"

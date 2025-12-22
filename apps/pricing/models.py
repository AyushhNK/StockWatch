from django.db import models
from apps.stocks.models import Stock

class StockPrice(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

    class Meta:
        indexes = [
            models.Index(fields=["stock", "timestamp"]),
        ]

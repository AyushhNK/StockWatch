from django.db import models
from apps.accounts.models import User
from apps.stocks.models import Stock

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class WatchlistItem(models.Model):
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    alert_thresholds = models.JSONField(default=dict)

    class Meta:
        unique_together = ("watchlist", "stock")

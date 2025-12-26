from rest_framework import serializers
from .models import Watchlist, WatchlistItem
from apps.stocks.models import Stock
class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = ["id", "name", "is_default", "created_at"]
        read_only_fields = ["id", "created_at"]
class WatchlistItemSerializer(serializers.ModelSerializer):
    symbol = serializers.CharField(write_only=True)
    stock_name = serializers.CharField(source="stock.name", read_only=True)
    stock_symbol = serializers.CharField(source="stock.symbol", read_only=True)

    class Meta:
        model = WatchlistItem
        fields = [
            "id",
            "symbol",
            "stock_symbol",
            "stock_name",
            "alert_thresholds"
        ]

    def create(self, validated_data):
        symbol = validated_data.pop("symbol")
        try:
            stock = Stock.objects.get(symbol=symbol)
        except Stock.DoesNotExist:
            raise serializers.ValidationError({"symbol": "Stock not found"})

        validated_data["stock"] = stock
        return super().create(validated_data)

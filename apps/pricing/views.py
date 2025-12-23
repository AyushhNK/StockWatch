from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.stocks.models import Stock
from .models import StockPrice
from .serializers import StockPriceSerializer

class LatestPriceView(APIView):
    def get(self, request, symbol):
        stock = get_object_or_404(Stock, symbol=symbol)
        price = StockPrice.objects.filter(stock=stock).latest("timestamp")
        return Response(StockPriceSerializer(price).data)

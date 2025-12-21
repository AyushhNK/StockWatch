from rest_framework.views import APIView
from rest_framework.response import Response
from stocks.models import StockPrice
from django.db.models import Avg, Max, Min

class StockAnalyticsAPIView(APIView):
    def get(self, request, symbol):
        prices = StockPrice.objects.filter(stock__symbol=symbol)

        return Response({
            "average": prices.aggregate(Avg('price'))['price__avg'],
            "maximum": prices.aggregate(Max('price'))['price__max'],
            "minimum": prices.aggregate(Min('price'))['price__min'],
        })

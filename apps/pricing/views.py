from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.pricing.models import StockPrice


class LatestPriceView(APIView):

    def get(self, request, symbol):
        price = (
            StockPrice.objects
            .filter(symbol=symbol)
            .order_by('-created_at')
            .first()
        )

        if not price:
            return Response(
                {"detail": f"No price data found for {symbol}"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response({
            "symbol": price.symbol,
            "price": price.price,
            "timestamp": price.created_at
        })

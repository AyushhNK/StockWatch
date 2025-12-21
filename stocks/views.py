from rest_framework import generics, permissions
from .models import Stock, Watchlist
from .serializers import StockSerializer, WatchlistSerializer

class StockListAPIView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class AddToWatchlistAPIView(generics.CreateAPIView):
    serializer_class = WatchlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserWatchlistAPIView(generics.ListAPIView):
    serializer_class = WatchlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Watchlist.objects.filter(user=self.request.user)

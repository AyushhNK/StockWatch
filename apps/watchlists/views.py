from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Watchlist
from .serializers import WatchlistSerializer

class WatchlistViewSet(ModelViewSet):
    queryset = Watchlist.objects.all()   # ✅ REQUIRED
    serializer_class = WatchlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

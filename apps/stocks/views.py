from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import Stock
from .serializers import StockSerializer

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdminUser]

from django.urls import path
from .views import StockAnalyticsAPIView

urlpatterns = [
    path('<str:symbol>/', StockAnalyticsAPIView.as_view()),
]

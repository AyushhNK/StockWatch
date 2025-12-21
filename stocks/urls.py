from django.urls import path
from .views import StockListAPIView, AddToWatchlistAPIView, UserWatchlistAPIView

urlpatterns = [
    path('', StockListAPIView.as_view()),
    path('watchlist/add/', AddToWatchlistAPIView.as_view()),
    path('watchlist/', UserWatchlistAPIView.as_view()),
]

from django.urls import path
from .views import LatestPriceView

urlpatterns = [
    path("latest/<str:symbol>/", LatestPriceView.as_view()),
]

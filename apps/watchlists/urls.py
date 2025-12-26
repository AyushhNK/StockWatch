from django.urls import path
from .views import *

urlpatterns = [
    path("", WatchlistListView.as_view()),
    path("create/", WatchlistCreateView.as_view()),
    path("<int:watchlist_id>/", WatchlistDetailView.as_view()),
    path("<int:watchlist_id>/add/", AddToWatchlistView.as_view()),
    path("<int:watchlist_id>/remove/<str:symbol>/", RemoveFromWatchlistView.as_view()),
    path("<int:watchlist_id>/set-default/", SetDefaultWatchlistView.as_view()),
]

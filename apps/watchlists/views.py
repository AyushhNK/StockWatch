from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Watchlist, WatchlistItem
from .serializers import WatchlistSerializer, WatchlistItemSerializer

class WatchlistCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = WatchlistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        is_default = serializer.validated_data.get("is_default", False)

        if is_default:
            Watchlist.objects.filter(
                user=request.user,
                is_default=True
            ).update(is_default=False)

        watchlist = serializer.save(user=request.user)

        return Response(
            WatchlistSerializer(watchlist).data,
            status=status.HTTP_201_CREATED
        )

class WatchlistListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        watchlists = Watchlist.objects.filter(user=request.user)
        serializer = WatchlistSerializer(watchlists, many=True)
        return Response(serializer.data)

class AddToWatchlistView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, watchlist_id):
        watchlist = get_object_or_404(
            Watchlist,
            id=watchlist_id,
            user=request.user
        )

        serializer = WatchlistItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        stock_symbol = serializer.validated_data["symbol"]

        if WatchlistItem.objects.filter(
            watchlist=watchlist,
            stock__symbol=stock_symbol
        ).exists():
            return Response(
                {"detail": "Stock already in watchlist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        item = serializer.save(watchlist=watchlist)

        return Response(
            WatchlistItemSerializer(item).data,
            status=status.HTTP_201_CREATED
        )

class RemoveFromWatchlistView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, watchlist_id, symbol):
        watchlist = get_object_or_404(
            Watchlist,
            id=watchlist_id,
            user=request.user
        )

        item = get_object_or_404(
            WatchlistItem,
            watchlist=watchlist,
            stock__symbol=symbol
        )

        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SetDefaultWatchlistView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, watchlist_id):
        watchlist = get_object_or_404(
            Watchlist,
            id=watchlist_id,
            user=request.user
        )

        Watchlist.objects.filter(
            user=request.user,
            is_default=True
        ).update(is_default=False)

        watchlist.is_default = True
        watchlist.save()

        return Response({"detail": "Default watchlist updated"})
    
    
class WatchlistDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, watchlist_id):
        watchlist = get_object_or_404(
            Watchlist,
            id=watchlist_id,
            user=request.user
        )

        items = WatchlistItem.objects.filter(watchlist=watchlist)
        items_serializer = WatchlistItemSerializer(items, many=True)

        return Response({
            "watchlist": WatchlistSerializer(watchlist).data,
            "stocks": items_serializer.data
        })

from rest_framework.generics import ListAPIView, CreateAPIView, \
UpdateAPIView, DestroyAPIView, RetrieveAPIView


from rest_framework.permissions import IsAuthenticated
from api.user.serializers import favouriteplaylist_serializer
from rest_framework import status 
from rest_framework.response import Response
from apps.users.models import Favouriteplaylist


class FavouriteplaylistListApiView(ListAPIView):
    queryset = Favouriteplaylist.objects.all()
    serializer_class = favouriteplaylist_serializer.FavouriteplaylistListSerializer
    permission_classes = [IsAuthenticated]


class FavouriteplaylistCreateApiView(CreateAPIView):
    queryset = Favouriteplaylist.objects.all()
    serializer_class = favouriteplaylist_serializer.FavouriteplaylistCreateSerializer
    permission_classes = [IsAuthenticated]



class FavouriteplaylistUpdateApiView(UpdateAPIView):
    queryset = Favouriteplaylist.objects.all()
    serializer_class = favouriteplaylist_serializer.FavouriteplaylistCreateSerializer
    permission_classes = [IsAuthenticated]


class FavouriteplaylistRetriveApiView(RetrieveAPIView):
    queryset = Favouriteplaylist.objects.all()
    serializer_class = favouriteplaylist_serializer.FavouriteplaylistListSerializer
    permission_classes = [IsAuthenticated]



class FavouriteplaylistDestroyApiView(DestroyAPIView):
    queryset = Favouriteplaylist.objects.all()
    permission_classes = [IsAuthenticated]


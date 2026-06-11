from rest_framework.generics import ListAPIView, CreateAPIView, \
UpdateAPIView, DestroyAPIView, RetrieveAPIView


from rest_framework.permissions import IsAuthenticated
from api.user.serializers import favourite_serializer
from rest_framework import status 
from rest_framework.response import Response
from apps.users.models import Favourite 


class FavouriteListApiView(ListAPIView):
    queryset = Favourite.objects.all()
    serializer_class = favourite_serializer.FavouriteListSerializer
    permission_classes = [IsAuthenticated]


class FavouriteCreateApiView(CreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = favourite_serializer.FavouriteCreateSerializer
    permission_classes = [IsAuthenticated]



class FavouriteUpdateApiView(UpdateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = favourite_serializer.FavouriteCreateSerializer
    permission_classes = [IsAuthenticated]


class FavouriteRetriveApiView(RetrieveAPIView):
    queryset = Favourite.objects.all()
    serializer_class = favourite_serializer.FavouriteListSerializer
    permission_classes = [IsAuthenticated]



class FavouriteDestroyApiView(DestroyAPIView):
    queryset = Favourite.objects.all()
    permission_classes = [IsAuthenticated]


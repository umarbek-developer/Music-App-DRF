from rest_framework.generics import ListAPIView, CreateAPIView, \
UpdateAPIView, DestroyAPIView, RetrieveAPIView


from rest_framework.permissions import IsAuthenticated
from api.user.serializers import playlist_serializer
from rest_framework import status 
from rest_framework.response import Response
from apps.music.models import Playlist 


class PlaylistListApiView(ListAPIView):
    queryset = Playlist.objects.all()
    serializer_class = playlist_serializer.PlaylistListSerializer
    permission_classes = [IsAuthenticated]


class PlaylistCreateApiView(CreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = playlist_serializer.PlaylistCreateSerializer
    permission_classes = [IsAuthenticated]



class PlaylistUpdateApiView(UpdateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = playlist_serializer.PlaylistCreateSerializer
    permission_classes = [IsAuthenticated]


class PlaylistRetriveApiView(RetrieveAPIView):
    queryset = Playlist.objects.all()
    serializer_class = playlist_serializer.PlaylistListSerializer
    permission_classes = [IsAuthenticated]



class PlaylistDestroyApiView(DestroyAPIView):
    queryset = Playlist.objects.all()
    permission_classes = [IsAuthenticated]


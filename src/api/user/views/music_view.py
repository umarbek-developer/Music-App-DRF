from rest_framework.generics import ListAPIView, CreateAPIView, \
UpdateAPIView, DestroyAPIView, RetrieveAPIView


from rest_framework.permissions import IsAuthenticated
from api.user.serializers import music_serializer
from rest_framework import status 
from rest_framework.response import Response
from apps.music.models import Music 


class MusicListApiView(ListAPIView):
    queryset = Music.objects.all()
    serializer_class = music_serializer.MusicListSerializer
    permission_classes = [IsAuthenticated]


class MusicCreateApiView(CreateAPIView):
    queryset = Music.objects.all()
    serializer_class = music_serializer.MusicCreateSerializer
    permission_classes = [IsAuthenticated]
    



class MusicUpdateApiView(UpdateAPIView):
    queryset = Music.objects.all()
    serializer_class = music_serializer.MusicCreateSerializer
    permission_classes = [IsAuthenticated]


class MusicRetriveApiView(RetrieveAPIView):
    queryset = Music.objects.all()
    serializer_class = music_serializer.MusicListSerializer
    permission_classes = [IsAuthenticated]



class MusicDestroyApiView(DestroyAPIView):
    queryset = Music.objects.all()
    permission_classes = [IsAuthenticated]


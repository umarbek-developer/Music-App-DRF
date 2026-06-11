from rest_framework.serializers import ModelSerializer
from apps.music.models import Playlist


class PlaylistListSerializer(ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'


class PlaylistCreateSerializer(ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'






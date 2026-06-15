from rest_framework.serializers import ModelSerializer
from apps.music.models import Music 


class MusicListSerializer(ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'


class MusicCreateSerializer(ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'




class MusicUpdateSerializer(ModelSerializer):

    class Meta:
        model = Music 
        fields = ['name', 'is_public', 'picture', 'lirics', 'source', 'playlist']



from rest_framework.serializers import ModelSerializer
from apps.users.models import Favouriteplaylist 


class FavouriteplaylistListSerializer(ModelSerializer):
    class Meta:
        model = Favouriteplaylist
        fields = '__all__'


class FavouriteplaylistCreateSerializer(ModelSerializer):
    class Meta:
        model = Favouriteplaylist
        fields = '__all__'






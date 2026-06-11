from rest_framework.serializers import ModelSerializer
from apps.users.models import Favourite 


class FavouriteListSerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'


class FavouriteCreateSerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'






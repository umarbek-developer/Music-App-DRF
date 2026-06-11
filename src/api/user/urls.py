from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.user.views import music_view


router = DefaultRouter()
router.include_root_view = False

urlpatterns = [
    path('music/', music_view.MusicListApiView.as_view()),
    path('music/create/', music_view.MusicCreateApiView.as_view()),

    # path('', include(router.urls)),
    # path('restaurant/', RestaurantViewset.as_view({'get': 'list','post':'create'}), name='restaurant-detail'),

]

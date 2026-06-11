from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.user.views import music_view
from api.user.views import playlist_view
from api.user.views import favourite_view
from api.user.views import favouriteplaylist_view


router = DefaultRouter()
router.include_root_view = False

urlpatterns = [
# music
    path('music/', music_view.MusicListApiView.as_view()),
    path('music/create/', music_view.MusicCreateApiView.as_view()),
    path('music/detail/<int:pk>/', music_view.MusicRetriveApiView.as_view()),
    path('music/update/<int:pk>/', music_view.MusicUpdateApiView.as_view()),
    path('music/delete/<int:pk>/', music_view.MusicDestroyApiView.as_view()),


# playlist
    path('playlist/', playlist_view.PlaylistListApiView.as_view()),
    path('playlist/create/', playlist_view.PlaylistCreateApiView.as_view()),
    path('playlist/detail/<int:pk>/', playlist_view.PlaylistRetriveApiView.as_view()),
    path('playlist/update/<int:pk>/', playlist_view.PlaylistUpdateApiView.as_view()),
    path('playlist/delete/<int:pk>/', playlist_view.PlaylistDestroyApiView.as_view()),


# favourite
    path('favourite/', favourite_view.FavouriteListApiView.as_view()),
    path('favourite/create/', favourite_view.FavouriteCreateApiView.as_view()),
    path('favourite/detail/<int:pk>/', favourite_view.FavouriteRetriveApiView.as_view()),
    path('favourite/update/<int:pk>/', favourite_view.FavouriteUpdateApiView.as_view()),
    path('favourite/delete/<int:pk>/', favourite_view.FavouriteDestroyApiView.as_view()),


# favouriteplaylist 
    path('favouriteplaylist/', favouriteplaylist_view.FavouriteplaylistListApiView.as_view()),
    path('favouriteplaylist/create/', favouriteplaylist_view.FavouriteplaylistCreateApiView.as_view()),
    path('favouriteplaylist/detail/<int:pk>/', favouriteplaylist_view.FavouriteplaylistRetriveApiView.as_view()),
    path('favouriteplaylist/update/<int:pk>/', favouriteplaylist_view.FavouriteplaylistUpdateApiView.as_view()),
    path('favouriteplaylist/delete/<int:pk>/', favouriteplaylist_view.FavouriteplaylistDestroyApiView.as_view()),

    # path('', include(router.urls)),
    # path('restaurant/', RestaurantViewset.as_view({'get': 'list','post':'create'}), name='restaurant-detail'),

]

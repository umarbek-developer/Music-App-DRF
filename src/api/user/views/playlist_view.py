from rest_framework.generics import ListAPIView, CreateAPIView, \
UpdateAPIView, DestroyAPIView, RetrieveAPIView


from rest_framework.permissions import IsAuthenticated
from api.user.serializers import playlist_serializer
from rest_framework import status 
from rest_framework.response import Response
from apps.music.models import Playlist 


class PlaylistListApiView(ListAPIView):
    queryset = Playlist.objects.filter(is_public=True)
    serializer_class = playlist_serializer.PlaylistListSerializer
    permission_classes = [IsAuthenticated]


class PlaylistCreateApiView(CreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = playlist_serializer.PlaylistCreateSerializer
    permission_classes = [IsAuthenticated]


    def create(self, request):
        data = request.data 
        data['author'] = request.user.id 
        ser = self.serializer_class(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
        return Response({"msg": "Playlist created successfully", 
        "data": ser.data
        },
        status=status.HTTP_201_CREATED)



class PlaylistUpdateApiView(UpdateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = playlist_serializer.PlaylistCreateSerializer
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        try:
            request.data.pop("author")
        except: pass
        instance = self.get_object()
        if request.user == instance.author:
            request.data['author'] = request.user.id
            ser = self.serializer_class(instance, data=request.data)
            if ser.is_valid(raise_exception=True):
                ser.save()
            return Response({
                "message": "ok",
                "data": ser.data
            },status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)



    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)




class PlaylistRetriveApiView(RetrieveAPIView):
    queryset = Playlist.objects.all()
    serializer_class = playlist_serializer.PlaylistListSerializer
    permission_classes = [IsAuthenticated]



class PlaylistDestroyApiView(DestroyAPIView):
    queryset = Playlist.objects.all()
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        try:
            request.data.pop("author")
        except: 
            pass
        return super().partial_update(request, *args, **kwargs)
    

    def update(self, request, *args, **kwargs):
        try:
            request.data.pop("author")
        except: 
            pass
        return super().partial_update(request, *args, **kwargs)


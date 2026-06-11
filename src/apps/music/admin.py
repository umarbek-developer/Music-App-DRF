from django.contrib import admin
from apps.music.models import Playlist, Music 

# Register your models here.

admin.site.register(Playlist)
admin.site.register(Music)

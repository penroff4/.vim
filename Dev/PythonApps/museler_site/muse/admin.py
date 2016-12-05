from django.contrib import admin

from .models import Channel, Video, Playlist, PlaylistVideo 

admin.site.register(Channel)
admin.site.register(Video)
admin.site.register(Playlist)
admin.site.register(PlaylistVideo)

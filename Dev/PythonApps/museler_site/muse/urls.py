from django.conf.urls import url

from . import views

# domain/muse/*
urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^registration/$', views.registration, name='registration'),
        url(r'^(P<user_id>[0-9]+)/home/$', views.user_home, name='u_home'),
        url(r'^(P<user_id>[0-9]+)/yt/videos$', views.user_yt_vids, name='u_yt_vids'),
        url(r'^(P<user_id>[0-9]+)/yt/channels$', views.user_yt_channels, name='u_yt_chans'),
        url(r'^(P<user_id>[0-9]+)/yt/playlists$', views.user_yt_playlists, name='u_yt_pl'),
        url(r'^(P<user_id>[0-9]+)/yt/playlist_videos$', views.user_playlist_videos, name='u_yt_pl_vids'), 
        ]


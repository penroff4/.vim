from django.shortcuts import render
from django.http import HttpResponse

from .models import Video, Channel, Playlist, PlaylistVideo

def index(request):
    """Home page for muse"""
    return render(request, 'muse/index.html')

def registration(request):
    """Page for user to register account"""
    return render(request, 'muse/registration.html')

def user_home(request):
    """A page for users to manage their muse"""
    if request.user.is_authenticated:
        current_user_id = request.id
    return render(request, 'muse/user_pages/user_home.html',
            {'current_user_id': current_user_id})

def user_yt_vids(request):
    """A view for all of a user's videos"""
    videos = Video.objects.order_by('video_name') 
    context = {'videos': videos}
    return render(request, 'muse/user_pages/user_yt_vids.html', context)

def user_yt_channels(request):
    """A view for all of a users YT channels"""
    return render(request, 'muse/user_pages/user_yt_channels.html')

def user_yt_playlists(request):
    """A view for all of a users YT playlists"""
    return render(request, 'muse/user_pages/user_yt_playlists.html')

def user_playlist_videos(request):
    """A view for all of a users YT Playlist Videos"""
    return render(request, 'muse/user_pages/user_yt_playlists_vids.html')


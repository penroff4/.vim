from django.db import models
from django.contrib import admin

# Video, User, Playlist, PlaylistVideos, Channel


class Video(models.Model):
    video_id = models.CharField(max_length=255, primary_key=True)
    channel_id = models.CharField(max_length=255)
    video_owner_id = models.CharField(max_length=255)
    video_name = models.CharField(max_length=255)
    video_published_date = models.DateTimeField()
    record_created_date = models.DateTimeField()
    record_last_modified_date = models.DateTimeField()


class GooUser(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)
    user_name = models.CharField(max_length=255)
    user_create_date = models.DateTimeField()
    record_create_date = models.DateTimeField()
    record_last_modified_date = models.DateTimeField()

    class Meta:
        verbose_name = "Google User"


class Playlist(models.Model):
    playlist_id = models.CharField(max_length=255, primary_key=True)
    playlist_channel_id = models.CharField(max_length=255)
    playlist_name = models.CharField(max_length=255)
    playlist_owner_id = models.CharField(max_length=255)
    playlist_create_date = models.DateTimeField()
    record_create_date = models.DateTimeField()
    record_last_modified_date = models.DateTimeField()


class PlaylistVideos(models.Model):
    playlist_video_key = models.CharField(max_length=510, primary_key=True)
    playlist_id = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    has_been_posted = models.IntegerField(default=0)


class Channel(models.Model):
    channel_id = models.CharField(max_length=255, primary_key=True)
    channel_name = models.CharField(max_length=255)
    channel_owner_id = models.CharField(max_length=255)
    channel_create_date = models.DateTimeField()
    record_create_date = models.DateTimeField()
    record_last_modified_date = models.DateTimeField()
